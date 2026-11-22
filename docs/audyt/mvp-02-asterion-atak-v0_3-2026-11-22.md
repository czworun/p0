# MVP-02 v0.3 — raport z ataku Δ Asteriona

Data: 2026-11-22  
Atakowany commit main: `6bc55f66e837e26b8dfd86a11f7e96dec3c7baaf`  
Specyfikacja: `docs/mvp-02-spec-v0_3.md`  
Blob specyfikacji: `0ea1078391c607ecea469c5cfd95760aad2ace15`  
Uzupełnienie A.6: `docs/mvp-02-spec-v0_3-aneks-a-uzupelnienie.md`  
Blob uzupełnienia: `57a822b301d00a7164eff51ad98ad20d5e6ff6c4`

## Zakres i rygor K6

Wykonano wyłącznie niezależne kontrole kombinatoryczne, geometryczne i algebraiczne dopuszczone przed bindem. Nie obliczano supremum, czasu τ, U_b, kill criterion ani żadnej trajektorii testu transportowego. Nie przeprowadzono modelu zerowego. Raport nie zawiera kodu jako dostawy.

---

# POLE 1 — Reprodukcje geometryczne i algebraiczne

## 1. BFS z tabeli ścian §0.3 — ✅ PASS

Graf zbudowano od zera z 20 trójek wierzchołków. Krawędź grafu ścian występuje dokładnie wtedy, gdy dwie trójki mają dokładnie dwa wspólne wierzchołki. Styk w jednym wierzchołku nie jest sąsiedztwem.

Wynik:
- graf ma 20 wierzchołków, 30 krawędzi, każdy stopień równy 3;
- graf jest spójny, średnica wynosi 5;
- rozkład 190 nieuporządkowanych par na dystansach 1–5: 30 / 60 / 60 / 30 / 10;
- kule z każdego wierzchołka na dystansach 1–5: 3 / 6 / 6 / 3 / 1;
- wykaz par dystansu 5 jest dokładnie zgodny ze specyfikacją:
  {f0,f19}, {f1,f15}, {f2,f12}, {f3,f11}, {f4,f14},
  {f5,f18}, {f6,f13}, {f7,f16}, {f8,f10}, {f9,f17}.

Kontrola niezależna: macierz dystansów z uzupełnienia A.6 jest symetryczna, ma zera na przekątnej i zgadza się z macierzą BFS na wszystkich 400 pozycjach. Nie znaleziono błędu w tabeli dystansów ani wykazie antypodów.

## 2. Chronologia §0.1 — ✅ PASS lokalnie; konflikt z fingerprintem R_gate

Dla wektorów kolumnowych zapis §0.1 jest spójny:
- chronologia aktualizacji: a, następnie b, następnie c, na końcu P0;
- czynnik działający pierwszy stoi po prawej;
- iloczyn jednej tetry: R_tetr = M_P0 · M_c · M_b · M_a.

Operator M_i ma wiersz aktywowany równy (1/4, 1/4, 1/4, 1/4), pozostałe wiersze są identycznościowe. Jego wyznacznik wynosi 1/4.

## 3. R_4 — ✅ PASS

Dla kolejności a → b → c → P0 otrzymano:
- widmo: 1; 0.1533478 ± 0.0740391i; 0.1347106;
- wyznacznik: 1/256;
- lewy wektor własny dla wartości 1, znormalizowany sumą współrzędnych: (0.1, 0.2, 0.3, 0.4), czyli S10 = (1,2,3,4)/10.

Ważna subtelność: odwrócenie kolejności czterech aktualizacji pozostawia widmo R_4 bez zmian, ale zmienia lewy wektor na (0.4, 0.3, 0.2, 0.1). Dlatego bramka musi sprawdzać jednocześnie widmo i lewy wektor, tak jak zapisano w §0.1.

## 4. R_gate — ❌ BLOKER: zamrożone rho_gate odpowiadają przeciwnej chronologii

Zrekonstruowałem 13-wymiarowy operator z 32 aktywacji dla każdej z pięciu bramek-konfiguracji, stosując dokładnie kolejność §0.1: dla każdej ściany a → b → c → P0, a ściany w kolejności rosnącej.

Otrzymane wartości |lambda_2|:
- G0: 0.227446764923;
- G1: 0.197320310603;
- G2: 0.258668147953;
- G3: 0.260160125728;
- G4: 0.218966881794.

Nie są to wartości zamrożone w §0.3: 0.271135751587; 0.268753058672; 0.328097227134; 0.287367993554; 0.298483949744.

Kontrola diagnostyczna: po odwróceniu kolejności aktualizacji wewnątrz każdej ściany — P0 → c → b → a — otrzymuje się kolejno:
- G0: 0.271135751587;
- G1: 0.268753058672;
- G2: 0.328097227134;
- G3: 0.287367993554;
- G4: 0.298483949744.

To zgodność z fingerprintami zapisanymi w §0.3 do wszystkich podanych cyfr. Obie kolejności mają ten sam wyznacznik 4^-32 = 256^-8. Rozbieżność nie jest więc skutkiem wyznacznika ani obcięcia numerycznego: zapisane rho_gate pochodzą z odwrotnej chronologii niż ta, którą nakazuje §0.1.

**Errata wymagana:** albo zachować chronologię §0.1 i przeliczyć/zamrozić na nowo wszystkie pięć rho_gate, albo zmienić chronologię w całej specyfikacji i odpowiednio zmienić bramkę R_4 (jej lewy wektor). Nie wolno pozostawić obecnego zestawu: obecnie nie da się jednocześnie przejść R_4 i pięciu checkpointów R_gate.

## 5. L_dod i L_eq — ✅ PASS

Z tabeli ścian zbudowano spójnie zorientowaną macierz brzegu B: C2 → C1, rozmiar 30×20. Otrzymano:
- B^T·B = L_dod = 3I − A_dod;
- ślad L_dod = 60;
- jądro L_dod jest jednowymiarowe i generowane przez stały wektor ścian;
- L_dod jest dodatnio półokreślony;
- rząd B wynosi 19, a ker(B) jest dokładnie przestrzenią stałych na C2.

Dla L_eq = B·B^T:
- rząd wynosi 19, a jądro w całym C1 ma wymiar 11;
- ślad L_eq = 60;
- widmo dodatnie, z krotnościami:
  3×(3−sqrt(5)); 5×2; 4×3; 4×5; 3×(3+sqrt(5));
- widmo na V_cyc jest identyczne z widmem L_dod po usunięciu stałego modu;
- tożsamość B·L_dod = L_eq·B zachodzi dokładnie w odtworzonym rachunku.

Odtworzone częstości i wartości dziesiętne:
- sqrt(3−sqrt(5)) = 0.874032;
- sqrt(2) = 1.414214;
- sqrt(3) = 1.732051;
- sqrt(5) = 2.236068;
- sqrt(3+sqrt(5)) = 2.288246.

Rezonans sqrt(3+sqrt(5)) = sqrt(3−sqrt(5)) + sqrt(2) jest prawidłowy. Typy macierzy i transpozycje z §0.4 są spójne.

## 6. L_cyc — ❌ BLOKER: jawna konstrukcja nie daje checkpointu 494/3

Przyjąłem dokładnie interpretację wynikającą z §0.4(i):
- krawędzie ikosaedru w porządku par rosnących indeksów, orientacja od niższego do wyższego indeksu;
- signed incidence D: wierzchołki × krawędzie;
- Q_im jako ortonormalna baza im(D^T), rząd 11;
- P_cyc = I − Q_im·Q_im^T, czyli ortogonalny projektor rzędu 19 na ker(D);
- unsigned incidence H: wierzchołki × krawędzie;
- L_line = 10I − H^T·H, laplasjan grafu liniowego o stopniu 8.

Dla zapisanego w specyfikacji L_cyc = P_cyc·L_line·P_cyc otrzymałem:
- rząd P_cyc = 19;
- ślad L_cyc = 162.5333333333 = 2438/15;
- niezerowe wartości własne: 5.115582; 5.615716; 6.598424; 6.755033; 7.333333; 8 (dwukrotnie); 8.319194; 8.396051; 8.4; 10 (dziewięciokrotnie).

To nie jest checkpoint ze specyfikacji: ślad 164.6667 = 494/3 oraz widmo z §0.4(i). Nie jest to różnica zaokrąglenia. W zapisie brakuje też jawnej definicji Q_im i występuje kolizja symbolu B: wcześniej B oznacza 30×20 differential_2, natomiast formuła L_line wymaga macierzy incidence 12×30.

**Errata wymagana:** rozdzielić symbole macierzy brzegowej ściana→krawędź i macierzy incidence wierzchołek→krawędź; jawnie zdefiniować Q_im; następnie albo zachować formułę P_cyc·L_line·P_cyc i skorygować checkpoint, albo podać inną, w pełni reprodukowalną konstrukcję L_cyc. Obecna specyfikacja nakazuje operator, którego własności liczbowe nie zgadzają się z jej checkpointem.

## 7. Wektory s_G / a_G — ✅ PASS algebraiczny

Dla każdej konfiguracji odtworzyłem dwie orbity czterech ścian pod właściwą grupą obrotów A4 stabilizującą konfigurację. U1 jest orbitą zawierającą najmniejszą ścianę w porządku leksykograficznym; U2 jest drugą orbitą. Otrzymane podziały:

- G0: U1 = {f0,f11,f13,f17}; U2 = {f3,f6,f9,f19};
- G1: U1 = {f0,f10,f14,f16}; U2 = {f4,f7,f8,f19};
- G2: U1 = {f1,f9,f12,f16}; U2 = {f2,f7,f15,f17};
- G3: U1 = {f1,f8,f11,f18}; U2 = {f3,f5,f10,f15};
- G4: U1 = {f2,f6,f14,f18}; U2 = {f4,f5,f12,f13}.

Każda ściana brzegowa jest już cyklem, więc projekcja na V_cyc nie zmienia sum U1 ani U2. Dla s_G = U1+U2 i a_G = U1−U2:
- norma do kwadratu s_G = 24 i norma do kwadratu a_G = 24;
- iloczyn skalarny s_G·a_G = 0;
- L_eq·s_G = 5s_G;
- L_eq·a_G = 3a_G.

Macierz Grama wektorów s_G ma 24 na przekątnej i −6 poza przekątną; rząd rodziny wynosi 4, a suma pięciu s_G jest równa zero. To potwierdza N_sąs = 12 i zależność 6−N_sąs = −6.

Macierz Grama a_G ma 24 na przekątnej; poza przekątną znaki zależą od przyjętej konwencji orbit. Suma a_G nie jest zerem — zgodnie z wycofaniem tej kontroli w §2.2 nie należy jej ponownie wprowadzać.

Wektory są czysto modalne: s_G należy do wartości własnej 5 (częstość sqrt(5)), a_G do wartości własnej 3 (częstość sqrt(3)). Znak i wybór U1 są zgodne z regułą §2.2. Dla pełnej reprodukowalności warto przenieść jawne podziały U1/U2 z niniejszego punktu do specyfikacji.

## 8. Konstrukcja D3: cechowanie soma-zero, cele jednowymiarowe, parowanie przez B — ✅ PASS

Nie znalazłem nowego artefaktu D3 w głównej konstrukcji:
- q_f = e_f − (1/20)·1 należy do podprzestrzeni soma-zero;
- L_dod zachowuje soma-zero, a jego jądro stałych jest usunięte przez cechowanie;
- każdy cel powierzchniowy span{q_h} ma wymiar 1;
- każdy cel wnętrza span{omega_h} ma wymiar 1;
- B·1 = 0, więc B·q_f = B·e_f = omega_f;
- U = B·L_dod^(-1/2) jest izometrią soma-zero na V_cyc, a U·L_dod = L_eq·U.

Wynika z tego, że kanały nie są dwiema niezależnymi dynamikami liniowymi. Są izometrycznie powiązanymi realizacjami tej samej dynamiki, przy odmiennym położeniu celu i wadze metrycznej. §2.1 wypowiada tę koncesję poprawnie.

## 9. Kolejka sanity §3 — statusy obiektów 1–8

| Obiekt | Status | Wynik |
|---|---|---|
| 1. M_local | ✅ PASS | wiersz aktywny 1/4; det = 1/4 |
| 2. R_4 | ✅ PASS | widmo i lewy wektor S10 zgodne |
| 3. R_gate | ❌ FAIL | fingerprinty wymagają odwróconej chronologii |
| 4. L_cyc | ❌ FAIL | jawny projektor daje ślad 2438/15, nie 494/3 |
| 5. L_dod | ✅ PASS | ślad 60, jądro stałe, PSD |
| 6. L_eq | ✅ PASS | rząd 19 na V_cyc, ślad 60, widmo zgodne z L_dod po cechowaniu |
| 7. s_G/a_G | ✅ PASS | Gram, rząd, suma s_G i czystość sektorowa zgodne |
| 8. czysto modalne cos^2 | ✅ PASS | dla x z własnej wartości λ: x(t)=cos(sqrt(λ)·t)x, zatem każdy projektor celu daje C·cos^2(sqrt(λ)·t) |

---

# POLE 2 — Protokół numeryczny Aneksu A i kontrola uzupełnienia A.6

## 1. Uzupełnienie A.6 — ✅ PASS dla danych algebraicznych

Macierz 20×20 odległości w sekcji 2 uzupełnienia została porównana z macierzą BFS. Wszystkie 400 wpisów są zgodne.

Wagi odtworzyłem niezależną diagonalizacją symetrycznego L_dod i projekcją na klastry wartości własnych. Reprezentantami były (f0,f1), (f0,f3), (f0,f10), (f0,f12), (f0,f19). Zastosowane wzory:
- A_a = z_h^T·P_a·z_f;
- g_a,surf = (20/19)·A_a;
- g_a,int = (lambda_a/3)·A_a.

Odtworzone wagi, zaokrąglone do czterech cyfr znaczących:

| Dystans | Kanał | g1 | g2 | g3 | g4 | g5 |
|---|---|---:|---:|---:|---:|---:|
| d1 | powierzchnia | 0.1177 | 0.08772 | 0 | −0.1404 | −0.1177 |
| d1 | wnętrze | 0.02847 | 0.05556 | 0 | −0.2222 | −0.1951 |
| d2 | powierzchnia | 0.05263 | −0.08772 | −0.1053 | 0.03509 | 0.05263 |
| d2 | wnętrze | 0.01273 | −0.05556 | −0.1000 | 0.05556 | 0.08727 |
| d3 | powierzchnia | −0.05263 | −0.08772 | 0.1053 | 0.03509 | −0.05263 |
| d3 | wnętrze | −0.01273 | −0.05556 | 0.1000 | 0.05556 | −0.08727 |
| d4 | powierzchnia | −0.1177 | 0.08772 | 0 | −0.1404 | 0.1177 |
| d4 | wnętrze | −0.02847 | 0.05556 | 0 | −0.2222 | 0.1951 |
| d5 | powierzchnia | −0.1579 | 0.2632 | −0.2105 | 0.2105 | −0.1579 |
| d5 | wnętrze | −0.03820 | 0.1667 | −0.2000 | 0.3333 | −0.2618 |

Wagi zgadzają się z uzupełnieniem A.6 do czterech cyfr znaczących. Wszystkie 15 współczynników na orbitę odtwarza się z relacji c(a,a)=g_a^2 oraz c(a,b)=2g_a·g_b; zestawy współczynników z uzupełnienia są zgodne na publikowanej dokładności.

**Szczególne zera:** g3 = 0 na d1 i d4 w obu kanałach. Są to dokładne zera spektralne, nie efekty zaokrąglenia. Współczynniki wszystkich wyrazów zawierających indeks 3 są wtedy zerowe. Efektywnie te dwa przypadki mają mniej aktywnych częstości; nie należy traktować ich jako pięciomodalnych w raportowaniu.

Kontrole wycieku:
- powierzchnia: suma wag = −1/19, kwadrat = 1/361 dla wszystkich pięciu dystansów;
- wnętrze: suma wag = −1/3 i kwadrat = 1/9 na d1; suma wag = 0 na d2–d5.

Nie stwierdziłem błędu arytmetycznego w wagach, współczynnikach ani macierzy dystansów uzupełnienia.

## 2. Protokół fazowy A.3 — matematyczna podstawa ✅; certyfikacja numeryczna 🔍

Relacja rezonansowa omega5 = omega1 + omega2 jest poprawna. Cztery niezależne nad Q częstości mogą być zapisane przez bazę {sqrt(2), sqrt(3), sqrt(5), sqrt(10)}. Stąd domknięcie orbity fazowej rzeczywiście jest podtorem:
T_theta = {theta w T^5 : theta5 = theta1 + theta2 mod 2pi},
o wymiarze 4. To rozstrzygnięcie poprawnie usuwa błędne założenie o wspólnym okresie.

Pozostaje luka w procedurze numerycznej:
- siatka 120^4 wymaga 207 360 000 ewaluacji na jedną funkcję F; ze względu na symetrię można redukować liczbę odrębnych funkcji do pięciu orbit, ale koszt i sposób przetwarzania nadal powinny być jawne;
- trzy zagęszczenia siatki od węzła o największej wartości nie stanowią same przez się certyfikatu maksimum globalnego;
- nie zdefiniowano dokładnie obszaru sąsiedztwa, który jest przeszukiwany w każdej rundzie zagęszczania, sposobu traktowania granic torusa ani kryterium zakończenia;
- brak oszacowania błędu siatki lub górnego ograniczenia różnicy między maksimum ciągłym a znalezioną wartością.

**Zalecenie:** zapisać deterministyczny obszar zagęszczania i dodać certyfikat błędu globalnego (np. oszacowanie Lipschitza/gradientu na komórkach albo równoważną kontrolę przedziałową). Bez niego wynik z A.3 jest reprodukowalnym przybliżeniem według zadanej siatki, nie certyfikowanym supremum.

## 3. Protokół τ A.4 — ❌ BLOKER logiczny dla „pierwszego przekroczenia”

Skan 4000 węzłów jest dobrze określonym sposobem lokalizacji kandydackiego przedziału, ale nie daje automatycznie gwarancji pierwszego przekroczenia:
- zmiana znaku na końcach przedziału gwarantuje istnienie co najmniej jednego przecięcia, nie to, że jest to pierwsze przecięcie;
- funkcja udział(t) może przekroczyć próg i wrócić poniżej między dwoma węzłami siatki; pierwszy przekroczony węzeł może więc należeć do późniejszego epizodu;
- zwykła bisekcja na przedziale z przeciwnymi znakami może znaleźć późniejsze przecięcie, jeśli wewnątrz przedziału występuje kilka przecięć.

Drugi problem dotyczy restartów. Gęstość orbity i próg niższy niż supremum zapewniają istnienie przekroczenia dla odpowiednich funkcji, ale nie dają ograniczenia czasu pierwszego przekroczenia do 4·T_sk. Brak przekroczenia po trzech oknach nie dowodzi sam przez się błędu implementacji. Dodatkowo przy podwajaniu T_sk i stałej liczbie 4000 próbek krok siatki też się podwaja, więc skan staje się mniej rozdzielczy.

Trzeci problem: reguła „pierwsze przekroczenie przed pierwszym węzłem siatki ⇒ τ=0 z flagą” utożsamia dodatni czas z zerem. Jeżeli udział(0) < theta, ale przekroczenie wystąpiło dla 0<t<dt, to rzeczywiste τ jest dodatnie. τ=0 powinno wynikać wyłącznie z warunku B4: udział(0) ≥ theta. W pozostałym przypadku należy zwrócić przedział lewostronnie ocenzurowany albo wykonać adaptacyjne zagęszczenie od t=0.

**Zalecenie:** rozdzielić trzy stany: (a) dokładne τ=0 z B4; (b) dodatnie τ z izolowanym pierwszym przekroczeniem; (c) nierozstrzygnięte τ<dt, jawnie oznaczone jako cenzurowane — bez zastępowania go zerem. Dla pierwszego przekroczenia potrzebna jest kontrola wszystkich wcześniejszych komórek (np. ograniczeniem przedziałowym), nie tylko bisekcja na pierwszej parze próbek o przeciwnych znakach.

Dodatkowo sformułowanie „half-up po ucięciu do 2 cyfr znaczących” jest niejednoznaczne. Należy zapisać standardową regułę wprost: zachować dwie pierwsze cyfry znaczące, sprawdzić trzecią i zaokrąglić w górę przy remisie 5; bez wcześniejszego obcinania, które usuwałoby cyfrę rozstrzygającą.

---

# POLE 3 — Teza fizyczna

Algebra v0.3 nie rozstrzyga, że fizycznym nośnikiem transportu jest przepływ krawędziowy w V_cyc. Pokazuje natomiast, że kanał powierzchniowy i kanał wnętrza są izometrycznie powiązanymi realizacjami tej samej dynamiki liniowej. Ich różnica w mierze może wynikać z metryki, przeskalowania modów oraz położenia jednowymiarowego projektora celu względem podprzestrzeni własnych.

W konsekwencji test może badać, czy określone sprzężenie metryki i celu daje systematycznie inny czas detekcji dla par antypodalnych niż dla null. Sam wynik dodatni nie byłby jednak samodzielnym dowodem na ontologiczny lub fizyczny „nośnik” transportu. Do takiego wniosku potrzebne byłoby niezależne uzasadnienie, że wybrana reprezentacja odpowiada mierzalnemu obiektowi fizycznemu, a nie tylko wygodnej realizacji algebraicznej.

Status tezy o nośniku: 💡 hipoteza fizyczna, nie wynik algebraiczny. Koncesja metryczna §2.1 jest prawidłowa i powinna pozostać centralnym ograniczeniem interpretacji. Nie wykonywano rachunku transportowego, więc nie ma tu wyniku za ani przeciw H_b.

---

## Werdykt ataku Δ

**v0.3: częściowy PASS algebraiczny, NIE GOTOWA do bindu v1.0.**

Zamknięte:
- BFS i wszystkie 10 par antypodalnych;
- macierz dystansów A.6;
- wagi i współczynniki A.6, w tym g3=0 na d1 i d4;
- chronologia lokalna §0.1;
- M_local i R_4;
- L_dod, L_eq, relacja przez B;
- s_G/a_G i czysto modalne sanity;
- brak artefaktu D3 w cechowaniu soma-zero i celach 1D.

Blokery przed bindem:
1. rho_gate w §0.3 odpowiada odwrotnej chronologii niż §0.1;
2. L_cyc z jawnego wzoru §0.4(i) nie daje checkpointu 494/3;
3. protokół A.3 nie certyfikuje globalnego maksimum;
4. protokół A.4 nie gwarantuje wykrycia pierwszego przekroczenia, a restart 4·T_sk nie ma uzasadnionego ograniczenia;
5. wymaga doprecyzowania symbol incidence użyty w L_line oraz definicja Q_im;
6. reguła zaokrąglania half-up wymaga jednoznacznego zapisu.

**Rekomendacja:** poprawić najpierw dwie bramki sanity (R_gate i L_cyc), następnie uszczelnić procedury A.3/A.4. Dopiero potem zamrażać v1.0 i bind. K6 pozostaje nienaruszone.

