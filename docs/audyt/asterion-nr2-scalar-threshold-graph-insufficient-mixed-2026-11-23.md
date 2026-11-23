# N-R2: Scalar — graf progowy nie wystarcza do odtworzenia przyszłych profili

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Źródło:** P₀-Scalar v0.3.5, reguła lokalnego aktu progowego A2; wcześniejsze raporty Asteriona o punktach stałych A2 i profilach resztkowych.  
**Status:** kontrprzykład dla deterministycznego przejścia na samych grafach progowych ✅; kontrprzykład dla przyszłego profilu relacyjnego ✅; pełna klasyfikacja języka osiągania stabilności w skończonym czasie dla mieszanych grafów pozostaje otwarta 🔍.

## 1. Pytanie

Czy przyszłe profile Scalar można odtworzyć z samej relacji progowej:

\[
i\sim_\epsilon j
\iff
|r_i-r_j|<\epsilon,
\]

czy potrzebne są także ilościowe odległości między wartościami?

Jeśli graf progowy \(G_\epsilon(r)\) ma być wystarczającym stanem, to konfiguracje o tym samym grafie powinny po tym samym akcie \(C_i\) dawać ten sam graf następny. Poniższy kontrprzykład pokazuje, że tak nie jest.

## 2. Lokalna reguła i zależność od marginesów

Dla bieżącej konfiguracji \(r\), zbioru sąsiadów:

\[
N_\epsilon(i;r)=\{j\ne i:|r_i-r_j|<\epsilon\},
\]

akt \(C_i\) aktualizuje tylko współrzędną i:

\[
r_i'=
\frac{r_i+\sum_{j\in N_\epsilon(i;r)}r_j}
{1+|N_\epsilon(i;r)|}.
\]

Dla dowolnego \(k\ne i\):

\[
r_i'-r_k=
\frac{(r_i-r_k)+
\sum_{j\in N_\epsilon(i;r)}(r_j-r_k)}
{1+|N_\epsilon(i;r)|}.
\]

O tym, czy po aktualizacji powstanie krawędź \(\{i,k\}\), decyduje moduł tej sumy, a nie tylko początkowa informacja, czy poszczególne pary były sąsiadami.

Graf progowy zapisuje jedynie nierówności typu \(d_{ij}<\epsilon\) lub \(d_{ij}\ge\epsilon\). Nie zapisuje wartości marginesów \(d_{ij}\), które wchodzą do powyższego wzoru.

## 3. Dokładny kontrprzykład: ten sam graf, różny następny graf

Ustalmy:

\[
\epsilon=1,\qquad A=\{0,1,2\}.
\]

Rozważmy dwie konfiguracje:

\[
x=\left(0,\frac25,\frac65\right),
\qquad
y=\left(0,\frac25,\frac{11}{10}\right).
\]

Obie są ściśle rosnące. W obu:

\[
|r_0-r_1|<1,\qquad
|r_1-r_2|<1,\qquad
|r_0-r_2|\ge1.
\]

Dokładniej:

| Para | Konfiguracja \(x\) | Konfiguracja \(y\) |
|---|---:|---:|
| \(0,1\) | \(2/5\) | \(2/5\) |
| \(1,2\) | \(4/5\) | \(7/10\) |
| \(0,2\) | \(6/5\) | \(11/10\) |

Zatem oba grafy progowe są identyczne:

\[
G_\epsilon(x)=G_\epsilon(y)
=\{\{0,1\},\{1,2\}\}.
\]

To jest ścieżka \(0-1-2\), nie pełna klika ani suma rozłącznych klik.

### 3.1. Wykonujemy ten sam akt \(C_0\)

W obu konfiguracjach \(N_\epsilon(0)=\{1\}\). Stąd:

\[
x'=C_0(x)=
\left(\frac15,\frac25,\frac65\right),
\]

\[
y'=C_0(y)=
\left(\frac15,\frac25,\frac{11}{10}\right).
\]

Dla \(x'\):

\[
|x'_0-x'_2|=1,
\]

więc — przy ścisłym warunku sąsiedztwa \(<1\) — krawędź \(\{0,2\}\) nie powstaje. Graf pozostaje ścieżką:

\[
G_\epsilon(x')=\{\{0,1\},\{1,2\}\}.
\]

Dla \(y'\):

\[
|y'_0-y'_2|=\frac9{10}<1,
\]

więc powstaje trzecia krawędź:

\[
G_\epsilon(y')=
\{\{0,1\},\{1,2\},\{0,2\}\}=K_3.
\]

Otrzymaliśmy zatem:

\[
\boxed{
G_\epsilon(x)=G_\epsilon(y)
\quad\text{ale}\quad
G_\epsilon(C_0(x))\ne G_\epsilon(C_0(y)).
}
\]

**Wynik ✅:** przejście A2 nie jest funkcją samego grafu progowego. Graf progowy nie jest wystarczającą statystyką Markowa dla dynamiki Scalar.

## 4. Konsekwencja dla profilu przyszłych kontynuacji

Aby pokazać różnicę na poziomie profili, weźmy relacyjny test przyszłości: czy po danej historii aktywów para \(\{0,2\}\) stanie się krawędzią progową.

Dla ustalonego stanu początkowego \(r\) definiujemy język obserwacji:

\[
\mathcal L_r^{02}
=
\{w\in A^*:
|(T_w(r))_0-(T_w(r))_2|<1\}.
\]

Jest to język zdarzenia relacyjnego, nie zastępcza definicja stabilności całej konfiguracji.

Dla obu stanów początkowych para \(\{0,2\}\) początkowo nie jest krawędzią. Jednak dla jednoaktowej historii \(w=0\):

\[
0\notin\mathcal L_x^{02},
\qquad
0\in\mathcal L_y^{02}.
\]

Wobec tego przyszłe profile początkowe są różne:

\[
F_{\varepsilon,x}^{02}
=\mathcal L_x^{02}
\ne
\mathcal L_y^{02}
=F_{\varepsilon,y}^{02}.
\]

A jednak:

\[
G_\epsilon(x)=G_\epsilon(y).
\]

To jest bezpośredni kontrprzykład dla postulatu, że sam początkowy graf progowy wyznacza przyszły profil relacyjny. Nawet ta sama kolejność wszystkich wartości nie naprawia problemu; różnicę powodują marginesy odległości.

### Zastrzeżenie zakresu

Powyższy test dotyczy przyszłego pojawienia się konkretnej relacji progowej. Nie dowodzi jeszcze, że dla tych dwóch konfiguracji różne są języki:

\[
\mathcal L_{S,r}^{\mathrm{stab}}
=
\{w:T_w(r)\in\mathcal S_\epsilon\},
\]

czyli języki historii osiągających pełną stabilność A2 w skończonej liczbie aktów. Tego silniejszego kontrprzykładu nie uzyskaliśmy w tym rachunku. Nie należy go dopisywać do werdyktu.

Jednak już wykazana różnica kolejnego grafu oznacza, że automat oparty wyłącznie na progowej relacji sąsiedztwa nie może dokładnie odtwarzać wszystkich przyszłych relacji Scalar. Jeżeli chcemy badać wyłącznie osiąganie stabilności, trzeba osobno udowodnić, że utracone marginesy nie wpływają na ten konkretny język.

## 5. Jaki stan jest wystarczający?

Pełne współrzędne \(r\) zawierają więcej informacji, niż potrzeba do dynamiki: globalne przesunięcie i odbicie osi nie zmieniają reguły A2.

Wystarczającym stanem relacyjnym jest natomiast oznaczona macierz wszystkich odległości:

\[
D(r)=(d_{ij}),\qquad d_{ij}=|r_i-r_j|.
\]

Dla konfiguracji punktów na prostej pełna oznaczona macierz odległości rekonstruuje położenia z dokładnością do translacji i globalnego odbicia. Obie symetrie komutują z aktualizacją średnią, więc nie zmieniają przyszłych odległości ani grafów progowych.

Zatem mamy trzy poziomy informacji:

1. **Graf progowy:** tylko informacja \(d_{ij}<\epsilon\) / \(d_{ij}\ge\epsilon\); niewystarczający do dokładnej dynamiki.
2. **Macierz odległości:** zawiera dokładne wielkości relacyjne; wystarczająca do odtworzenia przyszłej dynamiki z dokładnością do izometrii prostej.
3. **Wektor współrzędnych:** wystarczający, ale zawiera arbitralną translację i orientację osi.

W Scalar relacyjność może więc usunąć absolutne położenie, lecz nie może w tym rachunku usunąć ilościowej informacji o odległościach.

## 6. Co z tego wynika dla N-R2?

Nie możemy utożsamiać profilu Scalar z samą partycją progową. Partycja mówi, które pary są aktualnie bliskie, lecz nie mówi, jak blisko są ani czy kolejny akt przekroczy próg.

Jeśli profil ma być stanem wystarczającym do przewidywania przyszłych aktów, musi zachowywać więcej niż graf progowy. Minimalnym bezpiecznym nośnikiem w obecnym formalizmie jest klasa konfiguracji wyznaczona przez pełną oznaczoną macierz odległości, z utożsamieniem translacji i odbicia.

To jest istotna różnica względem Centroidu, gdzie przyszły profil słowa zależy wyłącznie od zbioru użytych indeksów. W Scalar przyszłość zależy od ciągłych marginesów odległości, a nie tylko od kombinatorycznego wzorca sąsiedztwa.

Nie pojawia się tu selektor czterech. Przeciwnie: przejście do samego grafu progowego usuwa informację potrzebną do dokładnej ewolucji niezależnie od liczby współrzędnych.

## 7. Werdykt

- **✅** Dwie różne konfiguracje o identycznym grafie progowym i tej samej kolejności współrzędnych mogą po tym samym akcie A2 dać różne grafy następne.
- **✅** Graf progowy nie jest wystarczającym stanem Markowa dla lokalnej dynamiki Scalar.
- **✅** Dla relacyjnego testu pojawienia się krawędzi \(\{0,2\}\) skonstruowano dwa różne profile przyszłości przy tym samym początkowym grafie.
- **✅** Pełna oznaczona macierz odległości jest wystarczającym stanem relacyjnym z dokładnością do translacji i odbicia.
- **🔍** Nie dowiedziono jeszcze, że język osiągania stabilności w skończonej liczbie aktów różni się dla skonstruowanej pary stanów.
- **❌** Nie można zredukować dokładnej dynamiki Scalar do samej binarnej relacji progowej bez utraty informacji o przyszłych relacjach.
- **💡** Możliwy wspólny język P₀ powinien odróżniać relacyjną strukturę jakościową od ilościowej miary jej marginesów; sama zgodność/niezgodność par nie wystarczy.

## 8. Następny test

Następnie trzeba rozstrzygnąć silniejsze pytanie: czy język osiągania stabilności A2 w skończonym czasie jest już wyznaczony przez klasę konfiguracji modulo odległości, czy też istnieje para stanów o tym samym grafie progowym, dla których konkretny skończony ciąg aktów prowadzi do stabilności tylko w jednym przypadku.

Równolegle warto sprawdzić, czy w P₀-Relacje istnieje pojęcie relacyjnego marginesu, które nie zakłada z góry metryki euklidesowej, ale zachowuje informację potrzebną do przejścia przez próg.

## 9. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
