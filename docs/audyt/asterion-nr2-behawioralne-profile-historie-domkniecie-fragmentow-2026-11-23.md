# N-R2: profile jako behawioralna klasa historii aktów

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Punkty odniesienia:** P₀-Relacje v0.3 §§1, 4, 6–8; P₀-Philosophy v0.6.2 §§12–15; P₀-TAU v1.7.2 §1.1; raport o śladach bez nośnika (2026-11-23).  
**Status:** behawioralna równoważność historii jest kanoniczną relacją równoważności ✅; przy domknięciu języka dopuszczalnych historii na fragmenty iloczyn częściowy klas jest silnie łączny ✅; istnieją modele z dowolną liczbą profili bez nośnika węzłów ✅; sam alfabet aktów nie wybiera liczby profili ❌/kontrmodel; P₀-Relacje nie definiuje jeszcze testu dopuszczalności historii 💡/otwarte.

## 1. Motywacja: odejście od wspólnego interfejsu

Raport o śladach bez nośnika wykazał, że same typy śladów, rozumiane do izomorfizmu, nie wystarczają do ustalenia, czy dwa wystąpienia są jednym wspólnym interfejsem. Współdzielenie egzemplarza jest dodatkową strukturą.

Teraz zmieniamy podejście. Nie sklejamy końca jednego śladu z początkiem drugiego. Zaczynamy od pierwotnych aktów i ich historii, a profile definiujemy przez to, czy zachowują się tak samo we wszystkich możliwych kontekstach.

To jest zgodne z programowym ruchem P₀-Philosophy: akt kompensacji → ślad wielu aktów → stabilny wzorzec śladów. Nie oznacza jeszcze, że Philosophy dostarcza formalną definicję takiego śladu.

## 2. Historie aktów bez węzłów

Niech A będzie zbiorem typów aktów kompensacji. Nie zakładamy na A żadnej struktury źródło/cel ani indeksów węzłów.

Historią jest niepuste skończone słowo nad A:

\[
H=A^+.
\]

Konkatenacja \(uv\) oznacza wykonanie najpierw historii u, potem v. Sama konkatenacja jest totalna i łączna. Nie jest jeszcze prawem dopuszczalności — każda para słów da się formalnie skleić.

Potrzebujemy zatem zbioru historii dopuszczalnych (spójnych, zachowujących ślad):

\[
\mathcal L\subseteq A^+.
\]

Kluczowym warunkiem będzie **domknięcie na niepuste fragmenty ciągłe**:

\[
w\in\mathcal L
\implies
\text{każdy niepusty ciągły fragment słowa }w\text{ należy do }\mathcal L.
\tag{F}
\]

Warunek (F) mówi: jeśli cała historia zachowuje spójność, to każdy jej lokalny odcinek także jest dopuszczalny.

Nie jest to tautologia. To osobny aksjomat o stabilności śladu.

## 3. Kompozycja częściowa i łączność

Dla u,v∈\(\mathcal L\) definiujemy:

\[
u\diamond v=
\begin{cases}
uv,&uv\in\mathcal L,\\
\text{nieokreślone},&uv\notin\mathcal L.
\end{cases}
\]

### Twierdzenie

Jeżeli \(\mathcal L\) spełnia (F), to \(\diamond\) jest silnie łącznym działaniem częściowym:
- \((u\diamond v)\diamond w\) jest określone wtedy i tylko wtedy, gdy \(u\diamond(v\diamond w)\) jest określone;
- jeśli są określone, oba wyniki są równe \(uvw\).

### Dowód

Lewa strona jest określona wtedy i tylko wtedy, gdy:

\[
uv\in\mathcal L
\quad\text{i}\quad
uvw\in\mathcal L.
\]

Prawa strona jest określona wtedy i tylko wtedy, gdy:

\[
vw\in\mathcal L
\quad\text{i}\quad
uvw\in\mathcal L.
\]

Jeżeli \(uvw\in\mathcal L\), to z (F) wynika \(uv\in\mathcal L\) oraz \(vw\in\mathcal L\), ponieważ oba są niepustymi fragmentami ciągłymi słowa \(uvw\). Zatem obie strony są określone dokładnie wtedy, gdy \(uvw\in\mathcal L\). Wynikiem obu jest ten sam ciąg \(uvw\). ∎

**Istotne:** łączność nie wynika z samej sekwencji. Wynika z sekwencji plus aksjomatu (F), który zabrania sytuacji, w której cały ślad jest dopuszczalny, ale któryś z jego fragmentów nie jest.

## 4. Profile jako nierozróżnialne historie

Dla u,v∈\(\mathcal L\) definiujemy:

\[
u\sim_{\mathcal L}v
\iff
\forall p,q\in A^*:
\quad
puq\in\mathcal L
\iff
pvq\in\mathcal L.
\]

Słowa p i q mogą być puste. Relacja mówi, że u i v mają dokładnie takie samo zachowanie w każdym wcześniejszym i późniejszym kontekście aktów.

Jest to relacja równoważności:
- zwrotność i symetria wynikają z równoważności logicznej;
- przechodniość wynika z przechodniości równoważności przynależności do \(\mathcal L\).

Co ważniejsze, jest to **kongruencja dwustronna** konkatenacji. Jeżeli u~v, to dla dowolnych x,y:

\[
xuy\in\mathcal L
\iff
xvy\in\mathcal L.
\]

Można więc przejść do klas:

\[
\mathcal P=\mathcal L/\sim_{\mathcal L}.
\]

Klasa [u] jest profilem behawioralnym historii u. Dwie historie są tym samym profilem, jeżeli żaden możliwy kontekst nie potrafi ich rozróżnić.

Nie użyliśmy:
- zbioru węzłów;
- współrzędnych;
- źródła ani celu;
- wspólnej pozycji świadka;
- identyfikatora egzemplarza interfejsu.

Użyliśmy jedynie alfabetu aktów oraz testu dopuszczalności całej historii.

## 5. Iloczyn klas jest dobrze określony i łączny

Na profilach definiujemy:

\[
[u]\diamond[v]=[uv]
\quad\text{wtedy i tylko wtedy, gdy }uv\in\mathcal L.
\]

Ta definicja nie zależy od wyboru reprezentantów.

Jeżeli u~u' oraz v~v', to:
1. z u~u', przy kontekście q=v, mamy \(uv\in\mathcal L\iff u'v\in\mathcal L\);
2. z v~v', przy kontekście p=u', mamy \(u'v\in\mathcal L\iff u'v'\in\mathcal L\).

Zatem dopuszczalność kompozycji jest niezależna od reprezentantów. Z dwustronnej kongruencji wynika również:

\[
uv\sim_{\mathcal L}u'v'.
\]

Wartość klasy iloczynu jest więc jednoznaczna.

Łączność na klasach dziedziczy się z §3:

\[
([u]\diamond[v])\diamond[w]
=
[u]\diamond([v]\diamond[w])
=
[uvw]
\]

dokładnie wtedy, gdy \(uvw\in\mathcal L\).

**Wynik ✅:** domknięty na fragmenty język historii wraz z równoważnością kontekstową daje obiektowo-bezpostaciowy, silnie łączny częściowy półgrupowy układ profili — bez jawnie podanej listy obiektów i bez źródeł/celów.

Jeżeli do A⁺ dodamy słowo puste, otrzymamy globalną jednostkę. W tej konstrukcji jej nie dodajemy, więc nie zakładamy nawet globalnej identyczności.

## 6. Kontrmodel: jeden typ aktu daje dowolną liczbę profili

Niech alfabet zawiera tylko jeden akt:

\[
A=\{a\}.
\]

Dla dowolnego n≥1 definiujemy:

\[
\mathcal L_n=\{a,a^2,\ldots,a^n\}.
\]

Język jest domknięty na niepuste fragmenty: fragment \(a^k\) słowa \(a^m\) ma \(1\le k\le m\le n\), a więc nadal należy do \(\mathcal L_n\).

Profile [a], [a²], …, [aⁿ] są parami różne. Jeśli i<j, wybierzmy kontekst \(q=a^{n-j+1}\). Wówczas:

\[
a^j q=a^{n+1}\notin\mathcal L_n,
\]

ale:

\[
a^i q=a^{i+n-j+1}\in\mathcal L_n.
\]

Zatem \(a^i\not\sim_{\mathcal L_n}a^j\).

Otrzymujemy dokładnie n profili. Kompozycja ma postać:

\[
[a^i]\diamond[a^j]=
\begin{cases}
[a^{i+j}],&i+j\le n,\\
\text{nieokreślone},&i+j>n.
\end{cases}
\]

To jest łączne działanie częściowe, z n klasami profili.

| Maksymalna dopuszczalna długość n | Liczba profili |
|---:|---:|
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| dowolne n | n |

To bardzo mocny kontrmodel: nie potrzeba nawet kilku typów aktów, aby uzyskać dowolną liczbę profili. Liczba profili może być liczbą rozróżnialnych etapów historii.

Ale n zostało wpisane do testu dopuszczalności \(\mathcal L_n\) jako maksymalna długość. Nie zostało wyprowadzone z samej kompozycji.

## 7. Bez testu dopuszczalności nie ma selekcji profili

Dla tego samego alfabetu A={a} można wziąć:

\[
\mathcal L=A^+.
\]

Wtedy każda niepusta historia i każde jej otoczenie są dopuszczalne. Wszystkie historie są nierozróżnialne, więc iloraz ma jeden profil.

Dla \(\mathcal L_n\) z §6 mamy n profili.

Zatem ten sam pierwotny alfabet aktów daje:
- jeden profil, jeśli każda historia jest dopuszczalna;
- n profili, jeśli dopuszczalna jest historia o długości najwyżej n.

**Wniosek:** sama sekwencyjność aktów nie wyznacza profili. Selekcję wprowadza test, które historie zachowują spójny ślad. To właśnie jest brakująca reguła P₀.

## 8. Dlaczego domknięcie na fragmenty jest istotne

Nie wolno usunąć warunku (F) i nadal automatycznie przypisywać konstrukcji łączność.

Kontrprzykład: A={a,b,c} i:

\[
\mathcal L=\{a,b,c,ab,abc\}.
\]

Mamy:
- \(a\diamond b=ab\);
- \((a\diamond b)\diamond c=abc\) — określone;
- \(b\diamond c\) — nieokreślone, bo bc∉\(\mathcal L\);
- \(a\diamond(b\diamond c)\) — nieokreślone.

Lewa strona jest określona, prawa nie. Przyczyną jest brak fragmentu bc w języku mimo obecności abc.

A więc (F) nie jest ozdobnym założeniem. Jest dokładnie warunkiem, który wymusza wspólną dziedzinę obu nawiasowań w tej konstrukcji.

Czy P₀ powinno go przyjąć? Nie wiadomo. Jeśli kompensacja może być dopuszczalna wyłącznie w kontekście większej całości, (F) może być fałszywe. Trzeba to przetestować, nie zakładać.

## 9. Związek z korzeniami P₀

### P₀-Philosophy

§12 opisuje pytanie „co potrafi przetrwać jako organizacja aktów kompensacji?”. §15 przedstawia ciąg kompensacja → trwałe relacje → struktury jako program badawczy, a nie udowodniony łańcuch.

Nasze \(\mathcal L\) jest kandydatem na operacyjną wersję „przetrwania historii”: historia należy do \(\mathcal L\), jeśli zachowuje spójny ślad. Równoważność \(\sim_{\mathcal L}\) daje „trwały wzorzec śladów” jako klasę historii nierozróżnialnych w każdym kontekście.

Ale Philosophy nie definiuje \(\mathcal L\), funkcji śladu ani testu przetrwania. To nadal propozycja formalizacji, nie wynik odzyskany z tego korzenia.

### P₀-TAU

TAU daje motywację sekwencyjności — „kto mówi, kto słucha, kiedy” — oraz kolejność aktualizacji. W naszym formalizmie kolejność jest zachowana przez konkatenację słów.

Jednak TAU nie wyprowadza języka dopuszczalnych historii \(\mathcal L\). Aksjomat sekwencyjności nie jest aksjomatem domknięcia na fragmenty.

### P₀-Relacje

§4 deklaruje \(R_t\to D_t\to C_t\to R_{t+1}\), a §6 zapisuje \(R_{t+1}=F(R_t)\), lecz F pozostaje niezdefiniowane. Nie ma też predykatu, który rozstrzyga, czy dana historia aktów zachowuje spójny ślad.

Proponowana redukcja wymagałaby określenia:

\[
\mathcal L=
\{w\in A^+:\text{ślad historii }w\text{ spełnia kryterium spójności}\}.
\]

Następnie należałoby dowieść, że \(\mathcal L\) jest zamknięty na fragmenty i że powstałe klasy są stabilnymi wzorcami, a nie tylko klasami długości czy składni.

### P₀-Wave

Wave dostarcza przykładu, w którym słowa operatorowe niosą historię, a projektory opisują podprzestrzenie, które przetrwały dane słowo. To jest bliskie idei profilu behawioralnego, ale obecny formalizm Wave nadal używa zadanego alfabetu operatorów i wspólnej przestrzeni liniowej. Nie stanowi zatem jeszcze nośnikowo-bezpostaciowego wyprowadzenia \(\mathcal L\).

## 10. Werdykt

- **✅** Równoważność kontekstowa historii jest kanoniczną relacją równoważności i kongruencją dwustronną.
- **✅** Jeśli język dopuszczalnych historii jest zamknięty na niepuste fragmenty, częściowa konkatenacja profili jest silnie łączna.
- **✅** Profile można otrzymać jako klasy historii bez jawnych węzłów, źródeł, celów i liniowych współrzędnych.
- **✅** Już jeden typ aktu może dać dowolną liczbę n profili.
- **❌** Sama sekwencyjność i sama konkatenacja nie wybierają n=4 ani nawet nie wybierają liczby profili.
- **❌** Bez testu dopuszczalności wszystkie historie mogą zlać się w jeden profil; przy innym teście mogą dać dowolne n.
- **💡** Język historii zachowujących spójny ślad jest konkretnym kandydatem na brakującą regułę N-R2.
- **💡** Domknięcie na fragmenty jest minimalnym kandydatem na aksjomat koherencji wymagany do łączności w tym modelu; trzeba sprawdzić, czy wynika z dynamiki kompensacji.

## 11. Następny test

Nie należy teraz szukać geometrii K₄. Najpierw trzeba nadać operacyjną treść \(\mathcal L\).

Proponuję trzy kontrole:

1. **Test zaniku:** czy istnieje historia, której pełny ślad jest trwały, ale jakiś jej fragment nie jest? Jeśli tak, aksjomat (F) odpada.
2. **Test kontekstowy:** czy dwie różne historie mogą być nierozróżnialne dla wszystkich dalszych i wcześniejszych aktów? Jeśli nie, profil behawioralny jest zbyt drobny i obiekty nie emergują.
3. **Test replikacji:** czy \(\mathcal L\) da się obliczyć lub rozpoznać z istniejących operatorów Centroid/Scalar/Wave bez dopisywania ukrytych indeksów?

Dopiero jeżeli konkretny korzeń dostarczy \(\mathcal L\), liczba klas ilorazu będzie wynikiem, a nie parametrem.

## 12. Integralność zakresu

Analiza dotyczy matematycznych korzeni N-R2. Nie modyfikuje P₀-Relacje ani żadnego filaru. MVP-02 pozostaje poza zakresem. Zapis wyłącznie na gałęzi audytowej; bez merge/rebase z main.
