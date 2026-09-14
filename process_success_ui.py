import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Artist row from success UI
old_artist_row = '''              <div className="flex justify-between items-center">
                <span className="text-black text-[10px] font-bold tracking-[0.2em] uppercase">artist</span>
                <span className="text-black font-medium text-sm">{ARTISTS.find(b => b.id === state.artistId)?.name}</span>
              </div>'''
content = content.replace(old_artist_row, '')

# 2. Fix TOTAL price in success UI to use service.priceLabel
old_total = '''              <div className="flex justify-between items-center pt-4 border-t border-slate-200">
                <span className="text-black text-[10px] font-bold tracking-[0.2em] uppercase">TOTAL</span>
                <span className="text-black font-bold text-sm">{ARTISTS.find(b => b.id === state.artistId)?.priceLabel}</span>
              </div>'''
new_total = '''              <div className="flex justify-between items-center pt-4 border-t border-slate-200">
                <span className="text-black text-[10px] font-bold tracking-[0.2em] uppercase">TOTAL</span>
                <span className="text-black font-bold text-sm">{service?.priceLabel}</span>
              </div>'''
content = content.replace(old_total, new_total)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
