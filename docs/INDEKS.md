# INDEKS repo czworun/p0: mapa i stan prac

> Wpis porządkowy 2026-11-25 (na rozkaz właściciela, po pełnej lustracji repo). Cel tego pliku: jedno miejsce, w którym widać co jest już wykonane, aby nie dublować pracy. Zasada Z0 w mocy: nic nie usuwamy, bindi trzymają ścieżki. Aktualizacja: po każdej rundzie warsztatu.

## Statusy rejestrów (przeczytaj najpierw)

- **docs/wyniki.md** (245338 B) i **docs/zlecenia.md** (710751 B): stan ZAMROŻONY na erze 11cs (2026-11-19). Nagłówki statusowe na początku obu plików pochodzą z wpisu porządkowego 2026-11-25.
- Od 2026-11-22 rozliczenia rund prowadzone są w dzienniku roboczym warsztatu poza repo; repo pozostaje powierzchnią publikacji.
- Kolejki w zlecenia.md z ery 11cs są częściowo rozliczone (np. T15-1, T15-2). Przed podjęciem tematu sprawdź w tym INDEKSie, czy nie został już wykonany.
- Wersje specek (mvp-01 v0_1 do v0_9, mvp-02 v0_1 do v1_4 z v1_2r i dwoma aneksami) to celowa księga bindów, nie duplikaty.

## Spis prac per linia

**TAU / SERC / TETRA-20 (korpus replikowany)**: wyniki ✅ w [docs/wyniki.md](wyniki.md) (m.in. r_∞ = 0.12383, deficyt kątowy 7.356103°, SERC R₄, widmo ikosaedru 19-dim). Pnie dokumentów: [docs/korzenie/](korzenie/) (25 dokumentów: TAU 1.7.2, SERC 4.2, TETRA-20 0.2.4, Defect 0.8, Stalk 1.2, Lattice 1.2, Memory 3.7, Net 6.1, Wave 6.1, Flow 5.3, Estrada 0.7/0.8 i inne). Sesje TAU-10 do TAU-15/N1: sekcje rund (r11cq, r11cs i wcześniejsze) w docs/wyniki.md. Referencja N7: [docs/N7_RAB_referencja.txt](N7_RAB_referencja.txt).

**P0-Estrada**: T1 do T4 ✅ po czterech replikantach (Vibe, Asterion, Claude, DeepSeek); pakiet Z1: [docs/replikacja/](replikacja/) (p0-estrada-z1-*).

**MVP-01**: zamknięty; spece v0_1 do v0_9 (księga bindów).

**MVP-02**: ZAMKNIĘTY 2026-11-24. K3 = ✅ (trzy zgodne implementacje na bindzie v1.4: słój warsztatu w14, PROXY DeepSeek (wykonanie u właściciela w Colab), rerun Claude). Wynik rachunku transportowego: KILL = WYNIK TYPOWY, F_r = 0/20; wrażliwość third NIESPRAWIEDLIWIONE, twothirds NIEROZSTRZYGALNY. Bind v1.4: [docs/mvp-02-spec-v1_4.md](mvp-02-spec-v1_4.md), SHA-256 1240d31aaccd6f8be20f7750535924abd394f743d7cd43786a74ca4e54e13409, razem z aneksem v0_4 SHA-256 820231b0197a081bf498b2c4b36b95bbb381175f313724491f32d61ce5d10151; commit na main 3b885670. Receipty: gałęzie audytowe (sekcja niżej). Pole 3 (teza fizyczna, H_b): DOMKNIĘTE 2026-11-25 decyzją właściciela jako ODRZUCONE (❌), po wyniku testu K3 WYNIK TYPOWY (KILL, F_r = 0/20, trzy zgodne implementacje na bindzie v1.4); motyw właściciela: droga była cenniejsza niż potwierdzenie hipotezy (Z0). Erraty kandydackie (W-2, W-3) odłożone do ewentualnej v1.5.

**P0-AI (KOMÓRKA)**: spec [docs/p0-ai-komorka-spec-v0_1-DRAFT.md](p0-ai-komorka-spec-v0_1-DRAFT.md), kolejka wg jej §9: (1) atak zewnętrzny na DRAFT: trzy zlecenia gotowe w repo, ale NIGDY nieprzekazane wykonawcom (relay należy do właściciela): [docs/wklejka-claude-p0ai-atak.md](wklejka-claude-p0ai-atak.md) (rygor definicyjny), [docs/wklejka-asterion-p0ai-atak.md](wklejka-asterion-p0ai-atak.md) (geometria), [docs/wklejka-deepseek-p0ai-atak.md](wklejka-deepseek-p0ai-atak.md) (konwencje i warstwa symboliczna); (2) rozliczenie ataków plus erraty zbiorcze; (3) zamrożenie v1.0 z bindem (K6: publikacja hasha przed rachunkami); (4) implementacje Z1 plus replikacja TAU-9-TOY 🔍; (5) rozliczenie bramek B1 do B6. Sesja TAU-9 (decyzje D1 do D8) w repo istnieje wyłącznie w DRAFT i wklejkach. Przed v1.0 decyzja właściciela: nośnik doktryny P₀ (środek ikosaedru kontra centroidy K₄; napięcie z H-DEF-20).

**H-DEF (linia geometryczno-fizykalna, równoległa)**: dziennik H-DEF-1 do H-DEF-21: [docs/warsztat/h-def-dziennik-zbiorczy-2026-11-16.md](warsztat/h-def-dziennik-zbiorczy-2026-11-16.md) (plik wykonawcy, wpięty verbatim 2026-11-25). Zwięzle: pierścienie 5K₄ ze szczeliną δ = 7.356103° (tożsamą z deficytem rejestrowym TAU), holonomia nieprzemienna SO(3), pary antypodalne znoszą holonomię dokładnie, rozłączność poziomów jako aksjomat (H-DEF-18), przekaz A (zmiana skali +1.48%) kontra B-krawędź (reszta holonomiczna zależna od drogi, mediana 8.10°). Otwarty rachunek: dwupoziomowa symulacja A vs B. Statusy w dzienniku wg legendy wykonawcy; wg konwencji warsztatu to 🔍 i 💡, a ✅ dopiero po replikacji Z1.

**Uśpione i zamrożone**: E18c uśpiony; TAU-9-TOY 🔍 (replikacja po zamrożeniu v1.0); K6 i K8 w mocy.

## Mapa repo (skrót)

- root: [README.md](../README.md) (+ [README.en.md](../README.en.md), [README.es.md](README.es.md)), [ZAPROSZENIE.md](../ZAPROSZENIE.md) (osobne zaproszenie na laboratoria równoległe, nie kopia README), [GLOSSARY.md](../GLOSSARY.md) (żywy), LICENSE (CC BY 4.0), .github/ISSUE_TEMPLATE.
- docs/: [metodyka.md](metodyka.md) (Z0 do Z3, protokół zespołu modeli), [replikacja.md](replikacja.md) (jak wykonać Z1), [INDEKS.md](INDEKS.md) (ten plik), wyniki.md, zlecenia.md (zamrożone, patrz wyżej), N7_RAB_referencja.txt, spece mvp-01 (9 pozycji), spece mvp-02 (12 pozycji w tym v1_2r i dwa aneksy), p0-ai-komorka-spec-v0_1-DRAFT.md, wklejki (16: zlecenia i raporty wykonawców er 11cc do 11cx), korzenie/ (25 dokumentów pnia), replikacja/ (12 plików: pakiety Z1, PROXY), warsztat/ (TAU-8: sieć 12 sąsiadów; dziennik H-DEF), seminarium/ (1 pozycja), img/ (1 svg).
- Styl: pliki warsztatu (ten INDEKS, metodyka, spece, rejestry) bez em-dash; pliki wykonawców wpijane verbatim z ich własną typografią, bez redakcji.

## Gałęzie audytowe (receipty wykonawcze)

21 gałęzi audit/*: receipty dostaw wykonawców; nigdy nie scalane do main, nieusuwalne (Z0). Cztery najnowsze, z zamknięcia MVP-02:

- audit/claude-mvp02-v14-rerun-2026-11-24 (commit 8e9f27977f432a9d1ef4713633b993511b81a281)
- audit/deepseek-mvp02-v14-proxy-2026-11-24 (commit a267bd516f7f8eb7668bf20fb04f2c2e194acafb)
- audit/claude-mvp02-v13-z1-2026-11-23 (commit 74a0f29c0ebe97cdfe1d3a889f4ed4bc32a0a733)
- audit/warsztat-mvp02-v14-rerun-2026-11-24 (commit 29a5db3417dabfdebcc9649e7ecb11cb3ce9147f)

Reguła nazewnicza: audit/\<wykonawca\>-\<linia\>-\<temat lub bind\>-\<RRRR-MM-DD\>.

## Reguły porządkowe (Z2)

1. Nic nie usuwamy ani nie przenosimy: bindi (spece, wklejki, gałęzie) trzymają ścieżki i SHA-256.
2. Wersje specek to księga bindów, nie duplikaty do czyszczenia.
3. Pliki wykonawców wpijamy verbatim, bez redakcji.
4. Ten INDEKS aktualizujemy po każdej rundzie warsztatu.
