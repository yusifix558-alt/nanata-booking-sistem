import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\lib\availability.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace OPENING_HOURS
old_hours = '''const OPENING_HOURS = {
  // 1 = Monday, 7 = Sunday
  1: { start: 12, end: 21 },
  2: { start: 12, end: 21 },
  3: { start: 12, end: 21 },
  4: { start: 12, end: 21 },
  5: { start: 13, end: 21 }, // Friday
  6: { start: 12, end: 21 },
  7: { start: 12, end: 21 },
};'''

new_hours = '''const OPENING_HOURS = {
  // 1 = Monday, 7 = Sunday
  1: { start: 10, end: 22 },
  2: { start: 10, end: 22 },
  3: { start: 10, end: 22 },
  4: { start: 10, end: 22 },
  5: { start: 10, end: 22 },
  6: { start: 10, end: 22 },
  7: { start: 10, end: 22 },
};'''

content = content.replace(old_hours, new_hours)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\lib\availability.ts', 'w', encoding='utf-8') as f:
    f.write(content)
