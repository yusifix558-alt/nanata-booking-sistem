import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'r', encoding='utf-8') as f:
    page = f.read()

# Remove 'Pilih artist & jadwal'
page = re.sub(r'<p className="text-\[10px\] uppercase tracking-widest.*?">Pilih artist & jadwal<\/p>', '', page)

# Make all text solid black instead of gray/slate
page = re.sub(r'text-slate-\d+(/\d+)?', 'text-black', page)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(page)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    wizard = f.read()

# Make all text solid black instead of gray/slate
wizard = re.sub(r'text-slate-\d+(/\d+)?', 'text-black', wizard)

# Fix step indicator spacing (make it much more spacious)
wizard = wizard.replace('className="mb-6 sm:mb-12"', 'className="mb-10 sm:mb-16 mt-6"')
wizard = wizard.replace('mb-3 sm:mb-4 px-2 sm:px-0', 'mb-8 px-4 sm:px-8')

# Remove the weird stepNumber !== 5 logic since it's only 3 steps now
wizard = wizard.replace("stepNumber !== 5", "stepNumber !== 3")

# Fix bottom navigation buttons spacing
wizard = wizard.replace(
    'className="flex justify-between pt-4 border-t border-slate-200"',
    'className="flex flex-col-reverse md:flex-row justify-between pt-8 mt-12 border-t border-slate-200 gap-4"'
)

# The "KEMBALI" button had border-[#E8A0BF]/20, let's make it a bit more visible if needed, but text is black now
# Let's check text-black in the KEMBALI button
wizard = wizard.replace('text-black px-6 py-3', 'text-black px-6 py-3')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(wizard)
