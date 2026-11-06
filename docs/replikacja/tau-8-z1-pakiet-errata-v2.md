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
