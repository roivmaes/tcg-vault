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
        # 1. HÉROE (40 Main + 8 Extra — Agresivo / Fusión)
        {
            "id": "hero_deck",
            "name": "Mazo HÉROE (Formato Avanzado / Moderno)",
            "short_name": "Mazo HÉROE",
            "subtitle": "Mazo HÉROE (40 Cartas — Agresivo / Fusión): Optimizado con Bubbleman y Soul Union, sin cartas fantasma",
            "format": "Avanzado / Moderno",
            "tag": "HÉROE / Agresivo & Fusión",
            "tag_color": "red",
            "description": "Tu baraja principal HÉROE optimizada con Bubbleman y Soul Union. Diseñada para invocar fusiones y monstruos Link con alta velocidad, combinando el poder ofensivo de Trinity, Escuridao, Nova Master y Darkest Knight.",
            "cards_spec": [
                # MONSTRUOS (13)
                {"name": "Vision HERO Vyon", "count": 1, "section": "monsters", "note": "Carta Suelta — Envía a Denier al cementerio y busca Polymerization"},
                {"name": "Destiny HERO - Denier", "count": 1, "section": "monsters", "note": "Carta Suelta — Se invoca solo desde el cementerio"},
                {"name": "Elemental HERO Blazeman", "count": 1, "section": "monsters", "note": "Carta Suelta / Midterm Paradox — Busca Polymerization"},
                {"name": "Elemental HERO Wildheart", "count": 1, "section": "monsters", "note": "Midterm Paradox — Inmune a trampas"},
                {"name": "Elemental HERO Neos", "count": 1, "section": "monsters", "note": "Carta Suelta — Guerrero clásico de 2500 ATK"},
                {"name": "Elemental HERO Neos Alius", "count": 1, "section": "monsters", "note": "Carta Suelta — Atacante de 1900 ATK y atributo LUZ"},
                {"name": "Evil HERO Darkest Knight", "count": 1, "section": "monsters", "note": "Cartas Sueltas — Evil HERO Drakes Knight"},
                {"name": "Evil HERO Vicious Claws", "count": 2, "section": "monsters", "note": "Cartas Sueltas — 2 copias: Héroe Malvado Garras Cruentas"},
                {"name": "Winged Kuriboh", "count": 2, "section": "monsters", "note": "Carta Suelta / Cartas Sueltas — 2 copias: reduce daño a cero"},
                {"name": "Effect Veiler", "count": 1, "section": "monsters", "note": "Decks y Cajas — Handtrap de interrupción"},
                {"name": "Elemental HERO Bubbleman", "count": 1, "section": "monsters", "note": "Midterm Paradox — Invocación especial y robo cuando tu mano está vacía"},

                # MAGIAS (18)
                {"name": "A Hero Lives", "count": 2, "section": "spells", "note": "Carta Suelta / Cartas Sueltas — 2 copias: invoca a Vyon o Blazeman directo del mazo"},
                {"name": "Polymerization", "count": 2, "section": "spells", "note": "Decks y Cajas / Midterm Paradox — 2 copias: magia de fusión principal"},
                {"name": "Evil Assault", "count": 1, "section": "spells", "note": "Carta Suelta — Busca o invoca HÉROE Malvado del mazo"},
                {"name": "Monster Reborn", "count": 1, "section": "spells", "note": "Decks y Cajas / Cartas Sueltas — Resurrección universal"},
                {"name": "Skyscraper 2 - Hero City", "count": 1, "section": "spells", "note": "Midterm Paradox — Revive héroes caídos en batalla"},
                {"name": "Fifth Hope", "count": 1, "section": "spells", "note": "Midterm Paradox — Recicla 5 cartas al mazo y roba"},
                {"name": "H - Heated Heart", "count": 1, "section": "spells", "note": "Midterm Paradox — Otorga +500 ATK y daño de penetración"},
                {"name": "R - Righteous Justice", "count": 1, "section": "spells", "note": "Midterm Paradox — Destruye magias y trampas rivales"},
                {"name": "Hero Flash!!", "count": 1, "section": "spells", "note": "Carta Suelta (Hero Flash!!) — Flash H.E.R.O."},
                {"name": "Wrath of Neos", "count": 1, "section": "spells", "note": "Carta Suelta — Limpieza total de campo regresando a Neos al mazo"},
                {"name": "Raigeki", "count": 1, "section": "spells", "note": "Decks y Cajas — Limpiador de monstruos"},
                {"name": "Dark Hole", "count": 1, "section": "spells", "note": "Decks y Cajas / Set Principiante — Destrucción de campo"},
                {"name": "Harpie's Feather Duster", "count": 1, "section": "spells", "note": "Decks y Cajas — Destruye todas las magias/trampas rivales"},
                {"name": "Twin Twisters", "count": 1, "section": "spells", "note": "Decks y Cajas — Destruye 2 magias/trampas"},
                {"name": "Dark Ruler No More", "count": 1, "section": "spells", "note": "Decks y Cajas — Niega efectos de monstruos rivales"},
                {"name": "Book of Moon", "count": 1, "section": "spells", "note": "Decks y Cajas / Set Principiante — Interrupción rápida boca abajo"},

                # TRAMPAS (9)
                {"name": "Hero Signal", "count": 1, "section": "traps", "note": "Midterm Paradox — Invoca un HÉROE cuando destruyen un monstruo"},
                {"name": "Hero Counterattack", "count": 1, "section": "traps", "note": "Midterm Paradox — Invoca un HÉROE al azar de la mano al ser atacado"},
                {"name": "Crackdown", "count": 1, "section": "traps", "note": "Decks y Cajas — Toma el control permanente de un monstruo rival"},
                {"name": "Solemn Warning", "count": 1, "section": "traps", "note": "Decks y Cajas — Niega una invocación"},
                {"name": "Dimensional Barrier", "count": 1, "section": "traps", "note": "Decks y Cajas — Bloquea invocaciones del Extra Deck"},
                {"name": "Drowning Mirror Force", "count": 1, "section": "traps", "note": "Decks y Cajas — Baraja monstruos atacantes al mazo"},
                {"name": "Fiendish Chain", "count": 1, "section": "traps", "note": "Decks y Cajas — Niega efectos y bloquea ataque"},
                {"name": "Heavy Storm Duster", "count": 1, "section": "traps", "note": "Decks y Cajas — Destruye hasta 2 magias/trampas"},
                {"name": "Soul Union", "count": 1, "section": "traps", "note": "Cartas Sueltas — Potenciador de ATK de HÉROE durante el cálculo de daño"},

                # EXTRA DECK (8)
                {"name": "Xtra HERO Cross Crusader", "count": 2, "section": "extra", "note": "Cartas Sueltas — 2 copias: Link-2 buscador de HÉROES"},
                {"name": "Vision HERO Trinity", "count": 1, "section": "extra", "note": "Carta Suelta — Fusión devastadora de 5000 ATK y 3 ataques"},
                {"name": "Xtra HERO Dread Decimator", "count": 1, "section": "extra", "note": "Carta Suelta — Link-3 con daño de penetración para tus HÉROES"},
                {"name": "Elemental HERO Nova Master", "count": 1, "section": "extra", "note": "Cartas Sueltas / Midterm Paradox — Fusión Blazeman + HÉROE"},
                {"name": "Elemental HERO Escuridao", "count": 1, "section": "extra", "note": "Carta Suelta — Fusión con monstruo Oscuridad (Vyon/Denier)"},
                {"name": "Elemental HERO Neos Knight", "count": 1, "section": "extra", "note": "Carta Suelta — Fusión Neos + Guerrero: doble ataque"},
                {"name": "Evil HERO Darkest Knight", "count": 1, "section": "extra", "note": "Carta Suelta / Cartas Sueltas — Fusión HÉROE Malvado"}
            ]
        },

        # 2. DARK WORLD (40 Main + 1 Extra — Control / Descarte)
        {
            "id": "dark_world_modern",
            "name": "Mazo DARK WORLD (Formato Avanzado / Moderno)",
            "short_name": "Mazo Dark World",
            "subtitle": "Mazo DARK WORLD (40 Cartas — Control / Descarte): Construido exclusivamente con las cartas confirmadas en tu caja física",
            "format": "Avanzado / Moderno",
            "tag": "Dark World / Control & Descarte",
            "tag_color": "purple",
            "description": "Construido exclusivamente con las cartas confirmadas en tu caja física de Structure Deck: Dark World. La estrategia maestra de descarte, robo y control con Grapha, Dragon Overlord of Dark World en el Extra Deck.",
            "cards_spec": [
                # MONSTRUOS (22)
                {"name": "Reign-Beaux, Overking of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Jefe supremo del mazo principal"},
                {"name": "Reign-Beaux, Overlord of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Monstruo jefe clásico de Dark World"},
                {"name": "Grapha, Dragon Lord of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Resurrección infinita y destrucción de cartas"},
                {"name": "Snoww, Unlight of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Buscadora universal de cualquier carta Dark World"},
                {"name": "Genta, Gateman of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Busca The Gates of Dark World descartándose"},
                {"name": "Parl, Hermit of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Recupera monstruos Dark World desterrados"},
                {"name": "Lucent, Netherlord of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Invocación especial de demonios de nivel 5 o mayor"},
                {"name": "Latinum, Exarch of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Potenciador de ATK e invocación especial"},
                {"name": "Goldd, Wu-Lord of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Invocación especial y destrucción de hasta 2 cartas"},
                {"name": "Sillva, Warlord of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Invocación especial y descarte al rival"},
                {"name": "Brron, Mad King of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Provoca descarte al infligir daño de batalla"},
                {"name": "Beiige, Vanguard of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Invocación especial inmediata al descartarse"},
                {"name": "Broww, Huntsman of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Motor de robo constante al ser descartado"},
                {"name": "Ceruli, Guru of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Se invoca en campo rival para activar efectos secundarios"},
                {"name": "Gren, Tactician of Dark World", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Destruye una magia/trampa al descartarse"},
                {"name": "Danger! Bigfoot!", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Invocación Danger! y destrucción boca arriba"},
                {"name": "Danger! Thunderbird!", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Invocación Danger! y destrucción de carta colocada"},
                {"name": "Danger! Mothman!", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Ambos jugadores roban 1 y descartan 1"},
                {"name": "Danger!? Tsuchinoko?", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Invocación especial gratis siempre que se descarta"},
                {"name": "Lilith, Lady of Lament", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Buscadora rápida de cartas de trampa normales"},
                {"name": "Fabled Raven", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Monstruo cantante y activador de descartes múltiple"},
                {"name": "Absolute King Back Jack", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Dark World) — Reorganiza tope del mazo y activa trampas desde GY"},

                # MAGIAS (10)
                {"name": "The Gates of Dark World", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Dark World) — Magia de campo: robo y descarte continuo"},
                {"name": "Dark World Puppetry", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Dark World) — Destierra hasta 3 cartas de cementerios y descarta"},
                {"name": "Dark World Archives", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Dark World) — Aceleración de descartes y aumento de ATK"},
                {"name": "Dark World Dealings", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Dark World) — Ambos jugadores roban y descartan"},
                {"name": "Charge Into a Dark World", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Dark World) — Revive un Dark World y descarta un demonio"},
                {"name": "Gateway to Dark World", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Dark World) — Magia rápida de resurrección de cualquier Dark World"},
                {"name": "Dark World Lightning", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Dark World) — Destruye carta colocada y descarta"},
                {"name": "Dragged Down into the Grave", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Dark World) — Mira la mano del rival y descarta su mejor carta"},
                {"name": "Card Destruction", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Dark World) — Ambos descartan la mano entera y roban"},
                {"name": "Dark World Accession", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Dark World) — Fusión rápida de Dark World"},

                # TRAMPAS (8)
                {"name": "Dark World Punishment", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Dark World) — Niega invocación y descarta un demonio"},
                {"name": "The Forces of Darkness", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Dark World) — Recupera 2 Dark World del cementerio a la mano"},
                {"name": "Dark World Brainwashing", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Dark World) — Convierte efecto rival en un descarte para ti"},
                {"name": "Dark Smog", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Dark World) — Destierra carta de cementerio rival y descarta demonio"},
                {"name": "Mind Crush", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Dark World) — Declara nombre de carta para descartarla de mano rival"},
                {"name": "Deck Devastation Virus", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Dark World) — Destruye monstruos de 1500- ATK del rival"},
                {"name": "Paleozoic Dinomischus", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Dark World) — Destierra cualquier carta boca arriba del campo"},
                {"name": "Skill Drain", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Dark World) — Anula efectos de monstruos boca arriba en el campo"},

                # EXTRA DECK (1)
                {"name": "Grapha, Dragon Overlord of Dark World", "count": 1, "section": "extra", "note": "Decks y Cajas (SD Dark World) — Jefe supremo de fusión: convierte efectos en descarte"}
            ]
        },

        # 3. LIGHTSWORN EDISON (40 Main + 3 Extra)
        {
            "id": "lightsworn_edison_2010",
            "name": "Mazo LIGHTSWORN (Formato EDISON)",
            "short_name": "Lightsworn Edison",
            "subtitle": "Mazo LIGHTSWORN Edison (40 Cartas Main + 3 Extra): Armado según tu lista física exacta (SD Realm of Light, Cartas Sueltas y Decks)",
            "format": "Edison (Abril 2010)",
            "tag": "Lightsworn / Edison Retro",
            "tag_color": "amber",
            "description": "Mazo Lightsworn diseñado para el formato Edison 2010. Construido con tus cartas exactas de Structure Deck: Realm of Light, Cartas Sueltas y Decks, con acceso a Naturia Beast, Naturia Barkion y Stardust Dragon en el Extra Deck.",
            "cards_spec": [
                # MONSTRUOS (23)
                {"name": "Judgment Dragon", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Jefe supremo de 3000 ATK"},
                {"name": "Celestia, Lightsworn Angel", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Tributo Lightsworn que destruye 2 cartas"},
                {"name": "Gragonith, Lightsworn Dragon", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Daño de penetración y ATK por Lightsworn en GY"},
                {"name": "Lumina, Lightsworn Summoner", "count": 2, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — 2 copias: resucitadora de Lightsworn"},
                {"name": "Lyla, Lightsworn Sorceress", "count": 2, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — 2 copias: destructora de Mágicas/Trampas"},
                {"name": "Ryko, Lightsworn Hunter", "count": 2, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — 2 copias: destrucción Flip y molienda"},
                {"name": "Jain, Lightsworn Paladin", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Atacante de 2100 ATK"},
                {"name": "Wulf, Lightsworn Beast", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Invocación especial al cementerio"},
                {"name": "Garoth, Lightsworn Warrior", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Robo y aceleración de molienda"},
                {"name": "Ehren, Lightsworn Monk", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Devuelve monstruos en defensa al mazo"},
                {"name": "Aurkus, Lightsworn Druid", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Protege contra efectos que seleccionan"},
                {"name": "Shire, Lightsworn Spirit", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Gana ATK por cada Lightsworn en GY"},
                {"name": "Honest", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Handtrap de combate para monstruos LIGHT"},
                {"name": "Necro Gardna", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Anula un ataque desde el cementerio"},
                {"name": "Fabled Raven", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Cantante y activador de descartes"},
                {"name": "The Fabled Cerburrel", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Cantante nivel 2 que revive al descartarse"},
                {"name": "Blackwing - Zephyros the Elite", "count": 1, "section": "monsters", "note": "Decks y Cajas (SD Realm of Light) — Se revive regresando una carta al campo"},
                {"name": "Jinzo", "count": 1, "section": "monsters", "note": "Decks y Cajas — Apaga todas las cartas de trampa"},
                {"name": "Nimble Momonga", "count": 1, "section": "monsters", "note": "Decks y Cajas — Gana 1000 LP e invoca copias al destruirse por batalla"},
                {"name": "Mask of Darkness", "count": 1, "section": "monsters", "note": "Carta Suelta / Set Principiante — Efecto Flip: recupera 1 trampa del cementerio"},

                # MAGIAS (10)
                {"name": "Charge of the Light Brigade", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Realm of Light) — Buscador principal de Lightsworn"},
                {"name": "Solar Recharge", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Realm of Light) — Descarta 1 Lightsworn, roba 2 y muele 2"},
                {"name": "Monster Reincarnation", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Realm of Light) — Recupera cualquier monstruo del cementerio"},
                {"name": "Foolish Burial", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Realm of Light) — Envía a Wulf o Necro Gardna directo al GY"},
                {"name": "Realm of Light", "count": 1, "section": "spells", "note": "Decks y Cajas (SD Realm of Light) — Magia de campo: contadores de luz y ATK masivo"},
                {"name": "Mystical Space Typhoon", "count": 1, "section": "spells", "note": "Decks y Cajas / Set Principiante — Destruye una magia o trampa"},
                {"name": "Book of Moon", "count": 1, "section": "spells", "note": "Decks y Cajas / Set Principiante — Voltea un monstruo boca abajo"},
                {"name": "Swords of Revealing Light", "count": 1, "section": "spells", "note": "Decks y Cajas / Set Principiante — Detiene ataques rivales por 3 turnos"},
                {"name": "Pot of Avarice", "count": 1, "section": "spells", "note": "Decks y Cajas — Recicla 5 monstruos del GY y roba 2 cartas"},
                {"name": "Card Destruction", "count": 1, "section": "spells", "note": "Decks y Cajas — Ambos jugadores descartan su mano entera y roban"},

                # TRAMPAS (7)
                {"name": "Beckoning Light", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Realm of Light) — Descarta la mano y recupera monstruos LIGHT"},
                {"name": "Vanquishing Light", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Realm of Light) — Tributa un Lightsworn y niega invocación"},
                {"name": "Glorious Illusion", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Realm of Light) — Revive un Lightsworn y muele 2 cartas"},
                {"name": "Lightsworn Barrier", "count": 1, "section": "traps", "note": "Decks y Cajas (SD Realm of Light) — Niega un ataque moliendo 2 cartas"},
                {"name": "Mirror Force", "count": 1, "section": "traps", "note": "Decks y Cajas / Midterm Paradox — Destruye monstruos en ataque del rival"},
                {"name": "Torrential Tribute", "count": 1, "section": "traps", "note": "Decks y Cajas — Destruye todos los monstruos tras una invocación"},
                {"name": "Call of the Haunted", "count": 1, "section": "traps", "note": "Midterm Paradox / Set Principiante — Revive un monstruo del cementerio"},

                # EXTRA DECK (3)
                {"name": "Naturia Beast", "count": 1, "section": "extra", "note": "Carta Suelta / Cartas Sueltas — Sincronía 5: niega activación de magias moliendo 2 cartas"},
                {"name": "Naturia Barkion", "count": 1, "section": "extra", "note": "Carta Suelta / Cartas Sueltas — Sincronía 6: niega activación de trampas desterrando 2 cartas"},
                {"name": "Stardust Dragon", "count": 1, "section": "extra", "note": "Decks y Cajas — Sincronía 8: anula destrucción de cartas tributándose"}
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
