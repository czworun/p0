# Raport niezależnej replikacji Z1 — P₀–Estrada (§35 + §36)

**Replikant:** Asterion  
**Data:** 2026-11-02  
**Podstawa:** przesłany pakiet „P₀–Estrada: pakiet replikacji Z1 (§35 + §36)”  
**Status raportu:** niezależna implementacja; wyniki numeryczne oznaczone 🔍, a zgodności dokładne jako kandydaci ✅ zgodnie z protokołem źródłowym.

## 1. Metoda niezależna

Macierze taktów zbudowałem bezpośrednio z definicji: `M_i` jest macierzą jednostkową z wierszem `i` zastąpionym przez `(1/4,1/4,1/4,1/4)`. Następnie złożyłem `W_nat = M_3 M_2 M_1 M_0`, `W_mir = M_2 M_3 M_1 M_0`, `P_c = I - J/4` oraz `B = P_c W`.

Wielomiany charakterystyczne sprawdziłem na macierzach wymiernych. Wartości własne i wektory wyznaczyłem numerycznie metodą rozkładu własnego; wektory dla pary zespolonej sprawdziłem drugi raz przez jądro wyznaczane SVD. Dla dynamiki iterowałem bezpośrednio `x_(n+1) = B x_n / ||B x_n||`. Krzywą graniczną próbkowałem w 200 000 równomiernych fazach. Dla lokalnych rzędów biegunów użyłem regresji log–log na 80 punktach logarytmicznych w przedziale `t = 1e-4 ... 1e-2`, z trzema kierunkami LCG na punkt; stan LCG aktualizowałem przed odczytem i prowadziłem jeden ciągły strumień.

**Kontrola wektorów własnych:** względne residua wyniosły: prawy wektor zespolony `1.04e-16`, lewy `1.91e-16`, wektor rzeczywisty `6.06e-17`. Zgodność wektorów dla pary zespolonej, po wyrównaniu fazy, między eigensolverem a niezależnym SVD: `9.19e-16` (prawy) i `1.28e-15` (lewy). Wszystkie są poniżej progu `1e-12`.

## 2. Wyniki bramek A — widmo bazowe

| Bramka | Wynik niezależny | Ocena |
|---|---|---|
| A1 | `λ⁴ − (369/256)λ³ + (131/256)λ² − (19/256)λ + 1/256` — dokładnie | ✅-kandydat |
| A2 | `λ⁴ − (113/256)λ³ + (18/256)λ² − (1/256)λ` — dokładnie | ✅-kandydat |
| A3 | `0`, `0.134710644695`, `0.153347802652 ± 0.074039102546 i` | 🔍 zgodne |
| A4 | `θ = 25.772093727472°`, `ρ = 0.170286045477` | 🔍 zgodne |
| A5 | `B·1 = (0,0,0,0)` — dokładnie | ✅-kandydat |
| A6 | `W_mir = P(23) W_nat P(23)` — równość dokładna, maks. różnica `0` | ✅-kandydat |
| A7 | `Φ(−x) = −Φ(x)` dla punktów, dla których `Φ` jest określona | ✅-kandydat |

Wielomiany A1 i A2 zostały uzyskane z rachunku wymiernego, a nie dopasowane z przybliżonych wartości własnych.

## 3. Wyniki bramek B — 14 punktów

| Bramka | Wynik niezależny | Ocena |
|---|---|---|
| B1 | `m̂_01 = (1,1,−1,−1)/2`; pozostałe przez permutację | ✅-kandydat |
| B2 | Iloczyny skalarne trzech osi środków: `0, 0, 0` | ✅-kandydat |
| B3 | Wszystkie trzy pary środków antypodalnych sumują się do zera | ✅-kandydat |
| B4 | Kąty: `54.735610317245°` oraz `125.264389682755°` | zgodne z formułą; uwaga o zaokrągleniu |

Punkty środkowe tworzą trzy ortogonalne osie antypodalne — wierzchołki ośmiościanu. Cztery `v̂_i` wraz z czterema antypodami dają osiem punktów tetraedrycznych. Łącznie otrzymujemy 14 punktów układu stella octangula.

## 4. Wyniki bramek C — dyskryminant

| Bramka | Wynik niezależny | Oczekiwane / ocena |
|---|---|---|
| C1 | Średni wykładnik przy 6 środkach: `1.999961731543` | `2.000`; zgodne |
| C2 | Średni wykładnik przy 4 wierzchołkach: `2.999972730475` | `3.000`; zgodne |
| C3 | Średni wykładnik na wybranym punkcie ogólnym ściany: `0.994392735149` (zakres kierunków `0.992849...0.995579`) | `1.000`; zgodne |
| C4 | `max |Δ| = 0.096225044865 = 1/(6√3)` numerycznie | `0.096225`; zgodne |
| C5 | Reprezentant maksimum, po uporządkowaniu współrzędnych: `(0.6738873, 0.2141865, −0.2141865, −0.6738873)` | proporcja `1 : 0.3178 : −0.3178 : −1`; zgodne |

W C3 użyłem jawnego punktu ogólnego ściany `x = (1,1,0,−2)/√6`. Pakiet nie wskazuje konkretnego punktu ogólnego ani dokładnej liczby próbek regresji; dlatego C3 jest reprodukowalne co do rzędu, ale nie co do ostatniej cyfry wyniku regresji.

## 5. Wyniki bramek D — dynamika

Starty: cztery znormalizowane projekcje `v̂_i`; iteracja `Φ(x)=normalize(Bx)`.

| Bramka | Wynik niezależny | Oczekiwane |
|---|---|---|
| D1 | minimalna szczelina po 1 rundzie: `0.096786783699` | `0.096787` |
| D2 | `0.104301502058, 0.264163714828, 0.096786783699, 0.350759975446` | zgodne |
| D3 | `0.004660306225, 0.075436020213, 0.028877577786, 0.087755657936` | zgodne |
| D4 | zakres `|Δ|`, n=100...300: `[9.862043e−5, 0.094072116190]` | `[9.86e−5, 0.094072]` |
| D5 | zakres minimalnej szczeliny obrazu do dowolnej ściany, n=100...300: `[0.000364354310, 0.419664679749]` | `[3.64e−4, 0.419665]` |
| D6 | odległości cięciwowe wszystkich 6 par orbit: `[0.717517701301, 1.985113330877]` | zgodne |
| D7 | odległości cięciwowe par (0,2) i (1,3): `[1.814063350886, 1.985113330877]` | zgodne |
| D8 | przyrost fazy `25.772093727472°` na rundę; maks. odchyłka w double od kąta własnego `7.8e−14°` | `25.7721°`; bramka `1e−9°` spełniona |
| D9 | średnia cięciwa `||X(n+14)−X(n)|| = 0.014118464848`, maksimum `0.022045831229` | `0.014118`, `0.022046` |
| D10 | `1.945753264126, 1.982095756066, 1.898856849701, 1.898856849701, 1.982095756066, 1.945753264126` | zgodne |
| D11 | `R_n`, n=100...200: `[0.962485207262, 0.987304200530]` | `[0.962485, 0.987304]` |
| D12 | `0.172981170512, 0.153673417368, 0.139808829439, 0.205749768220` | zgodne |

D11 odtwarza okno §35.5 do podanej dokładności. D8: odchyłka `7.8e−14°` jest nieco większa od dodatkowego opisu Vibe `6e−14°`, ale pozostaje ponad cztery rzędy wielkości poniżej tolerancji bramki `1e−9°`; traktuję to jako różnicę numeryczną implementacji, nie rozbieżność modelu.

## 6. Wyniki bramek E — krzywa graniczna

| Bramka | Wynik niezależny | Oczekiwane |
|---|---|---|
| E1 | osie elipsy: `0.842007669300`, `0.539465554822` | `0.842008`, `0.539466` |
| E2 | liczba zmian znaku na każdej z 6 ścian: `2` | dokładnie `2` |
| E3 | marginesy od środków (01,02,03,12,13,23): `0.102727453375, 1.067369770398, 0.427859161545, 0.427859161545, 1.067369770398, 0.102727453375` | zgodne |
| E4 | marginesy od antypodalnych par wierzchołków: `0.344211029064, 0.221983587218, 0.760304126558, 0.927426689098` | zgodne |
| E5 | `min|α|/max|α| = 0.640689597602` | `0.640676`; różnica `1.36e−5`, w tolerancji |
| E6 | minimalna odległość krzywej od `±û`: `0.693692171704` | `0.693692` |
| E7 | zakres `||B p||`: `[0.139596711417, 0.207722209128]` | zgodne |
| E8 | `max |Δ|` na krzywej: `0.094072422105` | `0.094072` |

E5 jest zgodne z tolerancją. Dokładny iloraz obliczony z niezaokrąglonych osi wynosi `0.640689597602`; wartość Vibe `0.640676` odpowiada ilorazowi osi zaokrąglonych do sześciu miejsc.

## 7. Wyniki bramek F — biegun przepływu

| Bramka | Wynik niezależny | Oczekiwane |
|---|---|---|
| F1 | `|û| = (0.711601299886, 0.609009446012, 0.191055615691, 0.293647469564)`; znaki `+−+−` | zgodne |
| F2 | kąty do środków: `84.111559°, 25.490465°, 65.294529°, 65.294529°, 25.490465°, 84.111559°` | zgodne |
| F3 | kąty do `±v̂_i`: `34.746033°, 45.313796°, 77.255017°, 70.179479°` | zgodne |
| F4 | nie można jednoznacznie odtworzyć bez definicji płaszczyzny `E` | pakiet nie definiuje `E` |
| F5 | `wᵀû` numerycznie rzędu `5e−16` | `0`, próg `1e−15` |
| F6 | kąt między `û_nat` i `û_mir`: `40.087410095216°` | `40.087°` |

**F4 — rozbieżność wymagająca doprecyzowania:** jeśli `E` oznacza naturalną płaszczyznę zespolonej pary własnej `span(Re z, Im z)`, otrzymuję kąt `40.589057°` między `û` a tą płaszczyzną (kąt do jej normalnej: `49.410943°`). Żadna z tych konwencji nie daje `46.814°`. W przesłanym pakiecie nie ma definicji płaszczyzny `E`, więc nie uznaję tego za falsyfikację F4 — to bramka niekompletna specyfikacyjnie.

## 8. Wyniki bramek G — jądra i rezolwenty

| Bramka | Wynik niezależny | Oczekiwane |
|---|---|---|
| G1 | wartości osobliwe: `0.226568418143, 0.145689719744, 0.118340051601` | zgodne |
| G2 | wartości własne operatora `G`: `1.054110938322, 1.021685785968, 1.014203275710` | zgodne |

Wszystkie wartości są skończone na `V_cyc`. Wartość własna `1` operatora `W` na kierunku konsensusu powoduje osobliwość `I−W`; projekcja `P_c` usuwa ten kierunek z dynamiki cyklicznej.

## 9. Wyniki bramek H — lustro i fazy

| Bramka | Wynik niezależny | Oczekiwane |
|---|---|---|
| H1 | `0°, −61.918347758°, −146.782499900°, 96.443023432°` | zgodne |
| H2 | odstępy cykliczne: `84.864152142°, 61.918347758°, 96.443023432°, 116.774476669°`; multizbiór lustrzany identyczny | zgodne |
| H3 | `−9.320545069°, −44.690402292°, 26.204240824°, −1.223823631°, 44.656009921°, −15.109980714°` | zgodne |
| H4 | `−9.320545069°, 26.204240824°, −44.690402292°, 44.656009921°, −1.223823631°, −15.109980714°` | zgodna permutacja (23) |
| H5 | `0°, −61.918347758°, 96.443023432°, −146.782499900°` | zgodne |

## 10. Kandydaci erraty i doprecyzowania

### ERT-1 — fałszywa implikacja `B = W na V_cyc`

W §2.1 pakietu zapisano, że z `B = P_c W` wynika `B = W` na `V_cyc`. To nie jest prawdą dla zdefiniowanego `W_nat`: `W_nat` nie zachowuje podprzestrzeni wektorów o sumie współrzędnych zero.

Dokładny kontrprzykład: dla `x=(1,−1,0,0)ᵀ`, które należy do `V_cyc`:

- `W_nat x = (0, −1/4, −1/16, −5/64)ᵀ`,
- suma współrzędnych `W_nat x` wynosi `−25/64`, więc `W_nat x` nie należy do `V_cyc`,
- `B x = (25/256, −39/256, 9/256, 5/256)ᵀ`.

**Proponowane brzmienie:** „`B = P_c W`; na `V_cyc` działamy operatorem `P_c W`. Samo `W` nie zachowuje `V_cyc`.” Wszystkie obliczenia w tym raporcie używają prawidłowo `B=P_cW`, zgodnie z definicją `Φ`.

### ERT-2 — nieokreślona płaszczyzna `E` w F4

Specyfikacja nie definiuje płaszczyzny `E`. Dla naturalnego odczytania `E=span(Re z, Im z)` otrzymuję `40.589057°`, a nie `46.814°`. Należy podać wektory bazowe płaszczyzny i konwencję mierzenia kąta.

### ERT-3 — precyzja / klasyfikacja bramek B4 i A3–A4

B4 podaje przybliżenia `54.7356°` i `125.2644°`, ale nagłówek sekcji mówi o tolerancji `≤1e−15`. Dokładne wartości to `54.735610317245°` i `125.264389682755°`; same skrócone zapisy dziesiętne nie mogą spełnić takiej tolerancji. Najczyściej pozostawić formuły `acos(1/√3)` i `180°−acos(1/√3)` albo podać tolerancję adekwatną do liczby wyświetlanych cyfr. Analogicznie A3–A4 są przybliżeniami wartości algebraicznych, a nie bramkami wymiernymi.

### ERT-4 — niespójność wewnętrzna E5 względem E1

Z definicji krzywej i fazy skośnej wynika, że `min|α|/max|α| = ax₂/ax₁`. Z moich niezależnych osi E1 otrzymuję `0.539465554822 / 0.842007669300 = 0.640689597602`; ten sam wynik wychodzi bezpośrednio z próbkowania `|α|`. Wartość E5 podana w pakiecie (`0.640676`) różni się o `1.36e−5`. Bramka E5 nadal przechodzi tolerancję `±1e−3`, ale dopisek „= ax₂/ax₁” nie zgadza się z podanymi osiami. Wartość źródłową E5 należy sprawdzić lub skorygować.

### DOP-1 — pełna deterministyczność testów LCG

Pakiet podaje parametry LCG, ale nie mówi jednoznacznie, czy odczyt następuje przed czy po aktualizacji stanu, czy generator resetuje się dla każdego punktu oraz ile punktów logarytmicznych trafia do regresji. Rząd lokalny jest stabilny i zgodny, ale dla odtwarzalności ostatnich cyfr trzeba dopisać te trzy szczegóły.

## 11. Wniosek statusowy

- **T1 — ✅:** geometria 14 punktów i lokalne rzędy 2/3 są zgodne; dodatkowo wynik wynika bezpośrednio z liczby zerujących się czynników Vandermonde'a.
- **T2 — ✅:** biegun przepływu jest oddalony od wszystkich środków; najbliższe są środki (02) i (13), po `25.490465°`.
- **T3 — ✅:** osobliwość `I−W` na konsensusie jest usuwana przez projekcję `P_c`; operator na `V_cyc` jest od niej wolny.
- **T4 — ✅:** krzywa przecina każdą z sześciu ścian dokładnie dwa razy i ma dodatnie marginesy od wszystkich 14 punktów.
- **Bramki numeryczne C–H — 🔍:** zgodne z wartościami Vibe w zadanych tolerancjach, z wyjątkiem niekompletnej definicji F4. Drobne różnice E5 i D8 mieszczą się w tolerancjach.
- **ERT-1 jest istotna:** nie zmienia żadnej z odtworzonych liczb, bo oba rachunki używają `B=P_cW`; poprawia jednak logiczny opis operatora działającego na `V_cyc`.

**Konkluzja:** zasadnicza konstrukcja Z1 przechodzi niezależną replikację. Nie rekomenduję jednak wpisywania do filara zdania „B=W na V_cyc” ani uznawania bramki F4 za zamkniętą, dopóki nie zostaną poprawione / uzupełnione.
