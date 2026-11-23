# N-R2: punkty stałe pełnej rundy A2 przy grafie zmieniającym się wewnątrz rundy

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Źródło:** P₀-Scalar v0.3.5 §§2.1–2.3, 3.1–3.2, 4; wcześniejszy raport o stabilnych profilach Centroid/Scalar.  
**Status:** stałe punkty pełnej rundy aktualizującej każdą współrzędną dokładnie raz są przecięciem zbiorów punktów stałych kroków lokalnych ✅; dla progowego A2 punkty stałe są dokładnie konfiguracjami o blokach równych wartości oddzielonych co najmniej ε ✅; wszystkie partycje indeksów są realizowalne jako profile Scalar ✅; n=4 nie jest wybierane ❌/kontrmodel; łączność kompozycji wielu nieliniowych rund progowych pozostaje otwarta 🔍.

## 1. Pytanie

Poprzedni wynik macierzowy dla Scalar zakładał, że graf G pozostaje stały przez całą rundę. W rzeczywistym A2 sąsiedztwo może zależeć od aktualnego stanu, więc po lokalnej aktualizacji może się zmienić.

Czy da się mimo tego opisać punkty stałe rundy bez zamrażania grafu?

Tak. Wystarczy wykorzystać fakt, że lokalny krok zmienia dokładnie jedną współrzędną, a pełna runda aktualizuje każdą współrzędną dokładnie raz.

## 2. Lemat ogólny: punkt stały pełnej rundy to wspólny punkt stały kroków

Niech \(Q\) będzie przestrzenią konfiguracji z n współrzędnymi. Dla każdego i niech \(C_i:Q\to Q\) będzie deterministycznym aktem, który może zmienić wyłącznie współrzędną i.

Weźmy dowolną permutację \(\sigma\) i pełną rundę:

\[
F=C_{\sigma(n)}\circ\cdots\circ C_{\sigma(1)}.
\]

**Lemat:**

\[
\boxed{\operatorname{Fix}(F)=\bigcap_{i=1}^n\operatorname{Fix}(C_i).}
\]

### Dowód

Niech \(F(x)=x\). Rozważmy współrzędną i. Żaden krok przed \(C_i\) nie może jej zmienić, bo każdy z nich zmienia inną współrzędną. Żaden krok po \(C_i\) również jej nie zmienia.

Jeżeli po całej rundzie współrzędna i wraca do wartości początkowej, to krok \(C_i\) musiał pozostawić ją bez zmiany. Ponieważ \(C_i\) modyfikuje tylko tę współrzędną, cały wektor po kroku jest identyczny z wektorem przed krokiem.

To dotyczy każdego i. W konsekwencji wszystkie stany pośrednie rundy są równe x, a \(C_i(x)=x\) dla każdego i.

Odwrotna implikacja jest natychmiastowa: jeżeli każdy krok lokalny pozostawia x bez zmian, pełna runda również pozostawia x bez zmian. ∎

**Ważne:** dowód nie wymaga, aby \(C_i\) były liniowe, ciągłe, ani aby ich reguły były ustalone niezależnie od stanu. Sąsiedztwo może być przeliczane po każdym kroku. Potrzebne jest tylko to, by każdy krok modyfikował własną, odrębną współrzędną i aby każda była aktualizowana raz.

## 3. Zastosowanie do progowego A2 w Scalar

P₀-Scalar definiuje lokalną aktualizację:

\[
\bigl(C_\epsilon^{(i)}(r)\bigr)_k=
\begin{cases}
r_k,&k\ne i,\\[2mm]
\displaystyle
\frac{r_i+\sum_{j\in N_\epsilon(i;r)}r_j}
{1+|N_\epsilon(i;r)|},&k=i,
\end{cases}
\]

gdzie:

\[
N_\epsilon(i;r)=\{j\ne i:|r_i-r_j|<\epsilon\}.
\]

Sąsiedztwo jest wyznaczane z bieżącej konfiguracji r, a więc może się zmieniać pomiędzy lokalnymi aktualizacjami.

Jednak z lematu z §2:

\[
r\in\operatorname{Fix}(\mathcal R_\epsilon)
\iff
r\in\bigcap_i\operatorname{Fix}(C_\epsilon^{(i)}).
\]

Dla każdego i warunek punktu stałego lokalnego jest równoważny:

\[
r_i=
\frac{r_i+\sum_{j\in N_\epsilon(i;r)}r_j}
{1+|N_\epsilon(i;r)|}.
\]

Po przekształceniu:

\[
|N_\epsilon(i;r)|\,r_i
=
\sum_{j\in N_\epsilon(i;r)}r_j.
\]

Niech \(G_\epsilon(r)\) będzie nieskierowanym grafem progowym: krawędź \(\{i,j\}\) istnieje dokładnie wtedy, gdy \(|r_i-r_j|<\epsilon\). Otrzymany układ równań to:

\[
L(G_\epsilon(r))\,r=0,
\]

gdzie L jest laplasjanem grafu.

## 4. Twierdzenie: profile stałe to klasy równych wartości

Dla skończonego grafu nieskierowanego jądro laplasjanu składa się dokładnie z wektorów stałych na każdej składowej spójności.

Zatem r jest punktem stałym pełnej rundy A2 wtedy i tylko wtedy, gdy jest stały na każdej składowej \(G_\epsilon(r)\).

Ale krawędzie grafu progowego łączą wyłącznie pary o różnicy mniejszej niż ε. Jeżeli wartości są stałe na składowych, to w każdej składowej wszystkie współrzędne są równe. Stąd równoważny warunek:

\[
\boxed{
r\in\operatorname{Fix}(\mathcal R_\epsilon)
\iff
\forall i,j:
\ |r_i-r_j|<\epsilon\Rightarrow r_i=r_j.
}
\]

Inaczej mówiąc: dowolne dwie współrzędne są albo identyczne, albo oddalone o co najmniej ε.

### Interpretacja profilowa

Definiujemy:

\[
i\sim_r j\iff r_i=r_j.
\]

W punkcie stałym klasy \(\sim_r\) są dokładnie składowymi grafu progowego. Profile nie zostały wpisane jako etykiety; są klasami współrzędnych, których wartości nie dają się rozróżnić w stabilnej konfiguracji.

To jest mocniejsze od wyniku dla grafu zamrożonego: opisuje zbiór punktów stałych prawdziwej rundy A2 nawet wtedy, gdy sąsiedztwo jest przeliczane po każdym lokalnym kroku.

## 5. Kontrmodel: Scalar dopuszcza każdą liczbę profili

Niech \(\mathcal P\) będzie dowolną partycją zbioru indeksów \(\{1,\ldots,n\}\) na m niepustych bloków.

Przypiszmy każdemu blokowi inną wartość \(z_1,\ldots,z_m\), tak aby:

\[
|z_a-z_b|\ge\epsilon\qquad(a\ne b).
\]

Dla każdego i z bloku \(P_a\) ustawmy \(r_i=z_a\).

Wtedy:
- współrzędne w tym samym bloku są równe i należą do tego samego grafowego klastra;
- różne bloki są rozdzielone progiem i nie mają krawędzi między sobą;
- każda lokalna aktualizacja jest identycznością;
- pełna runda jest punktem stałym.

Każda partycja jest więc realizowalna. Liczba profili m może wynosić dowolną liczbę od 1 do n.

W szczególności:
- n=3 dopuszcza 3 profile;
- n=4 dopuszcza 4 profile;
- n=5 dopuszcza 5 profili.

Nie ma selektora n=4. W rzeczywistości model Scalar dopuszcza wszystkie struktury partycyjne indeksów.

## 6. Co z łącznością?

Lemat z §2 daje dokładną regułę dla pełnej rundy złożonej z n różnych kroków lokalnych:

\[
\operatorname{Fix}(C_{\sigma(n)}\cdots C_{\sigma(1)})
=
\bigcap_i\operatorname{Fix}(C_i).
\]

Przecięcie zbiorów jest łączne, więc zbiór stabilnych konfiguracji pełnej rundy jest niezależny od kolejności aktualizacji i ma postać wspólnego zbioru punktów stałych kroków lokalnych.

Nie wolno jednak na tej podstawie automatycznie wnioskować, że dla dwóch różnych, nieliniowych pełnych rund progowych \(F_{\epsilon_1},F_{\epsilon_2}\):

\[
\operatorname{Fix}(F_{\epsilon_2}\circ F_{\epsilon_1})
=
\operatorname{Fix}(F_{\epsilon_1})\cap
\operatorname{Fix}(F_{\epsilon_2}).
\]

W takiej kompozycji każda współrzędna jest aktualizowana ponownie, więc krok drugiej rundy może zmienić współrzędną zmodyfikowaną już w rundzie pierwszej. Potrzebny jest osobny argument wykluczający kompensację zmian między rundami.

**Wynik ✅** dotyczy pełnej jednej rundy z lokalnymi krokami o rozłącznych współrzędnych. Łączność kompozycji dowolnej liczby rund nieliniowych pozostaje otwarta.

## 7. Konfrontacja z Centroidem

Lemat z §2 obejmuje również pełną rundę Centroidu \(M_{n-1}\cdots M_0\), ponieważ każdy \(M_i\) aktualizuje dokładnie jedną współrzędną.

Dla Centroidu wspólny punkt stały lokalnych aktualizacji na pełnej przestrzeni to wyłącznie konsensus:

\[
M_i x=x\ \forall i
\iff x_0=x_1=\cdots=x_{n-1}.
\]

Dlatego pełna runda ma wyłącznie trywialny profil stały w ilorazie przez globalne przesunięcie.

Różnica między Centroidem a Scalar nie polega więc na samej kolejności Gaussa–Seidela, lecz na regule lokalnej:
- Centroid zawsze uśrednia wszystkie współrzędne — pełny graf, jeden profil końcowy;
- Scalar uśrednia tylko aktualnych sąsiadów progowych — możliwe są stabilne podziały na wiele profili.

Wspólna jest zasada, że punkt stały pełnej rundy jest wspólnym punktem stałym wszystkich lokalnych aktów.

## 8. Werdykt

- **✅** Dla dowolnych deterministycznych kroków lokalnych, z których każdy modyfikuje jedną odrębną współrzędną dokładnie raz w rundzie, punkty stałe pełnej rundy są przecięciem punktów stałych kroków.
- **✅** Dla progowego Scalar punkty stałe są dokładnie konfiguracjami, w których każda para współrzędnych jest albo równa, albo oddalona o co najmniej ε.
- **✅** Profile stabilnego Scalar są klasami równych wartości i każda partycja indeksów jest realizowalna.
- **✅** Wynik nie wymaga zamrożenia grafu progowego wewnątrz jednej rundy.
- **❌** Liczba profili w Scalar nie jest ograniczona do czterech; może wynosić dowolne m≤n.
- **🔍** Łączność zbiorów punktów stałych dla jednej pełnej rundy jest zamknięta; dla złożenia wielu nieliniowych rund progowych nie jest jeszcze dowiedziona.
- **💡** Stabilne klasy równoważności mogą stanowić relacyjne profile wyłaniające się z aktów kompensacji, bez jawnego podawania źródeł i celów.

## 9. Następny krok

Trzeba teraz sprawdzić, czy punkty stałe lokalnych aktów można rozpoznać bez współrzędnych i wartości liczbowych. Najbardziej obiecujący kierunek to relacja nierozróżnialności:

\[
i\sim j
\iff
\text{żaden stabilny akt nie odróżnia i od j}.
\]

W Scalar daje ona dokładnie klastry równości. Pytanie otwarte brzmi, czy istnieje analogiczna definicja w P₀-Relacje, która nie zakłada z góry zbioru indeksów i zachowuje tę samą strukturę przy kompozycji.

MVP-02 poza zakresem.

## 10. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
