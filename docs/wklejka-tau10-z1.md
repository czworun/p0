# Wklejka TAU-10-Z1: replikacja świeżego wyniku 🔍 — pełny Jacobian F_W pary K₄ (pytanie (f) z recenzji tury 8)

**Do:** Claude / Asterion (GPT) / DeepSeek — za pośrednictwem Leszka. **Od:** warsztat P₀, szef lab. Vibe. **Data:** 2026-11-16 (runda 11cd).

## 0. Kontekst administracyjny

1. **Zlecenie:** niezależna replikacja (Z1) świeżego wyniku warsztatu (status 🔍, runda 11cc). Pytanie badawcze pochodzi z recenzji tury 8, wątek (f), autorstwa DeepSeeka: *„czy rank 6 Jacobianów (Estrada §23) przenosi się na pełny Jacobian F_W par K₄ — testowalne jednym uruchomieniem"*. Warsztat wykonał rachunek od zera i zarejestrował wynik; **wartości są BLIND**: wklejka ich nie zawiera. Raportuj własne liczby; porównanie nastąpi po złożeniu raportów.
2. **Zasady rejestru (Z0–Z3):** droga ważniejsza niż cel; replikacja niezależna (implementacja od zera, wyłącznie z niniejszej specyfikacji); jawna konwencja; specyfikacja, nie kod. Statusy ✅/🔍 nadaje warsztat po rozliczeniu, nie wykonawca.
3. **BLIND-HIGIENA:** jedyne wartości oczekiwane w tej wklejce to checkpoint konwencji §21 (K₄; pochodzi z dokumentu korpusu P0-Estrada v0.7, wcześniej niezależnie zweryfikowany przez Claude'a). ŻADNYCH wartości dla pary K₄ nie podajemy: ani rzędów, ani wartości singularnych, ani κ, ani struktury wierszy.
4. **STOP-rule:** każda niejednoznaczność specyfikacji → zgłoś STOP z opisem zamiast domyślać się konwencji (wzorzec E7). Uwaga: znakowana rep permutacyjna S₄ nie gra tu roli; cała praca odbywa się w zwykłej, bezznakowanej przestrzeni wartości krawędzi.

## 1. Definicje (verbatim wg P0-Estrada v0.7, §18 — odczyt edge-native)

Ważony Laplasjan budowany wprost z wartości krawędzi D (nie przez potencjał wierzchołkowy):

- L(D)_{ij} = −w(D_{ij}) dla i ≠ j;  L(D)_{ii} = Σ_{j≠i} w(D_{ij});
- w_e = f(|D_e|),  f(r) = e^{−r}  (odczyt e^{−|D|}: najbardziej stabilny z testowanych, NIE kanoniczny);
- K_t = e^{−t·L(D)};  F_{W,t}(D)_{ij} = K_{ii} + K_{jj} − 2·K_{ij}.

Gładkość: przy |D_e| = 0 odczyt ma kink; próbkowane stany muszą mieć min |D_e| > 10⁻³.

## 2. Obiekty

**K₄** (kontrola konwencji): wierzchołki {0,1,2,3}; krawędzie w porządku kanonicznym: (0,1),(0,2),(0,3),(1,2),(1,3),(2,3). F_W ma 6 składowych (pary i<j). Sektor: C¹(K₄) = Im(d) ⊕ ker δ, wymiary 3+3, gdzie d: (dx)_{ij} = x_i − x_j (gradient potencjałów wierzchołkowych), a ker δ = Im(d)^⊥ (dywergencja zero = przestrzeń cykli grafu; wymiar E−V+1 = 3).

**Para K₄ złączona wspólną ścianą** (obiekt testu; definicja z rejestru P₀-Lattice, sekcja „para K₄ złączona ścianą"): graf = **bipiramida trójkątna (K₅ bez jednej krawędzi)**. Wierzchołki {0,1,2,3,4}: szczyty 0 (strona A) i 4 (strona B), wspólna ściana {1,2,3}. Krawędzie (9, w porządku kanonicznym): (0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(4,1),(4,2),(4,3). **Krawędzi (0,4) NIE MA**: para szczytowa (0,4) w F_W jest odległością czysto emergentną. F_W pary ma 10 składowych (wszystkie pary i<j, w tym (0,4)). Sektor: C¹(pary) = Im(d) ⊕ ker δ = 4+5 (ker δ: wymiar E−V+1 = 5).

**Punkt referencyjny:** D = 𝟏 (wszystkie krawędzie = 1); t ∈ {0.1, 1, 2}.

## 3. Zadania

**A. Bramka konwencji (K₄, jawna).** Oblicz J = dF_W|_{D=𝟏} przy t=1 dwiema drogami niezależnie: (a) różnice centralne, (b) pochodna Frécheta funkcji macierzowej expm metodą bloku 2n×2n (Al-Mohy & Higham, SIAM J. Matrix Anal. Appl. 30(4), 2009). RAPORT: rząd J; pełna lista wartości singularnych (6 cyfr znaczących); rangi sektorowe; maksymalna odchyłka względna między drogami. BRAMKA: zgodność wartości singularnych z §21 (sekcja 4 niżej) do 10⁻⁶; w razie niezgodności → STOP diagnostyczny z opisem (konwencje §18 odczytane inaczej).

**B. Test główny (para, BLIND).** Oblicz J = dF_W|_{D=𝟏} pary: macierz 10×9 (wiersze: 10 par wierzchołków i<j; kolumny: 9 krawędzi). t ∈ {0.1, 1, 2}. RAPORT dla każdego t: rząd; pełna lista wartości singularnych (6 cyfr); κ = σ_min/σ_max; rangi sektorowe (projekcja J na Im(d), wym. 4, i na ker δ, wym. 5; bazy własne ortonormalne — rangi sektorowe są niezależne od wyboru bazy); zgodność obu dróg (jeśli użyto dwóch).

**C. Eksploracja (BLIND).** Własny świeży protokół, opisany jawnie (seed, rozkład, liczebność): co najmniej 240 losowych stanów D (sugerowane: składowe U(−2,2) i.i.d., odrzut stanów z min |D_e| < 10⁻³) × t ∈ {0.1, 1, 2}. RAPORT: liczba Jacobianów pełnego rzędu (w formacie x/720 lub analogicznym wg własnej liczebności); σ_min (minimum, mediana); κ (maksimum, mediana); czy któraś realizacja jest blisko utraty rzędu?

**H1. Badawcze (BLIND): wiersz pary szczytowej.** W J pary przy D=𝟏 (dowolne z trzech t) opisz wiersz odpowiadający parze (0,4): wpisy (6 cyfr) oraz średnie |wpisu| wg orbit krawędzi — orbita A: (0,1),(0,2),(0,3); orbita B: (4,1),(4,2),(4,3); orbita F (krawędzie wspólnej ściany): (1,2),(1,3),(2,3). Czy dostrzegasz coś strukturalnego? (opis; twierdzeń nie formułować).

**H2. Badawcze, opcjonalne (oferta własna DeepSeeka, bez terminu):** rodzina znormalizowana (a, b, −b, −a) zamiast (1, r, −r, −1): czy warunek krytyczny r⁴ − 10r² + 1 = 0 (wątek H-C5, domknięty w rodzinie (1,r,−r,−1)) jest uniwersalny dla całej rodziny, czy specyficzny dla (1,r,−r,−1)? Rachunek symboliczny, bez numeryki.

## 4. Checkpointy (jedyne wartości oczekiwane w tej wklejce)

- §21 P0-Estrada v0.7 (K₄, D=𝟏, t=1, baza ortonormalna): wartości singularne J = (.6756526, .3378263, .3378263, .3378263, .1689132, .1689132); rząd 6; rangi sektorowe 3/3; rząd 6 również przy t ∈ {0.1, 2}.
- Uwaga Z2 z dokumentu: macierz J §21 element-po-elemencie nie jest replikowalna (brak surowych wektorów bazowych g₂, g₃, z₁–z₃); rząd i wartości singularne są niezmiennikami bazy — tylko one są przedmiotem bramki.

## 5. Format raportu

Wg wzorca rejestru: (1) receipt zlecenia; (2) wyniki per zadanie z atrybucją każdej liczby (droga, ε, biblioteka + wersja, seed, liczba cyfr znaczących); (3) zastrzeżenia i STOP-y jawne; (4) wnioski opisowe bez nadawania statusów; propozycje numerowane P…, zarzuty A… jak zwykle.

## 6. Warianty wykonania (per wykonawca)

- **Claude, Asterion (GPT):** pełna numerika A–C + H1; obie drogi obowiązkowe w A, w B–C wystarczy jedna (jeśli druga potwierdzona w A).
- **DeepSeek:** pełna numerika A–C + H1 po uzyskaniu środowiska; dopuszczalne częściowo symbolicznie; dopuszczalna ścieżka PROXY wg wzorca §36 (v2): DeepSeek pisze kompletny skrypt z jawnych specyfikacji (seed jawnie), Leszek wykonuje mechanicznie bez edycji i zwraca surowy stdout verbatim, DeepSeek analizuje i składa raport z linią atrybucji „kod i analiza: DeepSeek; wykonanie proxy: Leszek". H2 opcjonalne, jego autorstwo.
- Bez pośpiechu, bez terminu.