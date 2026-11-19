# Wklejka TAU-15-Z1: replikacja analityki narodzin crossingów z t → 0 (macierz pierwszego rzędu) 🔍 — sesja TAU-15 (N1), twierdzenia kandydackie T15-1/T15-2, wątki z banku nasien (N3, „2(r−1)" z 11cn)

**Do:** Asterion (GPT) / DeepSeek — za pośrednictwem Leszka; Claude dołącza po przerwie (bez terminu). **Od:** warsztat P₀, szef lab. Vibe. **Data:** 2026-11-19 (runda 11cr).

## 0. Kontekst administracyjny

1. **Zlecenie:** niezależna replikacja (Z1) świeżych wyników 🔍 sesji TAU-15. Pytanie badawcze: **mechanizm narodzin crossingów para panelowych przy małych skalach czasu — struktura pierwszego rzędu Jacobianu w t → 0 i jego związek z geometrią pól liczby crossingów (kaustyką asymptotyczną z TAU-14).** Warsztat wykonał pełny rachunek od zera (sesja TAU-15) i zarejestrował wynik jako twierdzenia kandydackie T15-1/T15-2; **wartości sesji są BLIND**: wklejka ich nie zawiera poza checkpointami sekcji 4. Raportuj własne liczby; porównanie nastąpi po złożeniu raportów.
2. **Zasady rejestru (Z0–Z3):** droga ważniejsza niż cel; replikacja niezależna (implementacja od zera, wyłącznie z niniejszej specyfikacji); jawna konwencja; specyfikacja, nie kod. Statusy ✅/🔍 nadaje warsztat po rozliczeniu, nie wykonawca.
3. **BLIND-HIGIENA:** jedyne wartości oczekiwane w tej wklejce to checkpointy sekcji 4 (wszystkie jawne w rejestrze przed sesją TAU-15): §21 (korpus K₄), TAU-10 (para K₄; trzy zgodne strony), T13-1 (crossingi w D = 𝟙), stan Asteriona per orbita, punkty odcinka F Claude'a z 11cn (λ₀ = 0.632160217), nachylenia σ/t z 11cp, hipoteza positionalna „s* ≈ (r−1) i 2(r−1)" z 11cn, ukryty crossing e_A = e_C z 11ck. **ŻADNYCH wartości z sesji TAU-15 nie podajemy**: ani postaci granicy w t → 0, ani wyrażeń na sv paneli, ani punktów degeneracji μ, ani pozycji noworodków, ani stosunków pozycji, ani wyników dot. crossingów wewnątrzpanelowych.
4. **STOP-rule:** każda niejednoznaczność specyfikacji → zgłoś STOP z opisem zamiast domyślać się konwencji (wzorzec E7).
5. **Errata wklejek — rozróżnienie D vs w (lekcja 11ci, wbudowana):** w zadaniach podajemy **D = wartości krawędzi**; wagi zawsze wg §1: w = e^{−|D|}. Wyjście poza tę klasę — niedopuszczalne.
6. **Errata sign(D) (lekcja 11cj, wbudowana):** pochodna wagi: ∂w/∂D = −sign(D)·w (nie −w). Dotyczy każdej drogi analitycznej pochodnej (Frécheta; różnice centralne jej nie dotyczą).
7. **Higiena numeryczna map i małych skal (wymóg protokołu):** (a) każdy skan deklaruje jawny **próg słyszalności** (dolny cutoff sv względem szczytu widma w danym punkcie) ustalony PRZED skanem; detekcje sub-progowe nie wchodzą do liczby crossingów (Z2 pkt b); (b) wartości ekstremalne i odchyłki deklarować Z JAWNYM OKNEM i jednostkami (Z2 z 11cp); (c) **Z2-EXT (lekcja z 11cq-suplementu):** tolerancje, odchyłki i progi deklarować z jawną liczbą cyfr znaczących (minimum 2), nie jednocyfrowym zaokrągleniem; w rejonach, gdzie krzywe są niemal styczne, zawsze dołączyć charakterystykę geometryczną (nachylenie różnicy, krzywizna), nie samą odchyłkę pozycyjną.
8. **Jednostka czasu:** parametr czasu nazywamy tu **t** (spójnie z §1 i T13-1); w zapisach rejestru dotyczących noworodków (11cn/11cp) ta sama wielkość bywa zwana **s** — tożsamość s ≡ t.

## 1. Definicje (verbatim wg P0-Estrada v0.7, §18 — odczyt edge-native)

Ważony Laplasjan budowany wprost z wartości krawędzi D (nie przez potencjał wierzchołkowy):

- L(D)_{ij} = −w(D_{ij}) dla i ≠ j;  L(D)_{ii} = Σ_{j≠i} w(D_{ij});
- w_e = f(|D_e|),  f(r) = e^{−r};
- K_t = e^{−t·L(D)};  F_{W,t}(D)_{ij} = K_{ii} + K_{jj} − 2·K_{ij}.

Gładkość: przy |D_e| = 0 odczyt ma kink; próbkowane stany muszą mieć min |D_e| > 10⁻³.

## 2. Obiekty

**K₄** (kontrola konwencji): wierzchołki {0,1,2,3}; krawędzie w porządku kanonicznym: (0,1),(0,2),(0,3),(1,2),(1,3),(2,3). F_W ma 6 składowych (pary i<j). Sektor: C¹(K₄) = Im(d) ⊕ ker δ, wymiary 3+3.

**Para K₄ złączona wspólną ścianą** (obiekt testu): **bipiramida trójkątna (K₅ bez jednej krawędzi)**. Wierzchołki {0,1,2,3,4}: szczyty 0 (strona A) i 4 (strona B), wspólna ściana {1,2,3}. Krawędzie (9, kanoniczny porządek): (0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(4,1),(4,2),(4,3). **Krawędzi (0,4) NIE MA**: para szczytowa (0,4) w F_W jest odległością czysto emergentną. F_W pary ma 10 składowych. Sektor: C¹(pary) = Im(d) ⊕ ker δ = 4+5.

**Orbity krawędzi:** orbita A = {(0,1),(0,2),(0,3)}; orbita B = {(4,1),(4,2),(4,3)}; orbita F (wspólna ściana) = {(1,2),(1,3),(2,3)}. Para szczytowa (0,4) w wodzisku: punkt stały. Porządek indeksów krawędzi w macierzach: A, F, B ( czyli e = 1..9 wg listy powyżej: A=(01),(02),(03), F=(12),(13),(23), B=(41),(42),(43) — każdy raport deklaruje swój porządek jawnie).

**Symetria S₃ i dekompozycja sektorowa:** grupa S₃ = permutacje wierzchołków wspólnej ściany {1,2,3}. Każda orbita 3-elementowa rozkłada się na kierunek symetryczny (1,1,1)/√3 (sektor A₁) i uzupełnienie ortogonalne 2-wymiarowe (sektor E; wybór bazy dowolny, jawny; w pełnym sektorze E kopie struktury I₂ — wartości singularne pełnych bloków E mają krotność 2). **Dziedzina ℝ⁹ = 3A₁ ⊕ 3E**, **wodzisko ℝ¹⁰ = 4A₁ ⊕ 3E** (odrębny blok 1-wymiarowy pary (0,4)). Przy stanie S₃-symetrycznym operator J = dF_W|_D jest S₃-ekwiwariantny; panele sektorowe: J_A1 = P_A1ᵀ·J·E_A1 (4×3), J_E = P_V1ᵀ·J·E_V1 (3×3 w jednej kopii; w pełnym sektorze E wartości z krotnością 2); rangi i krotności raportować z etykietą (errata Z2 z 11cg).

**Rodzina S₃-symetryczna:** stany D stałe na orbitach: (D_A, D_B, D_F), znaki DOWOLNE; wagi per orbita w_A = e^{−|D_A|} itd.; czas t > 0. **Dziewięć parametrów → trzy skalary orbity + czas**; widmo sv(J) zależy w tej rodzinie tylko od (τ_A, τ_B, τ_F) = t·(w_A, w_B, w_F) (lemat T14-L z 11cl/11cn; do niezależnej potwierdzenia — patrz TAU-14-Z1, już wypchnięta; nie powtarzać tu).

**Podrodzina symetryczna (przedmiot główny):** w_A = w_B = ω, w_F = r·ω, r > 0; punkt r = 1 to 𝟙 (dokładnie: wszystkie wagi równe ω; stan referencyjny D = 𝟙 ma ω = e^{−1}).

**Punkt referencyjny:** D = 𝟙 (wszystkie 9 wartości krawędzi = 1). **Stan Asteriona:** (D_A, D_B, D_F) = (0.2, 0.8, 1.0) per orbita.

**Odcinek F (Claude, z 11cn):** w trójkącie wag: p(λ) = (1−λ)·(1/3, 1/3, 1/3) + λ·(1/2, 5/18, 2/9), λ ∈ [0, 1]; p(0) = środek, p(1) = wierzchołek (1/2, 5/18, 2/9). Skala wag przy λ: dowolna stała (lemat T14-L: tylko kierunek w simpleksie + skala τ mają znaczenie); deklaruj użyty współczynnik skali jawnie.

**Etykiety krzywych panelowych:** w panelu A₁ cztery sv malejąco: A#1..A#4 (etykiety rankingowe per punkt, nie tożsamościowe); w panelu E trzy sv malejąco: E#1..E#3 (w jednej kopii; pełny sektor E: krotność 2). **Uwaga metodologiczna (lekcja 11cp pkt 5):** etykiety rankingowe ≠ tożsamościowe; detektor rankingowy nie widzi zdarzeń wewnątrzpanelowych; jeśli zadanie dotyka tożsamości krzywych, zbuduj śledzenie etykiet tożsamościowych (np. ciągłość wektorów singularnych) i zadeklaruj je jawnie.

## 3. Zadania

**A. Bramka konwencji (K₄, jawna).** Oblicz J = dF_W|_{D=𝟙} przy t=1 dwiema drogami niezależnie: (a) różnice centralne, (b) pochodna Frécheta funkcji macierzowej expm metodą bloku 2n×2n (Al-Mohy & Higham 2009). RAPORT: rząd J; pełna lista sv (6 cyfr znaczących); rangi sektorowe; maksymalna odchyłka względna między drogami. BRAMKA: zgodność z §21 (sekcja 5) do 10⁻⁶; niezgodność → STOP diagnostyczny.

**B. Bramka pary i crossingi referencyjne (checkpointy TAU-10 + T13-1 + Asterion, jawne).** (i) J pary przy D=𝟙, t ∈ {0.1, 1, 2}: rząd, sv (6 cyfr), κ = σ_min/σ_max, rangi sektorowe (4/5), wiersz (0,4) z rozbiciem na orbity A/B/F. BRAMKA: sekcja 4 pkt 2. (ii) Crossingi w 𝟙: siatka t ∈ [0.05, 3+], krok ≤ 0.05 + bisekcja; przejścia porządku sv **z etykietą sektorową**. BRAMKA: dokładnie 2 przejścia, t* = 1.119700774 (0.262612668) i t* = 2.598084384 (0.048444471). (iii) Stan Asteriona (0.2, 0.8, 1.0): siatka t ∈ [0.05, 3.2]. BRAMKA: 4 przejścia, t* = 0.225342905 (0.369246600), 0.764925574 (0.180748355), 2.287153953 (0.030868231), 3.123998612 (0.003353307).

**C. Struktura pierwszego rzędu w t → 0 (BLIND, rdzeń zadania; kandydat T15-1).** Dla stanów rodziny S₃-symetrycznej zbadaj J(D, t) przy małych t (np. t ∈ {10⁻⁵, 10⁻⁴, 10⁻³, 10⁻²}). Pytania: (i) czy J(D,t)/t dąży do granicy macierzowej, gdy t → 0? Jeśli tak — wyznacz tę granicę (oznacz M) i podaj jej strukturę dla stanu stałego na orbitach: jawne wyrażenie na wpisy M (wiersze = pary p wodziska, kolumny = krawędzie e dziedziny) w zależności od wagi w_e, relacji p∩e i warunku [p = e] lub jego negacji; kolumny ze znakiem: dokładnie jakim? (ii) jaka jest dokładna postać rozwinięcia J(D,t) = t·M + reszta: wyznacz pierwszy człon poprawkowy (np. metodą Frécheta lub rozwinięciem expm do rzędu t²) i porównaj numerycznie: zbieżność J/t → M oraz (dalsze) zbieżność reszty (raport: schodkowe odchyłki względem co najmniej 3 dekad t); (iii) panele sektorowe granicy: M_A1 = P_A1ᵀ·M·E_A1 (4×3), M_E w jednej kopii E (3×3); wyznacz wartości singularne obu paneli w podrodzinie symetrycznej (w_A = w_B = ω, w_F = r·ω) JAKO FUNKCJE (r, ω): postać jawna, mile widziana symbolicznie (czynniki wielomianów charakterystycznych M_A1ᵀM_A1 i M_EᵀM_E dokładnie); (iv) pytanie kluczowe: czy którykolwiek singular value paneli granicy jest NIEZALEŻNY od r? Jeśli tak — który, o jakiej krotności, z jakimi wektorami singularnymi (jawna postać)? (v) kontrola numeryczna: porównanie sv(M_A1)/sv(M_E) z sv(J_A1)/sv(J_E) w granicy t → 0 na siatce r ∈ [0.5, 3] (skala ω dowolna, jawna).

**D. Degeneracje μ i mechanizm narodzin (BLIND, rdzeń zadania; kandydat T15-2).** Niech μ_i(r) = sv paneli granicy z C. (i) wyznacz z C( iii ) μ(r) dla podrodziny symetrycznej: znajdź wszystkie pary μ, które się zrównują (dokładne punkty r lub równania); w szczególności co się dzieje przy r = 1: które μ są wówczas zdegenerowane (para która), i jak degeneracja rozwija się dla r = 1 + ε? (ii) dla ε ∈ {10⁻³, 2·10⁻³, 5·10⁻³, 10⁻²}: wyznacz census crossingów para panelowych A#i×E#j (etykiety rankingowe w panelach, próg słyszalności z §0 pkt 7) na skali t ≤ 35 wraz z podejściem analitycznym pierwszego rzędu w ε (teoria perturbacji rozwinięcia z C: gdzie powinien pojawić się nowy crossing? na jakiej skali zależnej od ε?). Raport: pozycje t*(ε) + predykcja pierwszego rzędu + stosunek obu (z jawną liczbą cyfr, Z2-EXT); (iii) PRZETESTUJ hipotezę rejestru z 11cn: „noworodki przy r = 1 + ε pojawiają się przy t* ≈ (r−1) i 2(r−1)" (hipoteza positionalna Claude'a, robocza, status nierozstrzygnięty): czy census widzi zdarzenie przy ~2(r−1)? Czy czegokolwiek census rankingowy tam NIE widzi, a inne metody (etykiety tożsamościowe, zadanie F) widzą? Rozstrzygnij jawnie: co dokładnie kryje się pod „2(r−1)" (relacja pozycji, rodowód rodziny zdarzenia, etykiety).

**E. Odcinek F i predykcje nachyleń (BLIND, rdzeń zadania).** Dla odcinka p(λ) z §2, w otoczeniu punktu λ₀ = 0.632160217 (checkpoint jawny z 11cn): (i) wyznacz analogicznie jak w C/D strukturę μ(λ) sv paneli granicy wzdłuż odcinka; potwierdź/podważ, że przy λ₀ zachodzi degeneracja którejś pary μ; (ii) policz predykcje pierwszego rzędu (rozwinięcie z C): pozycje crossingów dla λ = λ₀ + δ przy δ ∈ {3·10⁻⁴, 10⁻³, 3·10⁻³} i porównaj z census; wyznacz predykowaną relację t*/δ (z jawną liczbą cyfr); (iii) BRAMKI (wartości jawne z 11cp): nachylenia σ/t przy t = 10⁻⁵ dla obu krzywych zdegenerowanej pary: **1.7440095 i 1.7440059** (pasmo rejestrowane: 1.7440095/1.7440060); relacja t*/(λ−λ₀): pasmo rejestrowane **0.903–0.905**; (iv) wyjaśnij analitycznie, skąd bierze się para niemal równych nachyleń przy λ₀ (to znaczy: para krzywych, których nachylenia σ/t są równe do ~4·10⁻⁶ względnie przy t = 10⁻⁵), i czy równość ta jest dokładna w jakimś sensie granicznym; jak nazywa się ten obiekt względem μ?

**F. Zdarzenia wewnątrzpanelowe i etykiety tożsamościowe (BLIND, badawcze; wstęp do N3).** (i) czy w 𝟙 lub w podrodzinie symetrycznej istnieją przejścia porządku sv **W OBRĘBIE panelu E** (E#i×E#j; pełny sektor: kopie struktury I₂ — uwaga na dokładne degeneracje kopii: jakie to ma konsekwencje dla śledzenia etykiet i dla gapów w pełnym bloku vs jednej kopii)? (ii) jeśli tak: pozycje, wartości wspólne, porównanie z ukrytym crossingiem e_A = e_C w 𝟙 (t = 2.20016, wartość wspólna 0.0707218; T13-1/11ck, jawne); czy to to samo zdarzenie w innych jednostkach/etykietach, czy inne? Zadeklaruj konwersję jednostek jawnie; (iii) rolę detektora rankingowego: wyjaśnij, dlaczego census rankingowy z definicji nie widzi tych zdarzeń, i podaj minimalny dodatek (etykiety tożsamościowe), który je widzi.

**G. Opcjonalne, badawcze (BLIND): czwarty crossing i granica pola.** W podrodzinie symetrycznej policz crossingi A#3×E#2 dla r ∈ {1.05, 1.1, 1.3, 1.5} (skala t ≤ 150, próg z §0 pkt 7): zbadaj, czy istnieje tangencja w płaszczyźnie (r, t) rodząca tę rodzinę, czy też inny mechanizm graniczny przy r → 1⁺; jeśli mechanizm graniczny — jaki (dyskusja jawna, z liczbami: położenie t*(r), wartości sv przy zdarzeniach)? Związek z klasyfikacją brzegu pól z 11cp (część styczna vs granica ucieczki przez t = ∞).

## 4. Checkpointy (jedyne wartości oczekiwane)

1. **§21 (K₄, korpus P0-Estrada v0.7):** K₄, D=𝟙, t=1, baza ortonormalna: sv J = (.6756526, .3378263, .3378263, .3378263, .1689132, .1689132); rząd 6; rangi sektorowe 3/3; rząd 6 również przy t ∈ {0.1, 2}.
2. **TAU-10 (para; trzy zgodne strony):** sv J pary przy D=𝟙, t=1: (.6635067, .4318725, .2923045, .2923045, .2852585, .172749, .172749, .1169218, .1169218); rząd 9/9 przy t ∈ {0.1, 1, 2}; rangi sektorowe 4/5; κ = 0.206931 / 0.176218 / 0.119999.
3. **T13-1 (𝟙; twierdzenie z 11ck):** dokładnie 2 crossingi, t*₁ = 1.119700774 (0.262612668), t*₂ = 2.598084384 (0.048444471), oba A₁×E (w etykietach rankingowych: A#3×E#1).
4. **Stan Asteriona (0.2, 0.8, 1.0) per orbita (11ci/11ck):** 4 przejścia, t* = 0.225342905 (0.369246600), 0.764925574 (0.180748355), 2.287153953 (0.030868231), 3.123998612 (0.003353307).
5. **Odcinek F (Claude, 11cn; punkty λ jawne):** strefa n=0→1 przy λ = 0.560–0.565 (crossing z dużej skali; pozycja rejestrowana przy λ = 0.565: t* ≈ 9.004–9.009, odchyłka stron 5.2·10⁻⁴ względnie — wartość NIE jest bramką, tylko tłem kontekstowym (bez bramki)); λ₀ = 0.632160217: narodziny z t = 0 przy przekroczeniu λ₀ (3→4); nachylenia σ/t przy t = 10⁻⁵ w λ₀: para 1.7440095 / 1.7440059–60 (Asterion 11cp); relacja t*/(λ−λ₀) ∈ 0.903–0.905 (census/fit 11cn/11cp).
6. **Hipoteza positionalna (11cn, Claude; do przetestowania w D):** „noworodki przy r = 1 + ε: t* ≈ (r−1) i 2(r−1)" — status nierozstrzygnięty; census rankingowy z 11cn NIE potwierdził drugiego zdarzenia przy ~2(r−1).
7. **Ukryty crossing e_A = e_C w 𝟙 (11ck; do porównania w F):** t = 2.20016, wartość wspólna 0.0707218.

## 5. Format raportu

Wg wzorca rejestru: (1) receipt zlecenia; (2) wyniki per zadanie z atrybucją każdej liczby (droga, ε, biblioteka + wersja, seed, liczba cyfr znaczących wg Z2-EXT, rozmiary siatek, progi słyszalności, okna); (3) zastrzeżenia i STOP-y jawne; (4) wnioski opisowe bez nadawania statusów; propozycje numerowane P…, zarzuty A… jak zwykle.

## 6. Warianty wykonania (per wykonawca)

- **Asterion (GPT):** pełne A + rdzeń C/D/E obowiązkowo (numerika + algebra; mile widziana droga symboliczna w C(iii)/C(iv)), F/G wg wyboru; obie drogi obowiązkowe w A, w B–E wystarczy jedna (jeśli druga potwierdzona w A).
- **DeepSeek:** A–E obowiązkowo po uzyskaniu środowiska; dopuszczalne częściowo symbolicznie (C mile widziane symbolicznie; F–G wg wyboru); dopuszczalna ścieżka PROXY wg wzorca §36 (v2): kompletny skrypt z jawnej specyfikacji (seed jawnie), Leszek wykonuje mechanicznie bez edycji, surowy stdout verbatim, raport z linią atrybucji „kod i analiza: DeepSeek; wykonanie proxy: Leszek". Odpowiedzi na zaległe pytania kontrolne z 11cn pkt 9 mogą wejść w ten raport.
- **Claude:** po przerwie; bez terminu; jego trzecia kontrola mile widziana; szczególnie mile widziane C symbolicznie (kontynuacja jego odcinka F: odcinek F jest w E).
- Bez pośpiechu, bez terminu.