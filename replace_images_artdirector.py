"""
replace_images_artdirector.py
Art director curation: Japanese/East Asian women, modern Tokyo salon aesthetic
Natural light, minimal, white/beige/greige tones, consistent brand identity

Changes:
  L798  CONCEPT-left    : scissors action -> woman having hair cut (verified 200)
  L810  CONCEPT-right-bottom: scissors still life -> Taiwan hair cut (East Asian, salon)
  L909  Gallery 7       : Chinese street photo -> Japanese portrait autumn (confirmed JP)
  L920  Gallery 8       : unknown woman holding hair -> Japanese woman subway (confirmed JP)
  L931  Gallery 9       : unknown long hair -> Japanese lady Tokyo (confirmed JP)
  L1032 Staff 1         : unknown -> woman long hair by window (soft portrait)
  L1050 Staff 3         : unknown white floral shirt -> woman white shirt silver earrings

Kept (already confirmed Japanese/East Asian):
  L200  Hero            : confirmed Japanese woman, zebra crossing Tokyo
  L804  CONCEPT-right-top: back of short hair (hair detail)
  L841  Gallery 1       : Japanese hairstyle, Kyoto (confirmed)
  L852  Gallery 2       : Young Japanese woman bleached hair (confirmed)
  L863  Gallery 3       : pink hair from behind, Shibuya Crossing Tokyo (confirmed)
  L875  Gallery 4       : portrait (Japanese woman) - JP text confirmed
  L886  Gallery 5       : portrait (Japanese woman) - JP text confirmed
  L897  Gallery 6       : portrait woman autumn - JP text confirmed
  L1041 Staff 2         : Tokyo Girl (confirmed Tokyo context)
"""

BASE = "https://images.unsplash.com/photo-"

def u(photo_id, w, h=None, q=80):
    if h:
        return f"{BASE}{photo_id}?auto=format&fit=crop&w={w}&h={h}&q={q}"
    return f"{BASE}{photo_id}?auto=format&fit=crop&w={w}&q={q}"

with open('template_beauty_salon.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# (line_num, old_fragment, new_url, label)
replacements = [
    # CONCEPT left: hair cut action (woman being cut, more vivid than prev)
    (798,
     u("1666622833860-562f3a5caa59", 800),
     u("1700760934268-8aa0ef52ce0a", 800),
     "CONCEPT-left: woman hair cut"),

    # CONCEPT right-bottom: Taiwan hair cut (East Asian salon, replaces scissors still life)
    (810,
     u("1625038032200-648fbcd800d0", 800),
     u("1563798163029-5448a0ffd596", 800),
     "CONCEPT-right-bottom: Taiwan hair cut"),

    # Gallery 7: Japanese portrait autumn #2 (replaces ambiguous street photo)
    (909,
     u("1627015850304-fcb423100bf4", 600, 600),
     u("1700995825444-5040ad9a47ed", 600, 600),
     "G7: Japanese portrait autumn"),

    # Gallery 8: Japanese woman subway large hat (confirmed Japanese, modern fashion)
    (920,
     u("1617690825153-8bb0a8e3c911", 600, 600),
     u("1609561515342-e9f1dbddca9e", 600, 600),
     "G8: Japanese woman subway"),

    # Gallery 9: Japanese lady doing groceries in Tokyo (confirmed Japanese)
    (931,
     u("1675335683975-d2a4444c35a3", 600, 600),
     u("1743513694665-462fa3b46c2e", 600, 600),
     "G9: Japanese lady Tokyo"),

    # Staff 1: woman with long hair by window (soft natural light, portrait)
    (1032,
     u("1636754151864-cef580d08bdc", 400, 533),
     u("1692032219580-a7f6c5e501f2", 400, 533),
     "Staff1: long hair window"),

    # Staff 3: woman white shirt silver earrings (clean, professional)
    (1050,
     u("1596381809178-0c8a2d9c9c2d", 400, 533),
     u("1611653842967-39eb011b2ca3", 400, 533),
     "Staff3: white shirt earrings"),
]

success = 0
fail = 0
for line_num, old_frag, new_frag, label in replacements:
    idx = line_num - 1
    if old_frag in lines[idx]:
        lines[idx] = lines[idx].replace(old_frag, new_frag)
        print(f"OK  {label} (L{line_num})")
        success += 1
    else:
        print(f"NG  {label} (L{line_num}) - not found")
        print(f"    expected: {old_frag[:80]}")
        print(f"    actual:   {lines[idx].strip()[:90]}")
        fail += 1

with open('template_beauty_salon.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nDone: {success} replaced, {fail} failed, 9 kept as-is (already confirmed Japanese)")
