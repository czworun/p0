# N-R2: wspólne niezmienniki jako reguła kompozycji aktów Centroidu

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Punkty odniesienia:** P₀-Centroid v5.2; P₀-TAU v1.7.2; P₀-Relacje v0.3 §§4, 6, 15; poprzednie raporty Asteriona o interfejsach rzędu jeden i częściowych przekształceniach.  
**Status:** dokładna formuła wspólnych niezmienników dla dowolnego słowa Centroidu ✅; przecięcie niezmienników daje łączne działanie częściowe ✅; n=4 jest minimalne dla zachowania niezerowego wspólnego niezmiennika przez dwa różne akty ✅/warunkowo; wyprowadzenie rodziny generatorów i n z pierwotnej relacji P₀ nadal otwarte 💡.

## 1. Pytanie

Czy zgodność dwóch aktów można rozpoznać po tym, co oba akty zachowują, zamiast po dopasowaniu ich źródeł i celów?

Poprzednie kryterium niezerowego parowania interfejsów \(V^*\times V\) było dla Centroidu zbyt liberalne: każda para generatorów była zgodna. Teraz używamy przestrzeni wspólnych niezmienników, które przeżywają działanie aktów.

To nadal rachunek w Centroidzie, a nie gotowa redukcja do pierwotnej ontologii P₀. Potencjalna wartość polega na tym, że zgodność może być zdefiniowana wewnętrznie z operatorów i ich niezmienników.

## 2. Operator na przestrzeni różnic

Niech:

\[
M_i=I+e_i c_i^T,\qquad
c_i=\frac1n\mathbf1-e_i,\qquad
P_\rho=I-\frac1nJ.
\]

Linia konsensusu \(\langle\mathbf1\rangle\) jest niezmiennicza, więc operatory schodzą do ilorazu \(\mathbb R^n/\langle\mathbf1\rangle\), identyfikowanego z \(V_\rho=\mathbf1^\perp\). Oznaczmy operator indukowany przez:

\[
\bar M_i=P_\rho M_i|_{V_\rho}.
\]

Dla \(x\in V_\rho\), ponieważ \(\mathbf1^Tx=0\), mamy \(M_ix=x-e_ix_i\), zatem:

\[
\bar M_i x=x-v_i x_i,\qquad
v_i=e_i-\frac1n\mathbf1.
\]

Identyfikujemy \(V_\rho^*\) z \(V_\rho\) przez standardowe parowanie euklidesowe. Dla \(w\in V_\rho\):

\[
w^T\bar M_i x=w^Tx-w_i x_i.
\]

Stąd:

\[
w^T\bar M_i=w^T
\iff w_i=0.
\]

Czyli pojedynczy akt zachowuje dokładnie te liniowe obserwable, które nie zależą od aktualizowanej współrzędnej.

## 3. Twierdzenie o niezmiennikach dowolnej sekwencji

Niech:

\[
P_\omega=M_{i_k}\cdots M_{i_1}
\]

będzie produktem dodatniego słowa generatorów Centroidu. Niech \(I(\omega)\) oznacza zbiór różnych indeksów występujących w słowie, a \(J(\omega)=\{0,\ldots,n-1\}\setminus I(\omega)\) — indeksy, których w tym słowie nie aktualizowano.

Definiujemy przestrzeń zachowanych obserwabli na ilorazie:

\[
\mathcal I(\omega)=
\{w\in V_\rho^*:w^T\bar P_\omega=w^T\}.
\]

**Twierdzenie.**

\[
\boxed{
\mathcal I(\omega)=
\left\{w\in V_\rho:
w_i=0\ \text{dla każdego }i\in I(\omega)\right\}.
}
\]

W konsekwencji:

\[
\boxed{
\dim\mathcal I(\omega)
=\max(n-|I(\omega)|-1,0).
}
\]

### Dowód

Każde \(M_i\) jest macierzą wierszowo-stochastyczną: wszystkie wiersze poza i-tym są jednostkowe, a i-ty wiersz jest równy \((1/n,\ldots,1/n)\). Produkt \(P_\omega\) również jest wierszowo-stochastyczny.

Jeżeli indeks j nie występuje w słowie, j-ty wiersz produktu pozostaje równy \(e_j^T\). Jest to stan pochłaniający odpowiadający nieaktualizowanej współrzędnej.

Jeżeli indeks i występuje w słowie, to przy jego ostatniej aktualizacji i-ty wiersz staje się średnią wszystkich aktualnych wierszy. Każda kolumna produktu ma niezerowy wpis w przynajmniej jednym wierszu: własność ta zachodzi dla macierzy jednostkowej i jest zachowana przez operację uśrednienia wiersza. Zatem po ostatniej aktualizacji i-ty wiersz jest ściśle dodatni.

W rezultacie \(P_\omega\) jest macierzą przejścia skończonego łańcucha Markowa, w którym:
- każdy j∈J jest odrębnym stanem pochłaniającym;
- każdy i∈I jest przejściowy, ponieważ jego wiersz jest dodatni i z każdego takiego stanu istnieje dodatnie prawdopodobieństwo przejścia do każdego j∈J.

Jeśli J jest niepuste, lewa przestrzeń własna dla wartości 1 jest rozpięta przez wektory \(e_j^T\), j∈J. Jej część o sumie współrzędnych równej zero ma wymiar \(|J|-1\) i składa się dokładnie z wektorów wspartych na J. Jeśli J jest puste, macierz jest ściśle dodatnia, więc rozkład stacjonarny jest jedyny i nie ma niezerowego niezmiennika o sumie zero.

Po przejściu do ilorazu przez linię konsensusu otrzymujemy:

\[
\mathcal I(\omega)=
\{w:\mathbf1^Tw=0,\ w_i=0\text{ dla }i\in I(\omega)\}.
\]

Jej wymiar wynosi \(\max(|J|-1,0)=\max(n-|I|-1,0)\). ∎

## 4. Wymiary dla n=2,3,4,5

Wymiar zależy wyłącznie od liczby r różnych generatorów użytych w słowie, a nie od ich kolejności ani liczby powtórzeń:

\[
\dim\mathcal I(\omega)=\max(n-r-1,0).
\]

| n | r=1 | r=2 | r=3 | r=4 |
|---:|---:|---:|---:|---:|
| 2 | 0 | 0 | — | — |
| 3 | 1 | 0 | 0 | — |
| 4 | 2 | 1 | 0 | 0 |
| 5 | 3 | 2 | 1 | 0 |

Interpretacja:
- n=3: jeden akt zostawia jeden niezmiennik, ale dwa różne akty niszczą wszystkie niezmienniki o sumie zero;
- n=4: dwa różne akty pozostawiają dokładnie jeden niezmiennik;
- n=5: dwa różne akty pozostawiają dwa niezmienniki, a trzy różne — jeden.

**Wniosek warunkowy:** n=4 jest najmniejszym rozmiarem, w którym dwa różne akty Centroidu mogą zachować wspólny niezerowy niezmiennik.

## 5. Łączne prawo kompozycji przez przecięcie niezmienników

Dla produktu P z dodatniego semigroupeneratorowego Centroidu definiujemy \(\mathcal I(P)\) jako jego przestrzeń zachowanych obserwabli na \(V_\rho\).

Dla dwóch produktów P,Q, przy kolejności „najpierw P, potem Q”, proponujemy:

\[
P\diamond Q=
\begin{cases}
QP,&\mathcal I(P)\cap\mathcal I(Q)\ne\{0\},\\
\text{nieokreślone},&\mathcal I(P)\cap\mathcal I(Q)=\{0\}.
\end{cases}
\]

Z twierdzenia z §3 wynika dokładna tożsamość:

\[
\boxed{\mathcal I(QP)=\mathcal I(P)\cap\mathcal I(Q).}
\]

Dlatego:
- jeśli P i Q mają wspólny niezerowy niezmiennik, ich iloczyn ma dokładnie tę przestrzeń zachowanych obserwabli;
- jeśli nie mają wspólnego niezmiennika, iloczyn jest niedopuszczalny w częściowym działaniu;
- wartość kompozycji jest zwykłym iloczynem operatorów, z zachowaniem kolejności.

### Łączność

Dla trzech produktów P,Q,R:

\[
\mathcal I((P\diamond Q)\diamond R)
=
(\mathcal I(P)\cap\mathcal I(Q))\cap\mathcal I(R),
\]

oraz:

\[
\mathcal I(P\diamond(Q\diamond R))
=
\mathcal I(P)\cap(\mathcal I(Q)\cap\mathcal I(R)).
\]

Obie strony są określone dokładnie wtedy, gdy:

\[
\mathcal I(P)\cap\mathcal I(Q)\cap\mathcal I(R)\ne\{0\}.
\]

Jeżeli są określone, obie dają ten sam operator \(RQP\).

**Wynik ✅:** w dodatnim semigroupeneratorowym Centroidu przecięcie wspólnych przestrzeni zachowanych niezmienników definiuje silnie łączne działanie częściowe.

Nie jest to dowolny aksjomat łączności. Jest konsekwencją dokładnej reguły \(\mathcal I(QP)=\mathcal I(P)\cap\mathcal I(Q)\), dowiedzionej przez strukturę absorbujących i przejściowych współrzędnych produktu stochastycznego.

## 6. Co dokładnie robi n=4?

Dla dwóch różnych generatorów \(M_i,M_j\), przy n=4, niech k,l będą dwoma pozostałymi indeksami. Wtedy:

\[
\mathcal I(M_i)\cap\mathcal I(M_j)
=
\operatorname{span}\{e_k-e_l\}.
\]

Po dwóch różnych aktualizacjach pozostaje zatem jedna różnica między dwiema nieaktualizowanymi współrzędnymi.

Jeżeli następnym aktem jest ponownie jeden z już użytych generatorów, ta linia przetrwa. Jeżeli do sekwencji dołączymy trzeci, nowy generator, nie pozostanie żaden niezerowy niezmiennik na \(V_\rho\).

Ogólnie, po sekwencji można zachować niezerową przestrzeń relacyjnej pamięci tylko wtedy, gdy co najmniej dwie współrzędne nie zostały jeszcze aktualizowane:

\[
|I(\omega)|\le n-2.
\]

Jest to selekcja **minimalnego rozmiaru dla dwóch różnych aktów**, a nie dowód, że jedynym możliwym rozmiarem jest cztery.

## 7. Ważne zastrzeżenia

1. Kryterium dopuszczalności \(\mathcal I(P)\cap\mathcal I(Q)\ne0\) jest symetryczne w P,Q. Kolejność nadal wpływa na wynik \(QP\), ale sam test wspólnego niezmiennika nie wybiera kierunku następstwa.
2. Dowód jest specyficzny dla dodatnich słów w generatorach Centroidu. Nie wolno przenosić go na dowolne endomorfizmy: kompozycja ogólnych operatorów może tworzyć nowe niezmienniki przez kasowanie lub periodyczność.
3. Przestrzeń \(V_\rho\), rodzina \(\{M_i\}\) i liczba n są już zadane. Nie wyprowadziliśmy ich z P₀-Relacje.
4. Pełne operatory Centroidu nadal składają się całkowicie. Częściowość dotyczy nowej reguły zachowania niezerowego wspólnego niezmiennika, nie pierwotnego mnożenia macierzy.
5. Dodatnie słowa w generatorach nie dostarczają lokalnych identyczności: ich wyznacznik wynosi \(n^{-k}\), więc nie są idempotentami. Łączność częściowa nie implikuje istnienia jednostek.

## 8. Potencjalny most do N-R2

Mamy teraz konkretną postać tego, czego wcześniej brakowało:

- akt pozostawia zbiór niezmienników;
- dwa akty mogą być składane, jeśli zachowują wspólny niezerowy niezmiennik;
- złożony akt zachowuje dokładnie przecięcie ich przestrzeni niezmienników;
- przecięcie jest łączne, więc prawo kompozycji jest łączne.

W języku P₀ można to interpretować jako ślad relacyjny, który przetrwał dwa akty kompensacji. Dla n=4 jest to dokładnie jeden niezależny kontrast między dwiema nieaktualizowanymi współrzędnymi.

To jest pierwszy kandydat, w którym liczba cztery pojawia się jako minimalny próg zachowania wspólnej relacyjnej pamięci przez dwa różne akty, zamiast jako liczba założona w definicji geometrii.

Nie można jednak jeszcze powiedzieć, że P₀ wyprowadza cztery. Potrzebny jest niezależny argument, dlaczego pierwotny formalizm powinien wymagać niezerowego wspólnego niezmiennika dla dwóch różnych aktów i dlaczego minimalna wystarczająca przestrzeń, a nie większa, jest właściwym wyborem.

## 9. Werdykt

- **✅** Dla dowolnego dodatniego słowa Centroidu przestrzeń zachowanych obserwabli jest dokładnie przestrzenią kontrastów na współrzędnych nieaktualizowanych.
- **✅** Jej wymiar wynosi \(\max(n-r-1,0)\), gdzie r jest liczbą różnych generatorów w słowie.
- **✅** Przecięcie przestrzeni niezmienników wyznacza łączne działanie częściowe na dodatnim semigroupeneratorowym Centroidu.
- **✅** n=4 jest najmniejszym rozmiarem, w którym dwa różne akty Centroidu pozostawiają wspólny niezerowy niezmiennik.
- **🔍** Dla n=4 wspólny niezmiennik pary aktów jest jednowymiarowy i odpowiada kontrastowi dwóch nieaktualizowanych współrzędnych.
- **❌** Nie wynika z tego jeszcze, że pierwotna relacja P₀ musi zachowywać taki niezmiennik ani że n=4 jest jedyną dopuszczalną liczbą.
- **💡** Wspólna zachowana obserwabla może być właściwym pojęciem relacyjnego śladu, który organizuje kompozycję aktów.

## 10. Następny test

Należy sprawdzić, czy ta sama reguła występuje poza Centroidem:
1. w P₀-Scalar — czy niezmienniki składowych i ich rozdzielenie spełniają analogiczną regułę przecięcia;
2. w P₀-Alchemy — czy próg rezydualny pozostawia wspólną niezerową relacyjną pamięć po dwóch aktach;
3. w P₀-Relacje — czy można zdefiniować \(\mathcal I(R)\) bez przestrzeni liniowej, np. jako zbiór stabilnych obserwabli lub równoważności konfiguracji;
4. czy warunek „co najmniej jeden wspólny niezmiennik” jest aksjomatem P₀, czy tylko własnością rodziny operatorów Centroidu.

Nie należy jeszcze przenosić statusu ✅ z rachunku Centroidu na cały korzeń N-R2.

## 11. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
