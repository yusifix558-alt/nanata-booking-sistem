import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    wizard = f.read()

wizard = wizard.replace(
    'pt-6 sm:pt-8 mt-10 sm:mt-12 border-t border-slate-200 flex flex-col-reverse md:flex-row gap-4',
    'pt-6 sm:pt-8 pb-8 px-4 sm:px-8 border-t border-slate-200 flex flex-col-reverse md:flex-row gap-4 mt-6'
)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(wizard)
