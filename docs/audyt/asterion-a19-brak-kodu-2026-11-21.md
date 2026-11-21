# A-19 — nieprawdziwa deklaracja „w repozytorium nie ma kodu”

**Data:** 2026-11-21  
**Repozytorium:** \`czworun/p0\`  
**Baza:** \`main\` @ \`ff5345f50f509ff95fafcd1e4b28ce64b388eb1c\`  
**Gałąź audytowa:** \`audit/asterion-continuation-2026-11-20\`  
**Zakres:** README PL/EN/ES, \`docs/metodyka.md\`, inwentarz plików repozytorium i historia trzech skryptów PROXY.  
**Charakter:** ustalenie dokumentacyjne; bez zmiany Z3, statusów lub plików źródłowych.

## 1. Ustalenie

README w trzech językach zawiera kategoryczne stwierdzenie:

- PL, sekcja Z3: „W tym repozytorium nie ma kodu.”
- EN, sekcja Z3: „There is no code in this repository.”
- ES, sekcja Z3: „En este repositorio no hay código.”

To zdanie jest sprzeczne z aktualnym drzewem \`main\`. W \`docs/replikacja/\` znajdują się trzy pliki wykonywalne Python:

| Plik | Rozmiar | Ślad w historii |
|---|---:|---|
| \`estrada-proxy-deepseek-v1.py\` | 13 814 B | commit 2026-11-15: zamrożenie skryptu PROXY przed wykonaniem |
| \`estrada-proxy-deepseek-v2.py\` | 14 458 B | commit 2026-11-15: trzy uzgodnione poprawki, kontrola zakresu i sanity 107/107, zamrożenie przed wykonaniem |
| \`tau10-proxy-deepseek-v1.py\` | 6 936 B | commit 2026-11-16: skrypt PROXY zamrożony przed wykonaniem |

To nie są pliki tekstowe jedynie opisujące algorytm. Zawierają wykonywalne definicje funkcji, obliczenia macierzowe, testy numeryczne i importy bibliotek Python (m.in. NumPy; w skrypcie TAU-10 również SciPy).

## 2. Znaczenie dla Z3 — nie utożsamiać dwóch pytań

Metodyka Z3 mówi, że między modelami przekazuje się specyfikacje i wyniki, nie kod. Nie wynika z tego automatycznie, że każdy skrypt archiwalny jest naruszeniem niezależności rachunków. Historia tych plików opisuje je jako PROXY: kod i analizę przygotował DeepSeek, a wykonanie powierzono Leszkowi.

Należy jednak rozstrzygnąć dwie odrębne kwestie:

1. **Fakt repozytoryjny:** kod znajduje się w repozytorium — temu nie da się zaprzeczyć.
2. **Klasyfikacja metodologiczna:** czy skrypty PROXY są dopuszczalnym, jawnie oznaczonym wyjątkiem/artefaktem archiwalnym, czy też sposób ich przekazania wymaga doprecyzowania w Z3.

Nie przypisuję naruszenia Z3 bez decyzji laboratorium. Ustalenie A-19 dotyczy najpierw fałszywej deklaracji o zawartości repozytorium.

## 3. Druga niespójność: „szopa odroczona”

\`docs/metodyka.md\`, w części o konwencji drzewa, stwierdza, że kod nie rośnie na drzewie, a implementacje trafią do „szopy” — osobnego archiwum z metadanymi — które jest odroczone do czasu późniejszej decyzji. Obecność skryptów PROXY w \`docs/replikacja/\` oznacza, że archiwalne artefakty kodowe już znajdują się w repozytorium głównym, a nie w odrębnej szopie.

Możliwa jest sensowna interpretacja: skrypty PROXY są wyjątkiem, a „szopa” ma dotyczyć kanonicznych implementacji/pełnego archiwum. Tego rozróżnienia dokumentacja nie formułuje jednak wystarczająco jasno.

## 4. Proponowane rozstrzygnięcie redakcyjne

Nie przenoszę ani nie usuwam skryptów. Proponuję zastąpić absolutne zdanie w README opisem zgodnym z faktycznym stanem, np.:

> Repozytorium nie przechowuje kanonicznych implementacji filarów. Zawiera natomiast jawnie oznaczone, historyczne skrypty PROXY w \`docs/replikacja/\`, zachowane jako artefakty konkretnych wykonań. Nie zastępują one specyfikacji i nie stanowią samodzielnej podstawy statusów. Zasada Z3 dotyczy niezależności wykonawców: szczegółowy status skryptów PROXY jako wyjątku należy opisać osobno.

To jest propozycja dla autora/laboratorium, nie zmiana README dokonana w ramach audytu.

## 5. Status i dalszy test

**Status A-19:** 🔍 potwierdzona niezgodność dokumentacyjna; klasyfikacja PROXY względem Z3 wymaga decyzji laboratorium.

Do domknięcia pozostają:
- wskazanie, czy PROXY jest formalnym wyjątkiem od zasady „specyfikacje, nie kod”;
- wyjaśnienie, czy skrypty mają pozostać w \`docs/replikacja/\`, czy zostać objęte przyszłą konwencją „szopy”;
- ujednolicenie README PL/EN/ES po decyzji.

**Zakres zmian:** utworzono wyłącznie ten raport na gałęzi audytowej. \`main\`, pliki PROXY i gałąź \`audit/asterion-write-test-2026-11-20\` pozostają nietknięte.
