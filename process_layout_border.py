import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\layout.tsx', 'r', encoding='utf-8') as f:
    layout = f.read()

layout = layout.replace('bg-paper relative shadow-2xl overflow-x-hidden border-x border-dark/10', 'bg-[#FFF7F9] relative shadow-[0_0_40px_rgba(0,0,0,0.05)] overflow-x-hidden')
layout = layout.replace('bg-[#EAEAEA]', 'bg-[#F3E8EB]') # softer background for desktop empty space

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\layout.tsx', 'w', encoding='utf-8') as f:
    f.write(layout)
