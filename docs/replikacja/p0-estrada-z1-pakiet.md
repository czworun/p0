> **Zrzut z warsztatu P₀, 2026-11-02.** Specyfikacja Z3 do niezależnej replikacji (Z1); żywa wersja prowadzona w warsztacie. Wyniki i rejestr: [p0-estrada-z1-wyniki.md](p0-estrada-z1-wyniki.md). Przykład raportu niezależnego: [p0-estrada-z1-raport-asterion.md](p0-estrada-z1-raport-asterion.md).


# Pakiet replikacji Z1 — P₀–Estrada, §35 (bazowe) + §36 (nieskończoności sektora cyklicznego)

**Do:** Claude, GPT, DeepSeek (protokół zespołu modeli; przekaz przez Leszka).
**Od:** Vibe, 2026-11-02 (sesja bez hasła — rachunek pojedynczy, 🔍; ten pakiet = specyfikacja Z3 do niezależnej replikacji Z1).
**Źródło:** filar P₀–Estrada v0.9, §35 (eksperyment P₀–Estrada-03, wykonany 2026-11-01) + analiza §36 „nieskończoności przestrzeni emergentnej" (2026-11-02, jeszcze niewpisana do filara — statuses poniżej).

## 0. Protokół (z metodyki P₀, obowiązujące bez wyjątków)

1. **Liczby jawnym tekstem** — inline math/LaTeX ginie w przekazie; każdą wartość piszemy cyframi.
2. **Atrybucja każdej wartości jawna** — skąd pochodzi każda liczba w Twoim raporcie (konstrukcja, bramka, seed).
3. **Wartość bez źródła w zleceniu ⇒ STOP i pytanie** — nie zgadujemy.
4. **Z1:** żaden wynik numeryczny nie dostaje ✅ z jednej implementacji. ✅ wymaga co najmniej dwóch zgodnych rachunków niezależnych implementacji tej samej specyfikacji. Raport pojedynczego modelu = 🔍 (lub ✅-kandydat dla bramek wymiernych, po zgodzie co do cyfry).
5. **Z2:** każda tabela podaje jednostki, porządek klas, orientację, normalizację.
6. **Z3:** przekazujemy specyfikacje i wyniki, nigdy kodu. Poniższe konstrukcje opisane są matematycznie; implementacja dowolna, byle spełniała bramki residuów.
7. **Erraty wprost.** Jeśli znajdziesz rozbieżność — zgłoś ją jako kandydata erraty z liczbami, nie „popraw się" same.
8. **Metodyka tolerancji:** bramki wymierne (oznaczone „wym.") — odchyłka ≤ 1e−12; bramki numeryczne — tolerancja podana przy bramce.

## 1. Kontekst merytoryczny

Sekwencyjny protokół SERC na K₄ (4 serca-wierzchołki, uśrednianie po jednym, deflacja konsensusu po rundzie + renormalizacja) wytwarza na sferze V_cyc ruch wieczny, nie kolapsując (§35.5). Pytanie §36: **gdzie w tej przestrzeni emergentnej siedzą „nieskończoności"** — hipoteza Leszka: na środkach krawędzi K₄. Teza do weryfikacji replikacją:

- (T1) Izolowane „nieskończoności" dyskryminantu relacyjnego to 14 punktów = stella octangula: 6 na środkach krawędzi (bieguny rzędu 2) + 8 na ±wierzchołkach (bieguny rzędu 3, głębsze).
- (T2) Bieguny przepływu ±û NIE leżą na środkach krawędzi (najbliżej: 25.49° od środków par przekątnych).
- (T3) Nieskończoność konsensusu (centrum, jedyna nieskończona rezolwenta) jest usunięta przez protokół.
- (T4) Trajektoria wiecznego ruchu muska ściany (przecina każdą 2× na okres) i trzyma wieczne marginesy od 14 punktów izolowanych.

## 2. Konwencje (Z2, jawne)

### 2.1 Bazowe (§35.0, bez zmian)

- Wierzchołki 0–3. Takt = aktualizacja jednego wierzchołka macierzą M_i = I z wierszem i równym 1/4 (include-self). Runda = 4 takty.
- Propagator rundy: W = M_ost · … · M_pierwszy (pierwszy takt po prawej).
- Porządki: naturalny [0,1,2,3] ⇒ W_nat = M_3·M_2·M_1·M_0; lustrzany [0,1,3,2] ⇒ W_mir = M_2·M_3·M_1·M_0.
- Deflacja PO rundzie: P_c = I − J/4 (J = macierz samych jedynek; P_c x = x − średnia(x)·𝟙).
- Renormalizacja L2 do normy 1. Φ = normalize ∘ P_c ∘ W.
- B4 = P_c·W; B4·𝟙 = 0. **ERT-1 (errata, Asterion 2026-11-02, przyjęta):** wcześniejsze tu zdanie „wnika: B4 = W na V_cyc" było FAŁSZYWE — W nie zachowuje V_cyc (kontrprzykład: x = (1,−1,0,0), Wx = (0,−1/4,−1/16,−5/64), suma = −25/64 ≠ 0; B4x = (25,−39,9,5)/256). Poprawne stwierdzenie: B4 i W mają wspólne wektory własne dla λ ≠ 1 (stąd przenoszenie widma na komplementum), ale jako operatory na V_cyc różnią się o składnik konsensusu: B4x = Wx − średnia(Wx)·𝟙.
- V_cyc = {x : suma współrzędnych = 0} ∩ {norma = 1} — sfera jednostkowa w 3-wymiarowej przestrzeni cyklicznej.

### 2.2 Nowe (§36)

- **Ściany:** C_ab = {x ∈ V_cyc : x_a = x_b}, 6 wielkich okręgów, pary (a,b) w porządku leksykograficznym: (0,1),(0,2),(0,3),(1,2),(1,3),(2,3). Wszystkie tabele 6-elementowe stosują ten porządek.
- **14 punktów:** v̂_i = (e_i − 𝟙/4) znormalizowane (wierzchołki, 4 szt. + 4 antypody); m̂_ij = (v̂_i + v̂_j) znormalizowane (środki krawędzi, 6 szt., pary antypodalne w środku zestawu: m̂_01 = −m̂_23, m̂_02 = −m̂_13, m̂_03 = −m̂_12).
- **Dyskryminant:** Δ(x) = iloczyn Vandermonde'a po wszystkich 6 parach: Δ(x) = (x_0−x_1)(x_0−x_2)(x_0−x_3)(x_1−x_2)(x_1−x_3)(x_2−x_3); na bramkach wartość bezwzględna. UWAGA: konwencja pełnego iloczynu 6-czynnikowego (punkt arytmetyczny (−3,−1,1,3)/√20 daje |Δ| = 0.096).
- **Faza skośna:** α(x) = wᵀx, gdzie w = lewy wektor własny B4 dla wartości własnej λ_c (część urojona dodatnia); α ma wartości zespolone (Re α i Im α to dwa rzeczywiste funkcjonały). Gauge: obrót fazy w tak, że α(v̂_0) jest rzeczywiste i dodatnie; fazą punktu x jest arg(α(x)) w stopniach, zawinięta do (−180, 180].
- **Odstępy faz wierzchołków:** 4 wartości φ(v̂_i) sortujemy rosnąco; odstępy = kolejne różnice + odstęp domykający (suma = 360°); multi-zbiór odstępów jest niezmienniczy względem gauge.
- **δ-offsety środka:** δ_ij = φ(m̂_ij) − (φ(v̂_i)+φ(v̂_j))/2, zawinięte do (−180,180]; jeśli |δ| > 90°, bierzemy drugiego reprezentanta (δ ∓ 180°) — konwencja |δ| ≤ 90°.
- **Krzywa graniczna:** z = wektor własny B4 dla λ_c znormalizowany tak, że suma_k |z_k|² = 1; krzywa to p(t) = cos(t)·Re z + sin(t)·Im z po rzucie na sferę (p/‖p‖), t ∈ [0, 360°). Osie elipsy = pierwiastki z wartości własnych macierzy Grama [[⟨z_r,z_r⟩, ⟨z_r,z_i⟩], [⟨z_r,z_i⟩, ⟨z_i,z_i⟩]].
- **Płaszczyzna E (definicja obowiązkowa dla F4; uzupełniona po erracie ERT-2):** E = span_R{Re z, Im z} — niezmiennicza płaszczyzna pary zespolonej (jak w §35.5 filara), czyli płaszczyzna krzywej granicznej. Kąt wektora do E: rzut ORTOGONALNY przez rozwiązanie układu Grama 2×2 (baza Re z, Im z NIE jest ortogonalna: ⟨Re z, Im z⟩ ≈ 0.183; rzut „naiwny" ⟨x,Re z⟩·Re z + ⟨x,Im z⟩·Im z jest BŁĘDNY — tak powstała wycofana wartość 46.814°, patrz ERR-2 w §14).
- **Marginesy:** odległość cięciwa (chord) min p(t) → punkt, po rzucie na sferę.
- **Promień osadzenia R_n:** średnia arytmetyczna (po 4 osadzonych wierzchołkach Φⁿ(e_i)) odległości od centroidu c_n = (1/4)·suma obrazów. (Definicja odzyskana 2026-11-02 — odtwarza okno §35.5.) Trajektorie Φⁿ(e_i) i Φⁿ(v̂_i) pokrywają się po normalizacji (W𝟙 = 𝟙, P_c𝟙 = 0 ⇒ P_cWⁿe_i = (√3/2)·P_cWⁿv̂_i) — obie konwencje startu dają te same obrazy (uwaga Claude'a 2026-11-02, przyjęta).
- **Kierunki losowe** (tylko bramki rzędów biegunów): LCG seed = 42, mod 2³¹, mnożnik 1103515245, przyrost 12345; wartość = seed/2³⁰ − 1. Każdy kierunek: rzut na V_cyc (odjęcie średniej), odjęcie składowej wzdłuż punktu bazowego, normalizacja. Determinizm (DOP-1, przyjęta): stan aktualizowany PRZED odczytem (v = nowe_seed/2³⁰ − 1), jeden ciągły strumień bez resetów między punktami; regresja rzędu: 3 punkty t ∈ {1e−2, 1e−3, 1e−4} na okręgu wielkim, wykładnik = (logΔ(1e−3) − logΔ(1e−4))/log 10.

## 3. Konstrukcje wektorów własnych (Z3: spec, nie kod) + ostrzeżenia solverowe

**Lekcja z sesji 2026-11-02 (dobra wstępna errata):** klasa błędów eliminacji Gaussa przy szukaniu jądra (B−λI): w podstawieniu wstecznym sumować wkłady WSZYSTKICH już wyznaczonych kolumn osiowych — dwie niezależne implementacje Vibe dały błędne wektory na tej samej zasadzie (wektory „wyznaczone", ale nie we własnej przestrzeni; przy prawidłowej implementacji zgodność 6.4e−17). Wymogi: (a) residuum ‖Bv − λv‖/‖v‖ ≤ 1e−12 dla KAŻDEJ pary; (b) co najmniej jedna para sprawdzona drugą, niezależną konstrukcją (zgodność ≤ 1e−12); (c) pierwiastki wielomianu charakterystycznego polerować Newtonem (2–3 iteracje) — surowe pierwiastki z metody iteracyjnej mogą mieć błąd ~1e−8, co psuje rangę macierzy osobliwej.

**Konstrukcja Krylowa (czysto rzeczywista, zalecana):**

- **z (prawy wektor, λ_c):** weź y generyczne (np. (0.37, −0.52, 0.81, −0.23)); u0 = B4·(B4 − λ_r)·y — zabija konsensus (przez B4) i mod λ_r (przez (B4−λ_r)), zostaje czysta podprzestrzeń pary zespolonej; v0 = B4·u0. Rzut B4 na span(u0, v0): rozwiąż rzut metodą Grama (rama NIEortogonalna: (α, β; γ, δ) z iloczynów skalarnych). Bramki kontrolne mini-macierzy: ślad = 2·Re λ_c, wyznacznik = |λ_c|². Wektor własny mini-macierzy: (ξ, η) ∝ (γ, λ_c − α); z = ξ·u0 + η·v0.
- **w (lewy wektor, λ_c):** jw., z B4ᵀ zamiast B4.
- **û (biegun, mod λ_r):** q = (B4² − 2·Re(λ_c)·B4 + |λ_c|²)·y — UWAGA: plus przy |λ_c|²·y (błąd znaku daje wektor o residuum ~6e−2, który przechodzi spot-checki); potem P_c·q (zabija konsensus) i normalizacja.
- **Tożsamości kontrolne:** α(z_r) − i·α(z_i) = 0 (wᵀz̄ = 0); |α| na krzywej granicznej ∝ 1/‖p(t)‖ (nigdy nie znika); wᵀû = 0.

## 4. Bramki A — bazowe spektralne (A1, A2, A5, A6, A7 wymierne, odchyłka 0; A3, A4 numeryczne, tolerancja ±1e−9 — restrykcja ERT-3, przyjęta)

| # | Bramka | Wartość oczekiwana |
|---|---|---|
| A1 | wielomian charakterystyczny W_nat | λ⁴ − 369/256·λ³ + 131/256·λ² − 19/256·λ + 1/256 (ślad 369/256, det 1/256) |
| A1b | jawne macierze wymierne propagatorów (kanoniczna forma kontrolna; wkład DeepSeek 2026-11-02, weryfikacja Vibe: zgodność co do cyfry, 256·W całkowite, sumy wierszy 256) | W_nat = 1/256 · [[64,64,64,64],[16,80,80,80],[20,36,100,100],[25,45,61,125]]; W_mir = 1/256 · [[64,64,64,64],[16,80,80,80],[25,45,125,61],[20,36,100,100]] (wiersze 2↔3 względem W_nat, zgodnie z P(23)) |
| A2 | wielomian charakterystyczny B4 (i B4_mir) | λ⁴ − 113/256·λ³ + 18/256·λ² − 1/256·λ (wyraz wolny 0) |
| A3 | widmo B4 | {0, 0.134710644695, 0.153347802652 ± 0.074039102546·i} (pełna precyzja) |
| A4 | θ = arg λ_c, ρ = |λ_c| | θ = 25.772093727472°/rundę (skrócone 25.7721°); ρ = 0.170286045477 |
| A5 | B4·𝟙 | 0 (norma 0) |
| A6 | sprzężenie lustrzane | W_mir = P(23)·W_nat·P(23) identycznie (max odchyłka 0) |
| A7 | nieparzystość Φ | Φ(−x) = −Φ(x) identycznie (B4 liniowe, normalize komutuje z −) |

## 5. Bramki B — struktura 14 punktów (formuły kanoniczne; weryfikacja numeryczna ≤ 1e−15 względem formuły — restrykcja ERT-3, przyjęta)

| # | Bramka | Wartość oczekiwana |
|---|---|---|
| B1 | środki jako wzorce | m̂_01 = (1, 1, −1, −1)/2 co do cyfry (analogicznie pozostałe z permutacji) |
| B2 | ortogonalność osi | m̂_01·m̂_02 = m̂_01·m̂_03 = m̂_02·m̂_03 = 0 (trzy osie osmiościanu) |
| B3 | antypodalność | m̂_01 + m̂_23 = 0; m̂_02 + m̂_13 = 0; m̂_03 + m̂_12 = 0 |
| B4 | kąty wierzchołek–środek | dokładnie: acos(1/√3) = 54.735610317245°… gdy i ∈ {i,j}; 180° − acos(1/√3) = 125.264389682755°… gdy i ∉ {i,j} (formuły kanoniczne; skrócone zapisy dziesiętne nie podlegają tolerancji 1e−15) |

## 6. Bramki C — dyskryminant Δ (rzędy 2/3/1 podniesione do twierdzeń analitycznych — zliczanie znikających czynników Vandermonde'a, DeepSeek 2026-11-02, niezależnie potwierdzone fitami numerycznymi Vibe/Asterion/Claude: w m̂_ij giną dokładnie czynniki (x_i−x_j) i (x_k−x_l), pozostałe 4 ≠ 0 ⇒ rząd 2; w v̂_i giną dokładnie (x_j−x_k),(x_j−x_l),(x_k−x_l) dla {j,k,l} ⊂ współrzędnych równych, pozostałe 3 ≠ 0 ⇒ rząd 3; na ogólnym punkcie ściany ginie dokładnie 1 czynnik ⇒ rząd 1)

| # | Bramka | Wartość oczekiwana | Tolerancja |
|---|---|---|---|
| C1 | rząd biegunu na środku (fit log-|Δ| vs log-t po okręgu wielkim, t ∈ 1e−4…1e−2, 3 kierunki LCG 42) | wykładnik = 2.000 | ±0.01 |
| C2 | rząd biegunu na wierzchołku ±v̂_i | wykładnik = 3.000 | ±0.01 |
| C3 | rząd na punkcie ogólnym ściany | wykładnik = 1.000 | ±0.02 |
| C4 | max |Δ| na sferze V_cyc | dokładnie 1/(6√3) = 0.096225044865 (podniesione do twierdzenia, patrz §14: warunek krytyczny r⁴ − 10r² + 1 = 0 w rodzinie (1,r,−r,−1); dowód analityczny Vibe + numeryka Vibe/Asterion/Claude, zgodność 15 cyfr) | ±1e−9 |
| C5 | typ argmaxu | składniki ∝ (1, r, −r, −1) z r = √(5−2√6) ≈ 0.317837245; orbita S₄; ciąg prawie-arytmetyczny ~3.147 : 1 : −1 : −3.147, NIE dokładnie (3,1,−1,−3)/√20 (tam |Δ| = 0.096 < 1/(6√3)) | — |

## 7. Bramki D — dynamika (numeryczne; starty = 4 wierzchołki v̂_i; okna jawnie)

| # | Bramka | Wartość oczekiwana | Tolerancja |
|---|---|---|---|
| D1 | ucieczka w 1 rundę: min szczelina ściany (min po 4 startach, po parach) | 0.096787 | ±1e−4 |
| D2 | szczeliny ścian po 1 rundzie (starty 0,1,2,3) | 0.104302, 0.264164, 0.096787, 0.350760 | ±1e−4 |
| D3 | |Δ| po 1 rundzie (starty 0,1,2,3) | 0.004660, 0.075436, 0.028878, 0.087756 | ±1e−4 |
| D4 | |Δ| asymptotycznie, n ∈ [100, 300] | [9.86e−5, 0.094072] | ±1e−3 |
| D5 | własne szczeliny ścian obrazów, n ∈ [100, 300] | [3.64e−4, 0.419665] | ±5% na dolnej granicy |
| D6 | odstępy obrazów (wszystkie 6 par, 4 starty), n ∈ [100, 300] | [0.717518, 1.985113] | ±1e−3 |
| D7 | odstępy par przekątnych (0,2) i (1,3) | [1.814063, 1.985113] (obrazy niemal antypodalne) | ±1e−3 |
| D8 | tętno: przyrost fazy skośnej na rundę | dokładnie θ od n = 0; odchyłka implementacyjna rzędu 1e−13…1e−14° (Vibe 5.7e−14, Asterion 7.8e−14, Claude 7.8e−14) na 300 rundach × 4 starty | 1e−9° |
| D9 | precesja: cięciwa ‖X(n+14) − X(n)‖, n ∈ [100, 286], 4 starty | średnia 0.014118, max 0.022046 | ±2e−3 |
| D10 | transport środków ‖Φ(m̂_ij) + m̂_ij‖ (pary wg porządku) | 1.945753, 1.982096, 1.898857, 1.898857, 1.982096, 1.945753 (niemal antypodalny) | ±1e−3 |
| D11 | promień osadzenia R_n, n ∈ [100, 200] | [0.962485, 0.987304] | ±1e−4 |
| D12 | kroki startowe ‖B4·v̂_i‖ | 0.172981, 0.153673, 0.139809, 0.205750 | ±1e−5 |

## 8. Bramki E — krzywa graniczna (numeryczne)

| # | Bramka | Wartość oczekiwana | Tolerancja |
|---|---|---|---|
| E1 | osie elipsy (normalizacja z: suma |z_k|² = 1) | 0.842008, 0.539466 | ±1e−4 |
| E2 | zmiany znaku na ścianach (6 ścian) | dokładnie 2 na każdą | dokładność liczby |
| E3 | marginesy od środków (pary (01),(02),(03),(12),(13),(23)) | 0.102727, 1.067370, 0.427859, 0.427859, 1.067370, 0.102727 | ±1e−3 |
| E4 | marginesy od ±v̂_i (i = 0,1,2,3) | 0.344211, 0.221984, 0.760304, 0.927427 | ±1e−3 |
| E5 | |α| na krzywej nie znika; niezmiennik min/max | stosunek min/max = ax₂/ax₁ = 0.640689597602 (pełna precyzja; ERR-3: wcześniejsza wartość 0.640676 błędna — geneza: wczesne próbkowanie siatkowe, nie zaokrąglenie osi; potwierdzone przez Asteriona i Claude'a) | ±1e−5 |
| E6 | min dystans krzywa → û | 0.693692 | ±1e−3 |
| E7 | kroki ‖B4·p‖ na krzywej | [0.139597, 0.207722] | ±1e−4 |
| E8 | max Δ na krzywej | 0.094072 | ±1e−3 |

Wzorzec E3/E4 symetryczny pod odwróceniem (0↔3, 1↔2) — echo C2.

## 9. Bramki F — biegun przepływu ±û (numeryczne; û określone co do znaku — bramki znakowo-niezależne)

| # | Bramka | Wartość oczekiwana | Tolerancja |
|---|---|---|---|
| F1 | |komponenty û| | 0.7116, 0.6090, 0.1911, 0.2936 (znaki naprzemienne: +−+− lub −+−+) | ±1e−4 |
| F2 | kąty do środków (min po ±m̂), pary (01),(02),(03),(12),(13),(23) | 84.11°, 25.49°, 65.29°, 65.29°, 25.49°, 84.11° | ±0.05° |
| F3 | kąty do ±v̂_i (i = 0,1,2,3) | 34.75°, 45.31°, 77.26°, 70.18° | ±0.05° |
| F4 | kąt û do płaszczyzny E (definicja: §2.2; E = span_R{Re z, Im z}; rzut ORTOGONALNY przez układ Grama 2×2, baza nieortogonalna) | 40.589057° (komplement do normalnej E: 49.410943°). ERR-2: wcześniejsze 46.814° = błąd rzutu naiwnego u Vibe; poprawka potwierdzona trzema rachunkami (Vibe, Asterion, Claude) | ±0.005° |
| F5 | wᵀ·û (w lewy wektor λ_c) | 0 | ≤ 1e−15 |
| F6 | kąt û_nat do û_mir | 40.087° | ±0.05° |

Odczyt T2: najbliższe środkom pary przekątne (0,2),(1,3) — te same, od których krzywa trzyma największe marginesy (E3: 1.067370).

## 10. Bramki G — jądra i rezolwenty (numeryczne)

| # | Bramka | Wartość oczekiwana | Tolerancja |
|---|---|---|---|
| G1 | wartości osobliwe B4 na V_cyc (sqrt z wartości własnych (B4V)ᵀ(B4V), V = baza ortonormalna V_cyc) | 0.226568, 0.145690, 0.118340 (malejąco) | ±1e−5 |
| G2 | G = (I − B4ᵀB4)⁻¹ na V_cyc | 1.054111, 1.021686, 1.014203 — wszędzie skończone | ±1e−4 |

Nieskończona rezolwenta tylko (I − W)⁻¹ na konsensusie — usunięta protokołem (T3).

## 11. Bramki H — lustro (permutacja (23); fazy w gauge φ(v̂_0) = 0)

| # | Bramka | Wartość oczekiwana | Tolerancja |
|---|---|---|---|
| H1 | φ(v̂_i), naturalny (i = 0,1,2,3) | 0°, −61.918°, −146.782°, 96.443° | ±0.02° |
| H2 | multi-zbiór odstępów cyklicznych | {61.918, 84.864, 96.443, 116.774}° — lustrzany identyczny | ±0.02° |
| H3 | δ-offsety naturalne (pary (01),(02),(03),(12),(13),(23)) | −9.321°, −44.690°, 26.204°, −1.224°, 44.656°, −15.110° | ±0.02° |
| H4 | δ-offsety lustrzane | dokładna permutacja (23) tabeli H3: −9.321°, 26.204°, −44.690°, 44.656°, −1.224°, −15.110° (zamiana par (02)↔(03) i (12)↔(13)) | ±0.02° |
| H5 | φ(v̂_i) lustrzany | 0°, −61.918°, 96.443°, −146.782° (etykiety 2↔3 zamienione względem H1) | ±0.02° |

## 12. Format raportu replikacji

1. Tabela: bramka | wartość | odchyłka od oczekiwanej | uwagi. Każda liczba z atrybucją (konstrukcja/metoda; dla kierunków LCG — seed).
2. Bramki A, B: potwierdzenie co do cyfry ⇒ raportujesz „✅-kandydat (wymierna)".
3. Bramki C–H: zgodność w tolerancji ⇒ „zgodne z rachunkiem Vibe (🔍)"; rozbieżność poza tolerancją ⇒ kandydat erraty z pełnym opisem konstrukcji (STOP-rule z §0 pkt 3).
4. Wartości ujemne wyników nie obalają zlecenia — errata jest pełnowartościowym owocem (Z0).
5. Statusy docelowe po zgodności dwóch implementacji: T1 ⇒ ✅ (układ ścian/14 punktów); T2, T4 ⇒ ✅ (geometria bieguna, marginesy); dynamika numeryczna (D, E) pozostaje 🔍 do skumulowania zgodności; T3 ⇒ ✅ (algebraiczne).

## 13. Atrybucja wartości oczekiwanych

Wszystkie wartości: Vibe, rachunek pojedynczy, 2026-11-02, pełna podwójna precyzja, bez bibliotek zewnętrznych; wektory własne konstrukcją Krylowa z bramkami residuów ≤ 2e−16 (zgodność z niezależną, naprawioną eliminacją Gaussa: 1.9e−15); pierwiastki polerowane Newtonem; maksimum |Δ| — wspinaczka ze startu siatki 16×32 na parametryzacji sfery V_cyc; krzywa — siatka 20000 punktów; tolerancje bramek uwzględniają rozdzielczość siatek. Wartości bazowe A1–A4 zgodne z korpusem (SERC R₄, tetr; §35.1). Kierunki losowe: LCG seed 42. Okna asymptotyczne jawnie w bramkach D.

## 14. Rejestr replikacji i errat

| Replikant | Data | Zakres | Wynik |
|---|---|---|---|
| Vibe (autor pakietu) | 2026-11-02 | A–H | rachunek źródłowy; dwie niezależne konstrukcje wektorów własnych (Krylow + GE po naprawie), zgodność 1.9e−15 |
| Asterion (GPT) | 2026-11-02 | A–H | A, B co do cyfry (✅-kandydat); C–H zgodne w tolerancjach; residua par własnych ≤ 2e−16, druga droga (SVD) zgodna ≤ 1.3e−15 |
| Claude | 2026-11-02 | A–H | A, B co do cyfry (✅-kandydat); C–H zgodne w tolerancjach; F4: 40.589° dla E = span(Re z, Im z) — zgodne z erratą; eig + Krylow zgodne ≤ 4e−16 |
| DeepSeek (raport podpisany „GPT/ChatGPT\"; relay Leszka identyfikuje jako DeepSeek) | 2026-11-02 | A, B symbolicznie; C1–C3 analitycznie | A1–A7, B1–B4 ✅-kandydat (wymierna) — w tym NOWE: jawna macierz W_nat = 1/256·[[64,64,64,64],[16,80,80,80],[20,36,100,100],[25,45,61,125]] (przyjęta jako bramka A1b) oraz niezależna droga A2 przez dzielenie A1/(λ−1) — korzysta z poprawionej lemy spektralnej ERT-1; C1–C3 wyprowadzone ANALITYCZNIE zliczaniem znikających czynników Vandermonde'a (rzędy 2/3/1 — trzecia droga, podniesione do twierdzeń, patrz §6); A3/A4 „warunkowo" (zgodność arytmetyczna z A2: suma 113/256, iloczyn 1/256); C4–H = STOP uczciwe (brak środowiska numerycznego; §0 pkt 3 zachowane) |

**Uwaga atrybucyjna (Z2):** raport DeepSeeka nosił nagłówek „GPT (ChatGPT)" przy treści z niezależnego środowiska DeepSeeka; wg identyfikacji Leszka (relay, 2026-11-02) autor = DeepSeek. Odnotowane tu jako lekcja protokołu: atrybucja należy do pola nadawcy, nie samo-deklaracji modelu.

**Erraty przyjęte (koncesje Vibe wprost):**
- ERT-1 (Asterion): „B4 = W na V_cyc" fałszywe — poprawione w §2.1; kontrprzykład wymierny.
- ERT-2 / ERR-2 (Asterion, potwierdzone przez Claude'a): F4 bez definicji E + błąd rzutu naiwnego u Vibe (46.814° → 40.589057°); definicja E i rzutu w §2.2.
- ERT-3 (Asterion): klasyfikacja tolerancji B4 i A3–A4 — formuły kanoniczne, tolerancje adekwatne.
- ERR-3 (Asterion, Claude): E5 = 0.640676 → 0.640689597602 = ax₂/ax₁ (pełna precyzja).
- DOP-1 (Asterion): determinizm LCG — uzupełnione w §2.2.
- R_n (Claude): równoważność startów e_i/v̂_i — uzupełnione w §2.2.

**Podniesienie (✅-kandydat):** C4 jako twierdzenie domknięte: max |Δ| na V_cyc = 1/(6√3) = 1/√108 dokładnie, osiągnięte na orbicie S₄ punktu (1, r, −r, −1)/‖·‖ z r = √(5−2√6) ≈ 0.317837245 (warunek krytyczny r⁴ − 10r² + 1 = 0). Drogi: dowód analityczny (Vibe 2026-11-02) + numeryka niezależna (Vibe wspinaczka, Asterion, Claude Nelder–Mead 400 startów) — zgodność do 15 cyfr.

**Wniosek statusowy — PRZYJĘTY (decyzja Leszka, 2026-11-02):** trzy zgodne rachunki (Vibe, Asterion, Claude) ⇒ **T1–T4 ✅ formalnie** (wpisane do filara P₀–Estrada v0.10 §36). Bramki numeryczne D, E: zgodność wielokrotna, status wg §12 pkt 5 (🔍 do skumulowania zgodności, formalne podniesienie przy wpisie do pnia).**