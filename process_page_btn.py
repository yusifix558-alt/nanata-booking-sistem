import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace secondary buttons
content = re.sub(
    r'className="w-full bg-white\/50 backdrop-blur-xl border border-white\/80 text-slate-800 rounded-2xl py-4 text-xs font-bold uppercase tracking-widest text-center hover:bg-white\/90 hover:border-white transition-all shadow-sm hover:shadow-md"',
    r'className="w-full bg-white border border-[#E8A0BF]/20 text-slate-700 rounded-full py-4 text-xs font-bold uppercase tracking-widest text-center hover:border-[#E8A0BF] hover:text-[#E8A0BF] transition-colors shadow-sm"',
    content
)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
