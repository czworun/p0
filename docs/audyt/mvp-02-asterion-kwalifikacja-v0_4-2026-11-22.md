# MVP-02 v0.4 — kwalifikacja Asteriona

Data: 2026-11-22  
Atakowana specyfikacja: `docs/mvp-02-spec-v0_4.md`  
Commit specyfikacji: `858f9394bc95f6e0561fc06d333f5fba8609cff6`  
Blob specyfikacji: `c4ef2d4174735fa1dd30a8235cdd828748b26846`  
Atakowane uzupełnienie: `docs/mvp-02-spec-v0_4-aneks-a-uzupelnienie.md`  
Commit uzupełnienia: `1ffdd3d4428b74c9306464cfefd02579f8c6f3d4`  
Blob uzupełnienia: `e68906bed162eb6f0aecec416c6bba9e1b655482`

## Granice kwalifikacji

Wykonano wyłącznie rachunki algebraiczne i kombinatoryczne. Nie wyznaczano theta, sup, tau, U_b, F_r ani kill. Nie uruchamiano żadnej trajektorii transportowej ani modelu zerowego. K6 zachowane. Raport nie dostarcza kodu.

---

# POLE 1 — Atak na protokoły A.3 i A.4

## A.3 — certyfikat Lipschitza

**Wynik: 🔍 CZĘŚCIOWY PASS; certyfikat w obecnej postaci nie jest globalnie ważny.**

### Co jest poprawne

Po podstawieniu theta5 = theta1 + theta2 każdy składnik udziału ma postać c(a,b)·cos(k_a·theta)·cos(k_b·theta), gdzie k1, k2, k3, k4 są osiami współrzędnych, a k5 = (1,1,0,0).

Dla metryki torusa indukowanej normą L1, czyli odległością będącą sumą modułów czterech różnic fazowych, oszacowanie L_F = 2·suma(|c(a,b)|) jest poprawną górną granicą modułu każdej składowej gradientu. Uwzględnienie rezonansu nie wymaga więc automatycznie większego współczynnika niż 2. Dla pojedynczego składnika z indeksem 5 pochodne po theta1 i theta2 są sprzężone przez tę samą fazę; ich składowe nie przekraczają osobno 2·|c(a,b)|. Zatem sam wzór na L_F może pozostać.

Dla jednorodnej siatki o kroku h w każdej z czterech współrzędnych każdy punkt torusa leży w odległości L1 nie większej niż 4·h/2 = 2h od węzła siatki. Stąd poprawne jest oszacowanie:
sup(F) ≤ M_grid + 2·L_F·h,
gdzie M_grid jest maksimum wartości na CAŁEJ siatce globalnej.

### Bloker A3-1 — lokalne zagęszczenie nie zmniejsza globalnego promienia pokrycia

Specyfikacja wykonuje globalną siatkę 120^4, a następnie lokalne zagęszczenie od węzła o największej wartości. Po trzech lokalnych rundach wpisuje krok końcowy h/4^3 do certyfikatu globalnego:
sup ≤ M + L_F·(h/4^3)/2·4.

To przejście nie jest uzasadnione. Lokalna siatka wokół jednego węzła nie pokrywa całego T_theta z krokiem h/4^3. Poza zagęszczonym obszarem nadal obowiązuje co najwyżej globalny promień pokrycia pierwotnej siatki h. Użycie h/4^3 w globalnym certyfikacie może zaniżyć górne ograniczenie i nie certyfikuje maksimum na całym podtorusie.

**Errata wymagana — jedna z dwóch dróg:**
1. zachować globalną siatkę h i używać w certyfikacie h, albo
2. zastosować globalne/adaptacyjne zagęszczanie wszystkich komórek, których górne ograniczenie może przekraczać aktualne dolne ograniczenie maksimum; zakończyć dopiero wtedy, gdy każda komórka torusa jest albo odrzucona, albo pokryta siatką o zadanym promieniu.

Wariant 2 może być branch-and-bound z lokalnymi promieniami komórek. Nie wystarczy zagęścić wyłącznie otoczenia najlepszego węzła.

### Bloker A3-2 — niepełna reguła zakończenia i definicja M

Protokół dopuszcza do pięciu dodatkowych rund, jeśli szerokość certyfikatu przekracza 10^-4, ale nie określa wyniku, gdy po piątej dodatkowej rundzie szerokość nadal przekracza 10^-4. W takim przypadku trzeba zwrócić status NIE-CERTYFIKOWANE i zakazać użycia tej wartości do wyznaczenia theta.

Należy też zdefiniować M jako największą wartość spośród wszystkich faktycznie ocenionych punktów, w tym globalnej siatki i punktów zagęszczania. Nie wolno bezwarunkowo utożsamiać M z wynikiem lokalnego optymalizatora, który może zwrócić punkt gorszy od najlepszego punktu startowego.

### Adnotacja E5

Dla d1 i d4 współczynnik g3 jest dokładnie zerowy, więc funkcja nie zależy od theta3 i rzeczywisty wymiar torusa fazowego spada do 3. Pełna siatka czterowymiarowa pozostaje poprawna, ale ma dokładnie 120-krotny nadmiar kosztu. To nie jest błąd matematyczny ani blocker, lecz koszt, który warto jawnie zachować w rejestrze.

## A.4 — certyfikacja pierwszego przekroczenia

**Wynik: 🔍 CZĘŚCIOWY PASS; oszacowanie Lipschitza jest poprawne, ale algorytm pierwszego przekroczenia nie jest jeszcze kompletny.**

### Co jest poprawne

Dla udziału będącego sumą 15 składników c(a,b)·cos(omega_a·t)·cos(omega_b·t), stała
L_t = suma(|c(a,b)|·(omega_a + omega_b))
jest poprawną globalną granicą modułu pochodnej czasowej.

Dla dowolnego t w przedziale [t_k,t_(k+1)] odległość od bliższego końca nie przekracza Δt/2. Zatem:
udział(t) ≤ max(udział(t_k), udział(t_(k+1))) + L_t·Δt/2.
Jeżeli prawa strona jest ściśle mniejsza od theta, przedział jest poprawnie certyfikowany jako wolny od przekroczenia.

Warunek udział(0) ≥ theta ⇒ tau = 0 z flagą PRZECIEK jest spójny z definicją B4. Nie należy zastępować nim przypadku udział(0) < theta.

### Bloker A4-1 — „bisekcja wszystkich niecertyfikowanych przedziałów” nie jest algorytmem pierwszego trafienia

Specyfikacja nie podaje dokładnej reguły wyboru i dalszego dzielenia przedziałów, które:
- mają oba końce poniżej theta,
- nie spełniają warunku certyfikacji g_k < theta,
- mogą zawierać ukryte przekroczenie i późniejszy powrót poniżej progu.

Zwykła bisekcja przedziału z przeciwnymi znakami znajduje pewne przecięcie, ale bez dodatkowej kontroli nie gwarantuje pierwszego przecięcia. W jednym przedziale może wystąpić więcej niż jedno przekroczenie. Możliwe jest też styczne dotknięcie progu, bez zmiany znaku na końcach.

**Errata wymagana:** zapisać deterministyczny algorytm chronologicznego branch-and-bound:
1. przetwarzać niecertyfikowane przedziały od najwcześniejszego czasu;
2. dzielić najwcześniejszy niecertyfikowany przedział na dwie połowy;
3. jeżeli lewa połowa zostanie certyfikowana jako wolna od przekroczenia, przejść do prawej; w przeciwnym razie kontynuować rekurencję w lewej połowie;
4. uznać przedział za bracket pierwszego przekroczenia dopiero wtedy, gdy wszystkie wcześniejsze przedziały są certyfikowane jako wolne od przekroczenia;
5. jeżeli przedział pozostaje niecertyfikowany przy osiągnięciu tolerancji, zwrócić NIEROZSTRZYGNIĘTY PRZEDZIAŁ, nie deklarować tau jako certyfikowanego.

Trzeba jawnie opisać przypadek stycznego dotknięcia theta. Obecny Lipschitz upper bound może nie rozstrzygnąć takiego przypadku w skończonej liczbie podziałów. Wtedy prawidłowy wynik to nierozstrzygnięcie w zadanej tolerancji albo dodatkowy certyfikat dolny/warunek stacjonarności, a nie wymuszone wskazanie przecięcia.

### Bloker A4-2 — restart i siatka 4000

Nie jest jasne, czy przy oknach T_sk, 2·T_sk, 4·T_sk, 8·T_sk liczba 4000 oznacza:
- 4000 przedziałów na całym nowym, wydłużonym oknie, co podwaja krok przy każdym restarcie, czy
- zachowanie pierwotnego kroku Δt = T_sk/4000 i dokładanie kolejnych przedziałów tylko na nowym fragmencie.

Pierwsza interpretacja pogarsza rozdzielczość w czasie i może utracić wcześniejsze wąskie przekroczenie. Należy zamrozić drugą interpretację: krok bazowy pozostaje T_sk/4000 na wszystkich restartach; wcześniej sprawdzone przedziały zachowują swoje certyfikaty, a skan dopisuje wyłącznie nowy zakres. Restart nie może unieważniać wcześniejszej certyfikacji.

Flaga PRAWO-OCENZUROWANE po 8·T_sk jest poprawną kategorią proceduralną, o ile raport jasno mówi, że jest to cenzura administracyjna okna obserwacji, a nie dowód braku przekroczenia w całym t ≥ 0.

### Bloker A4-3 — szerokość 10^-4 nie gwarantuje dwóch cyfr znaczących

Deklaracja „10^-4 gwarantuje 2 cyfry znaczące dla tau ≥ 0.01” jest fałszywa. Przykład przedziału [0.01045, 0.01054] ma szerokość 0.00009 < 10^-4, ale końce zaokrąglają się half-up do dwóch cyfr znaczących odpowiednio do 0.010 i 0.011.

**Errata wymagana:** punktowy wynik tau z dwiema cyframi znaczącymi wolno podać jako certyfikowany tylko wtedy, gdy oba końce ostatniego przedziału bisekcji zaokrąglają się half-up do tej samej wartości. W przeciwnym razie trzeba kontynuować bisekcję albo raportować wyłącznie przedział i flagę NIEROZSTRZYGNIĘTY-ROUNDING. Kryterium 10^-4 pozostaje kryterium szerokości przedziału, ale nie zastępuje kontroli stabilności zaokrąglenia.

### Bloker A4-4 — zapis half-up jest niejednoznaczny

Fraza „half-up po ucięciu do 2 cyfr znaczących” może oznaczać przedwczesne obcięcie cyfry rozstrzygającej. Standardowa reguła powinna brzmieć: ustalić wykładnik dziesiętny, zachować dwie pierwsze cyfry znaczące, użyć trzeciej cyfry do zaokrąglenia; przy trzeciej cyfrze równej 5 zaokrąglić w górę. Bez uprzedniego obcinania wartości do dwóch cyfr.

### Status kategorii cenzury i TAU-MAŁE

- LEWO-OCENZUROWANE [0,t1]: poprawna kategoria raportowania, jeżeli przekroczenie jest potwierdzone w pierwszym przedziale, a dokładniejszy pierwszy moment nie został wyznaczony. Nie wolno podawać jednej liczby tau jako certyfikowanej.
- PRAWO-OCENZUROWANE: poprawna kategoria po wyczerpaniu ustalonego okna; nie oznacza tau = nieskończoność.
- tau = 0: wyłącznie przy dokładnym warunku B4 udział(0) ≥ theta.
- TAU-MAŁE: flaga < 0.01 jest użyteczna, lecz powinna być nadawana na podstawie całego przedziału [lo,hi]. Jeśli przedział przecina 0.01, status „małe/nie-małe” również jest nierozstrzygnięty.
- Dla tau < 0.01 podanie przedziału obok dwóch cyfr jest właściwe, ale dwie cyfry nie mogą być przedstawiane jako potwierdzone, jeśli oba końce przedziału nie dają tego samego zaokrąglenia.

---

# POLE 2 — Reprodukcje geometryczne i algebraiczne

## 1. BFS z tabeli ścian §0.3 — ✅ PASS

Graf odtworzono wyłącznie z 20 trójek ścian. Dwie ściany są sąsiadami wtedy i tylko wtedy, gdy ich trójki mają dokładnie dwa wspólne wierzchołki.

Wynik:
- 20 wierzchołków grafu, 30 krawędzi;
- stopień każdego wierzchołka = 3;
- graf spójny, średnica = 5;
- rozkład nieuporządkowanych par dla dystansów d1 do d5: 30 / 60 / 60 / 30 / 10;
- kule dystansu dla każdej ściany: 3 / 6 / 6 / 3 / 1;
- pary antypodalne (dystans 5):
  {f0,f19}, {f1,f15}, {f2,f12}, {f3,f11}, {f4,f14},
  {f5,f18}, {f6,f13}, {f7,f16}, {f8,f10}, {f9,f17}.

## 2. Niezależna kontrola uzupełnienia A.6 — ✅ PASS

Macierz dystansów sekcji 2 uzupełnienia porównano wpis po wpisie z macierzą BFS. Wszystkie 400 pozycji zgadzają się; nie ma ani jednego rozbieżnego elementu.

Tablica przecięć z sekcji 6 uzupełnienia również zgadza się z grafem:
- b = (3, 2, 1, 1, 1);
- c = (1, 1, 1, 2, 3);
- a dla warstw 0 do 5 = (0, 0, 1, 1, 0, 0).

Dla wszystkich 20 możliwych źródeł i wszystkich wierzchołków każdej warstwy liczby sąsiadów w warstwach poprzedniej i następnej są zgodne z tablicą przecięć. Nie jest to wyłącznie zgodność jednego wiersza bazowego.

## 3. L_cyc według jawnych definicji ORIENT-02-A — ✅ PASS

Odtworzenie:
- krawędzie: 30 par w porządku combinations(range(12),2);
- D_inc: 12×30, dla krawędzi (i,j), i<j: +1 przy i, −1 przy j;
- H_inc: 12×30, bez znaków;
- ranga D_inc = 11;
- Q_im: ortonormalna baza obrazu D_inc^T;
- P_cyc = I − Q_im·Q_im^T, ranga 19;
- L_line = 10I − H_inc^T·H_inc;
- L_cyc = P_cyc·L_line·P_cyc.

Otrzymane 19 niezerowych wartości własnych:
5.11558182; 5.61571569; 6.59842412; 6.75503345; 7.33333333; 8 (krotność 2); 8.31919352; 8.39605140; 8.4; 10 (krotność 9).

Ranga L_cyc = 19.

Momenty obliczone z jawnej konstrukcji:
- ślad = 2438/15 = 162.5333333333;
- ślad kwadratu = 323756/225 = 1438.9155555556;
- ślad sześcianu = 44162552/3375 = 13085.2005925926.

Widmo i wszystkie trzy momenty zgadzają się z ORIENT-02-A. Nie użyto orientacji ścian jako substytutu zadanej orientacji krawędzi.

## 4. Partycje U1/U2 i automorfizmy — ✅ PASS

Niezależna enumeracja automorfizmów grafu ścian dała dokładnie 120 elementów. Po podniesieniu do automorfizmów grafu wierzchołkowego ikosaedru i klasyfikacji względem orientacji przestrzeni otrzymano:
- 60 symetrii właściwych (obroty);
- 60 symetrii niewłaściwych.

Terminologiczna uwaga Z2: „60 odbić” należy rozumieć jako 60 symetrii niewłaściwych, a nie 60 zwykłych odbić w płaszczyznach. Nie każdy element niewłaściwy jest odbiciem płaszczyznowym.

Dla każdej konfiguracji G stabilizator w grupie obrotów ma rząd 12. Jego orbity na ośmiu ścianach konfiguracji są dokładnie partycjami U1/U2 ze specyfikacji:

- G0: U1 = {0,11,13,17}; U2 = {3,6,9,19}.
- G1: U1 = {0,10,14,16}; U2 = {4,7,8,19}.
- G2: U1 = {1,9,12,16}; U2 = {2,7,15,17}.
- G3: U1 = {1,8,11,18}; U2 = {3,5,10,15}.
- G4: U1 = {2,6,14,18}; U2 = {4,5,12,13}.

W każdym przypadku orbita zawierająca najmniejszą ścianę leksykograficznie jest U1. Reguła znaku jest więc jednoznaczna i odtwarza wszystkie pięć podziałów.

### Stabilizatory uporządkowanych par ścian

Dla reprezentantów orbit odległościowych otrzymano:

| Dystans | Reprezentant | Rząd stabilizatora | Rozmiar orbity |
|---|---|---:|---:|
| d1 | (f0,f1) | 2 | 60 |
| d2 | (f0,f3) | 1 | 120 |
| d3 | (f0,f10) | 1 | 120 |
| d4 | (f0,f12) | 2 | 60 |
| d5 | (f0,f19) | 6 | 20 |

To zgadza się z |I_h| = 120 oraz z licznościami uporządkowanych par 60 / 120 / 120 / 60 / 20.

---

# POLE 3 — Teza fizyczna

Wyniki tej kwalifikacji są algebraiczne i kombinatoryczne. Nie dostarczają dowodu, że przepływ krawędziowy V_cyc jest fizycznym nośnikiem transportu. Specyfikacja sama poprawnie przyznaje w §2.1, że kanał powierzchniowy i wnętrza są izometrycznie powiązanymi realizacjami tej samej dynamiki liniowej, a miara porównuje sprzężenie metryki i położenia projektora celu.

W konsekwencji nawet przyszły wynik różnicujący czasy detekcji nie będzie samodzielnym dowodem ontologicznym na „nośnik”. Będzie wynikiem o ważeniu sektorów i geometrii celu w dwóch równoważnie sprzężonych realizacjach. Teza o fizycznym nośniku pozostaje 💡 hipotezą wymagającą niezależnego mostu do obserwabli fizycznej.

---

## Werdykt kwalifikacji v0.4

**Geometria i algebra: ✅ PASS. Protokoły A.3/A.4: 🔍 CZĘŚCIOWY PASS — wymagają errat przed bindem v1.0.**

Domknięte:
- BFS, rozkład par, kule i wykaz antypodów;
- wszystkie 400 wpisów macierzy dystansów;
- tablica przecięć grafu dwunastościanu;
- L_cyc ORIENT-02-A, ranga, widmo i trzy momenty;
- 120 automorfizmów, pięć partycji U1/U2 i rzędy stabilizatorów par;
- chronologia i konwencja montażu §0.1.

Do poprawy:
1. A.3: nie wolno używać lokalnego kroku zagęszczenia jako globalnego promienia pokrycia torusa;
2. A.3: jawnie określić M i wynik po wyczerpaniu maksymalnej liczby rund bez certyfikatu;
3. A.4: zapisać deterministyczną chronologiczną procedurę dzielenia wszystkich wcześniejszych niecertyfikowanych przedziałów, także przy stycznym dotknięciu progu;
4. A.4: zamrozić zachowanie kroku T_sk/4000 podczas restartów;
5. A.4: wymagać zgodności zaokrąglenia obu końców przedziału, nie tylko szerokości < 10^-4;
6. A.4: usunąć niejednoznaczność „half-up po ucięciu”.

**Rekomendacja:** nie blokuję geometrii ani operatorów v0.4. Nie rekomenduję jednak bindu v1.0 przed poprawieniem A.3 i A.4. K6 pozostaje nienaruszone.
