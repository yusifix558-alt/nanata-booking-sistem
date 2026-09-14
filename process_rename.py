import os

directory = r'c:\Users\Windows\Videos\NAIL ART WEBSITE'

files_to_check = [
    os.path.join(directory, 'tailwind.config.ts'),
    os.path.join(directory, 'src', 'app', 'layout.tsx'),
    os.path.join(directory, 'src', 'app', 'page.tsx'),
    os.path.join(directory, 'src', 'components', 'Header.tsx'),
    os.path.join(directory, 'src', 'components', 'Footer.tsx'),
    os.path.join(directory, 'src', 'components', 'booking', 'BookingWizard.tsx'),
    os.path.join(directory, 'src', 'app', 'api', 'booking', 'route.ts'),
]

for filepath in files_to_check:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace variations
        content = content.replace('Namata', 'Nanata')
        content = content.replace('namata', 'nanata')
        content = content.replace('NAMATA', 'NANATA')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
