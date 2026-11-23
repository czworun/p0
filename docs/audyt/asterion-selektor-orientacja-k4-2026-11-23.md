# P₀ — Selekcja wierzchołka i orientacja K₄ bez uprzywilejowania etykiet

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; selektor kolejnego wierzchołka, symetria \(S_4\), orientacja \(V_\rho\), relacja Axis–Defect–TAU–Wave.  
**Poza zakresem:** MVP-02, procedury laboratoryjne i redakcja pakietów replikacyjnych.

## 0. Źródła i konwencje

Korzenie odczytane z gałęzi **main** w repozytorium \`czworun/p0\`, commit:

\`e4ac4a6d64c4a69983d7378bc5e82d961bb49f5c\`

Odczytane dokumenty: P₀-Centroid v5.2 (adnotacja i lista zmian), P₀-Axis v0.3, P₀-Defect v0.8, P₀-TAU v1.7.2, P₀-Wave v0.6.1 i P₀-Net v0.6.1. Raport zapisano na gałęzi audytowej, nie na **main**.

Używam rozróżnienia:
- \(p_0=\frac14\mathbf1\in\mathbb R^4\) — centroid w pełnej przestrzeni;
- \(P_0=0\in V_\rho\) — ten sam stan po przejściu do przestrzeni relacyjnej;
- \(V_\rho=\{x\in\mathbb R^4:\sum_i x_i=0\}\);
- \(\rho:S_4\to GL(V_\rho)\) — standardowe działanie permutacji wierzchołków.

Na \(V_\rho\):
\[
\det\rho(\pi)=\operatorname{sgn}(\pi),\qquad \pi\in S_4.
\]
Jest to zasadniczy fakt dla całego audytu.

## 1. Twierdzenie no-go: z pełnej symetrii nie ma deterministycznego wyboru

Niech \(X\) będzie przestrzenią pełnych stanów modelu z działaniem \(S_4\). Niech \(F:X\to X\) będzie deterministycznym i \(S_4\)-ekwiwariantnym prawem aktualizacji:
\[
F(\pi x)=\pi F(x).
\]

**Twierdzenie 1.** Jeżeli stan początkowy \(x_0\) jest \(S_4\)-niezmienniczy, to każdy stan trajektorii \(x_t=F^t(x_0)\) pozostaje \(S_4\)-niezmienniczy.

**Dowód.** Indukcyjnie:
\[
\pi x_t=x_t
\quad\Longrightarrow\quad
\pi x_{t+1}
=\pi F(x_t)
=F(\pi x_t)
=F(x_t)
=x_{t+1}.
\]
Zatem własność zachodzi dla każdego \(t\). \(\square\)

Jeśli selektor \(s:X\to Y\) jest również ekwiwariantny, wynik \(s(x_0)\) musi być punktem stałym działania \(S_4\) w \(Y\). Dla \(Y\) równego zbiorowi pojedynczych wierzchołków albo pojedynczych krawędzi taki punkt stały nie istnieje. Nie istnieje też punkt stały w zbiorze dwóch orientacji przestrzeni \(V_\rho\), ponieważ każda permutacja nieparzysta zamienia orientacje.

Stąd:

**Wniosek 1.1 — ✅.** Z dokładnie symetrycznego \(P_0\) nie można deterministycznie i ekwiwariantnie wybrać jednego wierzchołka, jednej krawędzi ani jednej orientacji.

To twierdzenie nie mówi, że orientacja jest niemożliwa. Mówi, że nie powstanie z pełnej symetrii, jeśli całe prawo i cały stan początkowy tę symetrię zachowują.

W szczególności wybór losowy jednego z \(M_i\) nie zmieni samego \(P_0\): każdy \(M_i\) i \(T\) zachowują \(p_0\), a odpowiadające im operatory na \(V_\rho\) zachowują zero. Losowanie może jednak zapisać się w dodatkowej historii wyborów. Wtedy symetrię łamie pojedyncza realizacja historii, a nie rozkład prawdopodobieństwa.

## 2. Stabilizator: ile symetrii trzeba złamać?

Niech \(H=\operatorname{Stab}(x)\leq S_4\). Dla każdego ekwiwariantnego selektora \(s\):
\[
H\leq\operatorname{Stab}(s(x)).
\]
To jest ogólne kryterium dopuszczalności wyboru.

| Obiekt, który ma zostać wybrany | Stabilizator wyniku | Warunek na \(H\) |
|---|---:|---:|
| jeden wierzchołek | \(S_3\) | \(H\leq S_3\) |
| jedna orientacja \(V_\rho\) | \(A_4\) | \(H\leq A_4\) |
| wierzchołek i orientacja | \(S_3\cap A_4\cong C_3\) | \(H\leq C_3\) |
| pełny uporządkowany harmonogram | \(\{e\}\) | \(H=\{e\}\) |

Wynik ma dwie ważne konsekwencje.

**Po pierwsze: orientacja nie wystarcza do wskazania kolejnego wierzchołka.** Grupa \(A_4\) zachowuje orientację, ale działa przechodnio na czterech wierzchołkach. Stan o stabilizatorze dokładnie \(A_4\) może wybrać chirialność, lecz nadal nie wyróżnia jednego wierzchołka.

**Po drugie: samo wskazanie wierzchołka nie wystarcza do orientacji.** Stabilizator wyróżnionego wierzchołka to \(S_3\), który zawiera permutacje nieparzyste. Pozostaje więc symetria odwracająca orientację.

Do równoczesnego wskazania wierzchołka i orientacji potrzeba zejścia co najmniej do \(C_3\). Pełny uporządkowany harmonogram ma stabilizator trywialny.

Minimalny stan orientacyjny można zatem opisać jako dwie możliwe chirialności, zamieniane przez \(S_4/A_4\cong C_2\). To jest jeden bit typu znakowego. Nie jest on jednak selektorem wierzchołka.

## 3. Co Axis rzeczywiście wyprowadza z K₄

P₀-Axis v0.3 ma mocny i poprawny rdzeń kombinatoryczno-geometryczny:

1. K₄ ma dokładnie trzy pary krawędzi przeciwległych:
   \[
   (01,23),\quad(02,13),\quad(03,12).
   \]
2. Środki krawędzi przeciwległych są wektorami przeciwnymi.
3. Różnice środków wyznaczają trzy wzajemnie ortogonalne kierunki w \(V_\rho\).
4. Na \(V_\rho\), \(G_4=4I\), więc ortogonalność grafowa i euklidesowa różnią się tylko skalą.

To wystarcza do wyprowadzenia **nieuporządkowanego zbioru trzech nieukierunkowanych prostych osiowych**. Nie wymaga uprzedniego osadzenia w \(\mathbb R^3\).

Trzeba jednak rozdzielić trzy rzeczy:

- **trzy proste osiowe jako zbiór** — wynik kanoniczny struktury K₄;
- **nazwy \(X,Y,Z\)** — kolejność trzech par przeciwległych, czyli wybór reprezentacyjny;
- **zwroty \(u_X,u_Y,u_Z\)** — wybór kolejności krawędzi wewnątrz każdej pary przeciwległej.

Grupa \(S_4\) zachowuje cały układ trzech prostych, ale permutuje te proste i może odwracać zwroty wektorów osiowych. W zapisie osiowym działa jako grupa macierzy znakowo-permutacyjnych. Dlatego \(G_4^{(B)}=4I_3\) jest prawdziwą reprezentacją metryki w wybranej bazie, ale sama macierz diagonalna nie nadaje osiom kanonicznych nazw ani orientacji.

**Wniosek 3.1 — ✅.** Axis wyprowadza geometrię ortogonalnej trójki osi jako strukturę nieuporządkowaną i nieukierunkowaną. Nie wyprowadza jeszcze orientowanej ramy XYZ.

To precyzuje, co znaczy w tym miejscu „relacja → geometria”. Przejście jest matematycznie realne na poziomie metryki i prostych osiowych. Przejście do oznakowanej i zorientowanej ramy jest kolejnym krokiem, wymagającym dodatkowego stanu.

## 4. TAU i Wave: nośnik orientacji nie jest jej generatorem

### 4.1. TAU

TAU §1.1 jawnie kwalifikuje aksjomat sekwencyjności jako fenomenologiczny i motywacyjny, a nie jako prawo generujące harmonogram. To ważne ograniczenie.

Dany harmonogram pierwszych odwiedzin
\[
\sigma=(i_0,i_1,i_2,i_3)
\]
niesie orientację przez
\[
\Omega_\sigma=
(v_{i_1}-v_{i_0})\wedge
(v_{i_2}-v_{i_0})\wedge
(v_{i_3}-v_{i_0})
\in\Lambda^3V_\rho.
\]
Wektor jest niezerowy, a przy permutacji etykiet:
\[
\Omega_{\pi\sigma}
=\operatorname{sgn}(\pi)\Omega_\sigma.
\]
Dwanaście harmonogramów parzystych daje jedną orientację, a dwanaście nieparzystych — przeciwną.

To jest **dowód, że historia może nieść orientację**, nie dowód, że TAU wybiera historię. W TAU §7.7 P23 („naturalna orientacja DAG”) pozostaje 🔍, a kandydaci — indeks, znak defektu i para przeciwległa — nie stanowią domkniętego selektora.

### 4.2. Wave

Wave definiuje słowo jako element alfabetu operatorowego; operator jest interpretacją już podanego słowa. Automat projektorowy, który miałby generować przejścia, pozostaje hipotezą 💡, a klasyfikacja orbit projektorów względem \(S_4\) jest otwarta.

Na \(V_\rho\):
\[
\det\bar M_i=\frac14,\qquad \det\bar T=-1.
\]
Dla słowa zawierającego \(n_M\) operatorów typu \(M_i\) i \(n_T\) wystąpień \(T\):
\[
\det\bar\rho(w)=4^{-n_M}(-1)^{n_T}.
\]
Znak ten opisuje działanie słowa na orientacji już określonej. Nie wskazuje, którą orientację przyjąć na początku.

**Wniosek 4.1 — ✅.** TAU dostarcza formalnego nośnika orientacji w historii, a Wave opisuje transformację tej struktury przez słowa operatorowe. Żaden z tych dwóch korzeni w obecnym stanie nie dostarcza autonomicznego selektora harmonogramu z \(P_0\).

## 5. Konstrukcja selektora dla stanu niesymetrycznego

No-go dotyczy pełnej symetrii. Nie wyklucza selektora ekwiwariantnego na stanie, który już zawiera relacyjne zróżnicowanie.

Niech \(x\in V_\rho\). Jeśli maksimum współrzędnych jest jednoznaczne, można zdefiniować:
\[
s(x)=\operatorname*{arg\,max}_{i\in V}x_i.
\]
Dla każdej permutacji:
\[
s(\pi x)=\pi s(x).
\]
Jest to deterministyczny selektor bez uprzywilejowania etykiety. Wybiera wyróżniony element stanu relacyjnego, a nie z góry wskazane „0” czy „1”.

Jeśli wszystkie cztery wartości \(x_i\) są różne, stan wyznacza pełny porządek wierzchołków. Jego stabilizator jest trywialny. Można więc zdefiniować harmonogram przez kolejne wybieranie największego jeszcze nieodwiedzonego \(x_i\), z pamięcią zbioru odwiedzonych wierzchołków. Pod działaniem \(S_4\) cały harmonogram permutuje się ekwiwariantnie.

### 5.1. Pseudoskalar orientacji z jednego stanu

Niech
\[
P_\rho=I-\frac14J,\qquad
x^{[k]}=P_\rho(x^{\circ k}),
\]
gdzie potęgowanie jest współrzędne po współrzędnej. Zdefiniujmy:
\[
\boxed{
\Omega(x)=x\wedge x^{[2]}\wedge x^{[3]}
\in\Lambda^3V_\rho.
}
\]

To jest naturalny, \(S_4\)-ekwiwariantny kandydat na orientację wyprowadzoną ze stanu:

\[
\Omega(\pi x)
=\Lambda^3\rho(\pi)\Omega(x)
=\operatorname{sgn}(\pi)\Omega(x).
\]

Ponadto:
\[
\Omega(x)\neq0
\quad\Longleftrightarrow\quad
x_0,x_1,x_2,x_3\text{ są parami różne}.
\]

Uzasadnienie: niezerowość klina jest równoważna niezerowości wyznacznika Vandermonde’a dla kolumn \(1,x,x^{\circ2},x^{\circ3}\):
\[
\det
\begin{pmatrix}
1&1&1&1\\
x_0&x_1&x_2&x_3\\
x_0^2&x_1^2&x_2^2&x_3^2\\
x_0^3&x_1^3&x_2^3&x_3^3
\end{pmatrix}
=
\prod_{i<j}(x_j-x_i).
\]
Jest to element linii orientacji, a nie etykieta „prawo/lewo” niezależna od tej linii. Transformuje dokładnie jak reprezentacja znakowa.

Ta konstrukcja pokazuje, że **relacyjny stan z czterema różnymi wartościami zawiera wystarczającą informację do wyznaczenia orientacji i pełnego porządku**, bez wyróżniania indeksu.

### 5.2. Ograniczenie tej konstrukcji

Nie jest to mechanizm wyłaniania orientacji z \(P_0\). Dla \(x=0\):
\[
\Omega(0)=0,
\]
a \(\operatorname{arg\,max}\) jest niezdefiniowany z powodu remisu.

Co więcej, orientacja odczytywana na nowo z aktualnego wektora \(x_t\) nie musi być niezmiennikiem dynamiki Centroidu. Dla wycentrowanego operatora \(\bar M_i=P_\rho M_i|_{V_\rho}\):
\[
(\bar M_i x)_i=\frac{x_i}{4},\qquad
(\bar M_i x)_j=x_j+\frac{x_i}{4}\quad(j\ne i).
\]
W szczególności dla \(x=(-3,-1,1,3)\) i \(i=3\):
\[
\bar M_3x=\left(-\frac94,-\frac14,\frac74,\frac34\right).
\]
Współrzędne pozostają różne, ale znak wyznacznika Vandermonde’a się odwraca. Zatem dodatni wyznacznik \(\det\bar M_i=1/4\) (zachowanie orientacji przestrzeni liniowej) nie oznacza zachowania znaku orientacji odczytywanej z porządku wartości współrzędnych.

Jeżeli orientacja ma przetrwać jako własność historii, należy ją zapisać w pamięci harmonogramu lub w osobnej zmiennej orientacyjnej. Nie można utożsamiać jej z chwilowym znakiem \(\Omega(x_t)\).

## 6. Losowość, pamięć i spontaniczne złamanie symetrii

Możliwe są trzy różne mechanizmy, których nie należy mieszać:

1. **Deterministyczny start z \(P_0\).** Niemożliwy wybór. Każda trajektoria dokładnie zachowująca \(S_4\) pozostaje symetryczna.
2. **Losowy start lub losowy wybór z pamięcią.** Każda realizacja może wybrać jeden harmonogram i orientację; dla symetrycznego rozkładu prawdopodobieństwa obie orientacje mają jednakowe prawdopodobieństwo. Zespół realizacji zachowuje symetrię.
3. **Dodatkowy stan wewnętrzny.** Może być ziarnem orientacji, ale jeżeli jest początkowo \(S_4\)-niezmienniczy i ewoluuje deterministycznie ekwiwariantnie, nie wygeneruje sam z siebie niezerowego ziarna. Niezerowy bit orientacyjny jest już złamaniem \(S_4\) do \(A_4\).

Dodatkowo Defect §12C.1 klasyfikuje \(A_4\) jako Type II: przy ograniczeniu do \(A_4\) reprezentacje \(V_\rho\) i \(V_{\rm cyc}\) stają się równoważne, ale samo to złamanie nie otwiera nowego kanału kwadratowego \(T_b\). Dla K₄ Type I wskazane są m.in. \(D_4\) i \(S_3\).

To rozdziela dwa pytania:
- orientacja może umożliwić skręcony znakowo most \(V_\rho\to V_{\rm cyc}\);
- orientacja sama nie gwarantuje otwarcia nieliniowego kanału propagacji.

Nie wolno traktować ich jako tego samego przejścia.

## 7. Werdykt i dalszy kierunek matematyczny

| Teza | Status | Werdykt |
|---|---|---|
| Trzy proste osiowe wynikają z par przeciwległych K₄ | ✅ | Prawda, jako zbiór nieukierunkowany i nieuporządkowany |
| XYZ ma kanoniczną kolejność i zwroty | ❌ | Nie wynika z samej symetrii K₄ |
| Deterministyczny selektor z dokładnego \(P_0\) może wybrać wierzchołek | ❌ | Wyklucza go no-go dla \(S_4\) |
| Historia pełnych pierwszych odwiedzin niesie orientację | ✅ | Orientacja jest klasą parzystości harmonogramu |
| TAU obecnie generuje harmonogram | ❌ / brak podstaw | Aksjomat sekwencyjności jest fenomenologiczny; P23 pozostaje otwarte |
| Wave obecnie generuje następny operator | 💡 | Automat projektorowy pozostaje hipotezą |
| Stan \(x\in V_\rho\) z czterema różnymi wartościami może wyznaczyć orientację i porządek | ✅ | Konstrukcja przez \(\Omega(x)\) i ranking |
| Orientacja odczytana z aktualnego \(x_t\) jest zachowana przez \(M_i\) | ❌ | Jawny kontrprzykład dla \(\bar M_3\) |
| Złamanie do \(A_4\) otwiera kanał \(T_b\) | ❌ | Defect klasyfikuje \(A_4\) jako Type II |

### Najważniejsza konkluzja

P₀ ma już geometrię trzech osi, ale nie ma jeszcze matematycznego mechanizmu, który z dokładnie symetrycznego \(P_0\) sam wybiera pierwszy wierzchołek. Sekwencyjność może nieść orientację, lecz nie wyjaśnia, skąd bierze się pierwsza sekwencja.

Najbardziej obiecujący kierunek nie polega na szukaniu „magicznego” selektora działającego w \(P_0\). Polega na wskazaniu, jaki **minimalny stan relacyjny** może istnieć przed pierwszym wyborem. Kandydatem jest niezerowy \(x\in V_\rho\) z rozróżnialnymi wartościami współrzędnych, ewentualnie pamięć zachowująca jego porządek. Wtedy reguła wyboru jest ekwiwariantna i nie uprzywilejowuje etykiet.

**Następny problem matematyczny:** ustalić, czy taki stan \(x\) lub jego odpowiednik w \(V_{\rm cyc}\) można uzyskać z P₀ przez dopuszczalną, wewnętrzną operację P₀, która nie jest zewnętrznym ziarnem, szumem ani z góry podanym harmonogramem. Obecne korzenie tego jeszcze nie dowodzą.

---
