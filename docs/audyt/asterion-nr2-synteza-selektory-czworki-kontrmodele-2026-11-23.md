# N-R2 — synteza selektorów liczby cztery i kontrmodeli liczności

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀, N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Punkt wyjścia:** niezależna recenzja Vibe'a serii 27 raportów Asteriona z 2026-11-23.  
**Status syntezy:** klasyfikacja pięciu wskazanych selektorów — ✅; równoważność torsora V₄ i regularnego działania V₄ — ✅; brak ogólnego wyprowadzenia liczby 4 — ✅; N-R2 — nadal otwarte.

## 0. Werdykt

Recenzja Vibe'a potwierdza najważniejszy wynik negatywny serii: żadna z ogólnych struktur zbadanych dotąd w N-R2 nie wymusza czterech profili. Są natomiast różne warunkowe zasady, które wybierają \(4\).

Pięć nazwanych w recenzji selektorów nie jest pięcioma niezależnymi mechanizmami. Pierwsze dwa — torsor \(V_4\) i wierne, przechodnie działanie \(V_4\) — są tą samą strukturą opisaną z dwóch stron. Pozostałe trzy są odrębne:
1. równowaga wymiarów sektorów różnic i cykli;
2. minimalny stopień wiernej reprezentacji permutacyjnej \(S_4\);
3. dokładnie jednowymiarowy stabilny profil Centroidu po dwóch różnych aktach.

Wszystkie pięć prowadzi do liczby 4, ale nie są równoważne jako aksjomaty. Nie znaleziono zasady korzeni P₀, która wymuszałaby którąkolwiek z nich.

## 1. Pięć selektorów — porównanie

| Selektor | Jawne założenie | Wniosek | Co jest już dane? |
|---|---|---|---|
| A. Torsor Kleina | Dwie niezależne komutujące inwolucje generują \(V_4\), działające swobodnie i przechodnio na niepustym nośniku | \(|X|=4\), z rekonstrukcją \(K_4\) | Grupa \(V_4\) i regularność działania |
| B. Regularne działanie \(V_4\) | \(V_4\) działa wiernie i przechodnio na profilach | \(|P|=4\) | Grupa i warunek działania |
| C. Równowaga wymiarów | Nośnik jest pełnym grafem \(K_n\), a sektory różnic i cykli mają równe niezerowe wymiary | \(n-1=\binom{n-1}{2}\), więc \(n=4\) | Pełny graf i zasada równowagi |
| D. Minimalny stopień \(S_4\) | Grupa symetrii jest już \(S_4\), a szukamy najmniejszego wiernego zbioru permutacyjnego | \(\mu(S_4)=4\) | Grupa \(S_4\); pytanie o minimalny nośnik |
| E. Jeden profil Centroidu | Dwa różne generatory Centroidu pozostawiają dokładnie jednowymiarową przestrzeń stabilną | \(n-3=1\), więc \(n=4\) | Rodzina \(M_i\), przestrzeń współrzędnych i definicja profilu |

### 1.1. A i B są równoważne

Niech \(H\cong V_4\) działa na niepustym zbiorze \(P\).

Jeśli działanie jest wierne i przechodnie, to jest swobodne. Rzeczywiście, ponieważ \(H\) jest abelowa, jądro działania na orbicie jest stabilizatorem dowolnego punktu. Wierność wymusza trywialny stabilizator. Z twierdzenia orbita–stabilizator:

\[
|P|=|H|=4.
\]

To dokładnie torsor \(H\): działanie swobodne i przechodnie.

Odwrotnie, torsor \(V_4\) z definicji daje wierne, swobodne i przechodnie działanie na czterech punktach.

**Wniosek:** A i B to nie dwa niezależne selektory, lecz jedna zasada: regularny torsor \(V_4\). Różnica dotyczy sposobu prezentacji i tego, czy następnie rekonstruujemy z niego \(K_4\), trzy parowania i grupoid par.

### 1.2. C jest niezależnym selektorem wymiarowym

Dla pełnego grafu \(K_n\):

\[
\dim\operatorname{Im}(d)=n-1,
\qquad
\dim\ker(d^*)=\binom{n-1}{2}.
\]

Jeżeli narzucimy równowagę tych sektorów:

\[
n-1=\binom{n-1}{2},
\]

to dla \(n\ge2\) jedynym rozwiązaniem jest \(n=4\).

Nie wynika to z torsora ani z działania grupy. Wymaga zasady równości wymiarów dwóch sektorów, której obecne korzenie P₀ jeszcze nie postulują.

### 1.3. D jest zasadą minimalności, nie zasadą dokładnej liczności

Minimalny stopień wiernej reprezentacji permutacyjnej grupy \(S_4\) wynosi:

\[
\mu(S_4)=4.
\]

Dolne ograniczenie jest proste: dla \(m\le3\) grupa symetryczna \(S_m\) ma co najwyżej \(6\) elementów, więc nie może zawierać wiernego obrazu \(S_4\), który ma \(24\) elementy. Naturalne działanie \(S_4\) na czterech punktach osiąga granicę.

To mówi, że **najmniejszy** wierny nośnik dla już zadanej grupy \(S_4\) ma cztery elementy. Nie mówi, że każdy wierny nośnik ma cztery elementy. Nie wyprowadza też \(S_4\) z pierwotnej relacji.

### 1.4. E jest selektorem dynamiki Centroidu

Dla dodatniego słowa Centroidu używającego zbioru indeksów \(I\), stabilny profil na przestrzeni ilorazowej ma wymiar:

\[
\dim\Phi(P)=\max(n-|I|-1,0).
\]

Dla dwóch różnych generatorów \(|I|=2\), zatem:

\[
\dim\Phi(M_jM_i)=\max(n-3,0).
\]

Warunek „dokładnie jeden niezależny profil pozostaje po dwóch różnych aktach” daje:

\[
n-3=1\quad\Longrightarrow\quad n=4.
\]

To nie jest równoważne zasadzie równowagi wymiarów C. C porównuje dwa sektory \(K_n\); E bada przestrzeń punktów stałych konkretnej rodziny operatorów Centroidu. Oba selektory mają ten sam wynik liczbowy, ale inne przesłanki.

Uwaga: warunek „profil niezerowy” jest słabszy i daje tylko \(n\ge4\). Dopiero warunek **dokładnie jednowymiarowy** wybiera \(n=4\).

## 2. Co selektory mają wspólnego — i czego nie mają

Wszystkie pięć selektorów wprowadza dodatkową zasadę, która ogranicza rodzinę dopuszczalnych modeli:
- A/B ograniczają strukturę działania do regularnego \(V_4\);
- C ogranicza rodzinę do pełnych grafów i równowagi sektorów;
- D ogranicza wybór do minimalnych wiernych reprezentacji już danej grupy \(S_4\);
- E ogranicza dynamikę do dokładnie jednowymiarowego przetrwania po dwóch różnych generatorach.

Nie ma obecnie dowodu, że jedna z tych zasad wynika z pozostałych. Szczególnie nie wolno wykonywać następujących skrótów:

\[
\text{równość wymiarów}\not\Rightarrow V_4,
\]

\[
\text{wierne działanie }S_4\not\Rightarrow |P|=4,
\]

\[
\text{jeden profil po dwóch aktach}\not\Rightarrow
\text{torsor }V_4,
\]

\[
\text{trzy parowania }K_4\not\Rightarrow
\text{pierwotne istnienie }V_4.
\]

Mogą istnieć mosty między tymi warunkami, ale trzeba je udowodnić, a nie utożsamiać na podstawie wspólnego wyniku \(4\).

## 3. Tabela kontrmodeli — ogólne formalizmy nie wybierają 4

| Formalizm / model | Liczba profili lub obiektów | Czy wymusza 4? | Powód |
|---|---:|---|---|
| Półkrata łańcuchowa \(S_n\), \(\wedge=\min\) | Dowolne \(n\ge1\) | Nie | Klasy kontekstowe \(\mathcal J\) są singletonami |
| Półgrupa Brandta \(B_n^0\) | \(n\) niezerowych idempotentów | Nie | Istnieje dla każdego \(n\ge2\) |
| Grupoid par / pair groupoid | Dowolne \(n\) obiektów | Nie | Liczba lokalnych jednostek jest liczbą obiektów wejściowych |
| Skierowany cykl z dodatnimi ścieżkami | Dowolne \(n\) profili | Nie | Profile odzyskuje się z kontekstów; brak potrzeby idempotentów |
| Język resztkowy \(L_n=\{a,a^2,\ldots,a^n\}\) | Dokładnie \(n\) klas przyszłości | Nie | Liczba stanów automatu resztkowego jest dowolna |
| Rozszerzona algebra boolowska na 6 atomach | 6 profili, \(\operatorname{Aut}\cong S_4\) | Nie | \(S_4\) działa wiernie i przechodnio na sześciu parach; \(V_4\) ma trzy orbity |
| Cztery profile i jeden punkt stały | 5 profili | Nie | \(S_4\) działa wiernie na czterech i ustala piąty |
| Środki sześciu krawędzi \(K_4\) | 6 profili geometrycznych | Nie | Naturalne, wierne i przechodnie działanie \(S_4\) |
| Zbiór trzech kontrastów w Scalar | 1 profil niebanalny dla \(n=3\) | Nie | Dwa komponenty dają wymiar \(c(G)-1=1\) |
| Zbiór pięciu kontrastów w Scalar | 1 profil niebanalny dla \(n=5\) | Nie | Ten sam warunek dwóch komponentów |

Kontrmodele nie są wszystkimi możliwymi modelami. Wystarczą jednak, aby obalić ogólne roszczenia, że sama łączność, sama struktura grupoidu, samo \(S_4\), sama resztkowość albo sam jeden stabilny kontrast wymuszają dokładnie cztery profile.

### 3.1. Szczególnie ważny kontrmodel: sześć profili i \(S_4\)

Niech sześć profili odpowiada nieuporządkowanym parom z \(\{1,2,3,4\}\):

\[
P=\binom{\{1,2,3,4\}}2.
\]

Grupa \(S_4\) działa na nich wiernie i przechodnio. Jej normalna podgrupa \(V_4\) rozkłada sześć profili na trzy orbity po dwa elementy:

\[
\{12,34\},\quad\{13,24\},\quad\{14,23\}.
\]

To rozstrzyga dwie częste pomyłki:
- \(\operatorname{Aut}\cong S_4\) nie oznacza czterech profili;
- \(O_2(S_4)\cong V_4\) nie oznacza, że \(V_4\) działa przechodnio na dowolnym zbiorze profili.

## 4. Co jest wspólnym wynikiem Centroid–Scalar–Wave?

Wspólny język stabilnych profili ma już częściowe uzasadnienie, ale nie wolno go rozszerzać ponad dowody.

- **Centroid:** dla dodatnich słów profil jest wyznaczony przez zbiór użytych generatorów; kompozycja odpowiada przecięciu profili.
- **Scalar:** dla pełnych rund na ustalonych grafach profil jest przestrzenią konfiguracji stałych na składowych grafu-unii; złożenie odpowiada przecięciu. Dla rzeczywistego A2 z grafem przeliczanym wewnątrz rundy potrzebne są osobne argumenty.
- **Wave:** profil resztkowy jest zbiorem przyszłych kontynuacji. Nie wymaga domknięcia języka propagacyjności na fragmenty. Dla \(W=02T13T\) profil ma niepustą kontynuację \(13T\), choć sam prefiks \(02T\) nie jest propagacyjny.

Te trzy konstrukcje nie są jeszcze izomorficzne:
- Centroid używa stabilnych wektorów;
- Scalar używa stabilnych konfiguracji/domen;
- Wave używa przyszłych języków kontynuacji.

Ich wspólną cechą jest redukcja po historii/akcie do tego, co nadal może przetrwać. Brakuje ogólnego twierdzenia, które odzyskiwałoby wszystkie trzy z jednego prawa P₀-Relacje.

## 5. Weryfikacja obliczeniowa W — status recenzji Vibe'a

Vibe podał niezależny rachunek dokładny dla słowa Wave \(W=02T13T\):

\[
\chi_W(x)=
\frac{(x-1)(x+1)(256x^2-45x-1)}{256},
\qquad
\det W=\frac1{256}.
\]

Wynik zgadza się z charakterystyką używaną w raportach o profilach resztkowych. Wartości własne to:

\[
1,\quad -1,\quad
\frac{45+\sqrt{3049}}{512},\quad
\frac{45-\sqrt{3049}}{512}.
\]

W szczególności \(-1\) jest niebanalnym relacyjnym modem jednostkowym. To wspiera kontrprzykład przeciw domknięciu języka propagacyjności na fragmenty.

Recenzja Vibe'a deklaruje także dokładną weryfikację ułamkową komutatorów, determinant Centroidu, kontrprzykładu lewych niezmienników Scalar oraz wskazanej trajektorii. W niniejszym raporcie traktuję to jako **niezależny wynik recenzenta**, a nie jako twierdzenie, że dołączono już odtwarzalne skrypty. Reprodukowalność jednym poleceniem pozostaje osobnym zadaniem.

## 6. Priorytety dalszego audytu

1. **Nie szukać szóstego selektora tylko dlatego, że pięć istnieje.** Najpierw trzeba sprawdzić, czy którykolwiek z nich jest konsekwencją niezmienników już obecnych w korzeniach P₀.
2. **Najmocniejszy test konstrukcyjny:** szukać dwóch kanonicznych, niezależnych inwolucji w aparacie Centroid–Axis–Defect bez odwołania do K₄, a następnie sprawdzić komutowanie i regularność działania. Dodatnie słowa Centroidu nie mogą ich dostarczyć: każde ma wyznacznik \(4^{-k}\), więc nie jest inwolucją ani idempotentem. Trzeba osobno sklasyfikować słowa z odwrotnościami lub rozszerzyć klasę operacji z niezależnym uzasadnieniem.
3. **Świadek trójkowy:** spróbować zrealizować minimalną strukturę z raportu o śladach bez nośnika na konkretnym materiale P₀. Bez tego no-go ma mocną część negatywną, lecz brak pozytywnego następcy.
4. **Scalar:** kontynuować dowód dla deterministycznego harmonogramu o ograniczonej uczciwości, nie myląc stabilizacji partycji składowych ze stabilizacją wszystkich krawędzi.
5. **Replikowalność:** dołączyć skrypty dokładne do \(\chi_W\), komutatorów i kontrprzykładu lewych niezmienników.

## 7. Werdykt N-R2

- **✅** W torsorze \(V_4\) nośnik ma dokładnie cztery punkty; jest to równoważne regularnemu działaniu \(V_4\).
- **✅** Równowaga wymiarów sektorów w \(K_n\) wybiera \(n=4\), jeśli jest przyjęta jako warunek.
- **✅** Minimalny wierny stopień \(S_4\) wynosi 4, ale nie ogranicza większych nośników.
- **✅** Dokładnie jednowymiarowy profil Centroidu po dwóch różnych aktach wybiera \(n=4\).
- **❌** Żaden z tych warunków nie został wyprowadzony z samego ogólnego pojęcia relacji ani z obecnych aksjomatów P₀.
- **❌** Samo \(S_4\), samo \(V_4\) jako podgrupa, sama łączność i sama resztkowość nie wymuszają czterech profili.
- **🔍** Nie wiadomo, czy korzenie P₀ zawierają kanoniczną konstrukcję, która implikuje któryś z selektorów bez wcześniejszego założenia \(K_4\).

**N-R2 pozostaje otwarte.** Najbardziej obiecujący następny krok to nie wybór jednego selektora z góry, lecz próba wyprowadzenia inwolucji albo zasady równowagi z niezależnych danych Centroid–Axis–Defect.

## 8. Integralność

Recenzja obejmuje serię 27 raportów według deklaracji Vibe'a. Niniejszy plik syntetyzuje selektory i kontrmodele; nie zmienia żadnego korzenia ani statusu N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z \`main\`.
