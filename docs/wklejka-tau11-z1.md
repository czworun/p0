# Wklejka TAU-11-Z1: replikacja świeżych liczb strukturalnych 🔍 — sesja TAU-11, wątek P3 (krotności σ(t) vs reprezentacje D₃)

**Do:** DeepSeek / Asterion (GPT) — za pośrednictwem Leszka; Claude dołącza po przerwie (bez terminu). **Od:** warsztat P₀, szef lab. Vibe. **Data:** 2026-11-17 (runda 11ch).

## 0. Kontekst administracyjny

1. **Zlecenie:** niezależna replikacja (Z1) świeżych liczb strukturalnych warsztatu (status 🔍, sesja TAU-11, runda 11cg). Pytanie badawcze wątku P3 pochodzi z raportu §12 DeepSeeka (zastrzeżenie pkt 4, przyjęte do banku nasien w 11cf): obserwacja, że posortowane krotności wartości singularnych pary K₄ zmieniają się z t — **(1,1,2,1,2,2) przy t ∈ {0.1, 1} → (1,1,1,2,2,2) przy t=2** — z hipotezą autora: zmiana dominujących reprezentacji D₃ w widmie J·Jᵀ. Warsztat wykonał pełny rachunek od zera i zarejestrował wynik; **wartości są BLIND**: wklejka ich nie zawiera. Raportuj własne liczby; porównanie nastąpi po złożeniu raportów (wtedy też autor pytania otrzyma pełną odpowiedź rejestrową).
2. **Zasady rejestru (Z0–Z3):** droga ważniejsza niż cel; replikacja niezależna (implementacja od zera, wyłącznie z niniejszej specyfikacji); jawna konwencja; specyfikacja, nie kod. Statusy ✅/🔍 nadaje warsztat po rozliczeniu, nie wykonawca.
3. **BLIND-HIGIENA (lekcje 11bp/11cd):** jedyne wartości oczekiwane w tej wklejce to checkpointy §21 (korpus) oraz wartości TAU-10 dla pary K₄ (trzy zgodne strony: Vibe, Asterion (GPT), DeepSeek-PROXY). **ŻADNYCH wartości z rundy 11cg nie podajemy**: ani widm bloków, ani macierzy blokowych, ani czasów przejść, ani okien, ani składników parzystych/nieparzystych.
4. **STOP-rule:** każda niejednoznaczność specyfikacji → zgłoś STOP z opisem zamiast domyślać się konwencji (wzorzec E7). Znakowana rep permutacyjna nie gra roli; cała praca w zwykłej, bezznakowanej przestrzeni wartości krawędzi.
5. **Errata odczytu rejestru (Z2, wbudowana w zadanie):** krotności wartości singularnych raportować **z etykietą sektora** (A₁/E) — krotność bez etykiety jest niejednoznaczna.

## 1. Definicje (verbatim wg P0-Estrada v0.7, §18 — odczyt edge-native)

Ważony Laplasjan budowany wprost z wartości krawędzi D (nie przez potencjał wierzchołkowy):

- L(D)_{ij} = −w(D_{ij}) dla i ≠ j;  L(D)_{ii} = Σ_{j≠i} w(D_{ij});
- w_e = f(|D_e|),  f(r) = e^{−r};
- K_t = e^{−t·L(D)};  F_{W,t}(D)_{ij} = K_{ii} + K_{jj} − 2·K_{ij}.

Gładkość: przy |D_e| = 0 odczyt ma kink; próbkowane stany muszą mieć min |D_e| > 10⁻³.

## 2. Obiekty

**K₄** (kontrola konwencji): wierzchołki {0,1,2,3}; krawędzie w porządku kanonicznym: (0,1),(0,2),(0,3),(1,2),(1,3),(2,3). F_W ma 6 składowych (pary i<j). Sektor: C¹(K₄) = Im(d) ⊕ ker δ, wymiary 3+3 (ker δ: wymiar E−V+1 = 3).

**Para K₄ złączona wspólną ścianą** (obiekt testu; definicja z rejestru): **bipiramida trójkątna (K₅ bez jednej krawędzi)**. Wierzchołki {0,1,2,3,4}: szczyty 0 (strona A) i 4 (strona B), wspólna ściana {1,2,3}. Krawędzie (9, kanoniczny porządek): (0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(4,1),(4,2),(4,3). **Krawędzi (0,4) NIE MA**: para szczytowa (0,4) w F_W jest odległością czysto emergentną. F_W pary ma 10 składowych (wszystkie pary i<j, w tym (0,4)). Sektor: C¹(pary) = Im(d) ⊕ ker δ = 4+5.

**Punkt referencyjny:** D = 𝟙; t ∈ {0.1, 1, 2} (zadania A–C), siatka t dla zadania D jak niżej.

**Orbity krawędzi (definicje do zadań C–H):** orbita A = {(0,1),(0,2),(0,3)}; orbita B = {(4,1),(4,2),(4,3)}; orbita F (wspólna ściana) = {(1,2),(1,3),(2,3)}. Orbity par wierzchołkowych w wodzisku: te same trzy orbity po 3 pary + para szczytowa (0,4).

**Symetria S₃ i dekompozycja sektorowa (definicje):** grupa S₃ = permutacje wierzchołków wspólnej ściany {1,2,3} (działa na orbitach A, B, F jednocześnie; para (0,4) punkt stały). Każda orbita 3-elementowa rozkłada się na kierunek symetryczny (1,1,1)/√3 (sektor A₁) i jego uzupełnienie ortogonalne 2-wymiarowe (sektor E; wybór bazy dowolny, jawnie podany — wyniki niezmiennicze). Stąd **dziedzina ℝ⁹ = 3A₁ ⊕ 3E** (po jednej parze A₁⊕E na orbitę krawędzi), **wodzisko ℝ¹⁰ = 4A₁ ⊕ 3E** (trzy orbity par + odrębny blok 1-wymiarowy pary (0,4)). Przy każdym stanie S₃-symetrycznym (D stałe na orbitach) operator J = dF_W|_D jest S₃-ekwiwariantny; struktura blokowa w bazie sektorowej jest przedmiotem zadania C. Dodatkowa inwolucja ℤ₂ (zadanie H1): zamiana szczytów 0↔4 (z jednoczesną zamianą orbit A↔B, orbita F i para (0,4) nieruchome); przy stanie z w_A = w_B jest to symetria całego układu.

## 3. Zadania

**A. Bramka konwencji (K₄, jawna).** Oblicz J = dF_W|_{D=𝟙} przy t=1 dwiema drogami niezależnie: (a) różnice centralne, (b) pochodna Frécheta funkcji macierzowej expm metodą bloku 2n×2n (Al-Mohy & Higham, SIAM J. Matrix Anal. Appl. 30(4), 2009). RAPORT: rząd J; pełna lista wartości singularnych (6 cyfr znaczących); rangi sektorowe; maksymalna odchyłka względna między drogami. BRAMKA: zgodność z §21 (sekcja 5) do 10⁻⁶; niezgodność → STOP diagnostyczny.

**B. Bramka pary (checkpointy TAU-10, jawne).** Oblicz J pary przy D=𝟙, t ∈ {0.1, 1, 2} (macierz 10×9). RAPORT per t: rząd; wartości singularne (6 cyfr); κ = σ_min/σ_max; rangi sektorowe (4/5); wiersz (0,4) z rozbiciem na orbity A/B/F (6 cyfr). BRAMKA: zgodność z sekcją 5 do 10⁻⁶ (wartości sv, κ) i do 10⁻⁴ (wpisy wiersza (0,4)).

**C. Struktura Schura (BLIND, główne).** W bazie ortonormalnej sektorowej (sekcja 2; base: trzy A₁ dziedziny, trzy E dziedziny; wodzisko: 4 bloki A₁ w tym odrębny wiersz (0,4), trzy E) wyznacz J przy D=𝟙, t=1. RAPORT: (i) normy (lub max |wpisu|) wszystkich bloków skrośnych między sektorami A₁ i E (osobno dziedzina, osobno wodzisko); (ii) pełna macierz bloku E (6×6, 6 cyfr; jeśli wolisz, w formie opisanej); (iii) wartości własne/singularne bloku A₁ (bez wiersza (0,4) i z nim, jawnie) i bloku E (6 cyfr); (iv) porównanie: czy widmo pełnego J rozkłada się na widma bloków (odchyłka liczbowa)? Kontrolnie: powtórz (i)–(iii) dla jednego stanu S₃-symetrycznego z w_A ≠ w_B (własny wybór, jawny; np. w_A = 1.3·𝟙, w_B = 0.7·𝟙 na orbitach A/B, dowolne stałe na F).

**D. P3 — pytanie badawcze (BLIND, główne; autor hipotezy: DeepSeek).** W D=𝟙 wyznacz wartości singularne J (i przynależność sektorową każdej z nich: widmo bloku A₁ czy E) na siatce t ∈ [0.05, 3] o kroku nie większym niż 0.05 (gęstość lokalna do wyboru, jawna). RAPORT: (i) krotności wartości singularnych **z etykietą sektora** (A₁/E), w każdym punkcie siatki (wystarczy tabela przy zmianach + punkty krańcowe); (ii) posortowany wzór krotności po wartościach unikatowych (malejąco) — sektorami; (iii) czy w zakresie siatki występują zmiany porządku sortowania wartości między sektorami? Jeśli tak: **czasy przejść t\* z dokładnością co najmniej 10⁻³** (np. bisekcją; podać wspólne wartości sv w przejściu, 6 cyfr); (iv) kontrolnie: powtórz (i)–(iii) w jednym stanie S₃-symetrycznym z w_A ≠ w_B (jawnym) przy 3–5 punktach t wokół wykrytych przejść i porównaj wzory.

**H1. Opcjonalne, badawcze (BLIND): ℤ₂ 0↔4.** W D=𝟙 rozważ zamianę szczytów 0↔4 (sekcja 2). Rozłóż odpowiednie podprzestrzenie na składowe parzyste/nieparzyste względem tej inwolucji i opisz strukturę blokową oraz widma składowych (opis; twierdzeń nie formułować).

**H2. Opcjonalne, badawcze (BLIND): zależność od wag wspólnej ściany.** Dla stanu S₃-symetrycznego z w_A ≠ w_B (np. jak w C-kontrolce): czy F_W(0,4) i wpisy wiersza (0,4) w J zależą od wag orbity F? Przeskaluj same wagi orbity F przez c ∈ {0.5, 2.0, −0.8} i porównaj (raport: wartości przed/po, 6 cyfr; oraz pochodna ∂F_W(0,4)/∂c różnicami centralnymi).

**H3. Opcjonalne, badawcze (BLIND; bank nasien, kandydat P5): struktura bloku E przy złamanej zamianie A↔B.** W stanach S₃-symetrycznych z w_A ≠ w_B: opisz, które relacje między wpisami bloku E (lub jego postaci M⊗I₂, jeśli taką znajdziesz) łamią się, a które przeżywają (opisowa eksploracja; stan pojedynczy — hipotez nie formułować, twierdzeń nie nadawać).

## 4. Checkpointy TAU-10 (para K₄; trzy zgodne strony: Vibe 11cc, Asterion (GPT) 11ce, DeepSeek-PROXY 11cf)

- Wartości singularne J pary przy D=𝟙, t=1: (.6635067, .4318725, .2923045, .2923045, .2852585, .172749, .172749, .1169218, .1169218).
- rząd 9/9 przy t ∈ {0.1, 1, 2}; rangi sektorowe 4/5; κ = 0.206931 / 0.176218 / 0.119999 (t = 0.1/1/2).
- Wiersz (0,4) przy t=1: orbita A = orbita B = 0.122012 (na krawędź), orbita F ≈ 0 (rzędu 10⁻¹⁹; mechanizm domknięty analitycznie w 11cf).
- Eksploracja TAU-10: 720/720 pełnego rzędu (240 stanów U(−2,2), odrzut min |D_e| < 10⁻³, ×3 t).

## 5. Checkpoint §21 (K₄, korpus P0-Estrada v0.7)

- K₄, D=𝟙, t=1, baza ortonormalna: wartości singularne J = (.6756526, .3378263, .3378263, .3378263, .1689132, .1689132); rząd 6; rangi sektorowe 3/3; rząd 6 również przy t ∈ {0.1, 2}.
- Uwaga Z2 z dokumentu: macierz J §21 element-po-elemencie nie jest replikowalna (brak surowych wektorów bazowych g₂, g₃, z₁–z₃); rząd i wartości singularne są niezmiennikami bazy — tylko one są przedmiotem bramki.

## 6. Format raportu

Wg wzorca rejestru: (1) receipt zlecenia; (2) wyniki per zadanie z atrybucją każdej liczby (droga, ε, biblioteka + wersja, seed, liczba cyfr znaczących); (3) zastrzeżenia i STOP-y jawne; (4) wnioski opisowe bez nadawania statusów; propozycje numerowane P…, zarzuty A… jak zwykle.

## 7. Warianty wykonania (per wykonawca)

- **Asterion (GPT):** pełna numerika A–D; H1–H3 wg wyboru; obie drogi obowiązkowe w A, w B–D wystarczy jedna (jeśli druga potwierdzona w A).
- **DeepSeek:** pełna numerika A–D po uzyskaniu środowiska; dopuszczalne częściowo symbolicznie; dopuszczalna ścieżka PROXY wg wzorca §36 (v2): DeepSeek pisze kompletny skrypt z jawnych specyfikacji (seed jawnie), Leszek wykonuje mechanicznie bez edycji i zwraca surowy stdout verbatim, DeepSeek analizuje i składa raport z linią atrybucji „kod i analiza: DeepSeek; wykonanie proxy: Leszek". H1–H3 wg wyboru (H3 szczególnie mile widziane — bank nasien).
- **Claude:** po przerwie; bez terminu; jego trzecia kontrola mile widziana.
- Bez pośpiechu, bez terminu.