# N-R2: kontrola wspólnych niezmienników w Scalar i Alchemy

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Źródła:** P₀-Scalar v0.3.5 §§2.1–2.4, 3, 4.2; P₀-Centroid v5.2 §11.12; P₀-Alchemy v0.4.4-alpha §§0–2, 4–6.  
**Status:** dla stałego grafu Scalar wymiar relacyjnych niezmienników wynosi \(c(G)-1\) ✅; zgodność z macierzami N=3 Scalar ✅; pełne przeniesienie prawa przecięcia z Centroidu na dowolne rundy Scalar otwarte 🔍; Alchemy nie ma wspólnego niezerowego liniowego niezmiennika w przestrzeni kształtu dla K₁ i całej kompensacji ❌/warunkowy no-go dla tej konkretnej klasy niezmienników.

## 1. Pytanie

Czy reguła kompozycji przez zachowanie wspólnego niezmiennika jest własnością wyłącznie szczególnej rodziny operatorów Centroidu, czy pojawia się też w innych korzeniach P₀?

Sprawdzam dwa odmienne przypadki:
- P₀-Scalar: lokalne aktualizacje zależne od grafu progowego;
- P₀-Alchemy: globalne skalowanie centroidalne i nieliniowe korekty progowe par.

Nie zakładam, że podobieństwo słownictwa oznacza ten sam mechanizm.

## 2. Scalar: pełna runda na ustalonym grafie

Niech \(G=(V,E)\) będzie ustalonym, nieskierowanym grafem interakcji. Aktualizacja lokalna wierzchołka i zastępuje jego współrzędną średnią z jego zamkniętego sąsiedztwa \(\{i\}\cup N_G(i)\), a pozostałe współrzędne pozostawia bez zmian.

Macierz kroku \(U_i(G)\) jest wierszowo-stochastyczna:
- wiersz i ma dodatnie wpisy dokładnie w kolumnach zamkniętego sąsiedztwa i;
- pozostałe wiersze są jednostkowe.

Niech każdy wierzchołek zostanie zaktualizowany dokładnie raz w dowolnej ustalonej kolejności, a pełna macierz rundy będzie:

\[
R_G=U_{i_n}(G)\cdots U_{i_1}(G).
\]

### Twierdzenie: liczba klas rekurencyjnych równa się liczbie składowych G

Dla każdej krawędzi \(\{i,j\}\in E\) w macierzy \(R_G\) zachodzą oba wpisy:

\[
(R_G)_{ij}>0,\qquad (R_G)_{ji}>0.
\]

Jeśli i jest aktualizowany przed j, to podczas aktualizacji i wiersz j jest jeszcze jednostkowy, więc nowy wiersz i otrzymuje dodatni wpis w kolumnie j. Gdy później aktualizuje się j, korzysta z aktualnego wiersza i, który ma dodatni wpis w kolumnie i. Analogiczny argument działa po zamianie kolejności i,j.

Ponadto macierz \(R_G\) jest blokowo-diagonalna względem składowych spójności G, ponieważ żadna aktualizacja nie korzysta z wierzchołka spoza własnej składowej.

Zatem dodatni graf przejść w obrębie każdej składowej G jest silnie spójny. Każda składowa G tworzy dokładnie jedną klasę rekurencyjną macierzy stochastycznej \(R_G\).

Jeśli \(c(G)\) oznacza liczbę składowych spójności G, to:

\[
\dim\ker(R_G^T-I)=c(G).
\]

Na przestrzeni relacyjnej \(V_\rho=\mathbf1^\perp\) interesują nas obserwable o sumie współrzędnych zero. Odrzucamy więc jeden globalny kierunek masy/centroidu i dostajemy:

\[
\boxed{\dim\mathcal I_\rho(R_G)=c(G)-1.}
\]

To jest dokładny wynik dla ustalonego grafu podczas całej rundy A2.

## 3. Kontrola z rzeczywistymi macierzami Scalar dla N=3

P₀-Scalar §4.2 podaje następujące macierze rund:

### Region II: ścieżka P₃

\[
A_{II}=
\begin{pmatrix}
1/2&1/2&0\\
1/6&1/2&1/3\\
1/12&1/4&2/3
\end{pmatrix},
\qquad
\operatorname{spec}(A_{II})=\{1,1/2,1/6\}.
\]

Graf P₃ jest spójny, więc \(c=1\) i:

\[
\dim\mathcal I_\rho(A_{II})=0.
\]

Lewy wektor własny dla wartości 1 jest proporcjonalny do \((1,2,2)\), ale nie ma sumy zero. Jest niezmiennikiem skalarnym, nie kontrastem relacyjnym.

### Region III: K₂ + K₁

\[
A_{III}=
\begin{pmatrix}
1/2&1/2&0\\
1/4&3/4&0\\
0&0&1
\end{pmatrix},
\qquad
\operatorname{spec}(A_{III})=\{1,1,1/4\}.
\]

Graf ma dwie składowe, więc:

\[
\dim\mathcal I_\rho(A_{III})=1.
\]

Lewe wektory własne dla wartości 1 można wybrać jako \((1,2,0)\) oraz \((0,0,1)\). Po normalizacji do sumy 1 otrzymujemy rozkłady stacjonarne:

\[
\pi_1=(1/3,2/3,0),\qquad \pi_2=(0,0,1).
\]

Ich różnica \(\pi_1-\pi_2=(1/3,2/3,-1)\) ma sumę zero i jest zachowanym kontrastem między domeną K₂ a izolowanym wierzchołkiem.

### Region V: 3K₁

Graf ma trzy izolowane wierzchołki, macierz rundy jest identycznością, a:

\[
\dim\mathcal I_\rho(I)=3-1=2.
\]

Wszystkie dwa niezależne kontrasty między trzema singletonowymi domenami są zachowane.

**Wniosek:** trzy podstawowe przypadki Scalar potwierdzają dokładną regułę:

\[
\boxed{\text{liczba niezależnych kontrastów}
=\text{liczba składowych grafu}-1.}
\]

Jest to zgodne z wynikami o zachowaniu rozłączności domen i nierozrastaniu się komponentów w P₀-Centroid §11.12.

## 4. Granica: graf Scalar może zmieniać się w trakcie rundy

Powyższe twierdzenie wymaga, aby G był stały w czasie całej rundy. W P₀-Scalar sąsiedztwa progowe zależą od bieżącego stanu, a kolejne aktualizacje A2 działają na różnych stanach pośrednich. Dlatego pełny przebieg nie zawsze jest jednym produktem macierzy \(U_i(G)\) dla jednego ustalonego G.

Dokument Scalar sam odróżnia:
- lokalne macierze dla określonego regionu grafowego;
- przejścia między regionami, które mogą zmienić graf w trakcie iteracji.

Nie wolno więc przenosić wyniku \(\dim\mathcal I_\rho=c(G)-1\) na całą dynamiczną rundę bez warunku utrzymania grafu albo odrębnego dowodu dla sekwencji zmian grafowych.

To pozostaje 🔍/otwarte.

## 5. Alchemy: centroid jest zachowany, ale nie ma wspólnego liniowego niezmiennika kształtu

P₀-Alchemy v0.4.4-alpha definiuje:
- K₁: \(p_i'=(1-\alpha)p_i+\alpha C\), gdzie \(C=\frac14\sum_jp_j\);
- K₂: symetryczną korektę pary, w której jeden punkt przesuwa się o \(+\gamma u\), a drugi o \(-\gamma u\).

Oba kroki zachowują globalny centroid:
- K₁ zachowuje sumę, bo \(\sum_i p_i'= (1-\alpha)\sum_i p_i+4\alpha C=4C\);
- każda korekta K₂ zachowuje sumę, ponieważ przesunięcia dwóch punktów znoszą się.

To jest dokładny niezmiennik translacyjny.

Jednak po przejściu do przestrzeni kształtu, czyli po odjęciu centroidu, K₁ działa jako:

\[
\widetilde p_i'=(1-\alpha)\widetilde p_i.
\]

Dla \(\alpha\ne0\) jedynym liniowym funkcjonałem zachowanym przez to skalowanie jest funkcjonał zerowy. Zatem nie istnieje niezerowy liniowy niezmiennik kształtu wspólny już dla K₁ i całego K.

Atraktor Alchemy ma stałą sygnaturę odległościową i orbitę obrotową, ale sygnatura ta jest własnością granicznego atraktora, nie dokładnym niezmiennikiem zachowanym dla dowolnego stanu początkowego podczas każdego kroku K.

**Wniosek:** reguła wspólnych liniowych niezmienników Centroidu nie przenosi się bezpośrednio na Alchemy. Nie jest to obalenie mechanizmu Alchemy; oznacza jedynie, że potrzebuje on innej klasy obserwabli lub innego pojęcia zachowania.

## 6. Co można uznać za wspólny rdzeń?

Mamy trzy poziomy:
1. **Centroid:** dodatnie słowa generatorów mają dokładną regułę przecięcia przestrzeni niezmienników; daje ona łączne działanie częściowe.
2. **Scalar:** dla ustalonego grafu jedna pełna runda zachowuje dokładnie tyle niezależnych relacyjnych kontrastów, ile wynosi liczba składowych minus jeden; przejście do dynamicznych grafów pozostaje osobną luką.
3. **Alchemy:** centroid jest zachowany, ale po usunięciu translacji K₁ kurczy całą przestrzeń kształtu; brak niezerowego wspólnego liniowego niezmiennika.

Wspólny rdzeń może więc nie brzmieć „każda kompensacja zachowuje ten sam niezmiennik”, tylko raczej:

**Akty kompensacji organizują przestrzeń konfiguracji przez to, które rozróżnienia pozostają obserwowalne po ich zastosowaniu.**

To zdanie wymaga jeszcze formalizacji jako ogólna teoria obserwabli/inwariantów. Nie należy nadawać mu statusu ✅ jako twierdzenia całego P₀.

## 7. Werdykt

- **✅** Dla ustalonego grafu A2 w Scalar liczba niezależnych kontrastów po pełnej rundzie wynosi \(c(G)-1\).
- **✅** Macierze AII, AIII i identyczność dla N=3 Scalar są zgodne z tą regułą.
- **🔍** Przeniesienie wyniku na rundy, w których graf progowy zmienia się między lokalnymi aktualizacjami, wymaga osobnego dowodu.
- **✅** Centroid i Scalar wykazują związek między zachowanymi obserwablami a pozostającą strukturą domen/nieaktualizowanych współrzędnych.
- **❌** Wspólna liniowa reguła niezmienników kształtu nie obejmuje Alchemy, ponieważ jego krok K₁ kurczy całą przestrzeń wycentrowaną.
- **💡** Wspólne zachowane obserwable mogą być bardziej ogólnym pojęciem organizacji relacyjnej niż pojedynczy model parowania.

## 8. Następny test

Należy sprawdzić, czy w dynamicznym Scalar przestrzeń zachowanych kontrastów aktualizuje się jako przecięcie przestrzeni obserwabli kolejnych grafów:

\[
\mathcal I_{t+1}\stackrel{?}{=}
\mathcal I_t\cap\mathcal I(G_{t+1}).
\]

Jeżeli tożsamość zachodzi przy zmianach progowych, mamy możliwość uogólnienia prawa kompozycji poza Centroid. Jeżeli nie, należy zidentyfikować dokładny mechanizm, który tworzy lub niszczy nowe niezmienniki na granicach regionów.

MVP-02 pozostaje poza zakresem.

## 9. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
