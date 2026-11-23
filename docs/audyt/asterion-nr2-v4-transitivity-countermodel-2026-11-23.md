# N-R2: kiedy V4 rzeczywiście wymusza cztery profile — kryterium i kontrmodel

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀, N-R2; bez ingerencji w MVP-02.  
**Punkt wyjścia:** P₀-Relacje v0.3; P₀-Centroid v5.2 (lista zmian); P₀-Axis v0.3; P₀-Defect v0.8; wcześniejsze raporty Asteriona o no-go, półkratach, działaniu S4 i algebrze boolowskiej.  
**Status:** kryterium regularnego działania V4 ⇒ cztery profile ✅; kontrmodel sześciu atomów z Aut ≅ S4 i normalną V4 ✅; wyprowadzenie tego kryterium z pierwotnych relacji P₀ nadal 💡/otwarte.

## 1. Pytanie

Poprzedni raport pokazał, że w czystej skończonej algebrze boolowskiej B_n mamy Aut(B_n) ≅ S_n, a największa normalna podgrupa 2-grupowa O₂(S_n) jest izomorficzna z V₄ dokładnie dla n=4.

To jest prawdziwe w rodzinie B_n, ale nie wolno przenosić tego na wszystkie struktury relacyjne bez sprawdzenia. Dodatkowe relacje mogą zmniejszyć grupę automorfizmów do S₄, pozostawiając pięć, sześć albo więcej profili.

Celem raportu jest znaleźć najostrzejszy warunek grupowo-działaniowy, który naprawdę wymusza cztery, oraz sprawdzić, czy korzenie P₀ go uzasadniają.

## 2. Dwa komutujące inwolucje nie wystarczą

Niech a,b ∈ Aut(ℛ) spełniają:

\[
a^2=b^2=e,\qquad ab=ba,\qquad a\ne e,\ b\ne e,\ a\ne b.
\]

Wtedy ⟨a,b⟩ ≅ C₂×C₂ = V₄.

Ale z samego istnienia takich a,b nie wynika, że V₄ jest normalna w pełnej grupie automorfizmów ani że działa przechodnio na profilach.

Kontrprzykład grupowy: w S₅ elementy a=(12), b=(34) są niezależnymi komutującymi inwolucjami i generują V₄, ale ta podgrupa nie jest normalna w S₅. Jej sprzężenia dają inne podgrupy tego samego typu.

A zatem:
- dwa niezależne komutujące półobroty / inwolucje ⇒ podgrupa V₄;
- nie wynika stąd V₄ normalna;
- nie wynika stąd jeden orbita profili;
- nie wynika stąd cztery profile.

## 3. Najostrzejszy prosty warunek: wierne i przechodnie działanie V₄

**Twierdzenie 1.** Niech H ≅ V₄ działa wiernie i przechodnio na niepustym zbiorze P. Wtedy:

\[
\boxed{|P|=4.}
\]

**Dowód.** Dla dowolnego p ∈ P stabilizator H_p jest podgrupą H. Ponieważ H jest abelowa, wszystkie sprzężenia H_p w H są równe H_p. Jądro działania H na orbicie P jest więc równe H_p. Wierność działania wymusza H_p={e}. Z twierdzenia o orbicie i stabilizatorze:

\[
|P|=|H:H_p|=|H|=4.
\]

∎

Wersja przydatna dla N-R2:

\[
H=O_2(\operatorname{Aut}(\mathcal A))\cong V_4,
\qquad H\curvearrowright P
\text{ wiernie i przechodnio}
\quad\Longrightarrow\quad |P|=4.
\]

Warunek jest silniejszy niż samo „Aut zawiera V₄” lub „V₄ jest normalna”. W skończonej algebrze boolowskiej działanie Aut na atomach jest automatycznie wierne, bo każdy element algebry jest jednoznaczną sumą atomów; pozostaje wykazać przechodniość działania O₂.

## 4. Kontrmodel: sześć atomów, Aut ≅ S₄ i normalna V₄

Zbudujmy skończoną strukturę relacyjną z sześcioma atomami, na której pełna grupa automorfizmów jest S₄.

Niech sześć atomów odpowiada sześciu nieuporządkowanym parom z {1,2,3,4}:

\[
P=\binom{\{1,2,3,4\}}2
=\{12,13,14,23,24,34\}.
\]

Dla każdego i ∈ {1,2,3,4} określmy trójelementową rodzinę:

\[
S_i=\{ij:j\ne i\}.
\]

Niech dodatkowa relacja ternarna T wyróżnia dokładnie te cztery trójki S₁,S₂,S₃,S₄. Rozszerzmy algebrę boolowską 𝒫(P) o tę relację na atomach.

### Lemat 2. Grupa automorfizmów rozszerzonej algebry wynosi S₄

Każdy automorfizm algebry boolowskiej permutuje jej sześć atomów. Zachowanie T jest równoważne zachowaniu kolekcji {S₁,S₂,S₃,S₄}.

Każda permutacja atomów zachowująca tę kolekcję indukuje permutację σ czterech trójek S_i. Każdy atom ij jest jednoznacznie wyznaczony jako:

\[
\{ij\}=S_i\cap S_j.
\]

Zatem obraz atomu ij musi być atomem σ(i)σ(j). Każda dozwolona permutacja sześciu atomów jest więc indukowana przez dokładnie jedną permutację czterech indeksów. Odwrotnie, każda permutacja czterech indeksów zachowuje kolekcję trójek. Stąd:

\[
\operatorname{Aut}(\mathcal A)\cong S_4.
\]

Działanie S₄ na sześciu atomach jest wierne i przechodnie.

### Co robi normalna V₄?

W S₄:

\[
O_2(S_4)=V_4
=\{e,(12)(34),(13)(24),(14)(23)\}.
\]

Na sześciu atomach będących parami V₄ nie działa przechodnio. Dzieli je na trzy orbity dwuelementowe:

\[
\{12,34\},\qquad
\{13,24\},\qquad
\{14,23\}.
\]

Otrzymujemy więc strukturę z:
- sześcioma atomami / profilami;
- pełną grupą automorfizmów S₄;
- normalną V₄ jako największą normalną 2-podgrupą;
- wiernym i przechodnim działaniem S₄ na wszystkich sześciu profilach;
- nieprzechodnim działaniem V₄ na profilach.

**To jest kontrmodel rozstrzygający:** normalna V₄ oraz przechodniość pełnego S₄ nadal nie wymuszają dokładnie czterech profili.

Wewnętrzny warunek „V₄ działa wiernie i przechodnio na atomach” usuwa ten kontrmodel. Jest jednak warunkiem dodatkowym, którego nie wolno wprowadzić bez uzasadnienia w P₀.

## 5. Dlaczego czyste B₄ działa, a rozszerzenie sześciopunktowe nie

W czystej algebrze boolowskiej B₄:

\[
\operatorname{Aut}(B_4)=S_4.
\]

Normalna V₄ składa się z trzech podwójnych transpozycji. Każda z nich nie ma punktów stałych na czterech atomach, a cała V₄ działa regularnie:

\[
O_2(\operatorname{Aut}(B_4))\curvearrowright
\operatorname{At}(B_4)
\quad\text{jest regularne}.
\]

Dlatego liczba atomów wynosi cztery.

W rozszerzeniu z §4 pełne S₄ działa na sześciu atomach przez pary, a V₄ rozdziela je na trzy pary przeciwległe. Różnica nie leży w abstrakcyjnej grupie automorfizmów — w obu modelach jest to S₄. Różnica leży w reprezentacji tej grupy na atomach.

To pokazuje, że właściwym kryterium nie jest samo:

\[
O_2(\operatorname{Aut}(\mathcal A))\cong V_4,
\]

lecz także sposób działania tej podgrupy na wybranym nośniku profili.

## 6. Klasyfikacja O₂(S_n) i granica jej zastosowania

Dla czystej algebry boolowskiej B_n mamy Aut(B_n) ≅ S_n. Największa normalna 2-podgrupa grupy symetrycznej spełnia:

\[
O_2(S_n)=
\begin{cases}
1,& n=1,\\
C_2,& n=2,\\
1,& n=3,\\
V_4,& n=4,\\
1,& n\ge5.
\end{cases}
\]

Dla n≥5: jeśli N ⊲ S_n jest 2-grupą, to N∩A_n ⊲ A_n. Prostota A_n daje N∩A_n=1 (A_n nie jest 2-grupą). Znak ograniczony do N osadza więc N w C₂. Gdyby N miała rząd 2, jej jedyny element nieidentycznościowy musiałby być centralny w S_n, co jest niemożliwe dla n≥3. Stąd N=1.

Dla n=4: V₄ jest normalna, a iloraz S₄/V₄ ≅ S₃ nie ma nietrywialnej normalnej 2-podgrupy, więc O₂(S₄)=V₄.

Wniosek w rodzinie **czystych** algebr boolowskich jest prawdziwy:

\[
O_2(\operatorname{Aut}(B_n))\cong V_4
\iff n=4.
\]

Nie wolno go jednak rozszerzać na algebry z dodatkowymi relacjami: kontrmodel z §4 ma sześć atomów i tę samą grupę S₄.

## 7. Czy korzenie P₀ dostarczają dwóch pierwotnych inwolucji?

### Centroid

Rodzina M_i jest już indeksowana przez cztery wierzchołki. W n=4 operator aktualizacji ma na V_ρ widmo {1,1,1/4}; jego wyznacznik jest równy 1/4. Nie jest więc inwolucją. To samo widać z det(M_i)=1/4 w pełnej reprezentacji.

Komutatory Centroidu generują elementy algebry Liego Axis, ale sam komutator Liego nie jest automatycznie inwolucją. Wcześniejszy audyt wykazał, że konkretny komutator grupowy ma nieskończony rząd; nie jest to klasyfikacja wszystkich słów z odwrotnościami, więc nie wyciągam wniosku, że cała grupa generowana przez M_i nie zawiera żadnych elementów rzędu 2.

### Axis

P₀-Axis v0.3 rozpoczyna od:

\[
K_4=(V,E),\qquad V=\{0,1,2,3\}.
\]

Dopiero z trzech par przeciwległych krawędzi:

\[
(01)\leftrightarrow(23),\quad
(02)\leftrightarrow(13),\quad
(03)\leftrightarrow(12)
\]

wyprowadza trzy osie. To poprawna konstrukcja osi **z K₄**, ale nie wyprowadzenie K₄ z wcześniejszych operacji relacyjnych.

### Defect

P₀-Defect v0.8 otrzymuje V₄ jako normalną podgrupę struktury S₄ już działającej na podpisanej reprezentacji krawędzi K₄. Trzy elementy nieidentycznościowe odpowiadają trzem osiom półobrotu. To wynik struktury K₄, nie niezależny początek tej struktury.

### Relacje

P₀-Relacje v0.3 deklaruje ℛ jako obiekt pierwotny, ale nie podaje jeszcze:
- nośnika elementów relacyjnych;
- operacji pierwotnych i ich aksjomatów;
- pojęcia odwracalności operacji;
- grupy automorfizmów ℛ;
- definicji profilu jako atomu lub innego niezmiennika;
- kryterium, według którego kanoniczna część O₂(Aut(ℛ)) ma działać przechodnio na profilach.

W §6 pojawia się R_{t+1}=F(R_t), ale F pozostaje niezdefiniowane. N-R2 (V_t=𝒱(ℛ_t)) jest nadal programem, nie konstrukcją.

**Werdykt:** w aktualnych korzeniach nie ma jeszcze dwóch pierwotnych, kanonicznych, komutujących inwolucji ani dowodu, że grupa automorfizmów pierwotnej relacji ma normalną V₄ działającą regularnie na atomach.

## 8. Co można uczciwie uznać za wynik

- **✅** Dwie niezależne komutujące inwolucje generują V₄, ale sama ich obecność nie wymusza czterech profili.
- **✅** Wierne i przechodnie działanie V₄ na jednym zbiorze profili wymusza dokładnie cztery profile.
- **✅** Istnieje model z sześcioma atomami, Aut ≅ S₄, normalną V₄ i wiernym przechodnim działaniem S₄; V₄ działa na atomach w trzech parach.
- **✅** W czystej rodzinie B_n warunek O₂(Aut(B_n)) ≅ V₄ wybiera n=4.
- **❌** Sama normalna V₄ nie wymusza czterech atomów w ogólnej klasie struktur relacyjnych.
- **🔍** Regularność działania V₄ na atomach B₄ jest konkretną cechą, którą można testować po zbudowaniu algebry relacji.
- **💡** Warunek „O₂(Aut(ℛ)) działa wiernie i przechodnio na atomach relacyjnej algebry profili” jest kandydatem na wewnętrzne kryterium K₄.
- **💡** Aby przejść do 3D, po wyprowadzeniu czterech atomów trzeba jeszcze odzyskać pełne naturalne działanie S₄ oraz kanoniczną mapę afiniczną; wtedy wcześniejsze twierdzenie S₄ ⇒ wymiar 3 ma zastosowanie.

## 9. Następny krok matematyczny

Nie postulować teraz „istnienia V₄”. Najpierw należy spróbować zbudować z samej relacji ℛ algebrę kontekstów A, w której:

1. elementy są klasami operacji lub wzorców relacyjnych, a nie zadanymi węzłami;
2. istnieje naturalne zero i porządek „bycia częścią”;
3. profile są wewnętrznie zdefiniowanymi atomami / nierozkładalnymi elementami;
4. Aut(A) jest obliczana z operacji, nie deklarowana;
5. O₂(Aut(A)) jest wyprowadzana jako charakterystyczna podgrupa;
6. jej działanie na atomach jest testowane pod kątem wierności i przechodniości.

Testy kontrolne muszą obejmować czyste B₂, B₃, B₄, B₅, B₆ oraz rozszerzony model sześciu atomów z §4. Jeżeli proponowane aksjomaty nie odróżnią B₄ od sześciopunktowego kontrmodelu, cztery nie zostały wymuszone.

To jest teraz właściwy test N-R2: czy własność regularności V₄ wynika z wewnętrznej organizacji relacji, czy trzeba ją dopisać jako nowy aksjomat.

## 10. Integralność repo

Raport zapisano wyłącznie na gałęzi audit/asterion-continuation-2026-11-20. main pozostaje nietknięty; nie wykonano merge ani rebase. MVP-02 pozostaje poza zakresem.
