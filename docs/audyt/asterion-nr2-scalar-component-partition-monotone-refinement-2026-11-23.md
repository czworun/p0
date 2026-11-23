# N-R2: Scalar — składowe grafu progowego nie mogą się ponownie łączyć

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Źródło modelu:** P₀-Scalar v0.3.5, lokalny akt A2 i symetryczny próg \(<\epsilon\).  
**Status:** przedziały wypukłe różnych składowych są oddzielone co najmniej o \(\epsilon\) ✅; pojedynczy akt nie może utworzyć krawędzi między dotychczasowymi składowymi ✅; partycja na składowe tylko się rozdrabnia i ustala po najwyżej \(n-c_0\) podziałach ✅; wewnętrzna topologia każdej końcowej składowej może nadal się zmieniać 🔍.

## 1. Pytanie

W poprzednim etapie ustalono, że dokładna zbieżność A2 dla deterministycznych harmonogramów ograniczenie uczciwych zależy od tego, czy graf progowy może zmieniać topologię nieskończenie wiele razy.

Najpierw trzeba rozdzielić dwie różne topologie:
1. **partycję wierzchołków na składowe spójności**;
2. **pełny zbiór krawędzi wewnątrz tych składowych**.

Pierwsza ma prostą, silną monotoniczność. Druga — nie.

## 2. Przedziały wypukłe składowych są rozdzielone

Niech \(G_\epsilon(x)\) będzie grafem o wierzchołkach \(1,\ldots,n\), z krawędzią \(\{i,j\}\) wtedy i tylko wtedy, gdy:

\[
|x_i-x_j|<\epsilon.
\]

Dla składowej spójności \(C\) oznaczmy:

\[
m_C=\min_{i\in C}x_i,\qquad
M_C=\max_{i\in C}x_i,
\qquad
H_C=[m_C,M_C].
\]

**Lemat.** Dla różnych składowych \(C,D\):

\[
\boxed{\operatorname{dist}(H_C,H_D)\ge\epsilon.}
\]

### Dowód

Dla każdej składowej zdefiniujmy sumę otwartych przedziałów:

\[
U_C=\bigcup_{i\in C}
\left(x_i-\frac\epsilon2,x_i+\frac\epsilon2\right).
\]

Jeśli \(\{i,j\}\) jest krawędzią, to \(|x_i-x_j|<\epsilon\), więc odpowiadające przedziały o promieniu \(\epsilon/2\) przecinają się. Ponieważ C jest spójna, \(U_C\) jest spójnym zbiorem otwartym w \(\mathbb R\), a zatem przedziałem. Zawiera wszystkie punkty \(x_i\) oraz rozciąga się od \(m_C-\epsilon/2\) do \(M_C+\epsilon/2\).

Dla różnych składowych \(C,D\) zbiory \(U_C,U_D\) są rozłączne. Gdyby miały wspólny punkt, istniałoby \(i\in C,j\in D\), dla których dwa przedziały promienia \(\epsilon/2\) się przecinają, czyli \(|x_i-x_j|<\epsilon\). To dałoby krawędź między składowymi — sprzeczność.

Przedziały \(U_C,U_D\) są więc rozłączne, co wymusza oddalenie ich domkniętych rdzeni \(H_C,H_D\) o co najmniej \(\epsilon\). ∎

## 3. Pojedynczy akt zachowuje przedział swojej składowej

Niech i należy do składowej C w chwili t. Wszystkie jego aktualne sąsiedztwa należą do C, ponieważ krawędź nie może prowadzić poza składową.

Akt A2 ma postać:

\[
x_i'=
\frac{x_i+\sum_{j\in N_\epsilon(i;x)}x_j}
{1+|N_\epsilon(i;x)|}.
\]

Jest to średnia wartości należących do C. Zatem:

\[
\boxed{x_i'\in[m_C,M_C].}
\]

Pozostałe współrzędne nie zmieniają się. W efekcie przedział wypukły wszystkich wartości indeksów należących do starej składowej C nie rozszerza się:

\[
H_C'\subseteq H_C.
\]

Dla dwóch różnych starych składowych C,D ich przedziały były oddzielone o co najmniej \(\epsilon\), a po aktualizacji tylko się zwężają. Nie może zatem powstać nowa krawędź między C i D.

Aktualizacja może natomiast usunąć część krawędzi wewnątrz C i rozdzielić C na mniejsze składowe.

## 4. Twierdzenie: partycja na składowe tylko się rozdrabnia

Niech \(\mathcal P_t\) oznacza partycję indeksów na składowe spójności \(G_\epsilon(x^t)\).

Z lematu i własności średniej wynika:

\[
\boxed{\mathcal P_{t+1}\preceq\mathcal P_t,}
\]

gdzie \(\preceq\) oznacza „jest rozdrobnieniem”: każda składowa w chwili \(t+1\) zawiera się w jednej składowej z chwili t.

W szczególności liczba składowych:

\[
c_t=|\mathcal P_t|
\]

jest niemalejąca i ograniczona przez n:

\[
c_0\le c_t\le n.
\]

Każda ścisła zmiana partycji zwiększa \(c_t\) o co najmniej jeden. Jest więc najwyżej:

\[
\boxed{n-c_0}
\]

chwil, w których partycja składowych ulega zmianie.

**Wniosek ✅:** istnieje skończony czas \(T\), po którym partycja na składowe spójności jest stała dla wszystkich \(t\ge T\). Wynik nie wymaga:
- uczciwości harmonogramu;
- okresowości;
- losowego wyboru indeksu;
- zaniku przesunięć \(\Delta_t\);
- zbieżności wartości współrzędnych.

To jest czysto geometryczny skutek jednowymiarowości, symetrycznego progu i lokalnej aktualizacji będącej średnią sąsiadów z tej samej składowej.

## 5. Co twierdzenie nie mówi

Nie wynika z niego, że pełny graf progowy \(G_\epsilon(x^t)\) stabilizuje się po skończonej liczbie kroków.

Wewnątrz jednej końcowej składowej C krawędzie mogą być usuwane i dodawane, o ile składowa pozostaje spójna. Twierdzenie blokuje tylko ponowne łączenie różnych składowych; nie blokuje zmian krawędzi wewnętrznych.

Po czasie T wiemy zatem:
- każda końcowa składowa C pozostaje spójna w każdej chwili;
- różne końcowe składowe pozostają oddalone o co najmniej \(\epsilon\);
- lokalne aktualizacje nie przenoszą wartości poza przedział swojej końcowej składowej;
- zbiór krawędzi wewnątrz C może nadal zależeć od aktualnych marginesów.

To jest dokładna granica obecnego twierdzenia.

## 6. Związek z literaturą HK

Podobne rozdzielenie klastrów na prostej jest używane w analizie asynchronicznego HK. Etesami i Başar zauważają w dowodzie Lematu 7, że dwa rozdzielone klastry na prostej pozostają rozdzielone w dalszej dynamice; stąd można analizować je niezależnie. W ich modelu aktywacje są jednak wybierane jednostajnie losowo, a nie przez dowolny deterministyczny harmonogram. Zob. [Etesami–Başar, 2015, §V-A](https://arxiv.org/abs/1412.6546).

Ich Twierdzenie 6 dowodzi ponadto ograniczenia oczekiwanej liczby zmian pełnej topologii dla niezależnego, jednostajnego wyboru aktywowanego agenta:

\[
\mathbb E[\#\text{ zmian topologii}]\le16n^9.
\]

Stąd topologia zmienia się skończenie wiele razy z prawdopodobieństwem 1 w modelu losowym. Nie wynika z tego skończona liczba zmian dla każdego deterministycznego harmonogramu ograniczenie uczciwego.

W P₀ pozostaje też jawna różnica konwencji: próg jest ścisły \(<\epsilon\), podczas gdy klasyczna literatura HK często używa \(\le\epsilon\). Dowód rozdzielenia składowych powyżej został przeprowadzony bezpośrednio dla ścisłej konwencji P₀.

## 7. Konsekwencja dla zbieżności

Po czasie T dynamika rozkłada się na niezależne podukłady odpowiadające stałym blokom partycji końcowej:

\[
\mathcal P_T=\{C_1,\ldots,C_q\}.
\]

Dla każdego C:
- wszystkie aktualizacje są kombinacjami wypukłymi współrzędnych C;
- graf \(G_\epsilon(x^t)[C]\) pozostaje spójny;
- energia relacyjna wewnątrz C nie rośnie;
- przyrosty lokalne dążą do zera na mocy globalnego oszacowania Lyapunova.

Jeśli dodatkowo pełna topologia wewnątrz C ustali się, a harmonogram będzie ograniczenie uczciwy, zachodzi zbieżność do konsensusu w C (dowód macierzowy w raporcie o energii Lyapunova).

Jeśli topologia wewnętrzna nie ustala się, nadal nie mamy ogólnego dowodu zbieżności każdego współrzędnego. Skończona liczba podziałów składowych nie zastępuje dowodu skończonej liczby przełączeń krawędzi.

## 8. Werdykt

- **✅** Przedziały wypukłe różnych składowych grafu progowego na prostej są oddalone o co najmniej \(\epsilon\).
- **✅** Każdy akt A2 pozostaje w przedziale swojej bieżącej składowej.
- **✅** Żadne dwie różne składowe nie mogą się później połączyć.
- **✅** Partycja na składowe tylko się rozdrabnia i stabilizuje po najwyżej \(n-c_0\) ścisłych podziałach.
- **❌** Nie dowodzi to stabilizacji wszystkich krawędzi wewnątrz końcowych składowych.
- **🔍** Dla deterministycznego harmonogramu ograniczenie uczciwego pozostaje otwarte, czy krawędzie wewnętrzne mogą przełączać się nieskończenie wiele razy i czy mimo to wszystkie współrzędne zbiegają.
- **💡** Po rozdzieleniu składowych problem Scalar redukuje się do niezależnych układów jednowymiarowych, których grafy pozostają spójne w każdej chwili.

## 9. Następny test

W obrębie pojedynczej końcowej składowej należy teraz ustalić, czy ograniczona uczciwość aktualizacji i nieprzerwana spójność grafu wystarczają do konsensusu, nawet jeśli krawędzie zmieniają się w czasie.

Są dwie drogi:
1. wykazać jednolitą kontrakcję średnicy w każdym bloku o ograniczonej długości;
2. znaleźć dokładny kontrprzykład, w którym spójny graf progowy pozostaje spójny w każdej chwili, harmonogram jest ograniczenie uczciwy, lecz średnica nie dąży do zera.

Nie wolno zastępować tego założeniem, że krawędzie są stałe — to właśnie jest nierozstrzygnięty punkt.

## 10. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
