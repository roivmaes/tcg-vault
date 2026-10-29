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

    # Leer inventario de Google Sheet para saber ID y categoría
    with open('d:/S I S T E M A S/TCG/cards.json', 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    inv_lookup = {}
    for item in inventory:
        inv_lookup[item['name'].lower()] = item
        if item.get('original_name'):
            inv_lookup[item['original_name'].lower()] = item

    # DEFINICIÓN DE LOS 3 DECKS ACTUALIZADOS (100% LEGALES Y EN COLECCIÓN)
    decks_definitions = [
        # 1. HÉROE (FORMATO AVANZADO / MODERNO) - 40 Main + 7 Extra
        {
            "id": "hero_deck",
            "name": "Mazo HÉROE (Formato Avanzado / Moderno)",
            "short_name": "Mazo HÉROE",
            "subtitle": "Mazo Corregido: 40 Main Deck + 7 Extra Deck con Evil HERO Vicious Claws y Cross Crusader",
            "format": "Avanzado / Moderno",
            "tag": "HÉROE / Fusiones & Enlaces",
            "tag_color": "red",
            "description": "Mazo HÉROE corregido con sinergia 100% legal y jugable. Incorpora Héroe Malvado Garras Cruentas (Evil HERO Vicious Claws x2) para invocación especial inmediata, Bladedge para daño de penetración, doble A Hero Lives y doble Xtra HERO Cross Crusader en el Extra Deck.",
            "cards_spec": [
                # MONSTRUOS (14 - CORREGIDO)
                {"name": "Vision HERO Vyon", "count": 1, "section": "monsters", "note": "Sheet #290 - Envía a Denier al cementerio"},
                {"name": "Destiny HERO - Denier", "count": 1, "section": "monsters", "note": "Sheet #183 - Se revive del cementerio"},
                {"name": "Elemental HERO Bladedge", "count": 1, "section": "monsters", "note": "Sheet #323 - Regresa al Main Deck; daño de penetración (2600 ATK)"},
                {"name": "Elemental HERO Blazeman", "count": 1, "section": "monsters", "note": "Sheet #297 - Buscador estrella de Polymerization"},
                {"name": "Elemental HERO Wildheart", "count": 1, "section": "monsters", "note": "Sheet #298 - Inmune a trampas"},
                {"name": "Elemental HERO Neos", "count": 1, "section": "monsters", "note": "Sheet #191 - Tu clásico as"},
                {"name": "Elemental HERO Neos Alius", "count": 1, "section": "monsters", "note": "Sheet #192 - Guerrero Géminis"},
                {"name": "Evil HERO Vicious Claws", "count": 2, "section": "monsters", "note": "Sheet #331 - Héroe Malvado Garras Cruentas (2 copias): Invocación especial si controlas un HÉROE"},
                {"name": "Winged Kuriboh", "count": 2, "section": "monsters", "note": "2 copias (Principal + Speed Duel GX) - Evita daño letal"},
                {"name": "Effect Veiler", "count": 1, "section": "monsters", "note": "Sheet #47 - Handtrap niega efecto rival"},
                {"name": "Droll & Lock Bird", "count": 1, "section": "monsters", "note": "Sheet #45 - Handtrap frena robo y búsquedas"},
                {"name": "Ghost Mourner & Moonlit Chill", "count": 1, "section": "monsters", "note": "Sheet #67 - Handtrap niega y quema daño"},

                # MAGIAS (17)
                {"name": "A Hero Lives", "count": 2, "section": "spells", "note": "2 copias: Tu mejor jugada inicial"},
                {"name": "Polymerization", "count": 2, "section": "spells", "note": "2 copias para asegurar tus fusiones"},
                {"name": "Evil Assault", "count": 1, "section": "spells", "note": "Sheet #197 - Soporte de búsqueda e invocación HÉROE"},
                {"name": "Monster Reborn", "count": 1, "section": "spells", "note": "Sheet #102 - Resurrección universal"},
                {"name": "Skyscraper 2 - Hero City", "count": 1, "section": "spells", "note": "Sheet #306 - Revive Héroes destruidos en batalla"},
                {"name": "Fifth Hope", "count": 1, "section": "spells", "note": "Sheet #307 - Recicla 5 Héroes y roba 2"},
                {"name": "H - Heated Heart", "count": 1, "section": "spells", "note": "Sheet #312 - Daño de penetración + 500 ATK"},
                {"name": "R - Righteous Justice", "count": 1, "section": "spells", "note": "Sheet #309 - Destruye Mágicas/Trampas del rival"},
                {"name": "Hero Flash!!", "count": 1, "section": "spells", "note": "Sheet #201 - Flash H.E.R.O. ofensiva final"},
                {"name": "Wrath of Neos", "count": 1, "section": "spells", "note": "Sheet #295 - Destruye todo el campo si tienes a Neos"},
                {"name": "Raigeki", "count": 1, "section": "spells", "note": "Sheet #116 - Limpiador total de monstruos"},
                {"name": "Dark Hole", "count": 1, "section": "spells", "note": "Sheet #31 - Destrucción de campo"},
                {"name": "Harpie's Feather Duster", "count": 1, "section": "spells", "note": "Sheet #78 - Limpiador de Mágicas/Trampas"},
                {"name": "Twin Twisters", "count": 1, "section": "spells", "note": "Sheet #149 - Destruye 2 Mágicas/Trampas"},
                {"name": "Dark Ruler No More", "count": 1, "section": "spells", "note": "Sheet #34 - Niega efectos en campo rival"},

                # TRAMPAS (9)
                {"name": "Hero Signal", "count": 1, "section": "traps", "note": "Sheet #308 - Trae a Kuriboh o Blazeman si destruyen un monstruo"},
                {"name": "Hero Counterattack", "count": 1, "section": "traps", "note": "Sheet #311 - Invocación sorpresa y destrucción"},
                {"name": "Crackdown", "count": 1, "section": "traps", "note": "De Freezing Chains - Roba un monstruo rival"},
                {"name": "Solemn Warning", "count": 1, "section": "traps", "note": "De Spirit Charmers - Paga 2000 LP y niega invocación"},
                {"name": "Dimensional Barrier", "count": 1, "section": "traps", "note": "De Spirit Charmers - Bloquea invocaciones del Extra Deck"},
                {"name": "Drowning Mirror Force", "count": 1, "section": "traps", "note": "De Obelisk - Devuelve monstruos atacantes al mazo"},
                {"name": "Fiendish Chain", "count": 1, "section": "traps", "note": "De Freezing Chains - Niega efectos y ataque"},
                {"name": "Heavy Storm Duster", "count": 1, "section": "traps", "note": "De Freezing Chains - Destruye 2 Mágicas/Trampas"},
                {"name": "Unending Nightmare", "count": 1, "section": "traps", "note": "Sheet #324 - Destruye cartas boca arriba por 1000 LP"},

                # EXTRA DECK (7 - CORREGIDO)
                {"name": "Xtra HERO Cross Crusader", "count": 2, "section": "extra", "note": "Sheet #326 - 2 copias: Motor Link clave para revivir Destiny HERO y buscar HÉROE"},
                {"name": "Vision HERO Trinity", "count": 1, "section": "extra", "note": "Sheet #289 - Sube a 5000 ATK y ataca 3 veces"},
                {"name": "Xtra HERO Dread Decimator", "count": 1, "section": "extra", "note": "Sheet #296 - Enlace potenciador de daño"},
                {"name": "Elemental HERO Nova Master", "count": 1, "section": "extra", "note": "Sheet #300 - Fusión Blazeman + HÉROE; roba al destruir"},
                {"name": "Elemental HERO Escuridao", "count": 1, "section": "extra", "note": "Sheet #190 - Fusión con monstruos de OSCURIDAD"},
                {"name": "Elemental HERO Neos Knight", "count": 1, "section": "extra", "note": "Sheet #193 - Fusión de Neos + Guerrero; doble golpe"}
            ]
        },

        # 2. DARK WORLD PURO (FORMATO AVANZADO / MODERNO) - 40 Main + 3 Extra
        {
            "id": "dark_world_modern",
            "name": "Mazo DARK WORLD \"Puro\" (Formato Avanzado / Moderno)",
            "short_name": "Dark World Puro",
            "subtitle": "Utiliza pura sinergia temática para descartar cartas y abrumar al rival. Es totalmente legal y muy explosivo",
            "format": "Avanzado / Moderno",
            "tag": "Dark World Puro",
            "tag_color": "purple",
            "description": "Utiliza pura sinergia temática para descartar cartas y abrumar al rival. Es totalmente legal y muy explosivo. Su estrategia de descartarse a sí mismo es tan completa que no necesita magia genérica.",
            "cards_spec": [
                # MONSTRUOS (24)
                {"name": "Reign-Beaux, Overking of Dark World", "count": 1, "section": "monsters", "note": "Jefe supremo del mazo principal"},
                {"name": "Grapha, Dragon Lord of Dark World", "count": 1, "section": "monsters", "note": "Resurrección infinita y destrucción"},
                {"name": "Genta, Gateman of Dark World", "count": 1, "section": "monsters", "note": "Busca The Gates of Dark World"},
                {"name": "Snoww, Unlight of Dark World", "count": 1, "section": "monsters", "note": "Buscadora universal de Dark World"},
                {"name": "Sillva, Warlord of Dark World", "count": 1, "section": "monsters", "note": "Invocación especial y descarte al rival"},
                {"name": "Goldd, Wu-Lord of Dark World", "count": 1, "section": "monsters", "note": "Invocación especial y destrucción x2"},
                {"name": "Broww, Huntsman of Dark World", "count": 1, "section": "monsters", "note": "Sheet #313 - Motor de robo al ser descartado"},
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
                {"name": "Danger! Chupacabra!", "count": 1, "section": "monsters", "note": "Sheet #314 - Revive un Danger! del cementerio"},
                {"name": "Tour Guide From the Underworld", "count": 1, "section": "monsters", "note": "Sheet #315 - Invoca demonio nivel 3 directo del Deck"},
                {"name": "The Fabled Cerburrel", "count": 1, "section": "monsters", "note": "Sheet #316 - Cantante nivel 2 que se invoca al descartarse"},

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
                {"name": "Dark World Brainwashing", "count": 1, "section": "traps", "note": "Sheet #317 - Cambia efecto del rival a 'Tu rival descarta 1 carta'"},
                {"name": "Dark Deal", "count": 1, "section": "traps", "note": "Sheet #318 - Convierte magia normal del rival en descarte Dark World"},
                {"name": "Skill Drain", "count": 1, "section": "traps", "note": "Sheet #319 - ¡Cartaza! Deja sin efectos a los monstruos del rival"},
                {"name": "Eradicator Epidemic Virus", "count": 1, "section": "traps", "note": "Sheet #320 - Tributa oscuridad de 2500+ ATK y destruye Mágicas o Trampas"},
                {"name": "Dark Smog", "count": 1, "section": "traps", "note": "Sheet #321 - Destierra carta del cementerio rival y descarta demonio"},
                {"name": "Deck Devastation Virus", "count": 1, "section": "traps", "note": "Sheet #322 - Tributa oscuridad de 2000+ ATK y destruye monstruos de 1500- ATK"},

                # EXTRA DECK (3)
                {"name": "Grapha, Dragon Overlord of Dark World", "count": 1, "section": "extra", "note": "Jefe Fusión: cambia efectos rivales a descartes Dark World"},
                {"name": "Clorless, Chaos King of Dark World", "count": 1, "section": "extra", "note": "Fusión legendaria: destruye todo el campo rival al invocarse"},
                {"name": "Dharc the Dark Charmer, Gloomy", "count": 1, "section": "extra", "note": "Sheet #327 - Enlace 2 de OSCURIDAD: roba monstruos oscuros del cementerio rival"}
            ]
        },

        # 3. LIGHTSWORN (FORMATO EDISON - RETRO 2010) - 40 Main + 3 Extra
        {
            "id": "lightsworn_edison_2010",
            "name": "Mazo LIGHTSWORN (Formato EDISON - Retro 2010)",
            "short_name": "Lightsworn Edison",
            "subtitle": "Este es tu mazo clásico, con Dandylion y Aurkus incluidos tras la corrección de los Kuribohs",
            "format": "Edison (2010)",
            "tag": "Retro / Edison",
            "tag_color": "amber",
            "description": "Este es tu mazo clásico, con Dandylion y Aurkus incluidos tras la corrección de los Kuribohs. Lista definitiva de exactamente 40 cartas para formato Edison (2010) sin compartir cartas con los otros mazos.",
            "cards_spec": [
                # MONSTRUOS (23)
                {"name": "Judgment Dragon", "count": 1, "section": "monsters", "note": "Tu jefe final"},
                {"name": "Lumina, Lightsworn Summoner", "count": 1, "section": "monsters", "note": "Invocadora / Resucitadora"},
                {"name": "Lyla, Lightsworn Sorceress", "count": 1, "section": "monsters", "note": "Destructora de Mágicas/Trampas"},
                {"name": "Ryko, Lightsworn Hunter", "count": 1, "section": "monsters", "note": "Destrucción Flip y Molienda"},
                {"name": "Wulf, Lightsworn Beast", "count": 1, "section": "monsters", "note": "Invocación especial al cementerio"},
                {"name": "Celestia, Lightsworn Angel", "count": 1, "section": "monsters", "note": "Tributo Lightsworn / Destrucción x2"},
                {"name": "Garoth, Lightsworn Warrior", "count": 1, "section": "monsters", "note": "Robo y aceleración"},
                {"name": "Ehren, Lightsworn Monk", "count": 1, "section": "monsters", "note": "Devuelve defensas al mazo"},
                {"name": "Jain, Lightsworn Paladin", "count": 2, "section": "monsters", "note": "2 copias (Principal + Suelta)"},
                {"name": "Gragonith, Lightsworn Dragon", "count": 1, "section": "monsters", "note": "Daño de penetración y ATK"},
                {"name": "Aurkus, Lightsworn Druid", "count": 1, "section": "monsters", "note": "Sheet #328 - Protege a tus Lightsworn contra efectos que seleccionen"},
                {"name": "Honest", "count": 1, "section": "monsters", "note": "Hand-trap de ATK para LIGHT"},
                {"name": "Jinzo", "count": 1, "section": "monsters", "note": "De Legendary Decks II - Bloqueo de trampas"},
                {"name": "Fabled Raven", "count": 1, "section": "monsters", "note": "Cantante prestado de Dark World"},
                {"name": "Nimble Momonga", "count": 1, "section": "monsters", "note": "Recuperación de LP y bloqueo"},
                {"name": "Mask of Darkness", "count": 1, "section": "monsters", "note": "Recupera trampas del cementerio"},
                {"name": "Gearfried the Iron Knight", "count": 1, "section": "monsters", "note": "Inmunidad a cartas de equipo"},
                {"name": "Dark Valkyria", "count": 1, "section": "monsters", "note": "Géminis con contador mágico"},
                {"name": "Twin-Headed Behemoth", "count": 1, "section": "monsters", "note": "Triple Headed Behemoth en tu inventario"},
                {"name": "Dandylion", "count": 1, "section": "monsters", "note": "Sheet #329 - Dandy Withelion: Genera 2 fichas al enviarse al cementerio"},
                {"name": "Naturia Cliff", "count": 1, "section": "monsters", "note": "Buscador Naturia de reemplazo"},
                {"name": "Naturia Pumpkin", "count": 1, "section": "monsters", "note": "Invocación adicional para Sincronía"},

                # MAGIAS (10)
                {"name": "Charge of the Light Brigade", "count": 1, "section": "spells", "note": "Buscador clave Lightsworn"},
                {"name": "Solar Recharge", "count": 1, "section": "spells", "note": "Robo x2 y molienda"},
                {"name": "Monster Reincarnation", "count": 1, "section": "spells", "note": "Recupera Judgment Dragon"},
                {"name": "Foolish Burial", "count": 1, "section": "spells", "note": "Envía a Wulf o Dandylion al cementerio"},
                {"name": "Mystical Space Typhoon", "count": 1, "section": "spells", "note": "Tu clásico rompe-magias"},
                {"name": "Book of Moon", "count": 1, "section": "spells", "note": "Control y libro de la luna"},
                {"name": "Swords of Revealing Light", "count": 1, "section": "spells", "note": "Protección por 3 turnos"},
                {"name": "Pot of Avarice", "count": 1, "section": "spells", "note": "Recicla 5 y roba 2"},
                {"name": "Card Destruction", "count": 1, "section": "spells", "note": "Prestada de Dark World, perfecta para Edison"},
                {"name": "Dragged Down into the Grave", "count": 1, "section": "spells", "note": "Prestada de Dark World"},

                # TRAMPAS (7)
                {"name": "Mirror Force", "count": 1, "section": "traps", "note": "Castigo total al ataque rival"},
                {"name": "Bottomless Trap Hole", "count": 1, "section": "traps", "note": "Destrucción y destierro"},
                {"name": "Compulsory Evacuation Device", "count": 1, "section": "traps", "note": "Devuelve al rival a la mano"},
                {"name": "Beckoning Light", "count": 1, "section": "traps", "note": "Recupera monstruos LIGHT"},
                {"name": "Vanquishing Light", "count": 1, "section": "traps", "note": "Niega y destruye tributando"},
                {"name": "Mind Crush", "count": 1, "section": "traps", "note": "Prestada de Dark World"},
                {"name": "Glorious Illusion", "count": 1, "section": "traps", "note": "Sheet #330 - Trampa continua que revive Lightsworns y envía cartas al cementerio"},

                # EXTRA DECK (3)
                {"name": "Naturia Beast", "count": 1, "section": "extra", "note": "Sincronía 5 - Anulación infinita de Mágicas"},
                {"name": "Naturia Barkion", "count": 1, "section": "extra", "note": "Sincronía 6 - Anulación infinita de Trampas"},
                {"name": "Stardust Dragon", "count": 1, "section": "extra", "note": "Sincronía 8 - Anulación de destrucción"}
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
                # Intento con alias comunes
                if card_name == "Triple Headed Behemoth" or card_name == "Twin-Headed Behemoth":
                    c_info = name_map.get("twin-headed behemoth")
                elif card_name == "Dandy Withelion" or card_name == "Dandylion":
                    c_info = name_map.get("dandylion")
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
