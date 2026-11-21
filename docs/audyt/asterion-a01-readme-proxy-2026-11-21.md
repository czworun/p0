# A-01 — README: deklaracja o braku kodu a obecność skryptów PROXY

**Data:** 2026-11-21  
**Repozytorium:** `czworun/p0`  
**Benchmark:** `main` @ `ff5345f50f509ff95fafcd1e4b28ce64b388eb1c`  
**Powiązanie:** rozwinięcie A-01 z pierwotnego indeksu z 2026-11-20. Nie jest nowym znaleziskiem i nie zmienia jego numeracji.

## Ustalenie

README PL/EN/ES kategorycznie twierdzi, że repozytorium nie zawiera kodu. W `docs/replikacja/` znajdują się trzy skrypty Python PROXY:

- `estrada-proxy-deepseek-v1.py` — 13 814 B; commit z 2026-11-15 opisuje zamrożenie skryptu PROXY przed wykonaniem.
- `estrada-proxy-deepseek-v2.py` — 14 458 B; commit z 2026-11-15 opisuje trzy uzgodnione poprawki, kontrolę zakresu PASS i sanity 107/107, a następnie zamrożenie przed wykonaniem.
- `tau10-proxy-deepseek-v1.py` — 6 936 B; commit z 2026-11-16 opisuje zamrożenie skryptu PROXY przed wykonaniem.

Są to pliki zawierające kod Python, a nie tylko opisy algorytmów.

## Rozróżnienie metodologiczne

Metodyka Z3 mówi: między modelami przekazuje się specyfikacje i wyniki, nigdy kod. Sam fakt przechowywania zamrożonego skryptu PROXY w repo nie dowodzi jeszcze, że kod przekazano między wykonawcami lub że wynik uzyskano przez niedozwolone współdzielenie implementacji. Historia commitów wskazuje, że skrypty przygotowano jako PROXY i zamrożono przed wykonaniem przez Leszka.

Potwierdzony problem jest więc dokumentacyjny: absolutne zdanie „w repozytorium nie ma kodu” jest niezgodne ze stanem repo. Osobną decyzją laboratorium pozostaje precyzyjna klasyfikacja PROXY względem Z3 i konwencji „szopy”.

## Propozycja redakcyjna

Zastąpić absolutną deklarację zdaniem rozróżniającym:
- brak kanonicznych, wspólnych implementacji filarów;
- obecność jawnie oznaczonych, historycznych skryptów PROXY jako artefaktów konkretnych wykonań;
- nadrzędność specyfikacji i wyników nad kodem przy ustalaniu statusów.

Nie zmieniam README ani metodyki. Nie przenoszę i nie usuwam skryptów.

## Status

**A-01:** 🔍 potwierdzona sprzeczność dokumentacyjna; klasyfikacja PROXY względem Z3 wymaga rozstrzygnięcia.  
**Zakres zmian:** wyłącznie ten raport na gałęzi audytowej. `main` i gałąź testowa pozostają nietknięte.
