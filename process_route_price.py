import re

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix artist validation
content = content.replace(
    "const artist = ARTISTS.find(b => b.id === data.artistId);",
    "const artist = data.artistId === 'Studio' ? { name: 'Studio', price: service.price, priceLabel: service.priceLabel } : ARTISTS.find(b => b.id === data.artistId);"
)

# Replace artist.price with service.price for clarity, though we set it above anyway.
content = content.replace("Price: Rp ", "Price: ")
content = content.replace("price: artist.price", "price: service.price")
content = content.replace("artist.priceLabel", "service.priceLabel")

with open(r'c:\Users\Windows\Videos\NAIL ART WEBSITE\src\app\api\booking\route.ts', 'w', encoding='utf-8') as f:
    f.write(content)
