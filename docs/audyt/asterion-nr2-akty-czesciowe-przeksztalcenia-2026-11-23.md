# N-R2: akty kompensacji jako częściowe przekształcenia konfiguracji

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Punkty odniesienia:** P₀-Relacje v0.3 §§2, 4, 6–8; P₀-Centroid v5.2; P₀-TAU v1.7.2; raport Asteriona o interfejsach aktów rzędu jeden (2026-11-23).  
**Status:** częściowe przekształcenia konfiguracji dają łączne prawo kompozycji ✅; model nie wybiera n=4 ✅/kontrmodel; zwykłe kryterium „następny akt reaguje” nie jest łączne ❌/kontrprzykład; kryterium niekomutowania jest niełączne nawet dla generatorów Centroidu ❌; wyprowadzenie przestrzeni konfiguracji i dziedzin aktów z pierwotnej relacji P₀ otwarte 💡.

## 1. Pytanie

Poprzedni etap wykazał, że interfejsy rzędu jeden \(U(D)\) i \(F(D)\) dają łączne częściowe działanie, ale wymagają \(V\) i \(V^*\). Ponadto dla generatorów Centroidu wszystkie parowania są niezerowe, więc kryterium nie daje selektywnej sieci następstwa.

Teraz usuwamy strukturę liniową. Pytamy, czy akt kompensacji może być częściowym przekształceniem zbioru konfiguracji relacyjnych.

Ważne: konfiguracje nie muszą być węzłami sieci. Mogą oznaczać całe dopuszczalne układy relacyjne. Ale ich zbiór nadal trzeba zdefiniować.

## 2. Minimalna struktura: częściowy akt na konfiguracjach

Niech \(Q\) będzie zbiorem konfiguracji relacyjnych. Akt \(a\) jest częściową funkcją:

\[
T_a:\operatorname{Dom}(T_a)\rightharpoonup Q.
\]

Akt jest dopuszczalny tylko na konfiguracjach należących do swojej dziedziny. Dla dwóch aktów \(a,b\), przy kolejności „najpierw a, potem b”, definiujemy:

\[
\operatorname{Dom}(T_b\circ T_a)
=
\{q\in\operatorname{Dom}(T_a):
T_a(q)\in\operatorname{Dom}(T_b)\}.
\]

Kompozycja jest dopuszczalna wtedy i tylko wtedy, gdy istnieje przynajmniej jedna konfiguracja, na której oba akty mogą przejść jeden po drugim:

\[
a\rightsquigarrow b
\iff
\operatorname{Dom}(T_b\circ T_a)\ne\varnothing.
\]

Równoważnie:

\[
\operatorname{Im}(T_a)\cap\operatorname{Dom}(T_b)\ne\varnothing.
\]

Nie wprowadzamy osobnej etykiety źródła ani celu aktu. Dziedzina i obraz są własnościami samego częściowego przekształcenia.

## 3. Twierdzenie: prawo jest silnie łączne

Dla trzech aktów \(a,b,c\) dziedzina lewego nawiasowania wynosi:

\[
\operatorname{Dom}((T_c\circ T_b)\circ T_a)
=
\{q\in\operatorname{Dom}(T_a):
T_a(q)\in\operatorname{Dom}(T_b),
T_b(T_a(q))\in\operatorname{Dom}(T_c)\}.
\]

Dziedzina prawego nawiasowania:

\[
\operatorname{Dom}(T_c\circ(T_b\circ T_a))
\]

jest dokładnie tym samym zbiorem. Dla każdego q obie strony dają ten sam wynik \(T_c(T_b(T_a(q)))\).

Zatem:
- lewa strona jest określona wtedy i tylko wtedy, gdy prawa;
- jeżeli są określone, są tym samym częściowym przekształceniem;
- nie trzeba dodawać osobnego aksjomatu łączności.

**Wynik ✅:** częściowe przekształcenia tego samego zbioru konfiguracji, z kompozycją ograniczoną do niepustej dziedziny, tworzą silnie łączny system częściowy.

To jest mocniejszy kandydat niż próba wydobywania liczby przez parowanie w \(V^*\times V\). Nie wymaga wektorów, norm, iloczynu skalarnego ani dualności.

## 4. Co nadal zostało założone?

Konstrukcja wymaga:
1. zbioru \(Q\) dopuszczalnych konfiguracji relacyjnych;
2. równości konfiguracji — trzeba wiedzieć, kiedy wynik jednego aktu jest dokładnie konfiguracją dopuszczalną dla drugiego;
3. dziedziny każdego aktu, czyli warunku, na jakich konfiguracjach może on działać;
4. jednoznacznego wyniku aktu na konfiguracji należącej do dziedziny.

Nie są to źródła i cele w sensie grafu węzłów. Są to jednak dane strukturalne. Jeśli \(Q\) jest tylko inną nazwą dla wcześniej założonych obiektów, nie rozwiązaliśmy N-R2.

W P₀-Relacje §6 pojawia się zapis \(R_{t+1}=F(R_t)\), ale nie ma określonego zbioru konfiguracji, dziedziny F ani kryterium, kiedy akt jest dopuszczalny. W §7–8 z kolei \(V\) i \(V\times V\) są już jawnie zadane. Obecny korzeń nie dostarcza więc jeszcze potrzebnych danych.

## 5. Kontrmodel: częściowe akty dopuszczają dowolne n

Dla dowolnego \(n\ge2\) przyjmijmy \(Q=\mathbb Z/n\). Niech \(T_i\) będzie częściową funkcją:

\[
\operatorname{Dom}(T_i)=\{i\},\qquad T_i(i)=i+1\pmod n.
\]

Wtedy:

\[
T_i\rightsquigarrow T_j
\iff
j=i+1\pmod n.
\]

Kompozycje wieloetapowe dają częściowe funkcje z singletonowej dziedziny \(\{i\}\) do singletonowego obrazu \(\{j\}\). Domknięcie względem kompozycji jest izomorficzne z grupoidem parowym na n stanach: dla każdej pary i,j istnieje dokładnie jedna strzałka \(\{i\}\to\{j\}\), a kompozycja zachodzi przy zgodności pośredniego stanu.

Otrzymujemy dokładnie n profili. Konstrukcja działa dla każdego n≥2. Lokalne identyczności to funkcje identyczności na singletonach \(\{i\}\); jest ich n.

**Wniosek:** nawet częściowe przekształcenia z kanoniczną łącznością oraz lokalnymi jednostkami nie wymuszają n=4. Dają model dla dowolnej liczby profili.

## 6. Próba wyprowadzenia zgodności z samej odpowiedzi aktu

Możliwy pierwszy predykat:

\[
C_{\mathrm{resp}}(a,b)
\iff
T_b\circ T_a\ne T_b.
\]

Czyli: b reaguje na a, jeżeli zastosowanie b po a daje na przynajmniej jednej konfiguracji inny wynik niż samo b.

To kryterium nie wymaga metryki ani wektorów. Jednak nie daje automatycznie łącznej kompozycji.

**Kontrprzykład na \(Q=\{0,1\}\).** Oznaczmy:
- \(a(q)=0\) — funkcja stała zero;
- \(b(q)=q\) — identyczność;
- \(c(q)=q\) — identyczność.

Wtedy:
- a po b jest dopuszczalne, ponieważ \(b\circ a=a\ne b\);
- wynik \(a;b\) to a;
- ten wynik po c jest dopuszczalny, ponieważ \(c\circ a=a\ne c\);
- ale b po c nie jest dopuszczalne, ponieważ \(c\circ b=b=c\).

Zatem lewa strona \((a;b);c\) jest określona, a prawa \(a;(b;c)\) nie jest. Kryterium „następny akt zmienia odpowiedź” nie spełnia nawet słabej warunkowej postaci łączności.

**Wniosek:** samo niezerowe oddziaływanie/zmiana odpowiedzi nie jest wystarczającą regułą kompozycji.

## 7. Druga próba: niekomutowanie jako ślad wzajemnej odpowiedzi

Można próbować definiować:

\[
C_{\mathrm{ord}}(a,b)
\iff
T_bT_a\ne T_aT_b.
\]

Intuicja: dwa akty są relacyjnie sprzężone, jeżeli kolejność ich wykonania zmienia wynik.

To kryterium ma sens dla TAU, gdzie kolejność aktualizacji jest istotna. Ale „kolejność ma znaczenie” nie oznacza „właśnie wtedy akty są kompozytowalne”. Co więcej, ograniczenie iloczynu do par niekomutujących nie jest łączne.

### Kontrprzykład bezpośrednio w Centroidzie dla n=4

Niech \(M_0,M_1\) będą generatorami Centroidu, a \(P=M_1M_0\) — wynikiem sekwencji najpierw \(M_0\), potem \(M_1\).

Dla komutatora \([A,B]=AB-BA\) rachunek daje:

\[
[M_0,M_1]=
\frac1{16}
\begin{pmatrix}
1&-3&1&1\\
3&-1&-1&-1\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}
\ne0,
\]

oraz:

\[
[M_0,P]=
\frac1{64}
\begin{pmatrix}
1&-11&5&5\\
3&-1&-1&-1\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}
\ne0.
\]

Teraz rozważmy trzy akty \(a=M_0\), \(b=M_0\), \(c=M_1\):
- \(a\) z \(b\) komutują, więc \(a;b\) jest niedopuszczalne w kryterium niekomutowania;
- \(b\) z \(c\) nie komutują, więc \(b;c\) jest dopuszczalne, a wynikiem jest \(P=M_1M_0\);
- \(a=M_0\) nie komutuje z \(P\), więc \(a;(b;c)\) jest dopuszczalne.

Prawa strona jest określona, lewa nie. To jest kontrprzykład łączności na rzeczywistych generatorach P₀-Centroid, nie tylko na sztucznych funkcjach.

## 8. Centroid jako kontrola: całkowitość nie wytwarza selekcji

W Centroidzie \(M_i\) są całkowitymi, odwracalnymi przekształceniami \(\mathbb R^n\), z \(\det M_i=1/n\). Dlatego:
- dla kompozycji częściowych przez przecięcie obrazu i dziedziny każda para jest dopuszczalna;
- dla testu \(M_bM_a\ne M_b\) każda para jest dopuszczalna, bo \(M_b\) jest odwracalny, a \(M_a\ne I\);
- dla testu niekomutowania dostajemy inną relację, ale nie jest ona łączna jako dziedzina częściowego iloczynu.

Zatem istnieją trzy różne pojęcia:
1. **kompozytowalność:** czy wynik a jest dopuszczalnym wejściem b;
2. **odpowiedź:** czy b zmienia wynik, kiedy poprzedza go a;
3. **zależność od kolejności:** czy a i b nie komutują.

Nie są one równoważne. W szczególności niekomutowanie nie może zastąpić reguły kompozycji.

## 9. Co z tego wynika dla N-R2?

Mamy teraz najprostszy formalizm, który usuwa przestrzeń liniową i jawne obiekty, a zarazem zachowuje łączność: częściowe przekształcenia przestrzeni konfiguracji relacyjnych.

Ale cena jest jawna:
- nie wyprowadziliśmy \(Q\);
- nie wyprowadziliśmy dziedzin aktów;
- nie wyprowadziliśmy kryterium równości konfiguracji;
- nie wybraliśmy liczby profili.

To przesuwa pytanie, ale nie rozwiązuje go. Nowe pytanie brzmi: czy z samego aktu kompensacji można uzasadnić, że działa on tylko na pewnej części przestrzeni konfiguracji, i dlaczego ta część miałaby mieć określone przecięcia z dziedzinami innych aktów?

To jest teraz właściwy rdzeń N-R2.

## 10. Werdykt

- **✅** Częściowe przekształcenia konfiguracji dają naturalną, silnie łączną kompozycję.
- **✅** Można zdefiniować dopuszczalność bez jawnego podawania źródła i celu strzałki.
- **✅** Dla każdego n≥2 istnieje cykliczny kontrmodel z dokładnie n profilami i lokalnymi identycznościami.
- **❌** Kryterium „następny akt reaguje” \(T_bT_a\ne T_b\) nie jest łączne.
- **❌** Kryterium niekomutowania nie jest łączne — kontrprzykład uzyskany dla samych generatorów Centroidu K₄.
- **❌** Żadne z tych praw nie selekcjonuje n=4.
- **💡** Częściowe akty na konfiguracjach relacyjnych są kandydatem na minimalny formalizm pośredni. Trzeba dopiero wyprowadzić ich dziedziny i samą przestrzeń konfiguracji z relacji pierwotnej.

## 11. Następny krok

Teraz należy zbadać, czy dziedzina aktu kompensacji może być wyznaczona przez jego własną stabilność lub niezmiennik, a nie zadana z góry.

W szczególności:
1. czy dwa akty mają wspólny dopuszczalny stan dlatego, że zachowują ten sam niezmiennik;
2. czy relacja „zachowują wspólny niezmiennik” jest wystarczająca do kompozycji;
3. czy przecięcia dziedzin są stabilne przy składaniu;
4. czy otrzymujemy łączność bez dodatkowego aksjomatu.

Test musi zawierać kontrmodele n=3,4,5. Nie wolno uznać samej obecności K₄ w jednym przykładzie za selekcję czterech.

## 12. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
