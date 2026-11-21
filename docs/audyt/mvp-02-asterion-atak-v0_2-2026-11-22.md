# Atak Asteriona — MVP-02 v0.2: protokół τ, geometria, kanały i bramki sanity

Data: 2026-11-22  
Status: atak na v0.2; bez rachunków transportowych.  
Baza audytu: `a6d021f0001b0f9e591abb09a91a8d58a5a0387d`  
Źródło: `docs/mvp-02-spec-v0_2.md`, blob `af7c09c807b7341b7677ef082bbc15fb49c919a0`.

## Werdykt

v0.2 zamyka zasadnicze niejednoznaczności operatorowe wskazane w ataku v0.1. Chronologia aktualizacji, kolejność czynników, osadzenie M_local i skompresowany sweep bramki są teraz opisane w sposób zasadniczo deterministyczny. Wycofanie operatora trasy 13D z głównego testu usuwa poprzedni bloker 19D↔13D.

**Nie rekomenduję jednak zamrożenia v1.0 na podstawie obecnego v0.2.** Wykryłem co najmniej trzy problemy wpływające bezpośrednio na definicję miary: brak wspólnego okresu dla pięciu częstości, błędny wymiar powierzchniowego celu (w obecnym zapisie), oraz sprzeczność między liczbą 160 transferów a warunkiem f ∉ G'. Dodatkowo wiązanie kanałów przez differential_2 wymaga ujednolicenia typów macierzy.

Nie wykonano żadnych rachunków transportowych, obliczeń τ, symulacji, ani testu modelu zerowego.

## 1. Chronologia i operatory — PASS

### 1.1 §0.1: kolejność — PASS

Dla f=[a,b,c] konwencje są teraz rozdzielone:
- lista punktów: {a,b,c,P0};
- chronologia: a → b → c → P0;
- dla wektorów kolumnowych: R_tetr = M_P0 · M_c · M_b · M_a.

To jest spójne: prawostronny czynnik działa pierwszy, więc chronologia aktualizacji odpowiada M_a, M_b, M_c, M_P0. Określenie „apex-first” słusznie usunięto.

### 1.2 M_local i osadzenie 13D — PASS WARUNKOWY

Jawny opis całego aktywowanego wiersza jako (1/4,1/4,1/4,1/4), przy pozostałych wierszach identycznościowych, usuwa wcześniejszą niejednoznaczność. Osadzenie bloku na pozycjach a,b,c,P0, z P0 o indeksie globalnym 12, jest wystarczające.

Drobne doprecyzowanie: w implementacji należy podać, że lokalny indeks i oznacza wiersz aktualizowany, a kolejność mnożenia operatorów lokalnych jest zgodna z chronologią wyżej. Tekst zasadniczo już to implikuje.

### 1.3 Sweep bramki — PASS

R_gate jest teraz jednoznacznie zdefiniowany jako iloczyn 32 aktywacji na ośmiu ścianach bramki, w porządku rosnących indeksów, bez pozostałych dwunastu ścian. To jest dokładnie wariant skompresowany zaproponowany w ataku v0.1.

det R_gate = 4^-32 = 256^-8 jest poprawne strukturalnie.

### 1.4 A-05 / przestrzeń 13D — ROZWIĄZANE

Przyjęcie odrębnych przestrzeni reprezentacji dla kanału powierzchniowego i wnętrza usuwa potrzebę mapowania V_cyc do R^13 w teście głównym. To jest poprawna odpowiedź konstrukcyjna na wcześniejszy bloker. Operator 13D pozostaje fingerprintem i obiektem sanity/T2, a nie ukrytym mostem transportowym.

## 2. Krytyczny błąd kombinatoryczny: 160 transferów kontra f ∉ G'

§2.2 stwierdza, że każda para bramek współdzieli dokładnie dwie ściany. §2.3 definiuje transfer f → G' tylko wtedy, gdy f ∉ G'. Jednocześnie komplet określono jako 20 uporządkowanych par bramek × 8 ścian źródłowych = 160 transferów.

Te trzy stwierdzenia są sprzeczne.

Dla każdej uporządkowanej pary różnych bramek (G,G'):
- G ma 8 ścian;
- dokładnie 2 z nich należą również do G';
- warunek f ∉ G' pozostawia więc tylko 6 ścian źródłowych.

Zatem przy obecnym warunku transferu komplet wynosi:
- 20 uporządkowanych par × 6 = **120 transferów łącznie**;
- 8 uporządkowanych par przeciwległych × 6 = **48 testów**;
- 12 uporządkowanych par nieprzeciwległych × 6 = **72 przypadki null**.

Liczby 160/64/96 obejmują także 40 przypadków, w których źródłowa ściana należy już do bramki docelowej. Dla takich przypadków wejście leży w docelowej podprzestrzeni: udział(0)=1 i procedura zwróciłaby przeciek początkowy. To mogą być użyteczne kontrole przecieku, ale nie są transferami i nie spełniają warunku f ∉ G'.

**Wymagana decyzja przed v1.0:**
- albo poprawić komplet na 120 = 48 test + 72 null, a 40 przypadków wspólnych raportować osobno jako kontrole przecieku;
- albo jawnie włączyć 40 przypadków wspólnych jako osobną klasę kontroli i przestać nazywać je transferami. Nie mogą po cichu pozostać częścią rozkładu null.

To jest błąd arytmetyki zbiorów, nie kwestia konwencji numerycznej.

## 3. Wymiar celu powierzchniowego: 8, nie 7

§2.3 definiuje powierzchniowy cel jako span znaczników bramki G' w soma-zero, po czym przypisuje mu wymiar 8−1=7.

Przy literalnej definicji „znacznik e_f minus stała cechowania 1/20” wymiar wynosi **8**, nie 7.

Niech q_f = e_f − (1/20)·1 dla ośmiu różnych ścian f z G'. Załóżmy, że suma c_f q_f = 0. Na każdej z dwunastu współrzędnych spoza G' otrzymujemy −(1/20)·Σc_f = 0, zatem Σc_f=0. Na współrzędnej f∈G' pozostaje c_f=0. Wszystkie współczynniki są więc zerowe: osiem wektorów jest liniowo niezależnych.

Równoważnie, macierz Grama tych ośmiu wektorów ma postać I₈ − (1/20)J₈. Jej wartości własne to 1 (krotność 7) oraz 1−8/20=3/5 (krotność 1), więc ranga wynosi 8.

Wymiar 7 otrzymuje się dopiero dla przestrzeni różnic, np. span{q_f−q_g : f,g∈G'}, czyli po usunięciu wspólnego modu bramki. To nie jest jednak przestrzeń zdefiniowana obecnie jako span samych znaczników q_f.

**Wymagana errata:** zdecydować, czy celem jest pełna 8-wymiarowa podprzestrzeń znaczników, czy 7-wymiarowa podprzestrzeń różnic o sumie współczynników zero. Następnie odpowiednio zmienić projektor celu i uzasadnienie asymetrii 8 vs 7. Obecna asymetria nie wynika automatycznie z samego cechowania soma-zero.

## 4. differential_2: niezgodność konwencji transpozycji i typów

W §0.4 zapisano tożsamość differential_2 · differential_2^T = L_dod na 20-wymiarowej przestrzeni ścian, a równocześnie operator kanału wnętrza jako differential_2 · differential_2^T ograniczony do V_cyc (przestrzeń krawędziowa 30D, jej podprzestrzeń cykli 19D). §2.2 mówi, że obraz znacznika ściany przez differential_2 jest cyrkulacją krawędziową.

Nie da się spełnić wszystkich tych zdań jedną konwencją kształtu macierzy bez zmiany transpozycji.

Spójny zapis łańcuchowy jest następujący:
- B = ∂₂: C₂(ściany, 20D) → C₁(krawędzie, 30D), zatem B ma kształt 30×20;
- V_cyc = ker ∂₁ ⊂ C₁, wymiar 19;
- B e_f = omega_f, czyli brzeg ściany jest jej cyrkulacją;
- L_dod = B^T B, operator 20×20 na ścianach;
- L_eq = B B^T ograniczony do V_cyc, operator 30×30 na cyklach.

Wtedy zachodzi tożsamość wiążąca kanały:
`B L_dod = L_eq B`.

Jeśli autor używa differential_2 jako operatora transponowanego (kocobrzegu C₁→C₂), należy nazwać tę macierz osobno i zapisać odpowiednie transpozycje. Obecny tekst miesza kierunek mapowania z konwencją operatora Laplace'a.

**Wymagana errata:** podać jawne typy (dziedzina, przeciwdziedzina, rozmiar) differential_1 i differential_2 oraz konsekwentnie zapisać B^T B i B B^T. Bez tego nie da się niezależnie odtworzyć operatorów kanałów.

## 5. Skutek konstrukcji: kanały są sprzężone, różni je metryka

Po przyjęciu spójnego B z poprzedniego punktu:
- powierzchnia: L_surf = B^T B na soma-zero;
- wnętrze: L_int = B B^T na V_cyc;
- B jest izomorfizmem między 19-wymiarową przestrzenią soma-zero a V_cyc (jądro B na C₂ to stała, usunięta przez cechowanie);
- zachodzi B L_surf = L_int B.

Wobec tego dynamiki falowe są dokładnie sprzężone przez B:
`B cos(t·sqrt(L_surf)) y = cos(t·sqrt(L_int)) B y`.

Dla wejścia ścianowego q_f = e_f−(1/20)1 mamy B q_f = omega_f. Po normalizacji oba wejścia są proporcjonalne, a ich trajektorie pozostają proporcjonalne pod mapą B.

To znaczy, że kanały nie są dwoma niezależnymi prawami propagacji. Są dwiema realizacjami tej samej dynamiki liniowej, powiązanymi nieizometrycznym odwzorowaniem B. Różnice w udziale na celu mogą powstać przez:
- metrykę L2 na krawędziach kontra metrykę współrzędnych ścian;
- ortogonalne projektory celów w tych dwóch metrykach;
- wybór celu 8D lub 7D.

To może być sensowny test geometryczny, ale wynik U_b rozróżnia w pierwszej kolejności **metrykę i obserwabl**, nie samodzielnie „nośnik fizyczny”. Wniosek fizyczny musi być ograniczony do tego, co rzeczywiście mierzy konstrukcja.

## 6. Protokół τ: brak wspólnego okresu

Aneks A proponuje wyznaczanie sup_t udział(t) przez siatkę co 1/1000 „minimalnego okresu”, a następnie bisekcję.

W zestawie częstości są m.in. sqrt(2) i sqrt(3). Ich stosunek sqrt(2/3) jest niewymierny. Nie istnieje więc wspólny okres dla całej dynamiki zawierającej obie składowe.

W konsekwencji:
- nie ma jednego „minimalnego okresu” całego udział(t);
- siatka na jednym okresie pojedynczej składowej nie pokrywa globalnego zachowania funkcji;
- maksimum na skończonym przedziale nie jest automatycznie supremum po t≥0;
- bisekcja pierwszego przekroczenia jest poprawna dopiero po ustaleniu poprawnego progu i znalezieniu gwarantowanego przedziału bracketingowego.

Dla nieokresowej sumy skończonej liczby cosinusów właściwym obiektem jest domknięcie orbity fazowej na torusie (lub odpowiedni podtorus, jeśli istnieją relacje całkowite między częstościami). Supremum należy wyznaczać na tym zwartym zbiorze, a nie przez arbitralne obcięcie czasu do jednego okresu. Możliwa jest metoda certyfikowana: rozkład relacji częstotliwości, a następnie optymalizacja z ograniczeniami i przedziałowymi oszacowaniami błędu.

**Wymagana errata:** zastąpić „minimalny okres” formalną procedurą wyznaczania globalnego supremum. Jeżeli autor chce zamiast tego używać skończonego okna czasowego, musi jawnie zmienić definicję θ i uzasadnić horyzont.

Dodatkowo: stwierdzenie „brak rezonansów, bo pięć częstości jest parami różnych” jest za słabe, jeśli „rezonans” ma oznaczać brak całkowitych relacji między częstościami. Różność parami nie implikuje niezależności wymiernej.

## 7. Aneks A i dokładność numeryczna — niekompletne wejście

W pobranym commicie v0.2 Aneks A zawiera opis ogólny, ale nie zawiera obiecanych tabel wag projekcji celu ani pełnych współczynników jawnych sum udział(t). Sam dokument zapowiada ich dostarczenie jako uzupełnienia przed atakiem.

Bez tych danych nie da się niezależnie sprawdzić:
- czy wszystkie pięć składowych ma niezerowe wagi dla każdego wejścia/wyjścia;
- czy istnieją szczególne wejścia z redukcją liczby aktywnych częstości;
- jak szerokie są pierwsze przekroczenia progu;
- czy siatka nie pomija wcześniejszego przekroczenia.

Dodatkowo „bisekcja do 3 miejsc” i „raport 2 cyfry znaczące” powinny dostać jednoznaczne kryterium stopu (bezwzględne/względne), regułę zaokrąglania oraz zachowanie dla τ bardzo małego. To szczególnie istotne w pobliżu flagi PRZECIEK.

## 8. BFS i wykaz czterech par przeciwległych — brak danych do niezależnej reprodukcji

Zbiory G0–G4 są jawne, ale w samym wskazanym pakiecie v0.2 nie ma kompletnej tabeli 20 ścian jako trójek globalnych wierzchołków ani jawnej listy sąsiedztwa grafu dwunastościanu. Nie ma też ścisłej definicji, jak z dwóch ośmioelementowych zbiorów bramkowych wyznacza się ich wzajemny dystans na grafie (np. dystans między jakimi obiektami/zbiorami).

Samo „dystans na grafie dwunastościanu” nie wystarcza do odtworzenia BFS przez niezależnego wykonawcę, zwłaszcza gdy numeracja ścian jest leksykograficzna, ale nie podano tabeli indeks→trójka.

Wynik 4 par przeciwległych i 6 par nieprzeciwległych przyjmuję jako deklarację specyfikacji, nie jako niezależnie odtworzony wynik BFS. Do zamknięcia tego punktu potrzebne są:
1. tabela indeksu każdej ściany → trzy globalne wierzchołki;
2. jawna lista krawędzi grafu dwunastościanu (lub reguła jej jednoznacznego wyprowadzenia);
3. definicja dystansu między bramkami;
4. dopiero potem wykaz czterech par i rozkład odległości pozostałych sześciu.

Nie będę zgadywał etykiet par.

## 9. Artefakty D3 — nowa konstrukcja

### 9.1 Cechowanie soma-zero

Cechowanie przez q_f=e_f−(1/20)1 jest poprawne jako projekcja znacznika na podprzestrzeń sumy zero. Ponieważ B1=0 (suma zorientowanych ścian zamkniętej sfery ma zerowy brzeg), zachodzi B q_f=B e_f=omega_f. To jest dobre i usuwa arbitralność dodawania stałej.

Jednak cechowanie nie zmniejsza wymiaru span ośmiu znaczników do siedmiu — patrz §3.

### 9.2 differential_2 jako wiązanie kanałów

Właściwe wiązanie jest mocne: B q_f=omega_f. Ale jest to jednocześnie dowód sprzężenia dynamik, a nie tylko luźna korespondencja wejść. Trzeba więc opisać wynik jako porównanie metryk/projektorów, a nie dwóch niezależnych operatorów propagacji.

### 9.3 Asymetria 8 vs 7

Nie jest konsekwencją samego soma-zero. Jest dodatkowym wyborem celu, jeśli autor zamierza odjąć wspólny mod bramki. Wymaga jawnej definicji i uzasadnienia.

## 10. Bramki sanity dozwolone przed bindem

Bez rachunków transportowych można i należy sprawdzić następujące obiekty:
1. M_local: wiersz aktywowany równy (1/4,1/4,1/4,1/4), pozostałe wiersze identycznościowe, det=1/4.
2. R4: widmo i lewy wektor S10=(1,2,3,4)/10 zgodnie z kolejnością §0.1.
3. R_gate: liczba aktywacji 32, det=256^-8 oraz odtworzenie pięciu zamrożonych rho_gate.
4. L_cyc: tylko dla ORIENT-02-A; widmo checkpoint 494/3 i ranga projektora 19.
5. L_dod: grafowy laplasjan dwunastościanu; ślad 60, jądro stałe, PSD.
6. L_eq: zgodność widma z L_dod po usunięciu stałego modu, ranga 19 i równowariantność.
7. Wektory s_G/a_G: czystość sektorów, suma s_G=0, rząd rodziny 4 i Gram. Wzór ⟨s_G,s_G'⟩=6−N_sąs jest logicznie spójny, ale wymaga jawnego grafu ścian do niezależnego sprawdzenia N_sąs=12.
8. Dla czystych wektorów modalnych: przewidywanie udział(t)=C cos²(omega t) jest poprawną kontrolą degeneracji, pod warunkiem poprawnego projektora celu i jawnej normy.

Nie wykonałem tych rachunków; wskazuję je jako dopuszczalną kolejkę replikacji algebraicznej przed bindem.

## 11. Erraty wymagane przed v1.0

| ID | Priorytet | Problem |
|---|---|---|
| B-01 | BLOKER | 160/64/96 sprzeczne z f∉G'; poprawić na 120/48/72 albo wydzielić 40 przecieków |
| B-02 | BLOKER | powierzchniowy cel span{q_f} ma wymiar 8, nie 7 |
| B-03 | BLOKER | ujednolicić typy differential_2 i transpozycje w L_dod/L_eq |
| B-04 | BLOKER | brak wspólnego okresu; protokół globalnego sup i θ nie jest poprawnie zdefiniowany |
| B-05 | WYSOKI | dostarczyć tabele wag i pełne współczynniki Aneksu A |
| B-06 | WYSOKI | dostarczyć face table, graf i definicję dystansu bramek dla niezależnego BFS |
| B-07 | WYSOKI | ograniczyć interpretację: kanały są sprzężone, różnice τ mogą wynikać z metryki/projektora |
| B-08 | ŚREDNI | jawne kryterium stopu bisekcji, zaokrąglenia i obsługa τ≈0 |

## Konkluzja

v0.2 jest dużym postępem i zamyka poprzedni atak Asteriona na kolejność, osadzenie, sweep i niepotrzebny most 19D↔13D.

Jednak w obecnym brzmieniu miara U_b nie jest jeszcze jednoznacznie gotowa do bindu:
- liczba przypadków nie zgadza się z warunkiem transferu;
- wymiar celu powierzchniowego jest błędny;
- zapis differential_2 wymaga poprawienia typów;
- globalny próg θ nie może być uzasadniony siatką jednego okresu, bo wspólny okres nie istnieje;
- dwa kanały są sprzężone i test mierzy przede wszystkim różnicę metryk/projektorów.

**Rekomendacja Asteriona:** v0.2 pozostawić jako „do ataku”. Najpierw rozstrzygnąć B-01 do B-04. Nie uruchamiać transportu ani modelu zerowego przed poprawioną specyfikacją i hashem całego dokumentu.
