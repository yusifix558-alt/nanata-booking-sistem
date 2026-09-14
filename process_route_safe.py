import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'r', encoding='utf-8') as f:
    content = f.read()

old_logic = '''    // 2. Validate Service and artist (Get details from static data)
    const service = SERVICES.find(s => s.id === data.serviceId);
    const artist = data.artistId === 'Studio' ? { name: 'Studio', price: service.price, priceLabel: service.priceLabel } : ARTISTS.find(b => b.id === data.artistId);

    if (!service || !artist) {
      return NextResponse.json({ error: 'Layanan atau artist tidak ditemukan.' }, { status: 404 });
    }'''

new_logic = '''    // 2. Validate Service and artist (Get details from static data)
    const service = SERVICES.find(s => s.id === data.serviceId);
    if (!service) {
      return NextResponse.json({ error: 'Layanan tidak ditemukan.' }, { status: 404 });
    }
    
    const artist = data.artistId === 'Studio' ? { name: 'Studio', price: service.price, priceLabel: service.priceLabel } : ARTISTS.find(b => b.id === data.artistId);
    if (!artist) {
      return NextResponse.json({ error: 'Artist tidak ditemukan.' }, { status: 404 });
    }'''

content = content.replace(old_logic, new_logic)

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'w', encoding='utf-8') as f:
    f.write(content)
