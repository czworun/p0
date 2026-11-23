# P₀ — Centroid–Axis–Defect: czy istnieją kanoniczne inwolucje przed K₄?

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; poszukiwanie dwóch niezależnych, komutujących inwolucji, które mogłyby wymusić czteroelementowy nośnik.  
**Poza zakresem:** MVP-02, procedury laboratoryjne, pakiety replikacyjne.  
**Źródła:** `main`, commit `e4ac4a6d64c4a69983d7378bc5e82d961bb49f5c`; P₀-Centroid v5.2-zmiany, P₀-Axis v0.3, P₀-Defect v0.8, P₀-Relacje v0.3.  
**Poprzedni raport:** `asterion-nr2-wymuszenie-czterech-idempotentow-2026-11-23.md`.

## 0. Wynik

W obecnym aparacie Centroid–Axis–Defect **nie znalazłem pary dwóch kanonicznych, komutujących inwolucji, która istniałaby przed przyjęciem K₄**.

Znalazłem natomiast dokładnie taką strukturę *po* przyjęciu K₄: jedyną normalną podgrupę Kleina
[
V_4={e,(01)(23),(02)(13),(03)(12)}	riangleleft S_4.
]
Jej trzy nieidentycznościowe elementy są wzajemnie komutującymi inwolucjami i działają na (V_\rho) jako trzy półobroty wokół osi Axis. To jest mocna zgodność Centroid–Axis–Defect, ale kierunek zależności pozostaje:
[
K_4\longrightarrow S_4\longrightarrow V_4,
]
nie odwrotnie.

Istnieje warunkowe kryterium, które mogłoby wybrać (n=4): wymagać, aby pełna grupa symetrii rodziny operacji miała kanoniczną normalną podgrupę (C_2\times C_2). Dla rodziny Centroidu o (n) generatorach grupa symetrii zachowująca tę rodzinę jest (S_n), a spośród (S_n) taka normalna podgrupa istnieje dokładnie dla (n=4). Korzenie P₀ nie uzasadniają jednak jeszcze tego warunku.

## 1. Co dokładnie liczy się jako inwolucja?

Inwolucją nazywam tu element grupy lub odwracalny operator (T), dla którego
[
T^2=I,qquad T\ne I.
]
Samo występowanie operatora o kwadracie równym identyczności nie wystarczy do rozwiązania N‑R2. Potrzebne są jeszcze:
- kanoniczność (operator jest wyznaczony przez strukturę, nie wybrany z wielu równoważnych);
- niezależność (dwie inwolucje nie są tym samym elementem);
- komutowanie;
- brak wcześniejszego użycia czterech indeksowanych węzłów lub generatorów.

Rozdzielam trzy różne rzeczy:
1. operatory aktualizacji (M_i);
2. elementy algebry Liego, np. komutatory ([M_i,M_j]);
3. automorfizmy permutujące rodzinę generatorów.

W korzeniach te obiekty żyją na różnych poziomach. Nie wolno nazywać ich zamiennie „operacjami relacyjnymi”.

## 2. Centroid: generatory nie są inwolucjami

W Centroid v5.2 operatory aktualizacji mają postać
[
M_i=I+e_i c_i^T,qquad c_i=\frac1n\mathbf1-e_i.
]
Po przejściu do relacyjnej reprezentacji (V_\rho), P₀-Axis §14 podaje dla (n=4):
[
\operatorname{spec}(\rho_B(M_i))
=\left\{1,1,\frac14\right\}.
]
W konsekwencji:
[
\rho_B(M_i)^2\ne I,qquad
\det\rho_B(M_i)=\frac14.
]
Operator aktualizacji nie jest zatem inwolucją. Nie jest też idempotentem (M_i^2=M_i). Wartość własna (1/4) wystarcza do odrzucenia obu utożsamień.

Dla niepustego słowa złożonego wyłącznie z (k) operatorów aktualizacji, bez odwrotności,
[
W=\rho_B(M_{i_k})\cdots\rho_B(M_{i_1}),
qquad
\det W=4^{-k}.
]
Ponieważ wyznacznik inwolucji musi wynosić (+1) lub (-1), żadne niepuste słowo dodatnie w tych generatorach nie jest inwolucją.

Dopuszczenie odwrotności osłabia ten prosty test: słowo z równą algebraiczną liczbą generatorów i odwrotności może mieć wyznacznik 1. To nie dowodzi, że nie istnieją w grupie słowa będące inwolucjami. Wymagałoby to osobnej klasyfikacji. Niech \(\bar M_i\) oznacza operator Centroidu zapisany na wycentrowanej przestrzeni \(V_\rho\) (w bazie osiowej Axis), a nie surową macierz aktualizacji na całym \(\mathbb R^4\). Sprawdzony reprezentatywny komutator grupowy
[
C_{01}=\bar M_0\bar M_1\bar M_0^{-1}\bar M_1^{-1}
]
nie jest inwolucją: jego wielomian charakterystyczny w (V_\rho) wynosi
[
(\lambda-1)\left(\lambda^2-\frac32\lambda+1\right).
]
Para nierzeczywistych pierwiastków ma moduł 1 i (2\cos\theta=3/2), więc (\cos\theta=3/4). Z twierdzenia Nivena (\theta/\pi) nie jest wymierne; ten komutator ma nieskończony rząd. Jest to kontrola konkretnego słowa, nie twierdzenie o wszystkich słowach grupy.

**Wniosek 2 — ✅.** Rodzina lokalnych aktualizacji Centroidu nie dostarcza inwolucji jako swoich podstawowych generatorów. Proste dodatnie złożenia także nie są inwolucjami.

## 3. Axis: komutator Liego nie jest półobrotem

P₀-Axis §15 definiuje
[
K_{ij}=[\rho_B(M_i),\rho_B(M_j)].
]
To element algebry Liego, antysamosprzężony względem metryki relacyjnej:
[
K_{ij}^{*_{G_4}}=-K_{ij}.
]
Dla dodatnio określonej metryki niezerowy operator antysamosprzężony ma widmo czysto urojone (i ewentualnie zero), więc nie może spełniać (K_{ij}^2=I). Nie jest inwolucją.

Można oczywiście eksponencjować (K_{ij}) i dobrać parametr tak, aby otrzymać obrót o (\pi). To jednak wymaga:
1. wyboru konkretnego (K_{ij}) spośród sześciu;
2. normalizacji jego prędkości kątowej;
3. ustalenia parametru odpowiadającego dokładnie (\pi).

Axis §16 sam oznacza dodatkową strukturę sześciu kierunków jako otwartą. Ponadto sześć (K_{ij}) nie jest tym samym co trzy podwójne transpozycje w (S_4). Pierwsze są generatorami infinitesymalnymi otrzymanymi z par operatorów; drugie są skończonymi automorfizmami permutującymi cztery węzły.

**Wniosek 3 — ✅.** Nie wolno utożsamiać komutatorów Liego (K_{ij}) z inwolucjami grupy (V_4). Ewentualne półobroty z eksponenty są konstrukcją dodatkową, nie surowymi generatorami.

## 4. Gdzie naprawdę pojawia się (V_4)?

### 4.1. Centroid: symetria rodziny, nie samej algebry

Centroid v5.2 rozlicza korektę:
[
\operatorname{Aut}(\mathfrak g_4)\not\cong S_4,
]
bo pełna grupa automorfizmów algebry jest nieskończona.

Poprawne twierdzenie brzmi:
[
\boxed{\operatorname{Aut}(\mathfrak g_4;\{M_i\})\cong S_4.}
]
To automorfizmy zachowujące *wyróżnioną rodzinę czterech generatorów*. Macierz permutacji (P_\pi) spełnia
[
P_\pi M_iP_\pi^{-1}=M_{\pi(i)}.
]
Czyli (S_4) pojawia się dlatego, że rodzina ma cztery indeksowane operatory. Nie jest to grupa wyprowadzona z algebry (\mathfrak g_4) bez danych generatorów.

### 4.2. Jedyna normalna grupa Kleina

W (S_4) istnieje jedyna normalna podgrupa izomorficzna z (C_2\times C_2):
[
V_4=\{e,a,b,c\},
]
gdzie
[
a=(01)(23),\quad
b=(02)(13),\quad
c=(03)(12).
]
Spełnia ona:
[
a^2=b^2=c^2=e,qquad ab=ba=c,
]
oraz cyklicznie. Każde dwa różne elementy spośród (a,b,c) generują całe (V_4).

To jest kanoniczny *podgrupowy obiekt* wewnątrz (S_4), ponieważ jest jedyną normalną podgrupą tego typu. Nie ma jednak kanonicznego wyboru konkretnej pary generatorów: sprzężenia przez (S_4) permutują (a,b,c) dowolnie (działanie ilorazowe (S_4/V_4\cong S_3)). Żadna para z trzech elementów nie jest niezmiennicza pod całym (S_4).

### 4.3. Axis i Defect potwierdzają tę samą strukturę po K₄

W bazie trzech osi relacyjnych Axis, elementy (a,b,c) działają na (V_\rho) jako:
[
\rho(a)=\operatorname{diag}(1,-1,-1),
]
[
\rho(b)=\operatorname{diag}(-1,1,-1),
]
[
\rho(c)=\operatorname{diag}(-1,-1,1).
]
Są to trzy wzajemnie komutujące półobroty o (180^\circ), a ich osie są trzema parami przeciwległych krawędzi K₄.

P₀-Defect v0.8 §6 podaje tę samą grupę:
[
V_4=\{e,(12)(34),(13)(24),(14)(23)\},
]
działającą na (V_{\rm cyc}) jako trzy wzajemnie ortogonalne rotacje o (180^\circ). Jest to spójna realizacja tej samej kombinatoryki.

Ale w obu dokumentach wejściem jest już (K_4). Axis zaczyna od pełnego grafu na czterech wierzchołkach (§1), a dopiero potem wydobywa trzy przeciwległe pary (§3). Defect pracuje na (C^1(K_4)). Zatem obecność (V_4) w tych korzeniach jest potwierdzeniem struktury (K_4), nie źródłem czterech węzłów.

## 5. Warunkowy selektor: kiedy (S_n) wymusza (n=4)?

Centroid v5.2 dowodzi dla (n=4), że automorfizmy zachowujące rodzinę generatorów dają (S_4). Dowód uogólnia się bezpośrednio na rodzinę (n) generatorów:
[
\operatorname{Aut}(\mathfrak g_n;\{M_1,\ldots,M_n\})\cong S_n.
]
Permutacje indeksów działają przez sprzężenie; odwrotnie, automorfizm zachowujący zbiór generatorów jest wyznaczony przez permutację tych generatorów, ponieważ generują całą algebrę.

Dla (S_n), (n\ge2), zachodzi:
[
S_n\text{ ma normalną podgrupę }C_2\times C_2
\quad\Longleftrightarrow\quad n=4.
]
Dla (S_4) jest to dokładnie normalne (V_4) z podwójnymi transpozycjami. Dla (n\ge5) klasyfikacja normalnych podgrup (S_n) wyklucza taką normalną podgrupę; dla (n=2,3) grupa jest zbyt mała.

### Twierdzenie warunkowe

Jeżeli niezależnie od liczby węzłów pierwotna rodzina operacji ma pełną grupę symetrii (S_n), a dodatkowo jej symetria musi zawierać kanoniczną normalną podgrupę (C_2\times C_2), to:
[
\boxed{n=4.}
]

To jest rzeczywiste kryterium selekcji liczby cztery przez strukturę grupy automorfizmów. Jego koszt jest jednak jawny: postulat istnienia kanonicznego normalnego Klein four jest nowym warunkiem. Obecne korzenie P₀ nie wyprowadzają, dlaczego taka podgrupa ma być konieczna.

Dodatkowo rodzina (M_i) jest już indeksowana przez węzły i ma (n) elementów. Nawet jeśli jej grupa symetrii wybierze (n=4), nie rozwiąże to jeszcze wcześniejszego pytania Relacje: skąd wzięła się sama rodzina (M_i) bez nośnika (V)?

## 6. Werdykt

| Pytanie | Status | Uzasadnienie |
|---|---|---|
| Czy (M_i) są inwolucjami? | ❌ | Widmo ({1,1,1/4}) |
| Czy dodatnie słowa z (M_i) są inwolucjami? | ❌ | Wyznacznik (4^{-k}\ne\pm1) |
| Czy komutatory Liego (K_{ij}) są inwolucjami? | ❌ | Są antysamosprzężonymi generatorami infinitesymalnymi |
| Czy (S_4) rodziny generatorów ma kanoniczne (V_4)? | ✅ | Jedyna normalna podgrupa Klein four |
| Czy (V_4) jest obecne w Axis i Defect? | ✅ | Tak, ale po przyjęciu K₄ |
| Czy da się wybrać kanoniczną parę z trzech inwolucji (V_4\setminus\{e\})? | ❌ | (S_4) permutuje je przechodnio |
| Czy kryterium normalnego (V_4\triangleleft S_n) wybiera (n=4)? | ✅ warunkowo | Dokładnie dla (n=4) |
| Czy P₀ uzasadnia już takie kryterium przed K₄? | 💡/otwarte | Nie |

**Wniosek główny:** Centroid–Axis–Defect zawiera Klein four jako kanoniczną symetrię czterowęzłowej struktury. Nie zawiera jeszcze jej niezależnego źródła. Nie znalazłem więc podstaw, by odwrócić strzałkę i ogłosić, że (V_4) wyłania K₄.

## 7. Następny test

Nie będę szukał arbitralnych macierzy (T) spełniających (T^2=I) — pełna algebra afiniczna zawiera ich wiele, a ich istnienie niczego nie selekcjonuje.

Następny test powinien dotyczyć wcześniejszego poziomu niż Centroid: czy placeholdery (\mathcal R_t,F) z P₀-Relacje oraz (\mathcal R_k,\mathcal A_k) z P₀-Samoodniesienia mogą być zastąpione strukturą, której *własna* grupa automorfizmów ma charakterystyczny normalny (V_4), zanim pojawią się węzły. Dopóki nie ma typu danych i operacji na tym poziomie, nie wolno przypisać im takiej grupy.

Na dziś N‑R2 pozostaje otwarte. Wynik jest jednak ostrzejszy: znamy już dokładnie strukturę, która daje cztery, i wiemy, że w obecnych korzeniach występuje ona jako symetria K₄, a nie jako jej generator.
