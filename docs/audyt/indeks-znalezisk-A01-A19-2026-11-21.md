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
| A-01 | README: deklaracja o braku kodu a obecność zamrożonych skryptów proxy w `docs/replikacja/` | 🔍 potwierdzone | README PL/EN/ES; `docs/replikacja/` | Rozróżnić brak wspólnego kodu badawczego od obecności zamrożonych proxy |
| A-02 | Metadane \`docs/wyniki.md\`: deklarowany snapshot do tury 38 nie odpowiada całemu późniejszemu korpusowi wpisów | 🔍 otwarte | Ustalić datę/zakres snapshotu i zsynchronizować nagłówek |
| A-03 | `PILLARS-TABLE-1.md` jako historyczny, niepełny indeks | 🔍 potwierdzone | `docs/korzenie/PILLARS-TABLE-1.md` | Opracować aktualny indeks; nie traktować tabeli 1 jako kompletnego stanu bieżącego |
| A-04 | Niespójna klasyfikacja Alchemy: filar / gałąź | 🔍 otwarte | `GLOSSARY.md`, adnotacja korzenia Alchemy, `PILLARS-TABLE-1.md`, verbatim źródła | Ujednolicić pojęcie architektoniczne decyzją właściciela korpusu |
| A-05 | Błędne odnośniki do `docs/korzenie/PILLARS-TABLE.md` | 🔍 potwierdzone | Osiem aktywnych linków w sześciu korzeniach; właściwy plik to `PILLARS-TABLE-1.md` | Poprawić odnośniki w osobnej, zatwierdzonej zmianie |
| A-06 | Niejednoznaczny zakres terminu SSOT | 🔍 otwarte | README, tabela filarów, rejestr wyników i dokumenty korzeni | Nazwać osobno SSOT dla pnia formalnego, architektury/wersji i wyników |
| A-07 | Szablony GitHub Issues nie pokrywają wymaganych pól metodyki | 🔍 otwarte | `.github/ISSUE_TEMPLATE/zgloszenie-replikacji.md`, `errata-pytanie.md`, `docs/replikacja.md`, `docs/metodyka.md` | Dodać źródło specyfikacji (plik + §) i status weryfikacji erraty |
| A-08 | Treść wcześniejszego znaleziska niedostępna | ⚪ nieodtworzone | Odzyskać z poprzedniego indeksu/dziennika |
| A-09 | Sprzeczność architektoniczna: Scalar deklaruje gałąź Origins i jest tak ujęty w PILLARS-TABLE, Defect deklaruje absorpcję do Centroid; Axis również wymaga rozstrzygnięcia pozycji | 🔍 nierozstrzygnięte | Oddzielić absorpcję treści/wyników od zmiany pozycji architektonicznej; decyzja autora |
| A-10 | Transfer Flow → Defect i Memory → Net ma charakter selektywny, nie pełnego zastąpienia źródeł | 🔍 otwarte dokumentacyjnie | Flow §5.5.1, §5.7, §7.5 i Defect §12; Memory v0.3.7 i Net v0.6.1; raporty Defect↔Flow↔Hilbert oraz Net↔Memory | Zachować źródła i dodać jawne odsyłacze do nieprzeniesionych specyfikacji |
| A-11 | Brak osobnego korzenia P₀-Origins | 🔍 wyjaśnione; decyzja architektoniczna otwarta | Origins jest programem opisanym w Philosophy; Scalar pozostaje odrębną gałęzią | Zdecydować, czy wystarczy jawne objaśnienie w Philosophy, czy potrzebny osobny wpis glosariusza |
| A-12 | Rozbieżność liczby filarów: 7/8 | 🔍 otwarte | Philosophy i Experiments | Uzgodnić licznik i zakres pojęcia „filar” |
| A-13 | README PL/EN/ES zawierają nieaktualne lub nadmiernie szerokie opisy zawartości, zakresu korzeni i rejestru; częściowo wiąże się z A-02, ale ma osobny wymiar informacyjny | 🔍 otwarte | Zsynchronizować opisy językowe z aktualnym drzewem i snapshotem |
| A-14 | Szablony Issue nie zbierają wszystkich wymaganych przez metodykę danych: brak jawnego pola źródła specyfikacji (plik, §) w zgłoszeniu replikacji i statusu weryfikacji w erracie | 🔍 otwarte | Przygotować propozycję aktualizacji szablonów na gałęzi audytowej |
| A-15 | Glosariusz: osobny wpis P₀-Applications już dodany; osobnego P₀-Origins nadal brak, choć Philosophy wskazuje Dział IV jako jedyny tekst programu Origins | 🟡 częściowo rozwiązane | Rozstrzygnąć, czy potrzebny jest osobny wpis Origins |
| A-16 | \`ZAPROSZENIE.md\` obiecuje, że „wszystko jest jawne”, w tym nieprzycięty dziennik, mimo że repo zawiera snapshot publiczny, a dokumenty robocze są prowadzone w warsztacie | 🔍 potwierdzone | Zawęzić deklarację do materiałów rzeczywiście opublikowanych w repo |
| A-17 | README zapewnia, że wszystkie specyfikacje są publiczne i samowystarczalne; korpus jawnie odwołuje się do zależności/źródeł poza repo, a replikacja wymaga STOP przy brakach | 🔍 potwierdzone | Zastąpić absolutną deklarację kryterium kompletności dla konkretnej specyfikacji |
| A-18 | „Zero rozbieżności merytorycznych” w adnotacji PILLARS-TABLE-1 ma nieostry zakres; prawdopodobnie dotyczy tylko pięciu stempli wersji, nie całej architektury | 🔍 niejednoznaczność | Doprecyzować zakres zdania; nie rozstrzygać nim konfliktu Scalar–Defect |
| A-19 | Status źródła `p0_dowody.ipynb` | 🟡 odzyskane, archiwalne, do decyzji o wpięciu | Informacja przekazana przez Leszka: plik odzyskany i zweryfikowany jako tożsamy z przywołaniem w STALK | Decyzja o wpięciu do repo należy do właściciela korpusu; indeks nie dodaje ani nie modyfikuje notebooka |

## Ważne rozróżnienia

1. **A-02 i A-13 są powiązane, ale nie tożsame.** A-02 dotyczy metadanych i zakresu samego snapshotu \`docs/wyniki.md\`; A-13 dotyczy szerszej, wielojęzycznej prezentacji zawartości repo.
2. **A-09 nie rozstrzyga się przez liczenie dokumentów.** Należy rozdzielić przejęcie treści, przejęcie wyników i zmianę klasyfikacji architektonicznej.
3. **A-16, A-17 i A-19 są odrębnymi problemami: publiczność dziennika, kompletność specyfikacji i status notebooka STALK. A-01 dotyczy opisu skryptów PROXY.** A-16 dotyczy publiczności dziennika, A-17 — kompletności specyfikacji, A-19 — faktycznej obecności kodu i jego klasyfikacji.
4. **A-01 nie jest automatycznie stwierdzeniem naruszenia Z3.** Potwierdzony jest fakt obecności skryptów; decyzji wymaga ich metodologia przekazania i status archiwalny.


## Podstawa indeksu

- [A-01 — README i skrypty PROXY](asterion-a01-readme-proxy-2026-11-21.md) — rozwinięcie pierwotnego A-01; kwalifikacja Z3 pozostaje otwarta.
- [A-05 — błędne odnośniki do tabeli filarów](asterion-a05-bledne-odnosniki-2026-11-21.md) — osiem aktywnych odnośników w sześciu korzeniach.

Pierwotny indeks A-01–A-19 z 2026-11-20 (commit `97ed0e313a46a407cfabd49b297e3525948c6129`) jest źródłem zachowanej numeracji. Cztery raporty poniżej znajdują się na osobnych gałęziach audytowych (nie są scalone z gałęzią tego indeksu):

- [Kontynuacja — A-16, A-17, A-18 oraz aktualizacje A-02/A-13, A-09, A-14, A-15](https://github.com/czworun/p0/blob/audit/asterion-continuation-2026-11-20/docs/audyt/asterion-continuation-2026-11-20.md)
- [Defect ↔ Flow ↔ Hilbert — audyt matematyczny i źródłowy](https://github.com/czworun/p0/blob/audit/asterion-defect-flow-hilbert-2026-11-20/docs/audyt/asterion-defect-flow-hilbert-2026-11-20.md)
- [Net ↔ Memory — spójność definicji i testowalność H-MEM-1](https://github.com/czworun/p0/blob/audit/asterion-net-memory-2026-11-20/docs/audyt/asterion-net-memory-2026-11-20.md)
- [Scalar ↔ Centroid ↔ TAU — mosty operatorowe i asymptotyka](https://github.com/czworun/p0/blob/audit/asterion-scalar-centroid-tau-2026-11-20/docs/audyt/asterion-scalar-centroid-tau-2026-11-20.md)
- [ORIENT-02-A — audyt kompresji kanonicznej](https://github.com/czworun/p0/blob/audit/asterion-orient02a-2026-11-20/docs/audyt/asterion-orient02a-2026-11-20.md)
- [A-01 — README: deklaracja o braku kodu a obecność skryptów PROXY](https://github.com/czworun/p0/blob/audit/asterion-continuation-2026-11-20/docs/audyt/asterion-a19-brak-kodu-2026-11-21.md)

**Ograniczenie:** A-08 pozostaje jawnie oznaczony jako „do identyfikacji”, zgodnie z pierwotnym indeksem z 2026-11-20. Nie rekonstruuję go przez domysł. Po odzyskaniu wcześniejszego indeksu należy podmienić te placeholdery, zachowując identyfikatory i historię statusów.
