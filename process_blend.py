import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('className="object-contain" priority />', 'className="object-contain mix-blend-multiply" priority />')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
