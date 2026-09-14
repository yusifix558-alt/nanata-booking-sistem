import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the WhatsApp text template
wrong_text = "const text = Halo Nanata Studio, saya ingin konfirmasi booking dengan detail berikut:\\n\\n*Booking ID:* \\n*TREATMENT:* \\n*Tanggal:* \\n*Waktu:* ;"
correct_text = "const text = Halo Nanata Studio, saya ingin konfirmasi booking dengan detail berikut:\\n\\n*Booking ID:* \\n*TREATMENT:* \\n*Tanggal:* \\n*Waktu:* ;"

content = content.replace(wrong_text, correct_text)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
