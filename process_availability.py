import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\lib\availability.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace BARBERS with ARTISTS
content = content.replace("import { BARBERS } from './data';", "import { ARTISTS } from './data';")
content = content.replace("const barber = BARBERS.find(b => b.id === barberId);", "const artist = ARTISTS.find(a => a.id === barberId);")
content = content.replace("const calendarId = (barber as { calendarId?: string })?.calendarId", "const calendarId = (artist as { calendarId?: string })?.calendarId")

# Just to be safe, replace all other 'barber' references if any (barberId is fine since it's just the param name, but artist is better)
content = content.replace("barberId", "artistId")

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\lib\availability.ts', 'w', encoding='utf-8') as f:
    f.write(content)
