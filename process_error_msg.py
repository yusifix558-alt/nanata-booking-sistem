import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "error: 'Booking belum berhasil dibuat. Silakan coba lagi.'",
    "error: Booking belum berhasil dibuat. (Error: )"
)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'w', encoding='utf-8') as f:
    f.write(content)
