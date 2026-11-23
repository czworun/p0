# N-R2: Scalar — ten sam graf progowy, różne asymptotyczne profile

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Źródło:** P₀-Scalar v0.3.5, lokalna reguła A2; raporty Asteriona o niewystarczalności grafu progowego i zakazie skończonego osiągnięcia stabilności.  
**Status:** dokładny kontrprzykład jednakowego grafu początkowego i różnych granicznych partycji pod tym samym okresowym harmonogramem ✅; dokładne granice wyliczone przez dodatnie macierze stochastyczne ✅; asymptotyczny profil zależy od ilościowych marginesów, nie tylko od grafu ✅.

## 1. Pytanie

Wcześniejszy kontrprzykład pokazał, że ten sam graf progowy może po jednym lokalnym akcie dać różne grafy następne. Teraz sprawdzamy silniejsze pytanie:

Czy dwie konfiguracje o identycznej początkowej relacji progowej mogą — pod tym samym, uczciwym harmonogramem aktualizacji — dojść do różnych asymptotycznych profili stabilnych?

Tak. Poniższy przykład jest dokładny i używa wyłącznie ułamków wymiernych.

## 2. Dwie konfiguracje o tym samym grafie

Ustalmy:

\[
\epsilon=1,\qquad A=\{0,1,2,3\}.
\]

Wybierzmy:

\[
x=\left(0,-\frac9{10},\frac9{10},\frac9{10}\right),
\qquad
y=\left(0,-\frac7{10},\frac9{10},\frac9{10}\right).
\]

W obu konfiguracjach zachodzi:

- krawędzie \(\{0,1\},\{0,2\},\{0,3\},\{2,3\}\);
- brak krawędzi \(\{1,2\},\{1,3\}\).

Zatem:

\[
\boxed{
G_\epsilon(x)=G_\epsilon(y)
=
\{\{0,1\},\{0,2\},\{0,3\},\{2,3\}\}.
}
\]

To samo otoczenie: trójkąt (0-2-3) z liściem 1 dołączonym do wierzchołka 0. Różnica dotyczy wyłącznie marginesu \(d_{01}\):

\[
d_{01}(x)=\frac9{10},
\qquad
d_{01}(y)=\frac7{10}.
\]

Pozostałe krawędzie i niekrawędzie są identyczne.

## 3. Wspólny harmonogram

Stosujemy w obu przypadkach ten sam harmonogram okresowy:

\[
\sigma=(0,1,2,3)^\omega.
\]

Każdy indeks jest aktualizowany dokładnie raz w każdej rundzie. Jest to więc harmonogram okresowy i uczciwy.

## 4. Konfiguracja x: rozpad na dwa klastry

Pierwszy akt \(C_0\) widzi wszystkich pozostałych jako sąsiadów, więc:

\[
x^{(0)}=
C_0(x)=
\left(\frac9{40},-\frac9{10},\frac9{10},\frac9{10}\right).
\]

Po tej aktualizacji:

\[
\left|\frac9{40}-\left(-\frac9{10}\right)\right|
=\frac98>1.
\]

Krawędź \(\{0,1\}\) znika. Aktywny blok \(\{0,2,3\}\) pozostaje pełną kliką, ponieważ jego wartości leżą w przedziale:

\[
\left[\frac9{40},\frac9{10}\right],
\qquad
\operatorname{diam}=\frac{27}{40}<1.
\]

Indeks 1 pozostaje izolowany na zawsze:
- jego wartość \(-9/10\) nie zmienia się;
- wartości bloku \(\{0,2,3\}\) pozostają w przedziale wypukłym \([9/40,9/10]\);
- odległość od indeksu 1 do każdej współrzędnej aktywnego bloku pozostaje co najmniej \(9/8>1\).

Po pozostałych dwóch aktualizacjach pierwszej rundy:

\[
x^{(1)}
=
\left(
\frac9{40},
-\frac9{10},
\frac{27}{40},
\frac35
\right).
\]

Na bloku \((0,2,3)\) kolejna pełna runda jest produktem trzech operatorów średniej na pełnej trójce, w kolejności \(0,2,3\). W oznaczeniu współrzędnych bloku jako \((0,2,3)\) macierz jednej rundy wynosi:

\[
Q=
\begin{pmatrix}
1/3&1/3&1/3\\
1/9&4/9&4/9\\
4/27&7/27&16/27
\end{pmatrix}.
\]

Wszystkie wpisy Q są dodatnie, a suma każdego wiersza wynosi 1. Jest to dodatnia macierz stochastyczna, więc jej potęgi zbiegają do macierzy rzędu jeden. Jej rozkład stacjonarny lewostronny to:

\[
\pi_x=\left(\frac16,\frac13,\frac12\right).
\]

Wartość graniczna bloku:

\[
\frac16\frac9{40}
+\frac13\frac{27}{40}
+\frac12\frac35
=
\frac9{16}.
\]

Zatem:

\[
\boxed{
x^{(m)}\longrightarrow
\left(-\frac9{10},\frac9{16},\frac9{16},\frac9{16}\right)
}
\]

(z zachowaniem indeksów w kolejności \(0,1,2,3\); współrzędna 1 pozostaje równa \(-9/10\), a pozostałe zbiegają do \(9/16\)).

Granica jest stabilna, bo odległość między blokami wynosi:

\[
\frac9{16}+\frac9{10}
=\frac{117}{80}>1.
\]

Graniczna partycja:

\[
\boxed{\Pi_x=\{\{1\},\{0,2,3\}\}.}
\]

## 5. Konfiguracja y: pełny konsensus

Dla y pierwszy akt \(C_0\) daje:

\[
C_0(y)=
\left(\frac{11}{40},-\frac7{10},\frac9{10},\frac9{10}\right).
\]

Teraz:

\[
\left|\frac{11}{40}-\left(-\frac7{10}\right)\right|
=\frac{39}{40}<1.
\]

Krawędź \(\{0,1\}\) pozostaje. Wykonujemy kolejne akty z tej samej rundy.

Przy \(C_1\) jedynym sąsiadem indeksu 1 jest 0:

\[
r_1=
\frac12\left(-\frac7{10}+\frac{11}{40}\right)
=-\frac{17}{80}.
\]

Przy \(C_2\) sąsiadami są 0 i 3, zatem:

\[
r_2=
\frac13\left(
\frac9{10}+\frac{11}{40}+\frac9{10}
\right)
=\frac{83}{120}.
\]

Przy \(C_3\) sąsiadami są 0 i 2:

\[
r_3=
\frac13\left(
\frac9{10}+\frac{11}{40}+\frac{83}{120}
\right)
=\frac{28}{45}.
\]

Po pierwszej pełnej rundzie:

\[
y^{(1)}=
\left(
\frac{11}{40},
-\frac{17}{80},
\frac{83}{120},
\frac{28}{45}
\right).
\]

Rozstęp wszystkich współrzędnych wynosi:

\[
\max_i y_i^{(1)}-\min_i y_i^{(1)}
=
\frac{83}{120}+\frac{17}{80}
=
\frac{217}{240}<1.
\]

Graf progowy jest więc teraz pełną kliką \(K_4\). Ponieważ każda kolejna aktualizacja jest średnią współrzędnych należących do tego samego przedziału o średnicy mniejszej niż 1, graf pozostaje pełny na zawsze.

Jedna pełna runda na \(K_4\), w kolejności \(0,1,2,3\), ma macierz:

\[
P=
\begin{pmatrix}
1/4&1/4&1/4&1/4\\
1/16&5/16&5/16&5/16\\
5/64&9/64&25/64&25/64\\
25/256&45/256&61/256&125/256
\end{pmatrix}.
\]

Macierz jest dodatnia i stochastyczna. Jej rozkład stacjonarny lewostronny wynosi:

\[
\pi_y=\left(\frac1{10},\frac15,\frac3{10},\frac25\right).
\]

Granica pełnego konsensusu to:

\[
\begin{aligned}
c_y
&=
\frac1{10}\frac{11}{40}
-\frac15\frac{17}{80}
+\frac3{10}\frac{83}{120}
+\frac25\frac{28}{45}\\
&=\frac{1589}{3600}.
\end{aligned}
\]

Zatem:

\[
\boxed{
y^{(m)}\longrightarrow
\left(\frac{1589}{3600},
\frac{1589}{3600},
\frac{1589}{3600},
\frac{1589}{3600}\right).
}
\]

Graniczna partycja:

\[
\boxed{\Pi_y=\{\{0,1,2,3\}\}.}
\]

## 6. Twierdzenie porównawcze

Mamy jednocześnie:

\[
G_\epsilon(x)=G_\epsilon(y),
\]

ten sam porządek wartości względem etykiet, ten sam próg \(\epsilon=1\), ten sam harmonogram \((0,1,2,3)^\omega\), ale:

\[
\boxed{\Pi_x\ne\Pi_y.}
\]

Dokładniej:

\[
\Pi_x=\{\{1\},\{0,2,3\}\},
\qquad
\Pi_y=\{\{0,1,2,3\}\}.
\]

To dowodzi, że asymptotyczny profil Scalar nie jest funkcją samego początkowego grafu progowego — nawet przy ustalonym, okresowym i uczciwym harmonogramie.

Różnicę powoduje ilościowy margines \(d_{01}\): w pierwszej konfiguracji aktualizacja przesuwa 0 na tyle daleko od 1, że relacja progowa znika; w drugiej odległość pozostaje poniżej progu, po czym cały graf staje się kliką.

## 7. Związek z zakazem skończonej stabilizacji

Poprzedni lemat wykazał:

\[
C_i^{-1}(\mathcal S_\epsilon)=\mathcal S_\epsilon.
\]

Żadna z powyższych trajektorii nie osiąga zatem stabilności po skończonej liczbie aktów. Stabilność pojawia się dopiero jako granica:

\[
x^{(m)}\to x^\ast\in\mathcal S_\epsilon,
\qquad
y^{(m)}\to y^\ast\in\mathcal S_\epsilon.
\]

Przykład rozdziela więc dwie kwestie:
- skończone słowa aktów nie osiągają stabilności z niestabilnego stanu;
- nieskończony harmonogram może wyłonić graniczną partycję, a jej wybór zależy od marginesów odległości.

To jest właściwe miejsce na nietrywialny profil dynamiczny Scalar: nie w języku skończonych słów, ale w przyporządkowaniu granicznego profilu do stanu początkowego i nieskończonego harmonogramu.

## 8. Konsekwencje dla P₀

1. Sama relacja progowa nie wyznacza przyszłości Scalar.
2. Nawet przy tym samym harmonogramie graniczna partycja może zależeć od ilościowych marginesów.
3. Jeśli P₀ chce abstrahować od bezwzględnych współrzędnych, musi zachować co najmniej wystarczającą informację o relacyjnych odległościach lub ich analogach.
4. Nie można zastąpić tych danych samą binarną zgodnością/niezgodnością par.
5. Asymptotyczny profil nie jest jeszcze automatem resztkowym na skończonych historiach. Wymaga semantyki nieskończonych harmonogramów i granic.

Nie wynika stąd żaden selektor liczby cztery.

## 9. Werdykt

- **✅** Dwie konfiguracje o identycznym grafie progowym mogą pod tym samym okresowym harmonogramem dojść do różnych granicznych partycji.
- **✅** Dla konfiguracji x granica ma dwa klastry: \(\{1\}\) oraz \(\{0,2,3\}\), z wartościami \(-9/10\) i \(9/16\).
- **✅** Dla konfiguracji y granica jest pełnym konsensusem \(1589/3600\).
- **✅** Obie granice wynikają z dodatnich macierzy stochastycznych, więc zbieżność jest ścisła, nie jest jedynie obserwacją numeryczną.
- **✅** Asymptotyczny profil wymaga ilościowych marginesów odległości; sam graf progowy nie wystarcza.
- **🔍** Ogólne kryteria zbieżności dla wszystkich uczciwych harmonogramów A2 pozostają poza tym przykładem.
- **❌** Nie można zdefiniować dokładnego asymptotycznego profilu Scalar wyłącznie jako funkcji początkowej partycji progowej.
- **💡** W P₀ warto szukać relacyjnego odpowiednika marginesu: informacji o tym, jak daleko para relacji znajduje się od granicy kompatybilności, bez zakładania z góry euklidesowej metryki.

## 10. Następny test

Następnie należy sprawdzić, czy dla ustalonego okresowego harmonogramu A2 granica istnieje dla każdej konfiguracji początkowej, czy tylko dla badanych klas. Osobno trzeba zbadać zależność wyniku od kolejności harmonogramu: czy ta sama konfiguracja i inna permutacja pełnej rundy mogą wybrać inną graniczną partycję.

To rozdzieli trzy źródła informacji: początkowy graf, ilościowe marginesy i kolejność aktów.

## 11. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
