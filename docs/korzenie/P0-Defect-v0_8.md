# Korzeń: P₀-Defect — adnotacja (v0.8-formal-draft, 2026-09-13)

**Dokument filarowy:** „P₀-Defect v0.8 — Defekt Relacyjny w C¹(K_n): struktura kanałów, samoodziaływanie i kompleksyfikacja" (formal-draft, 2026-09-13). Filar łączący serii P₀: od struktury lokalnej (C¹(K₄)) do propagacji sieciowej (Net). **Okres:** VIII–IX 2026 (v0.1 i v0.5 od 2026-08-23; konsolidacje v0.6–v0.8 w IX), przed warsztatem. **Wchłonięcia deklarowane wprost:** §12A–§12G z P₀-Flow, §12H = P₀-Hilbert (całość), Axis i Scalar wchłonięte wcześniej do Centroid — przy ewentualnych wpięciach Flow/Hilbert/Axis rozliczyć konsolidację, nie duplikować treści. **Docelowi odbiorcy deklarowani:** Net odwołuje się do §1–§11 jako fundamentu. **Zasada repo:** adnotacja szefa lab. + pełny dokument verbatim (wzorzec poprzednich korzeni). **Uwaga redakcyjna:** wiersz v0.8 w tabeli historii wersji (§16) jest przerwany w oryginale (cytat „tabela widm" z niedomkniętym znacznikiem kodu); zachowane verbatim; dokument kończy się bez końcowego znaku nowej linii.

## Co bada ten korzeń

Defekt całkowalności relacji: D ∈ C¹(K₄) ≅ ℝ⁶ jest exact, gdy istnieje potencjał x ∈ C⁰(K₄) z D_ij = x_i − x_j (D ∈ Im(d)); w przeciwnym razie — defekt relacyjny. Struktura: C¹(K₄) = Im(d) ⊕ V_cyc, obie dim 3; kanoniczna identyfikacja V_cyc ≅ Λ²(V_ρ) ≅ 𝔰𝔬(V_ρ). Kanoniczny defekt Δ(D) = ‖P_cyc D‖ (P_cyc = I − dd⁺), rozdzielony strukturalnie od kwantytacji wymagającej metryki (C(D) = 0 i wzorzec 24/64 — strukturalne; Δ i δ√3 — ilościowe). Dwuwarstwowość jawnie: warstwa strukturalna trzyma się nad GF(2,3,5,7,11); warstwa ilościowa wymaga ℝ i porządku.

## Najmocniejsze (✅ w konwencji dokumentu)

- **Rozkład z podpisaną reprezentacją S₄:** C¹(K₄) ≅ V_std ⊕ (V_std ⊗ sign), Im(d) ≅ V_std, V_cyc ≅ V_std ⊗ sign — „exact = wektor, cykliczność = pseudowektor"; uśredniony projektor S₄ na V_cyc jest macierzą zerową (nierozkładalność).
- **Geometria defektu:** 24 realizowalne wzorce znaków (z 64) mają Δ(D_*) = δ dokładnie; rzut na V_cyc daje 6 kierunków oktaedru (stabilizatory C₄, Grama {+1, 0, −1}); V₄ = trzy ortogonalne osie 180° — te same osie co pary przeciwległych krawędzi (P_cyc(e,f) = 0 dokładnie dla trzech par przeciwległych; kombinatoryka K₄, nie geometria rysowania).
- **Twierdzenie A (m_n = 1 dla wszystkich n ≥ 4):** w pełnej symetrii S_n jedyny S_n-ekwiwariantny kanał V_cyc ⊗ V_cyc → V_cyc to bracket Liego; Hom(Sym²V_cyc, V_cyc) = 0. Dowód przez momenty cykli (charaktery, EGF, liczby Bella, momenty Poissona ½) + weryfikacja dokładna Fraction dla n = 4..20.
- **Architektura kanałów po złamaniu symetrii do S_{n−1}:** V_cyc = A ⊕ B z tożsamością A = Λ²B; dwa kanały: T_a (rotacja) i T_b (samosprzężenie, kandydat do amplifikacji); kryterium otwarcia Sym²(B) ⊇ B; klasyfikacja Type I/II/III dla podgrup K₄ i K₅ (D₄ i S₃ — Type I z otwarciem kanału; V₄/A₄ = Type II: złamanie znosi rozróżnienie sektorów, nie otwiera kanału); stabilność architektury względem n (λ_max(Φ) maleje z n, skalowanie 1/√(n−1)).
- **Wynik negatywny dla continuum:** kubiczny niezmiennik e₃ nie jest SO-niezmienniczy; T_b nie przenosi się naiwnie do granicy S_{n−1} → SO(n−2) (skończona lista par z kubicem: 𝔰𝔲(n), 𝔤₂, 𝔣₄, 𝔢₆). P₀-Flow = dwukanałowe rozszerzenie Eulera–Arnolda o kubiczny tensor, nie model NS (T_a ↔ (u·∇)ω tylko kandydatem).
- **Granica łączna wieży hierarchii (✅):** Δ^(L) = λ_L δ dokładnie (bez reszty, czysto algebraicznie: D_L = d(x^(L)) ⇒ P_cyc(D_L) = 0); miękki próg F_λ ma podłogę λδ, twardy δ; klasyfikacja remisów (0 remisów → λδ; dokładnie 1 → λδ/√2; ≥ 2 → 0); tempo zbieżności = tempo λ_L → 0 niezależnie od ε_L. Odporność sektora cyklicznego na zagnieżdżanie; ucieczka tylko przez koincydencję poziomów, nie symetrię statystyczną (0/5 prób).
- **Sprzężenie międzywęzłowe:** D-R1 (Δ_R = |D_e^B − D_e^A|/(2√2)); uogólnienie D-R3 przez kanał projekcyjny K_S z kernelem Im(d) ∩ ℝ^S (kierunek „ślepy" ⟺ rozszerzony zerami jest exact) i pełną tabelą widm P_cyc|_S dla 9 klas S (wyczerpująco do automorfizmu S₄), w tym pełna synchronizacja: dim ker = 3, defekt jest zjawiskiem częściowego współdzielenia.
- **Kompleksyfikacja §12H (wchłonięty P₀-Hilbert):** G = P_cyc ⊗ ℂ hermitowski idempotentny; tożsamość operatorowa CᵀC = 4P_cyc (cykle trójkątowe, singular values [2,2,2]) ✅; wynik główny: min Q_H = (√2 − 1)²δ² na torusie jednorodnych amplitud (3796/5000 L-BFGS-B + Differential Evolution 10⁻¹²) — 🔍 do zamknięcia analitycznego; wniosek strukturalny ✅: T_δ ∩ Im(d_ℂ) = ∅ — fazy względne modulują defekt, nigdy nie zerują go przy zachowanych modułach; jawnie: to nie własność kwantowa, to geometria torusa względem podprzestrzeni exact.

## Koncesje i sęki (obalenia — trwałe)

- **§5.1 — historia błędu reprezentacji S₄:** wersja 1 ⊕ V_std ⊕ V₂ z nieskierowanej reprezentacji permutacyjnej odrzucona; sygnałem był test równoważności d(π·x) = π·d(x), który nie przechodził. Zasada sformułowana: żadne twierdzenie o rozkładzie reprezentacyjnym bez testu równoważności na reprezentacji znakowanej. Wzorzec uczenia się na własnym błędzie sprzed warsztatu (proto-Z0).
- **§12B.5 — historia korekt krotności:** v0 (m = 3) ❌, v1 (1+1+1 symetrycznych) ❌, finalna (1, bracket) ✅. Zasada: żadne twierdzenie o krotnościach bez jawnego rachunku charakterów.
- **❌ „miękki próg → Δ→0 przy ε→0":** błąd wymierności granic cząstkowych — przekrój (λ→0, wejście stałe) to inna oś niż (ε→0, λ stałe). Wynik 3 §12.3: podłoga λδ dla λ > 0.
- **❌ „standard jedyny z Sym²(B) ⊇ B":** kontrprzykłady trivial i [k,k] dla S_{2k}; poprawnie: w konkretnym rozszczepieniu V_cyc|_G tylko B = standard daje T_b (Tw. E).
- **❌ „P_cyc = ½ blockdiag(I₂,I₂,I₂)":** (½I)² ≠ ½I; poprawnie: diagonalne wewnątrz par przeciwległych, korelacje ±¼ między parami.
- **Korekta δ√3 / δ√5 w wieży:** nie stosuje się do hierarchii — wieża produkuje różnice potencjałów, więc wzorzec zawsze realizowalny; δ_eff(L) ≡ δ (Wynik 2: 270/270 bez wyjątku, ε do 10⁻⁹).
- **Tw 4a domyka dosłowne „p₀ w p₀" jako trywialność** (dwupoziomowa identyczność nieodróżnialna od jednego globalnego stanu stałego); otwarte zostają: Wynik 1 §12.3 🔍 (zanik rozrzutu potencjałów std ∼ 0,6^L) i H-Bridge v0.3 💡.

## Struktury odkryte (🔍/💡)

- **Lokalność czarnej dziury (Obserwacja 4b, 💡):** węzeł w pełni skonsensusowany wewnętrznie może być punktem różnicy widzianym z zewnątrz — dokładnie D-R1 na styku dwóch exactów. Treść nie w „p₀ w p₀", lecz w „p₀ na poziomie k, defekt na poziomie k+1".
- **Odkrycia 1–3 H-Bridge ✅:** d jest S₄-ekwiwariantne; V_ρ ≅ Im(d) kanonicznie; ale lokalność Centroidu (M_v zmienia jeden wierzchołek) nie przechodzi przez d na lokalność Defectu (zmiana wszystkich krawędzi incydentnych z v) — bezpośredni izomorfizm dynamik nie zachodzi.
- **Trzy warianty modelu progowego:** Net-L (diagonalny: ❌ propagacja), Net-G (sektorowy + twardy próg: ✅ wszystko-albo-nic), Net-I (ciągły F_λ: ✅ proporcjonalnie do λ); wniosek kluczowy ✅: binarność przejścia jest artefaktem twardego progu, nie kanału.
- **„Rotacja → orientacja → amplituda"** — łańcuch A → T_a → B → T_b → B w języku P₀ (reframing strukturalny §12D.1).

## Mosty do pnia i warsztatu (odczytanie interpretacyjne, 💡)

- **Do P₀-AI (zamknięcie zależności):** P₀-AI §8.1 wskazuje Defect jako źródło P_cyc i V_cyc — tu pełna struktura: sektor exact = Im(d); tożsamość P_cyc·D = 0 z P₀-AI to sektor exact tego dokumentu; „architecture mismatch" M16/GDG = rozłączność Im(d) ⊕ V_cyc. Ta sama P_cyc, ten sam operatorski język.
- **Do P₀-Wave:** dokument pracuje w V_ρ (przestrzeń trylogii) i V_cyc ≅ 𝔰𝔬(V_ρ); T_a związane z podalgebrą 𝔰𝔬(3) ⊂ 𝔤₄ (Centroid §2.5) — kanał rotacyjny Defectu żyje w tej samej algebrze co słowa Wave; most skręcony znakiem z P₀-AI (V_ρ → V_cyc przez ⊗ sign) ma tu swoją reprezentacyjną treść: V_std ⊗ sign.
- **Rodzina S₄ i oktaedr, po raz kolejny:** podpisana reprezentacja (tu), stabilizator Σ w O(3) = S₄ (Wave), Aut(𝔤₄;{Mᵢ}) ≅ S₄ (Centroid v5.2 §8.1), orbita 24 atraktora (Alchemy) — teraz z geometrią oktaedru V_cyc (6 kierunków, stabilizatory C₄, trzy osie 180° grupy V₄). Do zestawienia w atlasie pnia z wynikiem stella octangula (osmiościan jako wnętrze pary przenikających się K₄): oktaedr pojawia się tu jako struktura sektora defektu.
- **Do P₀-Relacje:** aksjomat „relacja może być całkowalna albo posiadać defekt" jest przykładową formalizacją relacji jako poziomu pierwotnego (R) — defekt jako własność relacji, nie wierzchołków.
- **Pre-echo Z1 (replikacja niezależna):** §12H.9 deklaruje, że kompleksyfikacja może być zweryfikowana autonomicznie przez bezpośredni rachunek z macierzy d i P_cyc — dokument projektuje własną replikowalność niezależną od innych filarów; §12H.10 — jawna lista pułapek („to nie QM", „minimum numeryczne ≠ globalne") jako gotowa bramka sanity dla replikatora. Zasada redakcyjna §0 i odsyłacze „filar + sekcja, bez numeru wersji" — duch Z2 i higiena SSOT.
- **Do P₀-Net (kolejny korzeń):** §10–§11 i tabela trzech wariantów to bezpośredni fundament propagacji; pytanie otwarte nr 16 (interpretacja K_S w pełnej dynamice sieciowej) — most wprost.

## Sęk-odnogi (bank nasion z korzenia)

1. **Wysokie priorytety (§14):** efektywny operator na V_cyc dla sieci (nr 3), addytywność defektu na łańcuchu >2 węzłów (nr 4), alternatywna granica continuum z przeżyciem T_b (nr 7; kierunek G₂), klasyfikacja wszystkich podgrup z Sym²(B) ⊇ B (nr 8), granica 𝔰𝔬(n−1) → pola dywergencji na M (nr 9).
2. **Kompleksyfikacja (§12H.7):** dowód analityczny globalności (√2−1)δ (nr 11), jedyność konfiguracji faz (nr 12), niejednorodne ρ (nr 13, 🔍), √2−1 w metryce G₄ (nr 14), ewolucja unitarna (nr 15).
3. **Reszta:** T_a z komutatorów [ρ(M_i), ρ(M_j)] (§12C.7), związek z modelami kubicznymi Skyrme (nr 10), interpretacja 1/(2√2) (nr 5), rozkład S₄ nad GF(2)/GF(3) (nr 6).
4. **Skala (hipoteza H-Bridge v0.3):** lokalna algebra nie generuje globalnych korelacji wymaganych przez rozkład Schura; sieć R lub mieszanie sektorowe jako źródło nielokalności — do rozliczenia z Net i mechanizmami blokowymi warsztatu.

## Statusy: mapa legendy na konwencje warsztatu

Legenda identyczna z Alchemy/Wave/P₀-AI (✅ Dowiedzione · 📚 Klasyczne · 🔍 Zweryfikowane numerycznie lub symbolicznie · 💡 Przypuszczenie · ❌ Sfalsyfikowane). Mapowanie na Z1: większość „✅" tego dokumentu to twierdzenia z jawnymi dowodami algebraicznymi (rachunek charakterów, pseudoodwrotność, tożsamości operatorowe) — pełnoprawne kandydaty do niezależnej replikacji warsztatowej; wyniki „✅" czysto numeryczne (Fraction n ≤ 20, 270/270) traktować jako mocne 🔍 warsztatowe do ponownienia; minimum (√2−1)δ ma własny status 🔍 jawny; §13 i tabela §15 sumują, co wynikiem a co hipotezą — wzorcowa samoświadomość dokumentu.

P₀-Defect v0.8

Defekt Relacyjny w C¹(K_n) — struktura kanałów, samoodziaływanie i kompleksyfikacja

Wersja: 0.8-formal-draft
Status: ✅ Klasyfikacja podgrup i twierdzenie o znikaniu — dowiedzione dla wszystkich n ≥ 4. Twierdzenie o stabilności architektury kanałów. Wynik negatywny dla granicy continuum. Kompleksyfikacja (wchłonięta z P₀-Hilbert).
Data: 2026-09-13
Baza: P₀-Centroid, P₀-Axis (wchłonięte do Centroid), S4-Rep, P₀-Flow (konsolidacja)
Zmiana v0.7 → v0.8: przywrócono brakujące sekcje (historia błędu S₄ §5.1, pełna tabela widm P_cyc|_S §9.2, pełne Odkrycie 4 §12.1–§12.3 z Wynikiem 3, pułapki metodologiczne §12H.10). Usunięto redundancje przez odsyłacze (§12H.1 → §2.1, §12 Odkrycie 2 → §6, §8 → §12C.4, §12G.1 → §12A, §5 → §12C). Zaktualizowano numerację (Miejsce w architekturze przeniesione do §0.5).

---

0. Zasada redakcyjna

Żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia, którego dotyczy.

Statusy: ✅ Dowiedzione · 📚 Klasyczne · 🔍 Zweryfikowane numerycznie lub symbolicznie · 💡 Przypuszczenie · ❌ Sfalsyfikowane.

Uwaga o odsyłaczach. Wszystkie odwołania do innych filarów używają nazwy filaru i numeru sekcji (np. „Centroid §8"), bez numeru wersji — wersje zmieniają się, odsyłacze strukturalne nie.

---

0.5. Miejsce w architekturze filarów

P₀-Defect jest filarem łączącym serii P₀ — od struktury lokalnej (C¹(K₄)) do propagacji sieciowej (Net).

Relacja do innych filarów:

· Centroid — ten sam graf K₄, ale na poziomie wierzchołków (ℝ⁴). §12 pokazuje kanoniczny most. Axis i Scalar wchłonięte do Centroid.
· Wave — dynamika słów operatorowych.
· Net — odwołuje się do §1–§11 tego dokumentu jako fundamentu.
· Flow — wchłonął z Defect definicje V_cyc, P_cyc, Λ²(V_ρ); Defect odzyskuje z Flow wyniki o strukturze kanałów (§12A–§12G).
· Hilbert — wchłonięte jako §12H.

Zasada niezależności. Ten dokument opisuje wyłącznie strukturę jednego lokalnego węzła — grafu K₄ i przestrzeni jego relacji C¹(K₄).

---

1. Aksjomat filaru

Relacja może być całkowalna, albo posiadać defekt całkowalności.

Dla grafu K₄: D ∈ C¹(K₄) ≅ ℝ⁶.

Relacja jest exact, jeśli istnieje potencjał x ∈ C⁰(K₄) ≅ ℝ⁴ taki, że D_{ij} = x_i − x_j. W przeciwnym razie D ∉ Im(d) — defekt relacyjny.

---

2. Sektor exact i cykliczny

Fakt (✅). dim C¹(K₄) = 6, dim C⁰(K₄) = 4, ker d = ⟨1⟩ ⇒ dim Im(d) = 3.

C^1(K_4) = \operatorname{Im}(d) \;\oplus\; V_{\rm cyc}, \qquad \dim V_{\rm cyc} = 3.

Kluczowa identyfikacja (✅). V_cyc ≅ Λ²(V_ρ) ≅ 𝔰𝔬(V_ρ).

2.1. Niezależność od ciała

Twierdzenie (✅, wyczerpująco na GF(2,3,5,7,11)). Rangowo-strukturalna treść §1–§2 trzyma się identycznie nad każdym z pięciu ciał. Liczba 24 (§4) wymaga porządku na ciele.

Uwaga o dwuwarstwowej strukturze.

· Warstwa pierwsza (niezależna od ciała): dim Im(d) = 3, kryterium C(D) = 0.
· Warstwa druga (wymaga ℝ i porządku): 24, δ√3, faza, oktaedr.

Kompleksyfikacja (§12H) pokazuje, że warstwa pierwsza przenosi się na ℂ bez zmian.

---

3. Kanoniczny defekt Δ

Definicja (✅). Δ(D) = dist(D, Im(d)) = ‖P_cyc D‖, gdzie P_cyc = I − d d⁺.

Rozdzielenie:

Obiekt Wymaga metryki? Status
C(D) = 0 ❌ strukturalny
wzorzec 24/64 ❌ kombinatoryczny
Δ(D) ✅ ilościowy, kanoniczny
δ√3 w bazie trójkątów ✅ (zależny od bazy) reprezentacja

---

4. 24 realizowalne wzorce znaków

Fakt (✅). Spośród 64 wzorców znaków na 6 krawędziach, dokładnie 24 odpowiada rzeczywistym porządkom liniowym.

Klasyfikacja wg Δ:

Δ/δ liczba wzorców realizowalne?
1 24 ✅ wszystkie realizowalne
√3 16 nie
√5 24 nie

Konsekwencja: dla wszystkich 24 realizowalnych porządków, po progowaniu D_* = δ·sign(D_0): Δ(D_*) = δ dokładnie.

---

5. Reprezentacja S₄

Wersja poprawna (podpisana reprezentacja).
C^1(K_4) \cong V_{\rm std} \oplus (V_{\rm std} \otimes \mathrm{sign}), \quad \operatorname{Im}(d) \cong V_{\rm std}, \quad V_{\rm cyc} \cong V_{\rm std} \otimes \mathrm{sign}.

Uogólnienie na podgrupy G ⊆ S_n — patrz §12C.

5.1. Historia błędu — case study metodologiczny

❌ Wersja odrzucona w trakcie audytu: C¹(K₄) ≅ 1 ⊕ V_std ⊕ V₂ — wynik uzyskany przez błędną (nieskierowaną) reprezentację permutacyjną na krawędziach, niezgodną z antysymetrią D_{ij} = −D_{ji}.

Test równoważności d(π·x) �stackrel{?}{=} π·d(x) nie przechodził dla tej wersji — sygnał, że reprezentacja była zbudowana niepoprawnie.

✅ Wersja poprawna (podpisana reprezentacja, test równoważności przechodzi dokładnie):
C^1(K_4) \cong V_{\rm std} \oplus (V_{\rm std} \otimes \mathrm{sign}), \quad \operatorname{Im}(d) \cong V_{\rm std}, \quad V_{\rm cyc} \cong V_{\rm std} \otimes \mathrm{sign}.

Weryfikacja dodatkowa: uśredniony projektor S₄ na sektor V_cyc jest macierzą zerową (brak podprzestrzeni niezmienniczej) — potwierdza nieprzywiedlność, zgodną z V_std ⊗ sign, nie z 1 ⊕ V₂.

Wniosek metodologiczny. Interpretacja „exact = wektor, cykliczność = pseudowektor" jest poprawna, ale wymagała jawnego testu równoważności do rozstrzygnięcia między dwiema pozornie równie prawdopodobnymi wersjami rachunku.

Zasada. Żadne twierdzenie o rozkładzie reprezentacyjnym nie jest ustalone bez testu równoważności na reprezentacji znakowanej.

---

6. Struktura oktaedryczna V_cyc

Twierdzenie RD1-D (✅). Rzutując 24 realizowalne wzorce znaków na V_cyc, otrzymuje się dokładnie 6 kierunków, każdy trafiony przez 4 z 24 porządków.

· Macierz Grama: ⟨v_i, v_j⟩ ∈ {+1, 0, −1} — sygnatura wierzchołków ośmiościanu.
· Stabilizator każdego kierunku: C_4 (rząd 4) — stabilizator wierzchołka ośmiościanu.

Konsekwencja: w modelu progowym defekt węzła jest jednym z 6 dyskretnych kierunków.

Trzy ortogonalne osie 180° (✅). V_4 = {e, (12)(34), (13)(24), (14)(23)} działa na V_cyc jako trzy wzajemnie ortogonalne rotacje 180°. Te same osie odpowiadają trzem parom przeciwległych krawędzi z §7.

❌ Wersja odrzucona: „P_cyc = ½ blockdiag(I_2, I_2, I_2)" — niemożliwe strukturalnie ((½I)² ≠ ½I, a P_cyc musi być idempotentne). Poprawnie: P_cyc jest diagonalne wewnątrz każdej pary przeciwległej (korelacja zero), ale nie między różnymi parami (korelacja ±0,25 dla sąsiednich z różnych par).

---

7. Krawędzie przeciwległe vs sąsiednie

Fakt (✅, rachunek bezpośredni na P_cyc).
P_{\rm cyc}(e,f) = 0 \text{ dla wszystkich trzech par przeciwległych } (12,34),\,(13,24),\,(14,23);


P_{\rm cyc}(e,f) \neq 0 \text{ dla krawędzi sąsiednich (wspólny wierzchołek)}.

Fakt czysto kombinatoryczny (wynika z K₄), nie z późniejszego rysowania jako czworościan.

---

8. Dynamika progowa K = K₂∘K₁

K_1(D) = (1−α)D, K_2 — korekta progowa.

Dla realizowalnego porządku znaków, po progowaniu: D_* = δ·sign(D_0), dynamika realizuje przejście:
\operatorname{Im}(d) \longrightarrow C^1(K_4) \setminus \operatorname{Im}(d), \qquad \text{exact} \to \text{non-exact}.

Interpretacja: defekt może zostać wygenerowany przez samą dynamikę ograniczającą relacje.

Uwaga. Dla kryterium amplifikacji w kontekście kanału T_b zob. §12C.4.

---

9. Sprzężenie międzywęzłowe R_e

Dla dwóch węzłów A, B dzielących jedną wspólną krawędź e:
R_e(D_e^A, D_e^B) = \left(\tfrac{D_e^A+D_e^B}2, \tfrac{D_e^A+D_e^B}2\right).

Twierdzenie D-R1 (✅).
\Delta_R(A) = \frac{|D_e^B - D_e^A|}{2\sqrt{2}}, \qquad \Delta_R(A)=0 \iff D_e^A=D_e^B.

Ostrzeżenie o zakresie. Formuła ścisła tylko dla jednej wspólnej krawędzi. Przy współdzieleniu wierzchołka lub kilku krawędzi — potrzebne człony krzyżowe (§9.1).

9.1. Twierdzenie D-R3 — uogólnienie

Kanał projekcyjny. Dla S ⊆ {1,…,6}:
\mathcal{K}_S(h) = P_{\rm cyc}\tilde h.

Twierdzenie D-R3 (✅). Dla D_A ∈ Im(d), D_B dowolne, h_e = (D_e^B − D_e^A)/2:
\Delta_R(A)^2 = h^\top P_{\rm cyc}\big|_S\, h.

Dowód: D_A' = D_A + h̃, P_cyc(D_A) = 0, więc P_cyc(D_A') = P_cyc(h̃). Ponieważ P_cyc jest rzutem ortogonalnym, ‖P_cyc(h̃)‖² = hᵀP_cyc|_S h. ∎

Charakteryzacja jądra (✅).
\boxed{\ker \mathcal{K}_S = \operatorname{Im}(d) \cap \mathbb{R}^S.}

Kierunek h jest „ślepy" (nie generuje defektu) dokładnie wtedy, gdy h rozszerzone zerami poza S jest już exact.

9.2. Pełna tabela widm P_cyc|_S

Fakt (✅, zweryfikowane dla reprezentatywnych klas S do automorfizmu S₄):

S Widmo P_cyc\|_S dim ker K_S
1 krawędź {0,5} 0
2, sąsiednie {0,25; 0,75} 0
2, przeciwległe {0,5; 0,5} 0
3, gwiazda (wierzchołek) {0; 0,75; 0,75} 1
3, trójkąt {0,25; 0,25; 1} 0
3, ścieżka {0,146; 0,5; 0,854} 0
4 {0; 0,5; 0,5; 1} 1
5 {0; 0; 0,5; 1; 1} 2
6 (pełna synchronizacja, D-R2) {0;0;0; 1;1;1} 3

Kluczowe przypadki:

· Gwiazda (3 krawędzie z jednego wierzchołka): kierunek ślepy h = (a,a,a) odpowiada dokładnie potencjałowi (x_1, x_1−a, x_1−a, x_1−a). Defekt nie widzi tej części niezgodności, którą można wyjaśnić przesunięciem potencjału.
· Pełna synchronizacja (S = 6): dim ker K_S = 3 — defekt jest zjawiskiem częściowego współdzielenia (D-R2).

Rozkład dla gwiazdy. h = h̄·1 + h_⊥ daje Δ_R² = ¾‖h_⊥‖². Defekt mierzy wyłącznie niejednorodną (nieredukowalną cyklicznie) część niezgodności, nie jej średnią.

Status pytania. Zamknięte dla ustalonego S — prawo ogólne, dowód algebraiczny, jądro scharakteryzowane. Otwarte: interpretacja K_S w pełnej dynamice sieciowej Net (jak kanał projekcyjny wchodzi w interakcję z M_ef, R, progiem F).

---

10. Warunki propagacji

Wynik 1 (✅). Interfejsy węzła pasywnego w parze przeciwległej → propagacja strukturalnie niemożliwa (§7).

Wynik 2 (🔍). Sąsiedztwo krawędzi konieczne, ale niewystarczające.

Wynik 3 (🔍). Kanał sektorowy (K₂ działające na P_cyc D) → propagacja pojawia się.

Test β (🔍). Wynik binarny: β = 0 → brak propagacji; β > 0 → propagacja.

Test λ (🔍). Z ciągłą aktywacją F_λ efekt „wszystko-albo-nic" znika.

Wniosek kluczowy (✅). Efekt „wszystko-albo-nic" jest artefaktem twardego progu, nie kanału M_ef.

---

11. Trzy warianty modelu

Wariant K₂ Propagacja?
Net-L diagonalny ❌ nie
Net-G sektorowy + twardy próg ✅ wszystko-albo-nic
Net-I ciągły F_λ ✅ proporcjonalnie do λ

---

12. H-Bridge — związek z P₀-Centroid

Odkrycie 1 (✅). Operator d: ℝ⁴ → C¹(K₄) jest S₄-ekwiwariantny. Jego obraz = sektor exact, jądro = ⟨1⟩ = p₀. Kanoniczny izomorfizm:
V_\rho \cong \mathbb{R}^4/\langle 1\rangle \xrightarrow{d} \operatorname{Im}(d) \subset C^1(K_4).

Odkrycie 2 (✅). Trzy pary krawędzi przeciwległych odpowiadają trzem wzajemnie ortogonalnym osiom rotacji 180° — w V_ρ i w V_cyc. Szczegóły: patrz §6.

Odkrycie 3 (✅). Lokalność w Centroid (M_v zmienia jeden wierzchołek) nie przechodzi przez d na lokalność w Defect (d(M_v x) zmienia wszystkie krawędzie incydentne z wierzchołkiem v, nie jedną). Bezpośredni izomorfizm dynamik nie zachodzi.

Odkrycie 4 (💡). Rekurencyjne p₀ i lokalność „czarnej dziury" — pełna analiza w §12.1–§12.3.

12.1. Twierdzenie 4a — trywialność dosłownego zagnieżdżenia

Uwaga o historii. Pierwsza próba pytania („p₀ w p₀" przez rekurencyjną samoaplikację M_m/R₄) została odrzucona — test pokazał, że widmo/faza tej dynamiki jest zależne od struktury grafu, nie uniwersalne. Poniższa wersja buduje się wyłącznie na kryterium jądra d (§1–§2, sprawdzonym na 6 ciałach).

Konstrukcja. Rozróżniamy exact (D ∈ Im(d) — istnieje jakikolwiek potencjał) od p₀ (potencjał jest stały, D = 0; ścisły podzbiór exact). Rekurencja: poziom k+1 traktuje stałe wartości potencjałów czterech skonsensusowanych węzłów poziomu k jako swój własny potencjał wejściowy x^(k+1).

Twierdzenie 4a (✅, wynika wyłącznie z kryterium jądra d). p₀ na poziomie k+1 wymaga c_1 = c_2 = c_3 = c_4 dla czterech wartości wejściowych — czyli wszystkie węzły poziomu k muszą mieć identyczną stałą. Struktura dwupoziomowa spełniająca to jest nieodróżnialna od jednego globalnego stanu stałego.

Wniosek. Dosłowne „p₀ w p₀" nie niesie nowej treści.

12.2. Obserwacja 4b — lokalność czarnej dziury

Obserwacja (💡). Treść nie leży w „p₀ w p₀", lecz w „p₀ na poziomie k, defekt na poziomie k+1": węzeł w pełni skonsensusowany wewnętrznie (własne A0') może mieć wartość różną od sąsiada na tym samym poziomie k — a to jest dokładnie sytuacja D-R1 (§9): oba węzły exact z osobna, Δ_R > 0 na ich styku.

Wniosek. Czarna dziura relacyjna jest lokalna dla poziomu: unieruchamia węzeł od środka, ale nie chroni przed byciem punktem różnicy widzianym z zewnątrz.

12.3. Przypuszczenie 4c — nieosiągalność globalnego p₀ wieży

Wynik 1 (🔍). Rozrzut potencjałów na szczycie wieży zanika geometrycznie: std(x^(L)_szczyt) ∼ c^L, c ≈ 0,6 — zmierzone dla uproszczonej średniej i dla prawdziwej dynamiki R₄ (zgodność jakościowa).

Wynik 2 (✅, twardy próg). Δ stabilizuje się na δ niezależnie od L (sprawdzone dla ε aż do 10⁻⁹, L = 0..20, 270/270 prób bez wyjątku).

Korekta względem wcześniejszej wersji. Poprzedni zapis sugerował możliwość δ√3 lub δ√5 (klasyfikacja 64 wzorców z §4). To dotyczy sztucznie losowanego wektora w ℝ⁶, ale nie stosuje się do hierarchii: wieża produkuje na szczycie cztery liczby rzeczywiste x^(L) ∈ ℝ⁴, więc D_L = d(x^(L)) jest z definicji różnicą potencjałów. Z §4: różnica potencjałów ma zawsze realizowalny wzorzec znaków, nigdy nierealizowalny. Stąd δ_eff(L) ≡ δ dla każdej głębokości L (przy braku remisów).

Wynik 3 (✅, miękki próg). Wcześniejsza hipoteza „miękki próg → Δ→0 przy ε→0" jest fałszywa dla ustalonego λ>0. Dla |z|<δ: F_λ(z) = (1−λ)z + λδ·sign(z). Gdy z→0, pierwszy człon znika, drugi pozostaje: boost → λδ. Miękki próg ma więc podłogę λδ, analogiczną do podłogi δ twardego progu.

Błąd metodologiczny zidentyfikowany. Wcześniejszy wynik („przy λ→0 efekt wszystko-albo-nic znika") dotyczył przekroju (λ→0, wejście ≈ stałe) — innej osi niż przekrój (ε→0, λ = stałe) potrzebny do pytania o głębokość. Granice cząstkowe w przestrzeni (ε, λ) nie są wymienne.

Wynik 4 (✅, granica łączna). Dla dostatecznie dużych L (gdzie max|D_{L,ij}| < δ):
\boxed{\Delta^{(L)} = \lambda_L\, \delta \quad \text{dokładnie.}}

Dowód. D_L = d(x^(L)), więc P_cyc(D_L) = 0 dokładnie dla każdego L (algebraiczny fakt, nie asymptotyka). Z liniowości P_cyc:
P_{\rm cyc}(F_{\lambda_L}(D_L)) = (1−\lambda_L)\underbrace{P_{\rm cyc}(D_L)}_{=0} + \lambda_L\delta\,P_{\rm cyc}(\operatorname{sign}(D_L)).


Dla realizowalnego wzorca bez remisów, ‖P_cyc(sign(D_L))‖ = 1. Stąd Δ^(L) = λ_L δ bez członu resztowego. ∎

Tempo zbieżności Δ^(L) → 0 jest więc wyłącznie tempem λ_L → 0, niezależnie od profilu ε_L.

Wniosek 12.3′-a (✅, klasyfikacja remisów). Jeśli x^(L) zawiera remisy, norma wzorca znaków w V_cyc zależy wyłącznie od liczby remisów, nie od ich topologii (przeciwległe/sąsiednie dają ten sam wynik):

Liczba niezależnych remisów ‖P_cyc(sign D_L)‖ Δ^(L)
0 (ścisły porządek) 1 λ_L δ
dokładnie 1 1/√2 λ_L δ / √2
≥2 (dowolna konfiguracja) 0 0

Podłoga defektu znika całkowicie, gdy tylko dwa niezależne podwęzły zbiegną do tej samej wartości — nie tylko słabnie.

Wniosek architektoniczny. Niezależnie od charakteru progu, hierarchia zagnieżdżonych K₄ generuje trwały defekt na każdym poziomie pod warunkiem braku przypadkowych zgodności (remisów) — dla twardego progu podłoga to δ dokładnie, dla miękkiego (λ>0 stałe) — λδ. Sektor cykliczny V_cyc jest odporny na samo zagnieżdżenie, ale nie na przypadkową koincydencję dwóch lub więcej poziomów.

Zamknięcie (✅). Formuła Δ^(L) = λ_L δ jest lokalna względem szczytu — zależy wyłącznie od tego, czy cztery wartości na szczycie są parami różne, nie od rozmiaru poddrzew. Dla dowolnego rozkładu ciągłego liści to zachodzi p.n., niezależnie od głębokości.

Sprawdzono dodatkowo, czy reżim Δ = 0 jest osiągalny przez symetrię strukturalną zamiast przypadku. Wynik: nie. Gałęzie dosłownie identyczne (ten sam wkład powielony) dają remis trywialnie, ale to nie mówi nic o naturalnej hierarchii. Gałęzie o tej samej średniej, lecz niezależnym szumie (realistyczna wersja symetrii V_4) nigdy nie dają remisu (0/5 prób, różnice rzędu 10⁻³–10⁻¹). Symetria statystyczna i degeneracja strukturalna to różne rzeczy — tylko ta druga daje Δ = 0.

H-Bridge v0.3 (💡, hipoteza strukturalna).

Lokalna dynamika względem elementów naturalnej bazy (wierzchołki lub krawędzie) nie generuje globalnych korelacji wymaganych przez rozkład Schura. W obu przypadkach (Centroid i Defect) wymazanie informacji wynika z braku mieszania między składowymi rozkładu. Sieć (R) lub mieszanie sektorowe (K₂^cyc) są potrzebne jako źródło nielokalności, której lokalna algebra sama nie posiada.

---

12A. Twierdzenie A — pełna symetria

12A.1. Sformułowanie

Twierdzenie A (✅ dla wszystkich n ≥ 4). Przy pełnej symetrii S_n:
\dim \operatorname{Hom}_{S_n}\bigl(V_{\rm cyc} \otimes V_{\rm cyc}, V_{\rm cyc}\bigr) = m_n = 1,


i jedynym (z dokładnością do skalara) elementem jest bracket Liego [A, B] = AB − BA. Konsekwencja:
\boxed{\operatorname{Hom}_{S_n}\bigl(\operatorname{Sym}^2(V_{\rm cyc}), V_{\rm cyc}\bigr) = 0.}

12A.2. Kontekst reprezentacyjny

Dla ogólnego n ≥ 4:

· V_ρ = [n−1, 1] (standard S_n), dim V_ρ = n − 1,
· V_cyc = [n−2, 1, 1] (hook), dim V_cyc = (n−1)(n−2)/2.

Reprezentacja znakowana Q_sign: S_n → O(C¹(K_n)). Test równoważności d ∘ P_π = Q_sign(π) ∘ d przechodzi dokładnie.

12A.3. Reframing strukturalny

\boxed{\text{Pełna symetria } S_n \text{ usuwa tylko część symetryczną samoodziaływania } V_{\rm cyc}.}

Pozostaje wyłącznie kanał rotacyjny (bracket Liego). V_cyc = 𝔰𝔬(V_ρ) ma naturalną strukturę Liego i to jest jedyne, co może robić sam ze sobą.

12A.4. Jawna postać

\phi: \Lambda^2(V_{\rm cyc}) \to V_{\rm cyc}, \qquad \phi(A \wedge B) = [A, B] = AB − BA.

Właściwości:

· S_n-ekwiwariantna (konjugacja zachowuje bracket),
· antysymetryczna ([B,A] = −[A,B]),
· niezerowa (𝔰𝔬(m) prosta dla m ≥ 3).

---

12B. Dowód Twierdzenia A

12B.1. Redukcja do momentów cykli

Charakter χ_V(g) dla V = [n−2,1,1]:

\chi_V(g) = \binom{X_1(g) - 1}{2} - X_2(g),

gdzie X_1(g) = liczba cykli długości 1, X_2(g) = liczba cykli długości 2 w permutacji g.

Wyprowadzenie. χ_ρ(g) = X_1(g) − 1 (punkty stałe minus 1). χ_ρ(g²) = X_1(g) + 2X_2(g) − 1 (punkty stałe g² = punkty stałe g + punkty w 2-cyklach). V_cyc = Λ²(V_ρ), więc:
\chi_V(g) = \frac{\chi_\rho(g)^2 − \chi_\rho(g^2)}{2} = \binom{X_1 − 1}{2} − X_2.

12B.2. Lemat kombinatoryczny

Lemat (✅). Dla każdego i, j ≥ 0:
\sum_{\lambda \vdash n} \frac{(a_1)_i (a_2)_j}{z_\lambda} = \frac{\mathbf{1}[n \geq i + 2j]}{2^j},


gdzie (a_1)_i, (a_2)_j to falling factorials, z_λ = centralizer order.

Dowód: EGF cycle index Z_n(y_1, y_2). Różniczkowanie ∂_u^i ∂_v^j [e^{ut}e^{vt²/2}/(1−t)]|_{u=v=0} = t^{i+2j}/(2^j (1−t)). ∎

12B.3. Obliczenie m_n

Dla n ≥ 6, wszystkie wskaźniki w lemacie są nasycone:
m_n = \sum_{\text{monomials}} (\text{coef}) \cdot B_i \cdot T_j,


gdzie B_i to liczby Bella, T_j = Σ_l S(j,l)/2^l to momenty Poissona(1/2).

Wartości:

i B_i (Bella)  j T_j (Poisson 1/2)
0 1  0 1
1 1  1 1/2
2 2  2 3/4
3 5  3 11/8
4 15   
5 52   
6 203   

Rozwijając χ_V³:
m_n = \frac{19}{8} − \frac{9}{8} + \frac{9}{8} − \frac{11}{8} = 1 \quad \text{dla } n \geq 6.

Dla n = 4, 5 — bezpośrednie obliczenie: m_4 = m_5 = 1.

Weryfikacja numeryczna dokładna (Fraction): m_n = 1 dla n = 4, 5, \ldots, 20.

12B.4. Konkluzja

m_n = 1 dla wszystkich n ≥ 4, więc V_cyc występuje w V_cyc ⊗ V_cyc dokładnie raz. Ten jedyny element to antysymetryczny bracket, więc w Sym² krotność wynosi 0. ∎

12B.5. Historia korekt krotności

Wersja Twierdzenie Status
v0 (oryginalna) V_cyc⊗V_cyc (1) + V_cyc⊗V_ρ (2) = 3 ❌ Błędne
v1 (pierwsza korekta) 1+1+1 symetrycznych ❌ Błędne
v2 (finalna) Tylko V_ρ ⊙ V_cyc, krotność 1 ✅

Zasada metodologiczna. Żadne twierdzenie o krotnościach nie jest ustalone bez jawnego rachunku charakterów.

---

12C. Złamanie symetrii — podgrupy

12C.1. Klasyfikacja

Dla podgrupy G ⊆ S_n, m_G = dim Hom_G(Sym²V_cyc, V_cyc).

Type I: (cyc,cyc;cyc) ∈ ΔC(G) i V_ρ|_G ≇ V_cyc|_G — prawdziwe otwarcie.
Type II: (cyc,cyc;cyc) ∈ C(G) ale V_ρ|_G ≅ V_cyc|_G — utożsamienie sektorów.
Type III: m_G = 0.

Klasyfikacja dla K₄:

G Rząd V_ρ\|_G ≅ V_cyc\|_G? m_G Typ
S₄ 24 nie 0 Type III
V₄ 4 tak 3 Type II
A₄ 12 tak — Type II
D₄ 8 nie 1 Type I ✓
S₃ 6 nie 2 Type I ✓
Z/4 4 nie 4 Type I (abelowa)

Klasyfikacja dla K₅:

G ⊆ S₅ Rząd V_cyc\|_G T_b T_a
S₅ 120 [3,1,1] (nieprzyw.) ✗ ✗
S₄ (fix 4) 24 [3,1] ⊕ [2,1,1] ✓ ✓
A₅ 60 3a ⊕ 3b ✗ ✗
S₃ × S₂ 12 4 składniki ? ?
S₃ (fix 3,4) 6 (triv⊕sign) ⊕ 2·std ✓ ✓
D₅ 10 6 składników ? ?

Kluczowa obserwacja. A₅ ma V_cyc rozkładalną (3a ⊕ 3b), ale Sym²(3a) = 1 ⊕ 5 ⊉ 3a, więc T_b = 0. Rozkładalność nie wystarcza — potrzebne Sym²(B) ⊇ B.

Uwaga o V_4, A_4. V_4, A_4 ⊂ A_4 ⟹ sign|_{V_4} = 1 ⟹ V_ρ|_{V_4} ≅ V_cyc|_{V_4}. Formalnie m > 0, ale to Type II — złamanie znosi rozróżnienie sektorów, nie otwiera nowego kanału.

12C.2. Branching S_n ↓ S_{n-1}

Reguła Younga (📚). [n−2, 1, 1]|_{S_{n-1}} = [n−3, 1, 1] ⊕ [n−2, 1].

Notacja: A := [n−3, 1, 1], B := [n−2, 1] (standard S_{n-1}).

Wymiary: dim A = (n−2)(n−3)/2, dim B = n−2.

12C.3. Dwa kanały

· T_a: A × B → B — rotacja w B, zachowuje normę.
· T_b: B × B → B — samo-sprzężenie, może amplifikować.

Kluczowa własność Sym²(B) ⊇ B:

G B Sym²(B) Sym²(B) ⊇ B?
D₄ ⊂ S₄ χ₅ (2-wym.) triv ⊕ χ₃ ⊕ χ₄ NIE
S₃ ⊂ S₄ std (2-wym.) triv ⊕ std TAK
S₄ ⊂ S₅ std = [3,1] 1 ⊕ [3,1] ⊕ [2,2] TAK
S₄ ⊂ S₅ std_sgn = [2,1,1] 1 ⊕ [3,1] ⊕ [2,2] NIE
A₅ 3a 1 ⊕ 5 NIE

12C.4. Kryterium amplifikacji — hierarchia

\text{kanał} \Downarrow T_b \neq 0 \Downarrow \gamma_{\rm nl} > \gamma_{\rm lin}

Warunki dla trzech pierwszych:

1. Rozszczepienie V_cyc|_G = A ⊕ B,
2. Sym²(B) ⊇ B,
3. T_a ≠ 0.

Ostatni krok (γ_nl > γ_lin) jest weryfikowany numerycznie — nie wynika z samej algebry. Operator T_b może istnieć reprezentacyjnie, ale jego współczynnik w dynamice może być zerowy, dyssypatywny lub prowadzić do stabilnego atraktora.

12C.5. Istnienie T_b

Twierdzenie C (✅). Dla B = [n−2, 1] (standard S_{n-1}), n ≥ 4:
\operatorname{Sym}^2(B) = [n−1] \oplus B \oplus [n−3, 2].


Zawiera B z krotnością 1. ∎

Dowód: klasyczny rozkład sym² reprezentacji standardowej S_m.

12C.6. Istnienie T_a

Twierdzenie D (✅, uproszczony). Hom(A ⊗ B, B) ≅ Hom(A, B ⊗ B) ⊇ Hom(A, Λ²B) = ℝ. ∎

12C.7. Związek T_a z podalgebrą 𝔰𝔬(3)

T_a: A × B → B jest realizacją rotacji w B. Strukturalnie związane z podalgebrą 𝔰𝔬(3) ⊂ 𝔤₄ (Centroid §2.5). Nie jest jednak constraintem — jest jednym z kanałów dynamiki.

Otwarte: czy T_a można wyprowadzić wprost z komutatorów [ρ(M_i), ρ(M_j)]?

---

12D. Tożsamość A = Λ²B

\boxed{A = \Lambda^2(B)}

jako S_{n-1}-moduły. Weryfikacja wymiarowa: C(n−2, 2) = (n−2)(n−3)/2. ✓

12D.1. Reframing strukturalny

\boxed{A = \Lambda^2 B, \qquad B \subset \operatorname{Sym}^2 B}

· A = antysymetryzacja B (rotacja, skręt),
· B = w symetryzacji samego siebie (nieliniowa produkcja).

Łańcuch: A → T_a → B → T_b → B.

W języku P₀: rotacja → orientacja → amplituda.

---

12E. Asymetria A ↔ B

Twierdzenie E (✅). W konkretnym rozszczepieniu V_cyc|_G = A ⊕ B, tylko B = [n−2,1] (standard) daje T_b. Sektor A (jako kandydat na B) nie daje, bo Sym²([n−3,1,1]) ⊉ [n−3,1,1] (dla n ≥ 5).

Korekta wcześniejszego sformułowania. Fałszywe było „standard jest jedyną reprezentacją z Sym²(B) ⊇ B". Kontrprzykłady: triv, [k,k] dla S_{2k}. Poprawne: w konkretnym rozszczepieniu V_cyc|_G, tylko B = standard daje T_b.

---

12F. Stabilność architektury kanałów względem n

Twierdzenie 5 (✅ dla rodziny S_{n-1} ⊂ S_n). Dla każdego n ≥ 4:

1. Przy pełnej symetrii: Hom(Sym²V_cyc, V_cyc) = 0.
2. Przy złamaniu do S_{n-1}: V_cyc = A ⊕ B.
3. T_b istnieje, krotność 1.
4. T_a istnieje, krotność 1.
5. Asymetria A ↔ B niszczy T_b.
6. Stabilność architektury — reguła reprezentacyjna niezmiennicza, wymiary rosną z n.

Uwaga terminologiczna. Poprawne słowo: stabilność architektury kanałów, nie „niezmienniczość" (wymiary rosną).

12F.1. Dlaczego λ_max(Φ(x*)) maleje z n

K₄: λ_max ≈ 1,155, K₅: λ_max ≈ 0,224. Powód: Φ(x*) w bazie (e_A, e_1, …, e_{n-2}) skaluje się jak 1/√(n−1). Efektywność T_b maleje z n.

---

12G. Wynik negatywny dla granicy continuum

12G.1. Identyfikacja kandydacka

· V_ρ → im(d) (gradienty),
· V_cyc = 𝔰𝔬(n−1) ⊂ 𝔛_div(S^{n−2}) (podalgebra Killinga).

Uwaga. Pełna symetria (§12A) usuwa T_b. W złamanej symetrii (§12C) T_b istnieje lokalnie, ale nie przenosi się do continuum — to właśnie pokazuje §12G.

12G.2. Co przenosi się: T_a

T_a (✅). Bracket 𝔰𝔬:

· [𝔤₀, 𝔤₀] ⊂ 𝔤₀,
· [𝔤₀, 𝔤₁] = 𝔤₁ — to jest T_a,
· [𝔤₁, 𝔤₁] ⊂ 𝔤₀.

Związek z NS: T_a ↔ (u·∇)ω. Kandydat.

12G.3. Co NIE przenosi się: T_b

T_b (❌). Kubiczny niezmiennik e_3 na B = ℝ^{n−2} nie jest SO(n−2)-niezmienniczy.

Klasyfikacja. Istnieje skończony zbiór par (𝔤, V) z Sym³(V) ⊇ triv: 𝔰𝔲(n), 𝔤₂, 𝔣₄, 𝔢₆. Brak nieskończonej rodziny z dim V_n → ∞.

Wniosek: T_b nie przenosi się do continuum przez naiwną granicę S_{n-1} → SO(n−2).

12G.4. Identyfikacja z Eulerem–Arnoldem

Na 𝔤 = 𝔰𝔬(n−1) z anizotropią I = diag(I_A, I_B):
\dot R_A = -I_B[R_B, R_B], \qquad \dot R_B = -(I_B - I_A)[R_A, R_B].

P₀ z samym T_a jest Eulerem–Arnoldem z częściowo wyłączoną nieliniowością.

Wniosek (✅). P₀-Flow na C¹(K_n) to dwukanałowe rozszerzenie Eulera–Arnolda o kubiczny tensor. Nie jest modelem NS.

12G.5. Trzy scenariusze

(S1) P₀ na K_n nie jest modelem NS — najbardziej prawdopodobne.
(S2) P₀ jest modelem NS przez inną granicę continuum (grupa Liego z kubicem, G₂-manifold).
(S3) P₀-Flow opisuje inną dynamikę.

---

12H. Kompleksyfikacja sektora cyklicznego (wchłonięte z P₀-Hilbert)

12H.1. Motywacja

§2.1 pokazuje, że warstwa strukturalna (rank(d) = 3) jest niezależna od ciała. §2.1 wskazuje też dwie warstwy: strukturalną (niezależną od ciała) i ilościową (wymagającą ℝ). Kompleksyfikacja pyta: co się dzieje z warstwą strukturalną, gdy rozszerzymy skalary do ℂ?

12H.2. Konstrukcja

Przestrzeń i projektor.
\mathcal{H} = C^1(K_4) \otimes \mathbb{C} \cong \mathbb{C}^6, \qquad G = P_{\rm cyc} \otimes I_{\mathbb{C}}.

Fakt (✅). G jest hermitowski (G† = G) i idempotentny (G² = G), bo P_cyc jest symetryczny i idempotentny, a kompleksyfikacja jest funktorem dokładnym.

Fakt (✅). ker G = Im(d_ℂ), dim_ℂ Im(d_ℂ) = 3, dim_ℂ ker G = 3.

Forma kwadratowa defektu. Dla z ∈ ℂ⁶:
Q_H(z) = z^\dagger G z = \|Gz\|^2 = \|P_{\rm cyc} z\|^2.

Fakt (✅). Q_H(z) = 0 ⟺ z ∈ Im(d_ℂ). Forma Q_H rozróżnia exact od non-exact również po kompleksyfikacji.

Torus faz. Dla ρ = (ρ_1,…,ρ_6) > 0:
\mathcal{T}_\rho = \{z \in \mathbb{C}^6 : |z_e| = \rho_e\} \cong \mathbb{T}^6.


Globalna faza φ → φ + α1 nie zmienia Q_H. Rzeczywiste stopnie swobody: 5.

12H.3. Redukcja do problemu cykli

Operator cykli. C: ℂ⁶ → ℂ⁴ (cztery cykle trójkątowe).

Twierdzenie R3-1 (✅). Cᵀ C = 4 P_cyc.

Uzasadnienie. P_cyc jest rzutem na ker(dᵀ). C mapuje krawędzie na sumy cykliczne. Wartości singularne C|_{V_cyc} to (2, 2, 2) — potwierdzone numerycznie z dokładnością 10⁻¹⁶.

Konsekwencja (✅). Q_H(z) = ¼‖Cz‖².

12H.4. Wynik główny

Twierdzenie R3-2 (🔍, kandydat). Dla jednorodnych amplitud ρ_e = δ:
\boxed{\min_{\phi \in \mathbb{T}^6} Q_H(z(\phi)) = (3 − 2\sqrt{2})\delta^2 = (\sqrt{2} − 1)^2 \delta^2.}

W konsekwencji:
\boxed{\min_{|z_e|=\delta} \|P_{\rm cyc} z\| = (\sqrt{2} − 1)\delta \approx 0{,}414\delta.}

Weryfikacja numeryczna (🔍). 5000 losowych startów L-BFGS-B na 𝕋⁶. 3796 zbiegło do 3 − 2√2 (tolerancja 10⁻⁶). Differential Evolution potwierdził z dokładnością 10⁻¹².

Konfiguracja osiągająca minimum (✅). Modulo globalna faza:

Krawędź Faza φ_e z_e = e^{iφ_e}
01 0 1
02 −π/4 (1−i)/√2
03 +π/4 (1+i)/√2
12 −3π/4 (−1−i)/√2
13 +3π/4 (−1+i)/√2
23 +π/2 i

W tej konfiguracji wszystkie cztery cykle trójkątowe mają sumę wektorową o module √2−1.

12H.5. Interpretacja — odporność exact/cyclic

Wniosek R3-3 (✅/🔍).
\mathcal{T}_\delta \cap \operatorname{Im}(d_{\mathbb{C}}) = \varnothing.

Torus jednorodnych amplitud nie przecina zespolonej przestrzeni exact. Fazy względne modulują defekt, ale nie mogą go wyzerować przy zachowaniu modułów.

Co to oznacza. Kompleksyfikacja ℝ⁶ → ℂ⁶ dodaje 6 rzeczywistych stopni swobody (fazy), ale przy ograniczeniu |z_e| = δ struktura exact/cyclic jest odporna: sektor cyclic pozostaje niezerowy, minimalny defekt to (√2−1)δ.

To nie jest własność kwantowa — to geometria torusa 𝕋⁶ względem podprzestrzeni exact w ℂ⁶.

12H.6. Relacja do innych sekcji

Byt w §2–§4 Odpowiednik w kompleksyfikacji Status
P_cyc(e,f) = 0 dla przeciwległych Krawędzie przeciwległe mają \|(P_cyc z)_e\| ≈ 0,207 Potwierdzone
24 wzorce znaków Wzorce sign(D) ⊂ T_δ (fazy 0 lub π). Δ = δ > (√2−1)δ Konsekwentne
Struktura oktaedryczna Konfiguracja faz stabilizowana przez V_4 ⊂ S₄ 💡 hipoteza

12H.7. Otwarte pytania (R3-1..R3-5)

# Pytanie Status
R3-1 Dowód analityczny globalności minimum (√2−1)δ 💡
R3-2 Czy konfiguracja faz jest jedyna? 💡
R3-3 Dla niejednorodnych ρ — minimum mniejsze? 🔍
R3-4 Czy √2−1 ma interpretację w metryce G₄? 💡
R3-5 Kompleksyfikacja z dynamiką (unitarna ewolucja)? 💡

12H.8. Metodologia weryfikacji

Wszystkie obliczenia w podwójnej precyzji (float64).

1. Budowa P_cyc przez pseudoodwrotność d⁺ (SVD, tolerancja 10⁻¹⁵).
2. Weryfikacja projektora: ‖P_cyc − P_cycᵀ‖_F < 10⁻¹⁵, ‖P_cyc² − P_cyc‖_F < 10⁻¹⁵, trace(P_cyc) = 3.
3. Weryfikacja CᵀC = 4P_cyc: ‖·‖_F < 10⁻¹⁴.
4. L-BFGS-B (5000 startów) + Differential Evolution (populacja 50, 500 iteracji).
5. Kontrola: ‖P_cyc z‖² = ¼‖Cz‖² z dokładnością 10⁻¹⁶.

12H.9. Zasada niezależności

Kompleksyfikacja nie modyfikuje matematyki §1–§12G. Jeśli kandydat R3-2 okaże się błędny (kontrprzykład analityczny lub numeryczny), upada jedynie ten eksperyment — nie P_cyc, nie d, nie klasyfikacja 64 wzorców.

Kompleksyfikacja nie zależy od P₀-Net, P₀-Wave ani P₀-Centroid. Może być zweryfikowana autonomicznie przez bezpośredni rachunek z macierzy d i P_cyc dla K₄.

12H.10. Pułapki metodologiczne i jak ich uniknięto

Pułapka Jak uniknięto
„Kompleksyfikacja = QM" Nie zakładano unitarnej ewolucji, nieprzemienności ani relacji nieoznaczoności. Q_H to forma kwadratowa z rzutem, nie obserwabla w sensie von Neumanna.
„Fazy względne mogą zniknąć defekt" Sprawdzono eksplicytnie: T_δ ∩ Im(d_ℂ) = ∅. Defekt ma dolną granicę (√2−1)δ > 0.
„Minimum numeryczne = globalne" Użyto dwóch algorytmów (L-BFGS-B 5000 startów + Differential Evolution). Zbieżność 3796/5000 do tej samej wartości daje silną hipotezę, ale status pozostaje 🔍 do zamknięcia dowodu analitycznego.
„Cykle mają normę √2−1, więc `‖P_cyc z‖ = √2−1" Sprawdzono operatorowo: CᵀC = 4P_cyc, więc ‖P_cyc z‖² = ¼‖Cz‖². Norma cykli i norma rzutu są powiązane przez singular values [2,2,2], nie tożsame.

---

13. Co jest wynikiem, a co hipotezą

Wyniki matematyczne (✅)

· dim C¹(K₄) = 6, dim Im(d) = 3
· exactness ⟺ zerowa cyrkulacja
· 24 realizowalne porządki znaków
· C¹(K₄) ≅ V_std ⊕ (V_std ⊗ sign) (§5.1 — historia błędu)
· kanoniczny defekt Δ(D_*) = δ
· struktura oktaedryczna V_cyc
· trzy ortogonalne osie 180°
· D-R1, D-R3
· pełna tabela widm P_cyc|_S (§9.2)
· V_ρ ≅ Im(d) kanonicznie
· niezależność rank(d) = 3 od ciała
· Twierdzenie A (m_n = 1)
· Dowód przez momenty cykli
· Klasyfikacja podgrup z Sym²(B) ⊇ B
· Tożsamość A = Λ²B
· Asymetria A ↔ B
· Stabilność architektury względem n
· Wynik negatywny dla granicy continuum
· Tw. 4a — trywialność zagnieżdżenia p₀-w-p₀
· Wynik 2, 3, 4 z §12.3 (miękki próg, granica łączna)
· Klasyfikacja remisów (§12.3′-a)

Wyniki zależne od dynamiki (🔍)

· przejście exact → non-exact pod K
· warunki propagacji
· binarność przejścia β
· ciągłe skalowanie amplitudy z λ
· Kompleksyfikacja: minimum (√2−1)δ
· Konserwatywna podalgebra rotacji w 𝔤₄
· Wynik 1 z §12.3 (zanik rozrzutu potencjałów)

Hipotezy P₀ (💡)

· relacja ontologicznie pierwotna
· defekt = „energia" struktury
· H-Bridge v0.3
· lokalność „czarnej dziury" (Obserwacja 4b)
· nieosiągalność globalnego p₀ wieży (Przypuszczenie 4c)
· Globalność minimum R3-2
· Jedyność konfiguracji faz

Sfalsyfikowane (❌)

· suma zachowana przez rundę asynchroniczną
· niezmienniczość Regionu II (Scalar S12)
· kontrakcyjność globalna K (Alchemy §6.1)
· „standard jedyna reprezentacja z Sym²(B) ⊇ B"
· Hipoteza „miękki próg → Δ→0 przy ε→0"
· Wersja reprezentacji S₄ bez znaku (§5.1)

---

14. Otwarte pytania

# Pytanie Status Priorytet
1 Uogólnienie D-R1 na współdzielenie wierzchołka ✅ §9.1 —
2 Operator R = generator rotacyjny? ✅ §12A —
3 Efektywny operator W na V_cyc dla sieci 💡 Wysoki
4 Addytywność defektu na łańcuchu >2 węzłów 💡 Wysoki
5 1/(2√2) — interpretacja 💡 Niski
6 Rozkład S₄ nad GF(2)/GF(3) 💡 Niski
7 Alternatywna granica continuum, w której T_b przeżywa 💡 Wysoki
8 Klasyfikacja wszystkich podgrup G ⊆ S_n z Sym²(B) ⊇ B 💡 Wysoki
9 Granica 𝔰𝔬(n−1) → 𝔡𝔦𝔣𝔣vol(M) 💡 Wysoki
10 Związek T_b z modelami kubicznymi (Skyrme) 💡 Średni
11 Dowód analityczny globalności minimum R3-2 💡 §12H.7 Średni
12 Jedyność konfiguracji faz 💡 §12H.7 Niski
13 Minimum dla niejednorodnych ρ 🔍 §12H.7 Niski
14 Związek √2−1 z metryką G₄ 💡 §12H.7 Niski
15 Kompleksyfikacja z dynamiką (unitarna ewolucja) 💡 §12H.7 Niski
16 Interpretacja K_S w pełnej dynamice sieciowej Net 💡 §9.2 Średni

---

15. Status twierdzeń — tabela sumaryczna

Twierdzenie Status
C¹(K_n) ≅ V_ρ ⊕ V_cyc ✅
V_cyc ≅ Λ²(V_ρ) ≅ 𝔰𝔬(V_ρ) ✅
Twierdzenie A (m_n = 1) ✅
Konsekwencja A (Hom(Sym²V_cyc, V_cyc) = 0) ✅
Twierdzenie B (branching) ✅
Twierdzenie C (T_b) ✅
Twierdzenie D (T_a) ✅
Twierdzenie E (asymetria) ✅
Stabilność architektury ✅
T_b nie przenosi się do continuum ✅
Klasyfikacja podgrup (K₄, K₅) ✅
D-R1, D-R3 ✅
Pełna tabela widm P_cyc\|_S ✅ §9.2
Tw. 4a — trywialność zagnieżdżenia ✅ §12.1
Wynik 3 — miękki próg ✅ §12.3
Wynik 4 — granica łączna Δ^(L) = λ_L δ ✅ §12.3
Klasyfikacja remisów ✅ §12.3′-a
Kompleksyfikacja: CᵀC = 4P_cyc ✅ §12H.3
Kompleksyfikacja: minimum (√2−1)δ 🔍 §12H.4
Kompleksyfikacja: T_δ ∩ Im(d_ℂ) = ∅ ✅ §12H.5
H-Bridge 💡

---

16. Historia wersji

Wersja Data Zmiana
v0.1 2026-08-23 Pierwsza wersja
v0.5 2026-08-23 D-R3
v0.6 2026-09-12 Wchłonięto §12A–§12G z Flow
v0.7 2026-09-13 Wchłonięto P₀-Hilbert jako §12H
v0.8 2026-09-13 **Przywrócono: §5.1 (historia błędu S₄), §9.2 (pełna tabela widm `P_cyc

---

P₀-Defect v0.8-formal-draft. Defekt relacyjny w C¹(K_n) z pełną klasyfikacją podgrup, twierdzeniem o znikaniu i kompleksyfikacją. Odwołania do innych filarów bez numeru wersji. Synteza: 2026-09-13.