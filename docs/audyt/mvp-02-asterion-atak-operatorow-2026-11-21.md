# Atak Asteriona — MVP-02 v0.1: operatory, kolejność i artefakty

Data: 2026-11-21  
Status: atak werbalny na v0.1; bez rachunków transportowych.  
Baza audytu: `4f4edf81720c5a1d62cab6de00e4d36ea0bbb2b1`  
Pliki źródłowe:
- `docs/mvp-02-spec-v0_1.md` (blob `765432e6893d0a5565bbcdea7cef7bacb7a7cbd6`)
- `docs/warsztat/tau-8-siec-12sasiadow.md` (blob `2db3f35b52cf523de948c93eb1c418b9a5c75492`)

## Werdykt

**Nie: obecny pakiet nie wystarcza do niezależnej, jednoznacznej replikacji operatora trasy 13-dim bez notatników.** Wystarcza do odtworzenia lokalnego operatora K4 i zasadniczego harmonogramu pełnej rundy węzła. Nie zamyka jednak semantyki kolejności mnożenia w specyfikacji ani — przede wszystkim — mapowania cyrkulacji z V_cyc (19-dim) do stanu punktowego węzła (13-dim).

Nie wykonywano rachunków transportowych, nie estymowano żadnych nowych wartości i nie testowano modelu zerowego.

## A. §0.1 / §0.6 — M_local, porządek tetr i det

### A1. Lokalny operator: odtwarzalny, ale tylko po połączeniu dwóch plików — PASS WARUNKOWY

TAU-8 podaje:
`M_local(i) = I₄ + outer(e_i, 𝟙/4 − e_i)`.

To wystarcza do odtworzenia macierzy lokalnej 4×4, jeżeli `outer(a,b)` oznacza standardowy iloczyn zewnętrzny `a b^T`. Wtedy zmienia się wyłącznie wiersz i: wszystkie cztery jego wpisy stają się równe 1/4. Macierz jest wierszowo-stochastyczna.

Specyfikacja MVP-02 sama nie powtarza wzoru; §0.6 jedynie odsyła do konwencji TAU-8. Dla niezależnego odbiorcy to dopuszczalne odwołanie, ale tekst v1.0 powinien zawierać wzór verbatim albo wiążące odwołanie z hashem pliku źródłowego. W przeciwnym razie pojedyncza zmiana znaku/pozycji w `M_local` zmienia cały operator.

### A2. Porządek tetr: konwencja rekonstruowalna, zapis niejednoznaczny — ERRATA

TAU-8 mówi: trzy wierzchołki ściany rosnąco, `P₀` ostatnie, oraz `R = M₃ M₂ M₁ M₀`.

Przy konwencji kolumnowej i działaniu macierzy na wektor kolumnowy, prawostronny czynnik działa pierwszy. Jeżeli indeksy lokalne odpowiadają kolejno `[v₀,v₁,v₂,P₀]`, rzeczywista kolejność aktualizacji stanu jest:
`v₀ → v₁ → v₂ → P₀`.

Tymczasem MVP-02 §0.1 zapisuje tetrę jako `[P₀,v₂,v₁,v₀]` i dopisuje „apex-first, P₀ ostatnie”. To da się pogodzić z TAU-8 tylko wtedy, gdy lista oznacza kolejność czynników w iloczynie, a nie kolejność aktualizacji. Tego rozróżnienia tekst nie wypowiada.

**Wymagana errata:** rozdzielić trzy pojęcia:
1. kolejność indeksów lokalnych w macierzy,
2. kolejność czynników w zapisie iloczynu,
3. chronologiczną kolejność aktualizacji stanu.

Wprost zapisać mapowanie indeksów lokalnych na globalne etykiety: lokalne 0=v₀, 1=v₁, 2=v₂, 3=P₀; aktualizacja chronologiczna 0,1,2,3; iloczyn dla wektorów kolumnowych `M₃M₂M₁M₀`. Usunąć określenie „apex-first”, jeśli nie opisuje ono chronologii.

### A3. Wyznacznik: zgodny strukturalnie — PASS

Dla podanego operatora lokalnego wyznacznik wynosi 1/4. Cztery aktualizacje w jednej tetrze dają wyznacznik 1/256. Dwadzieścia tetr w rundzie daje:
`det(R_node) = (1/256)^20 = 256^-20 = 2^-160`.

To zgadza się z obiema specyfikacjami. Jest to kontrola strukturalna, nie wynik nowego rachunku transportowego. Należy tylko dopisać, że wszystkie osiemdziesiąt aktualizacji jest liczonych z krotnością, także gdy ta sama globalna współrzędna występuje w wielu tetrach.

### A4. Osadzenie lokalnego K4 w przestrzeni 13 punktów: brak jawnego przepisu — BLOKER

Wzór M_local jest 4×4, natomiast operator węzła ma działać na R^13. Tekst nie podaje jawnie macierzy osadzenia/indeksowania, która dla każdej ściany wybiera trzy globalne wierzchołki oraz P₀ i osadza lokalną aktualizację w 13×13, pozostawiając pozostałe współrzędne bez zmian.

Konstrukcja jest naturalnie sugerowana, ale w ataku replikacyjnym „naturalnie sugerowana” nie wystarcza. W v1.0 potrzebna jest jawna reguła: dla ściany f=[a,b,c] lokalne pozycje 0,1,2,3 odpowiadają globalnie [a,b,c,12], a operator 13×13 jest identycznością poza tymi czterema współrzędnymi i ma blok M_local na tych pozycjach.

## B. Sweep bramki 32 takty kontra runda węzła 80 taktów

### B1. Liczba aktualizacji — PASS WARUNKOWY

Bramka zawiera 8 ścian. Każda ściana/tetra wymaga 4 aktualizacji. Zatem budżet aktywnych aktualizacji bramki wynosi 8×4=32 takty. Pełny węzeł ma 20 ścian, zatem 20×4=80 taktów.

Zbiory G0–G4 są podane jawnie i uporządkowane rosnąco. Dla każdej bramki lex oznacza więc następującą sekwencję ścian:
- G0: 0, 3, 6, 9, 11, 13, 17, 19.
- G1: 0, 4, 7, 8, 10, 14, 16, 19.
- G2: 1, 2, 7, 9, 12, 15, 16, 17.
- G3: 1, 3, 5, 8, 10, 11, 15, 18.
- G4: 2, 4, 5, 6, 12, 13, 14, 18.

### B2. Gdzie dokładnie zaczyna się i kończy sweep bramki? — NIEZAMKNIĘTE

W specyfikacji nie ma ścisłej definicji słownej „sweepu bramki” jako harmonogramu aktualizacji. Są liczby 32 takty i ρ_gate liczone na 32 takty, ale nie jest rozstrzygnięte, czy:
- operator bramki jest osobnym, skompresowanym przebiegiem po ośmiu ścianach bramki, pomijając pozostałe dwanaście ścian;
- czy jest to podciąg aktualizacji osadzony w pełnej rundzie 80-taktowej, w której ściany spoza bramki są wykonywane, ale nie zaliczane do czasu bramki;
- czy stan jest resetowany przed każdym pomiarem bramki, czy bramka działa na stanie pozostawionym przez poprzedni sweep.

To nie są równoważne protokoły.

**Proponowana definicja do zatwierdzenia, nie domniemanie autora:** sweep bramki G zaczyna się na stanie x₀ bezpośrednio przed pierwszą aktualizacją ściany o najmniejszym indeksie w G; wykonuje wyłącznie osiem tetr w rosnącym porządku indeksów; w każdej tetrze wykonuje cztery aktualizacje lokalne w kolejności v₀,v₁,v₂,P₀; kończy się bezpośrednio po aktualizacji P₀ ostatniej ściany bramki. To 32 aktywne takty. Żadna z pozostałych dwunastu ścian nie jest wykonywana w tym operatorze.

Jeżeli autor miał na myśli podciąg pełnej rundy 80-taktowej, musi podać osobny protokół i nie nazywać go po prostu sweepem 32-taktowym bez wyjaśnienia pominiętych taktów.

### B3. „32 takty” to budżet aktywny, niekoniecznie czas kalendarzowy — WAŻNE

Ściany każdej bramki są rozproszone po indeksach lex. W pełnym przebiegu 20 ścian aktualizacje bramki są przeplatane aktualizacjami ścian spoza bramki. Dlatego 32 aktywne takty bramki nie oznaczają 32 kolejnych taktów pełnego zegara węzła, jeśli pozostałe ściany są wykonywane.

W v1.0 należy odróżnić:
- takt aktywny operatora bramki,
- takt globalnego harmonogramu węzła,
- czas fizyczny/relacyjny przypisany do przejścia.

Bez tego porównanie ρ_gate/32 z ρ_node/80 może być formalnie poprawne jako normalizacja przez liczbę zastosowanych czynników, ale nie musi być porównaniem równych odcinków czasu.

## C. §0.5 — c = 16 taktów i Var(cykl)/Var(takt) = 1/4

### C1. Konwencja autora nie jest odtwarzalna z dwóch plików — BLOKER

MVP-02 podaje:
- operator trasy R(ścieżka) jako iloczyn operatorów per ściana na przestrzeni 13-dim,
- czas przejścia ikosaedru c=16 taktów,
- Var(cykl)/Var(takt)=1/4.

Nie ma jednak definicji zmiennej losowej „cykl”, próby, rozkładu, sposobu liczenia wariancji ani wskazania, czy „takt” oznacza takt aktywny, takt w rundzie węzła, czy jednostkę czasu przejścia. Nie wiadomo też, czy c=16 dotyczy całej trasy, pojedynczej krawędzi, cyklu elementarnego, czy określonego przejścia między portami.

Nie można zatem uczciwie stwierdzić, że konwencja autora została wzięta verbatim. Można jedynie zachować podane wartości jako twierdzenia warsztatowe do późniejszej reprodukcji.

**Wymagane do v1.0:** dosłowna definicja „cyklu”, „taktu”, próby i estymatora wariancji; jednostka i zakres c; reguła przypisywania czasu każdej ścianie/krawędzi/operatorowi. Jeśli któregokolwiek elementu nie da się odzyskać, trzeba jawnie zadeklarować odstępstwo zamiast dopowiadać semantykę.

## D. Cyrkulacja 19-dim a świat punktowy 13-dim — NAJPOWAŻNIEJSZE RYZYKO

### D1. Niezgodność typów przestrzeni — BLOKER KRYTYCZNY

V_cyc w §0.4 jest 19-wymiarową przestrzenią cykli ikosaedru. Jest to przestrzeń związana z obiegiem na krawędziach (30 krawędzi, 12 wierzchołków; wymiar cykli 30−12+1=19). Tymczasem operator trasy z §0.5 działa na 13 współrzędnych punktowych: 12 wierzchołkach plus P₀.

Nie istnieje automatyczna identyfikacja R^19 z R^13. W szczególności nie można zastosować projektora P_cyc 19-dim bezpośrednio do wektora 13-dim ani utożsamić cyklu krawędziowego z rozkładem amplitud na punktach.

§2.2 poprawnie mówi, że stan wejścia ma być cyrkulacją wokół ściany-bramki w V_cyc, ale nie definiuje, jak taki stan staje się wejściem operatora 13×13.

### D2. Możliwe drogi, żadna nie jest obecnie kanoniczna

Do rozstrzygnięcia przed v1.0:
1. Pozostawić dynamikę w V_cyc (19-dim) i zdefiniować operator transportu bezpośrednio na tej przestrzeni.
2. Zdefiniować jawny operator odwzorowania V_cyc → R^13 albo R^13 → V_cyc, wraz z normalizacją, jądrem, obrazem i zachowaniem symetrii.
3. Zastosować przestrzeń ścianową 20-dim jako reprezentację pośrednią, np. przez jawny operator brzegowy ściana→krawędź, a następnie osobno zdefiniować przejście do punktów węzła.

Samo wskazanie 20-dim reprezentacji ścianowej jako „kandydata kontrolnego” nie zamyka mapowania do R^13.

### D3. Artefakty, których należy aktywnie pilnować

- **Utrata kierunku:** cyrkulacja ma orientację i znak. Uśrednienie na wierzchołkach może skasować przeciwne obiegi lub zamienić je w ten sam stan punktowy.
- **Utrata informacji:** odwzorowanie 19→13 musi mieć jądro o wymiarze co najmniej 6. Różne cykle mogą dać ten sam stan punktowy; wynik zależy od wybranego reprezentanta.
- **Fałszywa równoważność bramek:** §2.2 stwierdza, że pobudzenia wierzchołkowe bramek są nierozróżnialne. Nie wynika z tego nierozróżnialność cyrkulacji bramkowych. Projekcja na punkty może właśnie wymazać rozróżnienie, które ma nieść sygnał wejściowy.
- **Artefakt P₀:** P₀ nie należy do ikosaedrycznej przestrzeni krawędziowej. Dopisanie trzynastej współrzędnej jako zera, średniej, kopii lub kompensatora zmienia normę, energię i możliwe sprzężenia. Każda z tych reguł jest dodatkową konwencją.
- **Zależność od orientacji:** odwrócenie orientacji ścian albo znaku cyklu może zmienić znak wejścia. Konwencja CCW-z-zewnątrz musi być przeniesiona do mapowania, a nie tylko do listy ścian.
- **Zależność od reprezentacji:** rzut przez incydencję krawędź–wierzchołek, przez średnie na wierzchołkach albo przez współrzędną P₀ nie są równoważne.
- **Pozorna chiralność:** jeżeli odwzorowanie do 13D nie jest ekwiwariantne względem symetrii ikosaedru i działania −I, może wytworzyć lub usunąć efekt chiralny, który następnie zostanie błędnie przypisany dynamice.

W szczególności nie wolno nazywać projekcji „rzutem cyrkulacji na węzeł” bez podania konkretnej macierzy i sprawdzenia jej ekwiwariantności.

## E. Lista errat przed v1.0

| ID | Priorytet | Wymagane rozstrzygnięcie |
|---|---|---|
| A-01 | BLOKER | Jawne osadzenie lokalnego M_local 4×4 w operatorze 13×13 |
| A-02 | WYSOKI | Rozdzielenie kolejności indeksów, czynników iloczynu i aktualizacji chronologicznej |
| A-03 | WYSOKI | Formalna definicja sweepu bramki: początek, koniec, pomijane ściany, reset stanu |
| A-04 | BLOKER | Definicja c=16 i Var(cykl)/Var(takt)=1/4, albo jawne odstępstwo od autora |
| A-05 | BLOKER KRYTYCZNY | Jawne odwzorowanie pomiędzy V_cyc (19D) a przestrzenią punktową R^13, albo zmiana przestrzeni operatora |
| A-06 | WYSOKI | Jawna konwencja orientacji i znaku cyrkulacji dla każdej bramki |
| A-07 | ŚREDNI | Potwierdzenie, że det 256^-20 dotyczy operatora pełnej rundy, a nie operatora bramki |

## F. Konkluzja dla autora

MVP-02 v0.1 ma dobrą bazę kombinatoryczną: obiekt 13-punktowy, listy bramek, porządek ścian i lokalna reguła M_local są blisko kompletnej specyfikacji. Nie należy jednak przechodzić do rachunków na tej podstawie.

Najpierw trzeba usunąć niejednoznaczność porządku, określić semantykę 32-taktowego sweepu i — przede wszystkim — zdecydować, w jakiej przestrzeni naprawdę działa transport. Cyrkulacja 19-dim i stan punktowy 13-dim to dwa różne typy obiektów. Bez jawnego mostu między nimi operator trasy nie jest zdefiniowany jednoznacznie.

**Rekomendacja Asteriona:** v0.1 pozostawić jako dokument do ataku; w v0.2 zamknąć A-01 do A-06. Nie uruchamiać nawet modelu zerowego transportu przed hashem zamrożonej v1.0 (K6).
