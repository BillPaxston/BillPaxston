"""
replace_salon_fix.py
Fix non-salon-appropriate images:
  Hero: street crossing -> beautiful modern hair colour
  G7:   duplicate autumn portrait -> woman with long hair
  G8:   subway woman -> brown hair with white ribbon
  G9:   grocery shopping -> grey and black hair portrait
"""

BASE = "https://images.unsplash.com/photo-"

def u(photo_id, w, h=None, q=80):
    if h:
        return f"{BASE}{photo_id}?auto=format&fit=crop&w={w}&h={h}&q={q}"
    return f"{BASE}{photo_id}?auto=format&fit=crop&w={w}&q={q}"

with open('template_beauty_salon.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

replacements = [
    # Hero: woman at zebra crossing Tokyo (street snap) -> Beautiful modern hair colour
    (200,
     u("1609561515321-bd13ea22d74a", 1600, 900),
     u("1574773004910-1eeaabb62b55", 1600, 900),
     "Hero: hair colour"),

    # G7: duplicate autumn portrait (same series as G6) -> woman with long hair
    (909,
     u("1700995825444-5040ad9a47ed", 600, 600),
     u("1655517638449-872fe32a77c8", 600, 600),
     "G7: long hair woman"),

    # G8: Japanese woman on subway with large hat -> brown hair with white ribbon
    (920,
     u("1609561515342-e9f1dbddca9e", 600, 600),
     u("1605980625982-b128a7e7fde2", 600, 600),
     "G8: brown hair ribbon"),

    # G9: Japanese woman doing groceries -> grey and black hair portrait
    (931,
     u("1743513694665-462fa3b46c2e", 600, 600),
     u("1605980625600-88b46abafa8d", 600, 600),
     "G9: grey black hair"),
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
        print(f"    expected: {old_frag}")
        print(f"    actual:   {lines[idx].strip()[:100]}")
        fail += 1

with open('template_beauty_salon.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nDone: {success} replaced, {fail} failed")
