import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace disabled condition for confirmation button
old_disabled = 'disabled={isSubmitting || !state.termsAccepted}'
new_disabled = 'disabled={isSubmitting || !state.customer.name.trim() || !state.customer.whatsapp.trim()}'

content = content.replace(old_disabled, new_disabled)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
