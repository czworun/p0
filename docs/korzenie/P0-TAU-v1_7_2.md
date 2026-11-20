# Korzeń: P₀-TAU — adnotacja szefa lab. (v1.7.2, program 2026-09-22..27, korekta recenzyjna v1.7.2)

**Dokument:** „P₀-TAU — czas relacyjny" v1.7.2 (status nagłówka: korekta §7.8 — konwencja, cytat, P27 zamknięte). Data: 2026-09-27; historia §12: v0.1–v0.2 (09-22), v1.0–v1.5 (09-25), v1.6–v1.6.5 (09-26), v1.6.6/v1.7/v1.7.1/v1.7.2 (09-27, cztery wersje jednego dnia). Nowszy chronologicznie niż wszystkie dotąd wpięte korzenie (Memory 09-07/08, Net i SERC 09-13) i pierwszy dokument serii, który czyta wpięty wczoraj korpus jako zależność (pośrednio: M16a §8bis.4 z Memory, §7.5 most TAU↔Memory jawny). Recenzje wielomodelowe W TREŚCI, datowane 2026-09-27: Claude (wykrył błąd α_crit = 4/3 → 3/2; doprowadził do usunięcia fałszywego cytatu Dehn/Radin), GPT (adnotacje zakresu Tw. 7.8.7.1 i 7.8.7.2; zastrzeżenie do P10-alt). Zależności: P₀-TETRA-20 v0.2.4 (poza repo), P₀-Centroid v5.1 (w repo v5.2-audit), P₀-Scalar v0.3.5 §2.4 (poza repo; w kolejce wpięć), P₀-Memory v0.3.7 §8bis.4 (w repo), SERC⁺⁻ Tom 0, p0-memory, s4-rep, p0-axis, p0-net, p0-wave (warstwa notatników roboczych p0-*, poza repo; p0-axis w kolejce zależności jako Axis). Poza kolejką główną (kolejka przewidywała Scalar) — dostawa wg decyzji Leszka; przy wpięciu Scalar i Axis rozliczyć odsyłacze TAU (vide Mosty). Deklarowana pozycja: program badawczy czasu relacyjnego τ — wspólny czas relacji jako własność PARY, nie obiektu; formalna pozycja (kandydatura filarna, relacja do sesji warsztatowych pnia noszących tę samą nazwę TAU) — uregulowanie przy PILLARS-TABLE i scaleniu pnia.

**Co bada:** czy relacja ma wspólny czas τ i czy da się go zmierzyć. Cztery miary τ rozdzielone (§2): τ_period ✅ (K₄ 0,500; ikosaedr 0,448; skala 1/√λ_min), τ_relax 🔍 (podejście nieudane), τ_mix ❌ (P6), τ_relation ❌ — niezdefiniowane operacyjnie, NIE zmierzone (§4A jawnie); zasada: stwierdzenia o τ zawężać do miary, którą zmierzono. Aksjomat sekwencyjności §1.1 (fenomenologiczny, niefalsyfikowalny, motywacyjny): relacja jest sekwencyjna — kto mówi, kto słucha, kiedy; formalizacje symetryczne (ODE ciągłe, Verlet) to niewłaściwa klasa obiektu; M_m (z P₀-Centroid §1; Gauss-Seidel, kolejność jako część definicji) właściwa. Warstwy sekwencji i liczby pierwsze (§1.2, rozszczepienie v1.6.6): warstwa aktualizacji (harmonogram → P22) vs warstwa czasowa (hierarchia okresów → P10 ❌, P10-alt 💡: w 5K₄ warstwy k ∈ {2,3,5} pierwsze miałyby przetrwać uśrednienie dłużej niż k ∈ {1,4}; zastrzeżenie GPT: 1 struktura z 5 warstwami to za mało, by oddzielić pierwszość od liczby warstw). Hierarchia fraktalna poziomów (§3): K₄ → ikosaedr → K₄ wyższego rzędu, ta sama struktura, skala rośnie, τ się zmienia, fraktal (verbatim); analogia poziomów: galaktyka → układ → planeta → księżyc, od najwolniejszych do najszybszych τ, im wyższy poziom, tym więcej relacji do uzgodnienia. Obiekt nowy v1.7: 5K₄ (pięciokątna bipiramida; 5 foremnych czworościanów wokół wspólnej osi). Zmierzono (§4): widma L_cyc (K₄ λ={4,4,6}, dim V_cyc=3, z etykietą 3p = T₂g; ikosaedr λ = {4.9784, 6^×2, 7.3333^×3, 7.6, 8.0883, 10^×11}, dim 19); INC-08: 22 atraktory, korelacje średnia −0.0007, brak synchronizacji bez sprzężenia; INC-10c: selekcja modów (ikosaedr: ω = 2.765, 3.157 dominujące).

**Najmocniejsze (siedem twierdzeń ✅ z dowodami w treści; rachunek, nie eksperyment):**
1. **Tw. 7.3.1 (konsensus końcowy):** dla n ≥ 2, dowolnej kolejności σ, α ∈ (0, α*), granica R_σ^k x₀ = c_σ(x₀)·1 z wagami liniowymi w pozycji k (wcześniejszy mówca ma większą wagę); w_k^{(α,n)} jawne, liniowe w k dla każdego α.
2. **Tw. 7.3.2 (rozrzut po kolejnościach):** Δ_σ c = (α/nW)·Σ(2k−n−1)x_(k), W = n − α(n−1)/2; maksymalizacja po σ, nie po x₀; redukcja do α=1: b/W = 2/(n(n+1)); trzy miary rozdzielone czysto: konsensus zależy od σ TAK, tempo zbieżności i rate NIE (Fakt 7.3.0: R_σ = P_σ R_id P_σ⁻¹, sprzężenie permutacyjne z sanity checkem n=3).
3. **Tw. 7.3.6 (rodzina parametryczna):** punkty wyróżnione 0⁺ (identyczność), 1 (= wersja Centroid v5.1), n/(n−1) (= notatnik), 2n/(n−1) (granica stabilności z blokiem Jordana: dim ker(R−I)=1, dim ker((R−I)²)=2, iteracja rośnie liniowo) — geometria rodziny M_m(α) domknięta.
4. **Tw. 7.4.6 (Jacobi = symetryzacja GS):** średnia konsensusu po wszystkich kolejnościach = średnia(x₀) dla każdego α ∈ (0,α*) — UGRUNTOWANIE osi sekwencyjny/symultaniczny korpusu: tryb aktualizacji (czwarty parametr K₂ z Memory M16a: batch 0,71% vs sekwencyjny 67,76%) dostaje twierdzenie, nie tylko empirię; §7.5 most TAU↔Memory jawny (most ilościowy = P14 otwarty).
5. **Tw. 7.8.7.1 + Tw. 7.8.7.2 (5K₄, p₀ styku):** pełny konsensus jedynym punktem stałym modelu B dla α ∈ (0, 3/2), α > 0, krotność λ=1 równa dokładnie 1 (zakres doprecyzowany przez GPT); oraz c_m = 4/3 UNIWERSALNE dla mK₄, wszystkie m ≥ 3 (dowód: każdy czworościan ma dokładnie 3 sąsiadów dla apexu niezależnie od m; P27 zamknięte ✅). Adnotacja GPT: twierdzenie dotyczy wyłącznie mnożnika zaniku różnicy na wspólnej osi, nie pełnego widma.
6. **5K₄ jako pierwszy konkretny przedmiot τ:** deficyt δ = 2π − 5θ_d ≈ 7.356° (θ_d = arccos(1/3) nie dzieli 2π — elementarny rachunek kątowy, znany od błędu Arystotelesa z De Caelo); potwierdzony niezależnie w p0-axis §8.5.9 dwoma metodami (BFGS/SLSQP i wzór analityczny 1/(tan(π/5)√2), zgodność 5–6 cyfr) plus fizyczny model autora z 2026-09-27 (jawnie: sprawdzian realizowalności, nie pomiar; model się nie domyka, deficyt widoczny); struktura: 7 wierzchołków (2 apexy + 5 równikowych), 15 krawędzi zewnętrznych + oś wewnętrzna, 10 ścian zewnętrznych + 5 wewnętrznych, symetria D₅, Eulera 7−15+10=2 ✓; skurcz krawędzi przy kontakcie symetrycznym: 2,675% (r_scale = 0.973254); p₀^styk = podprzestrzeń A_top=A_bot, wymiar 6 w R⁷, niezmiennicza — droga do konsensusu, nie osobny cel.
7. **Higiena epistemiczna wzorcowa (Z0/Z2):** fałszywy cytat Dehn/Radin USUNIĘTY z pełną dyskusją (Dehn 1900 dotyczy scissors-congruence — trzeci problem Hilberta, własność niezależna; nie implikuje niemożności trybułacji; prawdziwe uzasadnienie i tak było elementarne); katalog 13 błędów metodologicznych WŁASNYCH (§6), w tym #12 artefakt α=0.5 (w punkcie testowym α = 1−α, hipoteza (1,α^k) wyglądała pozornie poprawnie (α=1−α w punkcie testowym) — artefakt P23 wyjaśniony) i #13 ciche przeniesienie liczby między rodzinami operatorów (α_crit = 4/3 z notatnika, include-self, n=4, izolowany K₄, przeniesione do 5K₄ exclude-self; poprawnie 3/2 — wykrył Claude); zasada sformułowana: ŻADNA liczba nie przenosi się między rodzinami operatorów bez jawnego przeliczenia konwencji; Tw. 7.8.3: wartości 3/2 i 2 nieporównywalne między konwencjami — twierdzenie „styk jest szybszym kanałem" USUNIĘTE jako artefakt porównania konwencji (include-self: styk i wnętrze identycznie λ = 1−α).

**Koncesje i sęki (jawnie):** τ_relation NIEZMIERZONE (§4A: w całej sesji nie wykonano eksperymentu mierzącego wspólny czas relacji; niezdefiniowane operacyjnie) — dokument uczciwie nie domyka tematu wiodącego; aksjomat §1.1 fenomenologiczny, niefalsyfikowalny, pełni funkcję motywacyjną nie dowodową (jawne); P10 ❌ (realizacja z v1.3 sfalsyfikowana) i P10-alt 💡 z zastrzeżeniem GPT (za mało struktur); P17 ❌ zamknięte (zasada: program po trzech rundach kandydatek bez pozytywnego wyniku zostaje zamknięty); P21 ❌ (kolorowanie krawędziowe odrzucone; χ'(iko)=5 zachowane tylko jako fakt); P23 🔍 (wynik Claude był artefaktem α=0.5); region stabilności 7.4.7 🔍 tylko numerycznie (n do 10000); asymptotyka 7.4.9 🔍 (układ transcendentny cosθ = r(1−ln r), θ − sinθ/r = −2π; r_∞ ≈ 0.12383, θ_∞ ≈ 67.40°); model C (P24) NIEZBUDOWANY — wymaga decyzji autora C1/C2/C3 (foremność, pokrywanie wierzchołków, kontrolowane odkształcenie) plus pytanie sekwencyjne vs symetryczne więzów; trzy programy zamknięte negatywnie w jednej sesji (P17, P21, Dehn/Radin) — dokument wie, że zamyka, i deklaruje to wprost; niezgodność liczebnika §11 („Sześć twierdzeń", wymienionych nazw siedem — vide uwagi redakcyjne); zależności poza repo niemożliwe do rozliczenia z korpusu (TETRA-20 v0.2.4, Scalar v0.3.5, notatniki p0-axis/s4-rep/p0-memory).

**Struktury 💡:** cztery miary τ jako rozdzielenie pojęcia od pomiaru; geometria rodziny M_m(α) z punktami wyróżnionymi (0⁺ / 1 / n/(n−1) / 2n/(n−1)) — drabina parametryczna z blokiem Jordana na końcu; trzy modele JEDNEJ struktury 5K₄ (§7.8.7): A geometryczny (pozycje w R³, sztywność), B skalarny (wartości na etykietach, uśrednianie Jacobi/GS — jawnie nie zna długości krawędzi, nie może odtworzyć nierówności promienisty/obwodowej modelu A), C mieszany (pozycje + więzy, do zbudowania) — model B bez metryki to strukturalnie ten sam problem co brak kanonicznego mostu w rodzinie Defect (realizacja nie przenosi własności źródła); p₀^styk jako droga, nie cel (podprzestrzeń niezmiennicza wymiaru 6, droga do konsensusu); hierarchia fraktalna poziomów (skala rośnie, τ się zmienia); etykieta reprezentacyjna V_cyc(K₄) = 3p = T₂g.

**Mosty 💡:**
1. **Most TAU↔Memory jawny (§7.5):** Tw. 7.4.6 przewiduje zgodność jakościową z danymi M16a (batch 0,71% vs sekwencyjny 67,76%); most ilościowy = P14; oś sekwencyjny/symultaniczny korpusu (K₂ w Memory/Net, 720 kolejności Gaussa-Seidela w ORB-05-R, P1/R_sym w Lattice, konwencja notatnika Stalka) dostaje twierdzenie spajające — przy scaleniu pnia pozycja: tryb aktualizacji jako parametr PODSTAWIOWY z teorią.
2. **n/(n−1) po raz drugi jako punkt wyróżniony:** §7.3.6 (notatnik) i Lattice tura 13 (c(n) = n/(n−1) jako tożsamość zaszywająca/spoiwo przy domknięciach tury 13) — dwie niezależne linie, jedna liczba; przy scaleniu pnia jedna pozycja atlasu.
3. **Deficyt 2,675% zbieg trzech kontekstów:** TAU (skurcz krawędzi 5K₄ przy kontakcie symetrycznym, z rachunku kątowego), SERC/Axis §16ter (deficyt dysklinacyjny jako model niezamkniętej pętli nawrotów klinicznych), p0-axis §8.5.9 (potwierdzenie niezależne dwiema metodami numerycznymi) — jedna geometria mK₄, trzy odczyty; przy wpięciu Axis rozliczyć wszystkie odsyłacze naraz (§8.5.9, §16ter, §16bis).
4. **Korekta między filarami w obie strony:** TAU §7.4.9 koryguje S11-A w P₀-Scalar (|λ|_∞ = 1/8, poprawnie ≈ 0.12383; jawnie: „korekta dotyczy Scalar, nie TAU") — przy wpięciu Scalar rozliczyć S11-A razem ze §11.6 (SERC: faza 25,77° rośnie z n) i §2.4 (zależność TAU); trzeci przypadek w korpusie korekty międzypilarowej jawnie z adresatem (vide Centroid errata, SERC odsyłacze).
5. **5K₄ jako sąsiad geometrii warsztatowej:** deficyt kątowy czworościanu (θ_d nie dzieli 2π) to ta sama klasa faktów co bramki 8 z 20 ścian i kanały 0→5→11→24 z rund warsztatowych oraz stella octangula (osmiościan jako wnętrze pary K₄); hierarchia K₄ → ikosaedr pojawia się tu (widmo L_cyc dim 19), w SERC (χ'(iko)=5) i w Lattice (drabina S₄→D₃h→C₃v→I_h) — kolejny głos rodziny „jeden obiekt, podgrupy" (Lattice tura 8); klasa mK₄ (bipiramidy m czworościanów, m ≥ 3) to nowy obiekt badawczy sąsiedni do pary K₄ i TETRA-20.
6. **Aksjomat sekwencyjności jako fundament filozoficzny osi asymetrii:** SERC tabela mechanizmów zaczyna od sekwencyjności R₄; TAU dowodzi, że formalizacje symetryczne to NIEWŁAŚCIWA KLASA OBIEKTU (nie tylko gorsze narzędzie) — wspiera transfer P₀-AI (target symetryczny wymaga absolutu) z drugiej strony; kategoria błędów §6 (Euler zamiast GS, myślenie spektralne zamiast relacyjnego, pomiar nie tej wielkości) to lista antywzorców dla wszystkich filarów.
7. **Relacja nazewnicza do sesji warsztatowych pnia:** wklejki pnia (TAU-10…TAU-15-Z1 w repo docs/) przywołują definicje „§18" i „§21" nieobecne w v1.7.2 (dokument kończy się na §12) — geneza wspólnej nazwy TAU i związek wersji do rozliczenia przy scaleniu pnia (Przegląd_Całości); wpięcie traktuje dokument jako korzeń niezależny od pnia operacyjnego.

**Sęk-odnogi (§9, §10):** priorytet 0 — pytania do autora (definicja warstwy czasowej ❌, wybór α w rodzinie M_m(α) 🔍); 1. P26 (sekwencyjna dynamika modelu B na 5K₄ — gotowe do uruchomienia, pierwszy eksperyment celowany); 2. P24 (model C — decyzje C1/C2/C3); 3. P19 (asymptotyka analityczna r_∞); 4. P20 (współczynnik bloku Jordana (n−1)/(n+1)); 5. P22 (kolorowanie wierzchołkowe jako harmonogram blokowy; blok GS 4×3 dla ikosaedru); 6. P23 (naturalna orientacja DAG; kandydatury: indeks, znak D_e z M16, para przeciwległa); 7. P10-alt (test hierarchii warstw); 8. P15/P14 (grafy niepełne; most ilościowy TAU↔Memory); zamknięte: P17 ❌, P21 ❌, P27 ✅, P25 (→P27).

**Statusy (mapa na Z1):** siedem twierdzeń ✅ z dowodami algebraicznymi w treści — ale każde liczone jedną ręką (autor) z recenzjami Claude/GPT przy dwóch korektach (α_crit, cytat Dehn/Radin): wzorzec PRZED-warsztatowy z recenzyjną kontrolą, nie pełna replikacja Z1; kandydaci do replikacji warsztatowej od najtańszego: Tw. 7.8.7.2 (czysto algebraiczny, dowód krótki), fakt 7.3.0 (sprzężenie permutacyjne), Tw. 7.4.6 (średnia po permutacjach), asymptotyka 7.4.9 🔍 (transcendentalna — trudniejsza, dobre zadanie BLIND), P26 jako pierwszy eksperyment; ❌ jawne i liczone (P10, P17, P21, cytat, α_crit=4/3); 🔍 (region stabilności do n=10000, asymptotyka, P23, τ_relax); konwencja statusów zgodna z korpusową (✅🔍💡❌).

**Uwagi redakcyjne (verbatim):** oryginał kończy się bez końcowego EOL (ostatnie zdanie o P26 gotowe do uruchomienia); 21 510 B, 456 linii wg wc -l (odczyt narzędziowy 457 — ostatnia bez EOL), md5 47b4e14a6fa646574a2116cea6246c7c (kopia robocza); tytuł „P₀-TAU — czas relacyjny", wersja nagłówkowa „1.7.2 (korekta §7.8 — konwencja, cytat, P27 zamknięte)"; data 2026-09-27 wspólna czterem wersjom jednego dnia (§12); status nagłówka jako mapa problemów z jawnymi statusami (RZADKI format — dokument otwiera się od stanu problemów, potem treść) — zachowane verbatim; NIEZGODNOŚĆ LICZEBNIKA §11: „Sześć twierdzeń ✅" wobec siedmiu nazw w nawiasie (Tw. 0.2.1, 7.3.1, 7.3.2, 7.3.6, 7.4.6, 7.8.7.1, 7.8.7.2 — v1.7.2 dodało siódme nie aktualizując liczebnika) — verbatim, do noty erratowej u autora; notacja LaTeX w delimiterach dolarowych wzdłuż całego dokumentu (jak w Net v0.6.1, inaczej niż w SERC/Memory z notacją unikodową); dwie notacje deficytu w jednym dokumencie (7,36° w prozie, 7.356° w rachunku §7.8.1) — zachowane; sekcja 4A (numeracja z literą — jedyna taka w serii); polski przecinek dziesiętny (7,356; 0,12383) i kropki w tabelach numerycznych (4.9784) — obie konwencje obecne, zachowane verbatim; jedno \boxed (§7.8.2); słownictwo charakterystyczne: bipiramida, styk, apex, deficyt dysklinacyjny; UWAGA: w nagłówku §7.8 oryginału litera cyrylicka w słowie bipiramida (glitch autorski, zachowany verbatim).
P₀-TAU — czas relacyjny

Wersja: 1.7.2 (korekta §7.8 — konwencja, cytat, P27 zamknięte)
Status: 🔍 §1.1 aksjomat fenomenologiczny;
§1.2 hipoteza strukturalna (rozszczepiona P10/P10-alt);
§0.2 adnotacja zakresu (równowaga α);
§7.8 skorygowane — 5K₄ jako obiekt, p₀ styku, jawna konwencja, usunięty fałszywy cytat;
§7.3–7.4 kompletne z twierdzeniami;
§7.5 most TAU↔Memory (💡);
§7.6 P17 zamknięte (❌);
§7.7 P21 zamknięte, P22/P23 otwarte;
P10 ❌ vs P10-alt 💡;
P24 otwarte (wymaga decyzji autora);
P26 gotowe do uruchomienia;
P27 zamknięte ✅ (Tw. 7.8.7.2)

Data: 2026-09-27
Zależności: P₀-TETRA-20 v0.2.4, P₀-Centroid v5.1, P₀-Scalar v0.3.5 §2.4, P₀-Memory v0.3.7 §8bis.4, SERC+−, Tom 0, p0-memory, s4-rep, p0-axis, p0-net, p0-wave

Zmiana v1.7.1 → v1.7.2. Trzy korekty mechaniczne, wszystkie w §7.8:

1. Usunięcie fałszywego cytatu Dehn/Radin. Cytat Radin 1997 nie potwierdza się; Dehn 1900 nie implikuje niemożności trybułacji. Prawdziwe uzasadnienie: elementarny rachunek kątowy (znany od Arystotelesa).
2. Tw. 7.8.7.1 z jawnym zakresem α — $\alpha > 0$.
3. Tw. 7.8.7.2 NOWE — P27 zamknięte: $c_m = 4/3$ dla wszystkich $m \geq 3$; korekta $\alpha_{\rm crit} = 3/2$ (nie 4/3 — Claude wykrył błąd w v1.7.1).

Adnotacja do Tw. 7.8.7.2 (GPT). Twierdzenie dotyczy wyłącznie mnożnika zaniku różnicy na wspólnej osi, nie pełnego widma operatora ani stabilności całego układu.

---

0.0 Stan bieżący (v1.7.2)

· §1.1 (aksjomat sekwencyjności): bez zmian. Fenomenologiczny, motywacyjny, niefalsyfikowalny.
· §1.2 (warstwy, liczby pierwsze): rozszczepienie z v1.6.6 utrzymane — warstwa aktualizacji (P22) vs warstwa czasowa (P10 ❌, P10-alt 💡).
· §5 (P5): bez zmian. Baseline.
· §7.3–7.4 (twierdzenia o $M_m$ na $K_n$): kompletne.
· §7.5 (most TAU↔Memory): 💡.
· §7.6 (P17): zamknięte negatywnie.
· §7.7 (P21/P22/P23): P21 ❌, P22 💡, P23 🔍.
· §7.8 (5K₄): skorygowane — jawna konwencja, usunięty fałszywy cytat, dwa twierdzenia o $p_0^{\rm styk}$, P27 zamknięte.
· P10: rozszczepione.

0.1 Cel dokumentu

Bez zmian.

0.2 Zakres §7.3–7.4

Twierdzenia §7.3–7.4 dotyczą jednopoziomowego konsensusu sekwencyjnego na grafie pełnym $K_n$. Tw. 0.2.1 (równoważność globalny/lokalny dla $K_n$ po przeskalowaniu α) — aktualne. Dla grafów niepełnych równoważność znika.

Adnotacja v1.7. §7.8 dotyczy struktury niepełnej (5K₄). Wynik §7.8 jest nowym wynikiem, nie przeskalowaniem §7.3–7.4.

---

1. Definicja — intuicja autora

τ to wspólny czas relacji. Nie własność pojedynczego obiektu, lecz własność pary — czas, w którym dwa elementy pozostają w relacji.

Hierarchia poziomów: galaktyka → układ gwiezdny → planeta → księżyc, od najwolniejszych do najszybszych τ. Zasada: im wyższy poziom, tym więcej relacji do uzgodnienia, tym wolniejsze wspólne τ.

1.1 Aksjomat sekwencyjności — status: fenomenologiczny

Aksjomat przyjęty z bezpośredniego doświadczenia autora. Nie falsyfikowalny eksperymentem w tym dokumencie. Pełni funkcję motywacyjną, nie dowodową.

Relacja jest sekwencyjna — kto mówi, kto słucha, kiedy. Formalizacje symetryczne (ODE ciągłe, Verlet) są niewłaściwą klasą obiektu. $M_m$ z P₀-Centroid §1 (Gauss-Seidel, kolejność jako część definicji) jest właściwą formalizacją.

1.2 Warstwy sekwencji i liczby pierwsze — 💡 hipoteza strukturalna

Rozszczepienie (v1.6.6):

· warstwa aktualizacji (harmonogram) → P22
· warstwa czasowa (hierarchia okresów $\{k\tau_0\}$) → P10 (❌), P10-alt (💡)

P10-alt (💡, v1.7). W 5K₄ warstwy czasowe mają naturalną realizację geometryczną: 5 czworościanów wokół wspólnej osi, deficyt $7{,}36°$ jako jednostka. Warstwy pierwsze: $k \in \{2, 3, 5\}$. Hipoteza: opierają się uśrednieniu dłużej niż złożone ($k \in \{1, 4\}$).

Zastrzeżenie (GPT, v1.7.1). 1 struktura z 5 warstwami to za mało, żeby oddzielić pierwszość od liczby warstw. P10-alt zostaje hipotezą geometryczno-dynamiczną, nie testem.

---

2. Status pojęcia — cztery miary

Miara Definicja Zmierzone?
τ_period okres podstawowy ✅ §4.4
τ_relax czas relaksacji 🔍 nieudany
τ_mix mixing time ❌ P6
τ_relation wspólny czas relacji ❌ §5, §7.3

Zasada: stwierdzenia o τ trzeba zawężać do miary, którą zmierzono.

---

3. Hierarchia poziomów — formalizacja konstrukcyjna

K₄ → ikosaedr → K₄ wyższego rzędu. Każdy poziom = ta sama struktura, skala rośnie, τ się zmienia. Fraktal.

P4. Co to relacja — krawędź, kanał S₄, poziom, kolejność mówienia? Wybór projekcji $\Pi_A,\Pi_B$ dla P5 jest wyborem odpowiedzi na P4.

---

4. Co zostało zmierzone

4.1 Widma $L_{\rm cyc}$

K₄: $\lambda=\{4,4,6\}$, $\dim V_{\rm cyc}=3$, $V_{\rm cyc}(K_4)=3p=T_{2g}$.
Ikosaedr: $\lambda=\{4.9784,6^{\times2},7.3333^{\times3},7.6,8.0883,10^{\times11}\}$, $\dim V_{\rm cyc}=19$.

4.2 τ_period

Poziom $\lambda_{\min}$ $1/\sqrt{\lambda_{\min}}$
K₄ 4.000 0.500
ikosaedr 4.978 0.448

4.3 Korelacja atraktorów (INC-08)

22 atraktory, $r$(średnia)$=-0.0007$, $\|r\|>0.3$ w 0/231 par. Brak synchronizacji bez sprzężenia.

4.4 Selekcja modów (INC-10c)

K₄: oba mody aktywne. Ikosaedr: dwa mody dominujące ($\omega=2.765, 3.157$).

---

4A. Co NIE zostało zmierzone

W całej sesji nie wykonano eksperymentu mierzącego wspólny czas relacji. τ_relation niezdefiniowane operacyjnie.

---

5. P5 — specyfikacja prerejestrowana

Status: gotowe do kodu. Baseline/porównawcze, nie docelowy test τ_relation. Sprzężenie symetryczne — zgodne z §1.1 niezgodne. Granica α → 0 rodziny $M_m(\alpha)$.

Wszystkie podsekcje §5.A–§5.H aktualne wobec v1.6.5.

---

6. Katalog błędów metodologicznych

1. Mylenie operatora z nazwą.
2. Signed vs unsigned action.
3. Myślenie spektralne zamiast relacyjnego.
4. Autokorelacja w chaosie.
5. Kwantyzacja pomiaru.
6. Euler zamiast RK4/Verlet.
7. Hz vs rad/jednostkę.
8. Błędny argument grupowy.
9. Pomiar nie tej wielkości (INC-07).
10. Korzystanie z widma jako dowodu na dynamikę.
11. Nazywanie maksimum po jednej zmiennej bez kwalifikatora.
12. Artefakt α=0.5 (P23, v1.6.6) — hipoteza $(1,\alpha^k)$ wyglądała poprawnie tylko dlatego, że α=1−α w punkcie testowym.
13. Ciche przeniesienie liczby między rodzinami operatorów (v1.7.1 → v1.7.2) — $\alpha_{\rm crit} = 4/3$ z §7.3.6 (notatnik, $n=4$, include-self, izolowany $K_4$) przeniesione jako własność 5K₄ (exclude-self, struktura 7-wierzchołkowa). Ten sam wzorzec co T2/$R_4$ vs $M_m(\alpha)$ (§7.6.5) i §0.2 (global/local). Zasada: żadna liczba nie przenosi się między rodzinami operatorów bez jawnego przeliczenia konwencji.

---

7. Nowe osie sesji

7.1 Konsekwencje dla innych filarów

Bez zmian wobec v1.6.5.

7.2 Regulacja τ — 💡, nieoperacyjne

Bez zmian.

7.3 Wersja sekwencyjna τ_relation — ✅ kompletna

7.3.1 Konstrukcja operatora rundy

$M_m(\alpha) = I - \alpha e_m e_m^\top + \frac{\alpha}{n} e_m \mathbf{1}^\top$. Pełna runda: $R_\sigma(\alpha) = M_{\sigma(n)}(\alpha)\cdots M_{\sigma(1)}(\alpha)$.

Fakt 7.3.0 (✅). $R_\sigma(\alpha) = P_\sigma R_{\rm id}(\alpha) P_\sigma^{-1}$, gdzie $P_\sigma$ = macierz permutacji odwrotna do kolejności aktualizacji. Sanity check $n=3$, $\sigma = (2,3,1)$: $\mu_{{\rm num}} = (3,1,2)/6 = P_\sigma \mu_{\rm id}$ ✓.

7.3.2 Twierdzenie 7.3.1 — konsensus końcowy (✅)

Dla $n \geq 2$, $\sigma$ dowolnej kolejności, $x_0 \in \mathbb{R}^n$, $\alpha \in (0, \alpha^*)$:
\lim_{k\to\infty} R_\sigma^k x_0 = c_\sigma(x_0)\mathbf{1}, \qquad
c_\sigma(x_0) = \frac{\sum_k w_k^{(\alpha,n)}\,x_{0,\sigma(k)}}{\sum_k w_k^{(\alpha,n)}}.

7.3.3 Twierdzenie 7.3.2 — rozrzut po kolejnościach (✅)

Dla $x_{(1)} \leq \cdots \leq x_{(n)}$, $\alpha \in (0, \alpha^*)$:
\Delta_\sigma c(x_0, \alpha) = \frac{\alpha}{nW}\sum_{k=1}^n (2k-n-1)\,x_{(k)}, \qquad W = n - \frac{\alpha(n-1)}{2}.

Maksymalizacja po $\sigma$, nie po $x_0$. Redukcja do α=1: $b/W = 2/(n(n+1))$.

7.3.4 Trzy miary — rozdzielenie

Miara Zależność od σ
konsensus $c_\sigma$ TAK
tempo $T_\epsilon$ NIE dla $n=4$, $\epsilon=10^{-6}$
rate $\rho_{\rm rate}$ NIE (Fakt 7.3.0)

7.3.5 Co pozostaje otwarte

1. Kto mówi pierwszy dla grafu niezupełnego (P4).
2. Definicja $\gamma^2_{\rm window}$ (P11).
3. Ogólna postać $T_\epsilon(\sigma)$.
4. Wybór α.
5. Rozszerzenie na grafy niepełne (P15).

7.3.6 Twierdzenie 7.3.6 — rodzina parametryczna (✅)

Wyróżnione punkty: $0^+$ (identyczność), $1$ (v5.1), $n/(n-1)$ (notatnik), $2n/(n-1)$ (granica stabilności).

w_k^{(\alpha,n)} = \frac{1 + \frac{\alpha}{n}(k-n)}{n - \frac{\alpha(n-1)}{2}}, \qquad k = 1,\dots,n.

Liniowość $w_k$ w $k$ dla każdego α. Suma: $n - \alpha(n-1)/2$. Blok Jordana przy $\alpha^* = 2n/(n-1)$: $\dim\ker(R-I)=1$, $\dim\ker((R-I)^2)=2$, iteracja rośnie liniowo.

7.4 Audyty i asymptotyka

7.4.6 Twierdzenie 7.4.6 — Jacobi = symetryzacja GS (✅)

$\text{mean}_{\sigma} c_\sigma^{(\alpha)}(x_0) = \text{mean}(x_0)$ dla każdego $\alpha \in (0, \alpha^*)$.

7.4.7 Region stabilności GS (🔍)

$\rho_{\rm rate}(\alpha, n) < 1$ dla $\alpha \in (0, \alpha^*)$, $n$ do 10000.

7.4.9 Asymptotyka widma $R_\sigma(\alpha=1)$ (🔍)

Układ transcendentny: $\cos\theta = r(1-\ln r)$, $\theta - \sin\theta/r = -2\pi$. Rozwiązanie: $r_\infty \approx 0{,}12383$, $\theta_\infty \approx 67{,}40°$.

Korekta do S11-A w P₀-Scalar. S11-A mówi $|\lambda|_\infty = 1/8$; poprawna asymptota $\approx 0{,}12383$. Korekta dotyczy Scalar, nie TAU.

7.4.10 Współczynnik bloku Jordana (🔍)

$\rho_{\rm rate}(\alpha^* - \varepsilon) = 1 - (n-1)/(n+1)\varepsilon + O(\varepsilon^2)$.

7.5 Most TAU↔Memory — 💡

Dane M16a §8bis.4: batch 0.71%, seq 67.76%. Tw. 7.4.6 przewiduje jakościową zgodność. Wymaga mostu ilościowego (P14).

7.6 P17 — relacyjna skala czasoprzestrzenna (❌ zamknięte)

P17-B sfalsyfikowane dla zamrożonej konfiguracji. P17-A nieprowadzone. P17d zarejestrowane. Zasada: program po trzech rundach kandydatek bez pozytywnego wyniku zostaje zamknięty.

7.7 P21/P22/P23

· P21 (❌) — kolorowanie krawędziowe jako definicja warstwy. Odrzucone (wymaga orientacji, tworzy czwarty operator). $\chi'({\rm iko})=5$ zachowane jako fakt o strukturze.
· P22 (💡) — kolorowanie wierzchołkowe jako harmonogram blokowy. Dla $K_4$ = GS, dla ikosaedru = blok GS (4 × 3).
· P23 (🔍) — naturalna orientacja DAG. Wynik Claude'a był artefaktem α=0.5. Kandydackie orientacje: indeks, znak $D_e$ (M16), para przeciwległa.

7.8 5K₄ — pięciokątna bipiramidа (SKORYGOWANE v1.7.2)

7.8.1 Struktura

Odniesienie empiryczne (2026-09-27). Autor wykonał fizyczny model 5 foremnych czworościanów wokół wspólnej krawędzi. Model nie domyka się — deficyt $7{,}36°$ widoczny.

Status modelu fizycznego. Sprawdzian realizowalności, nie niezależne potwierdzenie liczbowe. Potwierdza, że deficyt jest widoczny w realnej geometrii, ale nie dostarcza pomiaru z niepewnością. Deficyt $7{,}36°$ jest już potwierdzony niezależnie dwoma metodami numerycznymi w p0-axis §8.5.9 (BFGS/SLSQP i wzór analityczny $1/(\tan(\pi/5)\sqrt2)$, zgodność 5–6 cyfr).

Twierdzenie geometryczne. Deficyt $7{,}36°$ wynika z elementarnego rachunku kątowego: kąt dwuścienny foremnego czworościanu $\theta_d = \arccos(1/3) \approx 70{,}5288°$ nie dzieli $2\pi$. Znane od czasów błędu Arystotelesa (De Caelo).

Uwaga metodologiczna (Claude, 2026-09-27). Wcześniejsze wersje (v1.7.1) powoływały się na twierdzenie Dehna (1900) i pracę Radina (1997, Ann. of Math. 146). Cytat Radina nie potwierdza się. Co ważniejsze, Dehn nie implikuje niemożności trybułacji — dotyczy scissors-congruence (trzeci problem Hilberta), co jest niezależną własnością. Usunięte.

Struktura:

Element Liczba
Wierzchołki 7 (2 apex $A_{\rm top}, A_{\rm bot}$ + 5 równikowych $E_k$)
Krawędzie zewnętrzne 15
Krawędź wewnętrzna 1 (oś $A_{\rm top}$–$A_{\rm bot}$)
Ściany zewnętrzne 10
Ściany wewnętrzne 5
Czworościany 5 ($T_k = \{A_{\rm top}, A_{\rm bot}, E_k, E_{k+1}\}$, mod 5)
Symetria $D_5$
Eulera $7 - 15 + 10 = 2$ ✓

Deficyt: $\delta = 2\pi - 5\theta_d \approx 7{,}356°$. Skurcz z kontaktem symetrycznym: $r_{\rm scale} = 0{,}973254$ (skurcz krawędzi o $2{,}675\%$).

7.8.2 $p_0^{\rm styk}$ — analiza

Konwencja bazowa §7.8. Sub-tetraedry używają konwencji exclude-self: w $T_k$, $A_{\rm top}$ widzi $\{A_{\rm bot}, E_k, E_{k+1}\}$, nie siebie. Uśrednienie po 5 tetraedrach: $\frac{1}{5}\sum_k$.

Adnotacja porównawcza. §7.3.1 używa konwencji include-self ($x_m' = (1-\alpha)x_m + \frac{\alpha}{n}\sum_j x_j$). Obie konwencje są równoważne po przeskalowaniu α dla grafów pełnych (Tw. 0.2.1), ale nie są równoważne dla 5K₄ (bo $\deg(m)$ zależy od $m$). Wszystkie porównania z §7.3.1 wymagają przeliczenia na wspólną konwencję.

Rachunek. Dla $A_{\rm top}$: $A_{\rm top}' = (1-\alpha)A_{\rm top} + \frac{\alpha}{15}[5 A_{\rm bot} + 2\sum_k E_k]$. Odejmowanie:

\boxed{A_{\rm top}' - A_{\rm bot}' = \left(1 - \frac{4\alpha}{3}\right)(A_{\rm top} - A_{\rm bot}).}

Krytyczne α dla styku (exclude-self): $\alpha_{\rm crit}^{\rm styk} = 3/2$.

7.8.3 Porównanie z wnętrzem — skorygowane v1.7.2

Wynik (exclude-self, spójny). $\lambda_{\rm styk} = 1 - 4\alpha/3$, $\alpha_{\rm crit} = 3/2$.

Kontrola porównawcza (include-self). Ta sama struktura pod konwencją §7.3.1 daje $\lambda = 1 - \alpha$, $\alpha_{\rm crit} = 2$ — identycznie jak wnętrze $K_n$ w tej samej konwencji.

Wniosek. Styk i wnętrze mają identyczne tempo zbieżności pod każdą spójną konwencją. Wartości $3/2$ i $2$ nie są porównywalne — pochodzą z różnych konwencji. Nie ma podstaw do twierdzenia „styk jest szybszym kanałem". To był artefakt porównania konwencji (ten sam typ co w §0.2).

Co zostaje: $p_0^{\rm styk}$ istnieje — podprzestrzeń $A_{\rm top} = A_{\rm bot}$, wymiaru 6 w $\mathbb{R}^7$. Niezmiennicza, ale nie jest przestrzenią własną — wewnątrz niej $E_k$ nadal ewoluują (zbiegają do wspólnej wartości z $A_{\rm top}/A_{\rm bot}$). $p_0^{\rm styk}$ to droga do konsensusu, nie osobny cel.

7.8.7 Trzy modele tej samej struktury (NOWE v1.7.1)

5K₄ pojawia się w trzech różnych modelach:

Model Stan Dynamika Źródło
A — geometryczny pozycja w $\mathbb{R}^3$ sztywność (każdy tetraedr foremny) p0-axis §8.5.9
B — skalarny wartość na wierzchołku uśrednianie Jacobi/GS §7.8.2
C — mieszany pozycja + więzy uśrednianie pod więzami do zbudowania

Kluczowe rozróżnienie. Model B nie wie o długościach krawędzi — wierzchołki to etykiety bez struktury metrycznej. Nie może odtworzyć nierówności promienisty/obwodowy z modelu A.

Twierdzenie 7.8.7.1 (✅, zakres doprecyzowany GPT 2026-09-27). Niech $\alpha \in (0, \alpha_{\rm crit})$ dla modelu B (exclude-self, §7.8.2). Wtedy pełny konsensus ($A_{\rm top} = A_{\rm bot} = E_1 = \dots = E_5$) jest jedynym punktem stałym. Krotność wartości własnej $\lambda = 1$ wynosi dokładnie 1, wektor własny = wektor jednorodny.

Uwaga o α = 0. Operator jest identycznością — każdy stan jest punktem stałym. Zakres twierdzenia: $\alpha > 0$.

Uwaga o α ≥ α_crit. Dla α ≥ α_crit = 3/2 (Tw. 7.8.7.2) dynamika traci stabilność. Twierdzenie nie ma zastosowania.

Twierdzenie 7.8.7.2 (✅, NOWE v1.7.2, Claude 2026-09-27). Dla $m$K₄ (bipiramidy o $m$ foremnych czworościanach wokół wspólnej osi, $m \geq 3$), mnożnik zaniku różnicy na wspólnej krawędzi wynosi
\lambda_{\rm styk}^{(m)} = 1 - \frac{4\alpha}{3},


niezależnie od $m$. Krytyczne α dla styku: $\alpha_{\rm crit}^{(m)} = 3/2$ (exclude-self).

Dowód (szkic). Każdy tetraedr $T_k$ w $m$K₄ ma dokładnie 3 sąsiadów dla $A_{\rm top}$: $\{A_{\rm bot}, E_k, E_{k+1}\}$ (niezależnie od $m$). Uśrednienie po $m$ tetraedrach: suma $\sum_k (A_{\rm bot} + E_k + E_{k+1}) = m A_{\rm bot} + 2\sum_k E_k$. Odejmowanie daje $(1 - 4\alpha/3)(A_{\rm top} - A_{\rm bot})$. Identyczne dla każdego $m \geq 3$. ∎

Adnotacja GPT (2026-09-27). Twierdzenie dotyczy wyłącznie mnożnika zaniku różnicy na wspólnej osi, nie pełnego widma operatora ani stabilności całego układu. Pełne widmo ma inne wartości własne, które mogą być inne dla każdego $m$ — to jest osobne pytanie.

Konsekwencja. $c_m = 4/3$ jest uniwersalny w klasie $m$K₄.

Korekta v1.7.1 → v1.7.2. W v1.7.1 napisałem $\alpha_{\rm crit} = 4/3$ w odsyłaczu Korekty 2. To błąd — liczba $4/3$ pochodzi z §7.3.6 (notatnik, $n=4$, konwencja include-self, izolowany $K_4$), cicho przeniesiona jako własność 5K₄ (exclude-self). Prawidłowa wartość: $\alpha_{\rm crit} = 3/2$. Wykryte przez Claude (2026-09-27).

7.8.8 Co P10-alt nie twierdzi

· Warstwy czasowe ≠ warstwy aktualizacji (P22).
· Deficyt $7{,}36°$ ≠ $\tau_0$ w sensie §2.
· Warstwy pierwsze niekoniecznie opierają się uśrednieniu — to przewidywanie do testu.

---

8. Co wiemy

8.1 Ustalone ✅

1–5 (z sesji 21/22.09).

6. Tw. 7.3.1, 7.3.2, 7.3.6 — konsensus, rozrzut, rodzina.
7. Fakt 7.3.0.
8. Tw. 7.4.6 — Jacobi = symetryzacja GS.
9. Tw. 0.2.1 — równoważność globalny/lokalny dla $K_n$.
10. Blok Jordana przy α* ($n=3,\dots,12$).
11. $p_0^{\rm styk}$ w 5K₄ — niezmiennicza podprzestrzeń.
12. Tw. 7.8.7.1 — pełny konsensus jedynym punktem stałym modelu B ($\alpha > 0$).
13. Tw. 7.8.7.2 — $c_m = 4/3$ uniwersalne dla $m \geq 3$.
14. Deficyt $7{,}36°$ — kątowy, elementarny (nie przez Dehna).
15. Empiryczne potwierdzenie deficytu (sprawdzian realizowalności).

8.2 Sfalsyfikowane ❌

1–10 (z sesji 21-27.09).

11. P21 — kolorowanie krawędziowe jako definicja warstwy.
12. Cytat Dehn/Radin — nie potwierdza się.
13. $\alpha_{\rm crit} = 4/3$ dla 5K₄ — mylone z notatnikiem.

8.3 Kandydaci 🔍💡

1–9 (z v1.6.6).

10. P10-alt — hierarchia warstw przez 5K₄.
11. P24 — model C (dynamika pod więzami).
12. P25 — uogólnienie $p_0^{\rm styk}$ na $m$K₄ (rozstrzygnięte jako P27 ✅).
13. P26 — sekwencyjna dynamika na 5K₄.

---

9. Otwarte pytania

P1–P9, P11–P16. Bez zmian.

P10 (❌). Konkretna realizacja z v1.3 sfalsyfikowana.

P10-alt (💡). Hierarchia warstw przez 5K₄.

P17-A (💡) / P17-B (❌) / P17d (💡). Zamknięte jako program.

P18 (💡). Nowa klasa $(\ell, t)$ — wstrzymane.

P19 (💡). Asymptotyka analityczna.

P20 (💡). Współczynnik $(n-1)/(n+1)$.

P22 (💡). Kolorowanie wierzchołkowe.

P23 (🔍). Naturalna orientacja DAG.

P24 (💡, przepisane). Model C — dynamika pod więzami. Wymaga decyzji autora:

· C1 — foremność czworościanów,
· C2 — dokładne pokrywanie się wierzchołków,
· C3 — kontrolowane odkształcenie.
· Dodatkowo: sekwencyjne czy symetryczne aktualizacje więzów?

P26 (💡, gotowe do uruchomienia). Sekwencyjna dynamika modelu B (bez właściwości geometrycznych).

P27 (✅, zamknięte v1.7.2). $c_m = 4/3$ dla wszystkich $m \geq 3$.

Otwarte, nowe (v1.3.2). Wybór α w rodzinie $M_m(\alpha)$.

---

10. Rekomendacje i kolejność

10.1–10.2

Bez zmian.

10.3 Kolejność (v1.7.2)

Priorytet Zadanie Status
0 Definicja warstwy czasowej — pytanie do autora ❌
0 Wybór α — pytanie do autora 🔍
1 P26 — sekwencyjna dynamika modelu B 💡 gotowe do uruchomienia
2 P24 — model C (wymaga decyzji C1/C2/C3) 💡
3 P19 — asymptotyka analityczna 💡
4 P20 — współczynnik bloku Jordana 💡
5 P22 — blok GS dla ikosaedru 💡
6 P23 — naturalna orientacja DAG 🔍
7 P10-alt — test hierarchii warstw 💡
8 P15, P14 💡

Zamknięte: P17 (❌), P21 (❌), P27 (✅).

---

11. Meta — o sesji 21–27.09

Sesja dała:

· Sześć twierdzeń ✅ (Tw. 7.3.1, 7.3.2, 7.3.6, 7.4.6, 0.2.1, 7.8.7.1, 7.8.7.2).
· Fakt 7.3.0.
· Blok Jordana przy α*.
· Region stabilności (Tw. 7.4.7).
· Asymptotyka widma (§7.4.9, $r_\infty \approx 0{,}12383$, korekta do Scalar).
· Współczynnik $(n-1)/(n+1)$.
· $p_0^{\rm styk}$ w 5K₄ i uniwersalność $c_m = 4/3$.
· Most TAU↔Memory (💡).
· Trzy programy zamknięte negatywnie (P17, P21, Dehn/Radin).
· Fizyczne potwierdzenie deficytu $7{,}36°$.
· Trzynaście udokumentowanych błędów (§6).

Sesja 21–27.09 zamknięta. τ_relation nadal niezmierzone. Ale 5K₄ daje pierwszy konkretny przedmiot — strukturę, w której „wspólny czas relacji" ma geometryczny sens, i w której uniwersalność $c_m = 4/3$ została udowodniona.

---

12. Historia

Data Zmiana
2026-09-22 v0.1–v0.2
2026-09-25 v1.0–v1.5
2026-09-26 v1.6–v1.6.5
2026-09-27 v1.6.6 — §0.2 poprawione; P21 zamknięte; P22, P23 otwarte
2026-09-27 v1.7 — §7.8 NOWE (5K₄ jako obiekt); P10 rozszczepione; P24, P25, P26 nowe
2026-09-27 v1.7.1 — korekta §7.8 (konwencja exclude-self, usunięcie „szybszego kanału", §7.8.7 trzy modele); P24 jako pytanie otwarte
2026-09-27 v1.7.2 — usunięcie fałszywego cytatu Dehn/Radin; Tw. 7.8.7.1 z jawnym zakresem α; Tw. 7.8.7.2 NOWE (P27 zamknięte: $c_m = 4/3$ uniwersalne dla $m \geq 3$); korekta $\alpha_{\rm crit} = 3/2$ (nie 4/3) po wykryciu przez Claude; pozycja 13 w katalogu błędów

---

P₀-TAU v1.7.2. Korekta po recenzji Claude i GPT (2026-09-27). Kluczowe: dwa twierdzenia o $p_0^{\rm styk}$ (Tw. 7.8.7.1, 7.8.7.2), P27 zamknięte, usunięty fałszywy cytat. §1.1 motywacyjny, §1.2 rozszczepione, P10 ❌, τ_relation nadal niezmierzone. Kolejny krok: P26 (sekwencyjna dynamika modelu B) — gotowe do uruchomienia.