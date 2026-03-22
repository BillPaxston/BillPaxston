"""
replace_omotesando.py
表参道高価格帯サロン アートディレクター選定 - 最終版

戦略:
  HERO:    Unsplash - "woman at hairdresser" (salon + woman scene, w=1600 h=900)
  CONCEPT: Pexels cottonbro series - 東アジア系女性, clean modern salon
  GALLERY: 確認済み日本人Unsplash (G1/G2/G4/G5/G6) + Pexels salon (G3/G7/G8/G9)
  STAFF:   Unsplash professional portraits

NG→変更:
  - ヘアカラーのアップ写真だったHeroをサロンシーン女性に変更
  - コンセプト3枚をcottonbroの東アジア系女性に刷新
  - ピンクヘア渋谷(派手可能性)をサロンカットに変更
  - Gallery G7/G8/G9をPexels現代サロンに変更
  - Staff全3枚をより専門的なポートレートに変更
"""

BASE_U = "https://images.unsplash.com/photo-"
BASE_P = "https://images.pexels.com/photos"

def u(pid, w, h=None, q=80):
    if h:
        return f"{BASE_U}{pid}?auto=format&fit=crop&w={w}&h={h}&q={q}"
    return f"{BASE_U}{pid}?auto=format&fit=crop&w={w}&q={q}"

def p(pid, w):
    return f"{BASE_P}/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w={w}"

with open('template_beauty_salon.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

replacements = [
    # ===== HERO =====
    # 旧: "Beautiful modern hair colour" (ヘアのアップ)
    # 新: "Young beautiful woman having her hair cut" (サロン空間+女性)
    (200,
     u("1574773004910-1eeaabb62b55", 1600, 900),
     u("1700760934268-8aa0ef52ce0a", 1600, 900),
     "HERO: woman at hairdresser salon"),

    # ===== CONCEPT 3枚 =====
    # CONCEPT-左: 旧hair cut action → Pexels cottonbro ヘアウォッシュ (東アジア系)
    (798,
     u("1700760934268-8aa0ef52ce0a", 800),
     p(3993449, 800),
     "CONCEPT-L: hair wash East Asian (cottonbro)"),

    # CONCEPT-右上: 旧 back of head → Pexels cottonbro ヘアカット (東アジア系)
    (804,
     u("1670797904283-072ad4dde22c", 800),
     p(3993453, 800),
     "CONCEPT-RT: hair cut East Asian (cottonbro)"),

    # CONCEPT-右下: 旧 Taiwan hair cut → Pexels cottonbro ヘアカラー (東アジア系)
    (810,
     u("1563798163029-5448a0ffd596", 800),
     p(3993323, 800),
     "CONCEPT-RB: hair color East Asian (cottonbro)"),

    # ===== GALLERY =====
    # G3: 旧 Shibuya pink hair (派手の可能性) → Pexels cottonbro ヘアカット (クリーンサロン)
    (863,
     u("1564933383265-6e24b634fc69", 600, 600),
     p(3992875, 600),
     "G3: cottonbro salon haircut"),

    # G7: 旧 brown hair white ribbon → Pexels modern salon
    (909,
     u("1605980625982-b128a7e7fde2", 600, 600),
     p(7258723, 600),
     "G7: Pexels modern salon"),

    # G8: 旧 grey/black hair → Pexels contemporary salon
    (920,
     u("1605980625600-88b46abafa8d", 600, 600),
     p(7755663, 600),
     "G8: Pexels contemporary salon"),

    # G9: 旧 woman long hair → Pexels salon woman
    (931,
     u("1655517638449-872fe32a77c8", 600, 600),
     p(7755447, 600),
     "G9: Pexels salon woman"),

    # ===== STAFF 3枚 =====
    # Staff1: 旧 woman long hair window → Japan professional woman white coat
    (1032,
     u("1692032219580-a7f6c5e501f2", 400, 533),
     u("1581255745856-7de5fcfb52ca", 400, 533),
     "Staff1: Japan white coat professional"),

    # Staff2: 旧 "Tokyo Girl" → woman long hair window (professional portrait)
    (1041,
     u("1605932949609-4c0c805674f6", 400, 533),
     u("1692032219580-a7f6c5e501f2", 400, 533),
     "Staff2: long hair window portrait"),

    # Staff3: 旧 white shirt earrings → "Her story" portrait
    (1050,
     u("1611653842967-39eb011b2ca3", 400, 533),
     u("1526856857605-a8b0666be944", 400, 533),
     "Staff3: Her story portrait"),
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
        print(f"NG  {label} (L{line_num})")
        print(f"    expected: {old_frag[:90]}")
        print(f"    actual:   {lines[idx].strip()[:95]}")
        fail += 1

with open('template_beauty_salon.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\n{success} replaced, {fail} failed")
print("KEPT (already best): G1 Japanese hairstyle Kyoto, G2 Japanese bleached hair,")
print("                     G4/G5 Japanese portrait (JP text confirmed), G6 Japanese portrait autumn")
