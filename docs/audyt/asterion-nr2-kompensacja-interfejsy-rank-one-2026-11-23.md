# N-R2: interfejsy aktów kompensacji i częściowa kompozycja rangą jeden

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Źródło operatorskie:** P₀-Centroid v5.2, definicja \(M_i=I+e_i c_i^T\), \(c_i=\mathbf1/n-e_i\); P₀-TAU v1.7.2 (sekwencja aktualizacji Gaussa–Seidla); P₀-Relacje v0.3 §§1–8.  
**Status:** interfejsy rzędu jeden odzyskiwalne z operatora ✅; częściowy iloczyn interfejsów łączny ✅; dla Centroidu każda para aktów wzajemnie oddziałuje ✅; selektywna kompozytowalność z Centroidu niewyprowadzona ❌; wyprowadzenie przestrzeni i parowania z pierwotnej relacji P₀ otwarte 💡.

## 1. Cel

Poprzedni raport sprawdził kompozycję relacji binarnych przez wspólnego świadka \(y\). Wynik był łączny, ale wymagał wspólnego nośnika \(X\) i dwóch pozycji w parze.

Teraz schodzimy do aktu kompensacji. Pytanie brzmi: czy sam akt ma wewnętrzną strukturę, która pozwala rozpoznać, czy jego efekt może zostać podjęty przez następny akt, bez jawnego nazywania źródła i celu?

W P₀-Centroid pojedynczy operator ma postać:

\[
M_i=I+D_i,\qquad D_i=e_i c_i^T,\qquad c_i=\frac1n\mathbf1-e_i.
\]

\(D_i=M_i-I\) jest częścią zmiany wywołaną przez akt. Ma rangę jeden.

## 2. Interfejsy można odtworzyć z operatora rzędu jeden

Niech \(D:V\to V\) będzie niezerowym operatorem rzędu jeden. Wtedy istnieją \(u\in V\setminus\{0\}\) i \(\phi\in V^*\setminus\{0\}\), takie że:

\[
D=u\otimes\phi,\qquad D(x)=\phi(x)u.
\]

Rozkład nie jest jednoznaczny: \(u\mapsto\lambda u\), \(\phi\mapsto\lambda^{-1}\phi\) nie zmienia D. Jednak dwie proste są wyznaczone kanonicznie:

\[
U(D)=\operatorname{Im}D=\langle u\rangle\subset V,
\]

\[
F(D)=\operatorname{Ann}(\ker D)=\langle\phi\rangle\subset V^*.
\]

Interpretacja operacyjna:
- \(U(D)\): kierunek, w którym akt pozostawia zmianę;
- \(F(D)\): kierunek czułości, który określa, na jakie składowe wejścia akt reaguje.

Nie wprowadziliśmy etykiety „źródło” lub „cel”. Otrzymaliśmy dwa wewnętrzne interfejsy operatora jako jego obraz i anihilator jądra.

To jest jednak możliwe dlatego, że założone zostały: wspólna przestrzeń liniowa V, jej dual V* i struktura liniowa. Nie jest to rekonstrukcja z gołego, nieustrukturyzowanego zbioru relacji.

## 3. Kandydat na kompozytowalność: niezerowa odpowiedź następnego aktu

Niech dwa akty będą niezerowymi operatorami rzędu jeden:

\[
D_a=u_a\otimes\phi_a,\qquad D_b=u_b\otimes\phi_b.
\]

Definiujemy „b może podjąć efekt a” przez:

\[
a\rightsquigarrow b
\iff \phi_b(u_a)\ne0.
\]

Warunek jest niezmienniczy względem niejednoznaczności faktoryzacji: skalowanie \(u_a\) lub \(\phi_b\) zmienia wartość liczbową parowania, ale nie zmienia tego, czy jest ono zerowe.

Wtedy:

\[
D_bD_a
=\phi_b(u_a)\,u_b\otimes\phi_a.
\]

Jeśli parowanie jest niezerowe, złożony efekt nadal ma rangę jeden i zachowuje zewnętrzne interfejsy: kierunek efektu b oraz czułość a.

Możemy więc zdefiniować częściowy iloczyn:

\[
D_b\diamond D_a=
\begin{cases}
D_bD_a,&\phi_b(u_a)\ne0,\\
\text{nieokreślony},&\phi_b(u_a)=0.
\end{cases}
\]

To jest konkretny kandydat na prawo następstwa oparte na wewnętrznej zgodności aktów, a nie na równości jawnie nazwanych końców.

## 4. Twierdzenie: częściowy iloczyn jest silnie łączny

Niech:

\[
D_a=u_a\otimes\phi_a,\quad
D_b=u_b\otimes\phi_b,\quad
D_c=u_c\otimes\phi_c.
\]

Obie strony potrójnego iloczynu są określone wtedy i tylko wtedy, gdy:

\[
\phi_b(u_a)\ne0
\quad\text{i}\quad
\phi_c(u_b)\ne0.
\]

Wtedy:

\[
(D_c\diamond D_b)\diamond D_a
=
\phi_c(u_b)\phi_b(u_a)\,u_c\otimes\phi_a,
\]

oraz:

\[
D_c\diamond(D_b\diamond D_a)
=
\phi_c(u_b)\phi_b(u_a)\,u_c\otimes\phi_a.
\]

Zatem:
- lewa i prawa strona są określone równocześnie;
- jeżeli są określone, są identycznym operatorem;
- ich wartość jest znów niezerowym operatorem rzędu jeden.

**Wynik ✅:** niezerowe parowanie interfejsów daje łączne działanie częściowe na niezerowych operatorach rzędu jeden.

Łączność nie wymaga równości interfejsów. Wymaga niezerowego parowania, a czynnik pośredni mnoży się w obu nawiasowaniach w tej samej kolejności.

## 5. Test na rzeczywistych generatorach Centroidu

Dla \(D_i=e_i c_i^T\) mamy:

\[
U(D_i)=\langle e_i\rangle,\qquad
F(D_i)=\langle c_i^T\rangle.
\]

Parowanie następnego aktu j z efektem aktu i wynosi:

\[
H_{ji}=\phi_j(u_i)=c_j^T e_i
=\frac1n-\delta_{ji}.
\]

W szczególności:

\[
H_{ji}=
\begin{cases}
-\frac{n-1}{n},&i=j,\\[2mm]
\frac1n,&i\ne j.
\end{cases}
\]

Dla każdego \(n\ge2\) wszystkie wpisy są niezerowe. Macierz:

\[
H_n=\frac1nJ-I=-P_\rho
\]

ma jądro rozpięte przez \(\mathbf1\), a na \(V_\rho\) działa jako \(-I\). Dla n=4 przekątna wynosi \(-3/4\), a wszystkie pozostałe wpisy \(1/4\).

Wniosek:
- każdy z n aktów może podjąć efekt dowolnego z n aktów;
- każdy akt może następować po sobie;
- każdy akt może następować po sobie samym;
- z kryterium niezerowego parowania nie wyłania się żadna częściowa sieć następstwa.

Dla N=4 nie powstaje tu selektor czterech profili. Dokładnie ten sam wynik zachodzi dla każdego n≥2.

Co więcej, dla dowolnego słowa \(i_1,\ldots,i_k\):

\[
D_{i_k}\cdots D_{i_1}
=
\left(\prod_{r=2}^{k}
\left(\frac1n-\delta_{i_r,i_{r-1}}\right)\right)
e_{i_k}c_{i_1}^T\ne0.
\]

Każdy niepusty ciąg aktów pozostawia niezerowy kanał rzędu jeden.

## 6. Ważna koncesja: składamy kanały efektu, nie pełne operatory kompensacji

Nie wolno utożsamiać \(D_bD_a\) z pełnym złożeniem aktualizacji \(M_bM_a\). Ponieważ \(M_i=I+D_i\):

\[
M_bM_a=I+D_a+D_b+D_bD_a.
\]

Częściowy iloczyn \(\diamond\) z §3 śledzi wyłącznie kanał przeniesienia efektu \(D_bD_a\). Pomija bezpośrednie składniki \(D_a\), \(D_b\) i część tożsamościową.

Tymczasem właściwa sekwencja Centroidu używa pełnych operatorów \(M_i\). Ich kompozycja jest całkowita. Każdy \(M_i\) jest odwracalny (\(\det M_i=1/n\)), więc każde skończone słowo pełnych operatorów również jest odwracalne i niezerowe.

**To zasadnicze ograniczenie:** \(\diamond\) jest spójnym prawem interakcji kanałów, ale P₀-Centroid nie mówi, że jest ono właściwą regułą następstwa samych aktów kompensacji. Wymagałoby to nowego aksjomatu: „akt może następować po innym wtedy i tylko wtedy, gdy jego czułość wykrywa niezerowy efekt poprzednika”.

Bez tego aksjomatu nie wolno zastąpić całkowitej kompozycji \(M_bM_a\) częściową kompozycją kanałów \(D_bD_a\).

## 7. Kontrmodel: niezerowe parowanie może kodować dowolną sieć

Warunek \(\phi_b(u_a)\ne0\) nie wymusza szczególnej topologii. Niech istnieje m aktów i dowolny skierowany graf na m wierzchołkach, z pętlą przy każdym wierzchołku. Weźmy \(V=\mathbb R^m\) i bazę \(e_1,\ldots,e_m\). Dla macierzy sąsiedztwa \(G\) definiujemy:

\[
u_i=e_i,\qquad
\phi_j=\sum_{i=1}^m G_{ji}e_i^*,\qquad
D_j=u_j\otimes\phi_j.
\]

Wówczas:

\[
\phi_j(u_i)=G_{ji}.
\]

A więc:

\[
i\rightsquigarrow j
\iff G_{ji}\ne0.
\]

Każdy taki graf jest realizowany przez niezerowe akty rzędu jeden, a ich częściowa kompozycja nadal jest łączna.

**Wniosek:** interfejsowa reguła może generować bardzo bogate sieci, ale sama nie wybiera ich liczby ani topologii. Można otrzymać m=3,4,5,… i dowolną zadaną sieć z pętlami. Wybór grafu został zakodowany w parowaniach, nie wyprowadzony z samego pojęcia kompensacji.

## 8. Co ten wynik mówi o N-R2?

Mamy trzy oddzielne poziomy:

1. **Akt ma interfejsy.** Dla aktu rzędu jeden jego obraz i anihilator jądra wyznaczają dwa wewnętrzne kanały. To jest wynik matematyczny.
2. **Interfejsy mogą definiować łączne następstwo.** Niezerowe parowanie daje naturalny częściowy iloczyn, który jest silnie łączny. To również jest wynik matematyczny.
3. **P₀ ma wyprowadzić, dlaczego właśnie takie interfejsy i takie parowanie są pierwotne.** Tego nie ma w obecnym korpusie. To pozostaje otwarte.

Centroid potwierdza, że akty mogą posiadać bogatą strukturę interakcji, ale w jego przypadku wszystkie kanały są wzajemnie sprzężone. Sekwencyjność TAU dodaje kolejność aktualizacji, lecz harmonogram jest dany z zewnątrz; nie wyłania się z interfejsów.

## 9. Werdykt

- **✅** Niezerowy operator rzędu jeden wyznacza własny kierunek efektu i własną linię czułości.
- **✅** Niezerowe parowanie linii czułości następnego aktu z kierunkiem efektu poprzednika daje łączne działanie częściowe.
- **✅** Dla generatorów Centroidu wszystkie parowania są niezerowe, niezależnie od n≥2.
- **✅** Rodzina operatorów rzędu jeden może realizować dowolną skończoną sieć kompozytowalności z pętlami.
- **❌** W Centroidzie kryterium niezerowego parowania nie daje selektywnej kompozycji; pełne operatory \(M_i\) i tak składają się całkowicie.
- **❌** Reguła interfejsowa nie wyprowadza n=4 ani K₄.
- **💡** Interfejsy efekt–czułość są kandydatem na pośredni język między aktem kompensacji a kompozytowalnością, ale ich pierwotność i reguła niezerowego parowania wymagają osobnego uzasadnienia.

## 10. Następny krok

Najważniejsza próba nie polega już na szukaniu kolejnej definicji kompozycji. Trzeba znaleźć **niezmiennik aktu**, który nie wymaga wcześniej danej przestrzeni liniowej ani dualności, a mimo to rozdziela jego „efekt” i „czułość”.

Możliwy test: potraktować dwa akty jako wzajemną zmianę opisów i sprawdzić, czy ich wzajemna odpowiedź daje antysymetryczny lub symetryczny skalar, którego zero/niezero jest wewnętrznym kryterium następstwa. Należy jednak uważać: sama taka liczba może już zakładać ukryty iloczyn lub metrykę.

Warunki zaliczenia następnego kroku:
1. definicja z danych aktu, a nie z zewnętrznego V;
2. niezmienniczość względem zmiany reprezentacji;
3. łączność dla trzech aktów;
4. kontrmodele z różnymi m, w tym 3,4,5;
5. dopiero potem sprawdzenie, czy korzenie P₀ wyróżniają jedną rodzinę.

## 11. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
