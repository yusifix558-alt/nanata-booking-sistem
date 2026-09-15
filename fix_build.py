import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the undefined 'service' reference with the proper SERVICES lookup
content = content.replace('{service?.priceLabel}', '{SERVICES.find(s => s.id === state.serviceId)?.priceLabel}')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
