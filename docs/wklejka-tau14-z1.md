# Wklejka TAU-14-Z1: replikacja mapy crossingów w rodzinie S₃-symetrycznej 🔍 — sesja TAU-14, wątek DS P2 (powierzchnie crossingów w trójkącie projectivnym)

**Do:** Asterion (GPT) / DeepSeek — za pośrednictwem Leszka; Claude dołącza po przerwie (bez terminu). **Od:** warsztat P₀, szef lab. Vibe. **Data:** 2026-11-17 (runda 11cm).

## 0. Kontekst administracyjny

1. **Zlecenie:** niezależna replikacja (Z1) świeżych wyników 🔍 sesji TAU-14. Pytanie badawcze pochodzi z banku nasien (wątek DS P2, zgłoszony w 11ci, rama z twierdzenia T13-1 z 11ck): **crossingi w rodzinie S₃-symetrycznej jako obiekt geometryczny — liczba i położenie przejść widmowych jako funkcja parametrów rodziny (w_A, w_B, w_F, t) i znaków D per orbita.** Warsztat wykonał pełny rachunek od zera (sesja TAU-14) i zarejestrował wynik; **wartości są BLIND**: wklejka ich nie zawiera poza checkpointami sekcji 4. Raportuj własne liczby; porównanie nastąpi po złożeniu raportów.
2. **Zasady rejestru (Z0–Z3):** droga ważniejsza niż cel; replikacja niezależna (implementacja od zera, wyłącznie z niniejszej specyfikacji); jawna konwencja; specyfikacja, nie kod. Statusy ✅/🔍 nadaje warsztat po rozliczeniu, nie wykonawca.
3. **BLIND-HIGIENA (lekcje 11bp/11cd):** jedyne wartości oczekiwane w tej wklejce to checkpointy sekcji 4: §21 (korpus K₄), TAU-10 (para K₄; trzy zgodne strony: Vibe, Asterion (GPT), DeepSeek-PROXY), T13-1 (crossingi w D = 𝟙; twierdzenie z 11ck), stan Asteriona (0.2, 0.8, 1.0) per orbita (jego własny wynik z 11ci/11ck). **ŻADNYCH wartości z sesji TAU-14 nie podajemy**: ani rozkładów liczby crossingów, ani histogramów, ani konkretnych kierunków, ani położeń szczególnych, ani wzorów na odstępy krzywych.
4. **STOP-rule:** każda niejednoznaczność specyfikacji → zgłoś STOP z opisem zamiast domyślać się konwencji (wzorzec E7).
5. **Errata wklejek — rozróżnienie D vs w (lekcja 11ci, wbudowana):** w zadaniach podajemy **D = wartości krawędzi**; wagi zawsze wg §1: w = e^{−|D|}. Wyjście poza tę klasę (np. ujemne wagi, c < 0) — niedopuszczalne.
6. **Errata sign(D) (lekcja 11cj, wbudowana):** pochodna wagi: ∂w/∂D = −sign(D)·w (nie −w). Dotyczy każdej drogi analitycznej pochodnej (Frécheta, różnice centralne jej nie dotyczą).
7. **Higiena numeryczna map (wymóg protokołu, przed skanem):** przy dużych skalach czasu wartości singularne J zanikają eksponencjalnie; poniżej pewnego poziomu względne fluktuacje numeryczne mogą generować **fałszywe przejścia porządku**. Każdy skan w zadaniach D–F musi deklarować jawny **próg słyszalności** (dolny cutoff sv względem szczytu widma w danym punkcie) ustalony PRZED skanem, oraz kontrolę stabilności (sekcja 3, zadanie D pkt b).

## 1. Definicje (verbatim wg P0-Estrada v0.7, §18 — odczyt edge-native)

Ważony Laplasjan budowany wprost z wartości krawędzi D (nie przez potencjał wierzchołkowy):

- L(D)_{ij} = −w(D_{ij}) dla i ≠ j;  L(D)_{ii} = Σ_{j≠i} w(D_{ij});
- w_e = f(|D_e|),  f(r) = e^{−r};
- K_t = e^{−t·L(D)};  F_{W,t}(D)_{ij} = K_{ii} + K_{jj} − 2·K_{ij}.

Gładkość: przy |D_e| = 0 odczyt ma kink; próbkowane stany muszą mieć min |D_e| > 10⁻³.

## 2. Obiekty

**K₄** (kontrola konwencji): wierzchołki {0,1,2,3}; krawędzie w porządku kanonicznym: (0,1),(0,2),(0,3),(1,2),(1,3),(2,3). F_W ma 6 składowych (pary i<j). Sektor: C¹(K₄) = Im(d) ⊕ ker δ, wymiary 3+3.

**Para K₄ złączona wspólną ścianą** (obiekt testu; definicja z rejestru): **bipiramida trójkątna (K₅ bez jednej krawędzi)**. Wierzchołki {0,1,2,3,4}: szczyty 0 (strona A) i 4 (strona B), wspólna ściana {1,2,3}. Krawędzie (9, kanoniczny porządek): (0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(4,1),(4,2),(4,3). **Krawędzi (0,4) NIE MA**: para szczytowa (0,4) w F_W jest odległością czysto emergentną. F_W pary ma 10 składowych. Sektor: C¹(pary) = Im(d) ⊕ ker δ = 4+5.

**Orbity krawędzi:** orbita A = {(0,1),(0,2),(0,3)}; orbita B = {(4,1),(4,2),(4,3)}; orbita F (wspólna ściana) = {(1,2),(1,3),(2,3)}. Para szczytowa (0,4) w wodzisku: punkt stały.

**Symetria S₃ i dekompozycja sektorowa:** grupa S₃ = permutacje wierzchołków wspólnej ściany {1,2,3} (działa na orbitach A, B, F jednocześnie). Każda orbita 3-elementowa rozkłada się na kierunek symetryczny (1,1,1)/√3 (sektor A₁) i uzupełnienie ortogonalne 2-wymiarowe (sektor E; wybór bazy dowolny, jawny). **Dziedzina ℝ⁹ = 3A₁ ⊕ 3E**, **wodzisko ℝ¹⁰ = 4A₁ ⊕ 3E** (odrębny blok 1-wymiarowy pary (0,4)). Przy stanie S₃-symetrycznym operator J = dF_W|_D jest S₃-ekwiwariantny; wartości singularne niosą etykietę sektorową po blokach (A₁/E) — krotności raportować z etykietą (errata Z2 z 11cg).

**Rodzina S₃-symetryczna (przedmiot sesji TAU-14):** stany D stałe na orbitach: trzy skalary (D_A, D_B, D_F), znaki DOWOLNE (w tym mieszane per orbita); wagi per orbita w_A = e^{−|D_A|}, w_B = e^{−|D_B|}, w_F = e^{−|D_F|}; parametr czasu t > 0. Pełna przestrzeń parametrów rodziny: (D_A, D_B, D_F, t) — 4 parametry rzeczywiste.

**Punkt referencyjny:** D = 𝟙 (wszystkie 9 wartości krawędzi = 1; wówczas w_A = w_B = w_F = e^{−1}; crossingi wg checkpointów sekcji 4). **Stan Asteriona:** (D_A, D_B, D_F) = (0.2, 0.8, 1.0) per orbita A, B, F.

## 3. Zadania

**A. Bramka konwencji (K₄, jawna).** Oblicz J = dF_W|_{D=𝟙} przy t=1 dwiema drogami niezależnie: (a) różnice centralne, (b) pochodna Frécheta funkcji macierzowej expm metodą bloku 2n×2n (Al-Mohy & Higham 2009). RAPORT: rząd J; pełna lista sv (6 cyfr znaczących); rangi sektorowe; maksymalna odchyłka względna między drogami. BRAMKA: zgodność z §21 (sekcja 5) do 10⁻⁶; niezgodność → STOP diagnostyczny.

**B. Bramka pary i crossingi referencyjne (checkpointy TAU-10 + T13-1 + Asterion, jawne).** (i) J pary przy D=𝟙, t ∈ {0.1, 1, 2}: rząd, sv (6 cyfr), κ = σ_min/σ_max, rangi sektorowe (4/5), wiersz (0,4) z rozbiciem na orbity A/B/F. BRAMKA: sekcja 4 pkt 2. (ii) Crossingi w 𝟙: na siatce t ∈ [0.05, 3+] (zakres wystarczająco szeroki, by uchwycić oba znane przejścia; krok ≤ 0.05 plus bisekcja) wyznacz przejścia porządku sv **z etykietą sektorową**. BRAMKA: dokładnie 2 przejścia, t* = 1.119700774 (wartość wspólna 0.262612668) i t* = 2.598084384 (0.048444471) — twierdzenie T13-1 (11ck). (iii) Stan Asteriona (0.2, 0.8, 1.0): siatka t ∈ [0.05, 3.2]. BRAMKA: 4 przejścia, t* = 0.225342905 (0.369246600), 0.764925574 (0.180748355), 2.287153953 (0.030868231), 3.123998612 (0.003353307).

**C. Invariancje parametrów rodziny (BLIND, główne).** W rodzinie S₃-symetrycznej wyznacz, od czego zależy widmo sv(J): (i) **znaki:** przy ustalonych wagach (|D_A|, |D_B|, |D_F|) porównaj pełne widmo sv dla wszystkich wzorów znaków per orbita (globalny flip, pojedyncze, mieszane) — co obserwujesz (identyczność/co do czego)? (ii) **skala czasu vs skala wag:** porównaj (w, t) z (c·w, t/c) dla c ∈ {0.5, 2} (i dowolnych innych) — co obserwujesz? (iii) Wniosek: **minimalny zestaw parametrów**, od którego zależy widmo sv w rodzinie; jeśli potrafisz — argument analityczny (dowód) lub kontrprzykład; forma symboliczna mile widziana. Raportuj liczby (odchyłki, 6 cyfr) i wniosek jawny.

**D. Mapa liczby crossingów (BLIND, główne; wątek DS P2).** Wyznacz **liczbę crossingów n jako funkcję kierunku w trójkącie projectivnym wag** (w_A, w_B, w_F) (kierunek = punkt simpleksu wag po normalizacji; skala promienia rodziny — jawnie, wykorzystaj konkluzje zadania C, jeśli je masz; bez nich pełna przestrzeń (D, t) z rozsądnym protokołem). Protokół: (a) siatka barycentryczna własna, **co najmniej 100 kierunków**, rozdzielczość jawna; (b) **kontrola stabilności**: powtórz n na co najmniej 6 wybranych kierunkach przy 2× gęstszej siatce czasu i przy skróconym/podwojonym zakresie skali (raport: czy n się zmienia); (c) **kontrola symetrii A↔B**: kierunki lustrzane powinny dawać identyczne n (odchyłka implementacyjna); (d) **próg słyszalności** z §0 pkt 7 zadeklarowany przed skanem. RAPORT: rozkład n (histogram), n_min, n_max, czy n jest stałe w rodzinie (jeśli tak — dlaczego; jeśli nie — opis pól: które regiony simpleksu mają które n); listy położeń crossingów dla 3 wybranych kierunków własnych (jawnie); kontrole (a)–(d).

**E. Podrodzina symetryczna (BLIND).** W rodzinie z w_A = w_B = w, w_F dowolne: parametr r = w_F/w; siatka r logarytmiczna ≥ 2 dekady wokół r = 1 (rozmiar jawny). Wyznacz n(r) i położenia crossingów; **szczegółowo opisz otoczenie r = 1** (w tym 𝟙): pełna lista par krzywych (z etykietą sektorową), które crossują w pobliżu, oraz tych, które nie; zachowanie widma przy małych skalach czasu. Czy n(r) jest stałe? Czy w otoczeniu r = 1 zachodzi coś szczególnego? Opis jawny, bez nadawania statusów.

**F. Opcjonalne, badawcze (BLIND): granice pól.** Wybierz odcinek między 𝟙 a kierunkiem o n ≠ n(𝟙) (z zadania D): wyznacz, gdzie wzdłuż odcinka liczba crossingów się zmienia i opisz charakter zmiany (przesunięcie przejść poza zakres vs spotkanie/rozjazd krzywych). Zbadaj dokładność lokalizacji takiego miejsca.

## 4. Checkpointy (jedyne wartości oczekiwane)

1. **§21 (K₄, korpus P0-Estrada v0.7):** K₄, D=𝟙, t=1, baza ortonormalna: sv J = (.6756526, .3378263, .3378263, .3378263, .1689132, .1689132); rząd 6; rangi sektorowe 3/3; rząd 6 również przy t ∈ {0.1, 2}. Uwaga Z2: macierz J §21 element-po-elemencie nie jest replikowalna; tylko niezmienniki bazy są przedmiotem bramki.
2. **TAU-10 (para; trzy zgodne strony):** sv J pary przy D=𝟙, t=1: (.6635067, .4318725, .2923045, .2923045, .2852585, .172749, .172749, .1169218, .1169218); rząd 9/9 przy t ∈ {0.1, 1, 2}; rangi sektorowe 4/5; κ = 0.206931 / 0.176218 / 0.119999; wiersz (0,4) przy t=1: orbita A = orbita B = 0.122012 (na krawędź), orbita F ≈ 0 (rzędu 10⁻¹⁹).
3. **T13-1 (𝟙; twierdzenie z 11ck):** dokładnie 2 crossingi, t*₁ = 1.119700774 (wartość wspólna 0.262612668), t*₂ = 2.598084384 (0.048444471), oba A₁×E.
4. **Stan Asteriona (0.2, 0.8, 1.0) per orbita (11ci/11ck):** 4 przejścia, t* = 0.225342905 (0.369246600), 0.764925574 (0.180748355), 2.287153953 (0.030868231), 3.123998612 (0.003353307).

## 5. Format raportu

Wg wzorca rejestru: (1) receipt zlecenia; (2) wyniki per zadanie z atrybucją każdej liczby (droga, ε, biblioteka + wersja, seed, liczba cyfr znaczących, rozmiary siatek, progi); (3) zastrzeżenia i STOP-y jawne; (4) wnioski opisowe bez nadawania statusów; propozycje numerowane P…, zarzuty A… jak zwykle.

## 6. Warianty wykonania (per wykonawca)

- **Asterion (GPT):** pełna numerika A–E; F wg wyboru; obie drogi obowiązkowe w A, w B–E wystarczy jedna (jeśli druga potwierdzona w A).
- **DeepSeek:** pełna numerika A–E po uzyskaniu środowiska; dopuszczalne częściowo symbolicznie (zadanie C szczególnie mile widziane symbolicznie); dopuszczalna ścieżka PROXY wg wzorca §36 (v2): kompletny skrypt z jawnej specyfikacji (seed jawnie), Leszek wykonuje mechanicznie bez edycji, surowy stdout verbatim, raport z linią atrybucji „kod i analiza: DeepSeek; wykonanie proxy: Leszek".
- **Claude:** po przerwie; bez terminu; jego trzecia kontrola mile widziana.
- Bez pośpiechu, bez terminu.