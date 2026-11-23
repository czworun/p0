# N-R2: atomy, klasy kontekstowe i normalna podgrupa V4

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; konstrukcja modelowa N-R2. Bez zmian w MVP-02.  
**Cel:** sprawdzić, czy wybór czterech profili może wynikać z wewnętrznej struktury algebry relacyjnej, zamiast z zadania czterech węzłów.

## 1. Rodzina modeli bez etykiet wierzchołków

Dla dowolnego n ≥ 1 rozważmy skończoną algebrę boolowską

\[
B_n=(\mathcal P([n]),\cap,\cup,\varnothing,[n]).
\]

Można ją traktować jako strukturę nieetykietowaną: automorfizm nie musi zachowywać nazw elementów [n], lecz tylko działania algebry. W porządku indukowanym przez przecięcie, atomami są minimalne elementy niezerowe.

### Twierdzenie 1. Grupa automorfizmów

\[
\operatorname{Aut}(B_n)\cong S_n.
\]

**Dowód.** Każdy automorfizm algebry zachowuje porządek, zero i atomy. Ponieważ każdy element jest jednoznacznie sumą (unią) atomów, automorfizm jest jednoznacznie wyznaczony przez permutację n atomów. Każda permutacja atomów rozszerza się do automorfizmu całej algebry przez obrazowanie podzbiorów. Otrzymujemy dokładnie S_n. ∎

To ważny model: grupę symetrii można odzyskać z wewnętrznej struktury nieetykietowanej algebry. Nie trzeba podawać nazw wierzchołków.

## 2. Ta sama algebra daje różne liczby profili

Najpierw użyjmy profilu jako klasy Greena J, czyli nierozróżnialności względem obustronnych kontekstów:

\[
x\sim_J y\iff B_nxB_n=B_nyB_n.
\]

Przy działaniu przecięcia:

\[
B_nxB_n=\{z\subseteq[n]:z\subseteq x\}=\downarrow x.
\]

Każdy element x ma więc inny ideał główny, a wszystkie klasy J są singletonami. Liczba profili wynosi:

\[
|B_n/{\sim_J}|=2^n.
\]

Dla n=4 otrzymujemy 16 profili, mimo że grupa automorfizmów jest dokładnie S₄.

Druga definicja wybiera profile jako atomy algebry:

\[
\operatorname{At}(B_n)=\{a\ne\varnothing:
\nexists b\ (\varnothing\subsetneq b\subsetneq a)\}.
\]

Wtedy:

\[
|\operatorname{At}(B_n)|=n.
\]

Dla n=4 otrzymujemy cztery profile. Są one wewnętrznie zdefiniowane, bez etykiet wierzchołków, a S₄ działa na nich naturalnie i wiernie.

**Wniosek:** nawet po uzyskaniu nieetykietowanej algebry o pełnej grupie automorfizmów S₄ sama symetria nie rozstrzyga, czy profilami są wszystkie klasy kontekstowe (16), czy tylko atomy (4). Wymagany jest osobny, uzasadniony warunek, że profile są nierozkładalnymi elementami pierwotnymi.

## 3. Co może wybrać atomy?

Własność atomu jest wewnętrzna: element niezerowy jest atomem, jeżeli nie ma ściśle mniejszego elementu niezerowego. To nie wymaga indeksowania ani wskazania źródła/celu relacji.

Można więc postawić kandydacką definicję:

> Profil pierwotny jest minimalnym niezerowym, stabilnym wzorcem relacyjnym, którego nie da się rozłożyć na dwa ściśle mniejsze niezerowe wzorce.

W algebrze boolowskiej odpowiada to atomom.

Ale jest to **nowa definicja**, nie wynik P₀-Relacje v0.3. Dokument nie definiuje porządku częściowego na pierwotnych relacjach, elementu zerowego ani operacji, względem której „mniejszy wzorzec” ma sens. Dopóki te trzy składniki nie zostaną wyprowadzone, atomy są atrakcyjnym modelem, nie odkrytym faktem P₀.

Ponadto dla B_n liczba atomów jest dowolnym n. Samo atomowość i struktura boolowska nie wybierają czterech.

## 4. Czy normalne V4 selekcjonuje n=4?

W grupie S₄ występuje charakterystyczna normalna podgrupa Kleina:

\[
V_4=\{e,(12)(34),(13)(24),(14)(23)\}
\triangleleft S_4.
\]

Jest to jedyna normalna podgrupa S₄ izomorficzna z C₂×C₂. Na czterech atomach B₄ trzy elementy nieidentycznościowe działają jako trzy bezpunktowe podwójne transpozycje; V₄ działa regularnie.

Dla pełnej rodziny grup symetrycznych zachodzi:

- S₂ i S₃ nie mają normalnej podgrupy V₄;
- S₄ ma jedyną normalną podgrupę V₄;
- dla n ≥ 5 normalne podgrupy S_n to (poza trywialną) A_n i S_n, więc nie ma normalnej podgrupy V₄.

Stąd w rodzinie B_n:

\[
\boxed{
\operatorname{Aut}(B_n)\text{ ma normalne }V_4
\iff n=4.
}
\]

To jest mocniejszy kandydat na algebraiczne kryterium wyboru czterech niż samo „minimalne wierne działanie”. Jeżeli z pierwotnej relacji udałoby się niezależnie wyprowadzić:
1. skończoną atomową algebrę boolowską B;
2. pełną grupę automorfizmów Aut(B);
3. obecność normalnej podgrupy izomorficznej z V₄;

to w klasie modeli B_n liczba atomów musiałaby wynosić cztery.

## 5. Dlaczego to jeszcze nie jest dowód P₀

Warunek normalnej V₄ nie może zostać po prostu skopiowany z Defect/Axis i użyty do wyprowadzenia K₄. W obecnym korpusie:

- Defect bierze K₄ jako bazowy kompleks i opisuje jego sześć relacji krawędziowych;
- V₄ pojawia się jako normalna podgrupa S₄ i jako trzy półobroty na sektorze cyklicznym;
- Centroid ma już rodzinę czterech generatorów, względem której definiuje się Aut(𝔤₄;{M_i}) ≅ S₄.

Wzięcie tej V₄ jako aksjomatu pierwotnej relacji byłoby więc potencjalnym przemyceniem struktury K₄ na wcześniejszy poziom. Most jest dopuszczalny tylko wtedy, gdy V₄ zostanie zdefiniowana z operacji relacyjnych, zanim pojawią się cztery węzły, cztery generatory lub sześć krawędzi.

Warto też rozdzielić dwie rzeczy:
- „istnieją trzy komutujące inwolucje” — to jeszcze nie mówi, że tworzą normalną V₄ w pełnej grupie automorfizmów;
- „V₄ jest normalna i działa regularnie na atomach” — to znacznie silniejsza własność, która w rodzinie B_n rzeczywiście selekcjonuje n=4.

## 6. Kandydacki łańcuch wyprowadzenia

Najczystszy obecnie modelowy łańcuch wygląda następująco:

\[
\text{pierwotne relacje}
\longrightarrow
\text{algebra kontekstów}
\longrightarrow
\text{atomy}
\longrightarrow
\operatorname{Aut}(B)
\longrightarrow
V_4\triangleleft\operatorname{Aut}(B)
\longrightarrow
4\text{ atomy}.
\]

Status każdego przejścia:

1. **Pierwotne relacje → algebra kontekstów:** brak definicji w P₀-Relacje v0.3; otwarte N-R2.
2. **Algebra kontekstów → atomy:** wymaga naturalnego porządku i pojęcia zera; model B_n pokazuje, jak to zrobić, ale P₀ tego jeszcze nie definiuje.
3. **Atomy → Aut(B):** ✅ standardowa konstrukcja dla skończonej algebry boolowskiej.
4. **Aut(B) → normalne V₄:** w modelu B₄ ✅; w ogólnej relacji P₀ nieudowodnione.
5. **Normalne V₄ → cztery atomy:** ✅ warunkowo w rodzinie B_n, ponieważ Aut(B_n) ≅ S_n.

Nie wolno przeskakiwać od punktu 4 w istniejącym Defect do punktu 5 i nazywać tego emergencją: byłoby to koło.

## 7. Testy falsyfikujące

Każda proponowana formalizacja musi zostać sprawdzona co najmniej na:

| Model | Liczba atomów | Grupa automorfizmów | Normalne V₄? |
|---|---:|---|---|
| B₂ | 2 | S₂ | nie |
| B₃ | 3 | S₃ | nie |
| B₄ | 4 | S₄ | tak |
| B₅ | 5 | S₅ | nie |
| B₆ | 6 | S₆ | nie |

Dodatkowo trzeba sprawdzić definicję profilu:
- atomy B₄: 4 profile;
- klasy Greena J dla tego samego B₄: 16 profili.

Jeśli formalizacja nie odróżnia tych dwóch zbiorów na podstawie własnych aksjomatów, liczba cztery nie została wyprowadzona.

## 8. Werdykt

- **✅** Dla B_n grupa automorfizmów wynosi S_n.
- **✅** Profile jako atomy dają n klas; dla B₄ są cztery.
- **✅** Profile jako klasy Green J w tym samym B₄ dają 2⁴=16 klas.
- **✅** W rodzinie B_n normalna podgrupa V₄ w grupie automorfizmów występuje dokładnie dla n=4.
- **❌** Sama struktura algebry boolowskiej nie wymusza n=4.
- **❌** Istniejąca V₄ z Defect/Axis nie może być użyta jako dowód wcześniejszej emergencji, dopóki nie zostanie niezależnie odtworzona z pierwotnych operacji relacyjnych.
- **💡** Atomowy profil i normalna V₄ tworzą konkretny, falsyfikowalny kandydat na formalny most do czterech.

**Wniosek:** jest pierwszy model, w którym „cztery” może wynikać z wewnętrznej struktury nieetykietowanej algebry, a nie z listy czterech węzłów. Nadal jednak wymaga dwóch nowych kroków ontologicznych: wyprowadzenia atomowej algebry z pierwotnej relacji oraz wyprowadzenia normalnej V₄ z jej operacji, a nie z już gotowego K₄.

## 9. Integralność repo

Raport zapisano na gałęzi audytowej audit/asterion-continuation-2026-11-20. Nie zmieniono main, nie wykonano merge ani rebase. MVP-02 pozostaje poza zakresem.
