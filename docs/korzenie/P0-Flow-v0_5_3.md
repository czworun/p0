# Korzeń: P₀-Flow — adnotacja (v0.5.3-final, zamrożony 2026-09-13)

**Dokument filarowy:** „P₀-Flow v0.5.3-final — relacyjna postać dynamiki przepływu" (status: ZAMROŻONA; konsolidacja czterech dokumentów: pierwotny P₀-Flow + P₀-Mechanism-VII + Dodatek A + Asymmetria strukturalna, wchłonięta jako §5.7; baza: Centroid, Defect, Net, Alchemy, Scalar, Memory, Estrada, AI, Hilbert, Axis). Pytanie wyjściowe: czy Navier–Stokes jest granicznym opisem dynamiki relacji P₀? **Odpowiedź negative, świadomie domknięta:** P₀-Flow na C¹(K_n) jest obiektem trzecim — dwukanałowym rozszerzeniem Eulera–Arnolda o kubiczny tensor (§7.5): ma kanał B×B→B (jak NS, nieobecny w pełnym EA), brak mu kanału B×B→A (obecnego w EA, nie NS), kanał A×B→B ma wspólny z oboma; algebra 𝔰𝔬(n−1), nie 𝔡𝔦𝔣𝔣_vol. Zamrożenie z uzasadnieniem redakcyjnym: „dalsze poprawki dają malejący zwrot — następny krok powinien być badawczy, nie redakcyjny" (wzorzec doboru momentu zamrożenia).

**Rozliczenie wchłonięcia (klauzula SSOT):** P₀-Defect (korzeń tego drzewa) wchłonął i rozwija konteksty flow-owe jako swoje §12A–G — tam żyje bieżące rozwinięcie. Ten plik jest **korzeniem źródłowym**: oryginał zamrożony, verbatim, jedyne źródło prawdy dla treści Flow jako takiej (w szczególności §5.5.1, §5.7, §7.5 — części, których w Defect nie ma). Przy PILLARS-TABLE: Flow figuruje jako korzeń źródłowy z odnośnikiem wchłonięcia do Defect §12A–G, nie jako duplikat.

**Co bada:** dynamikę sektora cyklicznego C¹(K_n): kanały V_cyc⊗V_cyc → V_cyc przy pełnej symetrii S_n (Tw. A: jedyny kanał = bracket Liego; konsekwencja Hom(Sym²V_cyc, V_cyc) = 0) i po złamaniu do S_{n−1} (branching Younga: V_cyc↓S_{n−1} = A ⊕ B; A = Λ²B; B = [n−2,1] standard; łańcuch interpretacyjny: rotacja → orientacja → amplituda); słownik operatorów NS (§2.4: R ↔ u, dp ↔ ∇p, L ↔ Δ, P_cyc ↔ wirowość, kanał V_cyc⊙V_cyc ↔ vortex stretching); granicę continuum — co się przenosi (T_a jako bracket 𝔰𝔬: [𝔤₀,𝔤₁] = 𝔤₁, kandydat ↔ (u·∇)ω), a co nie (T_b: kubiczny niezmiennik e_3 nie ma analogu SO; klasyfikacja par (𝔤,V) z Sym³(V) ⊇ triv jest skończona: 𝔰𝔲(n), 𝔤₂, 𝔣₄, 𝔢₆).

**Najmocniejsze (✅):**
1. **Tw. A** (m_n = 1 dla n ≥ 4, dowód momentami cykli: χ_V = C(X₁−1,2) − X₂; lemat Σ_λ; rozwinięcie m_n = 19/8 − 9/8 + 9/8 − 11/8 = 1) — fundament; w P₀-Defect §5 wersja wzmocniona (EGF, Bell, Poisson(½), Fraction n ≤ 20).
2. **Tw. C/D/E + typologia podgrup:** Sym²([n−2,1]) ⊇ [n−2,1] z krotnością 1 (T_b istnieje); Hom(A⊗B, B) ≅ Hom(A, Λ²B) = ℝ (T_a istnieje); asymetria A↔B niszczy T_b; Type I/II/III dla K₄ (S₄: 0; A₄/V₄: tak; D₄, S₃: 1; Z/4: 4) i tabela K₅; obserwacja A₅: rozkładalność nie wystarcza (Sym²(3a) = 1 ⊕ 5 ⊉ 3a, więc T_b = 0).
3. **Tw. 4 — sfalsyfikowana synergia** (wzorzec uczciwości eksperymentalnej): trzy tryby (A: T_b; B: T_a+T_b; C: T_a-rand) dają γ różne o ~10⁻⁴ (w szumie); γ(θ) = γ₀ + C·sin θ bez synergii; cross-correlation oscylacyjno-gładka bez ostrego maksimum przyczynowego; wniosek twardy: **T_b jest jedynym kanałem amplifikacji; T_a istnieje algebraicznie, ale jest funkcjonalnie nieaktywny w asymptotyce**.
4. **Test kowariancji S₄ (§5.5.1)** — historia pięciu iteracji (od różnic γ 30× między kopiami S₃, przez T_inv = 0 — uśrednienie losowego tensora po S₄ daje zero z Hom_{S₄}(V_cyc^{⊗3}, triv) = 0, manifestacja lematu Schura i ta sama bariera co Tw. A — do wyostrzenia: γ identyczne co do 10⁻¹⁷ dopiero po **kowariantnym transporcie tensora i warunku początkowego x₀, y₀**: γ(u_a) = +0,043005 (std 7,29·10⁻¹⁷), γ(u_b) = +0,258696 (std 8,33·10⁻¹⁷, 4 kopie S₃). Zasada ogólna: żaden wynik nieliniowej dynamiki na C¹(K_n) nie jest strukturalny bez testu kowariancji względem pełnej grupy symetrii — spółbrzmienie z zasadą znakowanej reprezentacji (S4-Rep, Defect §5.1, Estrada §30bis).
5. **Zestawienie trójkanałowe z pełnym Eulerem–Arnoldem (§7.5):** pozytywna charakterystyka „obiektu trzeciego" zamiast samego „nie jest NS" — klasyczny wynik negative podniesiony do identyfikacji strukturalnej.
6. **Tw. 5 (stabilność architektury względem n):** reguła reprezentacyjna niezmiennicza, wymiary rosną; λ_max(Φ(x*)) ~ 1/√(n−1), efektywność T_b maleje z n.

**Koncesje i sęki (❌/⚠️):** historia korekt krotności Tw. A (v0: m = 3 ❌, v1: „1+1+1 symetrycznych" ❌; dopiero jawny rachunek charakterów ✅) z zasadą: żadne twierdzenie o krotnościach bez wypisanego iloczynu <χ_V, χ_W> — spółbrzmienie z Defect §12B.5; ❌ „standard jedyny z Sym²(B) ⊇ B" (kontrprzykłady triv, [k,k] dla S_{2k}); poprawnie: w konkretnym rozszczepieniu V_cyc|_G tylko B = standard daje T_b; artefakt wagi sin²θ → sin θ (δ(30°) = −0,004, zero); M18 ❌ z Memory (pamięć przez ω-granicę: |𝓜({R₄})| = 1, faza spirali nie jest elementem 𝓜) — H-MEM-1 ostrożnie: sfalsyfikowana wersja ω-graniczna, otwarta wersja operatorowa (M19/M20); kontrakcyjność globalna operatora Alchemy sfalsyfikowana (0,0776 → 0,0933, naruszenie 26,6%), lokacyjna kontrakcja zachodzi (ρ ≈ 0,27, Procrustes residual ~10⁻¹⁶).

**Struktury 💡:** taksonomia siedmiu mechanizmów asymetrii (sekwencyjność R₄: kontrakcja, |λ| ≈ 0,17; defekt: rzut; orientacja exp(tK): konserwacja, |λ| = 1; próg K₂: bistabilny; kolejność R_e: uśrednianie; target P₀-AI: zadaniowy; VII: samoodziaływanie Φ: możliwy wzrost) — sześć pierwszych kontrakcyjne lub konserwatywne, jedyny kandydat amplifikacji to VII, i to w asymptotyce liniowy, nie nieliniowy (reframing sloganu „symetria daje orbitę, asymetria daje różnicę" z wymaganym zastrzeżeniem o liniowości wzrostu); **dwie nieliniowości** (biliniowe T_b z e₃ + progowe K₂) jako źródło binarnego charakteru propagacji (most do Net §13); faza 25,77° specyficzna dla K₄ — drabina S11/Scalar §11.6: 15,79° (n=3) → 25,77° (n=4) → 32,56° (n=5) → ~67° (n→∞); geneza z RML: symetria relacyjna S₄ nie różnicuje elementów, P₀ wymaga mechanizmu asymetrii (asymetria kliniczna → SERC, strukturalna → tutaj; §5.7).

**Mosty 💡 do pnia:**
1. **Faza 25,77° po raz trzeci:** γ pary dominującej R₄ (SERC: ρ = 0,170286 ∠25,772°, okres ≈ 13,97), kąt wiecznego muskania T4 (Estrada §36) i tutaj — faza atraktora dla K₄ (§3.7, przez Φ(x*)), oraz niezależnie Scalar S11. Trzy-documentowa koincydencja liczbowa z Rosnąco-drabiną S11 jako pytaniem kluczowym przy P₀-Estrada-03: identyfikator lokalny (drabina n) czy uniwersalny (piramidy 25,77°)?
2. **Architecture mismatch — potrójna walidacja** (tabela §2.3: Flow §3.2 Schur, AI §7.1 P_cyc·D = 0, Memory §7.1 D_exact → 0 pod R₄): realna własność formalizmu, nie artefakt implementacji — łączy się z rozłącznością Im(d) ⊕ V_cyc (Defect) i domyka wszelkie próby dynamiki V_cyc z samego V_cyc: wymaga złamania S_n → S_{n−1}.
3. **T_b jako „mieszanie wewnątrz B"** (§12, Dla Defect) — algebraiczny odpowiednik mieszania sektorowego; most Net: propagacja Część A ↔ Część B przechodzi przez T_b.
4. **Atraktor x* = (1,1,1)/√3** z B̃(x*,x*) = (2/√3)·x*, widmem Φ(x*) = {2/√3, −1/√3, −1/√3} i tożsamością gradientową B̃(x,x) = ∇W(x), W = 2x₁x₂x₃ — łączy dynamikę z potencjałem; kandydat mostu do Alchemy (atraktor jako orbita SO(3) więcej stały kształt) i do wieży remisów Defect.
5. Konteksty: Hilbert §12H.4–5 ((√2−1)δ, CᵀC = 4P_cyc) przez §12.2, z hipotezą otwartą: czy faza zespolona z §12H.4 moduluje T_b; Axis §16ter (deficyt dysklinacyjny 2,675%, dwa solvery) — pytanie o odpowiednik w dynamice T_b; Centroid §12 #11 (kontrakcja vs rotacja) — częściowa odpowiedź: kontrakcja = M = (1−β)I + 2hΦ(x*), rotacja = T_a, ale „kryterium wewnętrzne algebry" nadal nie istnieje (💡 ze sprzężeniem).

**Sęk-odnogi (do banku pytań, wg priorytetów dokumentu):** (1) alternatywna granica continuum, w której T_b przeżywa (kandydaci: 𝔤₂, 𝔢₆, Kähler, G₂-manifold; wysoki), (2) czy T_a + T_b odpowiada znanemu równaniu fizycznemu (Skyrme, chiralne, Landau–Lifshitz; wysoki), (4) czy istnieje granica 𝔰𝔬(n−1) → 𝔡𝔦𝔣𝔣_vol (wysoki), (5) dlaczego T_a jest funkcjonalnie nieaktywny w asymptotyce (średni), (8) związek T_b z Lemma W-L z Wave (niski), oraz M19/M20 z Memory (czulsza pamięć niż ω-graniczna; kanoniczna metryka trajektorii) — wspólna pozycja z Memory; rekomendacja własna dokumentu: kolejność (A) → (D) → (B) → (C).

**Statusy (mapa legendy na Z1):** dokument nosi statusy wewnętrzne (✅ 📚 🔍 💡 ❌) zgodne z legendą warsztatu. Twierdzenia algebraiczne (A, C, D, E, 5, atraktor, EA-zestawienie) mają jawne dowody; **jedyna pozycja z formalnym Z1 ≥ 2 to Tw. A** (momenty cykli tutaj §3.1 + pełny aparat w Defect §5: EGF/Bell/Poisson/Fraction). Rachunki numeryczne (γ tryby A/B/C, cross-correlation, skan kowariancji v5, drabina faz) były pojedyncze — przy scaleniu do pnia zachowują statusy dokumentu; **kandydat replikacji Z1 (tani, wzorcowy jako bramka kowariancji):** §5.2 tabela trybów i §5.5.1 skan θ (4 kopie S₃: 0° +0,04300, 60° +0,22292, 90° +0,25870; γ(u_a)/γ(u_b) jak wyżej) — historia iteracji v1–v5 czyni ten test gotową bramką sanity dla każdej przyszłej dynamiki na C¹(K_n).

**Uwagi redakcyjne (verbatim):** oryginał kończy się bez końcowego EOL (zachowane); dokument zaczyna się tytułem bez nagłówka #; status „zamrożona" oznacza koniec errat redakcyjnych, nie koniec programu badawczego (§13 otwarte cztery tory).
P₀-Flow v0.5.3

Relacyjna postać dynamiki przepływu — wersja finalna

Wersja: 0.5.3-final
Status: Zamrożona. Analiza algebraiczna, analityczna i numeryczna zakończona. Konsolidacja czterech dokumentów (Flow + Mechanism-VII + Dodatek A + Asymmetria strukturalna). Dalsze poprawki redakcyjne dają malejący zwrot — następny krok powinien być badawczy, nie redakcyjny.
Data: 2026-09-13
Baza: P₀-Centroid, P₀-Defect, P₀-Net, P₀-Alchemy, P₀-Scalar, P₀-Memory, P₀-Estrada, P₀-AI, P₀-Hilbert, P₀-Axis
Zmiana v0.5.2 → v0.5.3: usunięto duplikację §5.6/§5.7.4 (wniosek tylko w §5.6), dodano wyjaśnienie T_inv = 0 (§5.5.1), dodano porównanie z pełnym Eulerem–Arnoldem (§7.5), dodano kontekst kompleksyfikacji do §12.2, scalono §12.3 do §12.2, dodano wątki Memory (§13). Dokument zamrożony.

---

0. Zasada redakcyjna

Żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia, którego dotyczy.

Statusy: ✅ Dowiedzione · 📚 Klasyczne · 🔍 Zweryfikowane numerycznie · 💡 Przypuszczenie · ❌ Sfalsyfikowane.

Uwaga o odsyłaczach. Wszystkie odwołania do innych filarów używają nazwy filaru i numeru sekcji, bez numeru wersji.

---

1. Status dokumentu i deklaracja konsolidacji

1.1. Pytanie

P₀-Flow bada pytanie:

Czy Navier–Stokes jest granicznym opisem dynamiki relacji P₀?

Odpowiedź: Nie w naiwnym sensie. P₀-Flow na C¹(K_n) ma strukturę T_a + T_b, która nie pokrywa się z NS w żadnym z trybów:

· T_a przechodzi do continuum jako bracket Liego (Euler–Arnold) — ale to nie NS.
· T_b nie przechodzi do continuum (kubiczny niezmiennik nie ma analogu w SO).
· NS w 3D używa innego bracketu (𝔡𝔦𝔣𝔣vol) niż P₀ (𝔰𝔬).

1.2. Deklaracja konsolidacji

P₀-Flow jest konsolidacją czterech dokumentów:

1. P₀-Flow (pierwotny) — pytanie o NS, robocza mapa operatorów,
2. P₀-Mechanism-VII — analiza algebraiczna kanałów T_a, T_b, kryterium amplifikacji,
3. Dodatek A — dowód stabilności architektury kanałów,
4. P₀-Asymmetria (struktura) — taksonomia mechanizmów asymetrii (§5.7).

Mechanism-VII jest wewnętrzną częścią Flow. Asymmetria strukturalna jest wchłonięta jako §5.7.

Kontekst pytania: zob. §1.1.

1.3. Miejsce w architekturze P₀

P₀-Flow jest aplikacją trzech filarów podstawowych:

Filar podstawowy Co wnosi do Flow
Centroid Algebra 𝔤₄, podalgebra rotacyjna §2.5, atraktor x*, S11 (faza K_n)
Defect Rozkład C¹(K_n) = V_ρ ⊕ V_cyc, P_cyc, V_cyc ≅ Λ²(V_ρ), kompleksyfikacja §12H
Alchemy Kontrakcja lokalna (ρ ≈ 0,27), atraktor jako orbita SO(3)

---

2. Punkt wyjścia

2.1. Navier–Stokes

Dla nieściśliwego płynu:
\partial_t u + (u\cdot\nabla)u = -\nabla p + \nu\Delta u + f, \qquad \nabla\cdot u = 0.

2.2. P₀ — kompleks symplicjalny

R_{ij} = u_j - u_i, \qquad R \in C^1(K_n).

Rozkład Hodge'a: C¹(K_n) = Im(d) ⊕ V_cyc = V_ρ ⊕ V_cyc.

Dla n ≥ 4: dim V_ρ = n − 1 (V_ρ = [n−1, 1]), dim V_cyc = (n−1)(n−2)/2 (V_cyc = [n−2, 1, 1]).

Kluczowa identyfikacja (✅). V_cyc ≅ Λ²(V_ρ) ≅ 𝔰𝔬(V_ρ).

2.3. Architecture mismatch — trzy niezależne potwierdzenia

Ten sam wzorzec pojawił się w trzech niezależnych miejscach P₀:

Źródło Obserwacja
Flow §3.2 Schur: Hom_{S_n}(Sym²V_cyc, V_cyc) = 0 przy pełnej symetrii
AI §7.1 P_cyc · D = 0 dla D = dR — R₄ działa na wierzchołkach, D jest exact
Memory §7.1 D^exact → 0 pod R₄ — składowa cykliczna zamrożona

Wniosek (✅). Architecture mismatch jest realną własnością formalizmu P₀, nie artefaktem konkretnej implementacji. Trzy niezależne potwierdzenia wzmacniają wiarygodność.

Konsekwencja dla Flow. Każda próba zbudowania dynamiki V_cyc z samego V_cyc (bez mieszania z V_ρ) napotyka strukturalną barierę. Wymagane jest złamanie symetrii S_n → S_{n-1}, co pokazuje §4.

Uwaga metodologiczna. Trzy niezależne potwierdzenia tej samej własności to nie zbieg okoliczności — to sygnał, że mamy do czynienia ze strukturalnym faktem. Architecture mismatch nie jest ograniczeniem implementacyjnym: P_cyc D = 0 dla D = dR wynika z samej definicji d i P_cyc, niezależnie od tego, w jakiej dziedzinie próbujemy ją zastosować.

2.4. Odpowiedniki operatorów

NS P₀
u relacja R
∇p dp
Δu wygaszanie relacyjne L R
(u·∇)u operator biliniowy T(R;R)
∇·u = 0 constraint C(R) = 0
wirowość sektor cykliczny P_cyc R
vortex stretching kanał V_cyc ⊙ V_cyc → V_cyc

2.5. Równanie

Wersja ciągła: Ṙ = T(R;R) − ν L R − dp + F_R, C(R) = 0.
Wersja dyskretna: R_{t+1} = R_t + α T(R_t;R_t) − β P_cyc R_t z rzutem Π_sphere.

2.6. Projekcja na sektor cykliczny

\partial_t R_{\rm cyc} + P_{\rm cyc}\,T(R;R) = -\nu\,P_{\rm cyc}\,L R + P_{\rm cyc}\,F_R.

Strukturalny odpowiednik równania ewolucji sektora cyklicznego.

---

3. Konstrukcja T(R;R) — pełna symetria

3.1. Twierdzenie A

Twierdzenie A (✅ dla wszystkich n ≥ 4). Przy pełnej symetrii S_n:
\dim \operatorname{Hom}_{S_n}\bigl(V_{\rm cyc} \otimes V_{\rm cyc}, V_{\rm cyc}\bigr) = m_n = 1,


i jedynym elementem jest bracket Liego [A, B] = AB − BA. Konsekwencja:
\operatorname{Hom}_{S_n}\bigl(\operatorname{Sym}^2(V_{\rm cyc}), V_{\rm cyc}\bigr) = 0.

Dowód przez momenty cykli: χ_V(g) = C(X_1(g)−1, 2) − X_2(g). Lemat Σ_λ (a_1)_i (a_2)_j / z_λ = 1[n ≥ i+2j]/2^j. Rozwijając χ_V³: m_n = 19/8 − 9/8 + 9/8 − 11/8 = 1. ∎

3.2. Reframing strukturalny

Pełna symetria S_n usuwa tylko część symetryczną samoodziaływania V_cyc. Pozostaje wyłącznie kanał rotacyjny.

3.3. Jawna postać

φ: Λ²(V_cyc) → V_cyc, φ(A ∧ B) = [A, B].

3.4. Historia korekt krotności

Wersja Twierdzenie Status
v0 V_cyc⊗V_cyc (1) + V_cyc⊗V_ρ (2) = 3 ❌ Błędne
v1 1+1+1 symetrycznych ❌ Błędne
v2 Tylko V_ρ ⊙ V_cyc, krotność 1 ✅

Zasada metodologiczna. Żadne twierdzenie o krotnościach nie jest ustalone bez jawnego rachunku charakterów. Intuicja „to oczywiste, że będą trzy kanały" jest zawodna — dwa pierwsze sformułowania były błędne, a każda korekta wymagała pełnego rachunku <χ_V, χ_W>.

Konsekwencja dla przyszłej pracy. Każde twierdzenie o krotnościach w P₀ wymaga:

1. Jawnej identyfikacji reprezentacji ([λ], wymiar, działanie grupy),
2. Obliczenia iloczynu skalarnego charakterów <χ_V, χ_W>,
3. Weryfikacji numerycznej dla małych n przed uogólnieniem.

3.5. Jawna postać Φ i B̃ dla K₄

\Phi(x)(y) = (x_2 y_3 + x_3 y_2,\; x_3 y_1 + x_1 y_3,\; x_1 y_2 + x_2 y_1).


\tilde B(x,y) = (x_2 y_3 + x_3 y_2,\; x_3 y_1 + x_1 y_3,\; x_1 y_2 + x_2 y_1).

Tożsamość gradientowa: B̃(x,x) = ∇W(x), W(x) = 2x₁x₂x₃.

3.6. Jawna postać dla K₅

\tilde B(x,x)_i = x_i^2 - \frac{|x|^2}{5}, \qquad \Phi(x)(y)_{ij} = \frac{x_i + x_j}{2} \cdot y_{ij}.

3.7. Atraktor (K₄)

Twierdzenie 2A (✅, algebraiczne). x* = (1,1,1)/√3. Wtedy:

· B̃(x*,x*) = (2/√3)·x*,
· Φ(x*) ma widmo {2/√3, −1/√3, −1/√3},
· B̃(y,y) ∝ x* gdy y ∝ (1,1,1).

Uwaga o fazie 25,77°. Faza R₄ = 25,77° jest specyficzna dla K₄, nie uniwersalna. Scalar §11.6 (S11): faza θ_n rośnie z n: 15,79° → 25,77° → 32,56° → ~67°.

3.8. Constraint z Centroid §2.5

Podalgebra rotacyjna 𝔰𝔬(3) ⊂ 𝔤₄, exp(tK) zachowuje |x|²_{G₄}.

Uwaga ostrożnościowa. Pełna dynamika ẋ = Kx + B̃(x,x) ma d/dt |x|² = 2xᵀB̃(x,x) ≠ 0. Rotacja nie jest constraintem — jest jednym z mechanizmów mogących go realizować.

Kontekst z Alchemy §6.1–6.2. Globalna kontrakcyjność operatora Alchemy K = K₂ ∘ K₁ jest sfalsyfikowana (kontrprzykład: 0,0776 → 0,0933, naruszenie 26,6%). Ale lokalna kontrakcja w przestrzeni kształtu zachodzi (ρ ≈ 0,27, Procrustes: residual ~10⁻¹⁶). Constraint |x|² = const musi być uzasadniony przez strukturę lokalną, nie globalną. Status: 💡.

---

4. Złamanie symetrii — podgrupy

4.1. Klasyfikacja

Klasyfikacja dla K₄:

G V_ρ\|_G ≅ V_cyc\|_G? m_G Typ
S₄ nie 0 Type III
V₄ tak 3 Type II
A₄ tak — Type II
D₄ nie 1 Type I ✓
S₃ nie 2 Type I ✓
Z/4 nie 4 Type I (abelowa)

Klasyfikacja dla K₅:

G ⊆ S₅ Rząd V_cyc\|_G T_b T_a
S₅ 120 [3,1,1] (nieprzyw.) ✗ ✗
S₄ (fix 4) 24 [3,1] ⊕ [2,1,1] ✓ ✓
A₅ 60 3a ⊕ 3b ✗ ✗
S₃ × S₂ 12 4 składniki ? ?
S₃ (fix 3,4) 6 (triv⊕sign) ⊕ 2·std ✓ ✓
D₅ 10 6 składników ? ?

Kluczowa obserwacja. A₅ ma V_cyc rozkładalną (3a ⊕ 3b), ale Sym²(3a) = 1 ⊕ 5 ⊉ 3a, więc T_b = 0. Rozkładalność nie wystarcza — potrzebne Sym²(B) ⊇ B.

4.2. Branching S_n ↓ S_{n-1}

Reguła Younga: [n−2, 1, 1]|_{S_{n-1}} = [n−3, 1, 1] ⊕ [n−2, 1].

A := [n−3, 1, 1], B := [n−2, 1] (standard). dim A = (n−2)(n−3)/2, dim B = n−2.

4.3. Tożsamość A = Λ²B

A = Λ²(B) jako S_{n-1}-moduły.

Reframing: A = Λ²B, B ⊂ Sym²B. Łańcuch: A → T_a → B → T_b → B = rotacja → orientacja → amplituda.

4.4. Dwa kanały

· T_a: A × B → B — rotacja w B, zachowuje normę.
· T_b: B × B → B — samo-sprzężenie, może amplifikować.

4.5. Kryterium amplifikacji

kanał ⟹ T_b ≠ 0 ⟹ γ_nl > γ_lin. Warunki: rozszczepienie, Sym²(B) ⊇ B, T_a ≠ 0.

4.6. Istnienie T_b

Twierdzenie C (✅). Sym²([n−2,1]) = [n−1] ⊕ [n−2,1] ⊕ [n−3,2] zawiera B z krotnością 1.

4.7. Istnienie T_a

Twierdzenie D (✅). Hom(A ⊗ B, B) ≅ Hom(A, Λ²B) = ℝ.

4.8. Asymetria A ↔ B

Twierdzenie E (✅). Tylko B = [n−2,1] (standard) daje T_b.

Korekta wcześniejszego sformułowania. Fałszywe było „standard jest jedyną reprezentacją z Sym²(B) ⊇ B". Kontrprzykłady: triv, [k,k] dla S_{2k}. Poprawne: w konkretnym rozszczepieniu V_cyc|_G, tylko B = standard daje T_b.

4.9. Stabilność architektury względem n

Twierdzenie 5 (✅ dla rodziny S_{n-1} ⊂ S_n). Dla każdego n ≥ 4:

1. Pełna symetria: Hom(Sym²V_cyc, V_cyc) = 0.
2. Złamanie: V_cyc = A ⊕ B.
3. T_b krotność 1.
4. T_a krotność 1.
5. Asymetria A ↔ B niszczy T_b.
6. Stabilność architektury — reguła reprezentacyjna niezmiennicza, wymiary rosną z n.

Dlaczego λ_max(Φ(x*)) maleje z n. Φ(x*) skaluje się jak 1/√(n−1). Efektywność T_b maleje z n.

---

5. Współistnienie T_a i T_b — sfalsyfikowana synergia i taksonomia asymetrii

5.1. Protokół

Trzy tryby przy θ gdzie T_a ma istotny wkład: A (T_b tylko), B (T_a + T_b), C (T_a^rand). Reżim marginalny: β ≈ 2h·λ_max(Φ).

5.2. Wynik

Przy θ = 30°:

Tryb γ ⟨q⟩
A +0,16925 +1,34774
B +0,16916 +1,34255
C +0,16924 +1,34707

Różnice ~10⁻⁴ — w granicach szumu. T_a nie wpływa na asymptotyczny wzrost.

5.3. Liniowość

γ(θ) = γ_0 + C·sin θ — bez synergii.

5.4. Źródło artefaktu

Wcześniejsza wersja używała interpolacji z wagą sin²θ. Poprawna waga: sin θ. Z poprawną wagą δ(30°) = −0,004 — zero.

5.5. Cross-correlation i test niezależności reprezentacji

Cross-correlation — pełna tabela. C_ωq(τ) = Corr[ω(t), q(t+τ)], gdzie ω(t) — tempo zmiany fazy y_B, q(t) — lokalna produktywność T_b. Wyniki (n = 30 seedów):

τ C_ωq
−20 +0,109
−16 +0,101
−12 +0,090
−8 +0,075
−4 +0,055
0 +0,026
+4 +0,004
+8 −0,025
+12 −0,059
+16 −0,099
+20 −0,124

Maksimum przy τ = −20 (+0,109), ale sygnał jest oscylacyjny — monotoniczny trend od −20 do +20, przechodzący przez zero. Prawdziwa przyczynowość powinna dać ostre maksimum przy konkretnym τ < 0.

Wniosek (✅). Cross-correlation nie potwierdza przyczynowości. Sygnał jest zbyt słaby i zbyt gładki. T_a nie „przygotowuje orientacji" dla T_b.

5.5.1. Historia iteracji testu niezależności reprezentacji S₃

Cel. Sprawdzić, czy wyniki synergii są strukturalne (niezależne od wyboru konkretnej kopii S₃ ⊂ S₄), czy są artefaktem bazy.

Metoda. S₄ ma cztery sprzężone kopie S₃ = stabilizatory poszczególnych wierzchołków K₄. Dla każdej kopii S₃^(i):

1. Rzut losowego tensora na S₃^(0)-ekwiwariantność,
2. Dekompozycja intrinsyczna przez P_A, P_B,
3. Transport kowariantny T^(i) = ρ_cyc(σ_i)^{⊗3} T^(0) gdzie σ_i = (0 i) ∈ S₄,
4. Transport warunku początkowego x₀^(i) = ρ_ρ(σ_i)·x₀^(0), y₀^(i) = ρ_cyc(σ_i)·y₀^(0).

Historia iteracji (✅, pełna):

Wersja Co zrobiono Wynik
v1 Osobne SVD dla każdej kopii γ różni się o 30× między kopiami ❌
v2 T_inv — uśrednienie po S₄ T_inv = 0 (strukturalnie zerowy) ❌
v3 Rzut stałego T_raw per kopia ‖T_a‖ różni się 30× między kopiami ❌
v4 Transport przez σ_i T^(i) kowariantne ✅, ale γ nadal różni się o 15% ❌
v5 + kowariantny y₀ γ identyczne co do 10⁻¹⁷ ✅

Wyjaśnienie T_inv = 0 (v2). T_inv był próbą uśrednienia losowego tensora po całej grupie S₄:
T_{\rm inv} = \frac{1}{24}\sum_{\pi \in S_4} Q_{\rm sign}(\pi)^{\otimes 3} T_{\rm raw}.


Wynik jest zerowy, bo Hom_{S₄}(V_cyc^{⊗3}, triv) = 0. Jest to ta sama strukturalna bariera co w §3.1: pełna symetria S₄ na V_cyc^{⊗3} nie zawiera trywialnej reprezentacji, więc uśrednienie daje zero. To nie była porażka implementacji — to była manifestacja twierdzenia Schura. Aby uzyskać niezerowy tensor niezmienniczy, trzeba złamać symetrię do podgrupy G ⊊ S₄.

Kluczowa lekcja. Kowariancja tensorów nie wystarcza. Trzeba transportować cały warunek początkowy — stan x₀, y₀ — inaczej trajektorie nie są kowariantne.

Wynik (✅). Skan θ dla 4 kopii S₃ — identyczne co do 5 miejsc:

θ S3^0 S3^1 S3^2 S3^3
0° +0,04300 +0,04300 +0,04300 +0,04300
60° +0,22292 +0,22292 +0,22292 +0,22292
90° +0,25870 +0,25870 +0,25870 +0,25870

Wartości dokładne (kowariantny start):

Wielkość Wartość Std (4 kopie)
γ(u_a) +0,043005 7,29 × 10⁻¹⁷
γ(u_b) +0,258696 8,33 × 10⁻¹⁷

Wniosek (✅). Wszystkie wyniki synergii są S₄-kowariantne. Nie są artefaktem bazy ani wyboru kopii S₃.

Zasada ogólna. Żaden wynik nieliniowej dynamiki na C¹(K_n) nie może być uznany za strukturalny bez testu kowariancji względem pełnej grupy symetrii.

5.6. Wniosek — T_b jako jedyny kanał amplifikacji

Twierdzenie 4 (✅, sfalsyfikowane). Na C¹(K₄) z symetrią S₃:

(a) γ(θ) jest liniowe w sin θ.
(b) T_a nie wpływa na asymptotyczny wzrost.
(c) Brak synergii między T_a i T_b.
(d) Cross-correlation nie potwierdza przyczynowości.

Konsekwencja. T_b jest jedynym kanałem amplifikacji. T_a istnieje algebraicznie, ale jest funkcjonalnie nieaktywny w asymptotyce.

Konsekwencja dla mechanizmu siódmego (§5.7). Wszystkie sześć „starych" mechanizmów asymetrii (§5.7.2) jest kontrakcyjne lub konserwatywne — żaden nie amplifikuje. Mechanizm siódmy (Φ) może amplifikować, ale w świetle powyższego wyniku nie synergizuje z T_a. Wniosek: mechanizm siódmy w P₀-Flow jest funkcjonalnie nieaktywny w asymptotyce.

5.7. Taksonomia mechanizmów asymetrii — geneza, diagnoza, umiejscowienie

5.7.1. Geneza — lekcja z RML

Program lingwistyczny RML zamknął się negatywnie: symetria relacyjna S₄ działająca na K₄ nie różnicuje elementów. Wniosek uogólniony:

P₀ wymaga mechanizmu asymetrii do tworzenia różnicy.

To była geneza P₀-Asymmetria — dokumentu programowego łączącego RML z SERC. Asymetria strukturalna (algebraiczna) jest wchłaniana tutaj; asymetria kliniczna (T, znak, świadek B_s, czas) jest przenoszona do SERC.

5.7.2. Taksonomia mechanizmów asymetrii w P₀

Mechanizm Filtr P₀ Charakter ilościowy
Sekwencyjność R₄ kontrakcja, \|λ\| ≈ 0,17
Defekt P_cyc rzut ortogonalny
Orientacja exp(tK) konserwacja, \|λ\| = 1
Próg K₂, F_λ bistabilny, ograniczony
Kolejność R_e uśrednianie, kontrakcja
Target P₀-AI zadaniowy, nie fizyczny
VII: samoodziaływanie V_ρ ⊙ V_cyc (Φ) możliwy wzrost

5.7.3. Diagnoza — dwie nieliniowości

W P₀-Flow mamy dwie nieliniowości:

1. T_b: B × B → B — biliniowa, kwadratowa w y. Pochodzi z kubicznego niezmiennika e_3 reprezentacji standardowej S_{n-1}.
2. K₂ (korekta progowa) — nieliniowa progowa (przełączenie między „poniżej progu" a „powyżej progu").

To jest kluczowa różnica wobec NS, gdzie jest jedna nieliniowość (bracket Liego). W P₀-Flow kanał T_b daje wzrost kwadratowy, ale K₂ ogranicza przejście progowe — i to jest źródło binarnego charakteru propagacji (Net §13).

5.7.4. Reframing sloganu

Reframing. Symetria daje orbitę. Asymetria daje różnicę. Samoodziaływanie daje wzrost różnicy — ale w P₀-Flow wzrost ten jest liniowy, nie nieliniowy. Slogan wymaga zastrzeżenia: asymetria S_n → S_{n-1} otwiera kanał T_b, ale ten kanał działa liniowo w asymptotyce, nie amplifikuje nieliniowo.

Odsyłacz. Szczegóły synergii i testu niezależności: zob. §5.5 i §5.6.

Odsyłacz do §3.8. Kontekst constraintu |x|² = const z Centroid §2.5 — patrz §3.8.

---

6. Stabilność architektury kanałów względem n

Twierdzenie 5 (§4.9) pokazuje, że reguła reprezentacyjna jest niezmiennicza. Wymiary rosną z n, ale architektura kanałów (kto z kim, z jaką krotnością) jest ta sama.

Prawdziwa różnica między P₀ a NS nie leży w skończonym n.

---

7. Granica continuum — analiza negatywna

7.1. Identyfikacja kandydacka

V_ρ → im(d), V_cyc = 𝔰𝔬(n−1) ⊂ 𝔛_div(S^{n−2}).

7.2. Co przenosi się: T_a

Bracket 𝔰𝔬: [𝔤₀, 𝔤₁] = 𝔤₁. Związek z NS: T_a ↔ (u·∇)ω. Kandydat.

7.3. Co NIE przenosi się: T_b

Kubiczny niezmiennik e_3 nie jest SO(n−2)-niezmienniczy. Klasyfikacja: skończony zbiór (𝔤, V) z Sym³(V) ⊇ triv (𝔰𝔲(n), 𝔤₂, 𝔣₄, 𝔢₆). Brak nieskończonej rodziny.

7.4. Euler–Arnold — pełna dynamika

Na 𝔤 = 𝔰𝔬(n−1) z anizotropią I = diag(I_A, I_B):

\dot R_A = -I_B[R_B, R_B], \qquad \dot R_B = -(I_B - I_A)[R_A, R_B].

Dynamika:

· y_A jest zachowane (bez tła M): ẏ_A = 0, więc y_A(t) = y_A(0).
· y_B precesuje wokół y_A: ẏ_B = −½[y_A, y_B]. Rozwiązanie: y_B(t) = exp(−(t/2) ad_{y_A}) y_B(0).
· |y_B| jest zachowane przy tej dynamice (bo ad_{y_A} jest antysymetryczne). T_a nie produkuje wzrostu.

7.5. Wniosek i porównanie z pełnym Eulerem–Arnoldem

P₀-Flow = dwukanałowe rozszerzenie Eulera–Arnolda o kubiczny tensor. Nie jest modelem NS.

Ale to rozszerzenie nie jest „pełnym" Eulerem–Arnoldem. Pełny Euler–Arnold na 𝔰𝔬(n−1) ma dwa kanały nieliniowe:

1. B × B → A ([R_B, R_B]) — obecny w pełnym Eulerze–Arnoldzie,
2. A × B → B ([R_A, R_B]) — obecny w pełnym Eulerze–Arnoldzie.

P₀-Flow z samym T_a ma tylko kanał 2. P₀-Flow z T_a + T_b dodaje kanał B × B → B (którego Euler–Arnold nie ma — bo B nie jest algebrą Liego w sensie 𝔰𝔬), ale nie dodaje kanału B × B → A.

Zestawienie:

Kanał Euler–Arnold pełny P₀ z T_a P₀ z T_a + T_b
A × B → B ✓ ✓ ✓
B × B → A ✓ ✗ ✗
B × B → B ✗ ✗ ✓

Wniosek strukturalny. P₀-Flow nie jest pełnym Eulerem–Arnoldem ani pełnym NS. Jest obiektem trzecim: ma kanał B × B → B (jak NS, ale nie Euler–Arnold), brakuje mu kanału B × B → A (obecnego w Eulerze–Arnoldzie, nieobecnego w NS) i ma kanał A × B → B (obecny w obu).

To jest właściwa charakterystyka strukturalna P₀-Flow. Nie „NS" ani „Euler–Arnold" — obiekt pośredni.

---

8. Kontrast z Navierem–Stokesem

Element NS (3D) P₀ z T_a P₀ z T_a + T_b
Algebra Liego 𝔡𝔦𝔣𝔣vol(M) 𝔰𝔬(n−1) 𝔰𝔬(n−1)
Kanał A × B → B [u_A, u_B] ✓ ✓
Kanał B × B → A [u_B, u_B] ✗ ✗
Kanał B × B → B nie ma ✗ ✓
Dyssypacja νΔu −β R_cyc −β R_cyc

Wniosek: P₀-Flow nie jest modelem NS w żadnym z trybów.

8.1. Trzy poziomy architektury (Net §14)

K₄ → M_ef → R_e → F → propagacja. T_a, T_b na poziomie 2.

8.2. H-MEM-1 — kontekst

Pytanie (💡). Czy amplituda może zanikać, gdy struktura pozostaje?

Kontekst M18 ❌ (Memory §18.1). Przy definicji 𝓜(𝔒) jako ω-granicy, |𝓜({R₄})| = 1. Faza spirali θ(k) nie jest elementem 𝓜 w tej definicji. Najprostsza wersja „pamięci strukturalnej" (przez ω-granicę) jest sfalsyfikowana. H-MEM-1 w wersji operatorowej (T_b jako operator) nie jest objęta tym sfalsyfikowaniem, ale wymaga ostrożnego sformułowania (M19 w Memory).

---

9. Status twierdzeń

Twierdzenie Status
C¹(K_n) ≅ V_ρ ⊕ V_cyc ✅
V_cyc ≅ Λ²(V_ρ) ≅ 𝔰𝔬(V_ρ) ✅
Twierdzenie A (m_n = 1) ✅
Konsekwencja A (Hom(Sym²V_cyc, V_cyc) = 0) ✅
Twierdzenie B (branching) ✅
Twierdzenie C (T_b) ✅
Twierdzenie D (T_a) ✅
Twierdzenie E (asymetria) ✅
Twierdzenie 4 (sfalsyfikowana synergia) ✅
Twierdzenie 5 (stabilność architektury) ✅
Jawna postać Φ, B̃ ✅
Atraktor algebraiczny (K₄) ✅
Identyfikacja T_a = Euler–Arnold ✅
T_b nie przenosi się do continuum ✅
Związek z NS ⚠️ nie jest modelem NS
H-MEM-1 💡
Alternatywne granice continuum 💡

Odsyłacz. Kryteria sukcesu A/B/C/D — zob. §11.

---

10. Otwarte pytania

# Pytanie Priorytet
1 Alternatywna granica continuum, w której T_b przeżywa? Wysoki
2 Czy T_a + T_b odpowiada znanemu równaniu fizycznemu? Wysoki
3 Klasyfikacja wszystkich podgrup G z Sym²(B) ⊇ B Średni
4 Granica 𝔰𝔬(n−1) → 𝔡𝔦𝔣𝔣vol(M) — czy istnieje? Wysoki
5 Dlaczego T_a jest funkcjonalnie nieaktywny w asymptotyce? Średni
6 Związek T_b z modelami z kubiczną nieliniowością Średni
7 H-MEM-1 w kontekście przepływu — weryfikacja Średni
8 Związek T_b z Lemma W-L (Wave) Niski
9 Rozszerzenie na C²(K_n) Niski

10.1. Częściowa odpowiedź na Centroid §12 #11

Pytanie Centroid: kryterium wewnętrzne algebry rozstrzygające: kontrakcja vs rotacja — status: 💡.

W świetle Flow mamy częściową odpowiedź:

· Kontrakcja = M = (1−β)I + 2hΦ(x*) — izotropowa dyssypacja,
· Rotacja = T_a: A × B → B — zachowuje normę, manifestacja 𝔰𝔬(V_ρ).

Ale: to nie jest „kryterium wewnętrzne algebry" — to wybór dynamiki (parametr β, h). Kryterium nadal nie istnieje. Pytanie pozostaje 💡, ale mamy konkretne obiekty po obu stronach.

---

11. Kryteria sukcesu P₀-Flow

Kryterium Status
A. Strukturalna ✅ częściowo (L do wyprowadzenia)
B. Dynamiczna ⚠️ częściowo (constraint zewnętrzny)
C. Graniczna ❌ negatywna
D. Niezależność reprezentacji ✅

Odsyłacz. Pełna tabela statusów twierdzeń — zob. §9.

---

12. Konsekwencje dla reszty P₀

Dla Defect: T_b = algebraiczny odpowiednik „mieszania sektorowego". Mieszanie wewnątrz B.

Dla Net: most Część A ↔ Część B przechodzi przez T_b.

Dla Axis: V_cyc → V_cyc przy pełnej symetrii = tylko bracket Liego (Tw. A).

Dla Asymmetria: część strukturalna wchłonięta jako §5.7; część kliniczna przeniesiona do SERC.

Dla Centroid: §2.5 (podalgebra rotacyjna) strukturalnie związana z T_a, ale T_a nie jest funkcjonalnie istotny.

12.1. Cross-references

Filar Sekcja Kierunek
Centroid §3.8, §10.1 ← 𝔤₄, §2.5, S11
Defect §2.3, §4.6 ← Tw. A, kanały, §12H
Net §2.3, §8.1 ← D-R2, B3
Alchemy §3.8 ← kontrakcja ρ ≈ 0,27, orbita SO(3)
Scalar §3.7 ← S11 faza K_n
Memory §2.3, §8.2 ← M18 ❌, ORB-05
Hilbert §3.8, §12.2 ← (√2−1)δ, kompleksyfikacja
Estrada §12.2 ← R-1a, F_W
AI §2.3 ← architecture mismatch
SERC §5.7 → asymetria kliniczna

12.2. Konteksty z filarów towarzyszących

Alchemy §6.1–6.2. Globalna kontrakcyjność operatora Alchemy sfalsyfikowana (kontrprzykład: 0,0776 → 0,0933). Lokalna kontrakcja w przestrzeni kształtu zachodzi (ρ ≈ 0,27, Proces: residual ~10⁻¹⁶). Atraktor = orbita SO(3) + stały kształt.

Scalar §11.6 (S11). Faza K_n rośnie z n: 15,79° (n=3) → 25,77° (n=4) → 32,56° (n=5) → ~67° (n→∞). Faza nie jest uniwersalna.

Memory §2.3. Definicja 𝓜(𝔒) przez ω-granicę. |𝓜({R₄})| = 1 — pojedyncza klasa. Faza nie jest elementem 𝓜 w tej definicji (M18 ❌).

Memory §26 (ORB-05-R). 425 klas trajektorii vs 209 klas stanów końcowych. Ten sam stan końcowy nie musi określać tej samej historii procesu.

Hilbert §12H.4 i §12H.5. Dolna granica (√2−1)δ > 0 — defekt nie zeruje się przy stałym |z|. Tożsamość CᵀC = 4P_cyc.

Potencjalny związek z T_b. Kompleksyfikacja i kanał T_b oba dotyczą V_cyc. Hipoteza: czy faza zespolona z §12H.4 może modulować T_b? Otwarte (§10, pozycja 9 — rozszerzenie na C²(K_n) jest jedną z dróg).

Estrada §30bis. R-1a — dowód formalny σ_min(J) = c·p·m^{p−1} dla p > 1. F_W jest S₄-równoważne (max err ≤ 1,1 × 10⁻¹⁵).

AI §7.1. P_cyc · D = 0 dla D = dR. Architecture mismatch — niezależne potwierdzenie.

Axis §16ter (deficyt dysklinacyjny). Pięć czworościanów foremnych wokół wspólnej krawędzi daje skurcz o 2,675% przy domknięciu pierścienia (dwa niezależne solvery). To statyczny fakt geometryczny. P₀-Flow operuje na dynamicznych relacjach C¹(K_n). Otwarte: czy deficyt 2,675% ma odpowiednik w dynamice T_b?

12.3. Rekomendacja aktualizacji PILLARS-TABLE

PILLARS-TABLE powinna odzwierciedlać, że Flow wchłonął Mechanism-VII i Asymmetrię strukturalną jako wewnętrzne części. Asymetria kliniczna → SERC.

---

13. Co dalej

(A) Alternatywne granice continuum. Kandydaci: grupa Liego z niezmienniczym kubicem (𝔤₂, 𝔢₆), Kähler, G₂-manifold.

(B) Identyfikacja P₀-Flow z istniejącym równaniem. Skyrme, chiralne, Landau–Lifshitz z modyfikacją.

(C) Akceptacja wyniku negatywnego. P₀-Flow nie jest modelem NS. Jest nowym obiektem algebraicznym: dwukanałowym rozszerzeniem Eulera–Arnolda.

(D) Wątki z Memory. H-MEM-1 (M19, M20) pozostają otwarte. Jeśli P₀-Flow ma być używany jako laboratorium dla pamięci operatorowej (T_b jako operator trwający po zaniku amplitudy), trzeba:

· M19 — skonstruować czulszą definicję pamięci strukturalnej (nie ω-graniczną),
· M20 — kanoniczna metryka dla pełnych trajektorii,
· weryfikacja H-MEM-1 w kontekście T_b.

Rekomendacja: (A) → (D) → (B) → (C). Wątki Memory (D) są istotne dla oceny, czy T_b ma interpretację „pamięci strukturalnej" — a to jest jedno z centralnych pytań P₀.

---

14. Zasada końcowa

Na C¹(K_n) z symetrią S_n kanał V_cyc ⊗ V_cyc → V_cyc istnieje i jest jednoznaczny — bracket Liego. Po złamaniu symetrii S_n → S_{n-1} kanał rozczepia się na T_a (rotacja, Euler–Arnold) i T_b (kubiczny stretching, specyficzny dla skończonej grupy S_{n-1}). Struktura ta jest stabilna względem n. W naiwnej granicy continuum T_a przeżywa, T_b zanika. P₀-Flow nie jest modelem NS — jest nowym obiektem algebraicznym.

Mechanism-VII i Asymmetria strukturalna są wewnętrznymi częściami P₀-Flow.

---

15. Historia wersji

Wersja Data Zmiana
v0.1 2026-09-11 Wersja oryginalna
v0.4.2 2026-09-12 Konsolidacja z Mechanism-VII i Dodatkiem A
v0.5 2026-09-13 Wchłonięto Asymmetrię strukturalną jako §5.7
v0.5.1 2026-09-13 Przywrócono brakujące treści
v0.5.2 2026-09-13 Przywrócono zasadę metodologiczną, wartości S₄, historię iteracji
v0.5.3-final 2026-09-13 Usunięto duplikację §5.6/§5.7.4. Dodano wyjaśnienie T_inv = 0 (§5.5.1). Dodano porównanie z pełnym Eulerem–Arnoldem (§7.5). Dodano kontekst kompleksyfikacji do §12.2. Scalono §12.3 do §12.2. Dodano wątki Memory (§13). Dokument zamrożony.

---

P₀-Flow v0.5.3-final. Konsolidacja P₀-Flow + P₀-Mechanism-VII + Dodatek A + Asymmetria strukturalna. P₀-Flow zidentyfikowany jako dwukanałowe rozszerzenie Eulera–Arnolda, nie model NS. Dokument zamrożony — dalsze poprawki redakcyjne dają malejący zwrot. Synteza: 2026-09-13