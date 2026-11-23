# N-R2: algebra relacji jako źródło profili — atomy identyczności i granica selekcji czterech

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀, N-R2. Bez zmian w MVP-02.  
**Punkt wyjścia:** P₀-Relacje v0.3 §§1–8; P₀-Axis v0.3 §§1–5; P₀-Defect v0.8 §§1–7.  
**Status:** konstrukcja profili jako atomów identyczności w skończonej algebrze relacji ✅; liczba profili dowolna n — kontrmodel ✅; warunek regularnej V₄ wybiera cztery w tej klasie ✅; wyprowadzenie algebry z pierwotnej ℛ P₀ pozostaje 💡.

## 1. Dlaczego algebra relacji

P₀-Relacje v0.3 chce odwrócić standardowy porządek: relacja → rozróżnienie → stan węzłów. W aktualnym zapisie §7 wraca jednak do ℛ_t=(V,E_t,X_t), gdzie V jest z góry przyjęte; alternatywa V_t=𝒱(ℛ_t) pozostaje niezbudowana.

Półkrata daje klasy kontekstowe, lecz nie rozróżnia wewnętrznie profilu od relacji między profilami. Dla tego rozróżnienia naturalniejsza jest algebra relacji: kompozycja składa relacje, konwersja odwraca kierunek, a wyróżniona relacja identyczności pozwala odzyskać profile jako lokalne identyczności.

To model matematyczny, nie twierdzenie, że P₀ już zawiera pełną algebrę relacji Tarskiego.

## 2. Definicja modelu skończonego

Niech X będzie skończonym zbiorem o n elementach. Rozważmy algebrę

\[
\mathcal R(X)=
(\mathcal P(X\times X),\cup,\cap,{}^c,0,1,;,{}^{-1},1').
\]

Znaczenie:
- 0 = ∅ — relacja pusta;
- 1 = X×X — relacja uniwersalna;
- 1′ = Δ_X = {(x,x):x∈X} — relacja identyczności;
- R⁻¹ = {(y,x):(x,y)∈R} — relacja odwrotna;
- R;S = {(x,z): istnieje y, że xRy i ySz} — kompozycja relacji.

Nazwy elementów X nie należą do sygnatury algebry. Można je wprowadzić do rachunku, ale izomorfizm algebry nie powinien zależeć od etykiet.

## 3. Profile odzyskane jako atomy pod identycznością

Dla x∈X zdefiniujmy diagonalną relację jednoelementową:

\[
e_x=\{(x,x)\}.
\]

Jest ona atomem algebry boolowskiej i spełnia e_x≤1′. Każdy atom leżący pod 1′ ma dokładnie taką postać.

Definiujemy zbiór profili:

\[
P(\mathcal R)=\operatorname{At}(1')
=\{e\ne0:e\le1'\text{ i nie ma }0<f<e\}.
\]

W reprezentacji ℛ(X):

\[
P(\mathcal R(X))=\{e_x:x\in X\},
\qquad |P(\mathcal R(X))|=n.
\]

To rozróżnia:
- wszystkie atomy algebry relacji — singletony {(x,y)}, których jest n²;
- atomy pod identycznością 1′ — wyróżniony podzbiór diagonalny, których jest n;
- atomy poza diagonalą — relacje między profilami.

Dostajemy zatem wewnętrzne kryterium odróżniania profilu od relacji między profilami, pod warunkiem że 1′ i kompozycja należą do formalizmu.

## 4. Grupa automorfizmów jest dokładnie S_n

**Twierdzenie 1.**

\[
\boxed{\operatorname{Aut}(\mathcal R(X))\cong S_n.}
\]

**Dowód.** Każdy automorfizm zachowuje stałą 1′, porządek boolowski i atomy. Musi więc permutować n atomów podidentycznościowych e_x. Każdy atom relacji a_xy={(x,y)} można odzyskać jako

\[
a_{xy}=e_x;1;e_y.
\]

Zatem permutacja atomów e_x jednoznacznie wyznacza obrazy wszystkich atomów algebry, a więc każdego elementu będącego ich sumą. Każda permutacja X indukuje automorfizm przez (x,y)↦(σx,σy). Automorfizmy są dokładnie permutacjami n profili. ∎

To ważne dla N-R2: grupa S_n może być odzyskana z samej algebry relacji, zamiast być zadana jako symetria czterech etykiet.

## 5. Kontrmodel: algebra relacji nie wymusza czterech

Konstrukcja działa dla każdego n≥1:

\[
|P(\mathcal R(X))|=n,
\qquad
\operatorname{Aut}(\mathcal R(X))\cong S_n.
\]

Istnieją więc modele o 2, 3, 4, 5, 6 i dowolnej skończonej liczbie profili. Sam zestaw operacji algebraicznych: Boolean, kompozycja, konwersja i identyczność, nie wybiera n=4.

To falsyfikuje mocną wersję hipotezy, że relacyjność sama w sobie wymusza cztery. Wybiera ona typ profilu i grupę automorfizmów, ale nie rozmiar nośnika.

## 6. Kiedy w tej klasie modeli wyłaniają się dokładnie cztery?

Dla Aut(ℛ(X))≅S_n rozważmy największą normalną 2-podgrupę O₂(S_n). Zachodzi:

\[
O_2(S_n)=
\begin{cases}
1,&n=1,\\
C_2,&n=2,\\
1,&n=3,\\
V_4,&n=4,\\
1,&n\ge5.
\end{cases}
\]

Dla n≥5 prostota A_n oznacza, że normalna 2-podgrupa N ma N∩A_n=1, więc osadza się w S_n/A_n≅C₂. Jej element nieidentycznościowy musiałby być centralny w S_n, co dla n≥3 jest niemożliwe. Dla n=4 V₄ jest normalna, a iloraz S₄/V₄≅S₃ nie ma nietrywialnej normalnej 2-podgrupy. Przypadki n=2,3 są bezpośrednie.

Dla n=4 trzy nieidentycznościowe elementy V₄ są podwójnymi transpozycjami. Działają bez punktów stałych na czterech atomach identyczności, a cała V₄ działa regularnie.

W tej konkretnej klasie pełnych algebr relacji warunek O₂(Aut(ℛ))≅V₄ wybiera zatem dokładnie cztery profile.

## 7. Granica: rozszerzenia relacyjne

W poprzednim raporcie skonstruowano strukturę na sześciu obiektach odpowiadających krawędziom K₄:
- pełna grupa automorfizmów jest S₄;
- S₄ działa wiernie i przechodnio na sześciu obiektach;
- normalna V₄ dzieli je na trzy pary.

Ten kontrmodel nadal obowiązuje dla ogólniejszych struktur relacyjnych i rozszerzeń algebry o dodatkowe predykaty. Zatem:
- w pełnej algebrze relacji ℛ(X) automorfizmy są S_n i O₂ selekcjonuje n=4;
- w rozszerzonej strukturze z dodatkowymi relacjami samo Aut≅S₄ i obecność normalnej V₄ nie wymuszają czterech;
- kryterium O₂ musi być połączone z działaniem na kanonicznie zdefiniowanych profilach, nie tylko z abstrakcyjnym typem grupy.

## 8. Porównanie z korzeniami P₀

**P₀-Relacje v0.3.** §1 deklaruje relację jako byt podstawowy, a §6 zapisuje R_{t+1}=F(R_t). Nie definiuje jednak kompozycji dwóch relacji, relacji odwrotnej, identyczności 1′ ani algebry kontekstów zamkniętej na te operacje. Powyższa konstrukcja jest zatem kandydatem na brakujący formalizm, nie odczytaniem gotowego twierdzenia.

**P₀-Axis v0.3.** Rozpoczyna jawnie od K₄=(V,E), |V|=4, a następnie wyprowadza trzy pary przeciwległych krawędzi, środki krawędzi i osie. Dowodzi własności geometrii relacyjnej już zadanego K₄, ale nie konstruuje 1′ ani atomów profili z obiektu wcześniejszego niż K₄.

**P₀-Defect v0.8.** Pracuje na C¹(K₄), czyli sześciu relacjach krawędziowych, z rozkładem exact/cyclic. W algebrze relacji analogicznie należy odróżnić atomy identyczności (profile) od atomów poza diagonalą (relacje między profilami). To potencjalnie usuwa pomieszanie czterech wierzchołków i sześciu krawędzi, ale wymaga przyjęcia kompozycji relacji.

## 9. Most do geometrii 3D

Jeśli z ℛ udałoby się wyprowadzić pełną skończoną algebrę relacji z czterema atomami pod identycznością, mamy naturalny zbiór czterech profili P. Aby uzyskać 3D, nadal trzeba:
1. odzyskać pełne naturalne działanie S₄ na czterech atomach;
2. skonstruować kanoniczną reprezentację afiniczną albo kernel Gramowski;
3. dowieść afinicznej niezależności.

Wcześniejsze twierdzenie o standardowej reprezentacji S₄ daje wtedy wymiar 3. Nie wynika stąd automatycznie, że metryka Centroidu G₄=4I−J jest jedyną możliwą metryką; trzeba ją wyprowadzić z operacji relacyjnych lub niezmiennika.

## 10. Werdykt

- **✅** Pełna skończona algebra relacji odzyskuje profile jako atomy pod identycznością, bez wcześniejszego etykietowania.
- **✅** Jej grupa automorfizmów jest dokładnie S_n.
- **✅** Liczba profili może być dowolnym n; sama algebra relacji nie wymusza czterech.
- **✅** W tej klasie O₂(Aut(ℛ))≅V₄ wybiera dokładnie cztery profile.
- **✅** Rozróżnienie atomów identyczności i atomów poza diagonalą daje naturalny podział: profile kontra relacje między profilami.
- **❌** Obecny P₀-Relacje v0.3 nie definiuje jeszcze operacji wymaganych przez pełną algebrę relacji.
- **💡** Algebra relacji może być właściwym pośrednim formalizmem N-R2, jeżeli kompozycja, konwersja i identyczność zostaną wyprowadzone, a nie po prostu dopisane.
- **💡** Regularność V₄ na atomach identyczności może być kryterium selekcji K₄; uzasadnienie tego warunku w P₀ pozostaje otwarte.

**Najważniejszy wniosek:** mamy mocniejszy model niż półkrata. Profile można odzyskać z algebry relacji jako atomy pod identycznością. Ale cztery nadal nie wynikają z relacyjności ogólnej. Wynikają dopiero po dodaniu konkretnego warunku strukturalnego o 2-rdzeniu grupy automorfizmów. Problemem nie jest już wymyślenie kolejnej algebry, lecz uzasadnienie, dlaczego relacyjna struktura P₀ miałaby spełniać właśnie ten warunek.

## 11. Integralność repo

Raport zapisano wyłącznie na gałęzi audit/asterion-continuation-2026-11-20. main nie został zmieniony; nie wykonano merge ani rebase. MVP-02 pozostaje poza zakresem.
