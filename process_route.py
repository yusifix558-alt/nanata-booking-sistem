import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('artistS', 'ARTISTS')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'w', encoding='utf-8') as f:
    f.write(content)
