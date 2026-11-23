# N-R2: cztery profile jako minimalny nośnik wymiaru 3?

**Data:** 2026-11-23  
**Zakres:** matematyczny audyt korzeni P₀; relacja pierwotna, rekonstrukcja profili, wymiar afiniczny i minimalność liczby cztery.  
**Źródło korzeni:** `main`, commit `e4ac4a6d64c4a69983d7378bc5e82d961bb49f5c`.  
**Dokument wiodący:** `docs/korzenie/P0-Relacje-v0_3.md`.  
**Poza zakresem:** MVP-02 i procedury laboratoryjne.

## 0. Pytanie i werdykt wstępny

Sugestia do sprawdzenia: czy cztery jest minimalną liczbą relacyjnych profili, z których może wyłonić się przestrzeń o wymiarze większym niż płaszczyzna?

**Werdykt:** w geometrii afinicznej — tak, dokładnie cztery punkty są minimalną liczbą punktów, których otoczka afiniczna może mieć wymiar 3. Jest to twierdzenie, nie analogia:
[
\dim\operatorname{aff}\{p_1,\ldots,p_m\}\le m-1.
]
Aby uzyskać wymiar 3, potrzeba (m\ge4). Dla (m=4) warunkiem koniecznym i wystarczającym jest afiniczna niezależność czterech profili.

To **nie dowodzi jeszcze**, że P₀ wyłania cztery profile z pierwotnej relacji. Dowodzi warunkowej minimalności nośnika wymiaru 3, jeśli nośnikiem mają być punkty/profile i jeśli wymiar emergentny jest wymiarem afinicznym ich konfiguracji.

## 1. Twierdzenie afiniczne

Dla (m) punktów (p_1,\ldots,p_m) przestrzeń kierunkowa ich otoczki afinicznej jest rozpięta przez:
[
p_2-p_1,\ldots,p_m-p_1.
]
Jest to (m-1) wektorów, więc:
[
\boxed{\dim\operatorname{aff}(p_1,\ldots,p_m)\le m-1.}
]
Dla czterech punktów:
[
\dim\operatorname{aff}(p_1,p_2,p_3,p_4)=3
\iff
\det[p_2-p_1\;p_3-p_1\;p_4-p_1]\ne0.
]
Wtedy cztery punkty są wierzchołkami niedegenerowanego tetraedru. Jeśli wyznacznik jest zerowy, leżą w jednej płaszczyźnie lub niższym wymiarze.

Wniosek jest ścisły, ale ma ograniczony zakres: cztery są minimalne dla 3-wymiarowej otoczki afinicznej zbioru punktów. Nie są minimalne dla każdej możliwej definicji przestrzeni trójwymiarowej ani dla każdej algebry relacji.

## 2. Wersja czysto relacyjna: odległości bez współrzędnych

Można usunąć z opisu współrzędne i pozostawić wyłącznie sześć odległości między czterema profilami:
[
d_{ij}^2,\qquad 1\le i<j\le4.
]
Niech (D^{(2)}) będzie macierzą kwadratów odległości, a
[
J=I-\frac14\mathbf1\mathbf1^T.
]
Wycentrowana macierz Grama jest rekonstruowana wyłącznie z odległości:
[
B=-\frac12 JD^{(2)}J.
]
Dla euklidesowej realizacji:
[
\operatorname{rank}B=\dim\operatorname{aff}\{p_1,p_2,p_3,p_4\}.
]
Zatem:
- ranga 0: wszystkie profile zlewają się;
- ranga 1: konfiguracja liniowa;
- ranga 2: konfiguracja płaska;
- ranga 3: konfiguracja tetraedryczna.

To jest ważny krok: **wymiar można odzyskać z nieoznaczonych relacji odległościowych, bez wcześniejszego osadzania w \(\mathbb R^3\)**. Wymagane jest jednak, aby cztery profile i ich sześć relacji były już określone. Ten formalizm nie wyprowadza jeszcze samych profili.

Równoważny test czteropunktowy daje wyznacznik Cayleya–Mengera:
[
\det\begin{pmatrix}
0&1&1&1&1\\
1&0&d_{12}^2&d_{13}^2&d_{14}^2\\
1&d_{12}^2&0&d_{23}^2&d_{24}^2\\
1&d_{13}^2&d_{23}^2&0&d_{34}^2\\
1&d_{14}^2&d_{24}^2&d_{34}^2&0
\end{pmatrix}
=288V_3^2.
]
Dodatni wynik oznacza niezerową objętość tetraedru; zero — degenerację płaską (przy założeniu, że odległości dopuszczają euklidesową realizację). Sam warunek dodatniości nie zastępuje warunków metrycznych i dodatniej półokreśloności Grama.

## 3. Co w tym sensie znaczy „z płaszczyzny relacyjnej”?

Trzeba rozdzielić trzy interpretacje:

1. **Płaszczyzna jako już dana przestrzeń geometryczna.** Jeśli wszystkie profile są punktami tej samej płaszczyzny, żaden ich skończony podzbiór nie utworzy tetraedru o dodatniej objętości. Czwarty punkt wciąż leży w płaszczyźnie. Przestrzeń 3D nie wyłania się z samego dodania punktu.
2. **Płaszczyzna jako poziom relacji/różnic, a nie zewnętrzne osadzenie.** Cztery profile mogą mieć macierz Grama rangi 3; wówczas relacje odległościowe wymuszają, że żadna realizacja nie mieści ich w 2D. Wymiar 3 jest odzyskany wewnętrznie z danych relacyjnych.
3. **Płaszczyzna jako przestrzeń stanów o dwóch stopniach swobody.** Przejście do rangi 3 wymaga pojawienia się trzeciego niezależnego kierunku. Cztery profile są minimalną liczbą, by ich różnice mogły ten kierunek rozpiąć.

Najbardziej obiecująca dla P₀ jest interpretacja 2, bo nie zakłada z góry przestrzeni euklidesowej 3D. Ale nadal trzeba wyjaśnić, skąd pochodzą cztery profile.

## 4. Pułapka: (K_4) nie jest automatycznie tetraedrem wypełnionym

Pełny graf (K_4) ma cztery wierzchołki i sześć krawędzi. Jako abstrakcyjny kompleks 1-wymiarowy jego realizacja geometryczna ma wymiar topologiczny 1. Tetraedr jako bryła to 3-simpleks: oprócz wierzchołków i krawędzi ma cztery ściany trójkątne i jedną komórkę 3-wymiarową.

Zatem:
[
K_4\;\text{(graf)}\ne\text{3-simpleks (bryła)}.
]
Aby otrzymać tetraedr jako obiekt geometryczny, potrzebne są:
- cztery afinicznie niezależne profile;
- metryka/forma, która pozwala stwierdzić ich niezależność;
- reguła interpretacji wnętrza i ścian, jeśli P₀ chce mówić o wypełnionej objętości, a nie tylko o konfiguracji czterech punktów.

To rozróżnienie zapobiega przeskokowi od sześciu relacji krawędziowych do twierdzenia o emergencji przestrzeni 3D.

## 5. Czy można uzyskać cztery profile bez węzłów?

P₀-Relacje v0.3 §1 deklaruje:
[
\text{relacja}\to\text{rozróżnienie}\to\text{stan węzłów}.
]
Jednak §7 zapisuje:
[
\mathcal R_t=(V,E_t,X_t),
]
a §8 definiuje (E_t\subseteq V\times V). To są już relacje z końcami w zbiorze (V). N-R2 dokumentu sam trafnie zauważa, że (V) pozostaje dane, nie wyprowadzone.

Propozycja (V_t=\mathcal V(\mathcal R_t)) nie jest jeszcze definicją, dopóki nie określimy:
- czym jest surowy obiekt (\mathcal R) bez elementów/nośnika;
- jak z niego wyznaczyć profile;
- kiedy dwa profile są tym samym profilem;
- jaka relacja równoważności tworzy klasy profili;
- jak z samych danych relacyjnych zdefiniować odległość, iloczyn skalarny albo rangę;
- dlaczego liczba stabilnych klas wynosi dokładnie cztery.

„Profil incydencji” względem zbioru relacji nie rozwiązuje problemu, jeśli relacje mają już źródła i cele. Wtedy profile tylko przepisują wcześniej założone węzły.

## 6. Połączenie z wcześniejszym testem (V_4)

Dwie drogi do liczby cztery są logicznie różne:

- **Algebraiczna:** normalna podgrupa (V_4\triangleleft S_n) selekcjonuje (n=4), ale wymaga uzasadnienia, dlaczego taka podgrupa ma być warunkiem pierwotnym.
- **Geometryczna:** cztery afinicznie niezależne profile są minimalnym nośnikiem wymiaru 3, ale wymaga uzasadnienia, dlaczego pierwotna relacja wytwarza takie profile i dlaczego ich ranga wynosi 3.

Nie należy ich utożsamiać. Możliwy most dopiero do wykazania: automorfizmy czterech profili mogą działać jako (S_4), a ich parowania jako (V_4). To jest konsekwencja tetraedrycznej konfiguracji, nie dowód, że geometria i algebra mają wspólne źródło.

## 7. Minimalny program formalny dla N-R2

Kolejność, która nie przemyca węzłów:

**A. Pierwotne dane.** Zdefiniować obiekt relacyjny jako strukturę algebraiczną/operacyjną bez jawnych zbiorów źródeł i celów. Każda definicja przez pary ((a,b)), morfizmy ze źródłem i celem albo macierze (D_{ij}) jest już nośnikowa i nie może być nazywana beznośnikową.

**B. Profile.** Zdefiniować profil jako wewnętrzny niezmiennik działania/kompozycji pierwotnych relacji. Równość profili ma wynikać z równoważności algebraicznej, nie z etykiet.

**C. Liczba.** Dowieść, że istnieją dokładnie cztery klasy profili pierwotnych (albo wykazać, że liczba nie jest określona).

**D. Geometria.** Zdefiniować relację podobieństwa/odległość między profilami i pokazać, że wycentrowana macierz Grama ma rangę 3.

**E. Symetria.** Obliczyć grupę automorfizmów danych profili i sprawdzić, czy jest (S_4), czy mniejsza. Sprawdzić, czy (V_4) pojawia się jako skutek, a nie założenie.

**F. Falsyfikacja.** Znaleźć kontrprzykład: strukturę spełniającą wszystkie pierwotne aksjomaty, ale mającą 2, 3 lub więcej niż 4 profile, albo rangę co najwyżej 2. Jeden taki model obala tezę o wymuszaniu czterech przez obecne aksjomaty.

## 8. Werdykt

| Teza | Status |
|---|---|
| Minimalnie 4 punkty/profile mogą rozpiąć wymiar afiniczny 3 | ✅ |
| Cztery profile wystarczają, jeśli są afinicznie niezależne | ✅ |
| Wymiar 3 można odzyskać z samych sześciu odległości | ✅, przy warunkach euklidesowej realizowalności |
| Samo dodanie czwartego punktu do płaszczyzny tworzy 3D | ❌ |
| Abstrakcyjny (K_4) sam w sobie jest bryłą 3D | ❌ |
| P₀-Relacje v0.3 wyprowadza cztery profile bez nośnika | ❌ / brak definicji |
| P₀ wyprowadza rangę 3 z pierwotnej relacji | 💡 otwarte |

**Najmocniejsza wersja sugestii:** cztery mogą być minimalną liczbą stabilnych, wzajemnie rozróżnialnych profili, których relacje pozwalają na niepłaską realizację, czyli na emergencję trzeciego niezależnego kierunku. To jest precyzyjna hipoteza matematyczna.

**Ale liczba cztery nie wynika z samego faktu „relacyjności”.** Wynika z relacyjności plus kryterium rangi 3 i niezależności afinicznej. N-R2 musi wyprowadzić oba te warunki, a nie wpisać je do definicji profilu.

## 9. Następny krok

Następnie należy skonstruować najmniejszy nośnikowy model relacyjny, w którym profile są klasami równoważności operacji, a nie zadanymi węzłami, i sprawdzić, czy jego macierz Grama ma wymuszoną rangę 3. Równolegle trzeba odszukać i porównać źródłowy dokument P₀-Samoodniesienie-Kompensacja-Emergencja v0.1, ponieważ P₀-Relacje §0.1 stwierdza, że oba formalizmy są obecnie niedookreślone i mogą być tym samym placeholderem.
