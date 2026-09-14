import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    wizard = f.read()

# Fix bottom navigation wrapper
wizard = wizard.replace(
    "className={mt-4 sm:mt-8 flex flex-col-reverse md:flex-row gap-3 md:gap-4 }",
    "className={pt-8 mt-12 border-t border-slate-200 flex flex-col-reverse md:flex-row gap-4 }"
)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(wizard)
