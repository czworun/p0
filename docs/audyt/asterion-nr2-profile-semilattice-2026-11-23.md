# N-R2: profile relacyjne jako klasy kontekstowe — kontrmodele i granica wymuszania 4

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; bez ingerencji w MVP-02.  
**Punkt wyjścia:** P₀-Relacje v0.3, zwłaszcza §§1–3, 7–9 i noty N-R1/N-R2.  
**Status:** wynik częściowy; kontrmodel obala wymuszanie liczby cztery z samej ogólnej struktury relacyjnej.

## 1. Teza geometryczna — poprawne sformułowanie

W klasie modeli, w których profile relacyjne są reprezentowane jako punkty w przestrzeni afinicznej:

[
dim operatorname{aff}{p_1,ldots,p_m}le m-1.
]

Zatem do uzyskania afinicznego wymiaru 3 potrzeba co najmniej czterech profili. Cztery są warunkiem koniecznym, ale niewystarczającym. Dla dokładnie czterech profili warunkiem wystarczającym jest afiniczna niezależność:

[
det[p_2-p_1;p_3-p_1;p_4-p_1]
e0.
]

To twierdzenie jest czysto geometryczne i nie wyprowadza jeszcze ani profili, ani ich geometrii z pierwotnej relacji.

## 2. Minimalny model relacyjno-algebraiczny bez nazwanych węzłów

Zamiast przyjmować graf z zadanym zbiorem wierzchołków, rozważmy abstrakcyjną półkratę (semilattice) jako półgrupę z jednym działaniem (wedge), spełniającym:

[
xwedge y=ywedge x,qquad
(xwedge y)wedge z=xwedge(ywedge z),qquad
xwedge x=x.
]

Nie wprowadzamy osobnego zbioru węzłów grafu ani etykiet źródło/cel. Pierwotnymi danymi formalnymi są elementy algebry i jej relacyjne działanie.

Profile definiujemy jako klasy kontekstowej nierozróżnialności (relację Greena (mathcal J)):

[
xsim_{mathcal J}y
iff SxS=SyS.
]

W półkracie łańcuchowej
[
S_n={0,1,ldots,n-1},qquad xwedge y=min(x,y),
]
mamy
[
S_nxS_n={0,1,ldots,x}.
]
Zbiory te są różne dla różnych (x), więc każda klasa (mathcal J) jest jednoelementowa. Liczba profili wynosi dokładnie (n).

Model nie potrzebuje etykiet wierzchołków ani zewnętrznego harmonogramu. Ma jedną operację binarną, a profile są odzyskiwane z równoważności kontekstowej.

## 3. Kontrmodel: liczba profili nie jest wymuszona

Dla każdego (nge1), (S_n) jest poprawną półkratą i ma dokładnie (n) profili. W szczególności istnieją modele o:

- 2 profilach,
- 3 profilach,
- 4 profilach,
- 5 profilach,
- dowolnej skończonej liczbie profili.

Wobec tego sama łączność, przemienność i idempotentność działania relacyjnego nie wymuszają czterech profili. Nie wymusza ich również samo przejście do klas kontekstowej równoważności.

**Wniosek:** twierdzenie „minimalna algebra relacyjna musi wyłonić dokładnie cztery profile” jest ❌ w tej ogólnej klasie modeli. Potrzebny byłby dodatkowy aksjomat, który wyklucza modele o 2, 3, 5 i większej liczbie klas.

## 4. Jak w jednym modelu pojawia się wymiar (n-1)

Możemy zbudować jawne osadzenie profili łańcucha w przestrzeni wektorowej. Niech (e_0,ldots,e_{n-1}) będzie bazą standardową (mathbb R^n), a profilowi (k) przypiszmy wektor wskaźnikowy jego kontekstu:

[
phi(k)=mathbf1_{{0,ldots,k}}
=sum_{j=0}^{k}e_j.
]

Wtedy
[
phi(k)-phi(k-1)=e_kquad(k=1,ldots,n-1),
]
więc różnice względem (phi(0)) są liniowo niezależne i

[
dimoperatorname{aff}{phi(0),ldots,phi(n-1)}=n-1.
]

Dla (n=4) otrzymujemy cztery afinicznie niezależne profile, a więc wymiar 3. Dla (n=3) wymiar 2, a dla (n=5) wymiar 4.

To jest konstruktywny przykład zgodny z intuicją użytkownika: cztery profile mogą być minimalnym nośnikiem trzech niezależnych kierunków. Ale konstrukcja nie wybiera (n=4); dla każdego (n) działa analogicznie.

## 5. Kluczowe rozdzielenie: liczba profili a ranga geometrii

Są tu dwa niezależne pytania:

1. Ile klas profili powstaje z algebry relacyjnej?
2. Jaki wymiar afiniczny ma ich reprezentacja?

Algebra półkratowa z §2 odpowiada na pierwsze pytanie, ale sama nie dostarcza kanonicznego iloczynu skalarnego ani macierzy Grama. Wskaźnikowe osadzenie z §4 jest naturalnym wyborem kontekstowym, lecz jest dodatkową regułą reprezentacji.

Bez jawnej mapy
[
Phi:{	ext{profile relacyjne}}	o W
]
i jawnej reguły metrycznej na (W), wyrażenie „ranga profili wynosi 3” nie ma jeszcze określonej treści matematycznej. Cztery różne klasy nie gwarantują rangi 3: ich obrazy mogą być współpłaszczyznowe. Z drugiej strony pięć lub więcej profili może rozpiąć wymiar większy niż 3.

Zatem:
- cztery profile (Rightarrow) maksymalnie możliwy wymiar afiniczny 3, jeśli rozpatrujemy dokładnie cztery punkty;
- cztery profile (
otRightarrow) wymiar 3;
- cztery profile + afiniczna niezależność (Rightarrow) wymiar 3;
- sama algebra relacyjna (
otRightarrow) ani liczby profili, ani konkretnej rangi, dopóki nie zostaną podane kryterium profilu i mapa geometryczna.

## 6. Czy model rozwiązuje N-R2?

Nie w pełni. Usuwa jawny zbiór węzłów grafu i zastępuje go klasami kontekstowej równoważności elementów algebry. To jest rzeczywisty model pośredni, ale nie ontologiczne wyprowadzenie wszystkiego z „czystej relacji bez nośnika”: półgrupa nadal ma nośnik elementów. Różnica polega na tym, że elementy nie są interpretowane jako uprzednio dane węzły, lecz jako składniki relacyjnego działania.

To przesuwa pytanie o poziom niżej:
- czy elementy algebry są pierwotnymi relacjami, czy ukrytymi obiektami?
- jaki warunek wewnętrzny wybiera klasę algebr, a nie dowolną półkratę (S_n)?
- czy profil ma być klasą (mathcal J), czy inną równoważnością kontekstową?
- jaka konstrukcja z samych kontekstów daje kanoniczną macierz Grama?

Dopóki te wybory nie zostaną uzasadnione, nie wolno twierdzić, że N-R2 jest rozwiązane.

## 7. Co mogłoby wymusić dokładnie cztery?

Nie wystarczy postulować „minimalności”, „stabilności” ani „zamknięcia”. Każdy taki warunek musi zostać zdefiniowany i sprawdzony na kontrmodelach (S_2,S_3,S_5,ldots).

Kandydat na poprawny program dowodowy:

1. Zdefiniować klasę dopuszczalnych algebr relacyjnych wyłącznie przez aksjomaty operacji i kontekstów.
2. Zdefiniować profile jako kanoniczne klasy równoważności, nie przez zadany indeks.
3. Udowodnić, że liczba klas jest skończona i równa 4 — albo znaleźć kontrmodel.
4. Zdefiniować kanoniczny kernel (K(p,q)) z relacyjnych danych, bez swobodnego wyboru osadzenia.
5. Udowodnić, że wycentrowana macierz Grama ma rangę 3 i jest dodatnio półokreślona.
6. Sprawdzić, czy automorfizmy tej struktury indukują (S_4), a trzy parowania tworzą normalne (V_4). To byłby most między drogą geometryczną a algebraiczną; obecnie nie jest dowiedziony.

## 8. Statusy i werdykt

- **✅** Dla (m) punktów wymiar afiniczny nie przekracza (m-1).
- **✅** Cztery profile są konieczne do uzyskania wymiaru afinicznego 3 w modelu punktowym.
- **✅** Cztery profile są wystarczające wtedy i tylko wtedy, gdy są afinicznie niezależne.
- **✅** Istnieje jednooperacyjny model relacyjny, w którym profile są klasami kontekstowymi, a liczba profili może być dowolnym (nge1).
- **❌** Sama ogólna algebra relacyjna z łącznością, przemiennością i idempotentnością nie wymusza liczby cztery.
- **🔍** Wskaźnikowa reprezentacja kontekstów łańcucha daje wymiar (n-1); jest to konstrukcja, nie uniwersalny niezmiennik.
- **💡** P₀ może uzyskać 3D jako minimalny wymiar reprezentacji czterech niezależnych profili, ale musi wyprowadzić zarówno te cztery profile, jak i kanoniczną geometrię.

**Werdykt:** intuicja „4 jest konieczne, ale niewystarczające dla 3D” jest matematycznie poprawna w modelu afinicznym. Nie wynika jednak jeszcze z korzeni P₀. Obecny kontrmodel pokazuje, że relacyjna algebra bez dodatkowego warunku nie wybiera liczby 4. Następnym właściwym zadaniem nie jest szukanie kolejnej reprezentacji tetraedru, lecz znalezienie minimalnego aksjomatu relacyjnego, który odrzuci (S_2,S_3,S_5,ldots), a następnie wyprowadzi rangę 3 z kanonicznego kernela.

## 9. Zakres i integralność repo

P₀-Relacje v0.3 i PILLARS-TABLE-1 odczytano z `main` w stanie `e4ac4a6d64c4a69983d7378bc5e82d961bb49f5c`. Tabela odnotowuje decyzję autora, że Samoodniesienie jest zapisem, nie osobnym filarem; dokument nie został znaleziony jako korzeń w repo, więc nie rekonstruowano go z domysłów.

Gałąź audytowa `audit/asterion-continuation-2026-11-20` pozostaje rozbieżna z `main` (36 commitów wyłącznie po stronie audytu, 20 wyłącznie po stronie main; status `diverged`). Raport zapisano wyłącznie na gałęzi audytowej. Nie wykonano merge, rebase ani zmian na `main`. MVP-02 pozostaje poza zakresem.
