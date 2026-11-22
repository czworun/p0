# K₄: środki krawędzi i sektor cykliczny — audyt algebraiczny

Data: 2026-11-22  
Zakres: rdzeń matematyczny P₀; bez ingerencji w MVP-02  
Źródła korzeni: gałąź \`main\` — \`docs/korzenie/P0-Axis_v0_3.md\`, \`docs/korzenie/P0-Defect-v0_8.md\`  
Status raportu: nowy rachunek łączący Axis i Defect; nie zmienia statusów źródłowych twierdzeń.

## 1. Wynik w skrócie

Środki sześciu krawędzi relacyjnego K₄ tworzą regularny ośmiościan wycentrowany w \(P_0=0\). Trzy pary przeciwległych środków są antypodalne i wyznaczają trzy wzajemnie prostopadłe proste. To dokładny wynik geometrii \(V_\rho\) z metryką indukowaną przez \(G_4\).

Nie istnieje zwykły, niezerowy \(S_4\)-splotnik \(V_\rho\to V_{\rm cyc}\). Nie wolno więc utożsamiać obu trójwymiarowych przestrzeni na podstawie wymiaru ani wspólnej kombinatoryki par przeciwległych krawędzi.

Istnieje jednak ścisły most po wyborze orientacji: operator częściowej izometrii \(J:U\to C^1(K_4)\), gdzie \(U\) jest przestrzenią nieukierunkowanych krawędzi. Operator spełnia
$$
J^*J=P_{\rm mid},\qquad JJ^*=P_{\rm cyc}.
$$
Jest \(A_4\)-ekwiwariantny i \(S_4\)-ekwiwariantny po skręceniu znakiem. Zatem środki krawędzi i sektor cykliczny są połączone dokładnie, ale nie przez kanoniczne utożsamienie pod pełną grupą \(S_4\).

## 2. Geometria środków — rachunek

Niech
$$
\bar e=\frac14(1,1,1,1),\qquad
W=V_\rho=\{x\in\mathbb R^4:\langle x,\mathbf1\rangle=0\},
$$
a \(v_i=e_i-\bar e\). Dla nieukierunkowanej krawędzi \(\{i,j\}\) definiujemy jej środek względem \(P_0=0\):
$$
q_{ij}=\frac12(v_i+v_j)=\frac12(e_i+e_j)-\bar e.
$$

Wtedy
$$
q_{01}=\frac14(1,1,-1,-1),\quad
q_{02}=\frac14(1,-1,1,-1),\quad
q_{03}=\frac14(1,-1,-1,1),
$$
oraz
$$
q_{23}=-q_{01},\quad q_{13}=-q_{02},\quad q_{12}=-q_{03}.
$$

Dla każdej krawędzi \(\|q_{ij}\|^2=1/4\). Środki dwóch różnych krawędzi ze wspólnym wierzchołkiem są ortogonalne. Środki krawędzi przeciwległych są przeciwne, a ich iloczyn skalarny wynosi \(-1/4\).

Sześć punktów to dokładnie
$$
\{\pm q_{01},\pm q_{02},\pm q_{03}\},
$$
czyli wierzchołki regularnego ośmiościanu. Wektory osiowe z Axis v0.3 spełniają
$$
u_X=2q_{01},\qquad u_Y=2q_{02},\qquad u_Z=2q_{03}.
$$
Środki krawędzi są więc dokładnie połowami trzech wektorów osiowych, nie tylko obiektami, z których osie można dopiero skonstruować.

Ponieważ \(G_4|_W=4I\), mamy \(\|q_{ij}\|_{G_4}=1\). To zmiana skali metrycznej, nie nowa geometria.

## 3. Przestrzeń krawędzi nieukierunkowanych

Niech \(U=\mathbb R^6\) ma bazę ortonormalną \(f_{01},f_{02},f_{03},f_{12},f_{13},f_{23}\), z naturalnym działaniem \(S_4\) przez permutację nieukierunkowanych krawędzi.

Definiujemy
$$
B:U\to W,\qquad Bf_{ij}=q_{ij}.
$$
W kolejności krawędzi \((01,02,03,12,13,23)\), macierz Grama kolumn \(q_{ij}\) wynosi
$$
B^*B=\frac14
\begin{pmatrix}
1&0&0&0&0&-1\\
0&1&0&0&-1&0\\
0&0&1&-1&0&0\\
0&0&-1&1&0&0\\
0&-1&0&0&1&0\\
-1&0&0&0&0&1
\end{pmatrix}.
$$
Dokładnie:
$$
BB^*=\frac12 I_W,\qquad
P_{\rm mid}:=2B^*B,\qquad
P_{\rm mid}^2=P_{\rm mid},\qquad
\operatorname{rank}B=3.
$$

Obraz \(P_{\rm mid}\) jest rozpięty przez trzy różnice przeciwległych krawędzi:
$$
f_{01}-f_{23},\quad f_{02}-f_{13},\quad f_{03}-f_{12}.
$$
Jądro \(B\) jest rozpięte przez trzy sumy:
$$
f_{01}+f_{23},\quad f_{02}+f_{13},\quad f_{03}+f_{12}.
$$
Jako reprezentacja \(S_4\):
$$
U\cong \mathbf1\oplus V_2\oplus V_{\rm std}.
$$
Mapa \(B\) zachowuje wyłącznie sektor \(V_{\rm std}\) i zeruje \(\mathbf1\oplus V_2\). To jawna postać projekcji środków krawędzi.

## 4. Dlaczego bezpośrednia identyfikacja z \(P_{\rm cyc}\) jest błędna

Dla orientacji \(i<j\), niech \(d:W\to C^1(K_4)\) będzie operatorem różnic \((dx)_{ij}=x_i-x_j\). Wtedy
$$
d^*d=G_4|_W=4I_W,\qquad
P_{\rm cyc}=I-\frac14dd^*.
$$
W bazie krawędzi \((01,02,03,12,13,23)\):
$$
P_{\rm cyc}=
\begin{pmatrix}
\frac12&-\frac14&-\frac14&\frac14&\frac14&0\\
-\frac14&\frac12&-\frac14&-\frac14&0&\frac14\\
-\frac14&-\frac14&\frac12&0&-\frac14&-\frac14\\
\frac14&-\frac14&0&\frac12&-\frac14&\frac14\\
\frac14&0&-\frac14&-\frac14&\frac12&-\frac14\\
0&\frac14&-\frac14&\frac14&-\frac14&\frac12
\end{pmatrix}.
$$

Porównanie jest rozstrzygające:
- \(B^*B\) ma niezerowe wyrazy pozadiagonalne dla par przeciwległych i zera dla par sąsiednich;
- \(P_{\rm cyc}\) ma zera dla par przeciwległych i niezerowe wyrazy dla par sąsiednich.

Przykładowo:
$$
\langle q_{01},q_{23}\rangle=-\frac14,\qquad P_{\rm cyc}(01,23)=0,
$$
$$
\langle q_{01},q_{02}\rangle=0,\qquad P_{\rm cyc}(01,02)=-\frac14.
$$
Nie ma więc równości \(B^*B\propto P_{\rm cyc}\), nawet po prostym przeskalowaniu. To nie obala mostu; ustala, że most nie jest identycznością współrzędnych krawędzi.

## 5. Przeszkoda \(S_4\) i jej dokładne obejście

Defect v0.8 ustala:
$$
C^1(K_4)\cong V_{\rm std}\oplus(V_{\rm std}\otimes\mathrm{sign}),
\qquad V_{\rm cyc}\cong V_{\rm std}\otimes\mathrm{sign}.
$$
Tymczasem \(W=V_\rho\cong V_{\rm std}\). Są to nieizomorficzne nierozkładalne reprezentacje \(S_4\). Stąd
$$
\operatorname{Hom}_{S_4}(W,V_{\rm cyc})=0,\qquad
\operatorname{Hom}_{S_4}(U,V_{\rm cyc})=0.
$$
To formalny powód, dla którego bezwarunkowy most \(V_\rho\to V_{\rm cyc}\) nie istnieje. Sam fakt, że oba sektory mają wymiar 3, niczego tu nie rozstrzyga.

Po ograniczeniu do \(A_4\subset S_4\), sytuacja się zmienia, ponieważ
$$
\mathrm{sign}|_{A_4}=1.
$$
Reprezentacje \(W|_{A_4}\) oraz \(V_{\rm cyc}|_{A_4}\) są równoważne. Wybór orientacji na \(W\) definiuje operator Hodge’a
$$
*:W\to\Lambda^2W,
$$
który jest \(A_4\)-ekwiwariantny. Dla nieparzystych permutacji zmienia znak — dokładnie ten znak, którego brakuje przy próbie splotu pod całym \(S_4\).

Niech \(\Phi:\Lambda^2W\to V_{\rm cyc}\subset C^1(K_4)\) będzie izometryczną wersją identyfikacji \(V_{\rm cyc}\cong\Lambda^2W\) z Defect. Definiujemy
$$
\boxed{J=\sqrt2\,\Phi\circ *\circ B:U\to C^1(K_4).}
$$
Ponieważ \(BB^*=\frac12 I_W\), otrzymujemy dokładnie
$$
\boxed{J^*J=2B^*B=P_{\rm mid},\qquad
JJ^*=P_{\rm cyc}.}
$$
Zatem \(J\) jest częściową izometrią: przenosi sektor środków krawędzi \(\operatorname{im}P_{\rm mid}\cong V_{\rm std}\) na sektor cykliczny \(V_{\rm cyc}\), a pozostały sektor \(\ker B=\mathbf1\oplus V_2\) zeruje.

Działanie symetrii spełnia
$$
\rho_{\rm cyc}(g)J=\operatorname{sgn}(g)\,J\sigma_U(g),
\qquad g\in S_4.
$$
Dla \(g\in A_4\) znak jest równy \(+1\), więc \(J\) jest zwykłym splotnikiem \(A_4\). Dla całego \(S_4\) jest splotnikiem skręconym znakiem. Zmiana orientacji odwraca znak \(J\), lecz nie zmienia projektorów \(J^*J\) i \(JJ^*\).

## 6. Interpretacja dla Axis i Defect

1. Axis nie musi zakładać osi XYZ. Trzy osie są już zakodowane w rozkładzie środków krawędzi na trzy pary antypodalne.
2. Defect nie jest „tym samym” co geometria środków. Jego sektor \(V_{\rm cyc}\) ma skręcone działanie \(S_4\).
3. Most jest dokładny po wyborze orientacji. Symetrią, przy której staje się zwykłym splotnikiem, jest \(A_4\), grupa obrotów czworościanu.
4. Wspólny rdzeń to trójwymiarowy sektor standardowy przeniesiony przez orientacyjny Hodge-star do sektora cyklicznego. Wyjaśnia to wspólną kombinatorykę bez zacierania różnicy reprezentacji.

## 7. Statusy i granice wniosku

- ✅ **Dowiedzione algebraicznie:** sześć środków tworzy ośmiościan; \(BB^*=\frac12I_W\); \(P_{\rm mid}=2B^*B\) jest projektorem rangi 3; bezpośrednia macierz \(B^*B\) nie jest \(P_{\rm cyc}\); brak zwykłego \(S_4\)-splotnika wynika z nieizomorficzności reprezentacji.
- ✅ **Dowiedzione konstrukcyjnie:** po wyborze orientacji istnieje częściowa izometria \(J\) z \(J^*J=P_{\rm mid}\) oraz \(JJ^*=P_{\rm cyc}\); jest \(A_4\)-ekwiwariantna i skręcona znakiem pod \(S_4\).
- 🔍 **Do niezależnej replikacji w rygorze Z1:** odtworzenie konstrukcji \(J\) z jawnych macierzy operatora \(C\) z Axis/Defect, bez używania abstrakcyjnej identyfikacji \(V_{\rm cyc}\cong\Lambda^2W\). Rachunek projekcji jest dokładny, lecz konstrukcję trzeba jeszcze odtworzyć z jawnych macierzy źródłowych.
- 💡 **Hipoteza interpretacyjna:** orientacja może być matematycznym przełącznikiem między opisem osiowym i cyklicznym. Nie wynika stąd jeszcze materia, pole fizyczne ani ontologia relacja→materia.
- ❌ **Odrzucone:** utożsamianie \(V_\rho\) z \(V_{\rm cyc}\) jako reprezentacji \(S_4\), utożsamianie \(B^*B\) z \(P_{\rm cyc}\), oraz wniosek „ten sam wymiar 3, zatem ta sama przestrzeń”.

## 8. Następny test rdzenia

Następny test to przepisać \(J\) wyłącznie przez jawne macierze Axis/Defect — w szczególności przez operator złożony z mapy brzegów 2-komórek \(C\) i macierzy \(T\) — i sprawdzić znakowy warunek splotnika dla wszystkich 24 permutacji. To rozstrzygnie, czy abstrakcyjny most Hodge’a jest dokładnie tym samym obiektem co most macierzowy obecny w korzeniu Axis, czy też obie konstrukcje różnią się dodatkową konwencją.
