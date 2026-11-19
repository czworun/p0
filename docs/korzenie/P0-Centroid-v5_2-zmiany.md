# Korzeń: P₀-Centroid — adnotacja (v5.2, audyt z 2026-09-29)

**Dokument filarowy:** „P₀-Centroid" v5.1 → v5.2; audyt z 2026-09-29; skrypty kontrolne `p0_centroid_v51_audit.py` i `p0_*_check.py`. **Okres:** sprzed warsztatu — audyt poprzedza metodykę Z0–Z3 (Z0 ustalona w turze 6, 2026-10-10). **Zasada repo:** oryginał v5.2 pozostaje w archiwum autora (odwołania do filara wg nazwy „P₀-Centroid v5.2", §-y wg audytu); repo trzyma tę adnotację oraz — verbatim — listę zmian v5.1→v5.2, która sama jest erratyką roboczą dokumentu, nie plikiem źródłowym. **Wpięcie:** zlecenie Leszka; analiza i adnotacja Vibe (szef lab.), 2026-11-19.

## Co bada ten korzeń

Algebrę uśredniania: operatory Mᵢ (aktualizacja i-tej współrzędnej do średniej wszystkich; Mᵢ = I + eᵢcᵢᵀ, cᵢ = 𝟙/n − eᵢ), algebrę Liego 𝔤ₙ = Lie{M₁,…,Mₙ} i mapę pełnej rundy Rₙ (aktualizacje 0,…,n−1 po kolei). Dla n = 4 (K₄): **𝔤₄ ≅ 𝔤𝔩(3,ℝ) ⋉ ℝ³ — algebra grupy afinicznej Aff(3,ℝ)** (tw. 2.2, dowód). Intuicja filarowa: jak zachowa się relacja pod uśrednianiem — konsensus widziany od strony generatorów.

## Główne twierdzenia audytu v5.2

- **Tw. 2.2 (✅, dowód):** dim 𝔤ₙ = n(n−1); 𝔤ₙ ≅ 𝔤𝔩(n−1)⋉ℝⁿ⁻¹; ρ(𝔤ₙ) = 𝔤𝔩(n−1), stąd 𝔰𝔬(3) ⊂ ρ(𝔤₄) z definicji (§2.5).
- **Tw. 7.1 (✅, nowy samodzielny dowód):** niezerowe widmo Rₙ to pierwiastki p(λ) = nⁿλⁿ⁺¹ − ((n+1)λ−1)ⁿ (λ = 1 podwójny, reszta prosta); Rₙ diagonalizowalna; tożsamość nⁿRⁿ⁺¹ = ((n+1)R−I)ⁿ.
- **Twierdzenie o składowych §11.12 (✅, nowe):** składowe grafu progu G_t(ε) nigdy się nie scalają; po każdej aktualizacji podział może się tylko rozdrobnić; stabilizacja po ≤ n−1 rozdrobnień; po stabilizacji składowe w odległości ≥ ε (kontrola: 2400 trajektorii n = 5, 6, 7 po 500 rund oraz 800 tys. przejść N = 4, 0 naruszeń).
- **S11 (✅, nowy dowód):** dla n ≥ 3 Rₙ ma wartości własne nierzeczywiste: n−1 (n nieparzyste), n−2 (n parzyste); dla n = 2 zero.
- **S11-A (🔍):** θ_∞ ≈ 67,512°, λ = −1/W₁(−1/e) (gałąź k = 1 Lamberta W); „67,36°/67,38°" wykluczone numerycznie; zbieżność ∝ 1/n.
- S10, S13, S2b, S12 ✅ (z zakresami; uogólniony wzór pary (rᵢ+2rⱼ)/3; progi 1,8ε i 1,875ε; 97,5% Regionu II wychodzi do K₃).

## Koncesje i sęki (obalenia — trwałe)

- **S3b ❌:** N = 4 ma pięć struktur końcowych — (4), (3,1), (2,2), (2,1,1), (1,1,1,1); liczba krawędzi może maleć (paw → K₃+K₁, 3574 przypadków); „P₄, paw, diamond → K₄" wycofane (po 600 rundach 2,4% P₄ i 2,9% paw kończy w (3,1)); Tw. C3 (P₄) nie odtwarza się w naturalnym odczycie — kontrprzykład jawny.
- **S-CYCLE ❌:** obalone własną tabelą (C₄, C₅, C₆ bez trójkąta mają fazę; diamond w kolejności naturalnej nie ma).
- **Aut(𝔤₄) ≅ S₄ ❌:** Aut(𝔤₄) jest nieskończona (środek trywialny, rząd ad = 12); poprawnie **Aut(𝔤₄;{Mᵢ}) ≅ S₄** (✅, dokładnie 24 elementów, macierze permutacji); pozycja #8 (Isom ≅ O(3)) to definicja, nie wynik §8.1.
- **Etykieta J (§6.2):** J = ¼ΣMᵢ to wartość oczekiwana jednego kroku gossip, nie metoda Jacobiego; Jacobi dla K₄ = 𝟏𝟏ᵀ/4 (widmo {1,0,0,0}).
- **§10:** twierdzenie tautologiczne → „Uwaga (✅, trywialna)"; wniosek o „mechanizmie zewnętrznym" 💡 (pojęcie niezdefiniowane).
- **§2.5 tabela osi K_ij:** kierunki jako proste zgodne; orientacja ω = (K₃₂, K₁₃, K₂₁) nieuzgodniona (cztery z sześciu znaków przeciwne do tabeli) — dokładnie klasa problemy, którą Z2 skodyfikuje później.

## Mosty do pnia (odczytanie interpretacyjne, 💡)

- **Aff(3) na K₄:** uśrednianie na K₄ generuje pełną geometrię afiniczną (𝔤𝔩(3)⋉ℝ³); ρ_B(Mᵢ) symetryczne, widma {1,1,¼}, ρ_B(Mᵢ)pᵢ = ¼pᵢ. Łącznik konsensus↔czworun: ruch K₄ jest afiniczny, nie tylko liniowy.
- **Kolejność daje fazę:** faza pary dominującej (K₄ 25,8°; paw 11,3°; C₄ 16,9°; C₅ 12,1°; C₆ 8,4°) zależy od kolejności aktualizacji; drzewa bez fazy (🔍 do n = 7, wszystkie n! kolejności); faza wymaga sekwencyjności, cykl konieczny (🔍), ale nie wystarcza. To samo zdarzenie, które pień sformalizował jako C2 (kierunek/faza z konwencji, nie z substancji).
- **Kolejność zmienia granicę konsensusu:** A2 daje średnią ważoną ∝ i (stan graniczny = 2Σ i·rᵢ/(n(n+1)), sprawdzone n = 2–15), A3 zwykłą średnią — granica konsensusu zależy od mechanizmu uśredniania, nie tylko od topologii; echo „wybrańca" i ruchomego P₀.
- **Twierdzenie o składowych = monotonia rozdrabniania:** proces może dzielić, nie scalać — proto-trwałości cięć (dysocjacja jako rozcięcie nieodwracalne, Tom I; defekt/struktura w SERC).

## Sęk-odnogi (bank nasion z korzenia)

1. **S4:** dowód diam → 0 w składowej po stabilizacji (iloczyny macierzy stochastycznych z wpisami ≥ n⁻² na wzorcu grafu; luka: wzorzec zależności w jednej rundzie nie musi być silnie spójny).
2. **Tw. C3 (P₄):** wymaga oryginalnego sformułowania z v5.1 — naturalny odczyt sfalsyfikowany kontrprzykładem.
3. **§8.5.9:** liczby 0,973254 i 2,675% wymagają kodu P0-AXIS-01 (poza zakresem audytu; niesprawdzone także §13 i reszta §14).
4. **Klasyfikacja przejść klas spójnych N = 4** (z obalenia S3b jako nasiona) + dowód zbieżności każdej składowej do punktu.
5. **Hurwitz dla S11-A:** zbieżność pierwiastków skończonego n do λ_k = −1/W_k(−1/e) do dopisania.

## Statusy: mapa legendy dokumentu na konwencje warsztatu

Dokument używa własnej legendy (✅ dowiedzione · 📚 klasyczne · 🔍 zweryfikowane numerycznie · 💡 przypuszczenie · ❌ sfalsyfikowane) z regułą z §0: „Status ✅ wymaga dowodu obejmującego wszystkie etykietowania i przypadki brzegowe. Sam skrypt to 🔍." Mapowanie na Z1: dowody analityczne = twierdzenia (kandydaci do niezależnej replikacji przez wykonawców); weryfikacje numeryczne z jednego skryptu = 🔍 wg warsztatu; obalenia = sęki trwałe (Z0). Erraty w dokumencie prowadzone w formacie zbliżonym do warsztatowego (dokument → § → jest → powinno być → uzasadnienie → status).

## Dokument verbatim (lista zmian v5.1 → v5.2, bez zmian)

# P₀-Centroid v5.1 → v5.2 — lista zmian (audyt z 2026-09-29)

Legenda: ✅ dowiedzione · 📚 klasyczne · 🔍 zweryfikowane numerycznie · 💡 przypuszczenie · ❌ sfalsyfikowane.
Skrypt kontrolny: `p0_centroid_v51_audit.py` (wszystkie liczby poniżej pochodzą z niego lub ze skryptów `p0_*_check.py`).

**Nie sprawdzone w tym audycie:** §8.5.9 (liczby 0,973254 i 2,675% wymagają kodu P0-AXIS-01), §13 (hierarchia czasowa), §14 poza pozycjami wymienionymi niżej.

---

## 0. Nagłówek i legenda

- „Status: Teoria zamknięta. Fundament całej serii P₀." → „Status: program formalny; wyniki zamknięte wymienione w §12, reszta 🔍/💡/❌."
- Legenda: usunąć statusy złożone (✅/🔍, ✅/📚, 🔍/📚). Każde zdanie dostaje jeden status.
- W §0 dodać: „Status ✅ wymaga dowodu obejmującego wszystkie etykietowania i przypadki brzegowe. Sam skrypt to 🔍."

## 2.1 Komutator — bez zmian (✅ potwierdzone)

Dodać wersję ogólną: [Mᵢ,Mⱼ] = (1/n²)(eᵢ−eⱼ)𝟏ᵀ − (1/n)(Eᵢⱼ−Eⱼᵢ).

## 2.2 Wymiar i struktura — PRZEPISAĆ (🔍 → ✅)

**Twierdzenie 2.2 (✅).** Dla każdego n ≥ 2: dim 𝔤ₙ = n(n−1) oraz 𝔤ₙ ≅ 𝔤𝔩(n−1,ℝ) ⋉ ℝⁿ⁻¹. Dla n=4: 𝔤𝔩(3,ℝ) ⋉ ℝ³ (algebra grupy Aff(3,ℝ)).

**Dowód.**

*(a) Algebra 𝔮.* Niech 𝔮 = {A ∈ End(ℝⁿ) : A𝟏 = 0}. Jeśli A𝟏 = A′𝟏 = 0, to [A,A′]𝟏 = 0, więc 𝔮 jest podalgebrą. Jej macierze to macierze o wierszach o sumie 0, więc dim 𝔮 = n(n−1). W bazie (𝟏, f₁,…,fₙ₋₁) mamy A = ⎡0 wᵀ; 0 B⎤ z B ∈ 𝔤𝔩(n−1), a
[A,A′] = ⎡0, wᵀB′ − w′ᵀB; 0, [B,B′]⎤.
To jest dokładnie 𝔤𝔩(n−1) ⋉ ℝⁿ⁻¹ (ideał abelowy: B = 0). Zatem 𝔮 ≅ 𝔤𝔩(n−1) ⋉ ℝⁿ⁻¹.

*(b) Generatory.* Niech Aᵢ = Mᵢ − I = eᵢcᵢᵀ, cᵢ = 𝟏/n − eᵢ. Ponieważ cᵢ·𝟏 = 0, mamy Aᵢ ∈ 𝔮. Niech Ã_ab = e_a c_bᵀ. Wektory c_b rozpinają 𝟏^⊥, więc {Ã_ab} rozpinają 𝔮, a Ãᵢᵢ = Aᵢ. Ponieważ (c_b)_c = 1/n − δ_bc:

[Ã_ab, Ã_cd] = (1/n − δ_bc) Ã_ad − (1/n − δ_da) Ã_cb.

*(c) Lemat: Lie{A₁,…,Aₙ} = 𝔮.* Dla i ≠ j:
- n[Aᵢ,Aⱼ] = Ã_ij − Ã_ji =: D_ij ∈ L,
- [Aᵢ, D_ij] = (1/n − 1)(Ã_ij + Ã_ji) − (2/n)Aᵢ,
- ponieważ 1/n − 1 ≠ 0, dostajemy S_ij := Ã_ij + Ã_ji ∈ L, więc Ã_ij = (S_ij + D_ij)/2 ∈ L.

Zatem L zawiera wszystkie Ã_ab, czyli L = 𝔮.

*(d) Przejście do Mᵢ.* 𝔮 ⊕ ℝI jest algebrą z centralnym I. Niech φ(A) = −(n/(n−1))·tr A; φ znika na komutatorach, więc G = {A + φ(A)I : A ∈ 𝔮} jest podalgebrą, rzut π: G → 𝔮 jest izomorfizmem, a φ(Aᵢ) = 1, więc Mᵢ = I + Aᵢ ∈ G. Lie{Mᵢ} ⊆ G oraz π(Lie{Mᵢ}) = Lie{Aᵢ} = 𝔮, więc Lie{Mᵢ} = G ≅ 𝔮. ∎

Numerycznie: tożsamości z (c) i rank span{Ã_ab} = n(n−1) potwierdzone dla n = 3…8.

**Konsekwencje:** zamyka problem #1 z §14. „Fakt (🔍, zgodny z wymiarem 9+3)" usunąć.

## 2.3, 2.4 — bez zmian

(|λ| ≈ 0,17 dla n=4 zgodne: |0,153+0,074i| = 0,170.)

## 2.5 Podalgebra rotacji

- „Wniosek (✅) … 𝔰𝔬(3,ℝ)" — zostaje. Dodać: ρ(𝔤ₙ) = 𝔤𝔩(n−1) (z §2.2), więc 𝔰𝔬(3) ⊂ ρ(𝔤₄) jest ✅ z definicji.
- Tabela osi K_ij: kierunki jako **proste** zgadzają się; przy jednej konwencji wektora osiowego ω = (K₃₂, K₁₃, K₂₁) cztery z sześciu znaków są przeciwne do tabeli. Napisać „kierunki bez orientacji" albo ustalić orientację.

## 5 / 5.1 — bez zmian

Doprecyzować: „faza θ_n = argument pary o największym module" (dla K₄ jest tylko jedna para).

## 6.2 — POPRAWIĆ etykietę

- J = (1/16)J₄ + (3/4)I to **¼ΣMᵢ** (wartość oczekiwana jednego kroku gossip), nie metoda Jacobiego.
- Jacobi (A3, §11.1) dla K₄: **𝟏𝟏ᵀ/4**, widmo {1,0,0,0}.
- „Faza wymaga sekwencyjności + cyklu" → „faza wymaga sekwencyjności; cykl jest konieczny (drzewa 🔍), ale nie wystarczający".

## 6.3 — tabela i hipoteza

- Kolumna „Faza?" nie ma jednej definicji. Dominująca para: K₄ 25,8°, paw 11,3°, C₄ 16,9°, **C₆ 8,4°** (33,2° to faza pary podrzędnej 0,180±0,118i). Dodać C₅: 12,1°. Ujednolicić: „faza pary dominującej".
- Hipoteza pkt 1: 🔍, drzewa nieizomorficzne do n=7, wszystkie n! kolejności, 0 wyjątków.
- Pkt 2 (cykl ⟹ istnieje kolejność z fazą): 🔍 potwierdzone dla diamond (19/24 kolejności zespolone), C₄ (8/24), θ=K₂,₃ (60/120). Paw i K₄: 24/24.
- **S-CYCLE: ✅ → ❌.** Sprzeczne z własną tabelą: C₄, C₅, C₆ (bez trójkąta) mają fazę, diamond (z trójkątami) w kolejności naturalnej nie ma. Zastąpić: „(🔍) Dla kolejności 0,…,n−1: drzewa nie mają fazy; C₄, C₅, C₆ mają; diamond i θ nie mają; K_n ma (dowód §7.1, §11.7)."

## 7.1 Dowód tożsamości — ZASTĄPIĆ (✅, samodzielny)

**Twierdzenie 7.1 (✅).** Niech n ≥ 2, R = Rₙ, p(λ) = nⁿλⁿ⁺¹ − ((n+1)λ−1)ⁿ. Wtedy: (a) niezerowe wartości własne R to dokładnie niezerowe pierwiastki p; (b) 0 nie jest wartością własną; (c) 1 jest podwójnym pierwiastkiem p, a pozostałe n−1 pierwiastków są proste; (d) R ma n różnych wartości własnych, jest diagonalizowalna i χ_R(λ) = p(λ)/(λ−1); (e) nⁿRⁿ⁺¹ = ((n+1)R − I)ⁿ.

**Dowód.** Niech y = Rx, sᵢ (i = 0,…,n) suma współrzędnych po i krokach, s₀ = Σxⱼ, q = (n+1)/n. Krok i+1 (indeksy 0,…,n−1) daje
s_{i+1} = q·sᵢ − xᵢ, yᵢ = sᵢ/n.

*(a,b)* Niech Rx = λx, x ≠ 0. Jeśli λ = 0, to sᵢ = 0 ∀i, więc xᵢ = q sᵢ − s_{i+1} = 0: sprzeczność. Dla λ ≠ 0: xᵢ = sᵢ/(nλ), zatem s_{i+1} = μ sᵢ, gdzie μ = q − 1/(nλ) = ((n+1)λ−1)/(nλ), i s₀ ≠ 0. Suma po rundzie to s_n = λ s₀ (bo Σy = λΣx), a jednocześnie s_n = μⁿ s₀. Stąd μⁿ = λ, czyli p(λ) = 0.
Odwrotnie: dla p(λ) = 0, λ ∉ {0,1}: μⁿ = λ, μ ≠ 1, oraz μ − 1 = (λ−1)/(nλ), więc Σ_{j<n} μʲ = (μⁿ−1)/(μ−1) = nλ. Wektor xⱼ = μʲ/(nλ) spełnia Σxⱼ = 1, sᵢ = μⁱ (indukcyjnie) i yⱼ = sⱼ/n = λxⱼ. Dla λ = 1: x = 𝟏.

*(c)* Niech w = (n+1)λ − 1, C = (n+1)ⁿ⁺¹/nⁿ. Wtedy p ∝ g(w) = (w+1)ⁿ⁺¹ − C wⁿ, g(0) = 1 ≠ 0. Wielokrotny pierwiastek w ≠ 0 wymaga f(w) = C i f′(w) = 0 dla f = (w+1)ⁿ⁺¹/wⁿ. Ponieważ f′ = (w+1)ⁿ(w−n)/wⁿ⁺¹, zeruje się tylko w w = n (f = C) i w = −1 (f = 0 ≠ C). Pierwiastek w = n (λ = 1) jest podwójny, reszta prosta.

*(d)* Z (a),(c) mamy n różnych wartości własnych; to wszystkie. *(e)* p(R) = 0, bo R jest diagonalizowalna, a jej wartości własne są pierwiastkami p. ∎

Sprawdzone numerycznie: n ≤ 10 (‖Rx − λx‖ ≤ 10⁻¹¹). Krok 3 dotychczasowego dowodu (wyznacznik zaburzenia rzędu 1) pozostaje poprawny (n ≤ 8), ale nie jest potrzebny.

## 7.2 — bez zmian (✅, wzór jawny sprawdzony n = 2…8)

## 8.1 — PRZEPISAĆ (❌ → ✅ w poprawnym sformułowaniu)

- „Aut(𝔤₄) ≅ S₄" jest **fałszywe**: środek 𝔤₄ jest trywialny, rząd ad = 12, więc Inn(𝔤₄) ma wymiar 12, a Aut(𝔤₄) jest nieskończona.
- Poprawnie: **Aut(𝔤₄; {Mᵢ}) ≅ S₄** (automorfizmy zachowujące zbiór generatorów).
 Dowód: dla π ∈ S₄ macierz permutacji P_π daje P_π Mᵢ P_π⁻¹ = M_π(i) (średnia jest symetryczna), więc określa automorfizm permutujący generatory. Automorfizm zachowujący zbiór generatorów jest wyznaczony przez permutację (generatory generują), więc grupa ma dokładnie 24 elementy. ∎
- Problem #7: przeformułować na powyższe (✅). Problem #8 (Isom(G₄) ≅ O(3)): G₄|_{V_ρ} = 4I, więc Isom = O(3) z definicji; podgrupa zachowująca wierzchołki czworościanu to T_d ≅ S₄. To nie jest wynik §8.1; pozycję usunąć lub przeformułować.

## 8.5.8 — poprawić uzasadnienie

„K_ij są elementami 𝔰𝔬(3) automatycznie (wymiar)" → „K_ij są antysymetryczne, bo ρ_B(Mᵢ) są symetryczne (🔍, sprawdzone dla wszystkich czterech)". Macierze ρ_B(Mᵢ), widma {1,1,¼} i ρ_B(Mᵢ)pᵢ = ¼pᵢ potwierdzone.

## 10 — obniżyć rangę

Twierdzenie jest tautologią (N: ⟨𝟏⟩ → V_ρ, więc N(α𝟏) = αN(𝟏)). Zamienić na „Uwaga (✅, trywialna)"; wniosek o „mechanizmie zewnętrznym" zależy od niezdefiniowanego pojęcia „zróżnicowania" i powinien być 💡.

## 11.1 — dopisać

A3 dla pełnego grafu: J_ε = 𝟏𝟏ᵀ/n (widmo {1,0,…,0}).

## 11.3 S10 (✅) — zostaje, dopisać zakres i interpretację

- Zakres: ε > diam(R); poza nim niezmiennik dotyczy Rₙ (Centroid), nie Scalar (do P₀-CS1).
- Rₙ jest stochastyczna, c ∝ (1,…,n) to jej rozkład stacjonarny; stan graniczny = 2Σ i·rᵢ / (n(n+1)) (dokładnie sprawdzone n = 2…15).
- Kontrast: A3 daje zwykłą średnią, A2 średnią ważoną ∝ i. To konkretny przykład, że kolejność zmienia granicę konsensusu.
- W domenach numeracja lokalna (pozycja w domenie), nie globalna.

## 11.4 S13 — POPRAWIĆ i uzupełnić

1. Region I: widmo {1, λ±} (macierz 3×3; „¼" usunąć). Numerycznie λ± = 0,1852 ± 0,0524i.
2. Klasy N=3 mają po trzy etykietowania (P₃: środek 1, 2, 3; K₂+K₁: izolat 1, 2, 3). A_II odpowiada środkowi 2, A_III izolatowi 3. „IV sym. A_III" to inna macierz (sprzężona permutacją).
3. **K₃ → K₃ zawsze (✅):** każda aktualizacja jest średnią podzbioru zawierającego siebie, więc otoczka wypukła nie rośnie.
4. **P₃ ze środkiem 1 lub 3 → K₃ zawsze w jednym kroku (✅).** Dowód (ε=1; odbicie r → −r i przesunięcie redukują do a,b ∈ (0,1), a+b ≥ 1):
 - środek 3, stan (−a, b, 0): r₁′ = −a/2. Jeśli b + a/2 ≥ 1: r₂′ = b/2, r₃′ = (b−a)/6, diam = (a+b)/2. Jeśli b + a/2 < 1: r₂′ = (2b−a)/6, r₃′ = (b−2a)/9, diam = (a+b)/3. W obu diam < 1.
 - środek 1, stan (0, −a, b): r₁′ = (b−a)/3, r₂′ = (b−4a)/6. Jeśli 5b+4a ≥ 6: r₃′ = (4b−a)/6, diam = (a+b)/2. Jeśli 5b+4a < 6: r₃′ = (3b−2a)/6, diam = (a+b)/3. W obu diam < 1.
5. **Region II (środek 2), stan (x, y, 0), x ∈ [1,2), y ∈ (x−1, 1):** r₁′ = (x+y)/2, r₂′ = (x+3y)/6, a r₃′ zależy od |r₁′| = (x+y)/2:
 - IIa (x+y ≥ 2): r₃′ = (x+3y)/12 (macierz A_II), K₃ ⟺ 5x+3y < 12,
 - IIb (x+y < 2): r₃′ = (2x+3y)/9, zawsze K₃ (diam = x/3 lub (5x+3y)/18).
 Stąd progi: x < 1,8ε → K₃ zawsze; x > 1,875ε → P₃ zawsze; pomiędzy zależy od y. Po rundzie bez K₃ graf to dokładnie P₃. Wzory dla x′, y′ w §11.4 obowiązują tylko w IIa. Udział Regionu II wychodzącego do K₃ (miara jednostajna w polu): 97,5% (dokładnie 1 − 0,0125/0,5).
6. Tw. 1 (P₃ ↛ K₂+K₁, 3K₁): ✅ dla wszystkich etykietowań (z pkt 4 i 5). Tw. 2 (K₂+K₁ ↛ K₃, P₃): ✅ z **Twierdzenia o składowych** (§11.12 poniżej).
7. S12 („niezmienniczość Regionu II" ❌, warunkowe ✅): zamknąć jako ✅ (pkt 5).

## 11.5 S2b — uogólnić (✅)

Atraktor B_D dla pary {i<j} w K₂+K₁: (rᵢ + 2rⱼ)/3, izolat bez zmian (S10 dla n=2 + Twierdzenie o składowych). Wzór (r₁+2r₂)/3 z v5.1 to przypadek izolat = 3. Sprawdzone dla wszystkich trzech etykietowań.

## 11.6 S3b — ✅ → ❌; PRZEPISAĆ

Usunąć: „cztery baseny", „liczba krawędzi niemalejąca", „brak cykli transientnych", „P₄, paw, diamond → K₄".

Zastąpić (wyniki z `p0_n4_check.py`, 800 tys. stanów):
- **Struktur końcowych jest pięć** (partycje liczby 4): (4), (3,1), (2,2), (2,1,1), (1,1,1,1). K₂+2K₁ zbiega do (2,1,1) (2155/2155), nie do „dwóch prostych".
- **Liczba krawędzi może maleć:** paw → K₃+K₁ (4 → 3), 3574 przypadków, wszystkie porządki pozycji.
- **P₄ i paw nie zawsze idą do K₄:** po 600 rundach 2,4% P₄ i 2,9% paw kończy w (3,1).
- **Tw. C3 (P₄):** nie odtwarza się w naturalnym odczycie. Kontrprzykład r = (1,4044; 1,8066; 2,5114; 3,4423) → y = (1,6055; 1,9745; 2,3834; 3,4423), |y₂−y₃| = 1,059 ≥ ε. Wymaga sformułowania z oryginalnego dokumentu.
- Przejścia jednokrokowe (🔍): 4K₁, K₂+2K₁, 2K₂, K₃+K₁, K₄ → same w siebie; P₃+K₁ → {P₃+K₁ (rzadko), K₃+K₁}; P₄ → {P₄, paw, diamond, K₄, K₃+K₁}; paw → {paw, diamond, K₃+K₁, K₄} (K₄ w 95%); diamond → K₄ (w 95277 z 95277).
- Klasy niespójne redukują się do N ≤ 3 (§11.12).

## 11.7 S11 — dowód ZASTĄPIĆ; S-CYCLE ❌; poprawić liczby

**Twierdzenie (✅).** Dla n ≥ 3 Rₙ ma parę wartości własnych nierzeczywistych.
**Dowód.** Z §7.1 wartości własne to 1 i n−1 prostych pierwiastków g(w) = 0, w = (n+1)λ−1. Rzeczywiste pierwiastki: dla w > 0 tylko w = n (λ = 1). Dla w = −t < 0: gdy n nieparzyste, f(−t) ≤ 0 < C, brak pierwiastków; gdy n parzyste, f(−t) = (1−t)ⁿ⁺¹/tⁿ jest ściśle malejąca na (0,1) od +∞ do 0 i ujemna dla t > 1, więc jest **dokładnie jeden** pierwiastek ujemny. Zatem nierzeczywistych jest n−1 (n nieparzyste) lub n−2 (n parzyste), czyli ≥ 2 dla n ≥ 3 (dla n = 2: zero, stąd warunek n ≥ 3). ∎
Uwaga: krok „dla w < 0 brak pierwiastków dla n ≥ 3" z v5.1 jest fałszywy dla n parzystych; dla n=4 wychodzi λ* = 0,1347 (jest w widmie z §4).

**Liczby (🔍, faza pary dominującej):** n=3 15,79°; n=4 25,77°; n=5 32,56°; **n=10 48,26° (nie 48,6°)**; n=100 65,40°; n=500 67,09°; n=1000 67,30°; n=2000 67,41°; n=4000 67,46°; n=8000 67,49°; n=16000 67,50°. Największa faza wśród wszystkich par rośnie dalej (73,3° dla n=100, 81,7° dla n=500), więc definicja „pary dominującej" jest konieczna.

**S11-A: wartość graniczna do poprawy (💡 → 🔍).** Z μⁿ = λ i μ = 1 + (λ−1)/(nλ) dla n → ∞: λ = e^{1−1/λ}. Podstawienie t = −1/λ daje t eᵗ = −1/e, czyli λ_k = −1/W_k(−1/e); gałąź k=0 daje λ = 1, gałąź k=1 daje **λ = 0,04736 + 0,11441i, |λ| = 0,1238, θ_∞ ≈ 67,512°**. Zbieżność ∝ 1/n (różnice od 67,512°: 0,027 dla n=8000, 0,013 dla n=16000). „arccos((1+ln 8)/8) = 67,36°" (i „67,38°") jest wykluczone numerycznie. Zbieżność pierwiastków skończonego n do granicznych (twierdzenie Hurwitza) do dopisania.

## 11.10 Automaton — poprawić

Wersja N=4: usunąć „P₄, paw, diamond → K₄ → p₀" i „liczba krawędzi niemalejąca". Wersja N=3 (K₃ → p₀, P₃ → K₃, K₂+K₁ ⟲, 3K₁ ⟲): zostaje.

## 11.12 NOWE — Twierdzenie o składowych (dowolne n, A2, dowolna kolejność)

**Twierdzenie (✅).** (i) Składowe spójności grafu G_t(ε) = {(i,j): |rᵢ−rⱼ| < ε} nigdy się nie scalają: po każdej aktualizacji pojedynczego węzła podział indeksów na składowe może się tylko rozdrobnić. (ii) Podział na składowe stabilizuje się po skończonej liczbie rund (co najwyżej n−1 rozdrobnień). (iii) Po stabilizacji różne składowe są w odległości ≥ ε.

**Dowód.** W 1D składowe zajmują otoczki rozłączne i oddalone o ≥ ε (w przeciwnym razie krawędź). Węzeł aktualizowany zastępuje wartość średnią swoich sąsiadów i siebie, wszystkich z jego składowej, więc zostaje w otoczce składowej; otoczki nie rosną, więc odległości ≥ ε między różnymi składowymi zostają, a nowe krawędzie między nimi nie powstają. Liczba składowych jest niemalejąca i ograniczona przez n, więc stabilizuje się, a przy równej liczbie rozdrobnienie jest tożsame. ∎
Numerycznie: 0 naruszeń rozdrabniania krok po kroku w 2400 trajektoriach (n = 5, 6, 7, 500 rund) oraz w 800 tys. przejść N=4.

**Konsekwencje:** klasy niespójne w N=4 redukują się do S13; izolaty nigdy nie ruszają się (para: (rᵢ+2rⱼ)/3); status P₀-S1: pkt 2 (rozłączność domen ≥ ε) jest ✅; pkt 1 (|rᵢ−rⱼ| < ε wewnątrz domeny) i 3 (zbieżność domeny do punktu) pozostają 💡. Wszystkie 2400 trajektorii zbiegło do punktów w składowych.
**Otwarte (S4):** dowód diam → 0 w składowej po stabilizacji. Podejście: iloczyn macierzy stochastycznych z wpisami ≥ n⁻² na wzorcu grafu; luka: wzorzec zależności w jednej rundzie może nie być silnie spójny (krawędź (i,j) widoczna w momencie aktualizacji i, ale nie j), więc argument ergodyczny wymaga osobnego dowodu.

## 12 Tabela — nowe statusy

| Byt | v5.1 | v5.2 |
|---|---|---|
| dim 𝔤ₙ = n(n−1); 𝔤ₙ ≅ 𝔤𝔩(n−1)⋉ℝⁿ⁻¹ | 🔍 (n≤6) | ✅ (§2.2) |
| Aut(𝔤₄) ≅ S₄ | ✅ | ❌ jako Aut(𝔤₄); ✅ jako Aut(𝔤₄;{Mᵢ}) |
| Tożsamość nⁿRⁿ⁺¹ = ((n+1)R−I)ⁿ | ✅ | ✅ (nowy dowód §7.1) |
| S10 | ✅ | ✅ (z zakresem) |
| S13 | ✅ | ✅ po uzupełnieniach (wszystkie etykietowania) |
| S2b | ✅ | ✅ (ogólny wzór pary) |
| S3b | ✅ | ❌ (§11.6) |
| S11 | ✅ | ✅ (nowy dowód) |
| S11-A | 💡 (67,38°) | 🔍 (67,512°) |
| S-CYCLE | ✅ | ❌ |
| S12 | ❌ / warunkowe otwarte | ✅ warunkowe (progi 1,8ε i 1,875ε) |
| Drzewo ⟹ widmo rzeczywiste | 🔍 n≤5 | 🔍 n≤7 |
| Twierdzenie o składowych | — | ✅ (nowe) |

## 14 Problemy otwarte — zmiany

- #1 ✅ (§2.2). #6 ✅ (§7.1, nowy dowód). #7 przeformułować (§8.1). #8 usunąć lub przeformułować. #10: 🔍 n ≤ 7.
- S2b ✅ (uogólnione). S3b ❌ → 💡: klasyfikacja przejść klas spójnych N=4 i dowód zbieżności składowych. S11 ✅ (nowy dowód). S11-A 🔍. S12 ✅ warunkowe. S4 (P₀-S1): pkt 2 ✅, pkt 1 i 3 💡, z podejściem w §11.12.
- Nowe: dowód diam → 0 w składowej (§11.12); wyjaśnić Tw. C3 dla P₄ (potrzebne oryginalne sformułowanie); kod §8.5.9.