# Asterion — audyt matematyczny Axis ↔ Centroid (etap 1: 5K₄)
**Data:** 2026-11-21  
**Baza repozytorium:** `main` @ `ff5345f50f509ff95fafcd1e4b28ce64b388eb1c`  
**Gałąź raportu:** `audit/asterion-continuation-2026-11-20`  
**Zakres:** kontrola niezależna liczb i zależności logicznych dla 5K₄; bez zmian w źródłach i `main`.

## 1. Materiał źródłowy i ograniczenie

Odczytano:
- `docs/korzenie/P0-TAU-v1_7_2.md`, §§7.8.1–7.8.3, 7.8.7;
- `docs/korzenie/P0-Centroid-v5_2-zmiany.md`, wskazanie §8.5.9 jako niezweryfikowanego bez kodu P0-AXIS-01;
- `docs/korzenie/P0-SERC-v0_4_2.md`, §§4.6, 19.3 i mapę statusów;
- `docs/korzenie/P0-Defect-v0_8.md`, dla kontroli granic transferu pojęć.

W aktualnym drzewie `main` nie ma pliku Axis, notebooka `p0-axis` ani kodu źródłowego P0-AXIS-01. Wśród plików programistycznych są jedynie trzy skrypty PROXY Estrady/TAU. TAU i SERC wskazują, że `p0-axis` pozostaje zależnością poza repo. Z tego powodu nie można odtworzyć ani zweryfikować implementacji BFGS/SLSQP ani pełnej definicji modelu A z §8.5.9. Poniższy rachunek niezależny sprawdza jawne wzory, nie zastępuje brakującego źródła.

## 2. Deficyt kątowy — wynik ✅

Dla foremnego czworościanu kąt dwuścienny spełnia
`cos(theta_d) = 1/3`, zatem
`theta_d = arccos(1/3) = 70.5287793655093...°`.

Dla pięciu czworościanów wokół wspólnej krawędzi:
`delta = 2*pi - 5*theta_d`
`delta = 0.128388220475713... rad`
`delta = 7.35610317245346...°`.

Wartość 7.356° z TAU jest poprawnym zaokrągleniem. Wniosek geometryczny jest elementarny: pięć regularnych kątów dwuściennych nie wypełnia pełnego kąta 2*pi wokół wspólnej krawędzi. To dowodzi deficytu kątowego; samo w sobie nie dowodzi jeszcze konkretnego współczynnika skurczu krawędzi.

## 3. Współczynnik skali — rachunek warunkowy ✅, interpretacja geometryczna otwarta

TAU podaje wzór:
`r_scale = 1/(tan(pi/5)*sqrt(2))`.

Z tożsamości połowy kąta:
`tan(theta_d/2) = sqrt((1-cos(theta_d))/(1+cos(theta_d)))`
`= sqrt((2/3)/(4/3)) = 1/sqrt(2)`.

Stąd równoważnie:
`r_scale = tan(theta_d/2)/tan(pi/5)`.

Niezależne obliczenie daje:
- `r_scale = 0.973248989467730163788...`;
- `1 - r_scale = 0.0267510105322698362...`;
- skurcz procentowy `100*(1-r_scale) = 2.67510105322698362...%`.

**Kontrola zapisu w korpusie:** TAU podaje `r_scale = 0.973254` oraz skurcz `2.675%`. Procent jest poprawny po zaokrągleniu do trzech miejsc po przecinku. Współczynnik `0.973254` różni się od wartości wynikającej z podanego wzoru o `0.00000501053227...` (około 5.15 ppm). Do sześciu miejsc po przecinku wzór daje `0.973249`, nie `0.973254`; do pięciu cyfr znaczących oba zapisy dają `0.97325`. Nie jest to duży błąd liczbowy, ale zapis do sześciu miejsc wymaga korekty albo wyjaśnienia, czy `0.973254` pochodzi z przybliżenia numerycznego o określonej tolerancji.

**Zastrzeżenie zasadnicze:** sprawdzono arytmetykę jawnego wzoru. Bez Axis §8.5.9 nie da się sprawdzić, czy `r_scale` rzeczywiście jest właściwym stosunkiem długości krawędzi w zadanej konstrukcji kontaktu symetrycznego. Do tego potrzebne są definicja konfiguracji, współrzędne/więzy, wskazanie krawędzi mierzonej przed i po kontakcie oraz dowód, że rozwiązanie jest geometrycznie dopuszczalne i właściwe (np. globalne minimum, jeśli tego wymaga definicja).

## 4. Rozdzielenie modeli A i B — ważna granica wnioskowania

TAU §7.8.7 jawnie rozróżnia:
- **Model A — geometryczny:** pozycje w `R^3`, sztywność foremnych czworościanów; źródło: `p0-axis §8.5.9`;
- **Model B — skalarny:** wartości na wierzchołkach i uśrednianie Jacobi/GS; źródło: TAU §7.8.2.

TAU stwierdza też, że Model B nie zna długości krawędzi i nie może odtworzyć nierówności promienisty/obwodowy z Modelu A.

W konsekwencji:
1. Dowód niezmienniczości `p₀^styk` i mnożnika `1 - 4*alpha/3` w Modelu B nie dowodzi współczynnika geometrycznego `r_scale` w Modelu A.
2. Zbieżność skalarna w Modelu B nie dowodzi, że geometria pięciu foremnych czworościanów może się domknąć po jednorodnym skurczu.
3. Deficyt kątowy Modelu A i atraktor Modelu B są wynikami o różnych obiektach. Ich zestawienie może być użytecznym mostem badawczym, ale nie jest jeszcze wyprowadzeniem jednego z drugiego.

To rozdzielenie jest zgodne z ostrzeżeniem TAU §7.8.7 i musi pozostać jawne w dalszych opracowaniach.

## 5. Granica interpretacji SERC

SERC §4.6 i H-SERC-3 przenoszą wartość 2.675% na hipotezę o systematycznej różnicy między kolejnymi epizodami klinicznymi. W tym audycie nie ma danych klinicznych ani modelu statystycznego, który łączyłby geometrię 5K₄ z taką różnicą. Status geometrycznego rachunku nie przenosi się na interpretację kliniczną. Ta druga pozostaje hipotezą do testu na danych longitudinalnych.

## 6. Rozliczenie statusów

| Twierdzenie / element | Status po kontroli | Uzasadnienie |
|---|---|---|
| `theta_d = arccos(1/3)` | ✅ | definicja kąta dwuściennego foremnego czworościanu |
| `delta = 2*pi - 5*theta_d = 7.356103...°` | ✅ | bezpośredni rachunek |
| `r = 1/(sqrt(2)*tan(pi/5))` jako liczba | ✅ warunkowo | wartość i tożsamość trygonometryczna sprawdzone |
| `r_scale` jako skala krawędzi w modelu Axis | 🔍 / otwarte | brak konstrukcji i kodu Axis |
| Niezależność dwóch solverów BFGS/SLSQP | 🔍 niezweryfikowane | brak skryptu, danych wejściowych, tolerancji i raportu zbieżności |
| Związek Modelu A z `p₀^styk` Modelu B | 💡 / otwarte | TAU jawnie rozdziela modele; brak mapy zachowującej metrykę |
| Interpretacja kliniczna 2.675% | 💡 | wymaga osobnego testu empirycznego |

## 7. Co jest potrzebne do zamknięcia audytu Axis

Minimalny pakiet źródłowy:
1. oryginalny `p0-axis` lub treść §8.5.9, §16bis i §16ter;
2. dokładna definicja konfiguracji 5K₄ w Modelu A oraz tego, co oznacza „kontakt symetryczny”;
3. jawny wzór lub układ równań prowadzący do `r_scale`;
4. kod BFGS i SLSQP, parametry startowe, ograniczenia, tolerancje, kryteria stopu i wartości reszt;
5. informacja, czy oba solvery liczą to samo zadanie i czy są niezależną kontrolą, a nie dwiema metodami rozwiązania tego samego źle postawionego problemu.

## 8. Wniosek etapu 1

**Deficyt kątowy 7.356103...° jest potwierdzony. Wartość wynikająca z jawnego wzoru na skalę to 0.973248989... (skurcz 2.675101...%).** Wartość procentowa z TAU jest poprawnie zaokrąglona; współczynnik 0.973254 nie jest poprawnym zaokrągleniem tego wzoru do sześciu miejsc po przecinku, choć zgadza się do pięciu cyfr znaczących.

Nie potwierdzono jeszcze, że wzór skali wynika z geometrii kontaktu symetrycznego w modelu Axis, ani że łączy się z algebrą Centroid. Nie potwierdzono także dwóch deklarowanych obliczeń solverowych. To są właściwe otwarte punkty, nie powód do odrzucenia samego rachunku kątowego.

**Decyzja audytowa:** zachować deficyt kątowy jako ✅; współczynnik skali jako poprawny rachunek warunkowy; status geometrycznej interpretacji `r_scale` i mostu Axis↔Centroid pozostawić 🔍/otwarte do odzyskania źródła.
