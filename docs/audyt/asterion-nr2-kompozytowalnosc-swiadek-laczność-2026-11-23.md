# N-R2: kompozytowalność jako zgodność wewnętrzna relacji

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. Bez zmian w MVP-02.  
**Gałąź docelowa:** `audit/asterion-continuation-2026-11-20`  
**Punkt wyjścia:** P₀-Relacje v0.3 §§1–8, N-R2; raport Asteriona o rekonstrukcji profili z semigroupoidu (2026-11-23).  
**Status:** no-go dla kompozytowalności z gołego zbioru atomów ✅; łączne prawo niepustej kompozycji relacji binarnych na wspólnym nośniku ✅; wyprowadzenie wspólnego nośnika z relacji P₀ 💡/otwarte; wybór n=4 ❌/niewynikający.

## 1. Pytanie

Czy można zdefiniować, kiedy dwie relacje mogą następować po sobie, nie odwołując się do wcześniej zadanych źródeł i celów? Jeśli tak, czy wynikająca częściowa kompozycja jest łączna?

Rozdzielam trzy poziomy:
1. goły zbiór relacji/atomów bez struktury;
2. relacje jako podzbiory wspólnego nośnika, z wewnętrznym świadkiem zgodności;
3. pierwotny formalizm P₀, który miałby wyprowadzić także sam nośnik i regułę zgodności.

Nie wolno utożsamiać sukcesu na poziomie 2 z rozwiązaniem poziomu 3.

## 2. No-go: sam zbiór atomów nie wyznacza bogatej zgodności

Niech A będzie zbiorem co najmniej trzech elementów, wyposażonym wyłącznie w równość. Szukamy binarnego predykatu C(a,b), który ma wyznaczać kompozytowalność i być kanoniczny, tj. niezmienniczy względem każdej permutacji A.

Grupa Sym(A) ma na A×A dokładnie dwie orbity:
- pary diagonalne (a,a);
- pary poza diagonalą (a,b), a≠b.

Zatem każdy taki predykat C jest jedną z czterech możliwości:
- nigdy nie zachodzi;
- zachodzi tylko dla a=b;
- zachodzi tylko dla a≠b;
- zachodzi dla każdej pary.

Żadna z nich nie rozpoznaje nietrywialnego dopasowania końca jednej relacji do początku drugiej. Nie ma w gołym zbiorze danych, które pozwalałyby odróżnić takie dopasowanie od innych par.

**Wniosek:** zgodność nie może zostać wyprowadzona z samego istnienia atomów relacyjnych. Potrzebny jest dodatkowy niezmiennik, świadek, ślad, struktura kontekstu lub prawo transformacji.

To jest ograniczenie strukturalne, a nie problem braku sprytnej definicji.

## 3. Kandydat: niepusty iloczyn relacji binarnych

Warunkowo przyjmijmy wspólny zbiór X. Relacje A,B są podzbiorami X×X. Definiujemy zwykły iloczyn relacyjny:

[
Astar B={(x,z)in X^2:exists yin X, (x,y)in Aland(y,z)in B}.
]

Przy konwencji „najpierw A, potem B” jest to złożenie ścieżek A→B. Nie definiujemy jednak dopuszczalności przez wcześniej nazwane źródło i cel relacji. Definiujemy ją przez istnienie wewnętrznego świadka y:

[
C(A,B)iff Astar B
earnothing.
]

Częściowe działanie:

[
Adiamond B=
egin{cases}
Astar B,& Astar B
earnothing,\
	ext{nieokreślone},& Astar B=arnothing.
end{cases}
]

Dziedziną działania są niepuste relacje binarne. Iloczyn może być pusty, a wtedy para nie jest kompozytowalna w tym częściowym działaniu.

To jest sensowny kandydat na „zgodność samych relacji”: zgodność zachodzi wtedy, gdy istnieje przynajmniej jeden wspólny ślad pośredni.

## 4. Twierdzenie: częściowy iloczyn jest łączny

Dla dowolnych relacji A,B,C⊆X×X zachodzi:

[
(Astar B)star C=Astar(Bstar C).
]

Dowód elementowy:

[
(x,w)in(Astar B)star C
]

wtedy i tylko wtedy, gdy istnieją y,z takie, że:

[
(x,y)in A,quad(y,z)in B,quad(z,w)in C.
]

To jest równoważne temu, że:

[
(x,w)in Astar(Bstar C).
]

W konsekwencji:
- (A⋆B)⋆C jest niepuste wtedy i tylko wtedy, gdy A⋆(B⋆C) jest niepuste;
- lewa strona częściowej kompozycji jest określona dokładnie wtedy, gdy prawa jest określona;
- jeżeli są określone, mają tę samą wartość.

Zatem ◆ jest łącznym działaniem częściowym w mocnym sensie: dla trójki A,B,C obie strony są określone równocześnie i są równe.

**Status: ✅ twierdzenie algebraiczne.**

Ważne: łączność nie wynika z samego predykatu C. Wynika z połączenia dwóch składników:
1. kompozycji relacyjnej zdefiniowanej przez wspólnego świadka;
2. ograniczenia dziedziny do par o niepustym iloczynie.

Dowolny predykat zgodności i dowolnie dobrana wartość kompozycji nie muszą być łączne.

## 5. Co dokładnie zostało ukrycie założone?

Konstrukcja z §3 nie używa nazw źródła i celu jako danych wejściowych, ale zakłada:
- wspólny nośnik X;
- rozróżnienie dwóch pozycji w parze (x,y);
- możliwość porównania drugiej pozycji jednej pary z pierwszą pozycją drugiej;
- egzystencjalne kryterium świadka pośredniego.

To jest już struktura. Nie jest neutralnym „samym istnieniem relacji”.

Jeżeli X jest zbiorem obiektów, to konstrukcja odtwarza standardową kompozycję relacji na X. Zmienia sposób podania kryterium, ale nie wyprowadza X.

Jeżeli X ma być zbiorem wyłonionym z relacji, trzeba najpierw zdefiniować, czym jest pozycja pierwsza i druga relacji, zanim powstanie X. Tego obecny P₀-Relacje nie robi.

## 6. Profile odzyskane w tym modelu nie muszą być punktami

Możemy sprawdzić konteksty kompozycji dla niepustych relacji binarnych:

[
L(A)={Q:Qdiamond A	ext{ określone}},
quad
R(A)={Q:Adiamond Q	ext{ określone}}.
]

Dla zwykłych relacji binarnych:
- Q⋆A≠∅ wtedy i tylko wtedy, gdy obraz Q przecina dziedzinę A;
- A⋆Q≠∅ wtedy i tylko wtedy, gdy obraz A przecina dziedzinę Q.

Zatem L(A) zależy od dziedziny A, a R(A) od obrazu A. Jeśli w nośniku dostępne są wszystkie niepuste relacje binarne, konteksty potrafią rozróżniać te podzbiory X.

To daje ważną korektę do poprzedniej rekonstrukcji semigroupoidu: po przejściu do relacji wielowartościowych odzyskiwany profil może być podzbiorem nośnika, a nie pojedynczym punktem. Węzeł nie wyłania się automatycznie jako atom.

Przykład: dwie relacje o tej samej dziedzinie, ale różnych obrazach, mają ten sam lewy kontekst L, lecz mogą mieć różne prawe konteksty R. Nie należy więc utożsamiać jednego rodzaju kontekstu z pełnym profilem.

## 7. Kontrmodel skali: prawo nie wybiera czterech

Konstrukcja działa na dowolnym X:
- |X|=2;
- |X|=3;
- |X|=4;
- |X|=5;
- dowolnym skończonym lub nieskończonym nośniku.

Łączność nie zależy od liczby elementów X. Sam warunek niepustości iloczynu również nie wybiera szczególnej liczności.

Można ponadto wybrać X o dowolnej liczności i rozważać tylko relacje na nim. Nie ma w tym prawie selektora n=4, V₄ ani K₄.

**Wniosek:** nawet po znalezieniu naturalnej łącznej zgodności relacji liczba cztery nie wynika z samej kompozycji.

## 8. Konfrontacja z P₀-Relacje v0.3

W dokumencie korzeniowym:
- §1 deklaruje relację jako poziom pierwotny, ale nie definiuje jej wewnętrznego typu;
- §2 traktuje relację jako historię R_ij(t), ale indeksy i para ij są już obecne;
- §4 wprowadza cykl D_t→C_t→R_{t+1}, lecz nie podaje binarnego prawa składania dwóch relacji;
- §6 zapisuje R_{t+1}=F(R_t), ale F pozostaje niezdefiniowane;
- §7 jawnie przyznaje, że V jest założone w zapisie (V,E_t,X_t);
- §8 definiuje E_t⊆V×V, a więc ponownie zakłada nośnik i jego pary.

Obecny korzeń nie dostarcza jeszcze:
1. pierwotnej przestrzeni X;
2. dwóch pozycji relacji, które można dopasować;
3. świadka zgodności;
4. reguły wartości kompozycji;
5. dowodu łączności tej reguły.

Konstrukcja z §3–4 może być formalnym modelem testowym, ale nie można jej przypisać P₀ jako wyniku wyprowadzonego z aksjomatów.

## 9. Ważne rozróżnienie: zgodność a podobieństwo

Nie należy zastępować C(A,B) przez miarę podobieństwa, korelację ani „wspólną treść” relacji bez osobnego uzasadnienia.

Zgodność kompozycyjna ma charakter świadkowy: istnieje konkretny element pośredni y, który umożliwia sklejenie dwóch par. Podobieństwo może być wysokie, a kompozycja nadal niemożliwa; relacje mogą być różne, a mimo to kompozytowalne.

Nie ma powodu, by metryka lub korelacja miały automatycznie wyznaczać dziedzinę działania.

## 10. Werdykt

- **✅** Z samego gołego zbioru atomów, przy pełnej niezmienniczości względem permutacji, nie da się uzyskać nietrywialnej reguły dopasowania.
- **✅** Dla relacji binarnych na wspólnym nośniku niepusty iloczyn relacyjny definiuje naturalną kompozytowalność.
- **✅** Ograniczenie kompozycji do niepustych iloczynów daje łączne działanie częściowe.
- **✅** Łączność wynika z istnienia tego samego łańcucha świadków po obu stronach nawiasowania.
- **🔍** Konteksty kompozycji w tym modelu odzyskują dziedziny i obrazy relacji, a więc profile mogą być podzbiorami nośnika.
- **❌** Konstrukcja nie wyprowadza wspólnego nośnika X ani rozróżnienia pozycji relacji z samego P₀.
- **❌** Nie wybiera n=4, V₄ ani geometrii K₄.
- **💡** Niepusty iloczyn relacyjny jest kandydatem na testowy formalizm N-R2, ale wymaga redukcji do danych pierwotnych P₀.

## 11. Następny test — najważniejszy

Należy zejść o poziom niżej niż relacje binarne i zapytać, czy „wspólny świadek” można odzyskać z samych śladów kompensacji.

Proponuję test trzech wymagań:
1. **Brak ukrytego nośnika:** definicja śladu nie może używać X ani indeksów i,j.
2. **Wewnętrzne sklejenie:** zgodność dwóch śladów musi być rozpoznawalna wyłącznie z ich własnych danych.
3. **Spójność trzech śladów:** jeśli a może następować po b, a b po c, reguła musi zapewniać zgodność obu nawiasowań oraz tę samą złożoną relację.

Jeśli nie da się zdefiniować świadka bez wcześniejszego rozróżnienia pozycji relacji, otrzymamy mocny no-go: N-R2 potrzebuje dodatkowego aksjomatu strukturalnego, a nie tylko aksjomatu „relacja jest pierwotna”.

Nie będę jeszcze dopisywał V₄ ani K₄. Najpierw trzeba wykazać, że sama relacja umie wytworzyć rozróżnienie, które umożliwia jej składanie.

## 12. Integralność zakresu

Analiza dotyczy wyłącznie matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Raport przeznaczony do zapisu wyłącznie na gałęzi audytowej; bez merge/rebase z main.
