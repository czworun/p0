# Audyt Asteriona — MVP-02 v0.4: replikacje algebraiczne i protokoły A.3/A.4

Data: 2026-11-22  
Audytowana wersja: `main`, commit `1ffdd3d4428b74c9306464cfefd02579f8c6f3d4`  
Specyfikacja: `docs/mvp-02-spec-v0_4.md`, blob `c4ef2d4174735fa1dd30a8235cdd828748b26846`  
Uzupełnienie: `docs/mvp-02-spec-v0_4-aneks-a-uzupelnienie.md`, blob `e68906bed162eb6f0aecec416c6bba9e1b655482`

## 1. Zakres i ograniczenie K6

Wykonano wyłącznie dozwolone przed bindem replikacje kombinatoryczne i algebraiczne. Nie obliczano supremów transportowych, czasów \(\tau\), miary \(U_b\), rozkładu zerowego ani wyniku testu. Nie zmieniano `main`.

## 2. Replikacje niezależne

### 2.1 Graf dwunastościanu i BFS — ✅

Z tabeli 20 ścian i reguły wspólnej krawędzi odtworzono graf:
- 20 wierzchołków, 30 krawędzi, stopień każdego wierzchołka 3;
- graf spójny, średnica 5;
- liczności nieuporządkowanych par według dystansu: 30, 60, 60, 30, 10;
- kule dystansu od dowolnej ściany: 3, 6, 6, 3, 1;
- pary antypodalne dokładnie: (0,19), (1,15), (2,12), (3,11), (4,14), (5,18), (6,13), (7,16), (8,10), (9,17).

Zgodność z §0.3 v0.4 pełna.

### 2.2 Partycje U1/U2 — ✅

Automorfizmy grafu icosahedralnego (na 12 wierzchołkach) enumerują 120 elementów. Spójna orientacja powierzchni rozdziela je na 60 zachowujących orientację i 60 odwracających. Dla każdej konfiguracji G0–G4 stabilizator w podgrupie zachowującej orientację ma rząd 12. Jego dwie orbity na ośmiu ścianach konfiguracji są dokładnie podanymi w §2.2 zbiorami U1 i U2. Wszystkie pięć podziałów potwierdzono.

### 2.3 L_cyc — ✅ (dokładny ślad)

Zbudowano orientowaną macierz incydencji D_inc i bezznakową H_inc w porządku krawędzi combinations(range(12),2). Dla
\[
P_{cyc}=I-D_{inc}^{T}(D_{inc}D_{inc}^{T})^{+}D_{inc},
\qquad L_{line}=10I-H_{inc}^{T}H_{inc},
\]
otrzymano dokładnie \(\operatorname{tr}(P_{cyc}L_{line}P_{cyc})=2438/15\), a \(\operatorname{rank}P_{cyc}=19\). To potwierdza checkpoint śladu ORIENT-02-A. Nie utożsamiam tego z potwierdzeniem całego widma — pełna replikacja widma wymaga osobnego zestawienia wartości i krotności.

### 2.4 Fingerprinty montażu właściwego — 🔍 (replikacja double)

Zrekonstruowano macierze 13×13 bezpośrednio z definicji M_local, aktywując w każdej tetrze wierzchołki rosnąco, P0 na końcu, a ściany rosnąco po indeksie. Wyniki double:
- G0: rho = 0.22744676492279…
- G1: rho = 0.19732031060304…
- G2: rho = 0.25866814795348… (para zespolona 0.257467127920 ± 0.024897566275 i)
- G3: rho = 0.26016012572819…
- G4: rho = 0.21896688179422…
- węzeł: tr(R) = 1.11963070776913…, rho = 0.06615917187705… (para zespolona 0.057041517005 ± 0.033515688284 i).

Wartości zgodne z v0.4. To niezależna kontrola konstrukcji i typologii, ale obliczenie double nie jest certyfikatem 12 cyfr; kolejka kwalifikacyjna Claude'a pozostaje zasadna.

## 3. Protokół A.3 — certyfikat supremum — ✅ z uwagą wykonawczą

Dla
\[
F(\theta)=\sum_{a\le b}c_{ab}\cos\theta_a\cos\theta_b,
\qquad \theta_5=\theta_1+\theta_2,
\]
w czterech niezależnych współrzędnych każda składowa gradientu jest ograniczona przez \(2\sum_{a\le b}|c_{ab}|\). Odległość punktu torusa od najbliższego węzła regularnej siatki w metryce L1 nie przekracza \(4(h/2)=2h\). Zatem
\[
0\le \sup F-M\le 2L_Fh,
\qquad L_F=2\sum|c_{ab}|,
\]
jest poprawnym, choć konserwatywnym certyfikatem globalnego maksimum.

Niezależnie z form zamkniętych wag oszacowano maksymalną szerokość certyfikatu po trzech początkowych zagęszczeniach:
- d1/d4: około 7.03·10^-4;
- d2/d3: około 3.64·10^-4;
- d5: około 3.27·10^-3.

Dalsze zagęszczenie czterokrotne na rundę: do zejścia poniżej 10^-4 potrzeba odpowiednio 2, 1 i 3 dodatkowych rund. Limit pięciu rund dodatkowych jest wystarczający dla wszystkich orbit i obu kanałów. W tym punkcie nie widzę błędu matematycznego w certyfikacie A.3.

**Uwaga wykonawcza:** należy zapisywać rzeczywistą szerokość przedziału certyfikatu dla każdego transferu, nie tylko deklarację PASS; A.3 wymaga również pełnej tabeli per transfer.

## 4. A.4 — dwa nierozliczone blokery protokołu

### A4-1. Przedział supremum nie jest przeniesiony na próg i wynik — 🔍 BLOKER

A.3 nie zwraca dokładnej liczby sup, tylko certyfikowany przedział \(S\in[S_-,S_+]\), o szerokości najwyżej 10^-4. Tymczasem §2.3 definiuje \(\theta=S/2\) dokładnie, a A.4 używa \(\theta\) jako pojedynczego progu do wyznaczania \(\tau\). Dokument nie mówi, jak z przedziału S uzyskać certyfikowany przedział czasu ani jak przenieść go do \(U_b=\tau_{surf}/\tau_{int}\) i porównania kill.

To nie jest sprzeczność definicji matematycznej: dokładny próg jest dobrze określony. To luka w procedurze numerycznej, która ma go odtworzyć. Minimalne domknięcie:
1. używać \(\theta\in[S_-/2,S_+/2]\), bez zastępowania go po cichu środkiem lub końcem przedziału;
2. wyznaczyć przedziały pierwszego przejścia dla obu skrajnych progów (monotoniczność czasu pierwszego przejścia względem progu daje obwiednię, o ile przypadki cenzury są obsłużone);
3. propagować te przedziały przez iloraz \(U_b\);
4. rozstrzygać kill tylko wtedy, gdy całe przedziały U_b pozostają po tej samej stronie granicy porównania z tolerancją. W przeciwnym razie wynik musi być nierozstrzygalny numerycznie.

### A4-2. „Bisekcja wszystkich niecertyfikowanych przedziałów” nie określa algorytmu izolacji pierwszego przejścia — 🔍 BLOKER

Warunek \(g_k<\theta\) poprawnie certyfikuje brak przekroczenia na przedziale. Jednak przedział niecertyfikowany nie musi zawierać przekroczenia: oba końce mogą być poniżej progu, a górne oszacowanie może być po prostu zbyt luźne. Wtedy zwykła bisekcja pierwiastka nie ma przedziału bracketingowego (brak zmiany znaku). Ponadto możliwe jest styczne osiągnięcie \(\theta\), dla którego nie ma zmiany znaku, mimo że definicja \(\tau\) używa \(\ge\).

A.4 zapowiada bisekcję po wszystkich niecertyfikowanych przedziałach, ale nie definiuje:
- rekurencyjnego podziału przedziału i kryterium odrzucania podprzedziałów;
- jak odróżnić fałszywie niecertyfikowany przedział od przedziału zawierającego pierwsze przejście;
- obsługi stycznego kontaktu z progiem;
- warunku zakończenia, gdy przedział pozostaje niecertyfikowany.

Minimalne domknięcie to jawny algorytm branch-and-bound/izolacji przedziałowej: dzielić od lewej, certyfikować podprzedziały poniżej progu, zachować pierwszy przedział z udowodnionym przekroczeniem lub kontaktem, a w razie braku rozstrzygnięcia w zadanej tolerancji zwrócić cenzurę/NIEROZSTRZYGALNY-PARCJALNY zamiast udawać wynik bisekcji.

### A4-3. TAU-MAŁE i iloraz U_b — 🔍 konsekwencja A4-1

Flaga TAU-MAŁE raportuje przedział ostatniego kroku dla \(\tau<0.01\), lecz nie mówi, jak przedział ten wpływa na iloraz \(U_b\) ani na 1-procentową tolerancję kill. Szczególnie mały mianownik może powiększyć niepewność ilorazu. Należy stosować przedziałowy iloraz; jeśli przedział mianownika obejmuje zero lub przedziały U_b nachodzą na granicę klasyfikacji, transfer nie może być traktowany jako rozstrzygnięty.

## 5. Wniosek

- Kombinatoryka BFS, antypody, partycje U1/U2 i dokładny ślad L_cyc: **potwierdzone**.
- Fingerprinty montażu właściwego: **zgodne w niezależnej replikacji double**, ale wymagają wskazanej w specyfikacji kwalifikacji wysokiej precyzji.
- Certyfikat globalnego maksimum A.3: **matematycznie poprawny i z limitem zagęszczeń wystarczającym dla wag z uzupełnienia**.
- A.4: **nie zamyka jeszcze certyfikowanej procedury pierwszego przejścia i propagacji niepewności progu do U_b/kill**. Nie wykonywać rachunku transportowego przed rozstrzygnięciem tych luk i zamrożeniem v1.0.

Status A4 pozostaje otwarty. Ten raport jest audytem, nie zmianą specyfikacji.
