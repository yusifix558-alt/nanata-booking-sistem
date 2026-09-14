import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Make everything sans-serif by removing font-serif and font-editorial
content = content.replace('font-serif', '')
content = content.replace('font-editorial', '')

# Remove animations
content = content.replace('animate-fade-in-up', '')
content = content.replace('animate-in fade-in zoom-in-95 duration-300', '')

# Adjust step headers text size
content = content.replace('text-lg font-bold text-dark', 'text-xl font-bold text-dark tracking-tight')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
