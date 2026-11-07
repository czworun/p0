# MVP-01 — specyfikacja v0.1 (pre-registracja kryteriów falsyfikacji; DO ATAKU modeli)

> Status: **v0.1 — dokument do ataku**, nie do rachunków. Zasada nadrzędna (Z0): droga ważniejsza niż cel — chronimy procedurę, nie wynik (maksyma GPT/Asterion z rundy 7, przyjęta jako reguła projektowa testu). v1.0 powstanie po rozliczeniu ataków trzech modeli i rozstrzygnięciu blokerów Z3 (§2). **Żaden rachunek testowy (w tym model zerowy) nie startuje przed zamrożeniem v1.0** (K6).
>
> Semantyka rejestru: **ρ = |λ₂| subdominanta**, nie promień spektralny (PF dominanta = trywialna 1, ker(R−I)=1). Konwencja po doprecyzowaniu DeepSeeka, runda 8.

## §0. Obiekty zamrożone (warstwa TAU-8, erraty v2–v4; fingerprinty z zamknięcia rundy 7)

Geometria exact Z[φ] (tabela v3, errata E8), 12 wierzchołków ikosaedru, ściana ⇔ d²=4, 20 ścian w porządku leksykograficznym (f0=[0,1,2]=F₀), blok W_nat, konwencja kolumnowa R=∏F/256 (F z lewej, ściany lex), tetr [P₀,v₂,v₁,v₀] (apex-first, Węzeł-0), 1 tetr = 4 takty, runda węzła = 80 taktów. Para: 23 punkty, Atp=[12,f₂,f₁,f₀], Btp=[22,w₂,w₁,w₀] (w=τ(ściana) posortowane; B-kanon — konwencja rundy 6), R_AB=S_B·S_A.

Fingerprinty (≥2 niezależne numeryki każda):
- **Węzeł-0:** ρ=0.174758932129 (rz., prosta); tr(R)=1.288968534521200119; ℓ(P₀)=0.037549919; det=2⁻¹⁶⁰=6.842277657836021·10⁻⁴⁹; tr(R₄)=7.570777927758172 (identyczna w obu konwencjach tetry — własność obiektu).
- **Para:** ρ(R_AB)=0.554641699189; dalej 0.113966222525; 0.075612350056; 0.073594090076±0.004120959044i; partycje Perrona ℓ(P₀ᴬ)=ℓ(P₀ᴮ)=0.022750332, ℓ(F₀)=0.211738028, ℓ(A-only)=ℓ(B-only)=0.371380653; ker(R_AB−I)=1; ker(S_A−I)=11 konstrukcyjnie.
- **Cut (obustronne odcięcie f0 z obu sweepów; 38 tetr, 152 takty):** ρ_cut=0.550107704834 — runda 8: niezależna rekonstrukcja Vibe (exact char poly BigInt + Durand–Kerner) vs GPT 0.550107705, zgodność 9 miejsc; dalsze subdominanty cut: 0.111748869766; 0.077838995626.
- **Bramki (rekonstrukcja 2-regularna, zbiory ścian lex):** G0={0,3,6,9,11,13,17,19} ρ=0.271135751587 (moduł pary 0.270223674±0.022220751i); G1={0,4,7,8,10,14,16,19} ρ=0.268753058672 (rz.); G2={1,2,7,9,12,15,16,17} ρ=0.328097227134 (para 0.321351939±0.066187020i); G3={1,3,5,8,10,11,15,18} ρ=0.287367993554 (para 0.285951363±0.028498807i); G4={2,4,5,6,12,13,14,18} ρ=0.298483949744 (rz.).

**Fakt geometryczny nowy (runda 8, exact):** każda para bramek współdzieli dokładnie 2 ściany i są to ściany antypodalne (G0∩G1={0,19}, G0∩G2={9,17}, G0∩G3={3,11}, G0∩G4={6,13}, G1∩G2={7,16}, G1∩G3={8,10}, G1∩G4={4,14}, G2∩G3={1,15}, G2∩G4={2,12}, G3∩G4={5,18}); każda ściana należy do dokładnie 2 bramek; |G∪G'|=14 dla każdej pary. **Nie istnieją pary bramek rozłączne.** Graf dwunastościanu środków ścian: 30 krawędzi, 3-regularny, rozkład odległości wierzchołków 30×1 + 60×2 + 60×3 + 30×4 + 10×5 (średnica 5; wszystkie 10 par ścian antypodalnych na odległości 5).

## §1. MVP-01a (etap złącza) — hipoteza i pre-registracja kryteriów

**H_a (operacjonalizacja komponentu hipotezy roboczej „kanał wierzchołkowy dominuje" w obiekcie pary):** w transmitancji przez złącze pary (A↔B) transport idzie kanałem wierzchołkowym — tożsamością współdzielonych punktów 0,1,2 (definicja strukturalna: podprzestrzeń złożona z identyfikacji punktów, niezależna od widma R) — a kanał ścianowy (aktualizacje wspólnej tetry F₀ jako bloki w obu sweepach) wnosi wkład marginalny.

**1.1 Miara (jedna, zero swobód):** U_f = 1 − ρ_cut/ρ_AB — względny wkład obustronnego odcięcia bloków wspólnej tetry w lukę subdominanty. Wartość miary na obiekcie jest publiczną, deterministyczną funkcją zamrożonych fingerprintów: **U_f = 0.008174637** (znana od rundy 8; ślepość protokołu nie dotyczy jej — obie składowe są w rejestrze od rundy 7 — lecz progu τ_z i rozkładu zerowego, które pozostają niepoliczone do zamrożenia v1.0).

**1.2 Model zerowy (K2 — matched null, najsilniejsza forma: komplet, nie losowanie):** wszystkie 361 par odcięć (t_A, t_B), t_A ∈ 19 ścian sweepu A bez f0, t_B ∈ 19 ścian sweepu B bez f0ᴮ; w każdej realizacji N_z = S_B(t_B odcięta)·S_A(t_A odcięta), ρ_z z exact wielomianu charakterystycznego (Newton/Leverrier, arytmetyka całkowitoliczbowa) + Durand–Kerner (metoda referencyjna E18b; iteracja odwrotna i iloraz Rayleigha ZAKAZANE dla estymacji ρ — lekcja E18b), U_z = 1 − ρ_z/ρ_AB. Rozkład pełny (brak generatora, brak seedu, brak parametrów): mediana_z = wartość U_z o randze 181 (sort rosnąco, n=361); τ_z = wartość o randze ⌈0.95·361⌉ = 343.

**1.3 Trzy kategorie wyniku (z góry, K3/C3 — kill criterion jawny):**
- **U_f < mediana_z ⇒ POTWIERDZENIE SILNE** — odcięcie wspólnej tetry wpływa na lukę subdominanty mniej niż typowe losowe podwójne odcięcie: kanał ścianowy interfejsu nie ma nadzwyczajnego statusu; dominacja kanału wierzchołkowego.
- **mediana_z ≤ U_f ≤ τ_z ⇒ POTWIERDZENIE SŁABE** — wspólna tetra typowa w rozkładzie; brak dowodu szczególnej istotności kanału ścianowego, ale też brak dowodu jego wyjątkowej nieistotności.
- **U_f > τ_z ⇒ OBALENIE** — wspólna tetra istotniejsza niż 95% losowych odcięć podwójnych: kanał ścianowy wnosi w lukę więcej niż typowa tetra; dominacja wierzchołkowa w tej postaci niepotwierdzona. **„Obalona" znaczy obalona — nie rewidowana, nie „do doprecyzowania".**

Kategoria czwarta (wynik nierozstrzygający) istnieje tylko przy degradacji rozkładu zerowego (np. τ_z = 0 przy degeneracji numerycznej ogonów) — wtedy jawna deklaracja i powtórzenie rachunku zerowego metodą exact z podwyższoną precyzją współczynników, przed jakąkolwiek interpretacją.

**1.4 Czystość dekompozycji (K1):** kanały zdefiniowane strukturalnie (tożsamość punktów = geometria przestrzeni stanu; bloki F₀ = struktura operatora), nie przez widmo R_AB ani wybór modów. Rozkład spektralny obiektu nie uczestniczy w definicji kanałów.

**1.5 Niezależność od przypadków (K4):** etap złącza nie używa bramek testowych; definicje kanałów nie zależą od wyboru pary odcięć; przypadek testowy jeden (para B-kanon) i jeden (cut F₀) — komplet z góry (K7): 1 obiekt, 1 miara, 361 realizacji zerowych wypisanych kombinatorycznie (brak wyboru).

**1.6 Symetryczność testu alternatywy (K5):** alternatywa face-dominant operacjonalizowana jako przeciwieństwo w tej samej miarze (U_f > τ_z); test symetryczny: każdy wynik wpada do jednej z trzech kategorii; „nieodróżnialność" nie istnieje strukturalnie (miara i prógi jednoznaczne), a jedyna forma nierozstrzygalności (degradacja zerowa) jest z góry zdefiniowana (1.3, akapit 2).

**1.7 Ślepy protokół (K6):** treść §0+§1 w wersji v1.0 (po ataku) jest hashowana SHA-256; hash publikuje Leszek (relay) w rozmowie i w rejestrze PRZED startem rachunku zerowego; rachunek zerowy (361× exact char poly + DK) wykonywany dopiero po publikacji hasha; porównanie U_f z (mediana_z, τ_z) i klasyfikacja — jedyna interpretacja, bez kontaktu z rachunkiem po fakcie.

**1.8 Liczba swobodnych parametrów (K8):** zero. Obiekty zamrożone (§0), miara jedna (1.1), prógi wyłącznie z pełnego rozkładu zerowego (percentyle 50/95 zamrożone z góry; n=361 wyznaczone kombinatorycznie). Stale protokołu (percentyl, ranga) nie są parametrami dopasowania — nie ma czego dopasowywać.

**1.9 Odpowiedzi na warunki Claude'a (C1–C5):** C1: konwencja jedna (§0, Węzeł-0 + B-kanon), fingerprinty krokowe k≥4 obowiązkowe przy każdej replikacji (E15); C2: kryterium liczbowe z progiem i metodą (1.1–1.3: miara, progi, metoda exact z E18b — wszystko przed rachunkiem); C3: kategorie przeciwnego wyniku z góry (1.3); C4: kontrola zerowa = model zerowy 1.2 (matched null w tym samym obiekcie: identyczne stopnie, topologia, budżet aktualizacji — różni się wyłącznie miejscem odcięcia); C5: rozdzielenie rachunku od interpretacji — rachunek daje U_f i klasyfikację; teza „kanał wierzchołkowy dominuje w sensie nośnika fizycznego" jest tezą wyższego rzędu, wymaga etapu b (§2) i nie wynika z samej liczby.

**1.10 Odpowiedzi na warunki GPT/Asteriona (A1–A5):** A1: „dominacja" zdefiniowana jako miara U_f względem progu z rozkładu zerowego — nie wartość własna, nie propagacja, nie masa Perrona; pojęcia nie są zamienne i nie są używane; A2: porównywalność kanałów zapewniona konstrukcyjnie — oba kanały w tym samym operatorze i przestrzeni, brak osobnych budżetów i normalizacji; A3: konfound stopni: obiekt w teście i w nullu identyczny (matched null eliminuje różnice stopni z PORÓWNANIA), ale interpretacja fizyczna pozostaje oddzielona (C5) — wpływ stopni wspólnych wierzchołków (10 vs 6) na kształt trybu kontrastu jest jawno zapisanym ograniczeniem etapu a, do rozstrzygnięcia w etapie b; A4: kryterium falsyfikacji z góry (1.3); A5: kolejność aktualizacji zamrożona w §0 (konwencja kolumnowa, lex, F z lewej) — każda zmiana kolejności to inny obiekt i wymaga własnego fingerprintu; badanie wrażliwości na kolejność jest legalnym polem ataku na v0.1, ale nie zmienną testu.

**1.11 Odpowiedzi na ataki DeepSeeka (K1–K8):** K1→1.4; K2→1.2 (null komplet w tym samym obiekcie, mocniejszy niż losowe grafy o tych samych stopniach); K3→1.3 („obalona = obalona"); K4→1.5; K5→1.6; K6→1.7; K7→1.5 i 1.2 (komplet kombinatoryczny, brak wyboru); K8→1.8. Deklaracja DeepSeeka („bez K1–K8 nie składam słoja") — spełniona punkt po punkcie; słój będzie złożony wyłącznie na v1.0 po jego ataku.

## §2. Etap b (bramki w pojedynczym węźle; pełna hipoteza robocza) — BLOKERY Z3, do rozstrzygnięcia przez właściciela korpusu

Hipoteza robocza z rejestru: „MVP-01: transport przez pojedynczy węzeł, bramki przeciwległe — kanał wierzchołkowy dominuje; nośnik: przepływ wokół ściany-bramki w V_cyc (opcja a)". Etap b NIE zostanie sformalizowany w v0.1, bo brakuje definicji korpusu (Z3: brak w specyfikacji = zgłoś, nie zgaduj). Blokery jawne:

1. **Definicja bramek autora (Z2):** notatnik warsztatowy mówi o sąsiedztwie bramek (5,1) i 28 parach — rekonstrukcja 2-regularna daje 5 bramek, 10 par, każda para współdzieli dokładnie parę antypodalną ścian (§0), zero par „sąsiednich" w sensie wspólnych krawędzi. Wymagany jawny spis definicji bramek autora.
2. **Nośnik V_cyc:** „przepływ wokół ściany-bramki w V_cyc (opcja a); skalar tylko benchmark" — wymagane definicje V_cyc i nośnika z notatników (Net v0.6.1, Estrada §36).
3. **Stan wejścia z bramki:** bramki są NIEODRÓŻNIALNE jako pobudzenia wierzchołkowe (2-regularność ⇒ każda bramka daje jednolity rozkład 1/12 na wierzchołkach) — stan 13-punktowy nie koduje wyboru bramki; wymagana reprezentacja ścianowa (20-dim) lub nośnik V_cyc.
4. **„Kanały 0→5→11→24"** (kontekst publikacyjny lematu jąder) — wymagana definicja i relacja do etapu b.
5. **Materiał warsztatowy:** [warsztat/tau-8-siec-12sasiadow.md](../warsztat/tau-8-siec-12sasiadow.md) — plik wskazany w rejestrze, nie istnieje w repo; do przekazania przez właściciela.

Do rozstrzygnięcia przed v1.0: etap b wchodzi do v1.0 (po dostarczeniu definicji) albo v1.0 = wyłącznie etap a, a etap b staje się MVP-02.

## §3. Podział ról (propozycja GPT/Asteriona z rundy 8, przyjęta)

- **DeepSeek:** kontrprzykłady i kryteria — atak na v0.1; deklaracja słojowa wiąże (1.11).
- **Claude:** symetrie, przestrzenie stanów, poprawność definicji — atak na v0.1.
- **GPT/Asterion:** niezależna analiza operatorów, kolejności aktualizacji i artefaktów — atak na v0.1.
- **Vibe (szef lab.):** autor protokołu — odpowiada na wszystkie trzy krytyki przed zamrożeniem v1.0; wykonuje rachunek zerowy metodą referencyjną E18b po publikacji hasha.
- **Leszek:** relay; materiały warsztatowe (§2.5) i rozstrzygnięcia definicyjne właściciela korpusu.
- Żaden model nie wykonuje rachunków transportowych przed zamrożeniem v1.0; wartości zamrożone w §0 są jedynymi liczbami w obiegu.

## §4. Tabela odpowiedzi na ataki (skrót)

| Atak | Odpowiedź | Miejsce |
| --- | --- | --- |
| K1 dekompozycja strukturalna | kanały = tożsamość punktów / bloki F₀, nie widmo | 1.4 |
| K2 próg z modelu zerowego | komplet 361, matched null w tym samym obiekcie | 1.2 |
| K3 jawny kill criterion | trzy kategorie, „obalona = obalona" | 1.3 |
| K4 niezależność od bramek testowych | etap a bez bramek; komplet kombinatoryczny | 1.5 |
| K5 test symetryczny vs face-dominant | alternatywa = to samo miarą, brak nieodróżnialności strukturalnej | 1.6 |
| K6 blind protocol + SHA-256 | hash §0+§1 v1.0 publikowany przed rachunkiem zerowym | 1.7 |
| K7 pre-registracja przypadków | 1 obiekt, 1 cut, 361 realizacji wypisanych | 1.5, 1.2 |
| K8 liczba swobód hipotezy | zero | 1.8 |
| C1 jedna konwencja | Węzeł-0 + B-kanon, fingerprinty k≥4 | §0, 1.9 |
| C2 próg i metoda z góry | miara + percentyle + E18b exact | 1.1–1.3, 1.9 |
| C3 kategorie z góry | potwierdzenie silne / słabe / obalenie (+degradacja) | 1.3 |
| C4 kontrola zerowa | matched null | 1.2, 1.9 |
| C5 rachunek ≠ interpretacja | U_f vs teza nośnikowa | 1.9 |
| A1 definicja dominacji | miara U_f, nie λ/propagacja/masa | 1.10 |
| A2 porównywalność kanałów | jeden operator, jedna przestrzeń | 1.10 |
| A3 konfound stopni | matched null + jawne ograniczenie interpretacyjne | 1.10 |
| A4 kryterium falsyfikacji | 1.3 | 1.10 |
| A5 kontrola kolejności | kolejność zamrożona; wrażliwość = legalny atak | 1.10 |

*Wersja v0.1, 2026-11-07. Autor: Vibe (szef laboratorium P₀). Identyfikator wersji (SHA-256 treści): podawany przez relay przy publikacji.*
