import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    wizard = f.read()

wizard = re.sub(
    r'className={pt-6 sm:pt-8 mt-10 sm:mt-12 border-t border-slate-200 flex flex-col-reverse md:flex-row gap-4\s*\$\{state\.step > 1 \? \'justify-between\' : \'justify-end\'\}}',
    r'className={pt-6 sm:pt-8 mt-6 sm:mt-8 pb-8 px-4 sm:px-8 border-t border-slate-200 flex flex-col-reverse md:flex-row gap-4 }',
    wizard
)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(wizard)
