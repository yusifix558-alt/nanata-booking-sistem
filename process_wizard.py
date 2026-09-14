import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    wizard = f.read()

# 1. Remove all gradients and replace with solid #E8A0BF
wizard = wizard.replace('bg-gradient-to-r from-[#ff7eb3] to-[#b473f5]', 'bg-[#E8A0BF]')
wizard = wizard.replace('border-[#b473f5]', 'border-[#E8A0BF]')
wizard = wizard.replace('text-[#b473f5]', 'text-[#E8A0BF]')
wizard = wizard.replace('bg-[#b473f5]', 'bg-[#E8A0BF]')

# 2. Fix Treatment Layout (less cramped, cleaner font)
# Current: className="font-sans text-base sm:text-lg font-bold text-slate-800" (Wait, I removed font-serif, so it might just be text-base sm:text-lg font-bold)
wizard = wizard.replace('text-base sm:text-lg font-bold text-slate-800', 'text-sm font-semibold text-slate-800')
# Increase padding and soften borders
wizard = wizard.replace('border p-4 sm:p-6', 'border p-5 sm:p-6 rounded-xl mb-3')
# Change active background from bg-[#E8A0BF]/5 to bg-[#FFF7F9]
wizard = wizard.replace('bg-[#E8A0BF]/5', 'bg-[#FFF7F9]')
wizard = wizard.replace('hover:border-[#E8A0BF]/30', 'hover:border-[#E8A0BF]/40')
wizard = wizard.replace('border-[#E8A0BF]/10', 'border-slate-200')

# 3. Form fields in Data Diri (add rounded corners, softer borders)
wizard = wizard.replace('className="w-full border-b border-[#E8A0BF]/20 py-3 font-sans text-slate-800 focus:border-[#E8A0BF] focus:outline-none bg-transparent"', 'className="w-full border border-slate-200 rounded-lg px-4 py-3 font-sans text-sm text-slate-800 focus:border-[#E8A0BF] focus:ring-1 focus:ring-[#E8A0BF] focus:outline-none bg-white"')
wizard = wizard.replace('className="w-full border-b border-[#E8A0BF]/20 py-3 font-sans text-slate-800 focus:border-[#E8A0BF] focus:outline-none bg-transparent resize-none h-24 text-sm"', 'className="w-full border border-slate-200 rounded-lg px-4 py-3 font-sans text-sm text-slate-800 focus:border-[#E8A0BF] focus:ring-1 focus:ring-[#E8A0BF] focus:outline-none bg-white resize-none h-24"')

# 4. Fix Calendar Buttons and Wrapper
wizard = wizard.replace('h-10 w-full text-sm sm:text-base font-medium flex items-center justify-center transition-all', 'h-10 w-full text-sm font-medium flex items-center justify-center transition-all rounded-full')
wizard = wizard.replace('shadow-md font-bold', 'shadow-sm font-bold')

# 5. Buttons (Lanjut, Kembali, Confirm)
wizard = wizard.replace('px-6 py-3 sm:px-10 sm:py-4 text-[10px] font-bold tracking-[0.15em] hover:bg-[#FFF7F9] transition-colors flex items-center justify-center uppercase w-full md:w-auto', 'px-6 py-3 sm:px-10 sm:py-4 text-xs font-bold tracking-[0.1em] hover:bg-slate-50 rounded-full transition-colors flex items-center justify-center uppercase w-full md:w-auto')
wizard = wizard.replace('px-6 py-3 sm:px-10 sm:py-4 text-[10px] font-bold tracking-[0.15em] hover:bg-[#E8A0BF]/90 disabled:bg-[#E8A0BF]/20 disabled:text-slate-800/50 transition-colors flex items-center w-full md:w-auto justify-center uppercase', 'px-6 py-3 sm:px-10 sm:py-4 text-xs font-bold tracking-[0.1em] rounded-full hover:opacity-90 disabled:opacity-50 transition-opacity flex items-center w-full md:w-auto justify-center uppercase')
wizard = wizard.replace('px-6 py-3 sm:px-10 sm:py-4 text-[10px] font-bold tracking-[0.15em] hover:bg-paper disabled:bg-[#E8A0BF]/10 disabled:text-slate-800/40 transition-colors w-full md:w-auto flex items-center justify-center uppercase', 'px-6 py-3 sm:px-10 sm:py-4 text-xs font-bold tracking-[0.1em] rounded-full hover:opacity-90 disabled:opacity-50 transition-opacity w-full md:w-auto flex items-center justify-center uppercase')

# 6. Overall Wizard Container Padding (less cramped)
wizard = wizard.replace('bg-white py-4 sm:py-6 md:py-10 min-h-[300px]', 'bg-white py-6 sm:py-8 md:py-10 px-2 sm:px-4 min-h-[300px]')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(wizard)
