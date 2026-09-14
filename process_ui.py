import re

# UPDATE PAGE.TSX
with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Change the black button to a vibrant gradient
old_btn = 'className="w-full bg-dark text-white rounded-2xl py-4 text-xs font-bold uppercase tracking-widest hover:bg-white hover:text-dark transition-all shadow-xl hover:shadow-2xl hover:-translate-y-0.5"'
new_btn = 'className="w-full bg-gradient-to-r from-[#ff7eb3] to-[#b473f5] text-white rounded-2xl py-4 text-xs font-bold uppercase tracking-widest hover:opacity-90 transition-all shadow-lg hover:shadow-xl hover:-translate-y-0.5"'
content = content.replace(old_btn, new_btn)

# Soften the text colors from strict dark to a deep purple/slate
content = content.replace('text-dark', 'text-slate-800')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

# UPDATE BOOKINGWIZARD.TSX
with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    wizard = f.read()

# Soften text-dark to text-slate-800 globally for text
wizard = wizard.replace('text-dark', 'text-slate-800')

# Replace bg-dark for primary buttons/active states with a colorful gradient or solid colorful
wizard = wizard.replace('bg-dark text-paper', 'bg-gradient-to-r from-[#ff7eb3] to-[#b473f5] text-white')
wizard = wizard.replace('bg-dark text-white', 'bg-gradient-to-r from-[#ff7eb3] to-[#b473f5] text-white')

# Replace border-dark for active states
wizard = wizard.replace('border-dark', 'border-[#b473f5]')

# Special replace for the small radio button active dots which were 'bg-dark'
wizard = wizard.replace('bg-dark', 'bg-[#b473f5]')

# Replace background of the entire wizard if it was pure white? It's fine as white, but buttons pop now.
# Replace nanata-pink (which is a very light pastel) to the new vibrant gradient if used in buttons
wizard = wizard.replace('bg-nanata-pink', 'bg-gradient-to-r from-[#ff7eb3] to-[#b473f5]')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(wizard)
