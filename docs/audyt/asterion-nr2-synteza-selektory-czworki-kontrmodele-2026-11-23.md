# N-R2 — raport scalony: kompozytowalność, profile i źródło liczby cztery

**Wersja:** 1.0 (raport główny, aktualizowany w miejscu)  
**Data aktualizacji:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2.  
**Gałąź:** `audit/asterion-continuation-2026-11-20`  
**Status całości:** N-R2 otwarte. Wyniki szczegółowe poniżej rozdzielają twierdzenia, wyniki warunkowe, kontrmodele i hipotezy.  
**Poza zakresem:** MVP-02, wdrożenia laboratoryjne, 4D/głębia P₀, publikacyjne opracowanie wyników.

> **Zasada utrzymania:** to jest kanoniczny raport N-R2. Kolejne etapy będą integrowane przez nadpisanie tego pliku, nie przez tworzenie kolejnych równoległych raportów. Historia kolejnych wersji pozostaje w commitach Git. Dotychczasowe pliki szczegółowe są materiałem archiwalnym i nie będą dalej rozbudowywane.

## 0. Pytanie główne i werdykt

N-R2 pyta, czy z pierwotnej relacji — bez wcześniejszego zadania obiektów, indeksów, źródeł, celów ani liczby węzłów — można wyprowadzić:

1. profil/nośnik relacyjny;
2. regułę, kiedy jedna relacja może następować po drugiej;
3. koherentną kompozycję dla trzech i większej liczby relacji;
4. szczególną liczność cztery i geometrię (K_4).

**Werdykt na dziś:** istnieją poprawne konstrukcje kompozycji i profili, ale każda z nich wymaga dodatkowej struktury lub testu dopuszczalności. Ogólna kompozycja, sama łączność, semigroupoid, automat resztkowy, (S_4), (V_4), jeden stabilny profil ani sama zgodność par nie wymuszają czterech węzłów. W aparacie Centroid–Axis–Defect znaleziono kanoniczne (V_4), lecz dopiero po przyjęciu (K_4). Nie znaleziono dotąd mechanizmu, który wyprowadzałby tę strukturę przed nośnikiem.

**N-R2 pozostaje otwarte.** Najważniejszy wynik jest obecnie negatywny, ale precyzyjny: wiemy, które konstrukcje działają, jakie dodatkowe dane zakładają i gdzie dokładnie zaczyna się brakujący krok.

## 1. Kryteria statusu

- **✅** twierdzenie dowiedzione w podanym zakresie;
- **🔍** wynik częściowy, numeryczny lub zależny od dodatkowych warunków;
- **💡** hipoteza albo kandydat na brakujący aksjomat;
- **❌** roszczenie obalone kontrmodelem lub sprzeczne z rachunkiem.

Nie utożsamiamy wyniku warunkowego z wyprowadzeniem z korzeni P₀. Każde założenie nośnika, alfabetu, indeksów, operatorów, źródła/celu lub języka dopuszczalności musi być jawne.

## 2. Co znaczy kompozytowalność bez źródła i celu?

### 2.1. Relacja na wspólnym nośniku — rozwiązanie znane, ale niewystarczające

Jeżeli relacje (R,Ssubseteq X	imes X) są już dane na wspólnym zbiorze (X), to:
[
R;S={(x,z):exists yin X, (x,y)in R, (y,z)in S}
]
jest silnie łączne. Świadkiem sklejenia jest (y).

To nie rozwiązuje N-R2: wspólny nośnik (X), pozycje i ich tożsamość zostały przyjęte z góry. Wspólny element (y) pełni rolę interfejsu.

### 2.2. Ślady bez nośnika — no-go dla samej zgodności typów

Rozróżniamy:
1. typ śladu, określony do izomorfizmu;
2. konkretny egzemplarz śladu;
3. świadka, że koniec jednego śladu i początek drugiego są tym samym interfejsem.

Jeżeli reguła zna wyłącznie typy, dwa odrębne, izomorficzne egzemplarze są nierozróżnialne od jednego wspólnego egzemplarza. Zgodność do izomorfizmu nie dowodzi tożsamości interfejsu. Jeżeli reguła wymaga tego samego egzemplarza, wprowadza już tożsamość pozycji/nośnik. Jeżeli używa izomorfizmu jako świadka, potrzebuje dodatkowego wyboru mapowania i koherencji tych mapowań dla trójek.

**✅** Same typy śladów nie wystarczają do ustanowienia wspólnego interfejsu.  
**💡** Kandydatem na brakujący aksjomat jest struktura interfejsów z koherentnym prawem identyfikacji. Nie wykazano, że wynika ona z P₀-Relacje.

### 2.3. Zgodność par nie implikuje łączności

Nawet kompletny predykat (C(a,b)) mówiący, które pary są zgodne, nie określa wyniku kompozycji i nie wymusza łączności. Kontrprzykład na (A={0,1}):
[
xstar y=x(1-y).
]
Wszystkie pary są dopuszczalne, ale:
[
(1star0)star1=0,qquad
1star(0star1)=1.
]
**✅** Potrzebna jest nie tylko zgodność par, ale także reguła wyniku i warunek koherencji trójkowej.

## 3. Konstrukcje kompozycji i profili — co działa, a co jest założone

### 3.1. Semigroupoid bez jawnych obiektów

Można zacząć od zbioru strzałek i częściowego produktu, określonego tylko dla par kompozytowalnych, z aksjomatem łączności. Przy konwencji (ab) = najpierw (a), potem (b):
[
L(a)={b:ba	ext{ określone}},qquad
R(a)={b:ab	ext{ określone}}.
]
Jeśli każdy obiekt ma co najmniej jedną strzałkę wchodzącą i wychodzącą, relacje równości kontekstów odzyskują wspólne źródło i cel. Profile/obiekty można więc zrekonstruować z częściowej kompozycji.

To jest rekonstrukcja obiektów z semigroupoidu, nie wyprowadzenie kompozycji z samej relacji. Częściowy produkt i jego łączność są danymi wejściowymi. Ponadto skierowany cykl z dodatnimi ścieżkami daje dowolną liczbę profili i nie wymaga idempotentów.

### 3.2. Interfejsy operatorów rzędu jeden

Dla (D=uotimesphi):
[
U(D)=operatorname{Im}D=langle uangle,qquad
F(D)=operatorname{Ann}(ker D)=langlephiangle.
]
Można zdefiniować:
[
aightsquigarrow biff phi_b(u_a)
e0,
]
bo (D_bD_a=phi_b(u_a)u_botimesphi_a). Otrzymujemy łączną częściową kompozycję.

Koszt: przyjęto (V,V^*), obrazy i funkcjonały. Dla operatorów Centroidu wszystkie odpowiednie parowania są niezerowe, więc reguła nie wybiera interesującej częściowej sieci. Ogólny formalizm pozwala zakodować dowolny graf; sam nie wybiera (K_4).

### 3.3. Częściowe transformacje

Częściowe funkcje na zbiorze konfiguracji (Q), składane wtedy, gdy wynik pierwszej należy do dziedziny drugiej, dają silną łączność. Ale (Q), dziedziny i kryterium dopasowania są założone. Kryteria typu (T_bT_a
e T_b) albo niekomutowanie nie są łączne i mają kontrprzykłady.

### 3.4. Algebra sekwencji a algebra profili

Trzeba rozdzielać:
- warstwę sekwencji: nieprzemienny iloczyn operatorów (T_{A_k}cdots T_{A_1});
- warstwę profili: stabilne obserwable/konfiguracje, często z operacją przecięcia.

Profilowa dokładność:
[
Phi(BA)=Phi(A)capPhi(B)
]
wystarcza, by częściowy produkt oparty na niepustym wspólnym profilu był silnie łączny. Centroid spełnia ten warunek dla dodatnich słów; Scalar spełnia go dla pełnych rund na ustalonych grafach. Ogólne macierze stochastyczne go nie spełniają.

**Wniosek:** łączność można uzyskać z bogatszej struktury, ale nie wynika ona z samego predykatu zgodności par.

## 4. Profile przyszłych kontynuacji — wspólna konstrukcja behawioralna

Dla alfabetu aktów (A) i języka dopuszczalnych historii (mathcal Lsubseteq A^*), definiujemy:
[
F_h={zin A^*:hzinmathcal L},qquad
hsim_{mathcal L}kiff F_h=F_k.
]
Przejście po akcie (a) ma postać (delta_a(F_h)=F_{ha}), jeśli profil nie jest pusty. Jest dobrze określone niezależnie od reprezentanta. Kompozycja przejść jest silnie łączna; nie wymaga, by (mathcal L) był domknięty na fragmenty.

To jest mocny ogólny formalizm, ale kluczowe pytanie przesuwa się na wcześniejszy poziom: **skąd pochodzi (mathcal L)?** Sama konstrukcja resztkowa nie mówi, które historie są propagacyjne.

### 4.1. Wave

W Wave dopuszczalność oznacza istnienie niebanalnego modułu jednostkowego na przestrzeni relacyjnej.

Dla (W=02T13T):
[
chi_W(x)=rac{(x-1)(x+1)(256x^2-45x-1)}{256},
qquad det W=rac1{256}.
]
Widmo:
[
1, -1, rac{45+sqrt{3049}}{512},rac{45-sqrt{3049}}{512}.
]
Zatem (W) ma niebanalny relacyjny mod (-1) i jest propagacyjne.

Dla prefiksu (U=02T):
[
chi_U(x)=rac{(x-1)(16x^3+7x^2+2x+1)}{16}.
]
Pierwiastki czynnika kubicznego mają moduł w przedziale ([2/7,1/2]), więc poza konsensusem (U) nie jest propagacyjne. Jednak (U) ma przyszłą propagacyjną kontynuację (13T), bo (U(13T)=W).

**✅** Język propagacyjności Wave nie jest domknięty na fragmenty; istnieje historia niepropagacyjna, ale żywa.  
**🔍** Pełna klasyfikacja wszystkich profili resztkowych Wave pozostaje nieustalona.

### 4.2. Centroid

Niech (I(w)) będzie zbiorem różnych indeksów występujących w dodatnim słowie (w). Dla rodziny Centroidu:
[
dimmathcal I(w)=max(n-|I(w)|-1,0).
]
Język przetrwania niezerowego relacyjnego niezmiennika:
[
mathcal L_C={win A^+:|I(w)|le n-2}.
]
Jest factorialny. Profil przyszłości zależy dokładnie od zbioru już użytych indeksów (S), a przejście dodaje nowy indeks, o ile nie przekroczy granicy (n-2).

Dla (nge3) żywe profile odpowiadają podzbiorom (Ssubseteq A), (|S|le n-2), a ich liczba wynosi:
[
N_C(n)=sum_{r=0}^{n-2}inom nr.
]
Dla (n=4): (N_C(4)=1+4+6=11), nie cztery. Dla (n=3): (N_C(3)=4). Ta liczba stanów automatu nie jest selektorem (K_4).

**✅** Automat resztkowy Centroidu jest dokładnie opisaną obciętą kratą podzbiorów.  
**❌** Sama resztkowość nie wymusza czterech profili.

### 4.3. Scalar

Dla progowego A2 stabilne konfiguracje spełniają:
[
mathcal S_epsilon=
{r:orall i,j, |r_i-r_j|<epsilonRightarrow r_i=r_j}.
]
Każda stabilna konfiguracja jest nieruchoma pod każdym lokalnym aktem. Żadna niestabilna konfiguracja nie może osiągnąć stabilności po skończonej liczbie aktów:
[
T_w(x)inmathcal S_epsilon
iff xinmathcal S_epsilon.
]
Zatem język skończonego osiągnięcia stabilności jest (A^*) dla stanu już stabilnego i pusty dla niestabilnego.

Dla ścisłego progu (<epsilon), przedziały wypukłe różnych składowych grafu progowego są oddalone o co najmniej (epsilon). Każdy akt pozostaje w przedziale swojej składowej; składowe nie mogą się ponownie połączyć. Partycja indeksów na składowe tylko się rozdrabnia i stabilizuje po najwyżej (n-c_0) podziałach. Nie oznacza to zamrożenia krawędzi wewnątrz składowej.

Energia:
[
Phi_epsilon(x)=sum_{i<j}min{(x_i-x_j)^2,epsilon^2}
]
spada przy każdym lokalnym akcie co najmniej o ((|N_i|+2)Delta_i^2). Stąd (sum_tDelta_t^2<infty) dla dowolnego harmonogramu. Wyniki literaturowe o skończonej liczbie zmian topologii dla jednostajnie losowych aktywacji nie rozstrzygają każdego deterministycznego harmonogramu ograniczenie uczciwego.

**✅** Partycja na składowe może się tylko rozdrabniać.  
**🔍** Stabilizacja wszystkich wewnętrznych krawędzi i pełna asymptotyka dla każdego deterministycznego harmonogramu pozostają odrębnymi pytaniami.  
**❌** Sam graf progowy nie wyznacza przyszłości: ilościowe marginesy i kolejność aktualizacji mają znaczenie.

### 4.4. Porównanie korzeni

| Własność | Wave | Centroid | Scalar A2 |
|---|---|---|---|
| Test dopuszczalności | niebanalny mod jednostkowy | niezerowy niezmiennik po słowie | stabilność progowa |
| Domknięcie na fragmenty | nie | tak | skończone osiągnięcie: (A^*) albo (arnothing) |
| Nieakceptowana, ale żywa historia | tak | nie | nie dla skończonej stabilizacji |
| Profil | przyszłe kontynuacje | zbiory użytych/nieużytych indeksów | partycja i ilościowe marginesy |
| Liczba profili | nieustalona | dokładna; dla (n=4) równa 11 | zależna od kryterium i danych |

Wspólny automat przyszłych kontynuacji jest konstrukcją behawioralną. Nie ma dowodu, że profile Wave, Centroidu i Scalar są tym samym obiektem matematycznym ani że jeden test P₀-Relacje już je wyznacza.

## 5. Czy ogólna kompozycja wymusza cztery?

Nie. Kontrmodele pokazują dowolną liczność:
- półkrata łańcuchowa (S_n), (wedge=min): dowolne (n);
- półgrupa Brandta (B_n^0): (n) niezerowych idempotentów dla każdego (nge2);
- grupoid par: dowolne (n) obiektów;
- skierowany cykl dodatnich ścieżek: dowolne (n) profili, bez potrzeby idempotentów;
- język (L_n={a,a^2,ldots,a^n}): dokładnie (n) klas przyszłości;
- Scalar: jeden niebanalny kontrast może wystąpić dla dowolnego (n), np. przy dwóch składowych grafu.

Sama liczba idempotentów nie jest selektorem: (B_n^0) daje ich dowolną liczbę. Samo odzyskiwanie profili z kontekstów też nie jest selektorem: liczność cyklu jest dowolna.

## 6. Pięć nazwanych selektorów liczby cztery

Pięć selektorów to w rzeczywistości cztery formalnie odrębne typy, bo torsor (V_4) i regularne działanie (V_4) są równoważne.

| Selektor | Jawne założenie | Wniosek | Ograniczenie |
|---|---|---|---|
| A. Torsor (V_4) | Dwie niezależne komutujące inwolucje działają swobodnie i przechodnio | (|P|=4) | Trzeba wyprowadzić inwolucje i regularność |
| B. Wierne, przechodnie (V_4) | (V_4) działa wiernie i przechodnio na profilach | (|P|=4) | To ten sam torsor co A |
| C. Równowaga wymiarów | Pełny (K_n) i równość wymiarów sektorów różnic/cykli | (n-1=inom{n-1}{2}), więc (n=4) | Zasada równowagi jest dodatkowa |
| D. Minimalny stopień (S_4) | Grupa jest już (S_4), szukamy najmniejszego wiernego nośnika | (mu(S_4)=4) | Nie wyklucza większych nośników |
| E. Dokładnie jeden profil Centroidu | Dwa różne akty pozostawiają dokładnie 1 wymiar stabilny | (n-3=1), więc (n=4) | Własność konkretnej dynamiki, nie ogólnej relacji |

### 6.1. A i B — ta sama zasada

Dla działania (Hcong V_4) wiernego i przechodniego, ponieważ (H) jest abelowa, stabilizator dowolnego punktu jest jądrem działania. Wierność wymusza stabilizator trywialny, więc działanie jest swobodne:
[
|P|=|H|=4.
]
Odwrotnie, torsor z definicji jest działaniem swobodnym i przechodnim.

### 6.2. Równowaga wymiarów

Dla pełnego (K_n):
[
dimoperatorname{Im}d=n-1,qquad
dimker d^*=inom{n-1}{2}.
]
Ich równość dla (nge2) daje (n=4). Ale sama geometria (K_n) nie wymusza, by sektory miały równe wymiary.

### 6.3. Minimalny stopień (S_4)

(mu(S_4)=4): dla (mle3), (|S_m|le6<24), więc nie ma wiernego działania (S_4) na (m) punktach; naturalne działanie na czterech osiąga minimum. To minimalność nośnika dla już zadanej grupy, nie wyprowadzenie (S_4).

### 6.4. Profil Centroidu

Dla dodatniego słowa używającego indeksów (I):
[
dimPhi=max(n-|I|-1,0).
]
Dla dwóch różnych generatorów (dimPhi=max(n-3,0)). Dokładnie jeden wymiar daje (n=4); warunek jedynie niezerowy daje (nge4).

## 7. Centroid–Axis–Defect: czy (V_4) istnieje przed (K_4)?

### 7.1. Generatory Centroidu nie są inwolucjami

[
M_i=I+e_ic_i^T,qquad c_i=rac1nmathbf1-e_i.
]
Dla (n=4) na (V_ho) widmo (ar M_i) wynosi ({1,1,1/4}), zatem (M_i^2
e I), a (detar M_i=1/4).

Dla dodatniego słowa długości (k):
[
det(ar M_{i_k}cdotsar M_{i_1})=4^{-k}.
]
Inwolucja musi mieć wyznacznik (pm1), więc żadne niepuste dodatnie słowo nie jest inwolucją. Słowa z odwrotnościami wymagają osobnej klasyfikacji; nie można ich automatycznie uznać za źródło (V_4).

### 7.2. Komutatory Axis nie są półobrotami

Komutatory Liego (K_{ij}=[ar M_i,ar M_j]) są antysamosprzężone względem dodatniej metryki relacyjnej. Niezerowe operatory tego typu mają widmo czysto urojone (ewentualnie zero), więc nie spełniają (K_{ij}^2=I). Eksponentowanie i dobranie parametru do obrotu o (pi) wymaga dodatkowego wyboru generatora i normalizacji.

### 7.3. Gdzie pojawia się Klein four?

Dla rodziny czterech generatorów:
[
operatorname{Aut}(mathfrak g_4;{M_i})cong S_4.
]
To automorfizmy zachowujące wyróżnioną rodzinę generatorów; nie jest to pełna grupa automorfizmów samej algebry.

W (S_4) znajduje się jedyna normalna podgrupa Klein four:
[
V_4={e,(01)(23),(02)(13),(03)(12)}.
]
Jej trzy nieidentycznościowe elementy są komutującymi inwolucjami. W Axis działają jako trzy półobroty na (V_ho); w Defect jako trzy ortogonalne rotacje na (V_{m cyc}).

Ale Axis i Defect zaczynają od (K_4). Kierunek uzasadniony przez obecne korzenie to:
[
K_4longrightarrow S_4longrightarrow V_4,
]
nie odwrotnie.

Nie ma kanonicznego wyboru konkretnej pary spośród trzech nieidentycznościowych elementów (V_4): (S_4) permutuje je przechodnio.

### 7.4. Warunkowy selektor przez normalne (V_4)

Dla rodziny (n) generatorów Centroidu:
[
operatorname{Aut}(mathfrak g_n;{M_1,ldots,M_n})cong S_n.
]
Warunek „grupa symetrii musi zawierać kanoniczną normalną podgrupę (C_2	imes C_2)” wybiera (n=4), ponieważ w rodzinie (S_n) taka normalna podgrupa występuje dokładnie dla (n=4).

To rzeczywisty selektor warunkowy, ale jego koszt jest jawny: postulat normalnego (V_4) jest nowym aksjomatem. Korzenie P₀ nie wyjaśniają jeszcze, dlaczego ma on obowiązywać przed nośnikiem.

**Werdykt:** nie znaleziono dwóch kanonicznych, niezależnych inwolucji przed (K_4). Znaleziono (V_4) po przyjęciu czterowęzłowej struktury.

## 8. Kontrmodele dla utożsamień grupowych i geometrycznych

Samo (operatorname{Aut}cong S_4) nie oznacza czterech profili:
- sześć nieuporządkowanych par z ({1,2,3,4}) tworzy sześć profili, na których (S_4) działa wiernie i przechodnio;
- normalna (V_4) dzieli te sześć profili na trzy orbity po dwa;
- można mieć cztery profile z wiernym działaniem (S_4) i dodatkowy punkt stały, czyli pięć profili;
- sześć środków krawędzi (K_4) daje sześć geometrycznych profili.

Nie wolno utożsamiać:
[
operatorname{Aut}cong S_4Rightarrow |P|=4,
]
ani
[
V_4	riangleleft S_4Rightarrow V_4	ext{ działa regularnie na dowolnym }P.
]
Oba wnioski są fałszywe.

## 9. K₄, Centroid, Axis i Defect — ustalone fakty geometryczne

Dla (K_4):
[
G_4=4I-J,qquad
V_ho={xinmathbb R^4:sum_i x_i=0},qquad
p_0=	frac14(1,1,1,1).
]
Na (V_ho), (G_4=4I).

Środki krawędzi:
[
q_{ij}=	frac12(e_i+e_j)-p_0
]
tworzą regularny ośmiościan w trójwymiarowej przestrzeni (V_ho). Trzy pary przeciwległych krawędzi określają trzy ortogonalne osie, ale bez kanonicznego oznakowania XYZ i zwrotu.

Dla (U=mathbb R^6), (Bf_{ij}=q_{ij}):
[
BB^*=	frac12I_{V_ho},quad
P_{m mid}=2B^*B,quad
P_{m mid}^2=P_{m mid},quad
operatorname{rank}B=3.
]
Obraz rozpięty jest przez różnice par przeciwległych, jądro przez sumy. (B) zachowuje (V_{m std}), zeruje (mathbf1oplus V_2).

W Defect:
[
C^1(K_4)cong V_{m std}oplus(V_{m std}otimesmathrm{sign}),
quad
V_{m cyc}cong V_{m std}otimesmathrm{sign}.
]
Nie ma niezerowego (S_4)-splotnika (V_ho	o V_{m cyc}). (B^*B) i (P_{m cyc}) nie są proporcjonalne; nie wolno utożsamiać sektorów tylko z powodu wspólnego wymiaru 3. Po wyborze orientacji (V_ho), Hodge (*:V_ho	oLambda^2V_ho) jest (A_4)-ekwiwariantny, a nieparzyste permutacje zmieniają znak.

Te wyniki są poprawną matematyką geometrii (K_4). Nie są dowodem, że (K_4) wyłania się z pierwotnej relacji.

## 10. Co obecnie wynika z N-R2 — mapa statusów

| Teza | Status | Zakres |
|---|---|---|
| Relacje na wspólnym nośniku składają się łącznie | ✅ | Nośnik i świadek są założone |
| Semigroupoid pozwala odzyskać profile/obiekty | ✅ | Częściowy produkt i łączność są danymi |
| Typy śladów do izomorfizmu wyznaczają wspólny interfejs | ❌ | Kontrmodel dwóch rozłącznych kopii |
| Zgodność par implikuje łączność | ❌ | Jawny produkt na dwóch elementach |
| Profile resztkowe dają łączny automat | ✅ | Po zadaniu języka dopuszczalności |
| Sam automat resztkowy wymusza cztery profile | ❌ | Liczba profili jest dowolna; Centroid (n=4) ma 11 |
| Centroid, Scalar i Wave mają identyczne profile | ❌ | Kryteria i struktury są różne |
| Torsor (V_4) ma cztery punkty | ✅ | Regularne działanie |
| Samo (S_4) wymusza cztery profile | ❌ | Kontrmodel sześciu par i pięciu punktów |
| Równowaga wymiarów (K_n) wybiera (n=4) | ✅ warunkowo | Równość sektorów jest dodatkowym założeniem |
| Dwa akty Centroidu pozostawiają jeden wymiar przy (n=4) | ✅ | Konkretna rodzina operatorów |
| Centroid–Axis–Defect wyprowadza (V_4) przed (K_4) | ❌/otwarte | Znaleziono (V_4) dopiero po (K_4) |
| Pierwotna relacja sama wyznacza kompozytowalność | 💡/otwarte | Brakuje niezależnego prawa interfejsów i koherencji |
| Pierwotna relacja sama wymusza (K_4) | 💡/otwarte | Brak selektora wyprowadzonego z korzeni |

## 11. Najbliższy plan matematyczny

Kolejne kroki mają sprawdzać brakujący poziom, nie dopasowywać strukturę do oczekiwanego wyniku.

1. **Poziom przed Centroidem:** zbadać, czy P₀-Relacje i P₀-Samoodniesienia zawierają typ danych i operację, których własna grupa automorfizmów może być określona bez uprzedniego nośnika. Nie przypisywać im (V_4), dopóki nie ma takiej definicji.
2. **Świadek trójkowy:** poszukać pozytywnej realizacji koherentnego sklejenia bez jawnych źródeł/celów; jeżeli to niemożliwe, doprecyzować zakres no-go.
3. **Inwolucje:** nie szukać arbitralnych macierzy (T^2=I). Klasyfikować wyłącznie operatory kanoniczne wynikające z korzeni. Słowa z odwrotnościami w Centroidzie wymagają osobnego rachunku.
4. **Scalar:** rozdzielić stabilizację partycji składowych od stabilizacji krawędzi wewnętrznych; sprawdzić deterministyczne harmonogramy ograniczenie uczciwe.
5. **Replikowalność:** przygotować dokładne skrypty dla charakterystyki (W), komutatorów Centroidu i kontrprzykładów Scalar. To kontrola rachunku, nie zastępnik pytania o korzeń.
6. **Nie wracać do selekcji liczby cztery, dopóki nie pojawi się niezależna zasada:** nie przyjmować (K_4), czterech generatorów, czterech profili ani (V_4) jako danych wejściowych.

## 12. Integralność i historia

- Audyt dotyczy matematycznych korzeni P₀, zgodnie z zakresem ustalonym przez użytkownika.
- MVP-02 pozostaje poza zakresem i nie jest otwierane ani modyfikowane.
- Nie rozwijamy obecnie wątku 4D/głębi P₀.
- Zmiany zapisujemy wyłącznie na gałęzi `audit/asterion-continuation-2026-11-20`; bez merge/rebase z `main`.
- Wersje tego raportu są zachowane w historii commitów. Ten plik zastępuje potrzebę tworzenia kolejnych raportów postępu N-R2.
- Niezależna recenzja Vibe'a potwierdziła wskazane rachunki dokładne i kontrprzykłady; jej weryfikacja nie oznacza jeszcze, że skrypty replikacyjne są już w repozytorium.

**Konkluzja:** mamy kilka matematycznie poprawnych dróg od dodatkowej struktury do kompozycji, profili i liczby cztery. Nie mamy jeszcze drogi od samej pierwotnej relacji do tej dodatkowej struktury. To jest właściwe, nierozwiązane jądro N-R2.
