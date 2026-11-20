# Indeks znalezisk audytu Asteriona: A-01–A-19

Data zestawienia: 2026-11-20  
Repozytorium: `czworun/p0`  
Benchmark korpusu: `main` @ `ff5345f50f509ff95fafcd1e4b28ce64b388eb1c`  
Gałąź audytowa: `audit/asterion-orient02a-2026-11-20`  
Charakter: indeks rozpoznanych kwestii dokumentacyjnych, architektonicznych i matematycznych. Nie jest rejestrem statusów matematycznych ani decyzją kanoniczną.

## Jak czytać statusy

- **Potwierdzone** — obserwacja audytowa ma wskazane źródło i została sprawdzona.
- **Otwarte** — wymaga decyzji właściciela korpusu, doprecyzowania albo dalszego testu.
- **Częściowo rozwiązane** — część uwagi została uwzględniona, ale pozostaje decyzja lub dopowiedzenie.
- **Wyjaśnione** — audyt wyjaśnił zakres lub ograniczenie; nie oznacza automatycznej zmiany korpusu.
- **Do identyfikacji** — zachowany materiał audytowy nie pozwala mi bezpiecznie przypisać szczegółowego opisu do tego numeru. Nie uzupełniam go domysłem.

## Indeks

| ID | Temat | Stan audytowy | Źródło / zakres | Dalszy krok |
|---|---|---|---|---|
| A-01 | README: deklaracja o braku kodu a obecność zamrożonych skryptów proxy w `docs/replikacja/` | Potwierdzone | README PL/EN/ES; `docs/replikacja/` | Rozróżnić brak wspólnego kodu badawczego od obecności zamrożonych proxy |
| A-02 | Metadane `docs/wyniki.md`: nagłówek snapshotu nie odpowiada późniejszej zawartości | Potwierdzone; otwarte dokumentacyjnie | `docs/wyniki.md` — deklaracja do tury 38 przy późniejszych wpisach | Zsynchronizować datę i zakres snapshotu |
| A-03 | `PILLARS-TABLE-1.md` jako historyczny, niepełny indeks | Potwierdzone | `docs/korzenie/PILLARS-TABLE-1.md` | Opracować aktualny indeks, nie traktować tabeli 1 jako kompletnego stanu bieżącego |
| A-04 | Niespójna klasyfikacja Alchemy: filar / gałąź | Potwierdzone; otwarte | `GLOSSARY.md`, adnotacja korzenia Alchemy, `PILLARS-TABLE-1.md`, verbatim źródła | Ujednolicić pojęcie architektoniczne decyzją właściciela korpusu |
| A-05 | Błędne odnośniki do `docs/korzenie/PILLARS-TABLE.md` | Potwierdzone | Linki w co najmniej sześciu korzeniach; właściwy plik to `PILLARS-TABLE-1.md` | Poprawić odnośniki w osobnej, zatwierdzonej zmianie |
| A-06 | Niejednoznaczny zakres terminu SSOT | Potwierdzone; otwarte | README, tabela filarów, rejestr wyników i dokumenty korzeni | Nazwać osobno SSOT dla pnia formalnego, architektury/wersji i wyników |
| A-07 | Szablony GitHub Issues nie pokrywają wymaganych pól metodyki | Potwierdzone; otwarte | `.github/ISSUE_TEMPLATE/zgloszenie-replikacji.md`, `errata-pytanie.md`, `docs/replikacja.md`, `docs/metodyka.md` | Dodać źródło specyfikacji (plik + §) i status weryfikacji erraty |
| A-08 | Szczegółowa treść pierwotnego punktu A-08 | Do identyfikacji | Nie została odtworzona w zachowanych raportach dostępnych przy sporządzaniu tego indeksu | Nie przypisywać numerowi tematu przez domysł; uzupełnić po odzyskaniu pierwotnego zapisu |
| A-09 | Konflikt architektoniczny Scalar ↔ Defect/Centroid: status gałęzi a deklaracja wchłonięcia | Potwierdzone; nierozstrzygnięte | `P0-Scalar-v0_3_5.md`, `P0-Defect-v0_8.md`, `PILLARS-TABLE-1.md`, Philosophy; raport `asterion-scalar-centroid-tau-2026-11-20.md` | Zdefiniować, czy „wchłonięcie” oznacza wyniki, treść, czy zmianę pozycji architektonicznej |
| A-10 | Transfer Flow → Defect i Memory → Net ma charakter selektywny, nie pełnego zastąpienia źródeł | Potwierdzone; otwarte dokumentacyjnie | Flow §5.5.1, §5.7, §7.5 i Defect §12; Memory v0.3.7 i Net v0.6.1; raport `asterion-defect-flow-hilbert-2026-11-20.md` oraz `asterion-net-memory-2026-11-20.md` | Zachować źródła i dodać jawne odsyłacze do nieprzeniesionych specyfikacji |
| A-11 | Brak osobnego korzenia P₀-Origins | Wyjaśnione; decyzja architektoniczna otwarta | Origins jest programem opisanym w Philosophy; Scalar pozostaje odrębną gałęzią | Zdecydować, czy wystarczy jawne objaśnienie w Philosophy, czy potrzebny osobny wpis glosariusza |
| A-12 | Rozbieżność liczby filarów: 7/8 | Potwierdzone; otwarte | Philosophy i Experiments | Uzgodnić licznik i zakres pojęcia „filar” |
| A-13 | README PL/EN/ES zawierają nieaktualne i niespójne opisy zakresu korzeni, kodu i rejestru | Potwierdzone; otwarte | `README.md`, `README.en.md`, `README.es.md` | Zsynchronizować trzy wersje językowe i opisać aktualny zakres repozytorium |
| A-14 | Brak wymaganych pól w szablonach Issues | Potwierdzone; otwarte | Szablon replikacji nie ma osobnego pola źródła specyfikacji; szablon erraty nie ma statusu weryfikacji | Uzupełnić szablony; punkt zachowuje odrębny identyfikator metodyczny mimo pokrewieństwa z A-07 |
| A-15 | Glosariusz: Applications już obecne, Origins nie ma osobnego wpisu | Częściowo rozwiązane | Aktualny `GLOSSARY.md` zawiera P₀-Applications v0.5.2; Philosophy opisuje program Origins | Zdecydować, czy dodać krótkie objaśnienie Origins w glosariuszu |
| A-16 | Zaproszenie nadmiernie obiecuje kompletność publicznego dziennika | Potwierdzone | `ZAPROSZENIE.md`, README, `docs/metodyka.md`; raport `asterion-continuation-2026-11-20.md` | Zawęzić deklarację do materiałów opublikowanych w repo i okresowo aktualizowanego zrzutu rejestru |
| A-17 | Deklaracja, że wszystkie specyfikacje są jawne i samowystarczalne, jest zbyt szeroka | Potwierdzone | README; zależności poza repo wskazane m.in. w PILLARS-TABLE-1 i Scalar; `docs/replikacja.md` | Oceniać kompletność per specyfikacja i jawnie wskazywać brakujące źródła |
| A-18 | Nieostry zakres deklaracji „zero rozbieżności merytorycznych” w adnotacji PILLARS-TABLE-1 | Potwierdzone | `docs/korzenie/PILLARS-TABLE-1.md`; raport `asterion-continuation-2026-11-20.md` | Ograniczyć deklarację do zgodności pięciu stempli wersji, jeśli taki był jej zamierzony zakres |
| A-19 | Status źródła `p0_dowody.ipynb` | Odzyskane, archiwalne, do decyzji o wpięciu | Informacja przekazana przez Leszka: plik odzyskany i zweryfikowany jako tożsamy z przywołaniem w STALK | Decyzja o wpięciu do repozytorium należy do właściciela korpusu; niniejszy indeks nie dodaje ani nie modyfikuje notebooka |

## Uwagi o kompletności indeksu

1. Benchmarkiem jest dokładnie `main` @ `ff5345f50f509ff95fafcd1e4b28ce64b388eb1c`; nie należy utożsamiać go z HEAD gałęzi audytowej.
2. A-07 i A-14 są blisko spokrewnione, ale zachowują osobne identyfikatory z wcześniejszego audytu.
3. A-08 pozostawiono jawnie jako „do identyfikacji”, ponieważ w zachowanych raportach dostępnych przy tworzeniu indeksu nie ma bezpiecznego przypisania jego pierwotnego opisu. To celowe oznaczenie luki źródłowej, nie nowa teza.
4. Statusy w tabeli opisują stan rozpoznania audytowego. Nie zmieniają statusów matematycznych ani decyzji laboratorium.
5. Plik jest indeksem na gałęzi audytowej; nie zmienia żadnego korzenia, rejestru, README ani `main`.
