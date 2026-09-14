import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Bio
bio_html = '''<h2 className="font-editorial text-2xl italic text-namata-pink">studio</h2>
        
        <div className="mt-6 flex flex-col items-center gap-2 text-[11px] text-dark/80 tracking-wider font-medium">
          <p>Eyelash, Nail Art, Hair.</p>
          <p className="text-center">Jl. Caman Raya No.11, Bekasi 17412</p>
          <p>Open 10.00 AM - 21.00 PM (Everyday)</p>
        </div>'''

content = content.replace('<h2 className="font-editorial text-2xl italic text-namata-pink">studio</h2>', bio_html)

# Update Instagram Link
content = content.replace(
    '''<a 
          href="#" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-transparent border border-dark text-dark rounded-[2rem] py-4 text-[11px] font-bold uppercase tracking-[0.2em] text-center hover:bg-dark hover:text-paper transition-colors"
        >
          Instagram
        </a>''',
    '''<a 
          href="https://www.instagram.com/nanata.studio" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-transparent border border-dark text-dark rounded-[2rem] py-4 text-[11px] font-bold uppercase tracking-[0.2em] text-center hover:bg-dark hover:text-paper transition-colors"
        >
          Instagram
        </a>'''
)

# Remove Pricelist button
pricelist_html = '''<a 
          href="#" 
          target="_blank" 
          rel="noreferrer" 
          className="w-full bg-transparent border border-dark text-dark rounded-[2rem] py-4 text-[11px] font-bold uppercase tracking-[0.2em] text-center hover:bg-dark hover:text-paper transition-colors"
        >
          Pricelist
        </a>'''

content = content.replace(pricelist_html, '')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
