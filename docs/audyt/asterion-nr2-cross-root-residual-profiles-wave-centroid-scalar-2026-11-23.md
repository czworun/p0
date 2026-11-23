# N-R2: porównanie profili resztkowych — Wave, Centroid i Scalar

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Punkty odniesienia:** P₀-Wave v0.6.1; P₀-Centroid v5.2; P₀-Scalar v0.3.5; wcześniejsze raporty o profilach resztkowych, niezmiennikach Centroidu i punktach stałych A2.  
**Status:** dokładny automat resztkowy Centroidu ✅; nieizomorficzność języków Wave i Centroid przy zachowaniu akceptacji ✅; Scalar nie wyznacza jednego języka bez warunku początkowego ✅; wspólny formalizm profili istnieje warunkowo względem języka dopuszczalności ✅; wyprowadzenie takiego języka z P₀-Relacje pozostaje otwarte 💡.

## 1. Pytanie i kryterium porównania

Poprzedni raport skonstruował profil historii z jej możliwych przyszłych kontynuacji. Dla języka historii \(\mathcal L\subseteq A^+\):

\[
F_h=\{z\in A^*:hz\in\mathcal L\},
\qquad
h\approx_{\mathcal L}k\iff F_h=F_k.
\]

Akty indukują na niepustych profilach dobrze określone częściowe przejścia. Ich kompozycja jest silnie łączna, także gdy \(\mathcal L\) nie jest domknięty na fragmenty.

To twierdzenie jest ogólne. Nie odpowiada jeszcze na pytanie, czy trzy korzenie P₀ dostarczają ten sam język \(\mathcal L\), ani czy ich profile mają tę samą strukturę.

W tym raporcie stosuję kryteria bezpośrednio związane z wynikami każdego korzenia:

- **Wave:** propagacyjność, czyli istnienie niebanalnego modu na okręgu jednostkowym w przestrzeni relacyjnej.
- **Centroid:** przetrwanie co najmniej jednego niezerowego niezmiennika liniowego po słowie generatorów.
- **Scalar:** osiąganie lub utrzymywanie stabilnej konfiguracji progowej A2.

Nie zakładam z góry, że te trzy kryteria są równoważne.

## 2. Centroid: dokładny język i automat resztkowy

Niech alfabetem będzie \(A=\{0,\ldots,n-1\}\), a słowo \(w=i_1\cdots i_k\) oznacza dodatni produkt generatorów Centroidu:

\[
P_w=M_{i_k}\cdots M_{i_1},
\qquad
M_i=I+e_i c_i^T,
\qquad
c_i=\frac1n\mathbf1-e_i.
\]

Pracujemy na przestrzeni relacyjnej \(V_\rho=\mathbf1^\perp\), czyli po usunięciu globalnego kierunku konsensusu.

Z wcześniejszego twierdzenia o niezmiennikach:

\[
\dim\mathcal I(w)=
\max(n-|I(w)|-1,0),
\]

gdzie \(I(w)\) jest zbiorem różnych indeksów występujących w słowie, a \(\mathcal I(w)\) jest przestrzenią zachowanych lewych obserwabli na \(V_\rho\).

To samo kryterium można zapisać spektralnie. Produkt \(P_w\) jest macierzą wierszowo-stochastyczną. Nieaktualizowane indeksy \(J=A\setminus I(w)\) są stanami pochłaniającymi, a zaktualizowane indeksy są przejściowe, gdy \(J\ne\varnothing\). Gdy \(J=\varnothing\), produkt jest ściśle dodatni. W obu przypadkach wszystkie niejednostkowe wartości własne mają moduł mniejszy od 1. Na ilorazie przez konsensus pozostaje więc niezerowy mod jednostkowy dokładnie wtedy, gdy \(|J|\ge2\).

Definiujemy zatem język:

\[
\boxed{
\mathcal L_C=
\{w\in A^+:\ |I(w)|\le n-2\}.
}
\]

Jest to język domknięty na wszystkie niepuste fragmenty.

### 2.1. Profile przyszłości

Dla niepustej historii \(h\), która sama należy do \(\mathcal L_C\), otrzymujemy:

\[
F_h=
\{z\in A^*:|I(h)\cup I(z)|\le n-2\}.
\]

Profil zależy wyłącznie od zbioru już użytych indeksów \(S=I(h)\), a nie od kolejności ani liczby powtórzeń.

Dla historii początkowej \(\varepsilon\):

\[
F_\varepsilon=\mathcal L_C.
\]

Dla \(n\ge3\) profil początkowy jest niepusty i różny od profili po niepustych historiach, ponieważ nie zawiera \(\varepsilon\), podczas gdy każdy profil po historii z \(\mathcal L_C\) zawiera \(\varepsilon\).

Profile odpowiadające różnym podzbiorom \(S,T\) o liczności nie większej niż \(n-2\) są różne. Po ewentualnej zamianie ról wybierz \(x\in S\setminus T\). Dobierz zbiór \(Z\) tak, aby \(T\subseteq Z\), \(|Z|=n-2\) oraz \(x\notin Z\). Taki wybór jest możliwy: do \(T\) trzeba dodać \(n-2-|T|\) indeksów, a poza \(T\cup\{x\}\) pozostaje \(n-|T|-1\) indeksów. Dla słowa \(z\) o nośniku \(Z\), kontynuacja jest dopuszczalna po \(T\), bo \(|T\cup Z|=n-2\), ale niedopuszczalna po \(S\), bo \(x\in S\setminus Z\) daje \(|S\cup Z|\ge n-1\).

Dla \(n\ge3\) otrzymujemy dokładną reprezentację żywych profili przez podzbiory:

\[
\boxed{
\mathrm{States}_{C,\mathrm{live}}
\cong
\{S\subseteq A:\ |S|\le n-2\}.
}
\]

Dla \(n\ge3\) liczba żywych profili, z profilem początkowym włącznie, wynosi:

\[
\boxed{
N_C(n)=\sum_{r=0}^{n-2}\binom nr.
}
\]

Historia z co najmniej \(n-1\) różnymi indeksami ma pusty profil przyszłości i jest stanem martwym; nie wliczam go do liczby żywych profili.

### 2.2. Przejścia

Dla \(S\subseteq A\), \(|S|\le n-2\), akt \(i\) działa według reguły:

\[
\delta_i(S)=
\begin{cases}
S\cup\{i\},& |S\cup\{i\}|\le n-2,\\
\text{nieokreślone},& |S\cup\{i\}|>n-2.
\end{cases}
\]

To obcięta krata podzbiorów. Ponowne użycie indeksu daje pętlę, a nowy indeks zwiększa zbiór aż do granicy \(n-2\).

Dla \(n=4\):

\[
N_C(4)=\binom40+\binom41+\binom42=1+4+6=11.
\]

Jest więc jeden profil początkowy, cztery profile po użyciu jednego generatora i sześć po użyciu dwóch różnych generatorów. Po pojawieniu się trzeciego różnego generatora przyszły profil jest pusty.

Dla \(n=2\) język \(\mathcal L_C\) jest pusty, więc nie ma żywych profili. Dla porównania \(N_C(3)=1+3=4\). Ta liczba cztery pojawia się dla \(n=3\), a nie \(n=4\), i jest wyłącznie liczbą węzłów obciętej kraty. Nie jest selektorem wymiaru ani argumentem na rzecz \(K_4\).

**Wynik ✅:** język Centroidu i jego żywy automat resztkowy są dokładnie wyznaczone przez liczbę różnych aktywnych generatorów.

## 3. Wave: profil żywy bez propagacyjności historii

W Wave język \(\mathcal L_W\) jest wyznaczony przez istnienie niebanalnego modu jednostkowego na przestrzeni relacyjnej.

Z wcześniejszego dokładnego rachunku:

\[
W=02T13T\in\mathcal L_W,
\]

ponieważ:

\[
\chi_{\rho(W)}(x)=
(x-1)(x+1)(256x^2-45x-1)/256,
\]

a więc \(W\) ma relacyjny mod \(\lambda=-1\).

Jednocześnie dla początkowego fragmentu \(U=02T\):

\[
\chi_{\rho(U)}(x)=
(x-1)(16x^3+7x^2+2x+1)/16.
\]

Pierwiastki czynnika kubicznego mają moduł z przedziału \([2/7,1/2]\), więc poza globalnym konsensusem U nie ma modułu jednostkowego:

\[
U\notin\mathcal L_W.
\]

Mimo to:

\[
F_U\ne\varnothing,
\]

ponieważ kontynuacja \(13T\) prowadzi do \(W\in\mathcal L_W\).

To daje strukturalną różnicę wobec Centroidu:

- w Centroidzie, z powodu domknięcia języka na fragmenty, każda niepusta historia z niepustym profilem jest już dopuszczalna;
- w Wave istnieje historia niepropagacyjna, lecz żywa, ponieważ ma przyszłą propagacyjną kontynuację.

Zatem automaty resztkowe Wave i Centroid nie są izomorficzne jako automaty oznaczone językiem akceptacji, nawet po dopuszczeniu przemianowania alfabetu: własność domknięcia na fragmenty jest niezmiennikiem takiego izomorfizmu.

Nie wyznaczono jeszcze liczby ani skończoności wszystkich profili resztkowych Wave. Kontrprzykład \(U,W\) dowodzi nie-factorialności, ale nie rozstrzyga rozmiaru minimalnego automatu.

**Wynik ✅:** Wave ma żywe profile historii, które nie są profilami historii już propagacyjnych.  
**Wynik 🔍:** pełna klasyfikacja profili resztkowych Wave pozostaje nieobliczona.

## 4. Scalar: stabilność nie wyznacza jednego języka historii

Dla progowego A2 w Scalar wcześniejsze twierdzenie daje zbiór punktów stałych pełnej rundy:

\[
\mathcal S_\epsilon=
\left\{
r:\forall i,j,\quad
|r_i-r_j|<\epsilon\Rightarrow r_i=r_j
\right\}.
\]

Są to konfiguracje, w których każda para współrzędnych jest albo równa, albo oddalona o co najmniej \(\epsilon\). Klasy równości wyznaczają stabilne profile/partycje.

Oznaczmy przez \(C_i\) lokalny akt aktualizujący współrzędną \(i\). Dla każdego \(r\in\mathcal S_\epsilon\) wszyscy sąsiedzi progowi współrzędnej \(i\) mają tę samą wartość co \(r_i\). Średnia używana przez \(C_i\) jest zatem równa \(r_i\), więc:

\[
\boxed{
C_i(r)=r
\quad
\forall r\in\mathcal S_\epsilon,\ \forall i.
}
\]

Każda stabilna konfiguracja jest więc punktowo nieruchoma pod każdym aktem, a nie tylko pod pełną rundą.

### 4.1. Statyczne profile Scalar tworzą kratę podziałów

Każda partycja zbioru indeksów \(A\) jest realizowalnym profilem stabilnym. Dla partycji \(\Pi=\{B_1,\ldots,B_m\}\) wybierzmy wartości \(z_1,\ldots,z_m\) tak, aby:

\[
|z_a-z_b|\ge\epsilon\qquad(a\ne b),
\]

i ustawmy \(x_i=z_a\) dla \(i\in B_a\). Wtedy równość współrzędnych wyznacza dokładnie partycję \(\Pi\), a konfiguracja należy do \(\mathcal S_\epsilon\).

Odwrotnie, każda konfiguracja z \(\mathcal S_\epsilon\) wyznacza partycję przez relację \(i\sim j\iff x_i=x_j\). Statyczne profile Scalar są zatem dokładnie elementami kraty podziałów \(\Pi_A\), a ich liczba jest równa liczbie Bella \(B_n\).

Dla \(n=4\):

\[
|\Pi_4|=B_4=15.
\]

To nie jest liczba profili resztkowych historii, lecz liczba możliwych stabilnych relacji równości. Rozróżnienie jest istotne: Centroid daje dla \(n=4\) 11 żywych profili przyszłości, Scalar daje 15 statycznych profili partycyjnych, ale same akty Scalar nie rozróżniają ich przez test utrzymania — wszystkie są punktowo nieruchome.

### 4.2. Kryterium samego utrzymania jest trywialne

Gdyby przyjąć:

\[
\mathcal L_S^{\mathrm{maint}}
=
\{w:\text{istnieje niebanalny }r\in\mathcal S_\epsilon
\text{ zachowany przez }w\},
\]

to — o ile istnieje przynajmniej jedna niebanalna stabilna partycja — otrzymujemy:

\[
\mathcal L_S^{\mathrm{maint}}=A^*.
\]

Każde słowo zachowuje każdą stabilną konfigurację. Wszystkie historie mają ten sam profil \(A^*\). Kryterium utrzymania gotowych domen nie różnicuje historii.

### 4.3. Kryterium osiągnięcia stabilności zależy od stanu początkowego

Można spróbować zdefiniować bardziej dynamiczny język, ale wtedy trzeba jawnie podać konfigurację początkową \(x\):

\[
\mathcal L_{S,x}
=
\{w\in A^*:T_w(x)\in\mathcal S_\epsilon\}.
\]

Ta definicja prowadzi do różnych języków dla różnych danych początkowych.

**Przypadek A — konfiguracja już stabilna.**  
Jeśli \(x\in\mathcal S_\epsilon\), każdy akt pozostawia x bez zmian. Stąd:

\[
\mathcal L_{S,x}=A^*.
\]

**Przypadek B — wszystkie wartości są w jednym klastrze progowym, lecz nie są równe.**  
Niech:

\[
\max_i x_i-\min_i x_i<\epsilon,
\qquad x\notin\langle\mathbf1\rangle.
\]

Graf progowy jest wtedy pełny. Każdy lokalny krok jest odpowiednim generatorem Centroidu \(M_i\), a wszystkie kolejne wartości pozostają w początkowym przedziale \([\min x,\max x]\). Graf pozostaje więc pełny po każdym kroku.

Ponadto:

\[
\det M_i=\frac1n\ne0.
\]

Każdy skończony produkt tych kroków jest odwracalny i zachowuje linię konsensusu. Nie może zatem przekształcić niekonsensusowego x w konsensus. A ponieważ wszystkie pary nadal są oddalone o mniej niż \(\epsilon\), warunek stabilności wymagałby, by wszystkie współrzędne były równe. Żadne skończone słowo nie prowadzi więc do \(\mathcal S_\epsilon\):

\[
\mathcal L_{S,x}=\varnothing.
\]

W tych dwóch dopuszczalnych reżimach Scalar daje odpowiednio język \(A^*\) lub język pusty. Profile resztkowe są w każdym przypadku trywialne, ale z przeciwnych przyczyn.

**Wniosek 🔍:** Scalar nie dostarcza jednego, niezależnego od konfiguracji początkowej języka dopuszczalnych historii. Statyczny zbiór punktów stałych wyznacza partycje, ale nie wybiera prawa przyszłych kontynuacji. Potrzebny jest dodatkowy warunek początkowy oraz rozstrzygnięcie, czy chodzi o osiągnięcie stabilności w skończonym czasie, czy o stabilność asymptotyczną.


### 4.4. Cała rodzina początkowych klastrów daje ten sam skrajny wynik

Powyższy argument rozszerza się na konfiguracje, których początkowy graf progowy jest rozłączną sumą klik. Niech bloki \(B_1,\ldots,B_m\) spełniają:

\[
\max_{i,j\in B_a}|x_i-x_j|<\epsilon,
\qquad
|x_i-x_j|\ge\epsilon\quad
(i\in B_a,\ j\in B_b,\ a\ne b).
\]

Każdy blok jest więc wewnętrznie pełnym klastrem, a bloki są od siebie oddzielone progiem.

Lokalna aktualizacja wewnątrz bloku jest średnią wszystkich współrzędnych tego bloku. Nowa wartość pozostaje w jego początkowym przedziale wypukłym. Średnica bloku nie rośnie, a odległości między blokami nie maleją poniżej progu. Podział na bloki pozostaje zatem niezmienny podczas dowolnej sekwencji lokalnych aktów.

Na bloku o liczności \(m_a\) każdy akt ma postać macierzy \(M_i^{(m_a)}\) o wyznaczniku \(1/m_a\) (dla bloku jednoelementowego akt jest identycznością). Każdy skończony produkt jest odwracalny i zachowuje linię stałą bloku. Nie może więc przekształcić niejednakowej konfiguracji bloku w wektor stały. Ponieważ wszystkie pary w obrębie bloku pozostają w odległości mniejszej niż \(\epsilon\), stabilność wymagałaby właśnie takiego wyrównania.

W konsekwencji, dla tej całej klasy początkowych konfiguracji:

\[
\mathcal L_{S,x}=
\begin{cases}
A^*,&\text{jeżeli każdy blok jest już stały},\\
\varnothing,&\text{jeżeli przynajmniej jeden blok nie ma stałej wartości}.
\end{cases}
\]

To wzmacnia wniosek: osiąganie stabilności w skończonej liczbie aktów nie daje bogatego, uniwersalnego automatu Scalar w obszarze konfiguracji, w którym graf progowy jest już rozłożony na oddzielone klastry. Dla bardziej ogólnych grafów progowych pozostaje osobny test.

### 4.5. Twierdzenie ogólne: stabilności nie da się osiągnąć w skończonej sekwencji

Późniejszy dowód zamyka wcześniejszą otwartą kwestię dla wszystkich grafów progowych, nie tylko dla jednej kliki czy rozłącznej sumy klik. Dla każdego lokalnego aktu:

\[
C_i^{-1}(\mathcal S_\epsilon)=\mathcal S_\epsilon.
\]

Jeśli po akcie \(C_i\) stan jest stabilny, to aktualizowana współrzędna musiała już mieć tę samą wartość co po aktualizacji. W przeciwnym razie stabilność końcowa wymusza, by wszyscy jej progowi sąsiedzi leżeli po tej samej stronie wartości końcowej, co uniemożliwia uzyskanie tej wartości przez ich średnią z aktualizowaną współrzędną.

Wobec tego dla dowolnego skończonego słowa \(w\):

\[
T_w(x)\in\mathcal S_\epsilon
\iff
x\in\mathcal S_\epsilon.
\]

Język skończonego osiągnięcia stabilności jest więc \(A^*\) dla stanu już stabilnego i pusty dla stanu niestabilnego. Nie ma żywego profilu nieakceptowanego w tym kryterium. Szczegóły dowodu: [raport o zakazie skończonego osiągnięcia stabilności A2](asterion-nr2-scalar-finite-time-stability-no-go-2026-11-23.md).

Oddzielnie pozostaje prawdziwe, że graf progowy nie jest wystarczającym stanem do przewidywania wszystkich przyszłych grafów relacji: aktualizacja zależy od ilościowych marginesów. Zob. [kontrprzykład dla mieszanego grafu progowego](asterion-nr2-scalar-threshold-graph-insufficient-mixed-2026-11-23.md).

## 5. Porównanie trzech korzeni

| Własność | Wave | Centroid | Scalar A2 |
|---|---|---|---|
| Kryterium akceptacji | niebanalny mod jednostkowy | niezerowy niezmiennik po słowie | osiągnięcie / utrzymanie stabilnej partycji |
| Domknięcie na fragmenty | nie | tak | tak dla skończonego testu stabilności (\(A^*\) albo \(\varnothing\)) |
| Profil nieakceptowany, ale żywy | tak — \(02T\) | nie | nie dla skończonej stabilizacji; asymptotyczne otwarte |
| Liczność profili | nieustalona | dokładna: \(\sum_{r=0}^{n-2}\binom nr\) | przy skończonej stabilizacji: \(A^*\) lub \(\varnothing\); asymptotycznie zależna od marginesów |
| Nośnik profilu | przyszłe kontynuacje słów | zbiory zachowanych indeksów / niezmienniki | graniczna partycja zależna od marginesów i harmonogramu |

### 5.1. Co jest wspólne?

Wszystkie trzy korzenie można osadzić w tym samym formalnym schemacie:

1. istnieje alfabet aktów;
2. dla danej historii określa się zbiór przyszłych kontynuacji spełniających test korzenia;
3. historie o identycznych zbiorach kontynuacji utożsamia się;
4. akty indukują częściowe przejścia na tych klasach;
5. kompozycja przejść jest silnie łączna.

To jest wspólna **konstrukcja behawioralna**, a nie jeszcze wspólna ontologia relacji.

### 5.2. Co jest różne?

- Wave mierzy przetrwanie relacyjnego modu w widmie produktu. Dopuszczalność może pojawić się dopiero po dalszej sekwencji.
- Centroid mierzy przetrwanie lewych obserwabli. Dla dodatnich słów profil jest dokładnie kodowany przez zbiór nieużytych generatorów.
- Scalar ma statyczne profile jako partycje równości, ale wszystkie stabilne konfiguracje są nieruchome pod każdym aktem. Co więcej, stabilności nie da się osiągnąć z niestabilnego stanu w skończonej liczbie aktów. Nietrywialne profile dynamiczne trzeba więc szukać w zachowaniu asymptotycznym, nie w skończonych słowach.

Nie ma podstaw, aby utożsamić:
\[
\text{mod jednostkowy}
\equiv
\text{zachowana obserwabla}
\equiv
\text{klasa równości}.
\]

Każde takie utożsamienie wymagałoby osobnego odwzorowania zachowującego działania i akceptację. Obecnie go nie mamy.

## 6. Konsekwencja dla N-R2 i P₀-Relacje

Uzyskany wynik nie jest porażką ogólnej konstrukcji profili resztkowych. Przeciwnie: konstrukcja pozostaje poprawna i łącznie działa niezależnie od factorialności języka.

Problem leży krok wcześniej. Każdy korzeń dostarcza innego, własnego testu:

\[
\mathrm{Prop}_{W}(w),\qquad
\mathrm{Inv}_{C}(w),\qquad
\mathrm{Stable}_{S}(T_w(x)).
\]

P₀-Relacje zapisuje \(R_{t+1}=F(R_t)\), ale operator \(F\) nie jest jeszcze zdefiniowany. Nie ma więc ogólnego testu \(\mathrm{Prop}_{P_0}(h)\), który odzyskiwałby trzy powyższe kryteria jako szczególne przypadki.

Najmocniejsza wspólna postać, którą można dziś obronić, brzmi:

\[
F_h^{P_0}
=
\{z:\mathrm{Prop}_{P_0}(hz)\}.
\]

Nie jest to jednak jeszcze prawo P₀ — to zapis miejsca, w którym prawo musi zostać podane. Sama równość przyszłych kontynuacji nie wyprowadza kryterium propagacyjności.

## 7. Werdykt

- **✅** Dla Centroidu język przetrwania niezerowego modu relacyjnego jest dokładnie językiem słów używających najwyżej \(n-2\) różnych generatorów.
- **✅** Żywy automat resztkowy Centroidu jest obciętą kratą podzbiorów; dla \(n=4\) ma 11 żywych profili, nie cztery.
- **✅** Wave i Centroid nie są izomorficzne jako automaty oznaczone językiem akceptacji: Wave ma nieakceptowaną, lecz żywą historię, Centroid jest factorialny.
- **✅** Każda stabilna konfiguracja Scalar A2 jest nieruchoma pod każdym lokalnym aktem.
- **✅** Kryterium samego utrzymania jakiejkolwiek niebanalnej stabilnej partycji daje w Scalar język \(A^*\).
- **✅** Dla kryterium osiągnięcia stabilności w skończonym czasie język Scalar zależy od konfiguracji początkowej; pokazano dokładne przypadki \(A^*\) i \(\varnothing\).
- **❌** Nie ma obecnie podstaw do utożsamienia profili Wave, Centroidu i Scalar jako tych samych obiektów matematycznych.
- **💡** Wszystkie trzy można traktować jako realizacje ogólnego automatu przyszłych kontynuacji, jeśli P₀ dostarczy niezależnego prawa określającego, które historie są żywe i propagacyjne.

## 8. Następny test

Nie należy teraz szukać liczby cztery w liczbie stanów automatu — wynik Centroidu pokazuje, że liczność zależy od przyjętego języka, a nie wynika z samej konstrukcji resztkowej.

Następny krok powinien dotyczyć nieskończonych harmonogramów A2: ustalić, czy trajektorie zbiegają do stabilnych partycji dla ogólnych konfiguracji, jak granica zależy od porządku aktualizacji i czy istnieje wspólna redukcja profili asymptotycznych Scalar–Centroid–Wave.

## 9. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
