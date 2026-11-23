# N-R2: slady bez nosnika — granica swiadka i no-go kompozycji

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. Bez zmian w MVP-02.  
**Punkt wyjścia:** P₀-Relacje v0.3, nota N-R2 (§7); raporty Asteriona o rekonstrukcji profili z semigroupoidu oraz kompozytowalności jako zgodności wewnętrznej; rozliczenie warsztatu Vibe'a z 2026-11-23.  
**Pytanie testowe:** czy świadek kompozycji dwóch relacji i jego zgodność dla trzech relacji dają się zdefiniować wyłącznie z własnych, wewnętrznych śladów relacji, bez ukrytego nośnika i bez uprzedniego rozróżnienia pozycji?  
**Status:** no-go dla śladów bez tożsamości wspólnych interfejsów — **✅ w ramach jawnie podanych założeń**; zgodność typów śladów nie wystarcza do kompozycji — **✅**; łączność nie wynika z samego predykatu zgodności par — **✅**; możliwość wyprowadzenia brakującej struktury z P₀ pozostaje **💡/otwarta**.

## 1. Rozdzielenie pytania

Nie badamy ponownie, czy relacje na zadanym wspólnym nośniku można składać. To zostało już rozliczone: kompozycja relacyjna ma mocną łączność, a świadek jest elementem pośrednim wspólnego nośnika.

Teraz usuwamy właśnie to, co tamten formalizm zakładał.

Nie wolno w definicji użyć:
- wspólnego zbioru pozycji X;
- funkcji źródła lub celu;
- wspólnego elementu x jako świadka;
- etykiety, która tylko zmienia nazwę pozycji, ale zachowuje jej tożsamość między relacjami.

Dopuszczamy jedynie ślady przypisane osobno każdej relacji. Trzeba odróżnić trzy poziomy:
1. **typ śladu** — jego strukturę z dokładnością do izomorfizmu;
2. **konkretny egzemplarz śladu** — określony obiekt, który może być współdzielony przez różne relacje;
3. **świadka sklejenia** — dane uzasadniające, że konkretny koniec jednego śladu i konkretny początek drugiego są tym samym interfejsem.

Poziom 2 zawiera już tożsamość między wystąpieniami. Tożsamość może być anonimowa i nieetykietowana, ale nadal jest strukturą wspólnego nośnika.

## 2. Twierdzenie: izomorfizm śladów nie daje świadka wspólności

Niech T+(a) oznacza wewnętrzny ślad końcowy relacji a, a T-(b) ślad początkowy relacji b. Załóżmy, że dane dostępne dla reguły kompozycji obejmują wyłącznie izomorfizmowe typy tych śladów, a nie tożsamość ich egzemplarzy.

Wówczas reguła
`a C b iff T+(a) ≅ T-(b)`
może rozpoznawać zgodność typu, ale nie może rozstrzygnąć, czy oba ślady są jednym i tym samym interfejsem.

**Dowód przez nierozróżnialność.** Weźmy dwa rozłączne, izomorficzne egzemplarze u i v tego samego śladu. W modelu I koniec a i początek b są jednym egzemplarzem u. W modelu II koniec a jest u, a początek b jest odrębnym egzemplarzem v. Wszystkie dane zachowane wyłącznie do izomorfizmu są w obu modelach takie same. Reguła zależna wyłącznie od tych danych musi więc dać ten sam wynik. Nie może jednocześnie poprawnie odróżnić wspólnego interfejsu od dwóch odrębnych, lecz izomorficznych interfejsów. ∎

Wniosek nie zależy od etykietowania. Nawet gdy oba egzemplarze są anonimowe, ich współdzielenie albo rozłączność jest dodatkową informacją.

**Konsekwencja:** zgodność strukturalna ≅ nie jest tożsamością interfejsu. Jeśli reguła wymaga równości konkretnych egzemplarzy, to egzemplarze te są już ukrytymi pozycjami/nośnikiem. Jeśli wymaga jedynie izomorfizmu, dopuszcza fałszywe sklejenia.

## 3. Czy izomorfizm może być świadkiem?

Można próbować wzmocnić regułę: świadkiem niech będzie konkretny izomorfizm phi: T+(a) → T-(b).

To nie rozwiązuje problemu automatycznie.

1. Sam wybór phi jest dodatkową daną, której nie wyznacza klasa izomorfizmu.
2. Jeżeli ślad ma nietrywialne automorfizmy, izomorfizmów może być wiele.
3. Dla trzech relacji a,b,c izomorfizmy użyte przy sklejeniu a z b oraz b z c muszą być zgodne na wspólnym śladzie b.
4. Aby wynik nie zależał od nawiasowania, trzeba dodatkowo wymagać, by złożony identyfikator dla a,b,c był taki sam w obu kolejnościach.

Warunek 4 jest już warunkiem koherencji sklejeń. Nie wynika z samego istnienia izomorfizmów par.

Można więc skonstruować formalizm z interfejsami, izomorfizmami i koherencją. Nie jest to jednak formalizm bez dodatkowej struktury: jego dane zawierają interfejsy i regułę ich identyfikacji. To uczciwy kandydat na nowy aksjomat, nie wyprowadzenie z samego słowa „relacja”.

## 4. Test trzech relacji: zgodność par nie implikuje łączności

Nawet jeśli predykat C(a,b) jest już dany, sama informacja, które pary są zgodne, nie określa wyniku kompozycji ani nie wymusza łączności.

Kontrprzykład jest całkowity, więc tym mocniej pokazuje lukę. Niech A={0,1}, a produkt będzie zdefiniowany przez
`x ⋆ y = x(1-y)`.
Wszystkie pary są dopuszczalne, zatem predykat kompozytowalności jest stały: C(x,y) zachodzi dla każdego x,y z A.

Dla trójki (1,0,1):
`(1 ⋆ 0) ⋆ 1 = 1 ⋆ 1 = 0`,
natomiast
`1 ⋆ (0 ⋆ 1) = 1 ⋆ 0 = 1`.
Zatem obie strony są różne.

Łączność nie wynika z samej zgodności par. Trzeba zadać dodatkową regułę wyniku kompozycji oraz aksjomat koherencji/łączności, albo wyprowadzić je z mocniejszej struktury świadków.

## 5. Co dokładnie musiałby spełniać świadek trójkowy

Minimalna specyfikacja, która nie przemyca od razu źródła i celu, powinna zawierać:

- dane śladu s(a) przypisane relacji a, bez odwołania do zewnętrznego X;
- regułę wyznaczania świadka w(a,b) wyłącznie z danych śladów;
- jednoznaczny wynik a∘b albo jawne uzasadnienie, dlaczego wynik może być niejednoznaczny;
- dla każdej trójki, dla której oba nawiasowania mają sens, koherencję świadków: w(a,b), w(a∘b,c) oraz w(b,c), w(a,b∘c) muszą indukować ten sam złożony ślad/identyfikację;
- warunek, że definicja w nie używa wspólnego identyfikatora pozycji, ukrytego indeksu ani wcześniej zadanego obiektu granicznego.

Ostatni warunek jest najtrudniejszy. Jeżeli świadek ma wskazać „ten sam” fragment w dwóch różnych relacjach, trzeba wyjaśnić, co ustanawia tę samą tożsamość. Sama zgodność kształtu nie wystarcza.

## 6. Trzy możliwe wyniki testu

**A. Wspólna tożsamość śladu.** Ślady mają egzemplarze, a kompozycja zachodzi, gdy egzemplarz końcowy jednej relacji jest tym samym egzemplarzem co początkowy drugiej. Formalizm działa, ale egzemplarze tworzą nośnik interfejsów. To poziom 2, nie rozwiązanie N-R2.

**B. Zgodność do izomorfizmu.** Kompozycja zachodzi, gdy ślady mają ten sam typ. Nie ma jednak podstaw do odróżnienia jednego wspólnego interfejsu od dwóch odrębnych kopii. Reguła może być użyteczna jako kompatybilność typów, ale nie jako świadek sklejenia bez dalszych danych.

**C. Ślad wraz z koherentnym świadkiem identyfikacji.** Można zbudować formalizm, który kontroluje wybory izomorfizmów i ich złożenia. Wtedy otrzymujemy bogatszą strukturę (interfejsy, mapowania i aksjomaty koherencji). Należy ją traktować jako nowy kandydat na aksjomat strukturalny i osobno sprawdzić, czy rzeczywiście wynika z P₀-Relacje.

## 7. Werdykt

- **✅** Same typy śladów, rozumiane do izomorfizmu, nie rozstrzygają tożsamości wspólnego interfejsu.
- **✅** Wymóg świadka jako wspólnego egzemplarza przywraca tożsamość pozycji, czyli strukturę nośnika interfejsów.
- **✅** Wybór izomorfizmu jako świadka wymaga dodatkowej informacji; przy automorfizmach może być niejednoznaczny.
- **✅** Zgodność par nie wymusza łączności — kontrprzykład na dwóch elementach jest całkowity.
- **❌** Nie ma podstaw, by uznać, że sam aksjomat „relacja jest pierwotna” wyprowadza wspólny nośnik, świadków sklejenia i koherencję trójkową.
- **💡** Kandydatem na brakujący aksjomat jest struktura interfejsów z koherentnym prawem identyfikacji. To jednak dodatkowa struktura; jej wyprowadzenie z P₀ pozostaje nieudowodnione.

## 8. Znaczenie dla N-R2

Wynik rozdziela dwa pytania, które łatwo pomylić:

1. Czy z już określonej kompozytowalności można odzyskać profile? Tak, przy warunkach z poprzedniego raportu.
2. Czy pierwotność relacji sama określa, kiedy relacje są kompozytowalne i jaki świadek je skleja? Tego dotychczasowe korzenie nie pokazują.

P₀-Relacje v0.3 deklaruje przejście R_t → D_t → C_t → R_(t+1), ale nie definiuje śladów interfejsowych, ich tożsamości ani koherencji sklejeń. Nie wolno uznać zapisu ewolucji za substytut tych definicji.

**Wniosek roboczy:** N-R2 wymaga dodatkowego aksjomatu strukturalnego albo konstrukcji, która go wyprowadzi. Na obecnym materiale nie ma jeszcze takiej konstrukcji. To jest pełnowartościowy wynik negatywny, a nie porażka obliczeniowa.

## 9. Następny test, jeśli program będzie kontynuowany

Nie należy teraz szukać czterech profili. Najpierw trzeba ustalić, czy którykolwiek korzeń P₀ zawiera niezależną od indeksów zasadę, z której da się wyprowadzić:
1. ślady interfejsowe;
2. relację identyfikacji śladów;
3. koherencję identyfikacji dla trzech i większej liczby relacji.

Jeśli nie, należy jawnie dodać aksjomat interfejsów albo pozostawić N-R2 otwarte. Nie wolno nazywać tego emergencją nośnika.

## 10. Integralność zakresu

Raport dotyczy wyłącznie matematycznych korzeni N-R2. Nie modyfikuje P₀-Relacje, MVP-02 ani żadnego filaru. Nie proponuje zmian na main. Nazwa pliku jest ASCII.
