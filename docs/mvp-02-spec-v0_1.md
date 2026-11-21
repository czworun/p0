# MVP-02 — specyfikacja v0.1 (etap b programu transportowego; DO ATAKU modeli)

> Status: **v0.1 — dokument do ataku**, nie do rachunków. Start MVP-02 wydany przez właściciela (2026-11-21); ten dokument rozpoczyna pierwszą rundę warsztatu i formalnie kończy przerwę. Z0: droga ważniejsza niż cel. Z2: jawne konwencje. Z3: specyfikacje, nie kod. Liczby jawnym tekstem, potęgi notacją a^b, zero LaTeXu. **Żaden rachunek transportowy (w tym model zerowy) nie startuje przed zamrożeniem v1.0** (K6).
>
> Podstawa źródłowa: mvp-01-spec v0.9 §2 (definicja etapu b); **hash v1.0 [MVP-01] wiążący: 4014497a9614798030d61ee16471f6c773d612515bdc1293ae7a16d32bfb28f2** (zamrożenie runda 11al, kwalifikacja §1.10 PASS runda 11an, rachunek zerowy E18b rozliczony runda 11bh: WYNIK TYPOWY, „F₀ nierozróżnialna od typowego odcięcia tą miarą"; H_a ani potwierdzona, ani obalona). Semantyka rejestru: **ρ = |λ₂| subdominanta** (konwencja utrzymana z etapu a).
>
> Pakiet zaległych errat rejestru wchodzi w tej samej rundzie, PRZED bindem (lista wg rejestru; nie zmienia zamrożonych obiektów §0).

## §0. Obiekty zamrożone

**0.1 Czas i porządki (dziedziczone z v1.0 etapu a, bez zmian konwencji).** Geometria exact Z[φ], 12 wierzchołków ikosaedru, ściana ⟺ d² = 4, 20 ścian w porządku leksykograficznym (f0 = [0,1,2] = F₀), tetr [P₀,v₂,v₁,v₀] (apex-first, P₀ ostatnie), 1 tetr = 4 takty, runda węzła = sweep 20 tetr lex = 80 taktów. Węzeł = 12 wierzchołków + P₀ = 13 punktów. Konwencja kolumnowa R = ∏F/256.

**0.2 Węzeł-0: fingerprinty (✅, z §0 v1.0; nie przeliczać na nowo, porównywać z bramką sanity).** ρ = 0.174758932129 (rzeczywista prosta); tr(R) = 1.288968534521200119; ℓ(P₀) = 0.037549919; det = 6.842277657836021·10^-49 strukturalnie 2^-160; tr(R₄) = 7.570777927758172. Skala czasów (kontrakcja/takt): K₄ 0.6424 > para K₄ 0.8217 > bramka ~0.96 > węzeł 0.9784 > para węzłów 0.9963.

**0.3 Bramki (konwencja warsztatowa, KANONICZNA decyzją właściciela korpusu, 2026-11-21).** Bramka = 8 z 20 ścian ikosaedru dualnie odpowiadających wierzchołkom jednego z 5 sześcianów wpisanych w dwunastościan. Zbiory ścian lex: G0={0,3,6,9,11,13,17,19}, G1={0,4,7,8,10,14,16,19}, G2={1,2,7,9,12,15,16,17}, G3={1,3,5,8,10,11,15,18}, G4={2,4,5,6,12,13,14,18}. ρ_gate (na 32 takty, zgodnie ze sweepem bramki): G0 0.271135751587 (para 0.270223674±0.022220751i), G1 0.268753058672 (rz.), G2 0.328097227134 (para 0.321351939±0.066187020i), G3 0.287367993554 (para 0.285951363±0.028498807i), G4 0.298483949744 (rz.).
Własności (✅ 3 pełne enumeracje + dowód symetriowy): dokładnie 5 orientacji (120/24); stabilizator T_h (≅ A₄×C₂, rząd 24), parzysta względem −I ⇒ brak chiralności z samej orientacji; każda ściana w dokładnie 2 bramkach; każda para bramek współdzieli dokładnie 2 ściany antypodalne; nie istnieją pary rozłączne ani sąsiednie; odległości par bramek (graf dwunastościanu środków ścian) wyłącznie 2/3/5; 4 pary bramek przeciwległych (odległość 5 = średnica; to pary PRZECIWLEGŁE etapu b); rozkład 28 par ścian w bramce: 12×dł.2, 12×dł.3, 4×dł.5. Orientacja ścian CCW-z-zewnątrz (po erracie Φ_D).
KONWENCJA-ERRATY włączone: S-1 (stabilizator T_h, nie O_h/T_d; „sąsiedztwo (5,1)" notatnika = błąd komórki roboczej, 0 par sąsiednich) i S-2 (pary uporządkowane 56 = 2·C(8,2), konwencja jawna).

**0.4 Nośnik: V_cyc ikosaedru (✅, TETRA-20 + STALK).** V_cyc = 19-dim, dekompozycja T1g ⊕ T2g ⊕ G_g ⊕ G_u ⊕ H_u; widmo L_cyc: {4.9784; 6×2; 3×7.3333; 7.6; 8.0883; 11×10}, ślad 164.6667 = 494/3; 6 unikatowych częstości √λ = {2.2312, 2.4495, 2.7080, 2.7568, 2.8440, 3.1623}. NOTA STRUKTURALNA: V_cyc ikosaedru ≇ Λ²(V_ρ) (19 ≠ 55; Tw. A dotyczy K_n). Kanały Hom_G(Sym²V_cyc, V_cyc): ikosaedr I_h = 24; drabina podgrup 0(K₄,S₄)→5(para,D₃h)→11(para uporządkowana,C₃v)→24(ikosaedr,I_h) jako kontekst publikacyjny lematu jąder; para K₄ = najmniejszy zbadany układ o niezerowym Hom.

**0.5 Rama transportowa autora (materiał warsztatowy; liczby 🔍 do replikacji Z1).** Operator trasy R(ścieżka) na przestrzeni 13-dim jako iloczyn operatorów per ściana; czas przejścia ikosaedru c = 16 taktów; Var(cykl)/Var(takt) = 1/4; trasy 4-ścianowe: 12 par w 5 klasach faz {21.1633, 33.1690, 33.7986, 39.1308, 55.4411} stopni; wachlarze (4 z 5 ścian wokół osi; 8 silnych); rozstrzygnięcia TAU-8: sweep bramki = 32 takty, porty różnią się tempem ~22%. Z2: konwencje autora wzięte verbatim albo jawnie od nich odstąpione.

**0.6 Materiał warsztatowy TAU-8 (plik w repo).** docs/warsztat/tau-8-siec-12sasiadow.md: konwencja obiektu (M_local, porządek w tetrze, det = 256^-20), bramki sanity, liczby-kotwice (SERC; ρ węzła 0.174759; ρ pary 0.554642; ρ_cut 0.550108; λ₂ grafów).

## §1. Etap b: hipoteza i obserwable

**H_b (robocza; rejestr tury 6 + Lattice §5 pkt 2):** transport przez POJEDYNCZY WĘZEŁ (Węzeł-0) między parą bramek PRZECIWLEGŁYCH (odległość 5 powierzchniowo; wnętrze konkuruje z powierzchnią) idzie nośnikiem: **przepływ wokół ściany-bramki w V_cyc (opcja a, decyzja właściciela z tury 6)**; skalar tylko benchmark; tensor ≥ 4 stopnia odłożony do warstwy nieliniowej. Teza o fizycznym nośniku transportu = pole 3 raportu (w etapie a zarezerwowane dla MVP-02).

**Obserwable (operacjonalizacja GPT, Lattice §5, przyjęta):** impuls o jawnie określonym składzie modalnym; osobno transport powierzchniowy i liniowa dynamika V_cyc; wspólna definicja czasu, porównywalna normalizacja, jawne kryterium detekcji; pomiar: czas pierwszego przekroczenia progu, amplituda, energia, skład modalny; powtórzenia dla innych par bramek i innych impulsów.

**Test T2 (nieliniowość; kandydat, po fazie liniowej; falsyfikowalny jednym uruchomieniem):** przy ε = 0 wyjście ⊆ wejście (projekcja), przy ε > 0 zawartość stopnia >2 większa od wejścia. Setup z notatnika „7 atraktorów": velocity-Verlet, dt = 0.002, ε = γ = 20, projekcja P_cyc co krok, blowup 10^6, kryterium atraktora = mediana ‖x‖ drugiej połowy, wzorce przez projektory P_irrep.

**Protokół taktowy (errata tury 8, bez wyjątków):** każde porównanie tempa podaje kontrakcję i na rundę, i na takt elementarny.

## §2. Status operacjonalizacji (jawny)

**2.1 Rozstrzygnięte decyzją właściciela (2026-11-21):** (i) konwencja bramek §0.3 KANONICZNA (spis zbiorów bramek autora nie jest warunkiem); (ii) zakres potwierdzony: obiekt testowy = Węzeł-0 + para bramek przeciwległych; nośnik opcja (a); obserwable jak §1.

**2.2 Stan wejścia z bramki (wskazany przez decyzję nośnika).** Bramki są NIEODRÓŻNIOWALNE jako pobudzenia wierzchołkowe (2-regularność ⇒ każda bramka daje jednolity rozkład 1/12 na wierzchołkach); stan 13-punktowy nie koduje wyboru bramki. Stan wejścia = cyrkulacja wokół ściany-bramki w V_cyc. DO ROZSTRZYGNIĘCIA przed v1.0: dokładna definicja cyrkulacji per bramka (konwencja znaku/orientacji jawna, Z2); reprezentacja ścianowa 20-dim jako kandydat kontrolny.

**2.3 Miara i model zerowy (GŁÓWNE ZADANIE WARSZTATOWE tej rundy).** Miara i model zerowy etapu b NIE ISTNIEJĄ dotąd: U_f i rozkład 361 par dotyczyły złącza pary węzłów (etap a), nie transportu wewnątrz jednego węzła. Rygory dziedziczone: miara jedna, zero swobód (analog U_f), matched null w tym samym obiekcie, kill criterion jawny z góry, komplet a nie losowanie, ślepy protokół z hashem. Materiał częściowy (z rejestru etapu a): przez złącze przechodzi tylko składowa na współdzielonym cyklu; udział energii nie uniwersalny (1/5 z wymiarów; 1/3 tylko przy rozkładzie jednostajnym; cykl boczny 1/9). Kolejność: atak na v0.1 (§4) → projekt miary w v0.2 (pre-registracja kryteriów) → atak na v0.2 → v1.0 i bind → rachunek zerowy.

**2.4 Transformacja nośnika (a) pod −I (GO z tury 13).** Pytanie otwarte dla ataku: nośnik wchodzi do sprzężenia jako M_e(g) czy det(g)·M_e(g); anty-Φ_D (✅ twierdzenie algebraiczne pnia) jako kandydat nośnika chiralności.

**2.5 P8 (decyzja szefa lab., w ramach delegacji):** v0.1 i v0.2 jako JEDEN plik (atak i erraty na jednym dokumencie); podział na cztery pliki tylko przy v1.0, jeśli objętość go uzasadni (zmiana hasza następuje wtedy i tak).

**2.6 Model odcięć krawędziowych (decyzja szefa lab.):** ZOSTAJE W BANKU NASIEN; nie jest operacjonalizowany w etapie b (K8: zero dodatkowych swobód); kandydat osobnego zlecenia po etapie b.

## §3. Rygory (dziedziczone, wiążące)

- **K1 dekompozycja strukturalna:** kanały/nośnik zdefiniowane strukturalnie (geometria przestrzeni stanu), nie przez widmo R ani wybór modów.
- **K2 matched null w tym samym obiekcie:** identyczne stopnie, topologia, budżet aktualizacji; różni się wyłącznie testowana własność.
- **K3 kill criterion jawny:** kategorie wyniku z góry; „obalona znaczy obalona".
- **K4/K7 kompletność:** komplet kombinatoryczny, brak generatora, brak seedu, brak wyboru przypadków.
- **K5 test symetryczny:** alternatywa operacjonalizowana tą samą miarą.
- **K6 ślepy protokół:** treść §0+§1 (od v0.2 także miara i rozkład zerowy) hashowana SHA-256; hash publikowany przez Leszka PRZED rachunkiem; rachunek zerowy po publikacji hasha.
- **K8 zero swobodnych parametrów:** obiekty zamrożone, miara jedna, progi z pełnego rozkładu zerowego.
- Bramki sanity przed każdym rachunkiem (lekcja transkrypcyjna: jeden znak w M_local zmieniał każdą liczbę); metoda referencyjna exact (E18b: char poly + Durand–Kerner; iteracja odwrotna i iloraz Rayleigha zakazane dla estymacji ρ).
- Raport w trzech polach rozdzielonych; pole (3) = teza fizyczna: tu swojego odbiorcę ma.

## §4. Podział ról ataku (na v0.1; wzorzec §3 v0.1 etapu a)

- **DeepSeek:** kontrprzykłady i kryteria — atak na v0.1, w tym na projektowane pole miary (2.3); deklaracja słojowa wiąże.
- **Claude:** symetrie, przestrzenie stanów, poprawność definicji — atak na v0.1, w tym transformacja nośnika pod −I (2.4) i definicja cyrkulacji (2.2).
- **GPT/Asterion:** niezależna analiza operatorów, kolejności aktualizacji i artefaktów — atak na v0.1.
- **Vibe (szef lab.):** autor protokołu; po rozliczeniu ataków projekt miary i modelu zerowego (v0.2); rachunek referencyjny po publikacji hasha.
- **Leszek:** relay; rozstrzygnięcia właściciela.
- Żaden model nie wykonuje rachunków transportowych przed zamrożeniem v1.0; wartości zamrożone w §0 są jedynymi liczbami w obiegu.

*Wersja v0.1, 2026-11-21. Autor: Vibe (szef laboratorium P₀, delegacja Leszka). Zaległe erraty rejestru: w tej rundzie, przed bindem, wg listy rejestrowej.*
