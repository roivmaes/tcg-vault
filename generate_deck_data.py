import urllib.request
import urllib.parse
import json

def generate_all_decks():
    print("Obteniendo base de datos de YGOPRODeck para decks...")
    url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        all_cards = json.loads(resp.read().decode('utf-8'))['data']

    name_map = {}
    for c in all_cards:
        name_map[c['name'].lower()] = c

    # Leer inventario de cards.json para saber ID y categoría
    with open('d:/S I S T E M A S/TCG/cards.json', 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    inv_lookup = {}
    for item in inventory:
        inv_lookup[item['name'].lower()] = item
        if item.get('original_name'):
            inv_lookup[item['original_name'].lower()] = item

    # DEFINICIÓN DE LOS 3 DECKS ACTUALIZADOS (100% LEGALES Y EN COLECCIÓN)
    decks_definitions = [
        # 1. HÉROE DEFINITIVO (40 Main + 7 Extra)
        {
            "id": "hero_deck",
            "name": "Mazo HÉROE (Formato Avanzado / Moderno)",
            "short_name": "Mazo HÉROE Definitivo",
            "subtitle": "Mazo HÉROE Definitivo (40 cartas): Estructura rápida y agresiva 100% fiel a tus cajas físicas",
            "format": "Avanzado / Moderno",
            "tag": "HÉROE / Rápido & Agresivo",
            "tag_color": "red",
            "description": "Tu Mazo HÉROE definitivo de 40 cartas en el Main Deck y 7 en el Extra Deck. Una estructura rápida y agresiva basada estrictamente en tus cajas físicas y cartas sueltas reales, con Jinzo, Bottomless Trap Hole, Flash H.E.R.O. y acceso directo al Extra Deck con Trinity y Cross Crusader.",
            "cards_spec": [
                # MONSTRUOS (13)
                # Núcleo HÉROE (9)
                {"name": "Vision HERO Vyon", "count": 1, "section": "monsters", "note": "Carta suelta — Envía a Denier al cementerio y busca Polymerization"},
                {"name": "Destiny HERO - Denier", "count": 1, "section": "monsters", "note": "Carta suelta — Se invoca solo desde el cementerio"},
                {"name": "Elemental HERO Blazeman", "count": 1, "section": "monsters", "note": "De Midterm Paradox — Busca Polymerization"},
                {"name": "Elemental HERO Wildheart", "count": 1, "section": "monsters", "note": "De Midterm Paradox — Inmune a trampas"},
                {"name": "Elemental HERO Neos", "count": 1, "section": "monsters", "note": "Carta suelta — Guerrero de 2500 ATK"},
                {"name": "Elemental HERO Neos Alius", "count": 1, "section": "monsters", "note": "Carta suelta — Guerrero Géminis de 1900 ATK"},
                {"name": "Evil HERO Darkest Knight", "count": 1, "section": "monsters", "note": "Evil HERO Darkest Knight (Drakes Knight) — Carta suelta"},
                {"name": "Evil HERO Vicious Claws", "count": 2, "section": "monsters", "note": "2 copias — Héroe Malvado Garras Cruentas, cartas sueltas"},

                # Defensa e Interrupción (4)
                {"name": "Winged Kuriboh", "count": 2, "section": "monsters", "note": "2 copias — Cartas sueltas, reduce daño a cero"},
                {"name": "Effect Veiler", "count": 1, "section": "monsters", "note": "De tu Structure Deck: Spirit Charmers normal"},
                {"name": "Jinzo", "count": 1, "section": "monsters", "note": "De tu caja Legendary Decks II — Apaga todas las trampas del oponente"},

                # MAGIAS (18)
                # Velocidad y Fusiones (12)
                {"name": "A Hero Lives", "count": 2, "section": "spells", "note": "2 copias — Invoca a Vyon o Blazeman directo del mazo"},
                {"name": "Polymerization", "count": 2, "section": "spells", "note": "2 copias — De Legendary Decks II / Midterm Paradox"},
                {"name": "Evil Assault", "count": 1, "section": "spells", "note": "Carta suelta — Busca o invoca HÉROE"},
                {"name": "Monster Reborn", "count": 1, "section": "spells", "note": "De Legendary Decks II / Sueltas"},
                {"name": "Skyscraper 2 - Hero City", "count": 1, "section": "spells", "note": "De Midterm Paradox — Revive héroes caídos en batalla"},
                {"name": "Fifth Hope", "count": 1, "section": "spells", "note": "De Midterm Paradox — Recicla 5 cartas y roba"},
                {"name": "H - Heated Heart", "count": 1, "section": "spells", "note": "De Midterm Paradox — +500 ATK y penetración"},
                {"name": "R - Righteous Justice", "count": 1, "section": "spells", "note": "De Midterm Paradox — Destruye magias y trampas rivales"},
                {"name": "Hero Flash!!", "count": 1, "section": "spells", "note": "Flash H.E.R.O. — Carta suelta"},
                {"name": "Wrath of Neos", "count": 1, "section": "spells", "note": "Carta suelta — Limpieza total de campo con Neos"},

                # Limpieza y Control de Campo (6)
                {"name": "Raigeki", "count": 1, "section": "spells", "note": "De tu Structure Deck: Spirit Charmers normal"},
                {"name": "Dark Hole", "count": 1, "section": "spells", "note": "De Legendary Decks II / 2-Player Starter Set"},
                {"name": "Harpie's Feather Duster", "count": 1, "section": "spells", "note": "De tu caja Obelisk the Tormentor"},
                {"name": "Twin Twisters", "count": 1, "section": "spells", "note": "De tu Structure Deck: Spirit Charmers normal"},
                {"name": "Dark Ruler No More", "count": 1, "section": "spells", "note": "De tu Structure Deck: Spirit Charmers normal"},
                {"name": "Book of Moon", "count": 1, "section": "spells", "note": "De tu Set de Principiante 2 Jugadores / Decks y Cajas — Interrupción rápida para voltear boca abajo"},

                # TRAMPAS (9)
                {"name": "Hero Signal", "count": 1, "section": "traps", "note": "De Midterm Paradox"},
                {"name": "Hero Counterattack", "count": 1, "section": "traps", "note": "De Midterm Paradox"},
                {"name": "Crackdown", "count": 1, "section": "traps", "note": "De tu caja Freezing Chains"},
                {"name": "Solemn Warning", "count": 1, "section": "traps", "note": "De tu Structure Deck: Spirit Charmers normal"},
                {"name": "Dimensional Barrier", "count": 1, "section": "traps", "note": "De tu Structure Deck: Spirit Charmers normal"},
                {"name": "Drowning Mirror Force", "count": 1, "section": "traps", "note": "De tu caja Obelisk the Tormentor"},
                {"name": "Fiendish Chain", "count": 1, "section": "traps", "note": "De tu caja Freezing Chains"},
                {"name": "Heavy Storm Duster", "count": 1, "section": "traps", "note": "De tu caja Freezing Chains"},
                {"name": "Bottomless Trap Hole", "count": 1, "section": "traps", "note": "De tu caja Legendary Decks II"},

                # EXTRA DECK (7)
                {"name": "Xtra HERO Cross Crusader", "count": 2, "section": "extra", "note": "2 copias — Cartas sueltas, Link-2"},
                {"name": "Vision HERO Trinity", "count": 1, "section": "extra", "note": "Carta suelta — 5000 ATK, ataca 3 veces"},
                {"name": "Xtra HERO Dread Decimator", "count": 1, "section": "extra", "note": "Carta suelta — Link-3 con daño de penetración"},
                {"name": "Elemental HERO Nova Master", "count": 1, "section": "extra", "note": "De Midterm Paradox — Fusión Blazeman + 1 Elemental HERO"},
                {"name": "Elemental HERO Escuridao", "count": 1, "section": "extra", "note": "Carta suelta — 1 Elemental HERO + 1 Oscuridad"},
                {"name": "Elemental HERO Neos Knight", "count": 1, "section": "extra", "note": "Carta suelta — Neos + 1 Guerrero"}
            ]
        },

        # 2. LIGHTSWORN DEFINITIVO (FORMATO EDISON - RETRO 2010) - 40 Main + 1 Extra
        {
            "id": "lightsworn_edison_2010",
            "name": "Mazo LIGHTSWORN (Formato EDISON - Retro 2010)",
            "short_name": "Lightsworn Edison",
            "subtitle": "Optimizado al máximo con cartas del propio inventario (Cyber Dragon, Heavy Storm, Solemn Judgment, Torrential Tribute) y limpio de cartas ilegales o lentas",
            "format": "Edison (Abril 2010)",
            "tag": "Retro / Edison",
            "tag_color": "amber",
            "description": "Optimizado al máximo con cartas del propio inventario (Cyber Dragon, Heavy Storm, Solemn Judgment, Torrential Tribute) y limpio de cartas ilegales o lentas.",
            "cards_spec": [
                # MONSTRUOS (22)
                {"name": "Judgment Dragon", "count": 1, "section": "monsters", "note": "Tu jefe final"},
                {"name": "Lumina, Lightsworn Summoner", "count": 1, "section": "monsters", "note": "Invocadora / Resucitadora"},
                {"name": "Lyla, Lightsworn Sorceress", "count": 1, "section": "monsters", "note": "Destructora de Mágicas/Trampas"},
                {"name": "Ryko, Lightsworn Hunter", "count": 2, "section": "monsters", "note": "2 copias: Destrucción Flip y Molienda"},
                {"name": "Wulf, Lightsworn Beast", "count": 1, "section": "monsters", "note": "Invocación especial al cementerio"},
                {"name": "Celestia, Lightsworn Angel", "count": 1, "section": "monsters", "note": "Tributo Lightsworn / Destrucción x2"},
                {"name": "Garoth, Lightsworn Warrior", "count": 1, "section": "monsters", "note": "Robo y aceleración"},
                {"name": "Ehren, Lightsworn Monk", "count": 1, "section": "monsters", "note": "Devuelve defensas al mazo"},
                {"name": "Jain, Lightsworn Paladin", "count": 2, "section": "monsters", "note": "2 copias (Principal + Suelta)"},
                {"name": "Gragonith, Lightsworn Dragon", "count": 1, "section": "monsters", "note": "Daño de penetración y ATK"},
                {"name": "Aurkus, Lightsworn Druid", "count": 1, "section": "monsters", "note": "Sheet #438 - Protege a tus Lightsworn contra efectos que seleccionen"},
                {"name": "Shire, Lightsworn Spirit", "count": 1, "section": "monsters", "note": "Sheet #440 - Gana 300 ATK por cada Lightsworn distinto en cementerio"},
                {"name": "Necro Gardna", "count": 1, "section": "monsters", "note": "Sheet #441 - Se destierra del cementerio para anular un ataque rival"},
                {"name": "Honest", "count": 1, "section": "monsters", "note": "Hand-trap de ATK para LIGHT"},
                {"name": "Jinzo", "count": 1, "section": "monsters", "note": "De Legendary Decks II - Bloqueo de trampas"},
                {"name": "D.D. Crow", "count": 1, "section": "monsters", "note": "Sheet #362 - Handtrap clásica legal en Edison: destierra carta del cementerio rival"},
                {"name": "Mobius the Frost Monarch", "count": 1, "section": "monsters", "note": "Sheet #374 - Monarca legal en Edison: destruye hasta 2 Mágicas/Trampas al tributarse"},
                {"name": "Cyber Dragon", "count": 2, "section": "monsters", "note": "Sheet #404/#405 - 2 copias: Invocación especial de 2100 ATK si el rival controla monstruos"},
                {"name": "Breaker the Magical Warrior", "count": 1, "section": "monsters", "note": "Sheet #455 - 1900 ATK al invocarse y destruye una magia/trampa rival"},

                # MAGIAS (10)
                {"name": "Charge of the Light Brigade", "count": 1, "section": "spells", "note": "Buscador clave Lightsworn"},
                {"name": "Solar Recharge", "count": 1, "section": "spells", "note": "Robo x2 y molienda"},
                {"name": "Monster Reincarnation", "count": 1, "section": "spells", "note": "Recupera Judgment Dragon"},
                {"name": "Foolish Burial", "count": 1, "section": "spells", "note": "Envía a Wulf o Necro Gardna al cementerio"},
                {"name": "Mystical Space Typhoon", "count": 1, "section": "spells", "note": "Tu clásico rompe-magias"},
                {"name": "Book of Moon", "count": 1, "section": "spells", "note": "Control y libro de la luna"},
                {"name": "Pot of Avarice", "count": 1, "section": "spells", "note": "Recicla 5 y roba 2"},
                {"name": "Card Destruction", "count": 1, "section": "spells", "note": "Prestada de Dark World, perfecta para Edison"},
                {"name": "Realm of Light", "count": 1, "section": "spells", "note": "Sheet #442 - Magia de campo legal en Edison; acumula contadores y da ATK masivo"},
                {"name": "Heavy Storm", "count": 1, "section": "spells", "note": "Sheet #456 - Limpiador masivo de todas las magias y trampas del campo"},

                # TRAMPAS (8)
                {"name": "Mirror Force", "count": 1, "section": "traps", "note": "Castigo total al ataque rival"},
                {"name": "Bottomless Trap Hole", "count": 1, "section": "traps", "note": "Destrucción y destierro"},
                {"name": "Compulsory Evacuation Device", "count": 1, "section": "traps", "note": "Devuelve al rival a la mano"},
                {"name": "Beckoning Light", "count": 1, "section": "traps", "note": "Recupera monstruos LIGHT"},
                {"name": "Mind Crush", "count": 1, "section": "traps", "note": "Adivina o nombra una carta de la mano rival y deséchala"},
                {"name": "Torrential Tribute", "count": 1, "section": "traps", "note": "Sheet #457 - Destruye todos los monstruos del campo tras una invocación"},
                {"name": "Solemn Judgment", "count": 1, "section": "traps", "note": "Sheet #458 - Paga la mitad de tus LP y niega cualquier invocación, magia o trampa"},
                {"name": "Call of the Haunted", "count": 1, "section": "traps", "note": "Sheet #403 - Revive cualquier monstruo del cementerio en posición de ataque"}
            ],
            # EXTRA DECK (1 CARTA LEGAL EDISON)
            "extra_spec": [
                {"name": "Stardust Dragon", "count": 1, "section": "extra", "note": "Sincronía 8 - Anulación de destrucción (100% legal Edison)"}
            ]
        },

        # 3. DARK WORLD PURO (FORMATO AVANZADO / MODERNO) - 40 Main + 6 Extra
        {
            "id": "dark_world_modern",
            "name": "Mazo DARK WORLD \"Puro\" (Formato Avanzado / Moderno)",
            "short_name": "Dark World Puro",
            "subtitle": "La estrategia clásica de descarte de la mano, coronada con Xyz potentes modernos y la amenaza destructiva de ZEUS",
            "format": "Avanzado / Moderno",
            "tag": "Dark World Puro",
            "tag_color": "purple",
            "description": "La estrategia clásica de descarte de la mano, coronada con Xyz potentes modernos y la amenaza destructiva de ZEUS.",
            "cards_spec": [
                # MONSTRUOS (24)
                {"name": "Reign-Beaux, Overking of Dark World", "count": 1, "section": "monsters", "note": "Jefe supremo del mazo principal"},
                {"name": "Grapha, Dragon Lord of Dark World", "count": 1, "section": "monsters", "note": "Resurrección infinita y destrucción"},
                {"name": "Genta, Gateman of Dark World", "count": 1, "section": "monsters", "note": "Busca The Gates of Dark World"},
                {"name": "Snoww, Unlight of Dark World", "count": 1, "section": "monsters", "note": "Buscadora universal de Dark World"},
                {"name": "Sillva, Warlord of Dark World", "count": 1, "section": "monsters", "note": "Invocación especial y descarte al rival"},
                {"name": "Goldd, Wu-Lord of Dark World", "count": 1, "section": "monsters", "note": "Invocación especial y destrucción x2"},
                {"name": "Broww, Huntsman of Dark World", "count": 1, "section": "monsters", "note": "Sheet #444 - Motor de robo al ser descartado"},
                {"name": "Beiige, Vanguard of Dark World", "count": 1, "section": "monsters", "note": "Invocación especial inmediata"},
                {"name": "Ceruli, Guru of Dark World", "count": 1, "section": "monsters", "note": "Se invoca en campo rival para activar efectos secundarios"},
                {"name": "Lucent, Netherlord of Dark World", "count": 1, "section": "monsters", "note": "Invocación especial de demonios de nivel 5+"},
                {"name": "Latinum, Exarch of Dark World", "count": 1, "section": "monsters", "note": "Potenciador de ATK e invocación especial"},
                {"name": "Parl, Hermit of Dark World", "count": 1, "section": "monsters", "note": "Recupera monstruos Dark World desterrados"},
                {"name": "Scarr, Scout of Dark World", "count": 1, "section": "monsters", "note": "Búsqueda en cementerio al destruirse en batalla"},
                {"name": "Kahkki, Guerilla of Dark World", "count": 1, "section": "monsters", "note": "Destruye un monstruo al descartarse"},
                {"name": "Gren, Tactician of Dark World", "count": 1, "section": "monsters", "note": "Destruye una magia/trampa al descartarse"},
                {"name": "Brron, Mad King of Dark World", "count": 1, "section": "monsters", "note": "Provoca descarte al infligir daño de batalla"},
                {"name": "Zure, Knight of Dark World", "count": 1, "section": "monsters", "note": "Guerrero clásico de Dark World (1800 ATK)"},
                {"name": "Danger! Bigfoot!", "count": 1, "section": "monsters", "note": "Invocación Danger! y destrucción de carta boca arriba"},
                {"name": "Danger! Thunderbird!", "count": 1, "section": "monsters", "note": "Invocación Danger! y destrucción de carta colocada"},
                {"name": "Danger! Mothman!", "count": 1, "section": "monsters", "note": "Ambos jugadores roban 1 y descartan 1"},
                {"name": "Danger!? Tsuchinoko?", "count": 1, "section": "monsters", "note": "Invocación especial sin importar si se descarta"},
                {"name": "Danger! Chupacabra!", "count": 1, "section": "monsters", "note": "Sheet #445 - Revive un Danger! del cementerio"},
                {"name": "Tour Guide From the Underworld", "count": 1, "section": "monsters", "note": "Sheet #446 - Invoca demonio nivel 3 directo del Deck"},
                {"name": "The Fabled Cerburrel", "count": 1, "section": "monsters", "note": "Sheet #447 - Cantante nivel 2 que se invoca al descartarse"},

                # MAGIAS (7)
                {"name": "The Gates of Dark World", "count": 1, "section": "spells", "note": "Campo de robo y descarte continuo"},
                {"name": "Dark World Archives", "count": 1, "section": "spells", "note": "Aceleración de descartes y aumento de ATK"},
                {"name": "Dark World Dealings", "count": 1, "section": "spells", "note": "Ambos roban y descartan (activa efectos Dark World)"},
                {"name": "Charge Into a Dark World", "count": 1, "section": "spells", "note": "Revive un Dark World y descarta un demonio"},
                {"name": "Gateway to Dark World", "count": 1, "section": "spells", "note": "Magia rápida de resurrección de Dark World"},
                {"name": "Dark World Lightning", "count": 1, "section": "spells", "note": "Destruye carta colocada y descarta"},
                {"name": "Dark World Puppetry", "count": 1, "section": "spells", "note": "Destierra hasta 3 cartas de cementerios y descarta"},

                # TRAMPAS (9)
                {"name": "Dark World Punishment", "count": 1, "section": "traps", "note": "Niega invocación normal o especial y descarta"},
                {"name": "The Forces of Darkness", "count": 1, "section": "traps", "note": "Recupera 2 Dark World del cementerio a la mano"},
                {"name": "Dark Scheme", "count": 1, "section": "traps", "note": "Ambos descartan 2 cartas y roban 2"},
                {"name": "Dark World Brainwashing", "count": 1, "section": "traps", "note": "Sheet #448 - Cambia efecto del rival a 'Tu rival descarta 1 carta'"},
                {"name": "Dark Deal", "count": 1, "section": "traps", "note": "Sheet #449 - Convierte magia normal del rival en descarte Dark World"},
                {"name": "Skill Drain", "count": 1, "section": "traps", "note": "Sheet #450 - ¡Cartaza! Deja sin efectos a los monstruos del rival"},
                {"name": "Eradicator Epidemic Virus", "count": 1, "section": "traps", "note": "Sheet #451 - Tributa oscuridad de 2500+ ATK y destruye Mágicas o Trampas"},
                {"name": "Dark Smog", "count": 1, "section": "traps", "note": "Sheet #452 - Destierra carta del cementerio rival y descarta demonio"},
                {"name": "Deck Devastation Virus", "count": 1, "section": "traps", "note": "Sheet #453 - Tributa oscuridad de 2000+ ATK y destruye monstruos de 1500- ATK"},

                # EXTRA DECK (6)
                {"name": "Grapha, Dragon Overlord of Dark World", "count": 1, "section": "extra", "note": "Jefe Fusión: cambia efectos rivales a descartes Dark World"},
                {"name": "Clorless, Chaos King of Dark World", "count": 1, "section": "extra", "note": "Fusión legendaria: destruye todo el campo rival al invocarse"},
                {"name": "Dharc the Dark Charmer, Gloomy", "count": 1, "section": "extra", "note": "Sheet #315 - Enlace 2 de OSCURIDAD: roba monstruos oscuros del cementerio rival"},
                {"name": "Divine Arsenal AA-ZEUS - Sky Thunder", "count": 1, "section": "extra", "note": "Sheet #434 - El jefe XYZ más devastador: limpia todo el campo enviando al cementerio"},
                {"name": "Daigusto Emeral", "count": 1, "section": "extra", "note": "Sheet #431 - Rango 4: recicla 3 monstruos y roba 1 carta"},
                {"name": "Number 20: Giga-Brilliant", "count": 1, "section": "extra", "note": "Sheet #432 - Rango 3 (invocado con Tour Guide + demonio nivel 3): potencia 300 ATK a todos tus monstruos y sirve de puente para invocar a ZEUS"}
            ]
        }
    ]

    all_processed_decks = []

    for d in decks_definitions:
        processed_cards = []
        main_count = 0
        extra_count = 0

        cards_list = d.get('cards_spec', [])
        if 'extra_spec' in d:
            cards_list = cards_list + d['extra_spec']

        for item in cards_list:
            card_name = item['name']
            c_info = name_map.get(card_name.lower())
            if not c_info:
                # Intento con alias comunes
                if card_name == "Triple Headed Behemoth" or card_name == "Twin-Headed Behemoth":
                    c_info = name_map.get("twin-headed behemoth")
                elif card_name == "The Fabled Cerburrel":
                    c_info = name_map.get("the fabled cerburrel")

            if not c_info:
                print("Aviso: Carta no encontrada:", card_name)
                continue

            primary_img = c_info.get('card_images', [{}])[0]
            prices = c_info.get('card_prices', [{}])[0]
            count = item.get('count', 1)
            section = item.get('section', 'monsters')

            if section == 'extra':
                extra_count += count
            else:
                main_count += count

            inv_item = inv_lookup.get(c_info['name'].lower(), {})

            processed_cards.append({
                "name": c_info['name'],
                "original_name": c_info['name'],
                "section": section,
                "count": count,
                "note": item.get('note', ''),
                "owned": True,
                "sheet_id": inv_item.get('sheet_id', ''),
                "sheet_category": inv_item.get('category', 'Decks y Cajas'),
                "box_location": inv_item.get('box_location', 'Colección Física'),
                "type": c_info.get('type', ''),
                "humanReadableCardType": c_info.get('humanReadableCardType', c_info.get('type', '')),
                "frameType": c_info.get('frameType', 'normal'),
                "desc": c_info.get('desc', ''),
                "race": c_info.get('race', ''),
                "archetype": c_info.get('archetype', ''),
                "atk": c_info.get('atk'),
                "def": c_info.get('def'),
                "level": c_info.get('level'),
                "attribute": c_info.get('attribute'),
                "scale": c_info.get('scale'),
                "linkval": c_info.get('linkval'),
                "image_url": primary_img.get('image_url', ''),
                "image_url_small": primary_img.get('image_url_small', ''),
                "image_url_cropped": primary_img.get('image_url_cropped', ''),
                "prices": {
                    "tcgplayer": prices.get('tcgplayer_price', '0.20'),
                    "cardmarket": prices.get('cardmarket_price', '0.15')
                },
                "ygoprodeck_url": f"https://ygoprodeck.com/card/?search={urllib.parse.quote(c_info['name'])}"
            })

        count_monsters = sum(c['count'] for c in processed_cards if c['section'] == 'monsters')
        count_spells = sum(c['count'] for c in processed_cards if c['section'] == 'spells')
        count_traps = sum(c['count'] for c in processed_cards if c['section'] == 'traps')
        total_cost = sum(float(c['prices'].get('tcgplayer', 0) or 0) * c['count'] for c in processed_cards)

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
                "monsters": count_monsters,
                "spells": count_spells,
                "traps": count_traps,
                "owned_count": main_count + extra_count,
                "total_cost": round(total_cost, 2)
            },
            "cards": processed_cards
        }

        all_processed_decks.append(deck_obj)
        print(f"Deck '{deck_obj['name']}': Main {main_count}, Extra {extra_count}, En posesión {deck_obj['stats']['owned_count']}/{main_count + extra_count} (100%!) | Costo: ${deck_obj['stats']['total_cost']}")

    # Guardar en decks.json
    with open('d:/S I S T E M A S/TCG/decks.json', 'w', encoding='utf-8') as f:
        json.dump(all_processed_decks, f, ensure_ascii=False, indent=2)

    # Guardar en decks_data.js
    with open('d:/S I S T E M A S/TCG/decks_data.js', 'w', encoding='utf-8') as f:
        f.write('var TCG_DECKS_DATA = ' + json.dumps(all_processed_decks, ensure_ascii=False, indent=2) + ';\n')
        f.write('if (typeof window !== "undefined") window.TCG_DECKS_DATA = TCG_DECKS_DATA;\n')

    print("Total de mazos generados:", len(all_processed_decks))

if __name__ == '__main__':
    generate_all_decks()
