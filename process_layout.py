import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\layout.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('import FloatingWhatsApp from "@/components/FloatingWhatsApp";', '')
content = content.replace('<FloatingWhatsApp />', '')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\layout.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
