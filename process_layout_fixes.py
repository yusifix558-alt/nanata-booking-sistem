import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    wizard = f.read()

# 1. Fix Top Header Spacing (make it less detached)
wizard = wizard.replace('className="mb-10 sm:mb-16 mt-6"', 'className="mb-6 mt-6"')
wizard = wizard.replace('className="flex items-center justify-between text-[10px] sm:text-xs font-medium tracking-widest mb-8 px-4 sm:px-8"', 'className="flex items-center justify-between text-[10px] sm:text-xs font-medium tracking-widest mb-6 px-4 sm:px-8"')

# 2. Fix Footer Spacing (add bottom padding so it doesn't touch the very bottom edge of the modal)
wizard = wizard.replace(
    "className={pt-6 sm:pt-8 mt-10 sm:mt-12 border-t border-slate-200 flex flex-col-reverse md:flex-row gap-4 }",
    "className={pt-6 sm:pt-8 mt-6 sm:mt-8 pb-8 px-4 sm:px-8 border-t border-slate-200 flex flex-col-reverse md:flex-row gap-4 }"
)

# 3. Double check "Pilih TREATMENT yang..." has black text (it does, I replaced it)
# Make sure the font-bold of step title is good.
wizard = wizard.replace('text-center text-xs sm:text-sm font-bold tracking-widest text-black', 'text-center text-sm sm:text-base font-bold tracking-widest text-black')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(wizard)
