# N-R2: rekonstrukcja profili z kompozytowalności — semigroupoid bez obiektów

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. Bez zmian w MVP-02.  
**Punkt wyjścia:** P₀-Relacje v0.3 §§1–8; P₀-TAU v1.7.2 §§1.1, 7.3–7.4; P₀-Flow v0.5.3 §§2–4; P₀-Centroid v5.2-zmiany; poprzednie raporty Asteriona o algebrze relacji i lokalnych jednostkach.  
**Status:** rekonstrukcja profili z dziedziny kompozycji ✅ przy warunku braku źródeł i ujść; profile dla dowolnego n ✅; lokalne identyczności nie wynikają z samej kompozycji ✅ (kontrmodel); przejście od TAU do semigroupoidu P₀ 💡/otwarte.

## 1. Pytanie

Czy można odzyskać profile jako klasy kontekstów kompozycji, nie podając wcześniej zbioru obiektów?

Odpowiedź jest warunkowo twierdząca. Nie trzeba znać źródła i celu każdej strzałki. Wystarczy znać:
- zbiór surowych strzałek A;
- informację, dla których par (a,b) kompozycja ab jest określona;
- jednoznaczną wartość kompozycji na parach dopuszczalnych;
- łączność tej częściowej kompozycji.

To jest opis obiektowo-bezpostaciowego semigroupoidu: nośnikiem pierwotnym jest zbiór strzałek i częściowe działanie, a nie jawna lista obiektów.

## 2. Dwa profile kontekstowe strzałki

Przyjmijmy konwencję: ab oznacza najpierw a, potem b. Dla każdej strzałki a definiujemy wyłącznie z dziedziny kompozycji:

\[
L(a)=\{b\in A:ba\text{ jest określone}\},
\qquad
R(a)=\{b\in A:ab\text{ jest określone}\}.
\]

L(a) zawiera dokładnie te strzałki, które mogą poprzedzać a. R(a) zawiera te, które mogą po nim następować.

Definiujemy relacje równoważności:

\[
a\sim_s b\iff L(a)=L(b),
\qquad
a\sim_t b\iff R(a)=R(b).
\]

Nie używamy nazw źródła ani celu w definicjach. Są to równoważności wyznaczone wyłącznie przez to, z czym dana strzałka może być złożona.

## 3. Twierdzenie rekonstrukcji profili

Załóżmy, że częściowa kompozycja pochodzi z semigroupoidu z nieznaną nam reprezentacją obiektową i spełnia warunek:

**Regularność wejścia/wyjścia:** każdy obiekt jest źródłem co najmniej jednej strzałki i celem co najmniej jednej strzałki.

Wtedy:
- \(\sim_s\) identyfikuje dokładnie strzałki o wspólnym źródle;
- \(\sim_t\) identyfikuje dokładnie strzałki o wspólnym celu.

**Dowód.** Jeśli a i b mają wspólne źródło x, to strzałka c może poprzedzać a dokładnie wtedy, gdy jej cel jest x; to samo kryterium dotyczy b. Zatem L(a)=L(b).

Jeśli źródła a i b są różne, L(a) i L(b) są rozłączne: żadna strzałka nie może kończyć się jednocześnie w dwóch różnych obiektach. Z założenia regularności oba zbiory są niepuste, więc nie mogą być równe. To dowodzi pierwszego punktu. Dualny argument dla R(a) i R(b) dowodzi drugiego. ∎

Aby skleić dwa rodzaje profili, rozważamy rozłączną sumę:

\[
P_s=A/\sim_s,
\qquad
P_t=A/\sim_t.
\]

Dla każdej dopuszczalnej kompozycji ab identyfikujemy klasę celu a z klasą źródła b:

\[
[a]_t\sim[b]_s.
\]

Bierzemy najmniejszą relację równoważności generowaną przez wszystkie takie sklejenia. Jej klasy są rekonstruowanymi profilami.

**Wniosek:** przy warunku regularności wejścia/wyjścia obiekty semigroupoidu można odzyskać z samej struktury kompozytowalności, z dokładnością do jednoznacznego izomorfizmu. Nie trzeba podawać etykiet źródła i celu.

## 4. Przykład: n profili bez podanej listy obiektów

Weźmy skierowany cykl o n pozycjach, ale przedstawmy go wyłącznie przez zbiór wszystkich niepustych skończonych ścieżek. Ścieżki można składać wtedy i tylko wtedy, gdy koniec pierwszej pasuje do początku drugiej. Nie dodajemy ścieżek pustych.

Każda pozycja ma przynajmniej jedną ścieżkę wchodzącą i wychodzącą. Z twierdzenia z §3 otrzymujemy dokładnie n klas profili.

Ważne: konstrukcja działa dla każdego n≥2. Liczba profili nie jest wybrana w definicji równoważności; jest odzyskiwana z kompozytowalności. Ale model nie wybiera n=4.

Przykład dowodzi możliwości rekonstrukcji. Nie dowodzi, że korzenie P₀ już zawierają taką strukturę.

## 5. Co się psuje bez regularności

Warunek nie jest dekoracją. Jeśli dwa profile są źródłami bez strzałek wchodzących, ich zbiory L(a) mogą być puste dla wszystkich strzałek wychodzących z obu źródeł. Wtedy równoważność \(\sim_s\) scala różne źródła.

Analogicznie, dwa ujścia bez strzałek wychodzących mogą zostać scalone przez \(\sim_t\).

Przykładowo dwa różne źródła mogą mieć strzałki prowadzące do tego samego odbiorcy i nie mieć żadnych strzałek wchodzących. Z poziomu samej dziedziny kompozycji ich puste profile wejściowe są nierozróżnialne.

Zatem N-R2 potrzebuje nie tylko reguły kompozycji, ale też zasady aktywności/separacji:
- każdy profil ma wejście i wyjście;
- różne profile mają rozróżnialne konteksty wejścia i wyjścia.

P₀-TAU nie ustanawia takiego warunku dla wszystkich relacyjnych jednostek.

## 6. Druga luka: lokalne identyczności nie wynikają z kompozycji

Skierowany cykl ze §4 jest semigroupoidem bez jednostek lokalnych. Niech |p| oznacza dodatnią długość ścieżki. Kompozycja dodaje długości:

\[
|pq|=|p|+|q|.
\]

Nie istnieje idempotentna strzałka p, ponieważ p²=p wymagałoby:

\[
2|p|=|p|,
\]

a więc |p|=0, wbrew temu, że w zbiorze są tylko niepuste ścieżki.

Mamy zatem model, w którym:
- profile można dokładnie odzyskać z kontekstów kompozycji;
- kompozycja jest łączna;
- każdy profil ma wejścia i wyjścia;
- nie istnieje żaden idempotent, który mógłby pełnić rolę lokalnej identyczności.

**Wniosek:** profile i lokalne jednostki to dwie różne warstwy. Pierwsze można zrekonstruować z kompozytowalności; drugie nie są wymuszone przez samą łączność i dziedzinę kompozycji.

## 7. Kanoniczne dopełnienie przez lokalne jednostki

Po rekonstrukcji zbioru profili P można skonstruować unitalne dopełnienie semigroupoidu: dla każdego p∈P dodajemy nowy element e_p i definiujemy:

\[
e_p a=a\quad\text{dla strzałek wychodzących z p},
\]

\[
a e_p=a\quad\text{dla strzałek kończących się w p},
\]

\[
e_p e_q\text{ jest określone wtedy, gdy }p=q,
\qquad e_p^2=e_p.
\]

Jest to kanoniczne dopełnienie po ustaleniu profili, z dokładnością do izomorfizmu zachowującego istniejące strzałki.

Ale e_p nie był elementem pierwotnego semigroupoidu. Został dodany w dopełnieniu. Nie wolno więc mówić, że został wygenerowany przez sekwencję strzałek.

Można także zacząć od unitalnej kategorii ścieżek, w której ścieżki puste e_p są od początku elementami nośnika. Wtedy e_p są algebraicznie rozpoznawalnymi idempotentami, ale ich obecność jest już częścią założonego modelu.

W obu wariantach liczba profili i jednostek może wynosić dowolne n.

## 8. Konfrontacja z operatorami Centroidu i TAU

Centroid i TAU dostarczają kompozycji operatorów, ale innego rodzaju.

Wszystkie M_i działają na tej samej przestrzeni liniowej. Każda para operatorów może być złożona, więc dziedzina kompozycji jest całkowita. W takim opisie każdy operator ma ten sam pełny zbiór lewych i prawych kontekstów. Rekonstrukcja z §2 daje jeden profil, nie cztery.

Dodatkowo dla bazowego operatora Centroidu:

\[
\det M_i=\frac14.
\]

Dla dodatniego słowa długości k:

\[
\det(M_{i_1}\cdots M_{i_k})=4^{-k}.
\]

Jeśli macierz A jest idempotentna, det(A)²=det(A), a więc det(A)∈{0,1}. Ponieważ 4^{-k} nie należy do {0,1}, żadne niepuste dodatnie słowo w generatorach M_i nie jest idempotentem.

To jest mocniejsza kontrola niż stwierdzenie, że pojedyncze M_i nie są idempotentami: cała dodatnia półgrupa słów nie zawiera idempotentów.

TAU R_σ=M_{σ(n)}⋯M_{σ(1)} formalizuje kolejność aktualizacji. Jednak każda aktualizacja działa na tej samej zadanej przestrzeni, a każda para macierzy jest kompozytowalna. To całkowita kompozycja endomorfizmów, a nie częściowa kompozycja strzałek między odzyskiwanymi profilami.

Wave również interpretuje słowa nad zadanym alfabetem operatorów. Konkatenacja słów daje globalny monoid z pustym słowem jako jednostką; sama nie wyprowadza jednostek lokalnych.

Flow definiuje dynamikę biliniową na C¹(K_n), ale K_n i jego przestrzeń krawędzi są już danymi wejściowymi.

## 9. Co z tego wynika dla P₀-Relacje

P₀-Relacje v0.3 deklaruje ℛ jako poziom pierwotny, lecz:
- nie definiuje częściowej kompozycji;
- nie określa, kiedy dwie relacje mogą następować po sobie;
- nie definiuje kontekstów wejścia/wyjścia;
- nie ustanawia warunku regularności bez źródeł i ujść;
- nie podaje reguły rozróżniania profili o identycznych kontekstach.

Zapis R_{t+1}=F(R_t) nie wystarcza: pojedyncza funkcja ewolucji nie jest jeszcze częściowym działaniem strzałek ani prawem kompozycji.

P₀-TAU opisuje „kto mówi, kto słucha, kiedy”, ale §1.1 jawnie klasyfikuje sekwencyjność jako aksjomat fenomenologiczny i motywacyjny. Daje on podstawę do rozważania semigroupoidu, nie dowodzi jego aksjomatów.

## 10. Werdykt

- **✅** Profile semigroupoidu można odzyskać z klas równoważności określonych przez lewe i prawe konteksty kompozycji.
- **✅** Przy warunku, że każdy profil ma wejście i wyjście, rekonstrukcja jest dokładna.
- **✅** Skierowany cykl z niepustymi ścieżkami daje dowolne n profili bez jawnej listy obiektów.
- **✅** Ten sam model może nie mieć żadnych idempotentów.
- **✅** Lokalne identyczności można kanonicznie dodać po rekonstrukcji profili.
- **❌** Sama łączność kompozycji nie generuje lokalnych jednostek.
- **❌** Sama sekwencyjność nie wybiera n=4.
- **❌** Obecne operatory Centroidu/TAU nie stanowią takiego semigroupoidu: ich kompozycja jest całkowita na wspólnej przestrzeni.
- **🔍** Dodatnie słowa w bazowych generatorach Centroidu nie są idempotentami, co wynika z wyznacznika 4^{-k}.
- **💡** Semigroupoid może być brakującym pośrednim formalizmem dla N-R2, jeśli jego częściowa kompozycja i warunek regularności zostaną wyprowadzone z pierwotnych relacji.

**Wniosek zasadniczy:** da się odzyskać nośnik profili z relacji kompozytowalności, ale nie da się odzyskać go z samego abstrakcyjnego hasła „relacja jest sekwencyjna”. Potrzebna jest konkretna reguła, kiedy relacje składają się ze sobą. Lokalne identyczności są jeszcze kolejnym krokiem, a liczba cztery — jeszcze kolejnym.

## 11. Następny krok

Teraz należy sprawdzić, czy P₀ może zdefiniować kompozytowalność jako wewnętrzną zgodność dwóch relacji, bez jawnego używania końca i początku. Następnie przetestować:
1. czy zgodność jest łączna;
2. czy rekonstruowane klasy są rozdzielone;
3. czy warunek wejścia/wyjścia ma uzasadnienie w korzeniach;
4. czy wyróżniona symetria V₄ działa regularnie na klasach;
5. czy modele z n=2,3,5,6 nadal spełniają te same aksjomaty.

Nie dopisywać V₄ ani n=4 do definicji, zanim nie przejdą testów kontrmodelowych.

## 12. Integralność repo

Raport zapisano wyłącznie na gałęzi audit/asterion-continuation-2026-11-20. main pozostaje nietknięty; nie wykonano merge ani rebase. MVP-02 pozostaje poza zakresem.
