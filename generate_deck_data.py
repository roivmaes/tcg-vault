import urllib.request
import urllib.parse
import json

def fetch_deck_info():
    print("Obteniendo base de datos de YGOPRODeck para decks...")
    url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        all_cards = json.loads(resp.read().decode('utf-8'))['data']

    name_map = {}
    for c in all_cards:
        name_map[c['name'].lower()] = c

    # Leer inventario de Google Sheet para saber ID y categoría
    with open('d:/S I S T E M A S/TCG/cards.json', 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    inv_lookup = {}
    for item in inventory:
        inv_lookup[item['name'].lower()] = item
        if item.get('original_name'):
            inv_lookup[item['original_name'].lower()] = item

    # DEFINICIÓN DE DECKS
    decks_definitions = [
        # 1. LIGHTSWORN (EDISON 2010)
        {
            "id": "lightsworn_edison_2010",
            "name": "Lightsworn (Formato Edison - 2010)",
            "short_name": "Lightsworn Edison",
            "subtitle": "Mazo Edison de 40 Cartas + 3 Extra Deck",
            "format": "Edison (2010)",
            "tag": "Retro / Edison",
            "tag_color": "amber",
            "description": "Lista unificada de 40 cartas para formato Edison (2010). Combina el núcleo de molienda y control de cementerio con Judgment Dragon, soporte versátil y un Extra Deck de sincronías para Fabled Raven.",
            "cards_spec": [
                {"name": "Judgment Dragon", "count": 1, "section": "monsters", "note": "Tu jefe final"},
                {"name": "Lumina, Lightsworn Summoner", "count": 1, "section": "monsters", "note": "Invocadora / Resucitadora"},
                {"name": "Lyla, Lightsworn Sorceress", "count": 1, "section": "monsters", "note": "Destructora de Mágicas/Trampas"},
                {"name": "Ryko, Lightsworn Hunter", "count": 1, "section": "monsters", "note": "Destrucción Flip y Molienda"},
                {"name": "Wulf, Lightsworn Beast", "count": 1, "section": "monsters", "note": "Invocación especial al enviarse al cementerio"},
                {"name": "Celestia, Lightsworn Angel", "count": 1, "section": "monsters", "note": "Tributo Lightsworn / Destrucción x2"},
                {"name": "Garoth, Lightsworn Warrior", "count": 1, "section": "monsters", "note": "Robo y aceleración"},
                {"name": "Ehren, Lightsworn Monk", "count": 1, "section": "monsters", "note": "Devuelve defensas al mazo"},
                {"name": "Jain, Lightsworn Paladin", "count": 2, "section": "monsters", "note": "2 copias (Principal + Suelta)"},
                {"name": "Gragonith, Lightsworn Dragon", "count": 1, "section": "monsters", "note": "Daño de penetración y ATK"},
                {"name": "Honest", "count": 1, "section": "monsters", "note": "Hand-trap de ATK para LIGHT"},
                {"name": "Jinzo", "count": 1, "section": "monsters", "note": "Bloqueo total de cartas Trampa"},
                {"name": "Fabled Raven", "count": 1, "section": "monsters", "note": "Cantante (Tuner) / Modifica nivel"},
                {"name": "Kuriboh", "count": 2, "section": "monsters", "note": "2 copias en tus cajas (Principal + Suelta)"},
                {"name": "Nimble Momonga", "count": 1, "section": "monsters", "note": "Recuperación de LP y bloqueo"},
                {"name": "Mask of Darkness", "count": 1, "section": "monsters", "note": "Recupera trampas del cementerio"},
                {"name": "Gearfried the Iron Knight", "count": 1, "section": "monsters", "note": "Inmunidad a cartas de equipo"},
                {"name": "Dark Valkyria", "count": 1, "section": "monsters", "note": "Géminis con contador mágico"},
                {"name": "Twin-Headed Behemoth", "count": 1, "section": "monsters", "note": "Resurrección automática (Triple-Headed)"},
                {"name": "Spirit of the Harp", "count": 1, "section": "monsters", "note": "Muralla defensiva (DEF 2000)"},
                {"name": "Naturia Cliff", "count": 1, "section": "monsters", "note": "Buscador Naturia de reemplazo"},
                {"name": "Naturia Pumpkin", "count": 1, "section": "monsters", "note": "Invocación adicional para Sincronía"},
                {"name": "Charge of the Light Brigade", "count": 1, "section": "spells", "note": "Buscador clave Lightsworn"},
                {"name": "Solar Recharge", "count": 1, "section": "spells", "note": "Robo x2 y molienda"},
                {"name": "Monster Reincarnation", "count": 1, "section": "spells", "note": "Recupera Judgment Dragon"},
                {"name": "Foolish Burial", "count": 1, "section": "spells", "note": "Envía a Wulf al cementerio"},
                {"name": "Mystical Space Typhoon", "count": 1, "section": "spells", "note": "Destrucción rápida de Mágicas/Trampas"},
                {"name": "Book of Moon", "count": 1, "section": "spells", "note": "Control y reutilización Flip"},
                {"name": "Swords of Revealing Light", "count": 1, "section": "spells", "note": "Protección por 3 turnos"},
                {"name": "Pot of Avarice", "count": 1, "section": "spells", "note": "Recicla 5 y roba 2"},
                {"name": "Card Destruction", "count": 1, "section": "spells", "note": "Renovación de mano y molienda"},
                {"name": "Dragged Down into the Grave", "count": 1, "section": "spells", "note": "Interrupción de mano rival"},
                {"name": "Mirror Force", "count": 1, "section": "traps", "note": "Castigo total al ataque rival"},
                {"name": "Bottomless Trap Hole", "count": 1, "section": "traps", "note": "Destrucción y destierro"},
                {"name": "Compulsory Evacuation Device", "count": 1, "section": "traps", "note": "Devuelve al rival a la mano"},
                {"name": "Beckoning Light", "count": 1, "section": "traps", "note": "Recupera monstruos LIGHT"},
                {"name": "Vanquishing Light", "count": 1, "section": "traps", "note": "Niega y destruye tributando"},
                {"name": "Mind Crush", "count": 1, "section": "traps", "note": "Lectura y descarte"},
                {"name": "Stardust Dragon", "count": 1, "section": "extra", "note": "Sincronía 8 - Anulación de destrucción"},
                {"name": "Naturia Beast", "count": 1, "section": "extra", "note": "Sincronía 5 - Anulación infinita de Mágicas"},
                {"name": "Naturia Barkion", "count": 1, "section": "extra", "note": "Sincronía 6 - Anulación infinita de Trampas"}
            ]
        },
        # 2. DARK WORLD (FORMATO ACTUAL / AVANZADO)
        {
            "id": "dark_world_modern",
            "name": "Dark World (Formato Actual / Moderno)",
            "short_name": "Dark World Moderno",
            "subtitle": "Mazo Competitivo de 40 Cartas + Extra Deck Fusión & Link",
            "format": "Avanzado / Actual",
            "tag": "Formato Actual",
            "tag_color": "purple",
            "description": "Tu opción más fuerte para el formato actual. Aprovecha al máximo la caja Structure Deck: Dark World y complementa con Handtraps (Effect Veiler, Droll & Lock Bird) y limpiacampos (Raigeki, Harpie's Feather Duster, Dark Ruler No More).",
            "cards_spec": [
                {"name": "Reign-Beaux, Overking of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Jefe del mazo principal"},
                {"name": "Grapha, Dragon Lord of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Resurrección infinita y destrucción"},
                {"name": "Genta, Gateman of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Busca The Gates of Dark World"},
                {"name": "Snoww, Unlight of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Buscadora universal del arquetipo"},
                {"name": "Sillva, Warlord of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Invocación especial y descarte al rival"},
                {"name": "Goldd, Wu-Lord of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Invocación especial y destrucción x2"},
                {"name": "Broww, Huntsman of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Motor de robo"},
                {"name": "Beiige, Vanguard of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Invocación especial inmediata"},
                {"name": "Ceruli, Guru of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Se invoca al rival para efectos secundarios"},
                {"name": "Lucent, Netherlord of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Invocación desde el Deck"},
                {"name": "Latinum, Exarch of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Modificador de ATK"},
                {"name": "Parl, Hermit of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Recuperación del cementerio"},
                {"name": "Scarr, Scout of Dark World", "count": 1, "section": "monsters", "note": "Caja Dark World - Buscador de nivel 2 o menor"},
                {"name": "Danger! Bigfoot!", "count": 1, "section": "monsters", "note": "Caja Dark World - Destrucción boca arriba y cuerpo 3000 ATK"},
                {"name": "Danger! Thunderbird!", "count": 1, "section": "monsters", "note": "Caja Dark World - Destrucción boca abajo y 2800 ATK"},
                {"name": "Danger! Mothman!", "count": 1, "section": "monsters", "note": "Caja Dark World - Robo y descarte masivo"},
                {"name": "Danger!? Tsuchinoko?", "count": 1, "section": "monsters", "note": "Caja Dark World - Invocación especial garantizada"},
                {"name": "Effect Veiler", "count": 1, "section": "monsters", "note": "Búscala en Spirit Charmers - Handtrap niega monstruo rival"},
                {"name": "Droll & Lock Bird", "count": 1, "section": "monsters", "note": "Búscala en Spirit Charmers - Handtrap frena robo y búsquedas"},
                {"name": "The Gates of Dark World", "count": 1, "section": "spells", "note": "Caja Dark World - Campo motor de robo y descarte"},
                {"name": "Dark World Archives", "count": 1, "section": "spells", "note": "Caja Dark World - Bono de ATK e invocación"},
                {"name": "Dark World Dealings", "count": 1, "section": "spells", "note": "Caja Dark World - Ambos roban y descartan"},
                {"name": "Charge Into a Dark World", "count": 1, "section": "spells", "note": "Caja Dark World - Resurrección y descarte"},
                {"name": "Gateway to Dark World", "count": 1, "section": "spells", "note": "Caja Dark World - Mágica rápida de resurrección"},
                {"name": "Dark World Lightning", "count": 1, "section": "spells", "note": "Caja Dark World - Destrucción boca abajo y descarte"},
                {"name": "Dark World Puppetry", "count": 1, "section": "spells", "note": "Caja Dark World - ¡Fusión de campo/cementerio!"},
                {"name": "Card Destruction", "count": 1, "section": "spells", "note": "Caja Dark World - Disparo masivo de efectos"},
                {"name": "Dragged Down into the Grave", "count": 1, "section": "spells", "note": "Caja Dark World - Control total de la mano rival"},
                {"name": "Raigeki", "count": 1, "section": "spells", "note": "Búscala en Spirit Charmers / Legendary Decks II - Limpiador total"},
                {"name": "Dark Hole", "count": 1, "section": "spells", "note": "Búscala en Legendary Decks II - Destruye todos los monstruos"},
                {"name": "Harpie's Feather Duster", "count": 1, "section": "spells", "note": "Búscala en Obelisk / Legendary Decks II - Limpiador Mágicas/Trampas"},
                {"name": "Dark Ruler No More", "count": 1, "section": "spells", "note": "Búscala en Spirit Charmers - Niega todo el campo rival"},
                {"name": "Monster Reborn", "count": 1, "section": "spells", "note": "Búscala en Legendary Decks II - Resurrección universal"},
                {"name": "Dark World Punishment", "count": 1, "section": "traps", "note": "Caja Dark World - Contratrampa anula invocación"},
                {"name": "The Forces of Darkness", "count": 1, "section": "traps", "note": "Caja Dark World - Recupera 2 Dark World a la mano"},
                {"name": "Dark Scheme", "count": 1, "section": "traps", "note": "Caja Dark World - Descarte disruptivo"},
                {"name": "Mind Crush", "count": 1, "section": "traps", "note": "Caja Dark World - Declara carta y descarta"},
                {"name": "Solemn Warning", "count": 1, "section": "traps", "note": "Búscala en Spirit Charmers - Paga 2000 LP y niega invocación"},
                {"name": "Dimensional Barrier", "count": 1, "section": "traps", "note": "Búscala en Spirit Charmers - Bloquea Extra Deck rival"},
                {"name": "Crackdown", "count": 1, "section": "traps", "note": "Búscala en Freezing Chains - Roba el mejor monstruo rival"},
                {"name": "Grapha, Dragon Overlord of Dark World", "count": 1, "section": "extra", "note": "Caja Dark World - ¡Jefe de Fusión! Altera efectos rivales"},
                {"name": "Clorless, Chaos King of Dark World", "count": 1, "section": "extra", "note": "Caja Dark World - Fusión masiva limpia-campos"},
                {"name": "Xtra HERO Dread Decimator", "count": 1, "section": "extra", "note": "Carta Link suelta (Sheet #296) - Enlaces y potencia de ataque"},
                {"name": "Decode Talker", "count": 1, "section": "extra", "note": "Caja 2-Player Starter Set / Ciberso - Monstruo Link 3"},
                {"name": "Link Spider", "count": 1, "section": "extra", "note": "Caja 2-Player Starter Set / Ciberso - Monstruo Link 1"}
            ]
        },
        # 3. MAZO HÉROE (ELEMENTAL, VISION, EVIL & DESTINY HERO)
        {
            "id": "hero_deck",
            "name": "Mazo HÉROE (Elemental, Vision, Evil & Destiny)",
            "short_name": "Mazo HÉROE",
            "subtitle": "Mazo de Fusión & Link de 40 Cartas + 7 Extra Deck",
            "format": "Avanzado / Casual GX",
            "tag": "HÉROE / Fusiones",
            "tag_color": "red",
            "description": "Mazo temático HÉROE unificado de 40 cartas principales y 7 en el Extra Deck. Aprovecha a Vision HERO Vyon y Destiny HERO Denier para enviar recursos al cementerio, fusiones devastadoras con Polymerization y Evil Assault, y soporte defensivo de primer nivel.",
            "cards_spec": [
                # MONSTRUOS (16)
                {"name": "Vision HERO Vyon", "count": 1, "section": "monsters", "note": "Sheet #290 - Tu mejor carta inicial: envía a Denier al cementerio"},
                {"name": "Destiny HERO - Denier", "count": 1, "section": "monsters", "note": "Sheet #183 - Se revive a sí mismo desde el cementerio"},
                {"name": "Evil HERO Darkest Knight", "count": 1, "section": "monsters", "note": "Sheet #198 - Tu atacante Evil HERO (Drakes Knight)"},
                {"name": "Elemental HERO Neos", "count": 1, "section": "monsters", "note": "Sheet #191 - Tu clásico as"},
                {"name": "Elemental HERO Neos Alius", "count": 1, "section": "monsters", "note": "Sheet #192 - Héroe Géminis de luz"},
                {"name": "Winged Kuriboh", "count": 1, "section": "monsters", "note": "Sheet #294 - Para defenderte y anular daño"},
                {"name": "Elemental HERO Bladedge", "count": 1, "section": "monsters", "note": "Caja Speed Duel GX - Daño de penetración (2600 ATK)"},
                {"name": "Elemental HERO Avian", "count": 1, "section": "monsters", "note": "Caja Speed Duel GX - Material de fusión clásico"},
                {"name": "Elemental HERO Burstinatrix", "count": 1, "section": "monsters", "note": "Caja Speed Duel GX - Material de fusión clásico"},
                {"name": "Elemental HERO Sparkman", "count": 1, "section": "monsters", "note": "Caja Speed Duel GX - Material de fusión clásico (1600 ATK)"},
                {"name": "Elemental HERO Clayman", "count": 1, "section": "monsters", "note": "Caja Speed Duel GX - Muralla defensiva (2000 DEF)"},
                {"name": "Effect Veiler", "count": 1, "section": "monsters", "note": "Sheet #47 (Spirit Charmers) - Handtrap niega monstruo rival"},
                {"name": "Droll & Lock Bird", "count": 1, "section": "monsters", "note": "Sheet #45 (Spirit Charmers) - Handtrap frena robo y búsquedas"},
                {"name": "Ghost Mourner & Moonlit Chill", "count": 1, "section": "monsters", "note": "Sheet #67 (Spirit Charmers) - Handtrap niega y quema daño"},
                {"name": "Jinzo", "count": 1, "section": "monsters", "note": "Sheet #92 (Legendary Decks II) - Evita trampas al atacar"},
                {"name": "Absolute King Back Jack", "count": 1, "section": "monsters", "note": "Sheet #123 (Caja Dark World) - Relleno defensivo / Trampa"},

                # MÁGICAS (16)
                {"name": "A Hero Lives", "count": 1, "section": "spells", "note": "Sheet #157 - Pagas mitad de LP e invocas Héroe directo del Deck"},
                {"name": "Evil Assault", "count": 1, "section": "spells", "note": "Sheet #197 - Soporte supremo para tu Darkest Knight"},
                {"name": "Polymerization", "count": 2, "section": "spells", "note": "Sheet #111 (Legendary Decks II) - 2 copias para asegurar fusiones"},
                {"name": "Hero Flash!!", "count": 1, "section": "spells", "note": "Sheet #201 - Flash H.E.R.O. ofensiva final"},
                {"name": "Wrath of Neos", "count": 1, "section": "spells", "note": "Sheet #295 - Destruye todo el campo con Neos"},
                {"name": "Monster Reborn", "count": 1, "section": "spells", "note": "Sheet #103 (Legendary Decks II) - Resurrección universal"},
                {"name": "Raigeki", "count": 1, "section": "spells", "note": "Sheet #118 (Spirit Charmers) - Limpiador total de monstruos"},
                {"name": "Dark Hole", "count": 1, "section": "spells", "note": "Sheet #37 (Legendary Decks II) - Destrucción de campo"},
                {"name": "Harpie's Feather Duster", "count": 1, "section": "spells", "note": "Sheet #78 (Obelisk) - Limpiador de Mágicas/Trampas"},
                {"name": "Twin Twisters", "count": 1, "section": "spells", "note": "Sheet #149 (Spirit Charmers) - Destruye 2 Mágicas/Trampas"},
                {"name": "Mystical Space Typhoon", "count": 1, "section": "spells", "note": "Sheet #104 (Starter Set) - Destrucción rápida"},
                {"name": "Book of Moon", "count": 1, "section": "spells", "note": "Sheet #11 (Starter Set) - Control y libro de la luna"},
                {"name": "Dark Ruler No More", "count": 1, "section": "spells", "note": "Sheet #38 (Spirit Charmers) - Niega efectos en campo rival"},
                {"name": "Pot of Avarice", "count": 1, "section": "spells", "note": "Sheet #114 (Obelisk) - Devuelve Héroes usados y roba 2"},
                {"name": "Swords of Revealing Light", "count": 1, "section": "spells", "note": "Sheet #144 (Legendary Decks II) - Protección 3 turnos"},

                # TRAMPAS (8)
                {"name": "Mirror Force", "count": 1, "section": "traps", "note": "Sheet #101 (Legendary Decks II) - Castigo al ataque rival"},
                {"name": "Bottomless Trap Hole", "count": 1, "section": "traps", "note": "Sheet #12 (Legendary Decks II) - Destierro en invocación"},
                {"name": "Compulsory Evacuation Device", "count": 1, "section": "traps", "note": "Sheet #24 (Starter Set) - Devuelve a la mano"},
                {"name": "Solemn Warning", "count": 1, "section": "traps", "note": "Sheet #137 (Spirit Charmers) - Paga 2000 LP y niega invocación"},
                {"name": "Dimensional Barrier", "count": 1, "section": "traps", "note": "Sheet #43 (Spirit Charmers) - Bloquea Extra Deck rival"},
                {"name": "Crackdown", "count": 1, "section": "traps", "note": "Sheet #32 (Freezing Chains) - Roba un monstruo rival"},
                {"name": "Fiendish Chain", "count": 1, "section": "traps", "note": "Sheet #57 (Freezing Chains) - Niega efectos y ataque"},
                {"name": "Drowning Mirror Force", "count": 1, "section": "traps", "note": "Sheet #46 (Obelisk) - Devuelve monstruos al mazo"},

                # EXTRA DECK (7)
                {"name": "Vision HERO Trinity", "count": 1, "section": "extra", "note": "Sheet #289 - ¡Tu jefe final! Gana 5000 ATK y golpea 3 veces"},
                {"name": "Xtra HERO Dread Decimator", "count": 1, "section": "extra", "note": "Sheet #296 - Tu monstruo Link: potencia ATK a enlaces"},
                {"name": "Elemental HERO Escuridao", "count": 1, "section": "extra", "note": "Sheet #190 - Fusión genérica muy versátil"},
                {"name": "Elemental HERO Shining Flare Wingman", "count": 1, "section": "extra", "note": "Sheet #194 - Gana ATK por cada Héroe en cementerio"},
                {"name": "Elemental HERO Neos Knight", "count": 1, "section": "extra", "note": "Sheet #193 - Fusión ofensiva con doble ataque"},
                {"name": "Elemental HERO Flame Wingman", "count": 1, "section": "extra", "note": "Caja Speed Duel GX - Quema daño de efecto al destruir"},
                {"name": "Elemental HERO Thunder Giant", "count": 1, "section": "extra", "note": "Caja Speed Duel GX - Destrucción por descarte"}
            ]
        }
    ]

    all_processed_decks = []

    for d in decks_definitions:
        processed_cards = []
        main_count = 0
        extra_count = 0

        for item in d['cards_spec']:
            card_name = item['name']
            c_info = name_map.get(card_name.lower())
            if not c_info:
                print("Aviso: Carta no encontrada:", card_name)
                continue

            primary_img = c_info.get('card_images', [{}])[0]
            card_prices = c_info.get('card_prices', [{}])[0] if c_info.get('card_prices') else {}

            inv_item = inv_lookup.get(card_name.lower())
            if not inv_item and card_name == "Twin-Headed Behemoth":
                inv_item = inv_lookup.get("triple-headed behemoth")

            is_owned = True
            sheet_id = inv_item.get('sheet_id') if inv_item else None
            sheet_category = inv_item.get('category') if inv_item else None

            custom_location = None
            if not sheet_id:
                if "Speed Duel GX" in item['note']:
                    custom_location = "Caja Speed Duel GX"
                elif "Dark World" in item['note']:
                    custom_location = "Caja Dark World"
                elif "Starter Set" in item['note']:
                    custom_location = "Caja Starter Set"
                elif "Kuriboh" in item['name']:
                    custom_location = "En tus Cajas / Suelta"
                else:
                    custom_location = "En tus Cajas"

            count = item['count']
            if item['section'] == 'extra':
                extra_count += count
            else:
                main_count += count

            processed_cards.append({
                "name": c_info['name'],
                "section": item['section'],
                "count": count,
                "note": item['note'],
                "owned": is_owned,
                "sheet_id": sheet_id,
                "sheet_category": sheet_category,
                "custom_location": custom_location,
                "type": c_info.get('type', ''),
                "humanReadableCardType": c_info.get('humanReadableCardType', c_info.get('type', '')),
                "frameType": c_info.get('frameType', 'normal'),
                "desc": c_info.get('desc', ''),
                "race": c_info.get('race', ''),
                "archetype": c_info.get('archetype', ''),
                "atk": c_info.get('atk', None),
                "def": c_info.get('def', None),
                "level": c_info.get('level', None),
                "attribute": c_info.get('attribute', None),
                "image_url": primary_img.get('image_url', ''),
                "image_url_small": primary_img.get('image_url_small', ''),
                "prices": {
                    "tcgplayer": card_prices.get('tcgplayer_price', ''),
                    "cardmarket": card_prices.get('cardmarket_price', '')
                },
                "ygoprodeck_url": f"https://ygoprodeck.com/card/?search={urllib.parse.quote(c_info.get('name', ''))}"
            })

        total_deck_cost = sum(float(c.get('prices', {}).get('tcgplayer', 0) or 0) * c.get('count', 1) for c in processed_cards)
        total_cards_count = main_count + extra_count

        deck_obj = {
            "id": d['id'],
            "name": d['name'],
            "short_name": d['short_name'],
            "subtitle": d['subtitle'],
            "format": d['format'],
            "tag": d['tag'],
            "tag_color": d['tag_color'],
            "description": d['description'],
            "stats": {
                "main_total": main_count,
                "extra_total": extra_count,
                "monsters": sum(c['count'] for c in processed_cards if c['section'] == 'monsters'),
                "spells": sum(c['count'] for c in processed_cards if c['section'] == 'spells'),
                "traps": sum(c['count'] for c in processed_cards if c['section'] == 'traps'),
                "owned_count": total_cards_count,
                "total_cost": round(total_deck_cost, 2)
            },
            "cards": processed_cards
        }
        all_processed_decks.append(deck_obj)
        print(f"Deck '{deck_obj['name']}': Main {main_count}, Extra {extra_count}, En posesión {deck_obj['stats']['owned_count']}/{total_cards_count} (100%!) | Costo: ${deck_obj['stats']['total_cost']}")

    with open("d:/S I S T E M A S/TCG/decks.json", "w", encoding="utf-8") as f:
        json.dump(all_processed_decks, f, ensure_ascii=False, indent=2)

    with open("d:/S I S T E M A S/TCG/decks_data.js", "w", encoding="utf-8") as f:
        f.write("var TCG_DECKS_DATA = " + json.dumps(all_processed_decks, ensure_ascii=False, indent=2) + ";\nif (typeof window !== 'undefined') { window.TCG_DECKS_DATA = TCG_DECKS_DATA; }\n")

    print(f"Total de mazos generados: {len(all_processed_decks)}")

if __name__ == "__main__":
    fetch_deck_info()
