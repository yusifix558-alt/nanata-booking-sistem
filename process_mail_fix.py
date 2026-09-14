import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything from // 6. Owner Notification (Email) to the end of that block.
# We'll use regex to match the block.
pattern = r"// 6\. Owner Notification \(Email\).*?return NextResponse\.json"
replacement = """// 6. Owner Notification (Gmail using Nodemailer)
    if (process.env.GMAIL_EMAIL && process.env.GMAIL_APP_PASSWORD) {
      try {
        const nodemailer = require('nodemailer');
        const transporter = nodemailer.createTransport({
          service: 'gmail',
          auth: {
            user: process.env.GMAIL_EMAIL,
            pass: process.env.GMAIL_APP_PASSWORD
          }
        });

        const ownerEmail = process.env.OWNER_EMAIL || process.env.GMAIL_EMAIL;
        
        await transporter.sendMail({
          from: `"Nanata Studio Booking" <${process.env.GMAIL_EMAIL}>`,
          to: ownerEmail,
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
        });
        console.log(`[NOTIFICATION_RESULT] Gmail sent to Owner (${ownerEmail}). Booking Code: ${bookingCode}`);
      } catch (err) {
        console.error(`[NOTIFICATION_RESULT] Failed to send Gmail:`, err);
      }
    } else {
      console.log(`[NOTIFICATION_RESULT] BLOCKED - GMAIL_EMAIL or GMAIL_APP_PASSWORD missing.`);
    }

    return NextResponse.json"""

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'w', encoding='utf-8') as f:
    f.write(content)
