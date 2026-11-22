# K₄: czy sekwencyjność wybiera orientację? — audyt TAU/Wave

Data: 2026-11-22  
Zakres: matematyczne korzenie P₀; bez ingerencji w MVP-02  
Źródła na \`main\`: \`P0-Axis_v0_3.md\`, \`P0-TAU-v1_7_2.md\`, \`P0-Wave-v0_6_1.md\`  
Powiązanie: raport \`asterion-k4-midpoints-defect-a4-2026-11-22.md\`

## 1. Konkluzja

**Sekwencja może nieść orientację K₄, ale obecne korzenie TAU/Wave nie dowodzą, że dynamika autonomicznie wybiera tę sekwencję z samego nieukierunkowanego K₄.**

To rozróżnienie ma ścisłą postać:

- statyczny K₄, \(p_0\) i \(G_4\) mają pełną symetrię \(S_4\);
- orientacja przestrzeni \(V_\rho\) transformuje według reprezentacji znakowej \(\mathrm{sign}\);
- deterministyczna dynamika \(S_4\)-ekwiwariantna, startująca z pełnego stanu \(S_4\)-niezmienniczego, nie może wybrać jednej niezerowej orientacji;
- wskazany harmonogram \(\sigma\) aktualizacji wszystkich czterech wierzchołków definiuje natomiast niezerowy element linii orientacji. Jest to orientacja **historii/harmonogramu**, nie dowód spontanicznego wyboru harmonogramu.

Statusy: ✅ dla twierdzeń algebraicznych poniżej; 💡 dla interpretacji sekwencji jako wewnętrznego mechanizmu wyboru orientacji; brak dowodu na autonomiczny selektor.

## 2. Orientacja K₄ jako reprezentacja znakowa

Niech
\[
W=V_\rho=\{x\in\mathbb R^4:\sum_i x_i=0\},
\qquad v_i=e_i-\frac14\mathbf1.
\]
Działanie \(\pi\in S_4\) na \(W\) ma wyznacznik
\[
\det(\rho(\pi))=\mathrm{sgn}(\pi).
\]
Wobec tego jednowymiarowa przestrzeń orientacji
\[
\det W:=\Lambda^3W
\]
jest reprezentacją znakową \(S_4\). Parzyste permutacje zachowują orientację, nieparzyste ją odwracają. Jej stabilizatorem jest dokładnie
\[
\operatorname{Stab}_{S_4}(\Omega)=A_4.
\]

To wyraża geometrię Axis w języku czystej algebry: \(A_4\) nie jest arbitralnie wybraną podgrupą. Jest jądrem charakteru wyznacznika standardowej reprezentacji K₄.

## 3. Harmonogram jednego pełnego przejścia niesie orientację

Niech
\[
\sigma=(i_0,i_1,i_2,i_3)
\]
będzie kolejnością, w której po raz pierwszy aktualizowane są cztery różne wierzchołki. Definiujemy
\[
\Omega_\sigma=
(v_{i_1}-v_{i_0})\wedge
(v_{i_2}-v_{i_0})\wedge
(v_{i_3}-v_{i_0})
\in\Lambda^3W.
\]
Wektory w nawiasach są liniowo niezależne, więc \(\Omega_\sigma\ne0\). Ich macierz Grama, niezależnie od \(\sigma\), ma postać
\[
\begin{pmatrix}
2&1&1\\
1&2&1\\
1&1&2
\end{pmatrix},
\qquad \det=4,
\]
a zatem \(\|\Omega_\sigma\|=2\) w metryce zewnętrznej indukowanej ze standardowej metryki na \(W\).

Dla relabelingu \(\pi\in S_4\):
\[
\boxed{\Omega_{\pi\sigma}
=\Lambda^3\rho(\pi)\,\Omega_\sigma
=\mathrm{sgn}(\pi)\,\Omega_\sigma.}
\]
Wynik:
- 12 harmonogramów parzystych niosą tę samą orientację;
- 12 harmonogramów nieparzystych niosą orientację przeciwną;
- orientacyjna klasa harmonogramu ma stabilizator \(A_4\).

To jest konstrukcja bez XYZ i bez dodatkowej geometrii osadzonej: kolejność czterech relacyjnych wierzchołków wyznacza orientację 3-simpleksu.

**Ale:** jeśli harmonogram \(\sigma\) został zadany z zewnątrz, orientacja została dostarczona przez harmonogram. Sam rachunek nie wyjaśnia, dlaczego właśnie ten harmonogram został wybrany.

Dla słowa Wave \(w\), które zawiera wszystkie symbole \(M_0,M_1,M_2,M_3\), można analogicznie wziąć kolejność pierwszego wystąpienia tych czterech symboli. Otrzymujemy \(\Omega_w\). Jest to niezmiennik historii słowa (z zachowaniem jego kolejności), niekoniecznie niezmiennik samego operatora \(\rho(w)\).

## 4. Twierdzenie o braku autonomicznego wyboru z danych symetrycznych

Niech \(X\) będzie przestrzenią stanów relacyjnych z działaniem \(S_4\), a \(x_0\in X\) stanem niezmienniczym pod całym \(S_4\). Niech \(F:X\to X\) będzie deterministyczną dynamiką ekwiwariantną:
\[
F(\pi x)=\pi F(x).
\]
Wtedy dla każdego \(t\):
\[
\pi F^t(x_0)=F^t(\pi x_0)=F^t(x_0).
\]
Każdy stan trajektorii pozostaje więc \(S_4\)-niezmienniczy.

Załóżmy, że z takiego stanu można wyznaczyć orientację \(\Omega(x)\in\Lambda^3W\), ekwiwariantnie względem działania grupy:
\[
\Omega(\pi x)=\mathrm{sgn}(\pi)\Omega(x).
\]
Ponieważ \(x_t=F^t(x_0)\) jest niezmienniczy, dla dowolnej nieparzystej \(\pi\):
\[
\Omega(x_t)=\Omega(\pi x_t)
=\mathrm{sgn}(\pi)\Omega(x_t)
=-\Omega(x_t).
\]
Stąd \(\Omega(x_t)=0\), co nie jest orientacją.

**Twierdzenie (✅):** dynamika deterministyczna, \(S_4\)-ekwiwariantna i startująca z pełnego stanu \(S_4\)-symetrycznego nie może wybrać jednej z dwóch orientacji K₄.

Granice twierdzenia:
- nie dotyczy dynamiki z zadanym harmonogramem, który już łamie symetrię;
- nie wyklucza spontanicznego złamania symetrii przez losową realizację lub perturbację; w symetrycznym zespole takich realizacji nie ma jednak wyróżnionego znaku orientacji;
- nie rozstrzyga dynamiki z dodatkowym stanem wewnętrznym, który sam niesie orientację.

## 5. Co rzeczywiście mówią TAU i Wave

### TAU

TAU §7.3.0 podaje:
\[
R_\sigma(\alpha)=P_\sigma R_{\rm id}(\alpha)P_\sigma^{-1}.
\]
Tożsamość oznacza, że harmonogramy są permutacyjnie sprzężone. Własności spektralne pełnej rundy, w tym argument dominującej pary zespolonej, są takie same dla wszystkich kolejności. Twierdzenia §7.3.1–7.3.2 pokazują, że kolejność zmienia rozkład wag końcowego konsensusu, ale nie tempo zbieżności i nie wybierają kolejności aktualizacji.

Dlatego faza \(25{,}77^\circ\) nie jest sama w sobie selektorem orientacji: pozostaje niezmieniona przy sprzężeniu przez nieparzystą permutację. Jest parametrem spektralnym sekwencji, nie znakiem jej orientacji.

TAU §1.1 jawnie kwalifikuje aksjomat sekwencyjności jako fenomenologiczny, motywacyjny i niefalsyfikowalny w tym dokumencie. TAU zakłada, że relacja ma porządek zdarzeń; nie podaje autonomicznego prawa, które ten porządek generuje z symetrycznego K₄.

### Wave

Wave §1 definiuje słowo jako ciąg liter \(\Sigma=\{M_0,M_1,M_2,M_3,T\}\), a operator jako jego interpretację. To właściwe miejsce do przechowywania historii: dwa słowa mogą różnić się kolejnością, nawet jeśli interesujący nas obserwowany parametr spektralny jest ten sam.

W ilorazie relacyjnym \(W\):
\[
\det(\bar M_i)=\frac14,\qquad
\det(\bar T)=-1,
\]
gdzie \(T=(0123)\) jest 4-cyklem. Zatem dla słowa z \(n_M\) literami typu \(M_i\) i \(n_T\) wystąpieniami \(T\):
\[
\boxed{\det(\bar\rho(w))
=4^{-n_M}(-1)^{n_T}.}
\]
To jest dokładny charakter orientacyjny operatora słowa: mówi, czy operator zachowuje, czy odwraca **już wybraną** orientację. Nie wybiera jej sam. W szczególności \(T\) jest permutacją nieparzystą i działa jako odwrócenie orientacji; wprowadzenie \(T\) jest zatem wprowadzeniem konkretnego generatora o znanej parzystości, nie wyprowadzeniem absolutnej orientacji z \(p_0\).

Dla pełnego harmonogramu zawierającego każdy \(M_i\) dokładnie raz, bez \(T\), wyznacznik produktu wynosi zawsze \(4^{-4}=1/256>0\), niezależnie od parzystości kolejności. To dodatkowo pokazuje, że parzystość harmonogramu \(\mathrm{sgn}(\sigma)\) i znak wyznacznika produktu operatorów nie są tym samym obiektem.

## 6. P23 i otwarta możliwość orientacji DAG

TAU §7.7 pozostawia P23 jako problem „naturalnej orientacji DAG” w statusie 🔍, z kandydatami: indeks, znak \(D_e\) (M16), para przeciwległa. Wcześniejszy wynik Claude'a został uznany za artefakt \(\alpha=0{,}5\). Nie ma podstaw, by uznać P23 za rozwiązany selektor orientacji K₄.

Warto rozdzielić dwa pytania:
1. czy DAG powstający z faktycznej historii aktualizacji ma orientację zgodną z \(\Omega_\sigma\)?
2. czy reguła tworzenia DAG potrafi wygenerować \(\sigma\) bez zewnętrznego harmonogramu i bez etykietowania wierzchołków?

Pierwsze jest testowalne dla ustalonego harmonogramu. Drugie jest właściwym problemem selekcji.

## 7. Status i dalszy kierunek matematyczny

- ✅ **Orientacja statyczna:** orientacja \(V_\rho\) transformuje jak \(\mathrm{sign}\); jej stabilizatorem jest \(A_4\).
- ✅ **Orientacja historii:** dowolna pełna kolejność czterech aktualizacji definiuje niezerowy \(\Omega_\sigma\); parzyste i nieparzyste harmonogramy wybierają przeciwne orientacje.
- ✅ **No-go:** symetryczna dynamika \(S_4\)-ekwiwariantna nie wybiera orientacji z symetrycznego stanu początkowego.
- ✅ **Wave:** wyznacznik słowa jest \(4^{-n_M}(-1)^{n_T}\); opisuje działanie na orientacji, nie jej absolutny wybór.
- 🔍 **TAU:** kolejność wpływa na konsensus, lecz twierdzenia TAU nie dostarczają selektora kolejności.
- 💡 **Hipoteza:** jeśli kolejność zdarzeń jest zmienną wewnętrzną P₀, a nie wejściowym harmonogramem, może stanowić źródło orientacji. Trzeba jednak podać jawne prawo wyboru i pokazać, że nie przemyca ono etykiet lub orientacji.

**Werdykt:** sekwencyjność daje P₀ nośnik orientacji w historii. Nie dowodzi jeszcze, że P₀ wybiera orientację z niczego. Najmocniejsza następna próba to znaleźć wewnętrzną, \(S_4\)-ekwiwariantną regułę wyboru kolejnego wierzchołka, a następnie sprawdzić, czy jej spontaniczne trajektorie tworzą dwie klasy \(\Omega\) o stabilizatorze \(A_4\), bez uprzywilejowanego indeksu.
