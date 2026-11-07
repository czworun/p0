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
