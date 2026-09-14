import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean Background & Blobs
content = re.sub(r'\{\/\* Colorful Holographic Blobs \*\/}.*?<\/div>\s*<\/div>', '', content, flags=re.DOTALL)
content = content.replace('bg-[#fdfcfb]', 'bg-[#FFF7F9]')

# 2. Fix Logo (crop to circle, remove mix-blend)
content = re.sub(
    r'<div className="relative w-44 h-44 mb-2">\s*<Image src="\/logo.jpg" alt="Nanata Studio Logo" fill className="object-contain mix-blend-multiply" priority \/>\s*<\/div>',
    r'<div className="relative w-32 h-32 mb-6 rounded-full overflow-hidden shadow-sm border-[3px] border-white">\n           <Image src="/logo.jpg" alt="Nanata Studio Logo" fill className="object-cover" priority />\n        </div>',
    content
)

# 3. Update Buttons (Solid feminine colors, rounded-full, better spacing)
content = re.sub(
    r'className="w-full bg-gradient-to-r from-\[#ff7eb3\] to-\[#b473f5\] text-white rounded-2xl py-4 text-xs font-bold uppercase tracking-widest hover:opacity-90 transition-all shadow-lg hover:shadow-xl hover:-translate-y-0.5"',
    r'className="w-full bg-[#E8A0BF] text-white rounded-full py-4 text-xs font-bold uppercase tracking-widest hover:bg-[#d98bb0] transition-colors shadow-md"',
    content
)

content = re.sub(
    r'className="w-full bg-white\/50 backdrop-blur-xl border border-white\/80 text-dark rounded-2xl py-4 text-xs font-bold uppercase tracking-widest text-center hover:bg-white\/90 hover:border-white transition-all shadow-sm hover:shadow-md"',
    r'className="w-full bg-white border border-[#E8A0BF]/20 text-slate-700 rounded-full py-4 text-xs font-bold uppercase tracking-widest text-center hover:border-[#E8A0BF] hover:text-[#E8A0BF] transition-colors shadow-sm"',
    content
)

# 4. Spacing and Typography fixes in page.tsx
content = content.replace('gap-3.5 mt-10', 'gap-4 mt-8') # increase button gap slightly
content = content.replace('text-[10px] opacity-80 mt-1', 'text-xs text-slate-500 mt-2')
content = content.replace('text-[10px] opacity-80', 'text-xs text-slate-500')
content = content.replace('text-dark/70', 'text-slate-600')
content = content.replace('text-dark', 'text-slate-800')
content = content.replace('font-semibold text-dark', 'font-bold text-slate-800 text-sm')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
