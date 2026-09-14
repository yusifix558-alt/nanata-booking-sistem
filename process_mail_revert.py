import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of the email block
start_idx = content.find('// 6. Owner Notification (Gmail using Nodemailer)')
if start_idx == -1:
    print("Could not find start block")

# Find the return NextResponse.json
end_idx = content.find('return NextResponse.json', start_idx)

if start_idx != -1 and end_idx != -1:
    replacement = """// 6. Owner Notification (Email using Resend)
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
                  <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>Waktu</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;">${data.date} pkl ${data.time}</td></tr>
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
      } catch (err) {
        console.error(`[NOTIFICATION_RESULT] Failed to send email via Resend:`, err);
      }
    }

    """
    
    new_content = content[:start_idx] + replacement + content[end_idx:]
    with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Reverted to Resend successfully")
