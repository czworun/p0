# P₀ — No-go dla wewnętrznego narodzin pierwszej różnicy z symetrycznego K₄

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; warunki konieczne dla powstania pierwszej asymetrii z dokładnie symetrycznego stanu.  
**Poza zakresem:** MVP-02, procedury laboratoryjne, pakiety replikacyjne.

## 0. Źródła i zakres odczytu

Korzenie analizowane na \`main\`, commit:
\`e4ac4a6d64c4a69983d7378bc5e82d961bb49f5c\`.

Odczytano Centroid v5.2 (lista zmian i konsekwencje algebraiczne), Defect v0.8 §12B–12G, Flow v0.5.3 §3.5–3.8 i §5.5–5.7, Wave v0.6.1 §1, Net v0.6.1 §18–24, Memory v0.3.7 §6–8 oraz Relacje v0.3 §1–6. Raport zapisano na gałęzi audytowej; \`main\` pozostaje nietknięty.

## 1. Twierdzenie ogólne: symetryczny stan nie opuszcza orbity symetrycznej

Niech grupa \(G\) działa liniowo na przestrzeni stanów \(X\). Stan \(x_0\) jest \(G\)-symetryczny, gdy \(gx_0=x_0\) dla każdego \(g\in G\). Niech aktualizacja \(F:X\to X\) będzie deterministyczna i ekwiwariantna:
\[
F(gx)=gF(x).
\]

Wtedy:
\[
gx_t=x_t \quad\Longrightarrow\quad
gF(x_t)=F(gx_t)=F(x_t).
\]
Zatem \(x_{t+1}\) pozostaje \(G\)-symetryczny. Indukcyjnie każda iteracja pozostaje w przestrzeni punktów stałych:
\[
x_t\in\operatorname{Fix}_X(G).
\]

To samo dotyczy autonomicznego równania różniczkowego \(\dot x=f(x)\), jeżeli pole wektorowe jest ekwiwariantne i rozwiązanie początkowe jest jednoznaczne. W punkcie symetrycznym \(x\), \(f(x)\) musi być wektorem stałym pod stabilizatorem \(x\). Przy jednoznaczności przepływu orbita punktu symetrycznego nie może opuścić podprzestrzeni punktów stałych.

**Twierdzenie 1 — ✅.** Żadna deterministyczna, ekwiwariantna i dobrze postawiona dynamika nie wytworzy asymetrii z dokładnie symetrycznego stanu początkowego. Może wzmacniać asymetrię już obecną, ale nie wybierze jednej z równoważnych gałęzi sama z siebie.

To nie jest ograniczenie liniowości. Obowiązuje dla dowolnej ciągłej, gładkiej, wielomianowej lub nieliniowej aktualizacji ekwiwariantnej.

## 2. Zastosowanie do pełnego stanu P₀ na K₄

### 2.1. Warstwa wierzchołkowa

Działanie \(S_4\) na \(\mathbb R^4\) rozkłada się:
\[
\mathbb R^4=\mathbf1\oplus V_\rho,\qquad
V_\rho=\mathbf1^\perp.
\]
Przestrzeń punktów stałych to:
\[
\operatorname{Fix}_{\mathbb R^4}(S_4)=\operatorname{span}\{\mathbf1\}.
\]
Po ustaleniu sumy współrzędnych (simpleks centroidowy) pozostaje dokładnie jeden stan symetryczny:
\[
p_0=\frac14\mathbf1.
\]
W reprezentancie zero-mean \(P_0=0\in V_\rho\).

Każdy operator centroidowy \(M_i\) zachowuje \(p_0\). Rodzina \(\{M_i\}\) jest permutowana przez \(S_4\), a nie każdy operator z osobna jest \(S_4\)-niezmienniczy. Wybór konkretnego \(M_i\) jest więc wyborem konkretnego indeksu, czyli złamaniem symetrii.

### 2.2. Warstwa krawędziowa Defect

Dla zorientowanych krawędzi:
\[
C^1(K_4)\cong V_\rho\oplus V_{\rm cyc},
\qquad
V_{\rm cyc}\cong V_\rho\otimes\operatorname{sign}.
\]
Obie składowe są nieizomorficznymi, nietrywialnymi reprezentacjami \(S_4\). W szczególności:
\[
\operatorname{Fix}_{C^1(K_4)}(S_4)=\{0\}.
\]
Projektor \(P_{\rm cyc}\) jest ekwiwariantny; rozdziela sektory, ale nie tworzy składowej cyklicznej z symetrycznego zera:
\[
P_{\rm cyc}(0)=0.
\]

Jeżeli pełny stan relacyjny jest parą \((x,D)\in V_\rho\oplus C^1(K_4)\), to jego \(S_4\)-stały stan w sektorach o zerowej średniej jest tylko \((0,0)\). Dodanie kilku zmiennych skalarnych (reprezentacji trywialnych) może pozwolić na ewolucję amplitudy skalarnej, ale nie daje ekwiwariantnego kanału ze skalaru do \(V_\rho\) lub \(V_{\rm cyc}\):
\[
\operatorname{Hom}_{S_4}(\mathbf1,V_\rho)
=
\operatorname{Hom}_{S_4}(\mathbf1,V_{\rm cyc})
=0.
\]

### 2.3. Uwaga o nieukierunkowanej przestrzeni krawędzi

Dla \(U=\mathbb R^6\) na nieukierunkowanych krawędziach istnieje jednowymiarowy sektor trywialny — wektor stały na wszystkich sześciu krawędziach. Jest to symetryczna amplituda krawędziowa, nie różnicowanie wierzchołków. Nie istnieje \(S_4\)-ekwiwariantna mapa z tego sektora do \(V_\rho\), bo \(\operatorname{Hom}_{S_4}(\mathbf1,V_\rho)=0\).

Zatem nawet dopuszczenie symetrycznej „energii krawędzi” nie rozwiązuje selekcji pierwszego wierzchołka ani orientacji.

## 3. Test istniejących mechanizmów korzeni

### 3.1. Centroid: symetryzacja generatorów nie wybiera kierunku

Na \(V_\rho\) dla \(K_4\) operator centroidowy ma postać:
\[
(\bar M_i x)_i=\frac{x_i}{4},\qquad
(\bar M_i x)_j=x_j+\frac{x_i}{4}\quad(j\ne i).
\]
Sumując cztery operatory, dla każdej współrzędnej \(j\):
\[
\sum_{i=0}^3(\bar M_i x)_j
=\frac{x_j}{4}+3x_j+\frac14\sum_{i\ne j}x_i
=3x_j,
\]
ponieważ \(\sum_i x_i=0\). Stąd:
\[
\boxed{\frac14\sum_{i=0}^3\bar M_i=\frac34 I_{V_\rho}.}
\]

Symetryczne użycie całej rodziny generatorów daje więc izotropową kontrakcję, a nie wyróżniony kierunek. To zgodne z lematem Schura: każda liniowa mapa komutująca z nieredukowalnym \(V_\rho\) jest skalarem.

Analogicznie, średnia po wszystkich 24 kolejnościach pełnej rundy jest \(S_4\)-ekwiwariantna, więc na \(V_\rho\) musi być skalarem. Konkretna runda \(R_{\rm id}\) może mieć fazę i kierunek, ale ustalona kolejność jest już dodatkową informacją. Rodzina \(R_\sigma=P_\sigma R_{\rm id}P_\sigma^{-1}\) nie wybiera sama jednej \(\sigma\).

**Wniosek 3.1 — ✅.** Symetryzacja operatorów Centroidu może kontraktować stan, ale nie może wytworzyć ani wybrać asymetrii z \(P_0\).

### 3.2. Wave: słowo niesie kolejność, ale nie wybiera pierwszej litery

Wave definiuje słowo nad alfabetem:
\[
\Sigma=\{M_0,M_1,M_2,M_3,T\}.
\]
Operator jest interpretacją zadanego słowa. \(S_4\) permutuje litery \(M_i\) i sprzęga \(T\) z jego obrazami. Żaden pojedynczy symbol alfabetu nie jest stały pod całym \(S_4\).

Wybór pierwszej litery wymaga zatem albo:
- zewnętrznego harmonogramu,
- stanu, który już wyróżnia orbitę/stabilizator,
- losowania (pojedyncza realizacja łamie symetrię),
- albo niejednoznacznej reguły przejścia z jawnym wyborem gałęzi.

Słowo może nieść orientację historii, ale nie jest samoistnym generatorem swojej pierwszej litery.

**Wniosek 3.2 — ✅.** Obecny formalizm Wave jest algebrą interpretacji słów, a nie domkniętym automatem wybierającym pierwszy symbol z symetrycznego stanu.

### 3.3. Defect i Flow: kanały downstream

Defect §12B dowodzi:
\[
\operatorname{Hom}_{S_4}(\operatorname{Sym}^2V_{\rm cyc},V_{\rm cyc})=0.
\]
Dopiero po ograniczeniu symetrii do odpowiedniej podgrupy (np. \(S_3\)) następuje rozszczepienie \(V_{\rm cyc}|_{S_3}=A\oplus B\), w którym może istnieć kanał:
\[
T_b:B\otimes B\to B.
\]
To kanał amplifikacji już istniejącego sektora \(B\), a nie generator jego pierwszego niezerowego elementu.

Flow §3.5 definiuje dla K₄:
\[
\Phi(x)(y)=
(x_2y_3+x_3y_2,\;
 x_3y_1+x_1y_3,\;
 x_1y_2+x_2y_1).
\]
Jest to sprzężenie dwóch wejść. Dla \(x=0\) lub \(y=0\) wynik jest zerowy. Mechanizm VII wymaga więc wcześniejszego niezerowego stanu w obu odpowiednich sektorach. Ponadto Flow §5.7.4 stwierdza, że wzrost przez samoodziaływanie jest liniowy w asymptotyce, a analiza §5.5–5.6 nie wykazuje synergii z \(T_a\).

**Wniosek 3.3 — ✅.** \(T_b\) i \(\Phi\) mogą opisywać propagację/wzmacnianie po pojawieniu się asymetrii. Nie rozwiązują jej genezy.

### 3.4. Net/Memory: deterministyczna rozbieżność ma warunek początkowy i most

Net M16 pokazuje deterministyczną rozbieżność atraktorów, ale:
- używa \(D_0\sim\mathcal N(0,2)\), a więc niezerowego, losowanego warunku początkowego;
- zamraża \(D^{\rm cyc}\), co jest decyzją konstrukcyjną;
- wybiera most A lub B, którego kanoniczność pozostaje 💡;
- wynik silnie zależy od wsadowego/sekwencyjnego trybu \(K_2\).

M16 nie jest zatem mechanizmem tworzenia pierwszej różnicy z dokładnego \(P_0\). Jest przykładem deterministycznego przetwarzania różnic już obecnych w \(D_0\), przy dodatkowych wyborach konstrukcyjnych.

Memory poprawnie rozdziela stan końcowy, trajektorię i \(\omega\)-granicę. Pamięć operatorowa może zachować informację o dopuszczalnych przyszłych zachowaniach, ale sama nie wybiera konkretnej realizacji z symetrycznego zbioru.

## 4. Najgłębszy problem: Relacje nie wyprowadza jeszcze zbioru węzłów

P₀-Relacje §1 deklaruje kierunek:
\[
\text{relacja}\to\text{rozróżnienie}\to\text{stan węzłów}.
\]
Jednak §3 definiuje:
\[
D_{ij}=x_i-x_j,
\]
czyli zakłada już istnienie \(x_i,x_j\). Dokument sam rejestruje napięcie N-R1.

Jeszcze ważniejsze jest N-R2: zbiór węzłów \(V\) jest w obecnym formalizmie dany z góry. Alternatywa:
\[
V_t=\mathcal V(\mathcal R_t),
\]
czyli węzły jako stabilne wzorce relacji, pozostaje niezbudowana.

To znaczy, że K₄ nie jest jeszcze wyprowadzony z pierwotnego zbioru relacji. K₄ jest pierwszym skończonym laboratorium, ale jego cztery wierzchołki są wejściem modelu. Zanim pytamy, jak relacja wybiera pierwszy wierzchołek, trzeba formalnie określić, jak relacje w ogóle wyznaczają nośnik, na którym wierzchołki mają się pojawić.

**Wniosek 4.1 — 🔍/otwarte.** W korzeniu Relacje istnieje jawna luka konstrukcyjna: nie ma jeszcze mapy, która z pierwotnego obiektu relacyjnego rekonstruuje zbiór węzłów bez uprzedniego ich założenia.

## 5. Co mogłoby obejść twierdzenie — i jaka byłaby cena

Twierdzenie 1 ma precyzyjne założenia. Są cztery możliwe wyjścia, ale każde zmienia treść modelu:

1. **Niejednoznaczna dynamika.** Np. nie-Lipschitzowskie równanie może mieć wiele rozwiązań z tego samego symetrycznego stanu. Równania dopuszczają wtedy asymetryczne gałęzie, lecz nie wybierają jednej; wybór gałęzi pozostaje dodatkową regułą.
2. **Losowość.** Pojedyncza realizacja może wybrać asymetrię, a rozkład zachować symetrię. To selekcja stochastyczna, nie deterministyczne wyłonienie.
3. **Ukryty stan niesymetryczny.** Wtedy model nie startuje naprawdę z pełnego \(P_0\); asymetria jest przeniesiona do zmiennej ukrytej.
4. **Zewnętrzny harmonogram lub warunek brzegowy.** Może wybrać jedną gałąź, ale łamie warunek autonomiczności.

W teorii bifurkacji symetryczny punkt może stać się niestabilny i rozgałęzić na orbitę niesymetrycznych stanów. To nie obala no-go: dokładna trajektoria startująca w punkcie symetrycznym pozostaje w nim przy jednoznacznej dynamice. Bifurkacja tworzy zbiór możliwych faz, nie wybiera jednej z nich.

## 6. Werdykt

| Pytanie | Status | Wniosek |
|---|---|---|
| Czy deterministyczna ekwiwariantna dynamika może wyjść z dokładnego \(P_0\)? | ✅ | Nie, jeśli ewolucja jest dobrze postawiona i jednoznaczna |
| Czy symetryczna kombinacja generatorów Centroidu wybiera kierunek? | ✅ | Nie; średnia na \(V_\rho\) to \(3I/4\) |
| Czy Wave wybiera pierwszą literę? | ❌/brak formalizmu | Obecny korzeń interpretuje słowa, nie generuje pierwszego symbolu |
| Czy Defect \(P_{\rm cyc}\) tworzy cykl z zera? | ❌ | Projektor rozdziela, nie zasila |
| Czy Flow \(\Phi\)/\(T_b\) tworzy pierwszą różnicę? | ❌ | Kanały wymagają wcześniejszych niezerowych składowych i złamania symetrii |
| Czy Net M16 dowodzi powstania różnicy z \(P_0\)? | ❌ | Warunek \(D_0\) jest losowany i niezerowy; most jest konstrukcyjny |
| Czy P₀-Relacje wyprowadza nośnik \(V\)? | 💡/otwarte | N-R2 jawnie pozostaje niezbudowane |

## 7. Konkluzja

W obecnych korzeniach P₀ nie ma mechanizmu, który deterministycznie i autonomicznie wyłania pierwszą różnicę z dokładnie symetrycznego \(P_0\), zachowując pełną ekwiwariancję \(S_4\).

To nie jest jeszcze obalenie całego programu P₀. Jest to twierdzenie o granicy tego, co może zrobić model przy obecnych założeniach. Jeżeli P₀ ma zachować autonomiczność i brak zewnętrznego ziarna, musi jawnie zmienić co najmniej jedno z założeń: definicję stanu początkowego, pojęcie dynamiki (np. dopuścić niejednoznaczność) albo poziom pierwotności (zbudować nośnik z relacji, zamiast zakładać K₄).

**Najbardziej uczciwy następny krok:** nie dopisywać ósmego mechanizmu asymetrii. Zbudować lub obalić formalnie N-R2 — rekonstrukcję nośnika \(V_t\) z pierwotnego obiektu relacyjnego — i sprawdzić, czy jego stabilizator jest od początku mniejszy niż \(S_4\). Jeżeli jest mniejszy, pierwsza asymetria nie została wygenerowana z symetrii: była wpisana w strukturę pierwotnej relacji. Jeżeli jest pełny \(S_4\), twierdzenie no-go nadal obowiązuje.

---
