# N-R2: dziedziczenie działania S4 przez profile i niejednoznaczność nośnika

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; audyt N-R2. Bez ingerencji w MVP-02.  
**Punkt wyjścia:** P₀-Relacje v0.3 §§0–9; P₀-Centroid (rodzina \(M_i\)); P₀-Defect v0.8 §§5–7; wcześniejsze raporty Asteriona o no-go, profilach półkratowych i geometrii afinicznej.  
**Status:** twierdzenia o działaniu grupy ✅; utożsamienie działania Centroidu z działaniem na profilach N-R2 ❌ jako wniosek z obecnych danych; dokładna liczba profili N-R2 pozostaje 💡/otwarta.

## 1. Pytanie

Czy pełna symetria \(S_4\), znana z Centroidu, może przejść na profile wyprowadzone z pierwotnej relacji? Jeśli tak, czy wymusza cztery profile?

Trzeba oddzielić trzy twierdzenia:

1. \(S_4\) działa na już zadanej rodzinie czterech operatorów Centroidu.
2. Działanie \(S_4\) przechodzi na klasy profili wyłącznie wtedy, gdy równoważność definiująca profile jest \(S_4\)-niezmiennicza.
3. Nawet wierne działanie \(S_4\) na profilach nie wymusza, że profili jest dokładnie cztery.

Pierwsze jest własnością istniejącej konstrukcji K₄/Centroid. Drugie jest warunkiem formalnym. Trzecie obala skrót „S₄ ⇒ dokładnie cztery profile”.

## 2. Lemat dziedziczenia działania na iloraz

Niech grupa \(G\) działa na zbiorze \(X\). Niech \(\sim\) będzie relacją równoważności na \(X\). Działanie indukuje dobrze określone działanie na ilorazie \(X/{\sim}\) wtedy i tylko wtedy, gdy

\[
x\sim y\implies gx\sim gy
\qquad(\forall g\in G).
\]

**Dowód.** Kandydatem na działanie jest \(g[x]=[gx]\). Jest ono niezależne od reprezentanta dokładnie wtedy, gdy równoważność jest zachowywana przez każde \(g\). ∎

W N-R2 nie wystarczy wskazać automorfizmów Centroidu. Trzeba zdefiniować profile jako klasy pewnej równoważności operacyjnej i dowieść, że każdy automorfizm relacyjnej struktury zachowuje tę równoważność.

## 3. Szczególny wynik dla czterech generatorów Centroidu

Niech

\[
M=\{M_0,M_1,M_2,M_3\}
\]

będzie naturalnym czteroelementowym zbiorem generatorów, na którym \(S_4\) działa przez \(\sigma(M_i)=M_{\sigma(i)}\).

Naturalne działanie \(S_4\) na czterech elementach jest 2-przechodnie. Stąd każda \(S_4\)-niezmiennicza relacja równoważności \(\sim\) na \(M\) jest jedną z dwóch:

- równość: cztery klasy;
- relacja uniwersalna: jedna klasa.

**Dowód.** Jeżeli istnieje para różnych elementów \(M_i\sim M_j\), to dla dowolnej pary różnych indeksów \(k\ne l\) istnieje \(\sigma\in S_4\) przenosząca uporządkowaną parę \((i,j)\) na \((k,l)\). Niezmienniczość daje \(M_k\sim M_l\). Wszystkie elementy należą więc do jednej klasy. Jeżeli takiej pary nie ma, klasy są singletonami. ∎

To daje uczciwy, ale wąski wynik:

\[
|M/{\sim}|\in\{1,4\}.
\]

Nie powstaje iloraz 2- ani 3-elementowy.

**Granica dowodu:** zbiór \(M\) ma już cztery elementy. Wynik nie wyprowadza rodziny \(M\) z relacji pierwotnej; tylko mówi, co stanie się z jej ilorazem, jeśli równoważność profili jest niezmiennicza. Nie wolno przedstawiać tego jako rozwiązania N-R2.

## 4. Wierne działanie S4 daje co najmniej cztery profile, nie dokładnie cztery

Niech \(P\) będzie skończonym zbiorem profili, a działanie \(S_4\curvearrowright P\) będzie wierne. Wtedy

\[
S_4\hookrightarrow \operatorname{Sym}(P).
\]

Jeżeli \(|P|\le 3\), to \(|\operatorname{Sym}(P)|\le 6<24=|S_4|\), więc takie włożenie jest niemożliwe. Zatem

\[
\boxed{|P|\ge4.}
\]

Granica jest osiągana przez naturalne działanie na czterech wierzchołkach. Ale nie ma tu górnego ograniczenia: działanie wierne może mieć większy nośnik.

### 4.1. Kontrmodel pięciu profili

Weźmy \(P=\{1,2,3,4,*\}\), na którym \(S_4\) permutuje pierwsze cztery profile i ustala \(*\). Działanie jest wierne, ale profili jest pięć. Można je zrealizować jako pięć punktów afinicznych: cztery wierzchołki tetraedru oraz odrębny punkt stały, np. jego barycentrum.

### 4.2. Kontrmodel sześciu profili zgodny z geometrią K₄

Niech profilami będą nieuporządkowane pary indeksów:

\[
P_2=\binom{\{0,1,2,3\}}2
=\{01,02,03,12,13,23\}.
\]

\(S_4\) działa na nich przez permutowanie indeksów. Działanie jest przechodnie i wierne: jedyną permutacją, która zachowuje wszystkie sześć par osobno, jest identyczność.

W geometrii Centroidu/Axis profile te mają naturalne reprezentanty — środki krawędzi:

\[
q_{ij}=\tfrac12(v_i+v_j)
=\tfrac12(e_i+e_j)-p_0.
\]

Tworzą one sześć wierzchołków regularnego ośmiościanu w \(V_\rho\), a więc ich otoczka afiniczna ma wymiar 3. Jest to wierne, przechodnie działanie \(S_4\) na **sześciu** naturalnych obiektach relacyjnych, nie na czterech.

To nie dowodzi, że N-R2 wyprowadza sześć profili. Dowodzi natomiast, że sam wybór pełnej grupy \(S_4\), nawet wraz z jej wiernym działaniem, nie rozstrzyga, czy profilem ma być wierzchołek, krawędź czy inny typ kontekstu.

## 5. Co dokładnie wynika z K₄, a czego nie

Obecna matematyka K₄ zawiera co najmniej dwie naturalne rodziny obiektów:

| Kandydat na profil | Liczność | Działanie S₄ | Geometria |
|---|---:|---|---|
| Wierzchołki | 4 | naturalne, wierne, przechodnie | tetraedr; wymiar afiniczny 3 |
| Krawędzie / ich środki | 6 | wierne, przechodnie | ośmiościan; wymiar afiniczny 3 |

W obu przypadkach grupa jest ta sama. Inny jest typ obiektu uznany za profil.

Z tego powodu nie wystarczy postulat „profile zachowują pełną symetrię K₄”. N-R2 musi podać **wewnętrzne kryterium wyboru poziomu obiektów**. Przykładowo: czy profil jest minimalnym stabilnym wzorcem, klasą nierozróżnialności operatorów, klasą kontekstów, czy atomem określonej algebry? Każda z tych definicji może dać inny nośnik.

## 6. Możliwy most przez minimalny wierny nośnik

Dla grupy \(G\) definiuje się minimalny stopień wiernego działania permutacyjnego:

\[
\mu(G)=\min\{|X|:G\hookrightarrow\operatorname{Sym}(X)\}.
\]

Dla \(S_4\):

- dolna granica: \(\mu(S_4)\ge4\), bo \(|S_3|=6<24\);
- górna granica: naturalne działanie na czterech elementach jest wierne, więc \(\mu(S_4)\le4\).

Zatem

\[
\boxed{\mu(S_4)=4.}
\]

To jest realny kandydat na twierdzenie „cztery” — ale tylko po przyjęciu warunku: profile są minimalnym wiernym nośnikiem działania pełnej grupy automorfizmów relacji.

Wtedy cztery nie są arbitralnym parametrem; są minimalnym stopniem reprezentacji permutacyjnej już wyprowadzonej grupy.

Koszt tego mostu jest istotny:
1. trzeba najpierw wyprowadzić \(\operatorname{Aut}(\mathcal R)\cong S_4\) z relacji, a nie z rodziny czterech generatorów;
2. trzeba uzasadnić, dlaczego profile mają być minimalnym wiernym nośnikiem, a nie dowolnym wiernym nośnikiem albo zbiorem wszystkich stabilnych kontekstów;
3. trzeba wykazać, że minimalny nośnik ma interpretację wewnętrzną w samej relacji, a nie jest zewnętrzną optymalizacją modelu.

Bez tych trzech kroków \(\mu(S_4)=4\) jest twierdzeniem grupowym bez mostu ontologicznego do N-R2.

## 7. Kontrmodel ogólnej algebry relacyjnej nadal obowiązuje

Poprzedni raport o półkratach pokazał, że dla

\[
S_n=\{0,\ldots,n-1\},\qquad x\wedge y=\min(x,y),
\]

klasy Greena \(\mathcal J\), zdefiniowane przez \(SxS=SyS\), są singletonami. Można więc uzyskać dowolną skończoną liczbę profili, nie tylko cztery.

Nowy wynik o \(S_4\) nie usuwa tego kontrmodelu, ponieważ nie wykazano, że automorfizmy tych ogólnych algebr muszą tworzyć \(S_4\). Z kolei sama obecność \(S_4\) w Centroidzie nie narzuca tej grupy półkracie N-R2.

Obecne dwa fakty są niezależne:

- ogólne operacje relacyjne nie wymuszają liczby cztery;
- zadana rodzina czterech generatorów Centroidu ma naturalną symetrię \(S_4\).

Brakuje twierdzenia, które łączyłoby je bez zakładania czteroelementowego nośnika.

## 8. Kontrola korzeni i statusu Samoodniesienia

P₀-Relacje v0.3 nadal jawnie stawia N-R2: zapis \(\mathcal R_t=(V,E_t,X_t)\) przyjmuje \(V\), a wariant \(V_t=\mathcal V(\mathcal R_t)\) pozostaje niezbudowany.

P₀-Defect v0.8 potwierdza dwa różne poziomy istniejącej struktury K₄: Centroid pracuje na poziomie wierzchołków, Defect na \(C^1(K_4)\), czyli sześciu krawędziach. Jego §6 identyfikuje sześć kierunków ośmiościanu i trzy osie \(V_4\). To potwierdza, że wybór czterech profili nie jest jedyną naturalną klasyfikacją obiektów w rdzeniu K₄.

PILLARS-TABLE-1 odnotowuje decyzję autora: P₀-Samoodniesienie nie jest osobnym filarem, tylko zapisem samoodniesienia. Nie traktuję go więc jako brakującego filaru ani nie rekonstruuję nieobecnego pliku. N-R2 pozostaje problemem P₀-Relacje.

## 9. Werdykt

- **✅** Działanie grupy przechodzi na iloraz klas wtedy i tylko wtedy, gdy równoważność jest niezmiennicza.
- **✅** Dla naturalnego działania \(S_4\) na czterech generatorach każda niezmiennicza równoważność daje 1 albo 4 klasy.
- **✅** Każde skończone wierne działanie \(S_4\) wymaga co najmniej czterech profili.
- **✅** Minimalny stopień wiernego działania \(S_4\) wynosi 4.
- **✅** Krawędzie K₄ tworzą drugi naturalny, sześciopunktowy, wierny i przechodni nośnik działania \(S_4\); ich reprezentacja geometryczna jest ośmiościanem w wymiarze 3.
- **❌** Z samego \(S_4\) nie wynika, że wszystkie profile muszą być dokładnie cztery.
- **❌** \(\operatorname{Aut}(\mathfrak g_4;\{M_i\})\cong S_4\) nie jest jeszcze dowodem, że N-R2 wyprowadziło cztery profile.
- **💡** Minimalny wierny nośnik może być mostem „S₄ ⇒ 4”, ale wymaga niezależnego wyprowadzenia S₄ i uzasadnienia minimalności profili.
- **💡** Najważniejsza luka N-R2 przesuwa się z pytania „skąd cztery?” na pytanie „jaki wewnętrzny test wybiera właściwy typ profilu?”.

**Wniosek operacyjny dla kolejnego audytu:** nie projektować jeszcze aksjomatu wymuszającego 4. Najpierw porównać trzy definicje profilu na tym samym obiekcie relacyjnym: (A) klasy operatorów, (B) klasy kontekstów / relacja Greena, (C) minimalny wierny nośnik automorfizmów. Sprawdzić, czy którakolwiek z nich wybiera cztery bez wstawienia K₄ lub \(S_4\) do definicji. Modele z 2, 3, 5 i 6 profilami muszą pozostać testami rozstrzygającymi.

## 10. Integralność repo

Raport zapisano wyłącznie na gałęzi audytowej audit/asterion-continuation-2026-11-20. Nie zmieniano main, nie wykonano merge ani rebase. Stan porównania sprawdzony przed zapisem: main i gałąź audytowa rozbieżne, 38 commitów wyłącznie po stronie audytu i 20 wyłącznie po stronie main. MVP-02 pozostaje poza zakresem.
