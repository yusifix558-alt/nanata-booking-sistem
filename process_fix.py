import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    wizard = f.read()

wizard = wizard.replace(
    "isSelected ? 'bg-gradient-to-r from-[#ff7eb3] to-[#b473f5] text-slate-800 shadow-md font-bold' :",
    "isSelected ? 'bg-gradient-to-r from-[#ff7eb3] to-[#b473f5] text-white shadow-md font-bold' :"
)

wizard = wizard.replace(
    'className="bg-gradient-to-r from-[#ff7eb3] to-[#b473f5] text-slate-800 px-6',
    'className="bg-gradient-to-r from-[#ff7eb3] to-[#b473f5] text-white px-6'
)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(wizard)
