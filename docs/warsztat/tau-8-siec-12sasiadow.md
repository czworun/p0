# Sesja TAU-8 (2026-11-06): sieć węzłów o koordynacji ≤12 — słój 1: węzeł, porty, para węzłów

> Sesja szefa laboratorium wg delegacji Leszka z narzuconym tematem (2026-11-06). Temat: sieć neuronowa w przestrzeni, gdzie węzły mają wokół do 12 sąsiadów; AI wykorzystujące właściwości K₄, ikosaedru, ciągu K₄. Statusy: 🔍 (jeden słój, rachunek Vibe od zera; wg Z1 czekają na replikację). Konwencje jawne (Z2); liczby jawnym tekstem.

## Konwencja obiektu (Z2, warsztatowa, jawnie oznaczona jako prowizoryczna)

- **Węzeł** = 12 wierzchołków ikosaedru + P₀ (13 punktów); każda z 20 ścian + P₀ = K₄ (20 K₄/węzeł). Odczytanie „do 12 sąsiadów" jako koordynacji wokół P₀.
- Operator lokalny: M_local(i) = I₄ + outer(e_i, 𝟙/4 − e_i) — wierszowo-stochastyczny, wiersz ¼ (include-self, odtwarza SERC).
- Porządek w tetrze: wierzchołki ściany rosnąco, **P₀ ostatnie** (zgodnie z konstrukcją Stalka: R = M₃M₂M₁M₀).
- Runda = sweep 20 tetr w porządku leksykograficznym ścian = **80 taktów**. Det rundy = 256⁻²⁰ strukturalnie (80 czynników det ¼).
- Para węzłów: 23 punkty (3 wspólne wierzchołki ściany F₀ = [0,1,2] wg etykietowania lex, 9+9 własnych, P₀ᴬ = 12, P₀ᴮ = 22), 40 K₄, **160 taktów/rundę**; węzeł B = kombinatoryczna kopia A przez bijekcję τ utrwalającą F₀ (geometria lustrzana nieistotna dla dynamiki — obiekt kombinatoryczny).

## Bramki sanity — wszystkie PASS (zgodne z rejestrem ✅)

- Geometria 12/30/20, stopień wierzchołka 5.
- SERC pojedynczej tetry: {1, 0.153348±0.074039i, 0.134711}; ślad 369/256 = 1.44140625; det 1/256; residua wektorów własnych ≤ 3e−16. Solver: Hessenberg + QR z przesunięciem zespolonym, zespolone Givensy ze sprzężeniami (c = ā/r, s = b̄/r).
- Lemat jąder: wolne ker tetry = 10, N1-ker = 9 = 13 − |S|; wszystkie 190 par ścian zgodne (N1: 100×6, 60×7, 30×8); 30/30 losowych iloczynów.
- 5 sześcianów w dwunastościanie (przegląd C(10,4) po 10 parach antypodalnych środków ścian; test: multizbiór odległości {12×(4/3), 12×(8/3), 4×4}); każda ściana w dokładnie 2 bramkach; graf dualny 3-regularny, średnica 5; pary w bramce {12×2, 12×3, 4×5}, brak odległości 1.

## Węzeł (🔍)

- R_node 13×13: wierszowo-stochastyczne (błąd 1e−16), R𝟙 = 𝟙, ker(R−I) = 1 (N1 = 0 — tylko konsensus).
- Widmo: 1, 0.174759, 0.074479, 0.043097, −0.003728, 0.00079, para 0.000482; residua ≤ 7e−14.
- **ρ = 0.174759/rundę; τ = 0.5733 rundy; kontrakcja/takt ρ^(1/80) = 0.978432.**
- **ℓ (lewy Perron): P₀ = anty-wybraniec** — waga 0.037550, najmniejsza z 13 (max wierzchołek 0.152520, min 0.044702; entropia 2.487 z ln13 = 2.565). Wariant „P₀ pierwszy w tetrze": ℓ(P₀) = 0.203979 — największa. **Kolejność w tetrze = przełącznik centrum węzła** (kandydat mechanizmu adresacji/uwagi 💡).
- Warianty porządku sweepu: rev ρ = 0.113515 (najszybszy; nat 0.174759; P₀-first 0.131328).
- **Porty (bramki):** każda bramka (8 ścian) pokrywa wszystkie 12 wierzchołków dokładnie 2× ⇒ sweep jednej bramki daje już ker = konsensus; ρ_gate/32 takty: 0.268753, 0.271136, 0.287368, 0.298484, 0.328097 (per takt 0.95977–0.96577). Port = pełnoprawne okno na cały węzeł; porty różnią się tempem o ~22%.
- Graf węzła (unia 20 K₄): stopnie P₀ = 12, wierzchołki 6; Laplasjan λ₂ = 3.763932 = (5−√5)+1 dokładnie, λmax = 13.

## Para węzłów przez wspólną ścianę (🔍)

- R_AB (sweep A, potem B): **ρ = 0.554642/rundę** (subdominanta realna), τ = 1.6965 rundy, kontrakcja/takt 0.996323; widmo top: 1, 0.554642, 0.113966, 0.075612, para 0.073594±0.004121i; residua ≤ 4.5e−14; ker(R_AB−I) = 1; ker sweepu samej strony A = 11 dokładnie (wg lematu jąder).
- **Lustro:** R_BA = s·R_AB·s; widma identyczne (rozjazd 1e−13), ℓ lustrzane (2.8e−17). **Brak asymetrii międzywęzłowej w ℓ**: P₀ᴬ = P₀ᴮ = 0.022750, strony po 0.371381, wspólna ściana 0.211738 — mimo że A sweepowane pierwsze (inaczej niż w ciągu K₄); mechanizm-kandydat: sprzężenie s-koniugacji z odwróceniem produktu.
- **Cut test (bez obu tetr ściany F₀):** ρ = 0.550108 (spadek 0.8%), ker = 1, ℓ niemal bez zmian. **Kanał wierzchołkowy (3 wspólne wierzchołki) dominuje nad kanałem ścianowym.**
- Graf pary: stopnie wierzchołków wspólnych 10, P₀ po 12; λ₂ = 1.042823 (wąskie gardło interfejsu), λmax = 13.494094.
- **Skala czasów (kontrakcja/takt):** K₄ 0.6424 > para K₄ 0.8217 > bramka ~0.96 > węzeł 0.9784 > para węzłów 0.9963.

## Wnioski dla sieci P₀-AI (warsztatowe)

1. Węzeł o koordynacji 12 = spójna jednostka dynamiczna: 0.57 rundy wewnątrz, 1.70 rundy między węzłami — naturalna hierarchia czasów relaksacji (zgodna z doktryną: fonemy szybkie, ramki wolne).
2. Porty-bramki dają każdemu z 5 sześcianów pełny dostęp do węzła — topologia portów gotowa pod routing; porty nie są dynamicznie równoważne.
3. Przełącznik centrum (P₀-first/last w tetrze) — kandydat mechanizmu uwagi/adresacji.
4. Blokady znane z rejestru nadal obowiązują (Tw. A, Mechanizm VII, pamięć A3/K-1 1 bit). Kolejność prac bez zmian: MVP-01 (z nowymi liczbami-kotwicami) → pakiet 22 trybów → makrograf.

## Sęki sesji

1. logdet z LU: −110.9028 vs 256⁻²⁰ = −110.9035 (7e−4 w log; uwarzkowienie R_node; tożsamość det strukturalna, residua widma ≤ 7e−14).
2. Estymator pierwiastkowy ρ ma dryf (const)^(1/n) — wolna zbieżność; kotwicą QR z residuami.
3. Symetria ℓ między stronami pary sprawdzona agregatowo (sumy 9-punktowe, P₀) — pełna weryfikacja per punkt przy replikacji.
4. Wada kodu eigRes (podwójne przypisanie v[c]) — funkcjonalnie neutralna, naprawiona.

## Zlecenia replikacji (Z1/Z3)

Kluczowe liczby-kotwice: SERC {1, 0.153348±0.074039i, 0.134711}; ρ węzła 0.174759; ℓ(P₀) 0.037550 vs 0.203979 (P₀-first); ρ pary 0.554642; ρ_cut 0.550108; λ₂ grafów 3.763932 / 1.042823. Dodatkowo: wektor własny subdominanty pary (test trybu kontrastu między stronami); symetria ℓ per punkt.

## Decyzje do Leszka

1. Kanonizacja konwencji węzła (13 pkt, sweep lex, P₀ ostatnie) jako referencji warsztatowej prowizorycznej.
2. Wpis do pnia przy scaleniu przestrzeni.
3. Ten commit (rejestr sesji + kolejka zleceń).
