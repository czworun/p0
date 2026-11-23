# P₀ — N‑R2: czy liczba cztery wynika z minimalnych operacji relacyjnych?

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; rekonstrukcja nośnika i liczby idempotentów bez etykiet węzłów.  
**Poza zakresem:** MVP-02, procedury laboratoryjne, pakiety replikacyjne.  
**Źródło korzeni:** `main`, commit `e4ac4a6d64c4a69983d7378bc5e82d961bb49f5c`.  
**Poprzedni krok:** `asterion-nr2-brandt-idempotenty-2026-11-23.md`.

## 0. Wynik w jednym zdaniu

**Sama kompozycja relacji nie wymusza czterech idempotentów.** Istnieją jednak dwie ścisłe, warunkowe drogi do liczby 4: (A) torsor grupy Kleina (C_2\times C_2), z którego wynika czteroelementowy nośnik i grupa symetrii (S_4); (B) równowaga wymiarów przestrzeni różnic i cykli w pełnym grafie (K_n), która ma jedyne nieosobliwe rozwiązanie (n=4). Żadna z tych dodatkowych zasad nie jest obecnie wyprowadzona z aksjomatów P₀. Werdykt N‑R2 pozostaje więc **otwarty**, ale wiadomo już dokładnie, jaki brak trzeba uzupełnić.

## 1. Pytanie i kryterium uczciwego rozwiązania

Nie wystarczy zbudować algebry, która ma cztery idempotenty. Trzeba wykazać, że:

1. liczba cztery wynika z praw operacji, a nie z deklaracji liczby elementów;
2. nie ma ukrytych etykiet ani uprzywilejowanego punktu;
3. pełna symetria odtworzonego K₄ nie jest skutkiem wyrzucenia informacji o niesymetrycznym ziarnie;
4. prawa operacji mają niezależne uzasadnienie w korzeniach P₀.

Punkt 4 jest rozstrzygający. Formalna prezentacja może być elegancka i poprawna, a mimo to jedynie przenieść założenie o liczbie cztery do innego symbolu.

## 2. Negatywny wynik: prawa Brandta nie wybierają (n=4)

Dla każdego (n\geq2) istnieje odwrotna półgrupa Brandta

\[
B_n^0=\{0\}\cup\{e_{ij}:1\leq i,j\leq n\},
\]

z mnożeniem

\[
e_{ij}e_{kl}=\begin{cases}
e_{il},&j=k,\\
0,&j\neq k.
\end{cases}
\]

Jej niezerowe idempotenty pierwotne to dokładnie (e_{11},\ldots,e_{nn}). Rekonstrukcja z poprzedniego raportu działa zatem dla **każdego (n)**:

\[
|V(B_n^0)|=n,\qquad
\operatorname{Aut}(B_n^0)\cong S_n.
\]

Ta sama reguła kompozycji dopuszcza więc (B_2^0,B_3^0,B_4^0,B_5^0,\ldots). Sam warunek „jedna relacja dla każdej uporządkowanej pary, z jednoznacznym odwrotnym elementem” nie ustala liczby obiektów.

Co więcej, nie jest nawet prawdą, że cztery to najmniejszy rozmiar niebanalnej struktury relacyjnej:

- (n=2): istnieje już relacja między dwoma różnymi obiektami;
- (n=3): istnieje już zamknięty cykl trójkątny.

Drugi punkt jest zgodny z P₀-Relacje §9.1–§9.2: dokument uznaje (N=3) za pierwszy rozmiar z nietrywialnym przejściem cyklicznym. Nie można zatem nazwać (K_4) minimalnym tylko dlatego, że ma cykle lub że da się na nim zbudować algebrę Brandta.

**Wniosek 1 — ✅.** Ogólny formalizm Brandta rekonstruuje nośnik, lecz nie wybiera jego liczności. Liczba cztery w (B_4^0) nadal pochodzi z wyboru wariantu (n=4).

## 3. Konstrukcja warunkowa A: torsor grupy Kleina

Istnieje krótsza prezentacja, w której cztery obiekty powstają z dwóch operacji, a nie z czterech zadanych idempotentów.

### 3.1. Dwie operacje wzajemnie odwrotne

Niech (a,b) będą dwiema niezależnymi operacjami spełniającymi

\[
a^2=b^2=1,\qquad ab=ba,
\]

przy czym (a\neq1), (b\neq1) oraz (a\neq b). Wtedy

\[
\Gamma=\langle a,b\rangle
=\{1,a,b,c\},\qquad c=ab,
\]

i

\[
\Gamma\cong C_2\times C_2.
\]

Cztery elementy nie zostały zadane osobno: wynikają z domknięcia dwóch niezależnych, komutujących inwolucji. Trzy elementy nieidentycznościowe (a,b,c) są również inwolucjami:

\[
a^2=b^2=c^2=1,\qquad ab=c,\quad bc=a,\quad ca=b.
\]

### 3.2. Nośnik jako torsor, bez wyróżnionego początku

Niech (X) będzie niepustym torsorem (Gamma), czyli zbiorem, na którym (Gamma) działa swobodnie i przechodnio. Wybór (x\in X) daje bijekcję

\[
\Gamma\longrightarrow X,\qquad g\longmapsto g\cdot x.
\]

Jest to bijekcja, więc

\[
\boxed{|X|=|\Gamma|=4.}
\]

Punkt (x) służy wyłącznie w dowodzie liczności; nie należy do struktury jako wyróżniony początek. Inny wybór daje równoważną prezentację torsora. Nie ma więc kanonicznego „pierwszego węzła”.

### 3.3. Odtworzenie K₄ i czterech idempotentów

Dla każdego (g\neq1) translacja (T_g:x\mapsto g\cdot x) jest inwolucją bez punktów stałych. Dzieli zatem cztery elementy (X) na dwie rozłączne pary. Trzy nieidentycznościowe elementy (Gamma) dają trzy doskonałe skojarzenia (perfect matchings).

Każda para różnych punktów (x,y\in X) wyznacza dokładnie jeden element (g\neq1), dla którego (T_g(x)=y). Trzy skojarzenia pokrywają zatem dokładnie sześć krawędzi:

\[
\boxed{G(X)\cong K_4,\qquad |V|=4,\quad |E|=6.}
\]

Teraz definiujemy grupoid par: dla każdej uporządkowanej pary (x,y\in X) istnieje dokładnie jeden strzał ([x,y]), a składanie ma postać

\[
[x,y]\,[u,v]=
\begin{cases}
[x,v],&y=u,\\
0,&y\neq u.
\end{cases}
\]

Lokalne jednostki

\[
p_x=[x,x]
\]

są idempotentami. Ponieważ (|X|=4), otrzymujemy dokładnie cztery idempotenty (p_x). Ponadto

\[
[x,y][y,x]=p_x,\qquad
[y,x][x,y]=p_y.
\]

W ten sposób liczba idempotentów jest twierdzeniem z rzędu grupy translacji, a nie osobnym warunkiem (|P|=4).

### 3.4. Symetria

Grupa automorfizmów afinicznych torsora nad (\mathbb F_2^2) ma postać

\[
\operatorname{AGL}(2,2)
=\mathbb F_2^2\rtimes\operatorname{GL}(2,2).
\]

Ponieważ

\[
|\operatorname{GL}(2,2)|
=(2^2-1)(2^2-2)=6,
\]

dostajemy

\[
|\operatorname{AGL}(2,2)|=4\cdot6=24.
\]

Działanie na czterech punktach jest wierne, zatem

\[
\boxed{\operatorname{AGL}(2,2)\cong S_4.}
\]

Trzy niezerowe translacje to dokładnie trzy podziały czterech punktów na przeciwległe pary. To daje algebraiczną, nieetykietowaną wersję kombinatoryki trzech par przeciwległych krawędzi z P₀-Axis §3.

**Twierdzenie 2 — ✅ warunkowo.** Jeżeli pierwotne operacje P₀ wyznaczają grupę (C_2\times C_2), a jej działanie na wzorcach relacyjnych jest swobodne i przechodnie, to nośnik ma dokładnie cztery elementy; jego grupoid par ma cztery lokalne idempotenty, grafem relacji jest (K_4), a grupa symetrii pełnego nośnika wynosi (S_4).

### 3.5. Co nadal jest założone

Konstrukcja nie jest jeszcze wyprowadzeniem z obecnych aksjomatów P₀. Wymaga czterech warunków:

1. istnieją dwie niezależne operacje inwolutywne;
2. operacje komutują;
3. nie zapadają się do tej samej operacji ani do identyczności;
4. działają na jednym niepustym wzorcu swobodnie i przechodnio.

Te warunki są krótsze niż postulat czterech węzłów, ale nie są obecnie twierdzeniami korzeni. Samo słowo „minimalny” nie uzasadnia ani komutowania, ani inwolutywności, ani działania regularnego.

Minimalność jest prawdziwa **wewnątrz tej klasy**: jedna niezależna inwolucja daje grupę (C_2) i torsor dwu-elementowy; dwie niezależne, komutujące inwolucje dają pierwszy przypadek z trzema niezerowymi translacjami i czterema punktami. Nie jest to jednak minimalność wśród wszystkich możliwych algebr relacyjnych.

## 4. Konstrukcja warunkowa B: równowaga wymiarów różnicy i defektu

Druga droga wynika bezpośrednio z geometrii pełnych relacji.

Niech relacyjny graf będzie pełnym grafem (K_n). Oznaczmy

\[
m=\binom n2.
\]

Dla spójnego grafu (K_n) operator incydencji (d:C^0\to C^1) ma rangę (n-1). Stąd:

\[
\dim\operatorname{Im}(d)=n-1
\]

i

\[
\dim\ker(d^*)=m-n+1
=\binom{n-1}{2}.
\]

Pierwszy wymiar liczy niezależne różnice węzłowe, drugi — niezależne defekty cykliczne. Jeśli zażądamy **równowagi liczby stopni swobody obu sektorów**, otrzymujemy:

\[
n-1=\binom{n-1}{2}.
\]

Dla (n\geq2):

\[
1=\frac{n-2}{2}
\quad\Longrightarrow\quad
\boxed{n=4.}
\]

Tabela pokazuje, że to nie jest przypadkowe trafienie:

| (n) | (dim\operatorname{Im}(d)) | (dim\ker(d^*)) |
|---:|---:|---:|
| 2 | 1 | 0 |
| 3 | 2 | 1 |
| 4 | 3 | 3 |
| 5 | 4 | 6 |
| 6 | 5 | 10 |

Dla pełnego grafu (K_n) liczba 4 jest zatem jedyną nieosobliwą licznością, przy której sektor różnic i sektor cykliczny mają równe niezerowe wymiary.

To dobrze tłumaczy szczególność K₄ w P₀-Centroid i P₀-Defect:

\[
\dim V_\rho=3=\dim V_{\rm cyc}.
\]

Jednak równość wymiarów **nie oznacza kanonicznej identyfikacji**. Dla (S_4):

\[
V_{\rm cyc}\cong V_\rho\otimes\mathrm{sign},
\]

więc (V_\rho) i (V_{\rm cyc}) są nieizomorficznymi reprezentacjami (S_4). Nie istnieje zwykły niezerowy (S_4)-splotnik między nimi. Dopiero po ograniczeniu do (A_4) i wyborze orientacji pojawia się izomorfizm przez operator Hodge’a.

**Twierdzenie 3 — ✅ warunkowo.** W klasie pełnych grafów (K_n) aksjomat równowagi (dim(	ext{różnice})=dim(	ext{cykle})) wymusza (n=4).

**Status zasady równowagi — 💡.** Korzenie pokazują zgodność wymiarów dla K₄, ale nie postulują, że dwa sektory muszą mieć tyle samo stopni swobody. P₀-Axis §16bis/§21 stawia pytanie, czy równość wymiarów (V_\rho) i (V_{\rm cyc}) jest zbiegiem wymiarowym, czy głębszą zgodnością. Nie wolno zmienić tego pytania w aksjomat bez osobnego uzasadnienia.

## 5. Kontrola pozornie krótszej drogi: dwa idempotentne generatory

Można próbować użyć prostszej półgrupy prostokątnej (R=I\times J) z mnożeniem

\[
(i,j)(k,l)=(i,l),\qquad |I|=|J|=2.
\]

Wtedy każdy element jest idempotentem, a dwa elementy (a=(0,0)), (b=(1,1)) generują:

\[
\{a,b,ab,ba\}=R,
\]

czyli cztery idempotenty z dwóch generatorów.

To nie jest rozwiązanie N‑R2:

- same równania (a^2=a), (b^2=b), (aba=a), (bab=b) nie wymuszają czterech elementów — spełnia je także dwuelementowa półgrupa lewostronna (xy=x);
- czteroelementowy przypadek prostokątny zakłada niekolapsujące się produkty (ab) i (ba), a więc dodatkową niezależność;
- algebra zachowuje dwa wyróżnione podziały (2+2) (wiersze i kolumny), a jej grupa automorfizmów wynosi (S_2\times S_2\cong V_4), nie (S_4).

Jej otoczka Karoubiego daje grupoid par na czterech obiektach, lecz pełne (S_4) pojawia się dopiero po zapomnieniu dwóch pierwotnych podziałów. To dobry przykład, jak konstrukcja może „wytworzyć” cztery obiekty, a jednocześnie przenieść ukrytą strukturę do generatorów. Nie przyjmuję jej jako rozwiązania P₀.

## 6. Konfrontacja z korzeniami P₀

### 6.1. P₀-Relacje

W §9.1–§9.2 (N=2) jest minimalną parą relacyjną, a (N=3) daje już zamknięty cykl trójkątny. §9.3 przechodzi do (N=4), ponieważ wtedy pojawia się konfiguracja tetraedryczna i operator (G_4=4I-J). Dokument nie wyprowadza jednak (N=4) jako minimalnej liczności całej relacyjności.

To ważne rozróżnienie: **minimalna relacja, minimalny cykl i szczególny układ zrównoważonych sektorów to trzy różne kryteria.** Pierwsze daje (N=2), drugie (N=3), a trzecie — warunkowo — (N=4).

### 6.2. Centroid

P₀-Centroid v5.2 podaje wynik ogólny:

\[
\dim\mathfrak g_n=n(n-1),\qquad
\mathfrak g_n\cong\mathfrak{gl}(n-1,\mathbb R)\ltimes\mathbb R^{n-1}.
\]

Dla (n=4) otrzymujemy (mathfrak{aff}(3)), ale twierdzenie jest prawdziwe dla całej rodziny (n\geq2). Algebra Centroidu sama nie wybiera (n=4).

### 6.3. Axis

P₀-Axis v0.3 w §1 deklaruje „obiekt pierwotny — K₄”. W §3 wyprowadza trzy pary przeciwległych krawędzi z kombinatoryki już przyjętego K₄, a następnie z nich trzy osie. Odwrócenie tego ciągu — trzy parowania (	o V_4	o) cztery punkty — jest matematycznie poprawne, lecz nie jest jeszcze niezależnym dowodem, że trzy parowania istniały przed K₄.

Axis dostarcza więc zgodności z konstrukcją torsorową, nie jej pierwotnego uzasadnienia.

### 6.4. Defect

Dla (K_n) przestrzeń cykli ma wymiar (inom{n-1}{2}), a dla (K_4) wynosi 3. W K₄ sektor cykliczny jest skręconą reprezentacją standardową. Zbieżność wymiarów jest rzeczywista; tożsamość sektorów pod pełnym (S_4) — fałszywa. Nie należy zastępować jednego stwierdzenia drugim.

## 7. Zestawienie wyników

| Teza | Status | Uzasadnienie |
|---|---|---|
| Sama kompozycja Brandta wymusza cztery obiekty | ❌ | Istnieją (B_n^0) dla każdego (n\geq2) |
| Cztery są minimalną niebanalną licznością relacyjną | ❌ | (N=2) ma relację, (N=3) ma cykl |
| Dwie niezależne komutujące inwolucje dają grupę czteroelementową | ✅ | (C_2\times C_2) |
| Nietrywialny torsor (C_2\times C_2) ma cztery punkty | ✅ | Działanie swobodne i przechodnie |
| Grupoid takiego torsora daje cztery lokalne idempotenty i (K_4) | ✅ | Jedna strzałka dla każdej pary |
| Symetria pełnego czteropunktowego nośnika to (S_4) | ✅ | (\operatorname{AGL}(2,2)\cong S_4) |
| P₀ wyprowadza obecnie dwie inwolucje i ich regularne działanie | 💡/otwarte | Brak takiego formalizmu w korzeniach |
| Równowaga wymiarów sektorów w (K_n) wymusza (n=4) | ✅ warunkowo | Jednoznaczne rozwiązanie równania wymiarów |
| P₀ postuluje tę równowagę jako zasadę | 💡 | W korzeniach jest pytaniem, nie aksjomatem |

## 8. Werdykt N‑R2

Mamy teraz dwa konkretne sposoby, w których **cztery staje się twierdzeniem**:

1. z działania torsorowego grupy (C_2\times C_2);
2. z równowagi wymiarowej przestrzeni różnic i przestrzeni cykli na pełnym grafie.

Oba dają dokładnie (K_4), a pierwszy zachowuje pełną symetrię (S_4) i nie wybiera punktu początkowego. Nie są jednak jeszcze wyprowadzeniami z samego P₀. Pierwszy przenosi problem do uzasadnienia dwóch komutujących inwolucji i regularności działania; drugi przenosi go do uzasadnienia zasady równości dwóch wymiarów.

Dlatego nie zmieniam statusu N‑R2 na ✅. **Cztery nie wynikają z samego pojęcia relacji ani z samej kompozycji.** Mamy dwa warunkowe twierdzenia, które precyzyjnie wskazują, jakiej dodatkowej struktury potrzeba.

## 9. Następny krok

Nie dodawać kolejnego postulatu tylko po to, by otrzymać (K_4). Następny test to sprawdzenie, czy w obecnym aparacie Centroid–Axis–Defect da się wskazać **kanoniczną parę niezależnych, komutujących inwolucji**, której definicja nie korzysta już z K₄.

W szczególności trzeba odróżnić:

- inwolucje rzeczywiście obecne w algebrze operacji;
- trzy podwójne transpozycje (V_4\triangleleft S_4), które pojawiają się dopiero po przyjęciu K₄;
- trzy pary przeciwległych krawędzi, które Axis wyprowadza dopiero z K₄.

Jeśli pierwsza para istnieje niezależnie, torsor daje nową drogę do emergencji nośnika. Jeśli pojawia się dopiero w drugim lub trzecim punkcie listy, mamy kolejne przepisanie K₄, nie jego wyprowadzenie.
