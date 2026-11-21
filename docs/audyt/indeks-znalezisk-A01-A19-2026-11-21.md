# Indeks znalezisk audytu Asteriona — A-01 do A-19

**Data aktualizacji:** 2026-11-21  
**Repozytorium:** \`czworun/p0\`  
**Baza źródłowa:** \`main\` @ \`ff5345f50f509ff95fafcd1e4b28ce64b388eb1c\`  
**Gałąź audytowa:** \`audit/asterion-continuation-2026-11-20\`

## Zasada odczytu

Indeks zbiera punkty, których treść i status można potwierdzić z raportów audytowych dostępnych w repozytorium. Nie odtwarzam brakujących opisów z samej numeracji. Pozycje oznaczone „nieodtworzone” wymagają porównania z wcześniejszym indeksem/dziennikiem Asteriona lub Vibe'a.

Statusy w tym indeksie opisują stan audytu, nie statusy matematyczne P₀. Żaden punkt sam w sobie nie zmienia statusu korzenia ani wyniku.

## Indeks

| ID | Temat | Status audytu | Następny krok |
|---|---|---|---|
| A-01 | Treść wcześniejszego znaleziska niedostępna w obecnym materiale audytu | ⚪ nieodtworzone | Odzyskać z poprzedniego indeksu/dziennika |
| A-02 | Metadane \`docs/wyniki.md\`: deklarowany snapshot do tury 38 nie odpowiada całemu późniejszemu korpusowi wpisów | 🔍 otwarte | Ustalić datę/zakres snapshotu i zsynchronizować nagłówek |
| A-03 | Treść wcześniejszego znaleziska niedostępna | ⚪ nieodtworzone | Odzyskać z poprzedniego indeksu/dziennika |
| A-04 | Treść wcześniejszego znaleziska niedostępna | ⚪ nieodtworzone | Odzyskać z poprzedniego indeksu/dziennika |
| A-05 | Treść wcześniejszego znaleziska niedostępna | ⚪ nieodtworzone | Odzyskać z poprzedniego indeksu/dziennika |
| A-06 | Treść wcześniejszego znaleziska niedostępna | ⚪ nieodtworzone | Odzyskać z poprzedniego indeksu/dziennika |
| A-07 | Treść wcześniejszego znaleziska niedostępna | ⚪ nieodtworzone | Odzyskać z poprzedniego indeksu/dziennika |
| A-08 | Treść wcześniejszego znaleziska niedostępna | ⚪ nieodtworzone | Odzyskać z poprzedniego indeksu/dziennika |
| A-09 | Sprzeczność architektoniczna: Scalar deklaruje gałąź Origins i jest tak ujęty w PILLARS-TABLE, Defect deklaruje absorpcję do Centroid; Axis również wymaga rozstrzygnięcia pozycji | 🔍 nierozstrzygnięte | Oddzielić absorpcję treści/wyników od zmiany pozycji architektonicznej; decyzja autora |
| A-10 | Treść wcześniejszego znaleziska niedostępna | ⚪ nieodtworzone | Odzyskać z poprzedniego indeksu/dziennika |
| A-11 | Treść wcześniejszego znaleziska niedostępna | ⚪ nieodtworzone | Odzyskać z poprzedniego indeksu/dziennika |
| A-12 | Treść wcześniejszego znaleziska niedostępna | ⚪ nieodtworzone | Odzyskać z poprzedniego indeksu/dziennika |
| A-13 | README PL/EN/ES zawierają nieaktualne lub nadmiernie szerokie opisy zawartości, zakresu korzeni i rejestru; częściowo wiąże się z A-02, ale ma osobny wymiar informacyjny | 🔍 otwarte | Zsynchronizować opisy językowe z aktualnym drzewem i snapshotem |
| A-14 | Szablony Issue nie zbierają wszystkich wymaganych przez metodykę danych: brak jawnego pola źródła specyfikacji (plik, §) w zgłoszeniu replikacji i statusu weryfikacji w erracie | 🔍 otwarte | Przygotować propozycję aktualizacji szablonów na gałęzi audytowej |
| A-15 | Glosariusz: osobny wpis P₀-Applications już dodany; osobnego P₀-Origins nadal brak, choć Philosophy wskazuje Dział IV jako jedyny tekst programu Origins | 🟡 częściowo rozwiązane | Rozstrzygnąć, czy potrzebny jest osobny wpis Origins |
| A-16 | \`ZAPROSZENIE.md\` obiecuje, że „wszystko jest jawne”, w tym nieprzycięty dziennik, mimo że repo zawiera snapshot publiczny, a dokumenty robocze są prowadzone w warsztacie | 🔍 potwierdzone | Zawęzić deklarację do materiałów rzeczywiście opublikowanych w repo |
| A-17 | README zapewnia, że wszystkie specyfikacje są publiczne i samowystarczalne; korpus jawnie odwołuje się do zależności/źródeł poza repo, a replikacja wymaga STOP przy brakach | 🔍 potwierdzone | Zastąpić absolutną deklarację kryterium kompletności dla konkretnej specyfikacji |
| A-18 | „Zero rozbieżności merytorycznych” w adnotacji PILLARS-TABLE-1 ma nieostry zakres; prawdopodobnie dotyczy tylko pięciu stempli wersji, nie całej architektury | 🔍 niejednoznaczność | Doprecyzować zakres zdania; nie rozstrzygać nim konfliktu Scalar–Defect |
| A-19 | README PL/EN/ES mówi, że repo nie zawiera kodu, lecz \`docs/replikacja/\` zawiera trzy skrypty Python PROXY zamrożone przed wykonaniem; ich status względem Z3 i „szopy” nie jest opisany | 🔍 potwierdzona sprzeczność dokumentacyjna; kwalifikacja Z3 otwarta | Ustalić, czy PROXY jest wyjątkiem, i poprawić opisy README/metodyki zgodnie z decyzją |

## Ważne rozróżnienia

1. **A-02 i A-13 są powiązane, ale nie tożsame.** A-02 dotyczy metadanych i zakresu samego snapshotu \`docs/wyniki.md\`; A-13 dotyczy szerszej, wielojęzycznej prezentacji zawartości repo.
2. **A-09 nie rozstrzyga się przez liczenie dokumentów.** Należy rozdzielić przejęcie treści, przejęcie wyników i zmianę klasyfikacji architektonicznej.
3. **A-16, A-17 i A-19 są trzema różnymi problemami.** A-16 dotyczy publiczności dziennika, A-17 — kompletności specyfikacji, A-19 — faktycznej obecności kodu i jego klasyfikacji.
4. **A-19 nie jest automatycznie stwierdzeniem naruszenia Z3.** Potwierdzony jest fakt obecności skryptów; decyzji wymaga ich metodologia przekazania i status archiwalny.

## Podstawa indeksu

- \`docs/audyt/asterion-continuation-2026-11-20.md\` — A-16, A-17, A-18 oraz aktualizacje A-02/A-13, A-09, A-14, A-15.
- \`docs/audyt/asterion-defect-flow-hilbert-2026-11-20.md\` — kontrola matematyczna i źródłowa Defect/Flow/Hilbert.
- \`docs/audyt/asterion-net-memory-2026-11-20.md\` — spójność definicji Net/Memory i testowalność H-MEM-1.
- \`docs/audyt/asterion-scalar-centroid-tau-2026-11-20.md\` — mosty operatorowe Scalar/Centroid/TAU.
- \`docs/audyt/asterion-orient02a-2026-11-20.md\` — odtworzenie widma ORIENT-02-A.
- \`docs/audyt/asterion-a19-brak-kodu-2026-11-21.md\` — A-19.

**Ograniczenie:** A-01, A-03–A-08 i A-10–A-12 są jawnie oznaczone jako nieodtworzone. Ten indeks nie udaje kompletnej rekonstrukcji ich treści. Po odzyskaniu wcześniejszego indeksu należy podmienić te placeholdery, zachowując identyfikatory i historię statusów.
