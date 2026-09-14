import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'Halo Nanata Studio, saya ingin konfirmasi booking dengan detail berikut:\\n\\n\*Booking ID:\* \$\{confirmedBookingCode \|\| \'N/A\'\}\\n\*TREATMENT:\* \\n\*Tanggal:\* \$\{state\.date\}\\n\*Waktu:\* \$\{state\.time\}',
    r'Halo Nanata Studio, saya ingin konfirmasi booking dengan detail berikut:\n\n*Booking ID:* \n*TREATMENT:* \n*Tanggal:* \n*Waktu:* ',
    content
)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
