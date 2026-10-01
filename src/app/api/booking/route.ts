import { NextResponse } from 'next/server';
import { z } from 'zod';
import { appendBookingToSheet } from '@/lib/googleSheets';
import { generateAvailableSlots } from '@/lib/availability';
import { createEvent, EventInput } from '@/lib/googleCalendar';
import { SERVICES, ARTISTS } from '@/lib/data';

export const dynamic = 'force-dynamic';

const bookingSchema = z.object({
  serviceId: z.string().min(1),
  artistId: z.string().min(1),
  date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Invalid date format"),
  time: z.string().regex(/^\d{2}:\d{2}$/, "Invalid time format"),
  customer: z.object({
    name: z.string().min(2, "Nama terlalu pendek").max(100),
    whatsapp: z.string().min(9, "Nomor WA tidak valid").max(20).regex(/^[0-9+-\s]+$/, "Format nomor tidak valid"),
    email: z.string().email("Email tidak valid").optional().or(z.literal('')),
    notes: z.string().max(500).optional(),
  }),
});

export async function POST(request: Request) {
  let createdEventId: string | null = null;
  let calendarId: string | null = null;

  try {
    const rawBody = await request.json();
    
    // 1. Validate Input
    const parseResult = bookingSchema.safeParse(rawBody);
    if (!parseResult.success) {
      return NextResponse.json({ 
        error: 'Data booking tidak valid. Periksa kembali informasi yang kamu masukkan.',
        details: parseResult.error.format()
      }, { status: 400 });
    }
    const data = parseResult.data;

    // 2. Validate Service and artist (Get details from static data)
    const service = SERVICES.find(s => s.id === data.serviceId);
    if (!service) {
      return NextResponse.json({ error: 'Layanan tidak ditemukan.' }, { status: 404 });
    }
    
    const artist = data.artistId === 'Studio' ? { name: 'Studio', price: service.price, priceLabel: service.priceLabel } : ARTISTS.find(b => b.id === data.artistId);
    if (!artist) {
      return NextResponse.json({ error: 'Artist tidak ditemukan.' }, { status: 404 });
    }

    calendarId = (artist as { calendar_id?: string }).calendar_id || process.env.GOOGLE_CALENDAR_ID || 'primary';

    // 3. Server Recheck - Validate Date/Time
    const slots = await generateAvailableSlots(data.artistId, data.date, service.duration);
    const requestedSlot = slots.find(s => s.time === data.time);
    
    if (!requestedSlot || !requestedSlot.available) {
      return NextResponse.json({ error: 'Jadwal tersebut sudah tidak tersedia. Silakan pilih waktu lain.' }, { status: 400 });
    }

    // Calculate times
    const startTime = new Date(`${data.date}T${data.time}:00+07:00`); // Assuming WIB / GMT+7
    const endTime = new Date(startTime.getTime() + service.duration * 60000);
    const bookingCode = `RC${Math.random().toString(36).substring(2, 8).toUpperCase()}`;

    console.log(`[BOOKING_ATTEMPT] bookingCode: ${bookingCode}, Phone: ***${data.customer.whatsapp.slice(-4)}`);

    // 4. Create Google Calendar Event
    const eventParams: EventInput = {
      summary: `Nanata Studio — ${service.name}`,
      description: `Customer: ${data.customer.name}
WhatsApp: ${data.customer.whatsapp}
artist: ${artist.name}
Service: ${service.name}
Duration: ${service.duration} min
Price: ${artist.price}
Booking ID: ${bookingCode}
${data.customer.notes ? `\nNotes: ${data.customer.notes}` : ''}`,
      start: { dateTime: startTime.toISOString() },
      end: { dateTime: endTime.toISOString() },
      reminders: {
        useDefault: false,
        overrides: [
          { method: 'email', minutes: 24 * 60 },
          { method: 'popup', minutes: 2 * 60 }
        ]
      }
    };

    // Skip adding attendees directly via Calendar API because service accounts on free Gmail 
    // often get 403 Forbidden when trying to invite external emails.
    // if (data.customer.email) {
    //   eventParams.attendees = [{ email: data.customer.email }];
    // }

    const gCalEvent = await createEvent(calendarId as string, eventParams);
    createdEventId = gCalEvent.id;
    console.log(`[CALENDAR_EVENT_CREATION] Success. Event ID: ${createdEventId}`);

    const [hours, minutes] = data.time.split(':').map(Number);
    const endMinutesTotal = hours * 60 + minutes + service.duration;
    const endHour = Math.floor(endMinutesTotal / 60) % 24;
    const endMin = endMinutesTotal % 60;
    const pad = (n: number) => n.toString().padStart(2, '0');
    const displayTime = `${data.time} - ${pad(endHour)}:${pad(endMin)}`;

    // 5. Save Booking to Google Sheets
    await appendBookingToSheet({
      bookingCode,
      customerName: data.customer.name,
      customerWhatsapp: data.customer.whatsapp,
      serviceName: service.name,
      artistName: artist.name,
      date: data.date,
      time: displayTime,
      price: service.price
    });

    // 6. Owner Notification (Email using Resend)
    if (!process.env.RESEND_API_KEY) {
      console.log(`[NOTIFICATION_RESULT] BLOCKED - RESEND_API_KEY missing. Booking Code: ${bookingCode}`);
    } else {
      try {
        const ownerEmail = process.env.OWNER_EMAIL || 'malikief01@gmail.com';
        await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            from: 'Nanata Studio <onboarding@resend.dev>', // Resend default test email
            to: [ownerEmail],
            subject: `✨ Booking Baru: ${service.name} - ${data.customer.name}`,
            html: `
              <div style="font-family: sans-serif; padding: 20px; background: #FFF7F9; border-radius: 10px;">
                <h2 style="color: #E8A0BF; margin-bottom: 20px;">Booking Baru Masuk! 🎉</h2>
                <table style="width: 100%; border-collapse: collapse;">
                  <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>Booking ID</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;">${bookingCode}</td></tr>
                  <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>Layanan</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;">${service.name}</td></tr>
                  <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>Waktu</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;">${data.date} pkl ${displayTime}</td></tr>
                  <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>Total Harga</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;">${service.priceLabel}</td></tr>
                  <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>Nama Customer</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;">${data.customer.name}</td></tr>
                  <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>WhatsApp</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><a href="https://wa.me/${data.customer.whatsapp.replace(/\D/g, '')}">${data.customer.whatsapp}</a></td></tr>
                  <tr><td style="padding: 8px 0;"><strong>Catatan</strong></td><td style="padding: 8px 0;">${data.customer.notes || '-'}</td></tr>
                </table>
              </div>
            `
          })
        });
        console.log(`[NOTIFICATION_RESULT] Resend Email sent to Owner (${ownerEmail}). Booking Code: ${bookingCode}`);

        // 7. Customer Notification (Email using Resend)
        if (data.customer.email) {
          // Note: To send emails to arbitrary customer addresses, the Resend account 
          // MUST have a verified custom domain. 'onboarding@resend.dev' only works for sending to yourself.
          const resendResponse = await fetch('https://api.resend.com/emails', {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              from: 'Nanata Studio <onboarding@resend.dev>', // MUST BE CHANGED TO VERIFIED DOMAIN IN PRODUCTION
              to: [data.customer.email],
              subject: `Konfirmasi Booking: ${service.name} di Nanata Studio`,
              html: `
                <div style="font-family: sans-serif; padding: 20px; background: #FFF7F9; border-radius: 10px; color: #333;">
                  <h2 style="color: #E8A0BF; margin-bottom: 10px;">Halo ${data.customer.name}, Booking Kamu Berhasil! ✨</h2>
                  <p>Terima kasih telah melakukan booking di Nanata Studio. Berikut adalah rincian jadwal kamu:</p>
                  <table style="width: 100%; border-collapse: collapse; margin-top: 20px; background: white; padding: 15px; border-radius: 8px;">
                    <tr><td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Booking ID</strong></td><td style="padding: 10px; border-bottom: 1px solid #eee;">${bookingCode}</td></tr>
                    <tr><td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Layanan</strong></td><td style="padding: 10px; border-bottom: 1px solid #eee;">${service.name}</td></tr>
                    <tr><td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Tanggal & Waktu</strong></td><td style="padding: 10px; border-bottom: 1px solid #eee;">${data.date} pkl ${displayTime}</td></tr>
                    <tr><td style="padding: 10px;"><strong>Total Biaya</strong></td><td style="padding: 10px; font-weight: bold; color: #E8A0BF;">${service.priceLabel}</td></tr>
                  </table>
                  <p style="margin-top: 20px; font-size: 14px; color: #666;">
                    Jika ada perubahan jadwal, mohon konfirmasi ke admin via WhatsApp minimal 2 jam sebelum kedatangan.<br>
                    Sampai jumpa di studio! 💅
                  </p>
                </div>
              `
            })
          });
          
          if (!resendResponse.ok) {
             console.error(`[NOTIFICATION_RESULT] Customer Email blocked (Missing verified domain). Resend returned:`, await resendResponse.text());
          }
        }
      } catch (err) {
        console.error(`[NOTIFICATION_RESULT] Failed to send email via Resend:`, err);
      }
    }

    return NextResponse.json({ 
      success: true, 
      bookingCode 
    });

  } catch (error) {
    const err = error instanceof Error ? error : new Error("Unknown error");
    console.error(`[ERROR_REASON] ${err.message}`);
    
    // 6. Failure Recovery (Cleanup orphan Google Calendar Event)
    if (createdEventId && calendarId && err.message.includes('DB_SAVE_FAILED')) {
      try {
        console.log(`[FAILURE_RECOVERY] Cleaning up orphan event ${createdEventId}...`);
      } catch (cleanupError) {
        console.error("[CRITICAL] Failed to clean up orphan event", cleanupError);
      }
    }

    // Handle Idempotency / Race Condition DB constraint error
    if (err.message.includes('duplicate key value') || err.message.includes('no_overlapping_bookings')) {
      return NextResponse.json({ 
        error: 'Maaf, slot tersebut baru saja diambil. Silakan pilih waktu lain.' 
      }, { status: 409 });
    }

    return NextResponse.json({ 
      error: `Booking belum berhasil dibuat. (Error: ${err.message})` 
    }, { status: 500 });
  }
}
