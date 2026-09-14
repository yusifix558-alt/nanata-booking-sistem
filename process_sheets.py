import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\lib\googleSheets.ts', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('barberName', 'artistName')
content = content.replace('// Capster', '// Artist')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\lib\googleSheets.ts', 'w', encoding='utf-8') as f:
    f.write(content)
