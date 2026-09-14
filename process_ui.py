import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix submitError position: move it to Step 3 so user can see it!
old_step3 = '''        {/* STEP 4: CUSTOMER DETAILS */}
        {state.step === 3 && (
          <div className="space-y-6">'''

new_step3 = '''        {/* STEP 4: CUSTOMER DETAILS */}
        {state.step === 3 && (
          <div className="space-y-6">
            {submitError && (
              <div className="bg-red-50 text-red-800 p-4 sm:p-6 flex items-start gap-4 border border-red-100 rounded-lg">
                <AlertCircle className="w-5 h-5 shrink-0 mt-0.5" />
                <p className="text-sm leading-relaxed">{submitError}</p>
              </div>
            )}'''
content = content.replace(old_step3, new_step3)

# Also remove submitError from step 4 just in case
old_step4_err = '''            {submitError && (
              <div className="bg-red-50 text-red-800 p-6 flex items-start gap-4 border border-red-100 mb-6">
                <AlertCircle className="w-5 h-5 shrink-0 mt-0.5" />
                <p className="text-sm leading-relaxed">{submitError}</p>
              </div>
            )}'''
content = content.replace(old_step4_err, '')

# 2. Fix handleWhatsApp template!
old_wa = '''  *Booking ID:* 
  *TREATMENT:* 
  *Tanggal:* 
  *Waktu:* '''

new_wa = '''  *Booking ID:* 
  *TREATMENT:* 
  *Tanggal:* 
  *Waktu:* '''
content = content.replace(old_wa, new_wa)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
