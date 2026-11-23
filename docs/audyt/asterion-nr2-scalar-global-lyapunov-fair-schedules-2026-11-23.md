# N-R2: Scalar — global energia Lyapunova i warunki zbieżności A2

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Źródło modelu:** P₀-Scalar v0.3.5, lokalny akt progowy A2.  
**Status:** globalny spadek energii relacyjnej przy każdym pojedynczym akcie ✅; suma kwadratów przesunięć jest skończona dla dowolnego harmonogramu ✅; globalne ekstrema mają granice ✅; zbieżność przy ustalonej topologii i harmonogramie okresowo/ograniczenie uczciwym ✅; zbieżność dla dowolnego uczciwego harmonogramu przy nieustannie zmieniającej się topologii pozostaje otwarta 🔍.

## 1. Pytanie

W poprzednich raportach wykazano:
- brak możliwości osiągnięcia dokładnej stabilności z niestabilnego stanu w skończonej liczbie aktów;
- zależność granicznej partycji od ilościowych marginesów odległości;
- zależność granicznej partycji od kolejności aktualizacji.

Pozostaje pytanie ogólniejsze: czy każdy przebieg A2 zbiega, czy też dotąd widzieliśmy tylko kilka zbieżnych harmonogramów?

Zamiast od razu zakładać zbieżność, szukam funkcji monotonicznej, która obowiązuje dla każdego aktu i każdego harmonogramu.

## 2. Energia relacyjna

Dla \(x=(x_1,\ldots,x_n)\) definiuję:

\[
\boxed{
\Phi_\epsilon(x)=
\sum_{1\le i<j\le n}
\min\{(x_i-x_j)^2,\epsilon^2\}.
}
\]

Własności:
- \(\Phi_\epsilon(x)\ge0\);
- \(\Phi_\epsilon(x)\le\binom n2\epsilon^2\);
- funkcja jest niezmiennicza względem translacji i odbicia osi;
- pary bliższe niż próg wnoszą kwadrat odległości, a pary poza progiem wnoszą wartość nasyconą \(\epsilon^2\).

To nie jest jeszcze energia całego P₀. Jest to dokładna funkcja Lyapunova konkretnego lokalnego A2.

## 3. Twierdzenie o spadku po jednym akcie

Niech:

\[
N_i(x)=\{j\ne i:|x_j-x_i|<\epsilon\},
\qquad
s_i=|N_i(x)|+1,
\]

a nowa wartość współrzędnej \(i\) będzie średnią:

\[
\bar x_i=
\frac{x_i+\sum_{j\in N_i(x)}x_j}{s_i}.
\]

Oznaczmy:

\[
\Delta_i=\bar x_i-x_i.
\]

**Twierdzenie:**

\[
\boxed{
\Phi_\epsilon(x)-\Phi_\epsilon(C_i(x))
\ge
(|N_i(x)|+2)\Delta_i^2.
}
\]

### Dowód

Tylko składniki energii zawierające indeks \(i\) mogą ulec zmianie.

Dla \(j\notin N_i(x)\) mamy \(|x_i-x_j|\ge\epsilon\), zatem stary składnik wynosi \(\epsilon^2\), a nowy jest nie większy niż \(\epsilon^2\). Takie pary nie mogą zwiększyć energii.

Dla \(j\in N_i(x)\) stary składnik to \((x_i-x_j)^2\), a nowy jest nie większy niż \((\bar x_i-x_j)^2\). Stąd:

\[
\begin{aligned}
\Phi_\epsilon(x)-\Phi_\epsilon(C_i(x))
&\ge
\sum_{j\in N_i(x)}
\left[(x_i-x_j)^2-(\bar x_i-x_j)^2\right].
\end{aligned}
\]

Niech \(S_i=\{i\}\cup N_i(x)\), zatem \(|S_i|=s_i\), a \(\bar x_i\) jest średnią elementów zbioru \(S_i\).

Tożsamość wariancji daje:

\[
\sum_{k\in S_i}(x_k-x_i)^2
=
\sum_{k\in S_i}(x_k-\bar x_i)^2
+s_i(\bar x_i-x_i)^2.
\]

Po odjęciu składnika dla \(k=i\) po stronie nowej sumy otrzymujemy dodatkowo \((\bar x_i-x_i)^2\). Zatem:

\[
\sum_{j\in N_i(x)}
\left[(x_i-x_j)^2-(\bar x_i-x_j)^2\right]
=(s_i+1)\Delta_i^2
=(|N_i(x)|+2)\Delta_i^2.
\]

Teza wynika z powyższych nierówności. ∎

## 4. Globalne konsekwencje — każdy harmonogram

Niech \(i_t\) będzie indeksem aktualizowanym w chwili t, a \(\Delta_t\) jego przesunięciem. Sumując spadki energii:

\[
\sum_{t=0}^{T}
(|N_{i_t}(x^t)|+2)\Delta_t^2
\le
\Phi_\epsilon(x^0)-\Phi_\epsilon(x^{T+1})
\le
\Phi_\epsilon(x^0).
\]

Po przejściu do granicy:

\[
\boxed{
\sum_{t=0}^{\infty}
(|N_{i_t}(x^t)|+2)\Delta_t^2
\le
\Phi_\epsilon(x^0)
\le
\binom n2\epsilon^2.
}
\]

Ponieważ \(|N_i|+2\ge2\), otrzymujemy również:

\[
\boxed{
\sum_{t=0}^{\infty}\Delta_t^2
\le
\frac12\binom n2\epsilon^2<\infty.
}
\]

W szczególności:

\[
\boxed{\Delta_t\longrightarrow0.}
\]

Jest to prawdziwe niezależnie od:
- okresowości lub losowości harmonogramu;
- uczciwości harmonogramu;
- liczby aktualizacji danego indeksu;
- zmienności grafu progowego.

W dodatku każdy akt jest średnią pewnych aktualnych współrzędnych, więc pozostaje w aktualnym globalnym przedziale. Jeśli:

\[
m_t=\min_i x_i^t,\qquad M_t=\max_i x_i^t,
\]

to:

\[
m_{t+1}\ge m_t,\qquad M_{t+1}\le M_t.
\]

Obie sekwencje są monotoniczne i ograniczone, więc mają granice. Cały wektor pozostaje ograniczony.

### Czego ten wynik jeszcze nie dowodzi?

Zbieżność \(\sum_t\Delta_t^2<\infty\) nie implikuje zbieżności \(\sum_t|\Delta_t|\), a więc sama nie dowodzi, że każde \(x_i^t\) ma granicę. Bounded sequence z przyrostami dążącymi do zera może nadal nie być zbieżna.

To rozróżnienie jest kluczowe. Mamy globalny zanik wielkości pojedynczych aktów, lecz jeszcze nie pełną zbieżność trajektorii.

## 5. Warunek wystarczający: topologia progowa ustala się na stałe

Można natomiast domknąć przypadek, w którym graf progowy od pewnego momentu nie zmienia się.

Załóżmy, że istnieje \(T\) i graf nieskierowany \(G^\ast\), takie że:

\[
G_\epsilon(x^t)=G^\ast
\qquad\forall t\ge T.
\]

Wtedy każdy akt \(C_i\) od chwili T jest już stałym liniowym operatorem wierszowo-stochastycznym: aktualizuje wiersz i do średniej z i oraz jego sąsiadów w \(G^\ast\). Każda waga na zamkniętym sąsiedztwie jest co najmniej \(1/n\).

Załóżmy, że \(G^\ast\) ma składową \(C\) o \(m\) wierzchołkach. Każdy aktualizowany wiersz ma wagę co najmniej \(\alpha=1/n\) na sobie i na każdym sąsiedzie. W dowolnych kolejnych \(B\) aktywacjach każdy wierzchołek jest aktualizowany przynajmniej raz.

Weźmy blok \(mB\) aktywacji i podzielmy go na \(m\) kolejnych podbloków długości B. Dla dowolnego źródłowego wierzchołka \(j\), jego własny wiersz zachowuje dodatni wpływ na początkową wartość \(x_j\), ponieważ każda aktualizacja zachowuje co najmniej współczynnik \(\alpha\) przy własnej dotychczasowej wartości. W każdym kolejnym podbloku wpływ ten może przejść o co najmniej jedną krawędź dalej: w danym podbloku aktualizowany jest każdy wierzchołek, a aktualizacja sąsiada wprowadza do jego wiersza co najmniej \(\alpha\) aktualnego wpływu poprzednika. Po najwyżej \(m-1\) podblokach wpływ źródła dociera do każdego wierzchołka C; w pozostałych aktualizacjach nie znika, bo współczynnik własny jest dodatni.

Wobec tego iloczyn macierzy aktualizacji w takim bloku jest wierszowo-stochastyczny i każdy jego wpis w obrębie C jest co najmniej \(\alpha^{mB}\). Współczynnik ergodyczny tego iloczynu jest więc ściśle mniejszy od 1, a średnica opinii w C kurczy się geometrycznie po kolejnych blokach długości \(mB\). Ponieważ każdy lokalny ruch jest nie większy od bieżącej średnicy C, suma bezwzględnych przesunięć w C jest skończona i każda współrzędna w C ma granicę.

W konsekwencji:
- każda składowa spójności \(G^\ast\) zbiega do jednej wspólnej wartości;
- pary z różnych składowych pozostają oddalone co najmniej o \(\epsilon\);
- granica jest punktem stałym A2, a partycja graniczna jest dokładnie partycją składowych \(G^\ast\).

**Wynik ✅/warunkowo:** przy ustalonej topologii i ograniczenie uczciwym harmonogramie A2 zbiega do stabilnej partycji. Nie wykazaliśmy jeszcze, że topologia musi ustalić się po skończonym czasie.

## 6. Związek z istniejącą literaturą

Reguła P₀-Scalar jest bliska asynchronicznemu modelowi Hegselmanna–Krausego na pełnym grafie społecznym: w każdej chwili aktualizuje się jeden agent, który uśrednia własną wartość i wartości aktualnych sąsiadów w zasięgu zaufania.

Berenbrink, Hoefer, Kaaser, Lenzner, Rau i Schmand, *Asynchronous Opinion Dynamics in Social Networks* (Distributed Computing, 2024), analizują ten model dla losowego wyboru agenta. Dla pełnego grafu podają ograniczenie oczekiwanego czasu dojścia do stanu \(\delta\)-stabilnego rzędu:

\[
O\!\left(n^3\left(n^2+(\epsilon/\delta)^2\right)\right).
\]

Ich \(\delta\)-stabilność oznacza, że wszystkie aktualne krawędzie wpływu mają długość co najwyżej \(\delta\); nie jest to to samo co dokładny punkt stały. Autorzy podkreślają też, że dokładny stan, w którym żaden agent nie zmienia opinii, może nie zostać osiągnięty po skończonej liczbie kroków. Zob. [pełny tekst artykułu](https://arxiv.org/abs/2201.12923) oraz [wersję wydawniczą](https://link.springer.com/article/10.1007/s00446-024-00467-3).

To jest zgodne z naszym rozdzieleniem:
- dokładna stabilność nieosiągalna w skończonym czasie z niestabilnego stanu;
- małe ruchy / \(\delta\)-stabilność mogą pojawić się w skończonym czasie;
- pełna zbieżność wektora wymaga osobnego argumentu.

Uwaga techniczna: literatura często przyjmuje warunek sąsiedztwa \(\le\epsilon\), podczas gdy P₀-Scalar używa \(<\epsilon\). Różnica dotyczy dokładnie przypadków na progu i musi pozostać jawna w porównaniach.

## 7. Nowe rozróżnienie harmonogramów

W dalszym audycie nie należy używać jednego słowa „uczciwy” na określenie różnych warunków:

1. **Uczciwość zwykła:** każdy indeks pojawia się nieskończenie wiele razy.
2. **Uczciwość ograniczona:** istnieje B, tak że każdy indeks pojawia się w każdych B kolejnych aktywacjach.
3. **Aktywacja losowa:** każdy krok wybiera niezależnie indeks z ustalonego rozkładu; przy rozkładzie jednostajnym każdy indeks pojawia się nieskończenie często z prawdopodobieństwem 1, ale odstępy między aktywacjami nie mają wspólnego ograniczenia.

Poprzednie dwa przykłady miały harmonogramy okresowe, czyli należą do klasy uczciwości ograniczonej. Nie uzasadniają same przez się wniosku dla każdego zwykłego harmonogramu uczciwego.

## 8. Werdykt

- **✅** Istnieje dokładna energia \(\Phi_\epsilon\), która nie rośnie przy żadnym pojedynczym akcie A2.
- **✅** Każdy akt obniża ją co najmniej o \((|N_i|+2)\Delta_i^2\).
- **✅** Suma kwadratów wszystkich przesunięć jest ograniczona przez \(\binom n2\epsilon^2/2\); stąd każdy pojedynczy ruch dąży do zera.
- **✅** Globalne minimum jest niemalejące, maksimum nierosnące; oba mają granice.
- **✅/warunkowo** Jeśli topologia progowa ustali się na stałe, a harmonogram jest ograniczenie uczciwy, dynamika zbiega do stabilnej partycji składowych.
- **🔍** Nie wykazano, że topologia progowa ustala się na stałe dla dowolnego uczciwego harmonogramu.
- **🔍** Nie wykazano jeszcze zbieżności każdego wektora trajektorii dla dowolnego zwykłego harmonogramu uczciwego.
- **❌** Z samego zaniku pojedynczych przesunięć nie wolno wnioskować o zbieżności całego wektora.

## 9. Następny test

Najważniejszym otwartym problemem jest teraz skończoność zmian grafu progowego:
- czy graf \(G_\epsilon(x^t)\) może zmieniać się nieskończenie wiele razy przy harmonogramie okresowym;
- czy może to nastąpić przy harmonogramie ograniczenie uczciwym;
- jeśli tak, czy mimo tego wartości współrzędnych zawsze zbiegają, czy istnieje kontrprzykład.

To jest właściwy test przed budowaniem asymptotycznego automatu Scalar.

## 10. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
