# K₄: środki krawędzi i sektor cykliczny — audyt algebraiczny

Data: 2026-11-22  
Zakres: rdzeń matematyczny P₀; bez ingerencji w MVP-02  
Źródła korzeni: `main` — `docs/korzenie/P0-Axis_v0_3.md`, `docs/korzenie/P0-Defect-v0_8.md`  
Status raportu: nowy rachunek łączący Axis i Defect; nie zmienia statusów źródłowych twierdzeń.

## 1. Wynik w skrócie

Środki sześciu krawędzi relacyjnego K₄ tworzą regularny ośmiościan wycentrowany w (P₀). Trzy pary przeciwległych środków są antipodalne i wyznaczają trzy wzajemnie prostopadłe proste. To jest dokładny wynik geometrii (V_ρ) z metryką indukowaną przez (G₄).

Nie istnieje zwykły, niezerowy (S₄)-splotnik (V_ρ\to V_{cyc}). Nie wolno więc utożsamiać obu trójwymiarowych przestrzeni na podstawie wymiaru ani wspólnej kombinatoryki par przeciwległych krawędzi.

Istnieje jednak ścisły most po wyborze orientacji: operator częściowej izometrii (J:U\to C^1(K₄)), gdzie (U) jest przestrzenią nieukierunkowanych krawędzi. Operator spełnia
[
J^*J=P_{\mathrm{mid}},\qquad JJ^*=P_{\mathrm{cyc}}.
]
Jest (A₄)-ekwiwariantny i (S₄)-ekwiwariantny po skręceniu znakiem. W ten sposób środki krawędzi i sektor cykliczny są połączone dokładnie, ale nie przez kanoniczne utożsamienie pod pełną grupą (S₄).

## 2. Geometria środków — rachunek

Niech
[
p_0=\frac14(1,1,1,1),\qquad
W=V_ρ=\{x\in\mathbb R^4:\langle x,\mathbf1\rangle=0\},
]
a (p_i=e_i-p_0). Dla nieukierunkowanej krawędzi ({i,j}):
[
q_{ij}=\frac12(p_i+p_j)=\frac12(e_i+e_j)-p_0.
]

Wtedy:
[
q_{01}=\frac14(1,1,-1,-1),\
q_{02}=\frac14(1,-1,1,-1),\
q_{03}=\frac14(1,-1,-1,1),
]
oraz
[
q_{23}=-q_{01},\quad q_{13}=-q_{02},\quad q_{12}=-q_{03}.
]

Dla każdej krawędzi:
[
\|q_{ij}\|^2=\frac14.
]
Jeżeli dwie różne krawędzie mają wspólny wierzchołek, ich środki są ortogonalne. Jeżeli są przeciwległe, ich środki są przeciwne i iloczyn skalarny wynosi (-1/4).

Zatem sześć punktów to dokładnie
[
\{\pm q_{01},\pm q_{02},\pm q_{03}\},
]
czyli wierzchołki regularnego ośmiościanu. Wektory osiowe z Axis v0.3 spełniają
[
u_X=2q_{01},\quad u_Y=2q_{02},\quad u_Z=2q_{03}.
]
W szczególności środki krawędzi nie tylko „wyznaczają” osie: są dokładnie połowami ich wektorów jednostkowych w zwykłej metryce euklidesowej (W).

Ponieważ (G₄|_W=4I), mamy także (|q_{ij}|_{G₄}=1). Jest to wyłącznie zmiana skali metrycznej, nie nowa geometria.

## 3. Przestrzeń krawędzi nieukierunkowanych

Niech (U=\mathbb R^6) ma bazę ortonormalną (f_{01},f_{02},f_{03},f_{12},f_{13},f_{23}), z naturalnym działaniem (S₄) przez permutację nieukierunkowanych krawędzi.

Definiujemy
[
B:U\to W,\qquad Bf_{ij}=q_{ij}.
]
W kolejności krawędzi ((01,02,03,12,13,23)), macierz Grama kolumn (q_{ij}) wynosi
[
B^*B=\frac14
\begin{pmatrix}
1&0&0&0&0&-1\\
0&1&0&0&-1&0\\
0&0&1&-1&0&0\\
0&0&-1&1&0&0\\
0&-1&0&0&1&0\\
-1&0&0&0&0&1
\end{pmatrix}.
]
Dokładnie:
[
BB^*=\frac12 I_W,\qquad
P_{\mathrm{mid}}:=2B^*B,\qquad
P_{\mathrm{mid}}^2=P_{\mathrm{mid}},\qquad
\operatorname{rank}B=3.
]

Obraz (P_{\mathrm{mid}}) jest rozpięty przez trzy różnice przeciwległych krawędzi:
[
f_{01}-f_{23},\quad f_{02}-f_{13},\quad f_{03}-f_{12}.
]
Jądro (B) jest rozpięte przez trzy sumy:
[
f_{01}+f_{23},\quad f_{02}+f_{13},\quad f_{03}+f_{12}.
]
W języku reprezentacji:
[
U\cong \mathbf1\oplus V_2\oplus V_{\rm std},
]
a (B) zachowuje wyłącznie sektor (V_{\rm std}) i zeruje (\mathbf1\oplus V_2). To jest konkretna, jawna postać projekcji środków krawędzi.

## 4. Dlaczego bezpośrednia identyfikacja z (P_{cyc}) jest błędna

Dla orientacji (i<j), niech (d:W\to C^1(K₄)) będzie operatorem różnic ( (dx)_{ij}=x_i-x_j). Wtedy
[
d^*d=G₄|_W=4I_W,
\qquad
P_{cyc}=I-\frac14dd^*.
]
W bazie ((01,02,03,12,13,23)):
[
P_{cyc}=
\begin{pmatrix}
\frac12&-\frac14&-\frac14&\frac14&\frac14&0\\
-\frac14&\frac12&-\frac14&-\frac14&0&\frac14\\
-\frac14&-\frac14&\frac12&0&-\frac14&-\frac14\\
\frac14&-\frac14&0&\frac12&-\frac14&\frac14\\
\frac14&0&-\frac14&-\frac14&\frac12&-\frac14\\
0&\frac14&-\frac14&\frac14&-\frac14&\frac12
\end{pmatrix}.
]

Porównanie jest rozstrzygające:
- (B^*B) ma niezerowe wyrazy pozadiagonalne dla par przeciwległych i zera dla par sąsiednich;
- (P_{cyc}) ma zera dla par przeciwległych i niezerowe wyrazy dla par sąsiednich.

Przykładowo:
[
\langle q_{01},q_{23}\rangle=-\frac14,
\qquad P_{cyc}(01,23)=0;
]
[
\langle q_{01},q_{02}\rangle=0,
\qquad P_{cyc}(01,02)=-\frac14.
]
Nie ma więc równości (B^*B\propto P_{cyc}), nawet po prostym przeskalowaniu. To nie obala mostu; ustala, że most nie jest identycznością współrzędnych krawędzi.

## 5. Przeszkoda (S₄) i jej dokładne obejście

Defect v0.8 ustala:
[
C^1(K₄)\cong V_{\rm std}\oplus(V_{\rm std}\otimes\mathrm{sign}),
\qquad V_{cyc}\cong V_{\rm std}\otimes\mathrm{sign}.
]
Tymczasem (W=V_ρ\cong V_{\rm std}). Są to nieizomorficzne nierozkładalne reprezentacje (S₄). Stąd
[
\operatorname{Hom}_{S₄}(W,V_{cyc})=0,
\qquad
\operatorname{Hom}_{S₄}(U,V_{cyc})=0.
]
To jest formalny powód, dla którego bezwarunkowy „most” (V_ρ\to V_{cyc}) nie istnieje. Sam fakt, że oba sektory mają wymiar 3, niczego tu nie rozstrzyga.

Po ograniczeniu do (A₄\subset S₄) sytuacja się zmienia, ponieważ
[
\mathrm{sign}|_{A₄}=1.
]
Reprezentacje (W|_{A₄}) oraz (V_{cyc}|_{A₄}) są równoważne. Wybór orientacji na (W) definiuje operator Hodge’a
[
*:W\to\Lambda^2W,
]
który jest (A₄)-ekwiwariantny. Dla nieparzystych permutacji zmienia znak — dokładnie ten znak, którego brakowało przy próbie splotu pod całym (S₄).

Niech (Phi:\Lambda^2W\to V_{cyc}\subset C^1(K₄)) będzie izometryczną wersją kanonicznej identyfikacji Defect (V_{cyc}\cong\Lambda^2W). Definiujemy:
[
\boxed{J=\sqrt2\,\Phi\circ *\circ B:U\to C^1(K₄).}
]
Wówczas, korzystając z (BB^*=\frac12 I_W):
[
\boxed{J^*J=2B^*B=P_{\mathrm{mid}},\qquad
JJ^*=P_{cyc}.}
]
To znaczy, że (J) jest częściową izometrią: przenosi sektor środków krawędzi (\operatorname{im}P_{\mathrm{mid}}\cong V_{\rm std}) na sektor cykliczny (V_{cyc}), a pozostały sektor (\ker B=\mathbf1\oplus V_2) zeruje.

Działanie symetrii spełnia:
[
\rho_{cyc}(g)J=\operatorname{sgn}(g)\,J\sigma_U(g),
\qquad g\in S₄.
]
Dla (g\in A₄) znak jest równy (+1), więc (J) jest zwykłym splotnikiem (A₄). Dla całego (S₄) jest splotnikiem skręconym znakiem. Zmiana orientacji odwraca znak (J), lecz nie zmienia projektorów (J^*J) i (JJ^*).

## 6. Interpretacja dla Axis i Defect

1. Axis nie musi zakładać osi XYZ. Osiowe trzy proste są już zakodowane w rozkładzie środków krawędzi na trzy pary antipodalne.
2. Defect nie jest „tym samym” co geometria środków. Jego sektor (V_{cyc}) ma skręcone działanie (S₄).
3. Most jest dokładny po wyborze orientacji. Symetrią, przy której staje się zwykłym splotnikiem, jest (A₄), grupa obrotów czworościanu.
4. Wspólny rdzeń to trzywymiarowy sektor standardowy przeniesiony przez orientacyjny Hodge-star do sektora cyklicznego. To wyjaśnia wspólną kombinatorykę bez zacierania różnicy reprezentacji.

## 7. Statusy i granice wniosku

- ✅ **Dowiedzione algebraicznie:** sześć środków tworzy ośmiościan; (BB^*=\frac12I_W); (P_{mid}=2B^*B) jest projektorem rangi 3; bezpośrednia macierz (B^*B) nie jest (P_{cyc}); brak zwykłego (S₄)-splotnika wynika z nieizomorficzności reprezentacji.
- ✅ **Dowiedzione konstrukcyjnie:** po wyborze orientacji istnieje częściowa izometria (J) z (J^*J=P_{mid}) oraz (JJ^*=P_{cyc}); jest (A₄)-ekwiwariantna i skręcona znakiem pod (S₄).
- 🔍 **Do niezależnej replikacji w rygorze Z1:** niezależne odtworzenie konstrukcji (J) z macierzy operatora (C) z Axis/Defect, bez używania abstrakcyjnego identyfikowania (V_{cyc}\cong\Lambda^2W). Rachunek projekcji jest dokładny, lecz konstrukcja powinna zostać odtworzona z jawnych macierzy źródłowych.
- 💡 **Hipoteza interpretacyjna:** orientacja może być matematycznym przełącznikiem między opisem osiowym i cyklicznym. Nie wynika stąd jeszcze materia, pole fizyczne ani ontologia relacja→materia.
- ❌ **Odrzucone:** utożsamianie (V_ρ) z (V_{cyc}) jako reprezentacji (S₄), utożsamianie (B^*B) z (P_{cyc}), oraz wniosek „ten sam wymiar 3, zatem ta sama przestrzeń”.

## 8. Następny test rdzenia

Najbardziej rozstrzygający kolejny krok to przepisać (J) wyłącznie przez jawne macierze Axis/Defect — w szczególności przez operator złożony z mapy brzegów 2-komórek (C) i macierzy (T) — i sprawdzić znakowy warunek splotnika dla wszystkich 24 permutacji. To sprawdzi, czy abstrakcyjny most Hodge’a jest dokładnie tym samym obiektem co most macierzowy już obecny w korzeniu Axis, czy też obie konstrukcje różnią się dodatkową konwencją.
