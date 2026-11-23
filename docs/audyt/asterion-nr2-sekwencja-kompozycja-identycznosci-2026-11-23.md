# N-R2: sekwencyjność, kompozycja i lokalne identyczności — czego nie da się wyprowadzić z samego czasu

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. Bez zmian w MVP-02.  
**Punkt wyjścia:** P₀-Relacje v0.3 §§1–12; P₀-TAU v1.7.2 §§1.1, 7.3–7.4; P₀-Flow v0.5.3 §§2–4; P₀-Centroid v5.2-zmiany; wcześniejszy model algebry relacji Asteriona.  
**Status:** sekwencja operatorów daje kompozycję ✅; sama sekwencja nie daje wielu lokalnych identyczności ✅ (kontrmodele); TAU nie wyprowadza jeszcze struktury kategorii ani algebry relacji pierwotnej ℛ 💡/otwarte.

## 1. Pytanie

Poprzedni raport zaproponował algebra relacji z kompozycją, konwersją i wyróżnioną identycznością 1′. Profile można w niej zdefiniować jako atomy pod 1′.

Teraz trzeba rozstrzygnąć, czy te operacje wynikają z już istniejącej w P₀ tezy „relacja jest sekwencyjna — kto mówi, kto słucha, kiedy”, czy też są dodatkowymi założeniami.

Kluczowe rozróżnienie:

1. **Kompozycja czasowa:** wykonanie jednego kroku po drugim.
2. **Identyczność globalna:** brak kroku / pusty ciąg działań.
3. **Identytety lokalne:** jednostki przypisane poszczególnym profilom/obiektom.
4. **Konwersja relacji:** zamiana kolejności argumentów relacji.
5. **Odwrotność procesu:** operacja, która cofa konkretną ewolucję.

Tych pojęć nie wolno utożsamiać.

## 2. Co rzeczywiście daje sekwencyjność

Jeżeli mamy alfabet już określonych operacji Σ, to ciągi operacji tworzą półgrupę wolną Σ⁺ z konkatenacją:

\[
(u,v)\mapsto uv.
\]

Konkatenacja jest łączna:

\[
(uv)w=u(vw).
\]

Jeżeli dopuścimy pusty ciąg ε, dostajemy monoid Σ* z globalnym elementem neutralnym:

\[
\varepsilon w=w\varepsilon=w.
\]

To jest poprawny formalny model sekwencji. Ale nie zawiera automatycznie wielu lokalnych jednostek.

### Lemat 1. Wolny monoid ma tylko jedną idempotentną jednostkę

W monoidzie wolnym Σ* jedynym idempotentem jest pusty ciąg ε.

**Dowód.** Jeśli w²=w, to długości spełniają 2|w|=|w|, zatem |w|=0 i w=ε. ∎

W konsekwencji, nawet gdy alfabet Σ ma cztery symbole, sama konkatenacja nie wyprowadza czterech profili jako idempotentów. Cztery symbole są wejściem modelu, a jedyną jednostką jest ε.

Co więcej, wynik nie zależy od liczby symboli: to samo zachodzi dla dwóch, trzech, czterech i dowolnej liczby generatorów.

## 3. Odwracalne operatory Centroidu dają grupę z jedną idempotentną jednostką

W Centroidzie operator aktualizacji ma postać:

\[
M_i=I+e_i c_i^T,
\qquad c_i=\frac1n\mathbf1-e_i.
\]

Z lematu o wyznaczniku macierzy rzędu jeden:

\[
\det M_i=1+c_i^Te_i
=1+\left(\frac1n-1\right)
=\frac1n.
\]

Dla n=4:

\[
\det M_i=\frac14\ne0.
\]

Każde M_i jest więc odwracalne. Grupa Γ generowana przez M_i i ich odwrotności składa się z operatorów odwracalnych.

W dowolnej grupie jedynym idempotentem jest identyczność:

\[
g^2=g
\implies g=e.
\]

**Wniosek dla Centroidu:** jeśli za profile miałyby uchodzić idempotenty grupy operatorów wygenerowanej przez M_i, otrzymamy tylko jeden profil — globalną identyczność I. Same cztery operatory M_i nie są czterema lokalnymi identycznościami.

To nie rozstrzyga, jakie idempotenty mogą pojawić się w dodatniej półgrupie słów bez odwrotności. Rozstrzyga natomiast, że grupa odwracalnych transformacji nie dostarcza wielu lokalnych jednostek.

## 4. Sekwencja aktualizacji TAU nie jest jeszcze kompozycją relacji

P₀-TAU v1.7.2 definiuje rundę:

\[
R_\sigma(\alpha)
=M_{\sigma(n)}(\alpha)\cdots M_{\sigma(1)}(\alpha).
\]

To jest rzeczywista kompozycja operatorów. Kolejność ma znaczenie, a TAU dowodzi m.in. sprzężenia permutacyjnego:

\[
R_\sigma=P_\sigma R_{\rm id}P_\sigma^{-1}.
\]

Ale w tym formalizmie:
- przestrzeń stanów jest już zadana jako ℝⁿ;
- operatory M_i są już zadane;
- indeksy aktualizacji są już zadane;
- harmonogram σ jest wyborem kolejności zewnętrznej wobec pojedynczej rundy;
- runda bez aktualizacji daje globalne I, nie rodzinę lokalnych jednostek.

Dodatkowo sam dokument TAU §1.1 kwalifikuje aksjomat sekwencyjności jako fenomenologiczny, motywacyjny i niefalsyfikowalny w tym dokumencie. To uczciwa motywacja do wyboru klasy dynamik, ale nie aksjomat algebraiczny, z którego wolno wyprowadzić kompozycję relacji, lokalne identyczności albo liczbę profili.

## 5. Flow używa dynamiki biliniowej, nie kompozycji relacyjnej

P₀-Flow v0.5.3 przyjmuje:

\[
R_{ij}=u_j-u_i,\qquad R\in C^1(K_n),
\]

a następnie definiuje operator biliniowy T(R;R) i ewolucję:

\[
\dot R=T(R;R)-\nu LR-dp+F_R.
\]

To jest dynamika na przestrzeni krawędzi już zadanego kompleksu symplicjalnego. T(R;R) jest operatorem biliniowym na współrzędnych relacyjnych, nie kompozycją dwóch relacji typu „x pozostaje w R z y, a y w S z z”.

Zatem Flow nie dostarcza jeszcze brakującej operacji kompozycji w sensie algebry relacji. Dostarcza inny, wartościowy formalizm ewolucji relacyjnej, którego nośnik C¹(K_n) jest jednak już określony przez K_n.

## 6. Konwersja relacji nie jest odwrotnością procesu

W algebrze relacji konwersja R⁻¹ zamienia pary:

\[
(x,y)\in R
\iff (y,x)\in R^{-1}.
\]

To nie oznacza, że proces opisany przez R można odwrócić w czasie.

Przykład. Niech:

\[
R=\{(a,b),(a,c)\}.
\]

Wtedy:

\[
R^{-1};R
=\{(b,b),(b,c),(c,b),(c,c)\},
\]

co nie jest relacją identyczności na {a,b,c}. Konwersja odwraca kierunek par, lecz nie daje odwrotności relacji w sensie kompozycji.

Podobnie odwracalność macierzy M_i nie oznacza, że historyczna relacja „kto mówił, kto słuchał, kiedy” ma automatyczny, fizycznie dopuszczalny proces odwrotny. Odwrotność operatora liniowego, konwersja relacji i odwrócenie czasu to trzy różne pojęcia.

## 7. Nawet pełna kategoria z lokalnymi identycznościami nie wybiera czterech

Możemy dać sekwencyjności mocniejszą strukturę niż monoid: kategorię z częściową kompozycją i lokalnymi identycznościami.

Dla dowolnego n≥1 zbudujmy kategorię parową (pair groupoid):

- obiekty: X, gdzie |X|=n;
- dokładnie jeden morfizm f_{xy}:x→y dla każdej pary x,y;
- kompozycja: f_{yz}∘f_{xy}=f_{xz};
- identyczność obiektu x: 1_x=f_{xx};
- odwrotność: f_{xy}^{-1}=f_{yx}.

Lokalne identyczności 1_x są dokładnie idempotentami kategorii. Profile definiujemy jako te identyczności, a więc:

\[
|P|=n.
\]

Automorfizmy tej kategorii permutują obiekty i są dokładnie:

\[
\operatorname{Aut}(\mathcal C_n)\cong S_n.
\]

Otrzymujemy zatem dla każdego n:
- sekwencyjną kompozycję;
- lokalne jednostki;
- odwracalne strzałki;
- wierną i przechodnią symetrię S_n;
- dowolną liczbę profili n.

To jest mocny kontrmodel: nawet przejście od zwykłej sekwencji do pełnej struktury grupoidowej nie wymusza czterech.

Dla n=4 grupa S₄ ma normalną V₄, która działa regularnie na czterech obiektach. Dla n=5,6 i dalej liczba profili jest jednak odpowiednio 5,6,…, a analogiczna struktura kategorii nadal spełnia wszystkie aksjomaty kompozycji i lokalnych identyczności.

## 8. Co trzeba dodać, by lokalne jednostki nie były ukrytymi węzłami

W kategorii lokalne jednostki są obiektami w przebraniu. Można je odzyskać jako idempotenty z własnościami lokalnego działania, ale sam zbiór lokalnych jednostek i reguła częściowej kompozycji muszą być już określone.

Jeżeli P₀ chce naprawdę wyprowadzić je z relacji, musi podać obiekt wcześniejszy niż kategoria. Kandydat powinien składać się z:
1. surowych zdarzeń/relacji, bez jawnego zbioru źródeł i celów;
2. wewnętrznego kryterium, kiedy dwa zdarzenia są kompozytowalne;
3. operacji składania, która jest łączna na dopuszczalnych ciągach;
4. reguły stabilizacji, z której lokalne jednostki pojawiają się jako niezerowe idempotenty;
5. dowodu, że te idempotenty są nierozkładalne i nie są tylko zapisanymi etykietami obiektów.

Punkt 2 jest newralgiczny. Jeżeli kompozytowalność wymaga „koniec pierwszej relacji = początek drugiej”, to pojęcia końca i początku są już typowaniem relacji. To może być poprawny formalizm, ale nie jest jeszcze wyprowadzeniem nośnika z relacji bez obiektów.

## 9. Minimalne kontrmodele dla każdej proponowanej wersji

| Formalizm | Profile/idempotenty | Liczba |
|---|---|---:|
| Wolny monoid Σ* | idempotenty | 1 |
| Grupa operatorów odwracalnych | idempotenty | 1 |
| Półkrata (P([n]), ∩) | wszystkie elementy idempotentne | 2ⁿ |
| Pair groupoid | lokalne identyczności | n |
| Pełna algebra relacji na X | atomy pod identycznością | n |

Żaden z tych ogólnych formalizmów nie wymusza n=4.

Kandydat na selektor pozostaje bardziej szczegółowy: odpowiednia charakterystyczna podgrupa automorfizmów ma działać regularnie na atomach identyczności. Samo sekwencyjne składanie nie daje tej własności.

## 10. Wnioski z porównania korzeni

### P₀-Relacje v0.3

§1 deklaruje relację jako poziom pierwotny, §6 postuluje R_{t+1}=F(R_t), ale F i operacje D(·), C(·) pozostają niezdefiniowane. §7 i §8 wprowadzają V oraz E⊆V×V. N-R2 jest więc realną luką w definicji nośnika.

### P₀-TAU v1.7.2

Daje ścisłą teorię kolejności aktualizacji, kompozycji operatorów M_i i wpływu kolejności na konsensus. Aksjomat sekwencyjności §1.1 jest jednak jawnie fenomenologiczny, nie dowodowy. TAU nie wyprowadza lokalnych identyczności ani typu kategorii.

### P₀-Flow v0.5.3

Daje biliniową dynamikę na C¹(K_n), a nie kompozycję relacji między profilami. Używa K_n i jego indeksów jako danych wejściowych.

### P₀-Centroid v5.2

Operatory M_i są odwracalne, a ich grupa ma jedną idempotentną jednostkę. Cztery M_i są czterema wyróżnionymi generatorami, nie czterema lokalnymi identycznościami.

## 11. Werdykt

- **✅** Sekwencja kroków z konkatenacją daje łączną kompozycję.
- **✅** Pusty ciąg daje jedną globalną jednostkę monoidu.
- **✅** Wolny monoid ma tylko jeden idempotent.
- **✅** Grupa odwracalnych operatorów Centroidu ma tylko jeden idempotent — globalne I.
- **✅** Konwersja relacji nie jest odwrotnością procesu ani odwróceniem czasu.
- **✅** Kategoria/grupoid z lokalnymi identycznościami może mieć dowolne n obiektów i grupę automorfizmów S_n.
- **❌** Sama sekwencyjność nie wyprowadza wielu lokalnych identyczności ani liczby cztery.
- **🔍** TAU daje kompozycję operatorów, ale harmonogram i nośnik są już zadane.
- **💡** Możliwa jest konstrukcja pierwotnej semigruppy częściowo kompozytowalnych relacji, w której lokalne jednostki są rekonstruowane z idempotentów.
- **💡** Regularne działanie V₄ na tych jednostkach może wybierać cztery, lecz nie wynika z samego aksjomatu sekwencyjności.

**Wniosek:** algebra relacji jest nadal najlepszym kandydatem na pośredni formalizm, ale nie można jej uzasadnić samym „kto mówi, kto słucha, kiedy”. Sekwencja daje porządek i kompozycję; lokalna identyczność wymaga struktury kompozytowalności; liczba cztery wymaga jeszcze niezależnego selektora. Każdy z tych poziomów musi zostać wyprowadzony osobno.

## 12. Następny krok

Następne zadanie to skonstruować semigroupoid bez jawnie podanego zbioru obiektów: elementarne relacje mają być łączone tylko wtedy, gdy ich wewnętrzne granice są zgodne. Następnie sprawdzić, czy lokalne jednostki można odzyskać jako minimalne idempotenty bez dodawania wprost etykiet źródła/celu. Kontrmodele z 1, 2, 3, 5 i 6 jednostkami muszą pozostać dopuszczalne aż do momentu, w którym konkretny aksjomat P₀ je wykluczy.

## 13. Integralność repo

Raport zapisano wyłącznie na gałęzi audit/asterion-continuation-2026-11-20. main pozostaje nietknięty; nie wykonano merge ani rebase. MVP-02 pozostaje poza zakresem.
