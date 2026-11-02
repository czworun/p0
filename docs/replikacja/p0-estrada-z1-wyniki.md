# P₀–Estrada §36 — nieskończoności przestrzeni emergentnej: wyniki i rejestr replikacji (zrzut 2026-11-02)

**Pytanie (Leszek):** gdzie w przestrzeni emergentnej protokołu SERC (wieczny ruch konfiguracji na sferze V_cyc, §35.5 filara) siedzą „nieskończoności"? Hipoteza robocza: na środkach krawędzi K₄.

**Status:** T1–T4 ✅ — formalnie przyjęte 2026-11-02, po czterech replikantach (trzy pełne rachunki numeryczne A–H + potwierdzenie symboliczne i dowód analityczny). Pełna specyfikacja bramek i konwencji: [p0-estrada-z1-pakiet.md](p0-estrada-z1-pakiet.md). Jak wykonywać replikację: [docs/replikacja.md](../replikacja.md).

## Tezy i wyniki

- **T1 ✅ — stella octangula.** Izolowane „nieskończoności" dyskryminantu relacyjnego Δ (pełny iloczyn Vandermonde'a po 6 parach współrzędnych) to 14 punktów: 6 środków krawędzi (bieguny rzędu 2), 8 punktów ±wierzchołkowych (bieguny rzędu 3 — głębsze), punkty ogólne ścian (rząd 1). Formuły kanoniczne dokładne: m̂_01 = (1, 1, −1, −1)/2; trzy osie osmiościanu ortogonalne; pary antypodalne m̂_01 = −m̂_23 itd. Rzędy: twierdzenie analityczne (zliczanie znikających czynników Vandermonde'a — w m̂_ij dokładnie 2, w v̂_i dokładnie 3, na ścianie ogólnej dokładnie 1) + trzy niezależne fity numeryczne (regresja log-|Δ|, kierunki LCG seed 42: 2.000 / 3.000 / 1.000). Hipoteza środków częściowo potwierdzona: środki są biegunami, ale płytszymi niż wierzchołki.
- **Twierdzenie o maksimum Δ (✅-kandydat, rekomendacja ✅):** max |Δ| na sferze V_cyc = 1/(6√3) = 0.096225044865 dokładnie, osiągnięte na orbicie S₄ punktu o składnikach ∝ (1, r, −r, −1) z r = √(5−2√6) ≈ 0.317837245 (warunek krytyczny r⁴ − 10r² + 1 = 0). Dowód analityczny (Vibe) + trzy niezależne numeryki (Vibe, Asterion, Claude — Nelder–Mead 400 startów), zgodność 15 cyfr. Punkt arytmetyczny (3,1,−1,−3)/√20 daje |Δ| = 0.096 — prawie-arytmetyczność argmaxu to złudzenie okrągłych liczb.
- **T2 ✅ — biegun przepływu nie na środkach.** Wektor własny B4 dla λ_r = 0.134710644695: |komponenty| 0.7116, 0.6090, 0.1911, 0.2936 (znaki naprzemienne); najbliższe środki: 25.49° (pary przekątne (0,2),(1,3)); kąt do płaszczyzny E pary zespolonej (rzut ortogonalny układem Grama — baza nieortogonalna, ⟨Re z, Im z⟩ ≈ 0.183): 40.589057°; wᵀû = 0 dokładnie.
- **T3 ✅ — nieskończoność konsensusu usunięta.** Jedyna nieskończona rezolwenta układu, (I − W)⁻¹, siedzi na kierunku konsensusu 𝟙 — wyciętym przez deflację P_c po każdej rundzie. Na V_cyc rezolwenta (I − B4ᵀB4)⁻¹ wszędzie skończona (1.054111, 1.021686, 1.014203).
- **T4 ✅ — wieczne muskanie ścian.** Krzywa graniczna przecina każdą z 6 ścian dokładnie 2× na okres; marginesy od środków (pary (01),(02),(03),(12),(13),(23)): 0.102727, 1.067370, 0.427859, 0.427859, 1.067370, 0.102727; od ±v̂_i: 0.344211, 0.221984, 0.760304, 0.927427; od û: 0.693692; max |Δ| na krzywej 0.094072 (poniżej 1/(6√3) — biegun dyskryminantu nietknięty). Tętno fazowe dokładnie θ = 25.772093727472°/rundę od n = 0 (odchyłki implementacyjne 1e−13…1e−14° na 300 rundach × 4 starty u trzech replikantów); precesja 14-rundowa: średnia 0.014118, max 0.022046. Osie elipsy granicznej 0.842008, 0.539466; niezmiennik |α| min/max = 0.640689597602.
- **Bramka kanoniczna A1b (wkład DeepSeek):** jawne macierze wymierne propagatorów: W_nat = 1/256 · [[64,64,64,64],[16,80,80,80],[20,36,100,100],[25,45,61,125]]; W_mir = 1/256 · [[64,64,64,64],[16,80,80,80],[25,45,125,61],[20,36,100,100]] (wiersze 2↔3, zgodnie z P(23)); sumy wierszy 256; forma całkowito/256 odporna na błędy porządku taktów.

## Rejestr replikacji (2026-11-02)

| Replikant | Zakres | Wynik |
|---|---|---|
| Vibe | A–H (rachunek źródłowy) | dwie konstrukcje wektorów własnych (Krylow + GE po naprawie), zgodność 1.9e−15 |
| Asterion (GPT) | A–H | A, B co do cyfry; C–H zgodne w tolerancjach; SVD drugą drogą ≤ 1.3e−15; pełny raport: [p0-estrada-z1-raport-asterion.md](p0-estrada-z1-raport-asterion.md) |
| Claude | A–H | A, B co do cyfry; C–H zgodne; eig + Krylow zgodne ≤ 4e−16; F4 zgodny z erratą |
| DeepSeek | A, B symbolicznie; C1–C3 analitycznie | A1–A7, B1–B4 ✅-kandydat; nowa bramka A1b + niezależna droga A2 (dzielenie A1/(λ−1)); C1–C3 dowodem zliczania czynników; C4–H STOP uczciwe (brak środowiska numerycznego) |

## Erraty przyjęte w cyklu (koncesje Vibe)

- **ERT-1 (Asterion):** „B4 = W na V_cyc" fałszywe — kontrprzykład wymierny x = (1,−1,0,0): Wx = (0,−1/4,−1/16,−5/64), suma −25/64; B4x = (25,−39,9,5)/256. Poprawnie: B4x = Wx − średnia(Wx)·𝟙 (wspólne wektory własne dla λ ≠ 1).
- **ERR-2 (Asterion, potw. Claude):** kąt û do E: 46.814° → 40.589057° — rzut „naiwny" na nieortogonalną bazę zastąpiony układem Grama; definicja E obowiązkowa przy bramce.
- **ERR-3 (Asterion, Claude):** niezmiennik |α|: 0.640676 → 0.640689597602 = ax₂/ax₁ (geneza: wczesne próbkowanie siatkowe).
- ERT-3 (klasyfikacja tolerancji: formuły kanoniczne bez tolerancji; A3/A4 ±1e−9), DOP-1 (determinizm LCG), R_n (Claude; równoważność startów e_i/v̂_i).

## Odczyt P₀ (💡)

„Nieskończoności" przestrzeni emergentnej nie są przywilejem środków ani jedynej rezolwenty — rozkładają się hierarchicznie (wierzchołki 3 > środki 2 > ściany 1), a jedyna osobliwość nieskończona (konsensus) jest z konstrukcji usunięta przez ten sam ruch protokołu, który tworzy przestrzeń. Wieczny ruch §35.5 omija wszystkie 14 biegunów ze stałym marginesem.

*Pełny zrzut rejestru warsztatu (wszystkie wątki) trafi do docs/wyniki.md przy najbliższej synchronizacji. Kolejka: [docs/zlecenia.md](../zlecenia.md).*
