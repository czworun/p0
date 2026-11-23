# P₀ — N‑R2: rekonstrukcja K₄ z algebry relacji przez idempotenty

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; relacja jako obiekt algebraiczny bez zadanego zbioru węzłów.  
**Poza zakresem:** MVP-02, procedury laboratoryjne, pakiety replikacyjne.  
**Źródło korzeni:** \`main\`, commit \`e4ac4a6d64c4a69983d7378bc5e82d961bb49f5c\`.

## 0. Pytanie i wynik w jednym zdaniu

Czy można odzyskać węzły jako obiekty wtórne, nie podając wcześniej zbioru \(V\)?

**Wynik: częściowo tak.** Z abstrakcyjnej algebry relacji typu Brandta można kanonicznie odzyskać cztery węzły jako niezerowe idempotenty pierwotne, a relacje między nimi odtworzyć jako elementy o określonych źródłach i celach. Dla odpowiedniej algebry otrzymujemy dokładnie graf \(K_4\), a jej grupa automorfizmów wynosi \(S_4\).

Nie jest to jednak jeszcze wyprowadzenie czterech węzłów z „samej relacji bez żadnej struktury”. Algebra musi już mieć dokładnie cztery niezerowe idempotenty pierwotne. Konstrukcja usuwa zewnętrzny indeksowany nośnik \(V\), ale przenosi jego czterokrotność do własności algebry. Nie wybiera też pierwszego węzła. No-go pozostaje w mocy.

## 1. Odczyt korzenia: gdzie dokładnie znajduje się luka

P₀-Relacje v0.3 deklaruje w §1:

\[
\text{relacja}\longrightarrow\text{rozróżnienie}
\longrightarrow\text{stan węzłów}.
\]

Jednak w dalszych sekcjach występują trzy różne poziomy:

1. W §6 pojawia się \(R_{t+1}=F(R_t)\), ale \(F\) i typ danych \(R_t\) pozostają niezdefiniowane.
2. W §7 pełny stan zapisano jako \(\mathcal R_t=(V,E_t,X_t)\), a więc \(V\) jest już składnikiem wejścia.
3. W §8 relacje zapisano jako \(E_t\subseteq V\times V\), co jawnie zakłada nośnik węzłów.

§9.2bis (Test A) pokazuje, że konkretną dynamikę różnicową S13 da się przepisać bez wartości bezwzględnych \(x_i\), lecz sam dokument zastrzega, że trzy ponumerowane węzły były w tym teście dane. Test A zamyka część N‑R1, nie N‑R2.

W Axis kolejność \(K_4\to V_\rho\to\) pary przeciwległych krawędzi \(\to\) osie jest spójna **po przyjęciu \(K_4\)**. Nie dostarcza niezależnej konstrukcji nośnika przed \(K_4\).

Wniosek źródłowy: symbol \(\mathcal R\) z §1 nie ma jeszcze własnego typu algebraicznego. Samo nazwanie go „strukturą relacyjną” nie wystarcza do odzyskania węzłów.

## 2. Odrzucenie pozornych rozwiązań

Poniższe zapisy nie rozwiązują N‑R2:

- para \((a,b)\): elementy \(a,b\) są już obiektami;
- strzałka \(a\to b\): źródło i cel zakładają obiekty;
- krawędź incydentna z wierzchołkami: wierzchołki są już nośnikiem;
- macierz \(R_{ij}\) lub \(D_{ij}\): indeksy \(i,j\) zakładają zbiór indeksów;
- graf \((V,E)\): to jawne podanie \(V\);
- zwykły monoid z jedną globalną jedynką: jego jedyna wyróżniona tożsamość daje naturalnie jeden obiekt, a nie cztery.

Ostatni punkt jest ważny dla tropu monoidowego. Idempotenty dodatkowe mogą zawierać więcej struktury niż globalna jedynka, ale trzeba wykazać, że ich wyodrębnienie jest kanoniczne, a nie arbitralne.

## 3. Kandydat: relacje jako elementy odwrotnej półgrupy Brandta

Niech \(n\geq 2\). Rozważmy skończony zbiór

\[
B_n^0=\{0\}\cup\{e_{ij}:1\leq i,j\leq n\}
\]

z działaniem

\[
e_{ij}e_{kl}=
\begin{cases}
e_{il},&j=k,\\
0,&j\neq k,
\end{cases}
\qquad
0a=a0=0,
\]

oraz inwolucją

\[
e_{ij}^{*}=e_{ji},\qquad 0^*=0.
\]

Jest to odwrotna półgrupa Brandta z trywialnymi grupami lokalnymi. Kluczowe jest to, że pierwotnym zbiorem danych jest tu algebra elementów i ich mnożenie, nie osobno zadany graf wierzchołków i krawędzi.

Dla każdego \(a=e_{ij}\):

\[
aa^*=e_{ii},\qquad a^*a=e_{jj}.
\]

Oba wyniki są idempotentami. W odwrotnej półgrupie odwrotność jest jednoznaczna, więc \(a^*\) nie jest dodatkowym wyborem dla każdego elementu.

Interpretacja algebraiczna:

- \(aa^*\) jest idempotentem celu;
- \(a^*a\) jest idempotentem źródła;
- \(a\) jest relacją między tymi dwoma idempotentami;
- \(a^*\) jest relacją odwrotną.

To jest prezentacja „bez obiektów” w sensie, że nie wprowadzamy osobnego zbioru \(V\). Obiekty zostaną odzyskane jako szczególne elementy samej algebry.

## 4. Rekonstrukcja nośnika — twierdzenie

W odwrotnej półgrupie idempotenty tworzą częściowy porządek naturalny:

\[
p\leq q\iff pq=qp=p.
\]

Idempotent \(p\neq0\) nazywamy pierwotnym, gdy nie istnieje idempotent \(q\) z \(0<q<p\).

W \(B_n^0\) idempotenty to dokładnie:

\[
E(B_n^0)=\{0,e_{11},e_{22},\ldots,e_{nn}\}.
\]

Niezerowe idempotenty \(e_{ii}\) są parami ortogonalne i pierwotne. Stąd definiujemy bez zewnętrznego zbioru wierzchołków:

\[
V(B_n^0):=E(B_n^0)\setminus\{0\}.
\]

Relację między \(p,q\in V(B_n^0)\) definiujemy przez istnienie elementu \(a\neq0\), dla którego

\[
aa^*=p,\qquad a^*a=q.
\]

Dla każdej uporządkowanej pary \((e_{ii},e_{jj})\) istnieje dokładnie jeden taki element: \(e_{ij}\).

### Twierdzenie 1 — rekonstrukcja

Z algebraicznej struktury \(B_n^0\) można kanonicznie odzyskać:

1. \(n\) węzłów jako niezerowe idempotenty pierwotne;
2. dokładnie jeden skierowany morfizm/relację \(e_{ij}\) dla każdej uporządkowanej pary węzłów;
3. jedną relację nieukierunkowaną \(\{e_{ij},e_{ji}\}\) dla każdej pary różnych węzłów.

Wynikowy graf prosty jest pełnym grafem \(K_n\).

**Dowód.** Idempotenty zostały wyliczone wyżej. Każdy niezerowy element ma postać \(e_{ij}\), a jego dwa idempotenty nośne są odpowiednio \(e_{ii}\) i \(e_{jj}\). Reguła mnożenia daje dokładnie jeden element o danej uporządkowanej parze nośników. Po utożsamieniu pary elementów odwrotnych \(e_{ij}\sim e_{ji}\) otrzymujemy dokładnie jedną krawędź dla każdej pary różnych idempotentów. \(\square\)

## 5. Przypadek \(n=4\): dokładne odzyskanie K₄

Dla \(n=4\):

- liczba niezerowych idempotentów pierwotnych: \(4\);
- liczba niezerowych elementów relacyjnych: \(4^2=16\);
- z nich 4 są relacjami tożsamościowymi \(e_{ii}\);
- 12 to relacje skierowane \(e_{ij}\), \(i\neq j\);
- po utożsamieniu relacji odwrotnych pozostaje \(\binom42=6\) krawędzi.

Zatem:

\[
V(B_4^0)=\{e_{11},e_{22},e_{33},e_{44}\},
\]

a graf rekonstruowany z relacji ma:

\[
|V|=4,\qquad |E|=6,\qquad G(B_4^0)\cong K_4.
\]

Liczba 4 nie jest tu liczbą etykiet. Jest niezmiennikiem algebry: liczbą niezerowych idempotentów pierwotnych.

## 6. Automorfizmy i stabilizatory

Każdy automorfizm półgrupy zachowuje mnożenie, zero i idempotenty pierwotne. Musi więc indukować permutację \(\pi\) czterech idempotentów:

\[
e_{ii}\mapsto e_{\pi(i)\pi(i)}.
\]

Ponieważ dla każdej uporządkowanej pary nośników istnieje dokładnie jeden element o tych nośnikach, obraz \(e_{ij}\) jest wymuszony:

\[
e_{ij}\mapsto e_{\pi(i)\pi(j)}.
\]

Każda permutacja \(\pi\in S_4\) rzeczywiście zachowuje mnożenie. Nie ma więc dodatkowego swobodnego wyboru na elementach relacyjnych.

### Twierdzenie 2 — grupa automorfizmów

\[
\boxed{\operatorname{Aut}(B_4^0)\cong S_4.}
\]

Działanie na czterech odzyskanych węzłach jest przechodnie. Stabilizator jednego węzła jest izomorficzny z \(S_3\). Żaden węzeł nie jest ustalony przez całe \(S_4\).

W konsekwencji nie istnieje kanoniczny, ekwiwariantny selektor

\[
s:B_4^0\longrightarrow V(B_4^0)
\]

wybierający jeden „pierwszy” węzeł. Dla każdego automorfizmu \(\varphi\), który pozostawia algebraiczny obiekt niezmieniony, ekwiwariantność wymagałaby:

\[
s(B_4^0)=\varphi(s(B_4^0)).
\]

Ponieważ automorfizmy działają przechodnio na czterech idempotentach, żaden z nich nie jest stały pod wszystkimi automorfizmami. Sprzeczność.

To dokładnie ten sam typ przeszkody stabilizatorowej, który pojawił się w poprzednim audycie orientacji K₄.

## 7. Co ta konstrukcja rozwiązuje, a czego nie

### 7.1. Co rozwiązuje

**✅ Rekonstrukcja bez zewnętrznego \(V\).** Zbiór węzłów jest zdefiniowany wewnętrznie przez niezerowe idempotenty pierwotne.

**✅ Odtworzenie K₄.** Relacje między idempotentami dają dokładnie sześć nieukierunkowanych krawędzi.

**✅ Kanoniczność do izomorfizmu.** Zmiana nazw nie zmienia algebry; wszystkie prezentacje z etykietami są izomorficzne.

**✅ Pełna symetria.** Grupa automorfizmów jest dokładnie \(S_4\); nie wprowadziliśmy ukrytej orientacji ani wyróżnionego węzła.

### 7.2. Czego nie rozwiązuje

**❌ Nie wyprowadza liczby cztery.** Aksjomat, że algebra ma dokładnie cztery niezerowe idempotenty pierwotne, jest już czterokrotnością zapisaną w jej strukturze. Nie ma jeszcze powodu wynikającego z wcześniejszego P₀, dlaczego ma ich być cztery, a nie trzy, pięć lub dowolne \(n\).

**❌ Nie wyprowadza samej algebry.** W P₀-Relacje \(\mathcal R_t\) i \(F\) pozostają placeholderami. Nie ma reguły, która z nierozróżnionego P₀ wytwarza mnożenie Brandta ani wykazuje, że taki typ algebry jest konieczny.

**❌ Nie wybiera pierwszego węzła.** Odtworzenie zbioru czterech równoważnych węzłów nie jest wyborem jednego z nich. Stabilizator pozostaje \(S_4\).

**❌ Nie należy utożsamiać zera Brandta z \(P_0\).** Element \(0\) w półgrupie jest absorbującym wynikiem niekomponowalnego mnożenia. Nie jest automatycznie centroidowym stanem zerowej różnicy ani ontologicznym Punktem Zerowym P₀.

Werdykt: konstrukcja odzyskuje nośnik z algebry relacji, ale nie tworzy algebry z niczego.

## 8. Powiązanie z reprezentacją Centroidu

Po odzyskaniu czterech idempotentów można dopiero zlinearyzować ich zbiór. Przestrzeń formalnych amplitud węzłowych ma reprezentację permutacyjną:

\[
\mathbb R^{V(B_4^0)}
\cong \mathbf1\oplus V_\rho.
\]

Wektor równomierny

\[
p_0=\frac14\sum_{i=1}^4 e_{ii}
\]

jest niezmienniczy względem \(S_4\). Po ustaleniu sumy współrzędnych część standardowa \(V_\rho\) opisuje różnice między czterema odzyskanymi węzłami.

To daje naturalny most do Centroidu, ale tylko po linearyzacji i wyborze amplitud. Sam Brandtowski obiekt relacyjny nie dostarcza jeszcze metryki \(G_4=4I-J\), operatorów \(M_i\), ani dynamiki kompensacyjnej. Te struktury trzeba wyprowadzić osobno, nie dopisywać ich do algebry przez interpretację.

Co istotne, \(p_0\) jest średnią symetryczną całego zestawu idempotentów. Nie wskazuje żadnego konkretnego \(e_{ii}\). Kanał:

\[
\mathbf1\longrightarrow V_\rho
\]

nadal jest zerowy jako splotnik \(S_4\). Rekonstrukcja nośnika nie obala twierdzenia no-go o pierwszym zróżnicowaniu.

## 9. Dlaczego zwykły monoid nie wystarcza

Wskazówka „idempotenty monoidu jako obiekty” wymaga doprecyzowania.

Monoid ma jedną wyróżnioną globalną jedynkę \(1\). Jeśli zinterpretujemy wyłącznie tę jedynkę jako obiekt, dostajemy kategorię jednoobiektową. Aby odzyskać wiele obiektów, trzeba przejść do pełniejszej struktury idempotentów — np. rozszczepienia idempotentów/Karoubi envelope — i ustalić, które idempotenty są właściwymi obiektami.

W \(B_4^0\) nie ma globalnej jedynki będącej jednym z czterech idempotentów. Są cztery ortogonalne idempotenty pierwotne, a mnożenie elementów relacyjnych koduje ich zgodność kompozycji. To jest precyzyjniejszy kandydat niż samo „monoid ma idempotenty”.

Uwaga: dodanie formalnej globalnej jedynki do \(B_4^0\) nie usuwa czterech idempotentów pierwotnych, ale wprowadza nowy, większy idempotent. Nie wolno wówczas utożsamić globalnej jedynki z jednym z czterech rekonstruowanych węzłów.

## 10. Ostateczny status N‑R2

| Pytanie | Status | Wynik |
|---|---|---|
| Czy relacje mogą być opisane bez jawnego zbioru \(V\)? | ✅ warunkowo | Tak, jako elementy odwrotnej półgrupy z kompozycją |
| Czy węzły można odzyskać wewnętrznie? | ✅ warunkowo | Jako niezerowe idempotenty pierwotne |
| Czy można odzyskać dokładnie K₄? | ✅ warunkowo | Z \(B_4^0\), po utożsamieniu relacji odwrotnych |
| Czy rekonstrukcja jest niezależna od etykiet? | ✅ | Tak, do izomorfizmu |
| Jaki jest stabilizator? | ✅ | Pełny \(S_4\); stabilizator węzła \(S_3\) |
| Czy z samego obiektu relacyjnego wynika liczba 4? | ❌/otwarte | Nie; czterokrotność jest aksjomatem algebry |
| Czy algebra wyłania się z P₀ bez ziarna? | ❌/otwarte | Brak reguły generującej strukturę algebry |
| Czy powstaje kanoniczny pierwszy węzeł? | ❌ | Nie; działanie \(S_4\) jest przechodnie |

## 11. Konkluzja i dalszy problem

N‑R2 nie jest już całkowicie niedookreślone. Istnieje konkretny, matematycznie spójny sposób, w którym relacje są pierwotnymi elementami struktury algebraicznej, a węzły są rekonstruowane jako idempotenty ich kompozycji. Dla odwrotnej półgrupy Brandta \(B_4^0\) odzyskujemy dokładnie K₄ i pełną symetrię \(S_4\).

Jednak to rozwiązanie ma ograniczony zakres: **wyjaśnia, jak węzły można odzyskać z relacji, lecz nie wyjaśnia, skąd bierze się algebra relacji ani dlaczego ma cztery idempotenty pierwotne.** Jest to formalna realizacja zasady „relacja przed obiektem” w sensie reprezentacji, nie dowód ontologicznego narodzenia czterech obiektów z absolutnie niezróżnicowanego P₀.

Najważniejszy następny test nie powinien polegać na dopisaniu kolejnej struktury. Trzeba sprawdzić, czy z minimalnego, nieetykietowanego układu operacji relacyjnych da się wymusić istnienie niezerowych idempotentów pierwotnych i czy liczba tych idempotentów może być twierdzeniem, a nie parametrem. Dopiero wtedy będzie można mówić o rzeczywistym wyprowadzeniu \(V_t=\mathcal V(\mathcal R_t)\).

**Werdykt końcowy:** 🔍 N‑R2 częściowo skonstruowane; geneza algebry i liczby czterech obiektów pozostają otwarte. No-go dla wyboru pierwszego węzła nie zostało naruszone.
