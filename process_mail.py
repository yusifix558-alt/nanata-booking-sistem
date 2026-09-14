import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Resend logic with Nodemailer logic
old_mail_logic = '''    // 6. Owner Notification (Email)
    if (!process.env.RESEND_API_KEY) {
      console.log([NOTIFICATION_RESULT] BLOCKED - NEEDS CONFIGURATION. Booking Code: );
    } else {
      try {
        const ownerEmail = process.env.OWNER_EMAIL || 'hallidbaabdillah@gmail.com';
        await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Authorization': Bearer ,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            from: 'Acme <onboarding@resend.dev>', // Resend test email
            to: [ownerEmail],
            subject: New Booking:  - ,
            html: 
              <h2>Booking Baru Masuk!</h2>
              <p><strong>Booking ID:</strong> </p>
              <p><strong>Layanan:</strong> </p>
              <p><strong>artist:</strong> </p>
              <p><strong>Waktu:</strong>  </p>
              <br/>
              <p><strong>Customer:</strong> </p>
              <p><strong>WA:</strong> </p>
            
          })
        });
        console.log([NOTIFICATION_RESULT] Email sent to Owner (). Booking Code: );
      } catch (err) {
        console.error([NOTIFICATION_RESULT] Failed to send email:, err);
      }
    }'''

new_mail_logic = '''    // 6. Owner Notification (Gmail using Nodemailer)
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
          from: "Nanata Studio Booking" <>,
          to: ownerEmail,
          subject: âœ¨ Booking Baru:  - ,
          html: 
            <div style="font-family: sans-serif; padding: 20px; background: #FFF7F9; border-radius: 10px;">
              <h2 style="color: #E8A0BF; margin-bottom: 20px;">Booking Baru Masuk! ðŸŽ‰</h2>
              <table style="width: 100%; border-collapse: collapse;">
                <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>Booking ID</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"></td></tr>
                <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>Layanan</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"></td></tr>
                <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>Waktu</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"> pkl </td></tr>
                <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>Total Harga</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"></td></tr>
                <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>Nama Customer</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"></td></tr>
                <tr><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><strong>WhatsApp</strong></td><td style="padding: 8px 0; border-bottom: 1px solid #ddd;"><a href="https://wa.me/"></a></td></tr>
                <tr><td style="padding: 8px 0;"><strong>Catatan</strong></td><td style="padding: 8px 0;"></td></tr>
              </table>
            </div>
          
        });
        console.log([NOTIFICATION_RESULT] Gmail sent to Owner (). Booking Code: );
      } catch (err) {
        console.error([NOTIFICATION_RESULT] Failed to send Gmail:, err);
      }
    } else {
      console.log([NOTIFICATION_RESULT] BLOCKED - GMAIL_EMAIL or GMAIL_APP_PASSWORD missing.);
    }'''

content = content.replace(old_mail_logic, new_mail_logic)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'w', encoding='utf-8') as f:
    f.write(content)
