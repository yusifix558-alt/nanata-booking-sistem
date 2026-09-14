import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove FadeIn import
content = re.sub(r'import FadeIn from "@/components/FadeIn";\n', '', content)

# 2. Remove FadeIn tags but keep children
# Since FadeIn had no custom props in this file, we can just replace <FadeIn> and </FadeIn>
content = re.sub(r'<FadeIn[^>]*>', '', content)
content = content.replace('</FadeIn>', '')

# 3. Remove animations
content = content.replace('animate-in fade-in zoom-in-95 duration-300', '')
content = content.replace('animate-in fade-in duration-500', '')

# 4. Replace Brand section with Logo image
brand_regex = re.compile(r'\{\/\* Top \/ Brand \*\/\}.*?\{\/\* BIO SECTION \*\/\}', re.DOTALL)

new_brand = '''{/* Top / Brand */}
      <div className="flex flex-col items-center mt-6 text-center">
        <div className="relative w-40 h-40 md:w-48 md:h-48 mb-4">
           <Image src="/logo.jpg" alt="Nanata Studio Logo" fill className="object-contain" priority />
        </div>
        
        {/* BIO SECTION */}'''

content = brand_regex.sub(new_brand, content)

# 5. Clean up typography - make buttons use font-sans, text-xs
# The fonts are already Jost (sans), let's ensure consistency
content = content.replace('font-editorial text-4xl', 'text-2xl') # in booking wizard header
content = content.replace('font-editorial text-5xl', 'text-3xl') # unused now due to brand removal
content = content.replace('italic text-nanata-pink', 'text-nanata-pink font-semibold')
content = content.replace('text-[11px] font-bold uppercase tracking-[0.2em]', 'text-xs font-semibold uppercase tracking-widest')
content = content.replace('text-[10px] uppercase tracking-widest flex items-center gap-2', 'text-xs uppercase tracking-widest font-semibold flex items-center gap-2')
content = content.replace('text-[9px] text-dark/40 uppercase tracking-widest', 'text-[10px] text-dark/40 uppercase tracking-widest')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
