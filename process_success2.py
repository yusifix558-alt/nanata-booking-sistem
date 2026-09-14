import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the actual success screen
content = content.replace('{artist?.priceLabel}', '{service?.priceLabel}')

old_artist_success = '''            <div className="flex justify-between">
              <span className="text-black text-sm font-medium tracking-widest">artist</span>
              <span className="text-black font-medium">{artist?.name || state.artistId}</span>
            </div>'''
content = content.replace(old_artist_success, '')

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\components\booking\BookingWizard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
