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


## 9. Most geometryczny, który można już wyprowadzić: Gram K₄ i holonomia

Istnieje ścisły most między macierzą `G₄ = 4I - J` z Centroid a geometrią foremnego czworościanu — na poziomie metryki, nie dynamiki.

Niech `v₁,…,v₄ ∈ R³` będą wierzchołkami foremnego czworościanu o krawędzi długości `a`, przesuniętymi tak, aby `Σᵢ vᵢ = 0`. Symetria daje wspólną wartość diagonalną `q = vᵢ·vᵢ` i wspólną wartość pozadiagonalną `p = vᵢ·vⱼ`. Z `Σᵢ vᵢ = 0` wynika `q + 3p = 0`; z `||vᵢ-vⱼ||² = a²` wynika `2(q-p)=a²`. Rozwiązanie: `q=3a²/8`, `p=-a²/8`. Zatem macierz Grama jest dokładnie

`H = (a²/8)(4I-J) = (a²/8)G₄`.

Wynik:
- `rank(H)=3`;
- `ker(H)=span{1}`;
- na `1^⊥` macierz H działa jako `(a²/2)I`;
- `G₄` jest więc, z dokładnością do skali `a²/8`, macierzą Grama regularnego czworościanu.

To daje konkretny geometryczny sens tej samej macierzy, która pojawia się w Centroid. Nie identyfikuje jednak automatycznie operatora dynamiki Centroid z operatorem metrycznym: identyfikuje formę Grama na przestrzeni wycentrowanej.

### Holonomia pięciu czworościanów

Przekraczając kolejno pięć ścian wokół wspólnej krawędzi, każda regularna tetraedryczna komórka wnosi obrót o kąt dwuścienny `theta_d` wokół tej osi. Iloczyn pięciu obrotów wokół tej samej osi jest obrotem o `5*theta_d`; modulo pełny obrót pozostaje deficyt `delta = 2*pi - 5*theta_d`. Ponieważ `delta ≠ 0`, holonomia nie jest identycznością. To jest geometryczny zapis braku domknięcia.

### Konsekwencja dla interpretacji skali

Jednorodne (izotropowe) przeskalowanie foremnego czworościanu nie zmienia jego kąta dwuściennego. Nie może zatem usunąć deficytu kątowego pięciu regularnych czworościanów. Jeżeli `r_scale` ma opisywać kontakt/domknięcie, musi dotyczyć konkretnej zmiany anizotropowej, projekcji albo innej wielkości geometrycznej — nie samej podobności foremnego czworościanu.

Podany wzór `r_scale = tan(theta_d/2)/tan(pi/5)` jest stosunkiem dwóch tangensów kątów połówkowych. Sam rachunek jest poprawny; jego nazwanie „skurczem krawędzi” wymaga wskazania trójkąta przekroju, przyjętej wielkości stałej i krawędzi mierzonej. Bez tych danych nie wolno wyciągać wniosku, że skurcz ten zamyka pięć regularnych czworościanów.

## 10. Zaktualizowany wniosek

Most Axis↔Centroid nie jest pusty: `G₄` jest dokładnie (z czynnikiem skali) macierzą Grama foremnego czworościanu. Z kolei pięciokrotna kompozycja lokalnych obrotów tetraedrycznych daje niezerową holonomię `delta`. To są dwa niezależne, ścisłe fakty geometryczno-algebraiczne.

Nie ma jeszcze dowodu, że współczynnik `r_scale` jest skurczem konkretnej krawędzi wynikającym z tej holonomii, ani że jest parametrem dynamiki Centroid. Co więcej, jednorodne skalowanie nie może zmienić kąta dwuściennego. Następny krok wymaga odzyskania Axis §8.5.9 i zapisania konstrukcji w jawnych współrzędnych/więzach.


## 11. Niezależne wyprowadzenie reprezentacji Centroid i pełnego `so(3))

Z definicji Centroid (dla `n=4`):
`M_i = I + e_i c_i^T`, gdzie `c_i = (1/4)1 - e_i`.
Niech `P = I - (1/4)11^T` będzie rzutem ortogonalnym na `V_ρ = 1^⊥), a `u_i = P e_i`.

Dla `x ∈ V_ρ` mamy `c_i^T x = -x_i`, zatem
`M_i x = x - x_i e_i`.
Po identyfikacji ilorazu `R⁴/span{1}` z `V_ρ` przez rzut P:
`ρ_B(M_i)x = P M_i x = x - (u_i^T x)u_i`,
czyli
`A_i := ρ_B(M_i) = I_{V_ρ} - u_i u_i^T`.

To od razu daje:
- `A_i` jest symetryczna;
- `||u_i||² = 3/4), więc widmo `A_i` to `{1,1,1/4}`;
- `u_i^T u_j = δ_ij - 1/4), więc dla `i ≠ j`, `u_i^T u_j = -1/4).

Komutator ma postać
`[A_i,A_j] = (u_i^T u_j)(u_i u_j^T - u_j u_i^T) = -(1/4)(u_i u_j^T-u_j u_i^T)`.
Jest więc antysymetryczny, a zatem należy do `so(V_ρ)`.

Co ważniejsze, nie tylko należy: komutatory rozpinają całe `so(3)`. Wektory `u₁,u₂,u₃` są liniowo niezależne, bo ich macierz Grama ma postać `I₃-(1/4)J₃` i wyznacznik `1/4 > 0`. Wobec tego `u₁∧u₂, u₁∧u₃, u₂∧u₃` tworzą bazę `Λ²V_ρ`. Odwzorowanie
`u∧v ↦ uv^T-vu^T`
jest izomorfizmem `Λ²V_ρ ≅ so(V_ρ)` w wymiarze 3. Stąd trzy komutatory `[A₁,A₂]`, `[A₁,A₃]`, `[A₂,A₃]` są liniowo niezależne i
`span{[A_i,A_j] : i<j} = so(V_ρ) ≅ so(3)`.

**Wniosek:** jeśli `ρ_B` w źródle Centroid jest tą naturalną reprezentacją ilorazową (co jest zgodne z podanymi w adnotacji symetrią i widmem `{1,1,1/4}`), to zdanie o rotacyjnej algebrze nie wymaga wyłącznie argumentu „antysymetryczne, więc należą do so(3)”: można dowieść mocniejszego wyniku, że komutatory generatorów rozpinają całe `so(3)`.

**Ograniczenie:** oryginalna definicja bazy B i konwencja zapisu `ρ_B` nie są w repozytorium. Wyprowadzenie jest kompletne dla naturalnej identyfikacji ilorazu z `1^⊥`; przed oznaczeniem zgodności z konkretną tabelą osi w §8.5.8 należy porównać macierze przez zmianę bazy/ortogonalne sprzężenie z oryginalnym źródłem.
