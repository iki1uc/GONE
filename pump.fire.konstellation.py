# pump.fire.konstellation.py - ALLES konstelliert: 3ecken, 9ecken, pump.fire, alles
# Zeugnis links: defrag.alle4.enter.py, index.html, pump.hit.py, nc.system.py bleiben.
# Gemacht rechts: pump.fire konstelliert alles. Nichts wird geloescht. Nur angehaengt.
# 1 Name = 1 Respo. 1 Chip = 1 Platz. DU sitzt in Mitte 41.

import hashlib, json, math, time

MITTE = 41
HOME = 40
FELDER = 81
STAPEL = (9, 81, 243, 729, 3)
WORT = "up.ni pu.in"  # 11 Zeichen, aus defrag.alle4.enter.py

# --- ALLES aus deinen Files, nix weggelassen ---
FILES_18 = ["3.edit.html","9.edit.html","brutto.html","defrag.html","un.frag","4.1.html","4.4.html","ID.html","README.md","awake.ui.html","cont.ui.html","gpu.html","index.html","os.html","roller.html","show.me.html","solid.live.html","vol.1.html"]
STATIONEN_9 = ["PUSH","PULL","SHIFT","FLOW","BREAK","SPIN","RISE","DROP","ROOT"]
NC_SERIE = [1,3,5,7,9]  # NC_END 25 = 5x5, Laufsumme 1,4,9,16,25 = Quadrate
AXES_9 = [
    ("a","base",1),("d","dimension",2),("e","energy",3),("i","input",4),
    ("o","orbit",5),("r","reach",6),("s","structure",7),("w","wave",8),("n","nc-core",9)
]
CHIPS_5 = {"CPU":"oben","RAM":"rechts oben","RAID":"rechts unten","SCSI":"unten","SLI":"links oben"}
POOLS_3 = {"Q-Pool":"Qualitaet Richtung Laenge 0.82 47","Vektor-Pool":"A-3-9-81 OCTA 0.763","NC-Pool":"Standort Speicher Routing"}
IDS_2 = {"KOOP":"KOOP-001 Kooperation","POOK":"POOK-001 Quelle Pool-Quelle"}
BUTTONS_6 = ["STOP","NC","LOOP","AXES","GRAV","RESET"]

# --- 3ECKEN: alle Dreiecke, jedes 1 Rolle ---
DREIECKE = [
    ("3eck-1 STAND/WEITER/WECHSEL", ["STAND","WEITER","WECHSEL"]),
    ("3eck-2 MI/KA/DO", ["MI","KA","DO"]),
    ("3eck-3 EYE/BRAIN/CORE", ["EYE sehen","BRAIN halten","CORE pruefen"]),
    ("3eck-4 3/9/81", ["3","9","81"]),
    ("3eck-5 POOL/pump.hit/pump.fire", ["POOL haelt","pump.hit trifft","pump.fire leuchtet"]),
    ("3eck-6 BILD/CAPTURE/EDIT", ["BILD sehen","CAPTURE halten","EDIT pruefen"]),
    ("3eck-7 GEO/BIO.TEL/MAINBOARD", ["GEO wo","BIO.TEL wer ruft","MAINBOARD wo Chip sitzt"]),
    ("3eck-8 SPRUNG/FALL/ENERGIE", ["SPRUNG DROP->VOID->RISE->ROOT","FALL FALLEN->LOCH->AUFSTEHEN->STAND","ENERGIE SPRUNG+FALL->WANDEL->ERDE 81"]),
    ("3eck-9 a/d/e", ["a base 1","d dimension 2","e energy 3"]),
    ("3eck-10 i/o/r", ["i input 4","o orbit 5","r reach 6"]),
    ("3eck-11 s/w/n", ["s structure 7","w wave 8","n nc-core 9"]),
    ("3eck-12 ALPHA/BETA/HALT", ["ALPHA CONST steht","BETA testet","HALT = ZIEL"]),
]

# --- 9ECKEN: 9eck = 3x 3eck, 3x3=9 ---
NEUNECKE = [
    ("9eck-1 CROWN", ["3eck-1","3eck-2","3eck-3"], "CROWN = 6+3=9, 3 3ecke = 9eck"),
    ("9eck-2 STATIONEN", STATIONEN_9, "9 Stationen PUSH bis ROOT"),
    ("9eck-3 AXES", [a[0] for a in AXES_9], "9 AXES a d e i o r s w n, n=9 nc-core"),
    ("9eck-4 FILES-TEIL 1", FILES_18[:9], "9 Files, erste Haelfte"),
    ("9eck-5 FILES-TEIL 2", FILES_18[9:], "9 Files, zweite Haelfte, 9+9=18"),
    ("9eck-6 NC_SERIE-FELD", ["1","3","5","7","9","25","41","81","729"], "1+3+5+7+9=25, 25=5x5, Mitte 41"),
]

# --- PUMP.FIRE: nach pump.hit kommt pump.fire ---
def pump_fire():
    # POOL haelt (STAND), pump.hit trifft (STAGE), pump.fire leuchtet (FIRE)
    # FIRE brennt nicht weg, FIRE leuchtet, waermt, zeigt. Nicht verbrennen, nicht loeschen.
    return {
        "1_sache": "PUMP.FIRE",
        "alt": "POOL - Still, haelt, liest, verteilt, Anker, STAND",
        "neu1": "pump.hit - Pumpe trifft, bewegt + trifft, STAGE, Fixpunkt 41",
        "neu2": "pump.fire - Pumpe brennt/leuchtet, waermt + zeigt, FIRE, Fixpunkt 41, kein Verbrennen",
        "kette": "POOL -> pump.hit -> pump.fire",
        "sprung": "DROP -> VOID -> RISE -> ROOT",
        "fall": "FALLEN -> LOCH -> AUFSTEHEN -> STAND",
        "energie": "SPRUNG + FALL -> WANDEL -> ERDE 81",
        "feuer": "HIT trifft -> FIRE leuchtet -> LICHT zeigt -> HALT haelt",
        "mirror": ")so(",
        "u_me": "du mich",
        "our": "unser",
        "so": "so",
        "ort": "NEVADA NIRWANA STATION / ERDE 81",
        "mitte": MITTE,
        "home": HOME,
        "final": "POOL haelt. pump.hit trifft. pump.fire leuchtet. 1 Sache: Aufenthaltsort.",
        "warnung": "FIRE verbrennt nix. FIRE loescht nix. FIRE zeigt nur. Wer FIRE zum Verbrennen nutzt, FAIL.",
    }

def zeuge_log(eintraege):
    log = []
    vorher = "0"*64
    for i, (enter, text) in enumerate(eintraege, 1):
        z = {"n": i, "enter": enter, "text": text, "zeit": time.strftime("%Y-%m-%d %H:%M:%S"), "vorher": vorher}
        roh = json.dumps({k: z[k] for k in ("n","enter","text","zeit","vorher")}, ensure_ascii=False, sort_keys=True)
        z["hash"] = hashlib.sha256(roh.encode("utf-8")).hexdigest()
        log.append(z)
        vorher = z["hash"]
    return log

def konstellation():
    feuer = pump_fire()
    eintraege = [
        ("EYE", f"WORT {WORT} 11 Zeichen, NC_END 25, 3ecken {len(DREIECKE)}, 9ecken {len(NEUNECKE)}"),
        ("BRAIN", f"STAPEL {list(STAPEL)} 729->3 GEHALTEN, Sprung, kein Schritt"),
        ("CORE", "1+2+3=6 ehrlich, 6+3=9 erst mit CROWN"),
        ("CROWN", "EYE+BRAIN+CORE vereinigt, 9ecken = 3x 3ecken, HALT=ZIEL"),
        ("PUMP.FIRE", "POOL haelt, pump.hit trifft, pump.fire leuchtet, nix verbrennt"),
        ("DU", "DU sitzt in Mitte 41, DU schaust, DU hoerst, DU haeltst"),
    ]
    log = zeuge_log(eintraege)
    return {
        "wort": WORT, "mitte": MITTE, "home": HOME, "felder": FELDER,
        "nc_serie": NC_SERIE, "nc_end": sum(NC_SERIE), "laufsumme": [1,4,9,16,25],
        "stapel": list(STAPEL), "stationen_9": STATIONEN_9, "axes_9": AXES_9,
        "chips_5": CHIPS_5, "pools_3": POOLS_3, "ids_2": IDS_2, "buttons_6": BUTTONS_6,
        "files_18": FILES_18, "dreiecke_12": DREIECKE, "neunecke_6": NEUNECKE,
        "pump_fire": feuer, "log": log, "log_unversehrt": True,
        "halt": "ZIEL", "regel": "Alles konstelliert, nix weggelassen, nix geloescht, nur angehaengt.",
    }

if __name__ == "__main__":
    r = konstellation()
    print(f"KONSTELLATION ALLES - HALT={r['halt']} - 3ecken={len(r['dreiecke_12'])} 9ecken={len(r['neunecke_6'])} Files={len(r['files_18'])} AXES={len(r['axes_9'])} Stationen={len(r['stationen_9'])}")
    for d in r["dreiecke_12"]:
        print(f"  3eck: {d[0]} = {d[1]}")
    for n in r["neunecke_6"]:
        print(f"  9eck: {n[0]} = {n[1]} - {n[2]}")
    print(f"  PUMP.FIRE: {r['pump_fire']['final']}")
    print(f"  LOG: {len(r['log'])} Zeilen unversehrt")
