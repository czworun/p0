# N-R2: Scalar — zakaz osiągnięcia stabilności w skończonej sekwencji A2

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Źródło:** P₀-Scalar v0.3.5, lokalna reguła progowa A2; raporty Asteriona o punktach stałych A2 oraz niewystarczalności grafu progowego.  
**Status:** lemat wstecznej niezmienniczości zbioru stabilnego dla każdego lokalnego aktu ✅; brak skończonego wejścia do stabilności z konfiguracji niestabilnej ✅; język skończonego osiągnięcia stabilności jest trywialny ✅; dynamika i profile asymptotyczne pozostają otwarte 🔍.

## 1. Pytanie

W poprzednim audycie pokazano, że dla części mieszanych grafów progowych język historii osiągających stabilność w skończonym czasie jest trywialny. Teraz sprawdzamy, czy to przypadek szczególny, czy prawo całego lokalnego A2.

Niech \(\epsilon>0\), \(r\in\mathbb R^n\), a lokalny akt \(C_i\) aktualizuje wyłącznie współrzędną i:

\[
N_\epsilon(i;r)=
\{j\ne i:|r_i-r_j|<\epsilon\},
\]

\[
(C_i(r))_k=
\begin{cases}
r_k,&k\ne i,\\[1mm]
\displaystyle
\frac{r_i+\sum_{j\in N_\epsilon(i;r)}r_j}
{1+|N_\epsilon(i;r)|},&k=i.
\end{cases}
\]

Zbiór stabilny pełnej rundy A2 ma postać:

\[
\mathcal S_\epsilon=
\{r:\forall i,j,\ |r_i-r_j|<\epsilon
\Rightarrow r_i=r_j\}.
\]

Pytanie brzmi: czy może istnieć \(r\notin\mathcal S_\epsilon\), dla którego pojedynczy akt albo skończony ciąg aktów daje stan w \(\mathcal S_\epsilon\)?

## 2. Lemat: każdy lokalny akt jest wstecznie niezmienniczy względem stabilności

**Twierdzenie.** Dla każdego \(i\):

\[
\boxed{
C_i^{-1}(\mathcal S_\epsilon)=\mathcal S_\epsilon.
}
\]

Równoważnie:

\[
C_i(r)\in\mathcal S_\epsilon
\iff
r\in\mathcal S_\epsilon.
\]

### Dowód

Niech \(s=C_i(r)\in\mathcal S_\epsilon\), a \(z=s_i\). Dla każdego \(k\ne i\) współrzędna nie ulega zmianie:

\[
s_k=r_k.
\]

Jeżeli \(N_\epsilon(i;r)=\varnothing\), to \(z=r_i\), więc \(s=r\) i teza jest natychmiastowa.

Załóżmy zatem, że zbiór sąsiadów jest niepusty. Mamy:

\[
z=
\frac{r_i+\sum_{j\in N_\epsilon(i;r)}r_j}
{1+|N_\epsilon(i;r)|}.
\]

Przypuśćmy, że \(r_i>z\). Weźmy dowolny \(j\in N_\epsilon(i;r)\). Ponieważ \(s\) jest stabilny i \(s_j=r_j\), zachodzi:

\[
|r_j-z|<\epsilon\Rightarrow r_j=z.
\]

W szczególności nie może być \(r_j<z\). Gdyby bowiem \(r_j<z\), stabilność dawałaby \(z-r_j\ge\epsilon\), a więc:

\[
r_i-r_j=(r_i-z)+(z-r_j)>\epsilon,
\]

co przeczy \(j\in N_\epsilon(i;r)\). Zatem każdy sąsiad spełnia \(r_j\ge z\).

Średnia liczby \(r_i>z\) oraz liczb \(r_j\ge z\) musi być ściśle większa od \(z\). Przeczy to definicji \(z\). Analogicznie przypadek \(r_i<z\) prowadzi do sprzeczności: wszyscy sąsiedzi musieliby spełniać \(r_j\le z\), więc średnia byłaby ściśle mniejsza od \(z\).

Pozostaje zatem \(r_i=z\). Wszystkie pozostałe współrzędne również są niezmienione, więc \(r=s\). Stąd \(r\in\mathcal S_\epsilon\).

Implikacja odwrotna jest prosta: jeśli \(r\) jest stabilny, każdy jego sąsiad progowy ma tę samą wartość co \(r_i\), zatem \(C_i(r)=r\). ∎

## 3. Wniosek: skończona sekwencja nie może osiągnąć stabilności

Niech \(w=i_1\cdots i_m\) będzie dowolnym skończonym słowem aktów, a:

\[
T_w=C_{i_m}\circ\cdots\circ C_{i_1}.
\]

Jeżeli \(T_w(r)\in\mathcal S_\epsilon\), to z lematu, stosowanego wstecz do ostatniego aktu, stan bezpośrednio przed nim również należał do \(\mathcal S_\epsilon\). Powtarzając argument dla wszystkich wcześniejszych aktów, otrzymujemy:

\[
T_w(r)\in\mathcal S_\epsilon
\Rightarrow r\in\mathcal S_\epsilon.
\]

Odwrotna implikacja wynika z tego, że każdy akt pozostawia stan stabilny bez zmian. W konsekwencji:

\[
\boxed{
T_w(r)\in\mathcal S_\epsilon
\iff
r\in\mathcal S_\epsilon
\quad\text{dla każdego skończonego }w.
}
\]

To twierdzenie nie zależy od:
- liczby współrzędnych;
- początkowego grafu progowego;
- kolejności aktualizacji;
- tego, czy graf zmienia się wewnątrz sekwencji;
- istnienia pełnej rundy, która aktualizuje każdy indeks dokładnie raz.

Wystarczy lokalna reguła A2 i stabilność zdefiniowana przez próg \(\epsilon\).

## 4. Język stabilności i profile resztkowe

Dla ustalonego stanu początkowego \(r\) zdefiniujmy język skończonego osiągnięcia stabilności:

\[
\mathcal L_{S,r}^{\mathrm{stab}}
=
\{w\in A^*:T_w(r)\in\mathcal S_\epsilon\}.
\]

Z twierdzenia:

\[
\boxed{
\mathcal L_{S,r}^{\mathrm{stab}}
=
\begin{cases}
A^*,&r\in\mathcal S_\epsilon,\\
\varnothing,&r\notin\mathcal S_\epsilon.
\end{cases}
}
\]

Zatem:
- dla stanu stabilnego wszystkie historie są akceptowane, a wszystkie resztkowe profile są identyczne;
- dla stanu niestabilnego żadna skończona historia nie jest akceptowana, więc nie istnieje żywy profil przyszłości względem tego kryterium.

**Wynik ✅:** finite-time reachability stabilności nie daje nietrywialnego automatu przyszłych kontynuacji w Scalar. Wcześniejsze przykłady dla pełnych klastrów i jednej kliki były szczególnymi przypadkami ogólnego prawa.

Nie oznacza to, że dynamika jest nieruchoma lub że konfiguracja niestabilna nie może zbliżać się do zbioru stabilnego. Oznacza wyłącznie, że nie może wejść do niego po skończonej liczbie lokalnych aktów.

## 5. Oddzielenie profili statycznych od profili dynamicznych

Z wcześniejszego wyniku wiadomo, że zbiór stabilny \(\mathcal S_\epsilon\) zawiera konfiguracje odpowiadające wszystkim partycjom indeksów. Dla \(n=4\) jest ich \(B_4=15\).

Nie wolno jednak utożsamiać tych 15 statycznych profili z 15 stanami automatu przyszłości:
- statyczna partycja opisuje relację równości w już stabilnej konfiguracji;
- profil resztkowy historii opisuje zbiór przyszłych kontynuacji spełniających wskazany test;
- przy teście skończonego osiągnięcia stabilności automat ma wyłącznie przypadek trywialny \(A^*\) albo pusty język.

Liczba Bella opisuje geometrię zbioru punktów stałych, nie liczbę dynamicznych stanów resztkowych.

## 6. Związek z niewystarczalnością grafu progowego

W osobnym raporcie podano dwie konfiguracje o tym samym początkowym grafie progowym:

\[
x=(0,2/5,6/5),\qquad
y=(0,2/5,11/10),\qquad \epsilon=1.
\]

Obie mają graf ścieżki \(0-1-2\), ale po tym samym akcie \(C_0\) jedna zachowuje ścieżkę, a druga przechodzi do \(K_3\).

Wniosek pozostaje ważny: graf progowy nie jest wystarczającym stanem do odtworzenia całej przyszłej dynamiki ani wszystkich zdarzeń relacyjnych. Jednocześnie obecne twierdzenie pokazuje, że kryterium skończonego osiągnięcia stabilności nie rozróżnia tych trajektorii — w obu przypadkach język akceptacji jest pusty, bo oba stany początkowe są niestabilne.

To ważne rozdzielenie:
- przyszłe grafy relacji zależą od ilościowych marginesów odległości;
- skończone osiągnięcie stabilności jest niemożliwe niezależnie od tych marginesów.

## 7. Co pozostaje otwarte: stabilność asymptotyczna

Możliwa jest sytuacja:

\[
r^{(m)}\notin\mathcal S_\epsilon
\quad\text{dla każdego skończonego }m,
\qquad
r^{(m)}\longrightarrow r^\ast\in\mathcal S_\epsilon.
\]

Lemat nie wyklucza takiego zbiegania. Aby zdefiniować nietrywialny język Scalar oparty na stabilności asymptotycznej, trzeba określić co najmniej:
1. klasę dopuszczalnych nieskończonych harmonogramów aktów;
2. warunek uczciwości harmonogramu (np. każdy indeks aktualizowany nieskończenie wiele razy);
3. rodzaj zbieżności i kryterium stabilnego profilu granicznego;
4. czy rozróżniamy granice identyczne, czy także orbity/klasy graniczne.

To nie jest kosmetyczna zmiana definicji. Przechodzimy z języka skończonych słów \(A^*\) do języka nieskończonych trajektorii \(A^\omega\) i analizy granic.

## 8. Werdykt

- **✅** Stabilny zbiór A2 jest wstecznie niezmienniczy względem każdego lokalnego aktu: \(C_i^{-1}(\mathcal S_\epsilon)=\mathcal S_\epsilon\).
- **✅** Żadna skończona sekwencja lokalnych aktualizacji nie przenosi stanu niestabilnego do stabilnego.
- **✅** Język skończonego osiągnięcia stabilności jest dokładnie \(A^*\) dla stanu już stabilnego i \(\varnothing\) dla stanu niestabilnego.
- **✅** Wynik obejmuje wszystkie początkowe grafy progowe, także mieszane; nie wymaga zamrożenia grafu ani określonego harmonogramu.
- **✅** Statyczne partycje stabilne nie są automatycznie dynamicznymi profilami resztkowymi.
- **🔍** Asymptotyczne osiąganie stabilnych profili pozostaje otwarte; wymaga analizy nieskończonych harmonogramów i granic trajektorii.
- **❌** Skończona kompozycja aktów nie może być mechanizmem wyłaniania stabilnego profilu Scalar z niestabilnego stanu początkowego.

## 9. Następny test

Następny krok to przejście do dynamiki nieskończonych harmonogramów A2: sprawdzić, czy dla harmonogramu okresowego lub uczciwego trajektoria zawsze zbiega do \(\mathcal S_\epsilon\), czy istnieją oscylacje/zmiany grafu i czy graniczna partycja jest jednoznaczna.

Dopiero tam może powstać nietrywialny język przyszłości dla Scalar. Nie należy go konstruować przez sztuczne uznanie skończonego fragmentu za „prawie stabilny”.

## 10. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
