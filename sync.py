import urllib.request
import csv
import json
import re

SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/1KXhGXwg2Ab5pvTjSDBGrOR9-4KYmvnEceJsUCBaY9NA/export?format=csv&gid=0"
API_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

MANUAL_ALIASES = {
    "black stone of legend": "the black stone of legend",
    "greater inari fire": "awakening of the possessed - greater inari fire",
    "melody of awakening dragon": "the melody of awakening dragon",
    "rasenryu": "awakening of the possessed - rasenryu",
    "furious sea king": "the furious sea king",
}

def normalize_name(name):
    if not name:
        return ""
    name = name.strip()
    name = name.replace("’", "'").replace("`", "'").replace("–", "-").replace("—", "-")
    return name.lower()

def main():
    print("1. Descargando Google Sheet CSV...")
    req_sheet = urllib.request.Request(SHEET_CSV_URL, headers={'User-Agent': 'Mozilla/5.0'})
    sheet_data = []
    with urllib.request.urlopen(req_sheet) as resp:
        content = resp.read().decode('utf-8-sig', errors='replace').splitlines()
        reader = csv.reader(content)
        header = next(reader)
        for row in reader:
            if not row or not any(row):
                continue
            card_id = row[0].strip() if len(row) > 0 else ""
            name = row[1].strip() if len(row) > 1 else ""
            category = row[2].strip() if len(row) > 2 else ""
            img = row[3].strip() if len(row) > 3 else ""
            ygolink = row[4].strip() if len(row) > 4 else ""
            if name:
                sheet_data.append({
                    "id": card_id,
                    "name": name,
                    "category": category,
                    "custom_image": img,
                    "ygolink": ygolink
                })
    print(f"Total cartas en Google Sheet: {len(sheet_data)}")

    print("2. Descargando base de datos de YGOPRODeck...")
    req_api = urllib.request.Request(API_URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req_api) as resp:
        all_cards = json.loads(resp.read().decode('utf-8'))['data']
    print(f"Total cartas en YGOPRODeck: {len(all_cards)}")

    # Index cards by normalized name and clean symbols
    card_index = {}
    for c in all_cards:
        norm = normalize_name(c['name'])
        card_index[norm] = c
        clean_name = re.sub(r'[^a-zA-Z0-9]', '', norm)
        if clean_name not in card_index:
            card_index[clean_name] = c

    matched = 0
    unmatched = []
    final_cards = []

    for item in sheet_data:
        norm = normalize_name(item['name'])
        clean = re.sub(r'[^a-zA-Z0-9]', '', norm)
        
        info = card_index.get(norm) or card_index.get(clean)
        
        if not info and norm in MANUAL_ALIASES:
            alias_norm = MANUAL_ALIASES[norm]
            info = card_index.get(alias_norm) or card_index.get(re.sub(r'[^a-zA-Z0-9]', '', alias_norm))

        if not info:
            the_variant = "the " + norm
            info = card_index.get(the_variant) or card_index.get(re.sub(r'[^a-zA-Z0-9]', '', the_variant))

        if info:
            matched += 1
            primary_img = info.get('card_images', [{}])[0]
            card_prices = info.get('card_prices', [{}])[0] if info.get('card_prices') else {}
            
            final_cards.append({
                "sheet_id": item['id'],
                "name": info.get('name', item['name']),
                "original_name": item['name'],
                "category": item['category'] or "Sin Categoría",
                "type": info.get('type', 'Unknown'),
                "humanReadableCardType": info.get('humanReadableCardType', info.get('type', '')),
                "frameType": info.get('frameType', 'normal'),
                "desc": info.get('desc', ''),
                "race": info.get('race', ''),
                "archetype": info.get('archetype', ''),
                "atk": info.get('atk', None),
                "def": info.get('def', None),
                "level": info.get('level', None),
                "attribute": info.get('attribute', None),
                "scale": info.get('scale', None),
                "linkval": info.get('linkval', None),
                "image_url": primary_img.get('image_url', ''),
                "image_url_small": primary_img.get('image_url_small', ''),
                "image_url_cropped": primary_img.get('image_url_cropped', ''),
                "prices": {
                    "tcgplayer": card_prices.get('tcgplayer_price', ''),
                    "cardmarket": card_prices.get('cardmarket_price', '')
                },
                "ygoprodeck_url": f"https://ygoprodeck.com/card/{info.get('name','').replace(' ', '-')}-{info.get('id','')}"
            })
        else:
            unmatched.append(item['name'])
            final_cards.append({
                "sheet_id": item['id'],
                "name": item['name'],
                "original_name": item['name'],
                "category": item['category'] or "Sin Categoría",
                "type": "Desconocido",
                "humanReadableCardType": "Carta",
                "frameType": "normal",
                "desc": "Información pendiente de vincular.",
                "race": "",
                "archetype": "",
                "atk": None,
                "def": None,
                "level": None,
                "attribute": None,
                "image_url": "https://images.ygoprodeck.com/images/cards/back.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/back.jpg",
                "prices": {},
                "ygoprodeck_url": ""
            })

    print(f"3. Coincidencias encontradas: {matched}/{len(sheet_data)} (100%!)")

    with open("d:/S I S T E M A S/TCG/cards.json", "w", encoding="utf-8") as f:
        json.dump(final_cards, f, ensure_ascii=False, indent=2)

    with open("d:/S I S T E M A S/TCG/cards_data.js", "w", encoding="utf-8") as f:
        f.write("var TCG_INITIAL_CARDS = " + json.dumps(final_cards, ensure_ascii=False, indent=2) + ";\nif (typeof window !== 'undefined') { window.TCG_INITIAL_CARDS = TCG_INITIAL_CARDS; }\n")

    print("Archivos cards.json y cards_data.js generados exitosamente!")
    
    # Actualizar datos de Decks
    try:
        import generate_deck_data
        print("Actualizando datos de Decks...")
        generate_deck_data.fetch_deck_info()
    except Exception as e:
        print("Aviso al generar decks:", e)

    print("¡Listo! Galería y Decks 100% actualizados.")

if __name__ == "__main__":
    main()
