import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the background blobs
old_blobs = '''{/* Decorative Background Blobs */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
        <div className="absolute top-[-5%] left-[-10%] w-[80%] h-[40%] rounded-full bg-nanata-pink/20 blur-3xl opacity-60"></div>
        <div className="absolute bottom-[-5%] right-[-10%] w-[80%] h-[40%] rounded-full bg-teal-100/40 blur-3xl opacity-60"></div>
      </div>'''

new_blobs = '''{/* Colorful Holographic Blobs */}
      <div className="absolute inset-0 overflow-hidden -z-10 pointer-events-none bg-[#fdfcfb]">
        <div className="absolute -top-[10%] -left-[10%] w-[70%] h-[60%] rounded-full bg-[#ffadd2] blur-[80px] opacity-90 mix-blend-multiply"></div>
        <div className="absolute top-[15%] -right-[15%] w-[80%] h-[70%] rounded-full bg-[#8cecf5] blur-[80px] opacity-90 mix-blend-multiply"></div>
        <div className="absolute -bottom-[10%] left-[5%] w-[70%] h-[60%] rounded-full bg-[#d6b4fc] blur-[80px] opacity-90 mix-blend-multiply"></div>
        <div className="absolute bottom-[20%] right-[10%] w-[50%] h-[50%] rounded-full bg-[#ffdf8c] blur-[80px] opacity-70 mix-blend-multiply"></div>
      </div>'''

content = content.replace(old_blobs, new_blobs)

# Update buttons to look better on a highly colorful background
old_booking_btn = '''className="w-full bg-dark text-paper rounded-2xl py-4 text-xs font-bold uppercase tracking-widest hover:bg-nanata-pink hover:text-dark transition-all shadow-lg hover:shadow-xl hover:-translate-y-0.5"'''
new_booking_btn = '''className="w-full bg-dark text-white rounded-2xl py-4 text-xs font-bold uppercase tracking-widest hover:bg-white hover:text-dark transition-all shadow-xl hover:shadow-2xl hover:-translate-y-0.5"'''
content = content.replace(old_booking_btn, new_booking_btn)

# Update secondary buttons to be more glassy and prominent
old_sec_btn = '''className="w-full bg-white/70 backdrop-blur-md border border-dark/10 text-dark rounded-2xl py-4 text-xs font-semibold uppercase tracking-widest text-center hover:bg-white hover:border-dark/30 transition-all shadow-sm hover:shadow-md"'''
new_sec_btn = '''className="w-full bg-white/50 backdrop-blur-xl border border-white/80 text-dark rounded-2xl py-4 text-xs font-bold uppercase tracking-widest text-center hover:bg-white/90 hover:border-white transition-all shadow-sm hover:shadow-md"'''
content = content.replace(old_sec_btn, new_sec_btn)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
