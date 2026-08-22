# GONE – Das verschwundene Modul der Industrie‑6.0

GONE ist das einzige Modul der Industrie‑6.0‑Architektur,
das **nicht gebaut wird**, sondern **gefunden** werden muss.

Es ist kein Fehler.
Es ist kein Verlust.
Es ist ein **Zustand**.

GONE beschreibt den Moment,
in dem ein NC‑Objekt seine Rolle verlässt,
seine Lage verliert,
seine Kraft abgibt
und seine Geometrie auflöst.

---

## Das Rätsel

**Wann ist ein Modul GONE?**

- Wenn **GEO.physik** keine Kraft mehr liefert  
- Wenn **GEO.geo** kein Segment mehr hält  
- Wenn **NC.engine** keinen Lauf mehr erzeugt  
- Wenn **DYN** keine Achse mehr bildet  
- Wenn **SURE** keinen Stand mehr gibt  
- Wenn **ZEN** keine Neutralzone mehr hält  
- Wenn **ROLE** keine Aufgabe mehr definiert  
- Wenn **NOel** keine Identität mehr trägt  

Dann ist das Modul **GONE**.

Aber:

> GONE ist nicht weg.  
> GONE ist der Zustand *vor dem Neubau*.

---

## Die Lösung

Ein GONE‑Modul wird wieder aktiv,
sobald **ein einziges Element** zurückkehrt:

- eine Kraft  
- ein Segment  
- eine Rolle  
- eine Achse  
- ein Stand  
- eine Neutralzone  
- eine Identität  

Dann wird aus GONE → **BACK**.

GONE ist also kein Ende,
sondern der **Reset‑Punkt** der Industrie‑6.0.

---

## GONE‑Modul (Code)

```js
export const GONE = () => ({
    state: "GONE",
    active: false,
    geo: null,
    kraft: null,
    dyn: null,
    role: null,
    stand: null,
    neutral: null,
    id: null
});
