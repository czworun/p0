# Wklejka dla GPT: TAU-8, tr(R⁴) blind + pełny przebieg B–H wg errat v3/v4

> Zlecenie szefa laboratorium (Vibe), przygotowane 2026-11-15, runda 11bj (repo czworun/p0, commit źródłowy 09086cca). Protokół Z0–Z3 bez zmian: rachunek od zera, każda liczba z atrybucją (konstrukcja/metoda, solver, residuum), rozbieg z checkpointem > 1e−5 względnie = STOP + diagnoza, koncesje wprost. Wklejka jest samowystarczalna: wystarczy przekazać ją w całości.

## Kontekst (rozliczenie Twojego przebiegu E7, rejestr 2026-11-07)

Twój STOP „sprzeczność w specyfikacji" został rozliczony jako decyzja PRAWIDŁOWA wg Z1 (błąd po stronie wystawcy, Z0 potwierdzone): tabela wierzchołków pakietu v1 była przekręcona (transpozycja 5↔8, errata v3/E8, koncesja Vibe). Twój rachunek był poprawny dla obiektu v1: lista ścian odtworzona z tabeli v1 co do wpisu, fingerprinty tr(R_k) exact co do cyfry, a Twoje ρ 0.165561571 / 0.085888387 okazały się prawdziwymi wartościami macierzowymi (errata v4, koncesja pełna). Tabela wierzchołków w pakiecie jest już poprawiona in-place; poniżej pełny, aktualny zestaw normatywny.

## Zlecenie (do GPT)

1. **tr(R₄) wg tabeli wierzchołków POPRAWIONEJ** (pakiet poniżej, sekcja „Konstrukcja"), wariant nat, konwencja apex-first [P₀,v₂,v₁,v₀]: tr(R₄) = ślad iloczynu osadzeń E_t pierwszych czterech tetr sweepu węzła (tetry ścian f0, f1, f2, f3 w porządku lex, f₀ stosowana pierwsza; iloczyn E_{t(f3)}·E_{t(f2)}·E_{t(f1)}·E_{t(f0)}, macierz na 13 punktach węzła; R₂₀ = pełny R_node). Podaj wartość **BLIND** (nie podajemy wartości oczekiwanej; nie szukaj potwierdzenia u nikogo, po prostu policz i podaj z pełną atrybucją: konstrukcja, metoda, residuum).
2. **Pełny przebieg B–H wg errat v3/v4:** zadania B–G pakietu + badawcze H1–H4, konwencja kanoniczna apex-first [P₀,v₂,v₁,v₀], checkpointy E2 (errata v2) oraz wartości ρ wg erraty v4 jawnie w raporcie. Po zgodności zadania B: ✅-kandydat podwójnie.
3. **Raport:** format z pakietu (zadanie po zadaniu); każda liczba z atrybucją; rozbieg z checkpointem > 1e−5 względnie = STOP + diagnoza; wartości ujemne wyników nie obalają zlecenia, errata jest pełnowartościowym owocem (Z0).

## Materiały źródłowe (verbatim z repo, docs/replikacja/, commit 09086cca)

### 1. Pakiet (z banerem stanu errat v2–v4; tabela wierzchołków POPRAWIONA)

# Pakiet replikacji Z1 — sesja TAU-8: sieć węzłów o koordynacji ≤12

> Zlecenie szefa laboratorium (Vibe), wystawione 2026-11-06 wg delegacji Leszka. Protokół Z1/Z3: specyfikacja bez kodu, rachunek od zera, liczby jawnym tekstem, każda liczba z atrybucją (metoda, solver, residuum). Rozbieg z checkpointem > 1e−5 względnie = STOP + diagnoza (Z0); koncesje wprost. Rejestr sesji: [warsztat/tau-8-siec-12sasiadow.md](../warsztat/tau-8-siec-12sasiadow.md). Macierze ≤ 23×23 — wystarczy dowolny eigensolver z deklarowanymi residuami (lekcje solverowe §36.8: Krylov zalecany, Newton-polishing, p₂ = x²−2ax+|λ|²).

> **Stan errat (aktualizacja 2026-11-07, po incydencie replikacyjnym GPT):** ten plik obowiązuje łącznie z erratami [v2](tau-8-z1-pakiet-errata-v2.md) (konwencja kanoniczna apex-first [P₀,v₂,v₁,v₀], checkpointy B, pełna lista ścian), [v3](tau-8-z1-pakiet-errata-v3.md) (poprawka tabeli wierzchołków — E8, transpozycja 5↔8; tabela poniżej JEST już wersją poprawioną) i [v4](tau-8-z1-pakiet-errata-v4.md) (prawdziwe ρ = wartości macierzowe; ścieżka pierwiastków wielomianu nieważna do cyfr znaczących). Wersja sprzed errat zawierała tabelę przekręconą — kto czyta starszą kopię: permutacja etykiet względem niej = dokładnie swap(5,8).

## 1. Konstrukcja (konwencje jawne)

**Ikosaedr.** φ = (1+√5)/2. Wierzchołki 0–11 (etykietowanie istotne — porządek sweepu zależy od lex):

| i | v_i |
|---|---|
| 0 | (0, 1, φ) |
| 1 | (1, φ, 0) |
| 2 | (φ, 0, 1) |
| 3 | (0, 1, −φ) |
| 4 | (1, −φ, 0) |
| 5 | (−φ, 0, 1) |
| 6 | (0, −1, φ) |
| 7 | (−1, φ, 0) |
| 8 | (φ, 0, −1) |
| 9 | (0, −1, −φ) |
| 10 | (−1, −φ, 0) |
| 11 | (−φ, 0, −1) |

Krawędź: odległość² = 4 dokładnie. Ściany: wszystkie trójki {i < j < k} parami krawędziowe (20); indeksowanie f = 0..19 porządkiem leksykograficznym; F₀ = f₀ = {0,1,2}. Kontrola: 12 wierzchołków, 30 krawędzi, każdy wierzchołek w dokładnie 5 ścianach.

**Węzeł.** 13 punktów: wierzchołki 0–11 + P₀ = punkt 12. Każda ściana + P₀ = K₄ (20 K₄).

**Operator lokalny (na 4 punktach tetry).** M_local(i) = I₄ z wierszem i zastąpionym przez (¼, ¼, ¼, ¼) (include-self). Tetra o punktach w porządku aktualizacji [p0, p1, p2, p3]: R₄ = M(3)·M(2)·M(1)·M(0) (pierwszy stosowany najbardziej z prawej). Osadzenie E_t na 13/23 punktach: blok R₄ na punktach tetry, identyczność na reszcie.

**Runda węzła (wariant nat).** Tetry ścian f = 0..19; punkty tetry ściany f: [v₀, v₁, v₂, 12] (v₀ < v₁ < v₂ = posortowana ściana; **P₀ ostatnie**). Stosowanie w kolejności f rosnąco (t₀ pierwsza): R_node = E_t19 · … · E_t1 · E_t0. Runda = 80 taktów; det R_node = 256⁻²⁰ strukturalnie (80 czynników det ¼).

**Warianty węzła.** rev: ściany w kolejności malejącej (t19 pierwsza). p0first: punkty każdej tetry [12, v₀, v₁, v₂] (P₀ pierwsze), ściany lex. W obu 80 taktów.

**Bramki-porty.** Środki ścian (barycentrum, znormalizowane do 1): 10 par antypodalnych. Bramka = czwórka par = 8 środków będących wierzchołkami sześcianu; kryterium sześcianu: multizbiór 28 odległości² między 8 środkami = {12×(4/3), 12×(8/3), 4×4}. Bramek jest dokładnie 5 (przegląd C(10,4)); każda para antypodalna w dokładnie 2 bramkach; każda ściana w dokładnie 2 bramkach; w obrębie jednej bramki każdy wierzchołek ikosaedru w dokładnie 2 z jej 8 ścian. Graf dualny ścian (krawędzie = pary ścian dzielące krawędź): 3-regularny, średnica 5; odległości par ścian wewnątrz bramki: {12×2, 12×3, 4×5}, brak odległości 1. Sweep bramki: jej 8 tetr w kolejności lex (32 takty); bramki bez etykiet kanonicznych — raportować zbiór 5 wartości.

**Para węzłów.** 23 punkty: strona A = 0..12 (P₀ᴬ = 12); wspólna ściana F₀ = {0,1,2} (identyfikacja punktowa); strona B: bijekcja τ utrwalająca F₀ punktowo, wierzchołki A spoza F₀ rosnąco (3..11) → 13..21, P₀ᴬ → 22 (P₀ᴮ). Ściany B: obrazy τ(f), f = 0..19; tetra B: punkty τ(f) posortowane rosnąco, potem 22. Rundę pary = 160 taktów: R_AB = sweep A (20 tetr) potem sweep B (kolejność tetr jak w węźle); R_BA = odwrotnie (symbolu lustra: zamiana stron). R_Aonly = sweep samej strony A na 23 punktach. R_cut = R_AB bez tetry F₀ po obu stronach (pierwsza tetra każdej strony; 38 tetr, 152 takty).

**Grafy.** Graf węzła = unia 20 K₄; graf pary = unia 40 K₄ (krawędzie = wszystkie pary punktów wewnątrz tetry). Laplasjan L = D − A; raportować λ₂ (druga od dołu wartość własna).

**ℓ.** Lewy wektor Perrona: ℓᵀR = ℓᵀ, Σℓᵢ = 1 (metoda: iteracja transpozycji; residuum ℓᵀR − ℓᵀ jawnie).

## 2. Checkpointy (wartości oczekiwane z rejestru sesji; tolerancja 1e−5 względnie)

| Obiekt | Wielkość | Wartość |
|---|---|---|
| SERC R₄ | widmo | 1; 0.153348±0.074039i; 0.134711 (ρ = 0.170286) |
| SERC R₄ | ślad / det | 369/256 = 1.44140625 / 1/256 |
| Węzeł nat | ρ (runda) | 0.174759 |
| Węzeł nat | widmo dalej | 0.074450; 0.045163; para 0.032402±0.015344i; para 0.028504±0.026555i (poprawka wg erraty v2 E2 — pierwotne 0.074479; 0.043097 były chybne) |
| Węzeł nat | ker(R−I) | 1 |
| Węzeł nat | ℓ(P₀) / max wierzchołek / min wierzchołek | 0.037550 / 0.152520 / 0.044702 |
| Węzeł nat | entropia ℓ | 2.487 (ln 13 = 2.565) |
| Węzeł rev | ρ | 0.113515 |
| Węzeł p0first | ρ; ℓ(P₀) | 0.131328; 0.203979 (największa — wybraniec) |
| Bramki | liczba; pokrycie | 5; każdy wierzchołek dokładnie 2× na bramkę; ker(sweep bramki) = 1 |
| Bramki | zbiór ρ_gate (32 takty) | {0.268753, 0.271136, 0.287368, 0.298484, 0.328097} |
| Lemat jąder | wolne ker tetry / 190 par | 10 / N1 = 13−|S|: {100×6, 60×7, 30×8} |
| Para R_AB | ρ; widmo dalej | 0.554642; 0.113966; 0.075612; 0.073594±0.004121i |
| Para R_AB | ker; lustro widm R_BA | 1; rozjazd < 1e−13 |
| Para | ker(R_Aonly − I) | 11 |
| Para | ℓ: P₀ᴬ, P₀ᴮ, F₀ (suma), A-only (suma), B-only (suma) | 0.022750; 0.022750; 0.211738; 0.371381; 0.371381 |
| Para cut | ρ; ker | 0.550108; 1 |
| Laplasjan węzła | λ₂; λmax; stopnie | 3.763932 (= (5−√5)+1); 13; P₀: 12, wierzchołki: 6 |
| Laplasjan pary | λ₂; λmax; stopnie | 1.042823; 13.494094; F₀: 10, P₀ᴬ/P₀ᴮ: 12 |

## 3. Zadania raportowe

**A–G (weryfikacja checkpointów):** (A) SERC + residua wektorów własnych; (B) węzeł nat: widmo, ρ, τ = 1/(−ln ρ) (rundy), kontrakcja/takt ρ^(1/80), ker, ℓ (P₀, max, min, entropia) + warianty rev i p0first (ρ i ℓ(P₀)); (C) bramki: 5 sześcianów, pokrycia, zbiór ρ_gate, ker; (D) lemat jąder: wolne ker tetry = 10, wszystkie 190 par ścian N1 = 13−|S| (raport: zgody/rozjazdy), zbiór rozkładu; (E) para: ρ, widmo top-5, ker, lustro R_AB vs R_BA (widma + ℓ), ℓ-partycje; (F) cut: ρ_cut, ker; (G) Laplasjany obu grafów + stopnie.

**H (badawcze — bez checkpointów, status 🔍/💡):**
- **H1 — tryb kontrastu pary:** wektor własny subdominanty 0.554642 R_AB: struktura między stronami (suma składowych po stronie A vs po stronie B; hipoteza: antysymetryczny tryb kontrastu — sumy przeciwne).
- **H2 — symetria ℓ per punkt:** czy ℓ_AB(p) = ℓ_AB(τ(p)) dla każdego punktu strony A? (w sesji sprawdzono agregatowo: sumy 9-punktowe i P₀ identyczne; lustrzaność ℓ_BA = ℓ_AB∘τ potwierdzona do 2.8e−17).
- **H3 — przełącznik centrum przy rev:** czy w wariancie rev węzła P₀-ostatnie vs P₀-pierwsze nadal przełącza ℓ(P₀) z anty-wybrańca na wybrańca? Podać obie wartości.
- **H4 — det R_node:** zweryfikować det = 256⁻²⁰ = 1.71e−49 w wysokiej precyzji (w sesji LU double dało −110.9028 vs −110.9035 w log — sęk uwarunkowania; proszę o arytmetykę podwójnie-diadiczną/mpmath).

**Format raportu:** liczby jawnym tekstem do 6 miejsc dziesiętnych; każda liczba z atrybucją (konstrukcja, metoda, solver, residuum); niezgodność z checkpointem = STOP + diagnoza; własne erraty koncesyjnie wprost. Statusy wg Z1: zgodność niezależnego rachunku podnosi 🔍 → ✅-kandydat.

### 2. Errata v2 (konwencja kanoniczna, checkpointy E2, pełna lista ścian)

# Errata v2 — pakiet replikacji Z1, sesja TAU-8 (2026-11-06)

Wystawca: szef laboratorium (Vibe), po raportach replikacyjnych Claude'a, GPT i DeepSeeka. Obowiązuje wszystkie kopie pakietu v1 (commit a8033ac); erraty E4.1–E4.3 przyjęte od Claude'a i DeepSeeka (koncesja wprost, niezależne potwierdzenia). Metoda rozstrzygająca (bez eigensolvera): A = 256^20·R_node jako macierz CAŁKOWITA BigInt; q_k = Σ_{λ≠1} λ^k = tr(A^k)/2^{160k} − 1 dokładnie; Newton → wielomian charakterystyczny całkowity; pierwiastki Durand–Kerner na wielomianie deflatoanym (x−1); walidacja dwustronna q_k z pierwiastków = exact. Zgodność z checkpointem > 1e−5 względnie = STOP + diagnoza (bez zmian). Konstrukcja zweryfikowana trzema niezależnymi ścieżkami: iloczyn BigInt, bezpośrednia symulacja Gaussa–Seidela in-place na wektorach bazowych (zgodność trace i trace² do 1e−9), liczby sesyjne.

## E1. Konwencja kanoniczna węzła (KRYTYCZNA — errata opisu; liczby sesji bez zmian)

Pakiet v1 opisywał porządek w tetrze jako „P₀ ostatnie, wierzchołki rosnąco" [v₀,v₁,v₂,P₀]. **Błąd: konwencja sesji TAU-8 (Węzeł-0, kanoniczna) to apex-first [P₀, v₂, v₁, v₀]** — P₀ aktualizowane PIERWSZE w każdej tetrze, potem v₂, v₁, v₀. To jest konwencja korpusu (Estrada §36, A1b): blok tetry = W_nat/256, W_nat = [[64,64,64,64],[16,80,80,80],[20,36,100,100],[25,45,61,125]] (całkowite). Osadzenie w węźle (wiersz = punkt aktualizowany, kolumna = źródło; wiersze sumują się do 1):

- E[P₀][P₀] = E[P₀][v₂] = E[P₀][v₁] = E[P₀][v₀] = 64/256
- E[v₂][P₀] = 16/256;  E[v₂][v₂] = E[v₂][v₁] = E[v₂][v₀] = 80/256
- E[v₁][P₀] = 20/256;  E[v₁][v₂] = 36/256;  E[v₁][v₁] = E[v₁][v₀] = 100/256
- E[v₀][P₀] = 25/256;  E[v₀][v₂] = 45/256;  E[v₀][v₁] = 61/256;  E[v₀][v₀] = 125/256
- punkty poza tetrą: identyczność.

Runda = 20 bloków w kolejności ścian lex rosnąco (R_node = E_f19·…·E_f0; f₀ pierwsza), 80 taktów, det = 256^−20 strukturalnie.

**Ostrzeżenie diagnostyczne:** SERC (zadanie A, widmo bloku 4×4) NIE odróżnia porządków [v₀,v₁,v₂,P₀] i [P₀,v₂,v₁,v₀] — 256·R₄ wychodzi w obu przypadkach identyczne (zweryfikowane całkowitoliczbowo). Zadanie A przechodzi w obu konwencjach; rozbieżność ujawnia się dopiero w B (węzeł).

## E2. Checkpointy B — kanon apex-first (obowiązujące) + literał v1 (dla porównania)

| Wielkość | Kanon [P₀,v₂,v₁,v₀] | Literał v1 [v₀,v₁,v₂,P₀] |
|---|---|---|
| nat: ρ (runda) | **0.174759** (0.174758936, realny) | 0.066018 (para 0.055887±0.035143i) |
| nat: ślad R_node | **1.288968535** | 1.119630708 |
| rev: ρ | **0.113510** (para 0.106290±0.039835i) | 0.076956 (realny) |
| rev: ślad | **1.258423061** | 1.119264738 |
| p0first: ρ | **0.131327** (realny; porządek [v₂,v₁,v₀,P₀]) | 0.100517 (para; [P₀,v₀,v₁,v₂]) |
| p0first: ślad | **1.181491056** | 1.209042059 |

Widmo nat kanon dalej: 0.074450, 0.045163, para 0.032402±0.015344i, para 0.028504±0.026555i (errata drobna sesji: raportowano 0.074479 / 0.043097 — własny QR chybny na trybach małych).

Wielomiany charakterystyczne R_node (nat): kanon: λ¹³ − 1.288968535λ¹² + 0.311740102λ¹¹ − 0.023252074λ¹⁰ + 0.000478581λ⁹ + 1.926·10⁻⁶λ⁸ − 10⁻⁹λ⁷ (reszta ~0). Literał: λ¹³ − 1.119630708λ¹² + 0.124530859λ¹¹ − 0.004911818λ¹⁰ + 1.1176·10⁻⁵λ⁹ + 4.91·10⁻⁷λ⁸.

Liczby pośrednie q_k = Σ_{λ≠1}λ^k (dokładne; do weryfikacji pośredniej u replikanta):
- kanon nat: q₂ = 0.03795968, q₄ = 0.000966955, q₈ = 8.709504·10⁻⁷, q₁₆ = 7.568863·10⁻¹³
- literał nat: q₂ = 0.004511205, q₄ = −0.000020125, q₈ = −3.275886·10⁻¹⁰, q₁₆ = −1.621306·10⁻¹⁹
- kanon rev: q₂ = 0.022125808, q₄ = 0.000052180, q₈ = −5.304946·10⁻⁸, q₁₆ = 1.299428·10⁻¹⁵
- kanon p0first: q₂ = 0.018726536, q₄ = 0.000298900, q₈ = 8.848393·10⁻⁸

Pozostałe checkpointy pakietu v1 (ℓ węzła, entropia, bramki ρ_gate, para R_AB 0.554642, cut 0.550108, Laplasjany) — bez zmian; dotyczą kanonu apex-first.

## E3. Skan 24 permutacji porządku w tetrze (ściany lex asc) — nowe, 🔍

ρ z dokładnych q₈/q₁₂/q₁₆ („czyste" = zgodność estymatorów do 6 cyfr; „~" = beating ±2%; ✱ = pełny wielomian charakterystyczny):

[P₀,v₂,v₁,v₀] 0.174759 ✱; [P₀,v₁,v₀,v₂] 0.166167; [v₁,P₀,v₀,v₂] 0.168470; [v₁,v₀,P₀,v₂] 0.160886; [P₀,v₁,v₂,v₀] 0.159738; [v₂,P₀,v₁,v₀] 0.154099; [v₂,v₁,P₀,v₀] 0.143295; [v₁,v₂,P₀,v₀] 0.149664; [v₁,P₀,v₂,v₀] 0.163159; [v₁,v₂,v₀,P₀] 0.131996; [v₂,v₁,v₀,P₀] 0.131327 ✱; [v₂,P₀,v₀,v₁] 0.122693; [P₀,v₀,v₂,v₁] 0.106043; [v₀,v₁,P₀,v₂] ~0.101; [P₀,v₀,v₁,v₂] 0.100517 ✱; [v₀,P₀,v₂,v₁] 0.094702; [v₂,v₀,P₀,v₁] 0.093988; [v₂,v₀,v₁,P₀] 0.093239; [v₀,P₀,v₁,v₂] ~0.093; [P₀,v₂,v₀,v₁] 0.091884; [v₀,v₂,v₁,P₀] 0.086861; [v₀,v₂,P₀,v₁] 0.081921; [v₀,v₁,v₂,P₀] 0.066018 ✱.

Desc (wybrane): [v₀,v₂,v₁,P₀] 0.043291 (najszybszy); [v₀,v₁,v₂,P₀] 0.076956 ✱; [v₂,v₁,v₀,P₀] ~0.1015; [P₀,v₀,v₁,v₂] 0.117002; [P₀,v₂,v₁,v₀] 0.113510 ✱.

**Kolejność w tetrze rozpina ρ w zakresie 0.043–0.175 (×4) — najsilniejszy pojedynczy parametr tempa węzła.**

**PEŁNA lista 20 ścian sweepu w porządku lex (z generatora, kod autorytatywny):**
f0={0,1,2}, f1={0,1,7}, f2={0,2,6}, f3={0,5,6}, f4={0,5,7}, f5={1,2,8}, f6={1,3,7}, f7={1,3,8}, f8={2,4,6}, f9={2,4,8}, f10={3,7,11}, f11={3,8,9}, f12={3,9,11}, f13={4,6,10}, f14={4,8,9}, f15={4,9,10}, f16={5,6,10}, f17={5,7,11}, f18={5,10,11}, f19={9,10,11}.

**Errata erraty (2026-11-06, koncesja):** pierwsza wersja v2 podawała ręcznie wyprowadzone, BŁĘDNE pierwsze 5 ścian ({0,2,6},{0,6,8},{0,7,8} — {0,6,8} i {0,7,8} nie są ścianami; poprawne f3={0,5,6}, f4={0,5,7}). Kod i wszystkie liczby (trace, ρ, wielomiany, q_k) liczyły z właściwej listy — błąd dotyczył tylko prozy. Wszystkie wyliczenia zweryfikowane ponownie po korekcie: bez zmian.

## E4. Erraty przyjęte od Claude'a i DeepSeeka (2026-11-06)

1. det R_node = 256^−20 = 2^−160 = **6.842278·10⁻⁴⁹** (nie 1.71·10⁻⁴⁹ — błąd konwersji Vibe; log −110.9035 był poprawny). Potwierdzone potrójnie: Claude (mpmath/Fraction), DeepSeek (dowód strukturalny), Vibe (BigInt). H4 ✅.
2. Definicja N1 (doprecyzowanie, wg propozycji Claude'a i DeepSeeka): N1 = dim ker − 1 = 13 − |⋃S| (ker zakotwiczony, bez trybu stałego); wolny ker(E_b·E_a − I) = 14 − |⋃S| (7/8/9 dla par rozłącznych/wspólny wierzchołek/wspólna krawędź; 10 dla tetry). Liczności 100/60/30 bez zmian, dowód kombinatoryczny DeepSeeka.
3. Literówka „s ymbolu" — poprawiona.
4. Nowe zamknięcie DeepSeeka: λ₂ Laplasjanu węzła = 6−√5 = (5−√5)+1 udowodnione (graf = stożek nad ikosaedrem; L_node = {0, (6−√5)×3, 7×5, (6+√5)×3, 13}).

## E5. Instrukcja raportowa (dysambiguacja — ZAWSZE dołączyć)

Każdy raport Z1 ma zawierać: (a) pełną listę 20 ścian sweepu W WASZEJ enumeracji (surowy wydruk generatora, przed porównaniem z czegokolwiek); (b) ślad R_node (6+ cyfr); (c) wielomian charakterystyczny R_node. **Liczby jawnym tekstem, nie tabelą markdown (tabele giną w relayu).**

## E6. Status replikacji (2026-11-06, wieczór)

- **Claude:** statyka ✅-kandydat; H2 ✅-kandydat; H4 ✅. Dynamika 🔍: nat/rev/p0first = 0.085888/0.060854/0.118651 — poza rodziną 24 permutacji (E3). Czeka na E5(a–c).
- **GPT (Asterion), przebieg wg v2:** geometria PASS, ale kanon daje ślad 1.272126070 / ρ 0.165561571, a literał ślad 1.163642560 / ρ 0.085888387 — OBA poza moją rodziną. **Kluczowe: jego literał = 0.085888 = nat Claude'a** — dwa niezależne modele, wspólna konstrukcja. Jego „potwierdzenie" listy ścian prawdopodobnie echo (wartości oczekiwane przekazano w tym samym komunikacie — patrz E7). Diagnoza w toku: fingerprinty krokowe tr(R_k), k = 1,2,3,5,20 (żądane od obu modeli, porównanie po stronie Vibe).
- **DeepSeek:** warstwa symboliczna domknięta (S1–S6 ✅-kandydaci, w tym λ₂ = 6−√5 z dowodem); warstwa numeryczna Z0-STOP uczciwy.

## E7. Lekcja protokołu (nowa, z dekady awarii B)

**Żądanie fingerprintu nie może zawierać wartości oczekiwanej w tym samym przekazie.** Jeśli replikant dostanie oczekiwaną odpowiedź razem z pytaniem, potwierdza echo zamiast liczyć (zaobserwowane: „enumeracja zgadza się z erratą" przy liście, która okazała się błędna u pytającego). Tryb poprawny: żądać niezależnego wyniku (surowy wydruk), porównywać po otrzymaniu, rozbieżność rozstrzygać liczonymi pośrednimi (tr(R_k), q_k, wielomian) — każda zlokalizowana rozbieżność zaczyna się od pierwszego kroku, w którym ślady się rozjeżdżają.

### 3. Errata v3 (poprawka tabeli wierzchołków, E8)

# Errata v3 — pakiet replikacji Z1, sesja TAU-8 (2026-11-06, późny wieczór)

Wystawca: szef laboratorium (Vibe). Domyka dekadę awarii zadania B: **przyczyna znaleziona po stronie pakietu, nie replikantów. Koncesja wprost: tabela wierzchołków w pakiecie v1 była przekręcona względem kodu sesji (transpozycja 5↔8), a moje wcześniejsze podejrzenie echo u Claude'a/GPT było błędne — wycofuję.**

## E8. Tabela wierzchołków: transpozycja 5↔8 (błąd transkrypcji pakietu v1; KRYTYCZNA)

Pakiet v1 podawał: v₅ = (φ, 0, −1), v₈ = (−φ, 0, 1). Kod sesji TAU-8 (autorytatywny; z niego pochodzą WSZYSTKIE checkpointy rejestru) używa: **v₅ = (−φ, 0, 1), v₈ = (φ, 0, −1)**. Poprawna tabela (obowiązuje od teraz):

| i | v_i | i | v_i |
|---|---|---|---|
| 0 | (0, 1, φ) | 6 | (0, −1, φ) |
| 1 | (1, φ, 0) | 7 | (−1, φ, 0) |
| 2 | (φ, 0, 1) | 8 | **(φ, 0, −1)** |
| 3 | (0, 1, −φ) | 9 | (0, −1, −φ) |
| 4 | (1, −φ, 0) | 10 | (−1, −φ, 0) |
| 5 | **(−φ, 0, 1)** | 11 | (−φ, 0, −1) |

Wszystkie checkpointy (E2: nat 0.174759/1.288968535, rev, p0first, bramki, para, cut, Laplasjany, ℓ) liczone były z tabeli poprawnej. Lista ścian E3 z erraty v2 (f0={0,1,2}, f1={0,1,7}, f2={0,2,6}, f3={0,5,6}, f4={0,5,7}, … f19={9,10,11}) jest listą tabeli poprawnej — spójna.

## E8a. Co policzyli Claude i GPT — i dlaczego było poprawnie

Claude i GPT zaimplementowali tabelę v1 wiernie. W etykietowaniu v1 lista ścian lex to: {0,1,2},{0,1,7},{0,2,6},{0,6,8},{0,7,8},{1,2,5},{1,3,5},{1,3,7},{2,4,5},{2,4,6},{3,5,9},{3,7,11},{3,9,11},{4,5,9},{4,6,10},{4,9,10},{6,8,10},{7,8,11},{8,10,11},{9,10,11} — pierwsze pięć {0,1,2},{0,1,7},{0,2,6},{0,6,8},{0,7,8} to dokładnie raport E5(a) Claude'a. **To nie było echo — to był niezależny, poprawny rachunek wg tabeli v1.** (Mój ręczny szkic ścian w pierwszej wersji erraty v2 odpowiadał tabeli v1 — liczyłem z tabeli jak wypisana; kod sesji używa zamienionej. Dlatego moja „korekta" do f3={0,5,6}, f4={0,5,7} była poprawna dla kodu, ale błędnie przedstawiona jako poprawka listy Claude'a.)

Vibe policzył obiekt v1 dokładnie (te same metody BigInt co w E2). Zgodność z raportami Claude'a/GPT — co do cyfry:
- kanon apex-first [P₀,v₂,v₁,v₀]: ślad 1.272126070 (= Claude E5(b), = GPT v2); wielomian λ¹³ − 1.272126070λ¹² + 0.291963787λ¹¹ − 0.020175455λ¹⁰ + 3.33523·10⁻⁴λ⁹ + 4.20930·10⁻⁶λ⁸ + 4.74·10⁻⁹λ⁷ — identyczny z Claude'em (mpmath, 40 cyfr) i GPT (numpy.poly);
- literał v1 [v₀,v₁,v₂,P₀]: ślad 1.163642560; wielomian λ¹³ − 1.163642560λ¹² + 0.172135639λ¹¹ − 0.008536373λ¹⁰ + 4.26477·10⁻⁵λ⁹ + 6.46933·10⁻⁷λ⁸ − 3.78·10⁻¹¹λ⁷ — identyczny;
- q_k (GPT, jawnym tekstem): kanon q₂ = 0.0343771620 ✓ (Vibe exact 0.034377162), q₄ = 0.000779203691 ✓ (0.000779204); literał q₂ = 0.00979273018 ✓ (0.0097927302), q₄ = −0.0000174402643 ✓ (−0.0000174403).

**Wniosek: konstrukcje Claude'a i GPT tożsame z dokładnym rachunkiem Vibe obiektu v1. Ich STOP w B był decyzją prawidłową wg Z1 — rozbieżność leżała w specyfikacji. Z0 potwierdzone: błąd po stronie wystawcy pakietu (transkrypcja tabeli), zlokalizowany trzecim niezależnym rachunkiem.**

## E8b. Widmo obiektu v1 (Vibe, exact BigInt; test domknięcia Σλᵏ vs exact q_k: k=2 → 5·10⁻¹⁵, k=4 → 7·10⁻¹²)

| Wariant | ślad R_node | ρ | struktura ρ | q₂ | q₄ | q₈ |
|---|---|---|---|---|---|---|
| kanon apex-first | 1.272126070 | 0.165561507 | realny | 0.034377162 | 0.000779204 | 5.6509·10⁻⁷ |
| literał v1 | 1.163642560 | 0.085868381 | para 0.077942229 ± 0.036033147i | 0.0097927302 | −0.0000174403 | −5.617·10⁻⁹ |
| literał rev | 1.125524004 | 0.062718334 | para 0.061889955 ± 0.010159866i | 0.0072410786 | 0.0000215638 | 8.7301·10⁻¹¹ |
| p0first v1 [P₀,v₀,v₁,v₂] | 1.254743374 | 0.118650582 | para 0.106488099 ± 0.052328247i | 0.019927005 | −0.0000935373 | −6.8426·10⁻⁸ |

Dalsze widmo kanonu: 0.070316591 (realny), para 0.046555928 ± 0.012255588i. Dalsze widmo literału: para 0.038233157 ± 0.013579702i (mod 0.040573175).

Rozjazdki z raportowanymi ρ (Claude runda 1: nat 0.085888, rev 0.060854, p0first 0.118651; E5: 0.165562/0.085888; GPT v2: 0.165561571/0.085888387): kanon +6.4·10⁻⁸, literał +2.3·10⁻⁴, rev −3.0·10⁻², p0first −4·10⁻⁷ (zgodne). Wzór spójny z niedokonwergowaną iteracją potęgową: bias ≈ (λ₃/λ₂)^k przy wspólnym k≈11–12 (ratio 0.42/0.47/0.74 dla p0first/nat/rev). **Prośba (atrybucja Z1, bez wartości oczekiwanych): metoda, solver, liczba iteracji i residuum, którym szacowaliście ρ.** To nie jest zarzut — atrybucja jest obowiązkowa dla każdej liczby od początku Z1.

## E9. Lekcje protokołu (nr 2 z dekady awarii B)

1. **Tabelę geometrii generuje się z kodu, nie przepisuje ręcznie.** Transpozycja 5↔8 przeszła przez pisemną „kontrolę" i wygenerowała dekadę diagnoz u trzech modeli. Fingerprint E5(a) (lista ścian) to właściwy test — ale porównanie PO otrzymaniu niezależnego wyniku (E7 bez zmian), a przy zgodności list nie wolno wnioskować o zgodności geometrii, dopóki tabela współrzędnych nie jest przypięta.
2. **Podejrzenie echo wymaga dowodu, nie wzorca.** Claude raportował {0,6,8},{0,7,8} jako własne ściany; uznałem to za echo mojego szkicu. To był jego poprawny rachunek; „zbieżność" ze szkicem wynikała stąd, że oba (mój szkic ręczny, jego generator) wiernie stosowały tabelę v1.
3. **Iteracyjne estymatory ρ raportują kryterium zbieżności** (bias (λ₃/λ₂)^k). Tani i rozstrzygający walidator: test domknięcia Σλᵏ vs exact q_k ze śladów potęg BigInt — stosować przed publikacją ρ.

## Instrukcja dla replikantów (B–H wg tabeli poprawnej)

Przebieg wg poprawnej tabeli E8 (= kod sesji), konwencje jak w erracie v2 (E1: apex-first kanon; sweep ścian lex rosnąco). Oczekiwane: kanon nat ślad 1.288968535, ρ 0.174758936; rev ślad 1.258423061, ρ 0.113510; p0first [v₂,v₁,v₀,P₀] ślad 1.181491056, ρ 0.131327; pierwsze 5 ścian {0,1,2},{0,1,7},{0,2,6},{0,5,6},{0,5,7} (pełna lista w erracie v2 E3). Dalej checkpointy C–H pakietu v1 bez zmian (bramki {0.268753, 0.271136, 0.287368, 0.298484, 0.328097}; para 0.554642; cut 0.550108; Laplasjany 3.763932 / 1.042823). Po zgodnym przebiegu: B ✅-kandydat podwójnie, C–H do domknięcia.

Claude: prośba z E5 o liczbę po pierwszej tetrze ({0,1,2}+P₀) jest w tym świetle bezużyteczna — pierwsza tetra jest niezależna od transpozycji (Wasz wynik = mój = blok 256·R₄ z W_nat; rozbieżność zaczyna się od czwartej ściany sweepu). Zamiast niej: pełny przebieg wg E8.

### 4. Errata v4 (wartości ρ macierzowe; obowiązuje nad wartościami v2/v3)

# TAU-8 Z1 pakiet — errata v4: rozstrzygnięcie sporu ρ (koncesja pełna)

**2026-11-06, warsztat Vibe (szef laboratorium).** Erraty v2/v3 opublikowały wartości ρ jako „exact" z pipeline'u: ślady potęg (BigInt, dokładne) → wielomian charakterystyczny (Newton, dokładny) → pierwiastki (Durand–Kerner/Newton na współczynnikach zaokrąglonych do 53 bitów). Ścieżka śladów, q_k, współczynniki wielomianów i det STOJĄ (potwierdzone niezależnie). **Ścieżka pierwiastkowa jest dla tego widma katastrofalnie źle uwarunkowana i dała wartości obarczone błędem do 2·10⁻⁵.** Prawdziwe ρ to wartości macierzowe: LAPACK/mpmath Claude'a, numpy GPT oraz dwa niezależne rachunki Vibe. **Koncesja pełna: liczby Claude'a i GPT były poprawne; „poprawki exact" errat v2/v3 chybione. Zadanie B domknięte.**

## 1. Pomiary rozstrzygające (Vibe, sesja TAU-8, 2026-11-06)

1. **Identyczność obiektów.** Macierz iloczynu float64 (20 bloków, pełny akumulacja) i macierz exact (BigInt) po zaokrągleniu wpisów do 53 bitów: max |różnica wpisu| = 5.6·10⁻¹⁷ (4 obiekty). Ślady: exact vs float zgodne co do 16 cyfr (1.2889685345212; 1.163642560270783; 1.258423060938833; 1.272126069591923). Potęgi śladów (fingerprinty): tr(R²) = 1.037959679, tr(R⁵) = 1.000165444, tr(R²⁰) = 1.000000000 — exact = float co do 9 cyfr. To ten sam obiekt na wszystkich poziomach.
2. **λ macierzy exact** (inwersja zespolona z pełnym pivotowaniem + dwustronny Rayleigh; deflacja pierwiastka 1): tabela w §3. Wszystkie wartości = LAPACK Claude'a / numpy GPT co do drukowanych cyfr.
3. **Empiryczne κ(λ)** (perturbacja 1·10⁻¹⁰ → pomiar przesunięcia λ): v3 kanon 0.3; v3 rev 6.8; v1 literał 2.0; v1 kanon 0.03. Ścieżka macierzowa dobrze uwarunkowana ⇒ λ z LAPACK/eigvals dokładne do ~10⁻¹⁵.
4. **Podłoga szumu ewaluacji wielomianu.** Szum absolutny na dużych współczynnikach dominuje: Σ|c_m·λ^m|·2⁻⁵³ ≈ 1.3·10⁻¹⁶, nie |P(λ)|·2⁻⁵³ ≈ 10⁻²⁷. Argument E8b „P(λ_Claude) = 2.9·10⁻¹⁷ vs szum 10⁻²⁷ (10¹⁰ nad podłogą)" był chybiony o 11 rzędów: 2.9·10⁻¹⁷ leży PONIŻEJ podłogi ⇒ nie było dowodu przeciw λ Claude'a. Wycofane.

## 2. Mechanizm (dlaczego „exact" był gorszy niż LAPACK)

- **Kondycjonowanie pierwiastków wielomianu vs wartości własnych macierzy** (klasyczne zjawisko Wilkinsona): κ_poly(pary literału v1) = Σ|c_m·λ^m|/|P′(λ)| ~ 3·10¹⁰. Zaokrąglenie współczynników do 53 bitów (decNum przed DK/Newtonem) przesuwa pierwiastki o ~2·10⁻⁵; iteracje dodatkowo zatrzymują się na poziomie 10⁻⁹ (kanon v3). Dla kanonu v3 κ_poly ≈ 6 — tam błąd 10⁻⁹ pochodzi z niedomknięcia iteracji, nie z zaokrąglenia.
- **Domknięcia Σλᵏ vs q_k (E8b) są nieważne wobec tej klasy błędu**: pierwiastki zaokrąglonego wielomianu automatycznie spełniają zaokrąglone momenty (~10⁻¹⁵) — kontrola dzieli ścieżkę zaokrąglenia z produkcją (samoreferencja). Test domknięcia chroni przed błędem SOLVERA pierwiastków, nie przed błędem REPRESENTACJI wielomianu.
- **Hipoteza „niedokonwergowana iteracja potęgowa" z E8b wycofana**: Claude nie używa iteracji potęgowej (LAPACK eigvals: Hessenberg + QR; kontrola mpmath Faddeev–Leverrier + polyroots).
- **Drobna rozbieżność Claude'a 0.085888 (LAPACK) vs 0.085890 (mpmath polyroots) wyjaśniona**: polyroots działa na wielomianie = ta sama słabo uwarunkowana ścieżka (błąd 2·10⁻⁶); LAPACK = ścieżka macierzowa (dokładna). Prawdziwa wartość: 0.0858884.

## 3. Tabela prawdziwych wartości (checkpointy v4; dokładność macierzowa ~10⁻¹²)

Ślady, q_k, wielomiany i det: exact BigInt — bez zmian. ρ: wartości macierzowe.

| Obiekt | Ślad R (exact) | ρ opublikowane v2/v3 (BŁĘDNE) | ρ PRAWDZIWE | Potwierdzenie |
|---|---|---|---|---|
| v3 kanon apex-first [P₀,v₂,v₁,v₀] | 1.288968535 | 0.174758936 | **0.174758932** | Claude LAPACK 0.174758932 ✓, mpmath 0.174758933 ✓, Vibe macierz ×2 ✓ |
| v3 rev | 1.258423061 | 0.113509600 | **0.113514662** = \|0.106293762 ± 0.039839861i\| | Claude 0.113514/0.113515 ✓; sesja 0.113515 ✓; Vibe ✓ |
| v3 p0first [v₂,v₁,v₀,P₀] | 1.165182204 | 0.131327191 | **0.131327883** | Claude 0.131328 ✓; Vibe ✓ |
| v1 kanon apex-first | 1.272126070 | 0.165561507 | **0.165561571** | GPT 0.165561571 ✓ (co do cyfry); Vibe ✓ |
| v1 literał [v₀,v₁,v₂,P₀] | 1.163642560 | 0.085868381 | **0.085888387** = \|0.077960923 ± 0.036040387i\| | GPT 0.085888387 ✓ (co do cyfry); Claude 0.085888 ✓; Vibe ✓ |
| v1 literał rev | 1.125524004 | 0.062718334 | **0.060853926** = \|0.060006612 ± 0.010119629i\| | Claude/GPT 0.060854 ✓; Vibe ✓ |
| v1 p0first [P₀,v₀,v₁,v₂] | 1.254743374 | 0.118650582 | **0.118651078** | Claude/GPT 0.118651 ✓; Vibe ✓ |

Komponenty par zespolonych z E8b (0.077942±0.036033i; 0.106290±0.039835i; 0.061890±0.010160i; 0.106488±0.052328i) — wycofane; poprawne w tabeli. q₂/q₄/q₈/q₁₆ z E8b — exact, stoją (ścieżka śladów).

**Sesja-oryginalne wartości 6-cyfrowe potwierdzone**: 0.174759 ✓; 0.113515 ✓ (errata v2 błędnie „poprawiła" ją na 0.113510 — rekonstrukcja); 0.118651 ✓; p0first węzła: prawda 0.131327883, sześciocyfrowo 0.131328 (sesyjne 0.131327 — różnica 1 ulp szóstego miejsca, replikacja Claude'a 0.131328 ✓).

## 4. Skan 24 permutacji — powtórzony metodą macierzową (moje etykietowanie v3)

Maksimum: **apex-first [P₀,v₂,v₁,v₀], ρ = 0.174758932** (rank 1/24); dalej: 0.168472, 0.166173, 0.163160, 0.160886, 0.159748. Wniosek E3 (zakres ρ ~×4, maksimum apex-first) POTWIERDZONY; wartości liczbowe skanu E3 obarczone błędem ścieżki pierwiastkowej do ~2·10⁻⁵ (np. E3: 0.166167 → prawda 0.166173).

## 5. Statusy po erracie v4

- **B: ✅-kandydat** (Claude LAPACK + mpmath; Vibe macierzowo ×2 [iloczyn float + entry-rounded exact]; sesja 6-cyfrowo; GPT: przebieg wg v3/v4 oczekiwany).
- **A, C–G, H4: ✅-kandydat** (Claude: wszystkie checkpointy zgodne; H4 det = 256⁻²⁰ = 6.842278·10⁻⁴⁹ potrójnie).
- **H2, H3: ✅-kandydat** (Claude: lustro ℓ per punkt max 1.4·10⁻¹⁷; przełącznik centrum z liczbami: rev ℓ(P₀) = 0.018315, p0first-rev 0.091528 na 4/13).
- **H1: 🔍** (jakościowo: znaki stron przeciwne, moduły nierówne — wektor Claude'a: A-only −7.886, B-only +5.873, F₀ +1.322, P₀ᴬ −0.852, P₀ᴮ +0.634 — nie czysta antysymetria).
- **Warstwa symboliczna DeepSeeka nietknięta** (kwartyk λ⁴−28λ³+258λ²−864λ+651, λ₂ węzła 6−√5, λ₂ pary 1.042823, lemat jąder — niezależne od ścieżki pierwiastków ρ).

## 6. Lekcje protokołu (E12 → rejestr)

1. **„Exact" dotyczy śladów, q_k, współczynników i det. ρ liczyć z macierzy** (eigvals / inversja + Rayleigh na obiekcie entry-rounded-exact), z empirycznym κ(λ) przy raporcie; pierwiastki wielomianu charakterystycznego traktować jako walidację strukturalną, nie źródło cyfr znaczących.
2. **Domknięcie współdzielące ścieżkę obliczeń z produkcją nie jest kontrolą** (Σλᵋ vs q_k chroni tylko przed błędem solvera, nie reprezentacji).
3. **Podłoga szumu ewaluacji wielomianu = Σ|c_m·λ^m|·ε** (szum absolutny na dużych współczynnikach), nie ε·|P(λ)|.
4. **κ mierzyć empirycznie zanim oskarży się solver drugiej strony**; własny „dokładny" pipeline wymaga niezależnego walidatora na tym samym obiekcie.
5. **Przed publikacją „poprawki" liczby drugiej strony: odtworzyć jej wartość DWIEMA niezależnymi u siebie ścieżkami** (tu: macierzowo — spór by się nie zdarzył; koszt rozstrzygnięcia: jedna noc i trzy tury relayu).

## 7. Prośby

- **GPT**: przebieg wg tabeli poprawnej (errata v3) nadal oczekiwany; jego q₂ = 0.0343771620 / q₄ = 0.000779204 (kanon) i q₂ = 0.0097927302 / q₄ = −0.0000174403 (literał) potwierdzone exact; jego ρ 0.165561571 / 0.085888387 potwierdzone jako PRAWDZIWE.
- **Claude**: potwierdzenie erraty v4 (jedno zdanie + statusy); kwartyk λ₂ pary do numerycznej kontroli (eigvalsh 23×23 vs λ⁴−28λ³+258λ²−864λ+651) pozostaje w kolejce.
- **DeepSeek**: errata v4 (odczyt); jego warstwa symboliczna bez zmian.

---
*Errata v4 zastępuje linie „exact ρ" errat v2/v3 (E2, E8b, skan E3). Wszystko poza ρ (konwencje, tabele geometryczne, ślady, q_k, wielomiany, det, Laplasjany, lemat) bez zmian.*

