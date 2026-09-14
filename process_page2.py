import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_brand = '''{/* Top / Brand */}
      <div className="flex flex-col items-center mt-8 md:mt-16 text-center">
        {/* Optional Logo Circle */}
        <div className="w-24 h-24 rounded-full bg-nanata-pink/20 border border-dark flex items-center justify-center mb-6 overflow-hidden relative">
           {/* You can replace this with an actual logo image */}
           <span className="text-2xl text-nanata-pink font-semibold leading-none pt-2">N</span>
        </div>
        <h1 className="text-3xl font-bold tracking-tight mb-1">nanata</h1>
        <h2 className="font-editorial text-2xl text-nanata-pink font-semibold">studio</h2>'''

new_brand = '''{/* Top / Brand */}
      <div className="flex flex-col items-center mt-8 md:mt-16 text-center">
        <div className="relative w-36 h-36 md:w-48 md:h-48 mb-2">
           <Image src="/logo.jpg" alt="Nanata Studio Logo" fill className="object-contain" priority />
        </div>'''

content = content.replace(old_brand, new_brand)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
