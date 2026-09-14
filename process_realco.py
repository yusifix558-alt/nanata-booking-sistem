import re

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Case insensitive replacement, but preserve case formatting where possible?
    # Actually, we can just replace specific strings.
    # We found:
    # 1. "Halo REAL.CO, saya ingin" -> "Halo Nanata Studio, saya ingin"
    # 2. "REAL.CO — ${service.name}" -> "Nanata Studio — ${service.name}"
    # 3. "Sampai jumpa di REAL.CO!" -> "Sampai jumpa di Nanata Studio!"
    # 4. "tim REAL.CO melalui WhatsApp" -> "tim Nanata Studio melalui WhatsApp"
    
    content = content.replace("REAL.CO", "Nanata Studio")
    content = content.replace("real.co", "Nanata Studio")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_in_file(r"c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\FloatingWhatsApp.tsx")
replace_in_file(r"c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx")
