# N-R2: profile resztkowy — nierozróżnialność przyszłych kontynuacji i kompozycja częściowa

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Punkty odniesienia:** P₀-Wave v0.6.1 §§1–4; P₀-Philosophy v0.6.2 §§12–15; poprzedni raport Asteriona o behawioralnych profilach historii; raport o śladach bez nośnika (2026-11-23).  
**Status:** profil jako zbiór dopuszczalnych kontynuacji jest kanoniczną klasą behawioralną ✅; akty indukują dobrze określone częściowe przejścia na profilach ✅; złożenie przejść jest silnie łączne bez domknięcia języka na fragmenty ✅; propagacyjność Wave nie jest domknięta na fragmenty — dokładny kontrprzykład ✅; n profili dla dowolnego n nadal możliwe ✅; wyprowadzenie testu dopuszczalnych kontynuacji z pierwotnej relacji P₀ pozostaje otwarte 💡.

## 1. Korekta po poprzednim modelu

Poprzedni raport używał języka dopuszczalnych historii \(\mathcal L\) domkniętego na wszystkie niepuste fragmenty. Warunek ten gwarantował silną łączność częściowego konkatenowania historii.

Jednak nie jest jasne, czy P₀ powinno spełniać taki warunek. Historia może być niepropagacyjna w danym momencie, a mimo to późniejsza sekwencja może odzyskać stabilny mod. W takim przypadku wcześniejszy fragment nie jest dopuszczalną historią samą w sobie, ale jest stanem, z którego można dojść do historii dopuszczalnej.

P₀-Wave dostarcza dokładnego kontrprzykładu dla domknięcia na fragmenty. Dlatego potrzebujemy pojęcia, które pamięta nie tylko, czy historia jest teraz dopuszczalna, lecz także jakie dalsze kontynuacje pozostają możliwe.

## 2. Język historii i jej przyszły profil

Niech A będzie alfabetem aktów. Niech:

\[
\mathcal L\subseteq A^+
\]

oznacza zbiór historii propagacyjnych / zachowujących relacyjny ślad. Nie zakładamy, że \(\mathcal L\) jest domknięty na fragmenty.

Dla każdej historii h∈A* definiujemy jej **resztkowy profil przyszłości**:

\[
F_h=\{z\in A^*:hz\in\mathcal L\}.
\]

\(F_h\) jest zbiorem wszystkich dalszych sekwencji, które po historii h doprowadzą do historii należącej do \(\mathcal L\).

Dwie historie są behawioralnie nierozróżnialne w przyszłości, gdy:

\[
h\approx_{\mathcal L}k
\iff
F_h=F_k
\iff
\forall z\in A^*:
(hz\in\mathcal L\iff kz\in\mathcal L).
\]

Profil nie mówi, jaki był początek ani koniec historii. Mówi, jakie kontynuacje są z niej jeszcze możliwe.

To relacja równoważności, ponieważ jest równością zbiorów przyszłych kontynuacji.

## 3. Akty działają na profilach — definicja przejścia

Dla aktu a∈A definiujemy częściowe przejście:

\[
\delta_a(F_h)=F_{ha}
\quad\text{wtedy i tylko wtedy, gdy }F_{ha}\ne\varnothing.
\]

Jeśli \(F_{ha}=\varnothing\), to po wykonaniu a nie istnieje żadna dalsza kontynuacja, która doprowadziłaby do historii dopuszczalnej. Taki akt prowadzi do martwego końca i nie jest przejściem w częściowym systemie profili.

### Lemat: przejście jest dobrze określone na klasach profili

Załóżmy \(F_h=F_k\). Wówczas dla każdego z∈A*:

\[
haz\in\mathcal L
\iff
az\in F_h
\iff
az\in F_k
\iff
kaz\in\mathcal L.
\]

Zatem \(F_{ha}=F_{ka}\). Wynik \(\delta_a(F_h)\) nie zależy od reprezentanta historii h.

**Wynik ✅:** nie trzeba pamiętać całej historii. Wystarcza jej klasa przyszłych kontynuacji.

## 4. Twierdzenie: częściowe przejścia są silnie łączne

Dla słowa \(u=a_1\cdots a_m\) definiujemy:

\[
\delta_u(F_h)=F_{hu},
\]

o ile \(F_{hu}\ne\varnothing\).

Jeżeli \(F_{hu}\ne\varnothing\), istnieje z∈A* takie, że \(huz\in\mathcal L\). Każdy prefiks v słowa u ma wtedy niepusty profil:

\[
F_{hv}\ne\varnothing,
\]

bo dalszym uzupełnieniem jest pozostała część u oraz z.

W konsekwencji wszystkie przejścia pośrednie w sekwencji u są określone, gdy tylko profil końcowy jest niepusty.

Dla dwóch słów u,v:

\[
\delta_v\circ\delta_u(F_h)=F_{huv}
\]

jest określone dokładnie wtedy, gdy \(F_{huv}\ne\varnothing\). Nie ma znaczenia, czy najpierw grupujemy u z v, czy v jest już złożone z kolejnych liter.

Dla trzech słów u,v,w:

\[
(\delta_w\circ\delta_v)\circ\delta_u
=
\delta_w\circ(\delta_v\circ\delta_u)
\]

jako częściowe przejścia: obie strony mają dokładnie tę samą dziedzinę, złożoną z profili \(F_h\), dla których \(F_{huvw}\ne\varnothing\), i dają \(F_{huvw}\).

**Wynik ✅:** częściowa kompozycja aktów na profilach resztkowych jest silnie łączna. Nie wymaga domknięcia \(\mathcal L\) na fragmenty.

Różnica wobec poprzedniego modelu jest zasadnicza:
- poprzednio składaliśmy tylko historie już dopuszczalne;
- teraz profil historii może być żywy, choć sama historia jeszcze nie jest dopuszczalna, o ile istnieje dalsze uzupełnienie prowadzące do dopuszczalnego śladu.

## 5. Test na konkretnym słowie P₀-Wave

P₀-Wave v0.6.1 podaje słowo:

\[
W=02T13T
\]

jako propagacyjne. Jego spektrum obejmuje:

\[
\{-0.02,\ 0.196,\ 1,\ -1\}.
\]

Zatem istnieje relacyjny mod \(\lambda=-1\), a więc \(W\in\mathcal L_{\mathrm{Wave}}\).

Sprawdźmy jego początkowy fragment:

\[
U=02T.
\]

Dla konwencji Wave \(\rho(c_1\cdots c_L)=a_L\cdots a_1\), z \(M_i=I+e_ic_i^T\), \(c_i=\frac14\mathbf1-e_i\), i cyklicznym T (0123), dokładny rachunek daje:

\[
\chi_{\rho(U)}(x)
=
(x-1)\frac{16x^3+7x^2+2x+1}{16}.
\]

Dla wielomianu \(16x^3+7x^2+2x+1\) współczynniki w porządku rosnących potęg to 1,2,7,16. Z twierdzenia Eneströma–Kakeyi wszystkie jego pierwiastki spełniają:

\[
\frac27\le|\lambda|\le\frac12.
\]

Jedyną wartością własną na okręgu jednostkowym jest więc \(\lambda=1\), należąca do globalnego kierunku \(\mathbf1\). Na części relacyjnej U nie ma niebanalnego modu \(|\lambda|=1\).

Wniosek:

\[
U\notin\mathcal L_{\mathrm{Wave}},
\qquad
W\in\mathcal L_{\mathrm{Wave}}.
\]

Ale:

\[
F_U\ne\varnothing,
\]

ponieważ sufiks \(13T\) prowadzi do W, a W jest propagacyjne.

To pokazuje dokładnie, dlaczego profil resztkowy jest właściwszy od prostego testu propagacyjności fragmentu: historia U nie ma jeszcze stabilnego modu, lecz nie jest martwa — ma możliwą kontynuację.

## 6. Co oznacza kompozytowalność w tym modelu?

W poprzednich próbach szukaliśmy globalnego predykatu:

\[
C(a,b)\in\{0,1\},
\]

który mówiłby, czy akt a może być połączony z aktem b niezależnie od kontekstu.

Tutaj kompozytowalność jest zależna od profilu:

\[
\delta_b\circ\delta_a
\text{ jest określone w profilu }F_h
\iff
F_{hab}\ne\varnothing.
\]

To ważna zmiana. Ta sama para aktów może być dopuszczalna w jednym profilu i niedopuszczalna w innym. Nie próbujemy więc definiować zgodności „samej pary” bez kontekstu. Kontekst nie jest jednak zewnętrznym obiektem lub węzłem — jest klasą przyszłego zachowania historii.

W ten sposób:
- historie są pierwotnymi zapisami sekwencji aktów;
- profile są klasami identycznych możliwości dalszego działania;
- akty są częściowymi przejściami między profilami;
- kompozycja przejść jest łączna.

Jest to automat resztkowy, ale jego stany nie zostały zadane z góry. Powstają jako równoważności historii.

## 7. Kontrmodel liczności: znów dowolne n

Weźmy pojedynczy akt a i język:

\[
\mathcal L_n=\{a,a^2,\ldots,a^n\}.
\]

Dla historii \(a^k\), \(1\le k\le n\):

\[
F_{a^k}=
\{\varepsilon,a,a^2,\ldots,a^{n-k}\}.
\]

Profile \(F_a,F_{a^2},\ldots,F_{a^n}\) są parami różne, ponieważ zawierają różne maksymalne długości możliwej kontynuacji.

Otrzymujemy n profili i przejścia:

\[
F_{a^k}\xrightarrow{a}F_{a^{k+1}}
\quad(k<n),
\]

a z \(F_{a^n}\) nie ma już przejścia a.

Zatem profilowa liczność pozostaje dowolna. Dla n=3,4,5 otrzymujemy odpowiednio trzy, cztery i pięć profili.

Samo przejście do profili resztkowych nie wyprowadza czterech. Wybór n jest zapisany w kryterium dopuszczalnej długości historii.

## 8. Związek z wcześniejszym no-go o wspólnych interfejsach

Ta konstrukcja nie obala no-go dla typów śladów:
- nie identyfikuje dwóch śladów przez podobieństwo;
- nie zakłada, że koniec jednej relacji jest tym samym egzemplarzem co początek drugiej;
- nie używa izomorfizmu interfejsów jako substytutu tożsamości.

Zamiast tego wprowadza inny rodzaj danych: test, czy istnieje przyszła kontynuacja historii, która jest dopuszczalna.

Wspólna tożsamość interfejsu nie jest wymagana, ale pojawia się nowa struktura: język \(\mathcal L\) lub funkcja oceny historii. Bez niej profile resztkowe nie są określone.

To przesuwa brakujący aksjomat z „wspólnego nośnika interfejsów” na „wewnętrzne prawo przetrwania historii”.

## 9. Związek z korzeniami P₀

### P₀-Wave

Wave dostarcza konkretny test historii: propagacyjność, czyli istnienie niebanalnego modu \(|\lambda|=1\). Jego język nie jest domknięty na fragmenty, ale może nadal generować profile resztkowe i częściowy automat przejść.

Nie dowodzi to, że taka sama konstrukcja jest właściwym rdzeniem P₀-Relacje. Pokazuje, że nie trzeba wymagać lokalnej propagacyjności każdego fragmentu.

### P₀-Philosophy

§12 i §15 stawiają stabilność organizacji aktów i trwały wzorzec śladów jako program interpretacyjny. Profil resztkowy daje temu możliwą formalną postać: trwały wzorzec to nie stan materialny, lecz zbiór wszystkich dalszych historii zgodnych z dotychczasowym przebiegiem.

### P₀-Relacje

§6 ma \(R_{t+1}=F(R_t)\), ale F jest niezdefiniowane. Aby uzyskać \(\mathcal L\), trzeba określić, co znaczy, że historia aktów jest dopuszczalna lub propagacyjna. Dopiero wtedy resztkowe profile powstaną kanonicznie.

## 10. Werdykt

- **✅** Równość zbiorów przyszłych kontynuacji daje kanoniczną równoważność behawioralną historii.
- **✅** Każdy akt indukuje dobrze określone częściowe przejście na profilach resztkowych.
- **✅** Kompozycja tych przejść jest silnie łączna bez domknięcia języka historii na fragmenty.
- **✅** W P₀-Wave istnieje dokładny przykład: \(02T13T\) jest propagacyjne, podczas gdy jego fragment \(02T\) nie jest; jednak \(02T\) ma przyszłą propagacyjną kontynuację \(13T\).
- **✅** Profile resztkowe mogą powstać bez uprzednio zadanej listy węzłów i bez identyfikowania wspólnych końców/początków.
- **❌** Nie istnieje na tej podstawie globalne kryterium zgodności pary aktów niezależne od profilu; dopuszczalność jest kontekstowa.
- **❌** Liczba profili nadal może być dowolna; n=4 nie wynika z samej konstrukcji.
- **💡** Profil resztkowy jest najmocniejszym dotąd kandydatem na relacyjny „stan” wyłaniany z historii aktów, a nie zakładany z góry.

## 11. Następny test

Następnie należy sprawdzić, czy profil resztkowy może być zdefiniowany z istniejących danych P₀ bez zewnętrznego języka akceptacji:
1. w Wave — automatycznie z kryterium propagacyjności;
2. w Scalar — z kryterium istnienia przyszłego rozdzielenia lub utrzymania domen;
3. w Centroid — z kryterium przeżycia niebanalnego profilu po dalszych słowach generatorów;
4. w P₀-Relacje — jako ogólne prawo, które te trzy testy odzyskuje.

Kluczowa próba: czy te trzy korzenie dają izomorficzne lub redukowalne profile resztkowe, czy też jedynie podobnie brzmiące, ale matematycznie różne konstrukcje?

Nie dopisywać n=4 ani V₄ do definicji przed tym testem.

## 12. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. MVP-02 nie było otwierane ani modyfikowane. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
