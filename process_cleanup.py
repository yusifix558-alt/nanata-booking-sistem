import re

# UPDATE PAGE.TSX
with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'r', encoding='utf-8') as f:
    page_content = f.read()

page_content = page_content.replace('className="bg-white border border-dark"', 'className="bg-white w-full"')
page_content = page_content.replace('href="https://wa.me/62881036695165"', 'href="https://wa.me/6285283120151"')
page_content = page_content.replace(
    'href="#" \n          target="_blank" \n          rel="noreferrer" \n          className="w-full bg-transparent border border-dark text-dark rounded-[2rem] py-4 text-xs font-semibold uppercase tracking-widest text-center hover:bg-dark hover:text-paper transition-colors"\n        >\n          Google Maps',
    'href="https://maps.app.goo.gl/iuF843vMhZYGH1YG9" \n          target="_blank" \n          rel="noreferrer" \n          className="w-full bg-transparent border border-dark text-dark rounded-[2rem] py-4 text-xs font-semibold uppercase tracking-widest text-center hover:bg-dark hover:text-paper transition-colors"\n        >\n          Google Maps'
)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(page_content)

# UPDATE BOOKINGWIZARD.TSX
with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    wizard_content = f.read()

# WhatsApp number
wizard_content = wizard_content.replace('https://wa.me/62881036695165', 'https://wa.me/6285283120151')

# Remove borders
wizard_content = wizard_content.replace('className="bg-white p-4 sm:p-6 md:p-10 shadow-sm border border-dark/5 min-h-[300px] sm:min-h-[400px]"', 'className="bg-white py-4 sm:py-6 md:py-10 min-h-[300px] sm:min-h-[400px]"')
wizard_content = wizard_content.replace('className="border border-dark/10 bg-transparent p-4 sm:p-6 shadow-sm"', 'className="bg-transparent py-4 sm:py-6"')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(wizard_content)
