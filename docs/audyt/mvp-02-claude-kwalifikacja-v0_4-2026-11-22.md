# MVP-02 v0.4: runda kwalifikacyjna Claude'a (druga replikacja drugim narzędziem)

> Zakres: zadania 1 (fingerprinty Węzła-0, zespolonosc subdominanty), 2 (rho_gate G0 do G4), 3 (drugi głos formy zamkniętej Aneksu, sekcja 6). Data: 2026-11-22. Gałąź docelowa: audit/claude-mvp02-v04-qual-2026-11-22; nie scalać do main.
> K6: żadnego theta, tau, U_b ani kill; żadnego udział(t). K8: żadnych własnych progów metodycznych poza opisanymi niżej kryteriami weryfikacji. Liczby jawnym tekstem, potęgi a^b, sqr() w formułach, zero LaTeXu, zero kodu w dostawie.
> Pola 1, 2 i 3 rozdzielone; pole 3 zawiera wyłącznie tezę fizyczną.

## ZASTRZEŻENIE O MATERIALE (ważne dla interpretacji)

Plików v0.4 (docs/mvp-02-spec-v0_4.md, commit 858f9394; docs/mvp-02-spec-v0_4-aneks-a-uzupelnienie.md, commit 1ffdd3d4) NIE pobrałem: adresy w zleceniu dotarły rozbite na kilka linii i narzędzie pobierania nie przyjęło ich w tej postaci (ani w wersji zrekonstruowanej, ani przez wyszukiwanie). Konsekwencje: (a) nie audytowałem brzmienia tekstu v0.4 (w tym sekcji 6 uzupełnienia, §0.1 i adnotacji w §0.2); (b) rachunki zadań 1 i 2 oparłem na v0.3 (wzór M_local, tabela ścian, bramki G0 do G4) oraz na konwencji podanej w zleceniu. Zgodność wyników z celami zlecenia co do 12 i więcej cyfr jest niezależnym dowodem, że ta rekonstrukcja daje te same obiekty co konwencja v0.4 w zakresie tych wielkości; nie zastępuje lektury tekstu. Zadanie 3 wykonałem jako rachunek od zera (nie diff z tekstem sekcji 6): wielomiany i wartości dokładne podaję niżej, do porównania przez Vibe.

Konwencja użyta w rachunku: R_tetr(f) = M_P0 · M_c · M_b · M_a dla ściany f = [a,b,c], wektory kolumnowe, aktywacja a pierwsza (prawy czynnik pierwszy); M_i: wiersz i zastąpiony przez (1/4,1/4,1/4,1/4) na czterech punktach {a,b,c,P0}, reszta wierszy z identyczności; osadzenie w R^13 z P0 = indeks 12. R_węzeł = R_f19 · ... · R_f0 (f0 pierwsza). R_gate(G) = iloczyn ośmiu R_tetr po ścianach konfiguracji, ściana najmniejsza w porządku lex pierwsza (prawy czynnik).

## POLE 1: wyniki replikacji

**1.1 Narzędzia i niezależność.** FLINT (python-flint 0.9.0): macierze wymierne dokładne (R ma mianowniki będące potęgami 4), wielomian charakterystyczny całkowity, dokładna ranga. mpmath 1.3.0 na 80 cyfr: diagonalizacja macierzy niesymetrycznej metodą Hessenberga z iteracją QR (NIE Durand-Kerner, zgodnie z zakazem warsztatowym). sympy użyty wyłącznie do dokładnego zliczania pierwiastków rzeczywistych (ciąg Sturma). Wykonawca ten sam (model) co w rundach v0.1 do v0.3; niezależna jest ścieżka i narzędzie, nie osoba.

**1.2 Bramka sanity lokalna (§0.1).** Lokalny R_tetr 4×4 (kolejność a, b, c, P0; a pierwsza): widmo {1; 0.153348 ± 0.0740391·i; 0.134711}, lewy wektor stacjonarny (1,2,3,4)/10. Zgodne z zamrożonym widmem R_4 i wektorem S10.

**1.3 Fingerprinty Węzła-0 (zadanie 1).**
- tr(R) = 1.119630707769134 (cel 1.119630707769: zgodne).
- |lambda_1| = 1 (dominanta, prosta).
- |lambda_2| = 0.06615917187705 (cel 0.0661591718770: zgodne co do 13 cyfr).
- lambda_2,3 = 0.0570415170054 ± 0.0335156882844·i (cel 0.0570415170 ± 0.0335156883·i: zgodne), kąt ±30.437071 stopnia (cel 30.4370710: zgodne). Następny moduł w widmie: 0.0132835.

**1.4 ZESPOLONOŚĆ subdominanty: POTWIERDZONA czterema metodami niezależnymi od Durand-Kernera.**
1. Dokładny ciąg Sturma na wielomianie charakterystycznym (całkowitym, po skalowaniu przez 4^80): 9 pierwiastków rzeczywistych z 13, więc 4 nierzeczywiste (dwie pary sprzężone).
2. Zliczenie okrężne (zasada argumentu, 40000 punktów na okręgu, maksymalny krok fazy 1.51 radianów, czyli poniżej pi, brak niedopróbkowania): w kole |z| < 0.029645 leży 10 pierwiastków; w kole |z| < 0.257214 leży 12; w kole |z| < 0.99999 leży 12 (poza nim tylko lambda_1 = 1). Pierścień 0.029645 < |z| < 0.257214 zawiera dokładnie 2 pierwiastki, a Sturm na tym pierścieniu daje 0 pierwiastków rzeczywistych (dokładnie), więc oba są nierzeczywiste, i nie ma żadnego pierwiastka rzeczywistego o module między 0.257 a 0.9999. Czyli para zespolona jest subdominantą, a nie ukryty pierwiastek rzeczywisty.
3. Rezidua wektora własnego (80 cyfr): ‖R·v − lambda·v‖ / ‖v‖ = 1.5·10^-61. Rzeczywista 2-wymiarowa podprzestrzeń niezmiennicza rozpięta przez Re v i Im v: blok 2×2 ma ślad 0.114083034011 (= 2·Re lambda), wyznacznik 0.00437703602346 (= |lambda|^2) i dyskryminant −0.00449321 < 0; rezyduum niezmienniczości 1.4·10^-61. Czyli nie istnieje rzeczywisty rozkład na dwie wartości własne rzeczywiste w tej podprzestrzeni.
4. Rozpiętość Kryłowa: dokładna ranga macierzy [x, Rx, ..., R^12 x] = 13 z 13 (wielomian minimalny równa się charakterystycznemu; macierz niederogatoryczna), więc para nie może być artefaktem wielokrotności.

**1.5 rho_gate (zadanie 2).** Wszystkie pięć wartości zgodne z celami co do wszystkich podanych cyfr (9 wiążących i 12 oczekujących):

| Konfiguracja | |lambda_2| (13 cyfr) | typ subdominanty | cel (12 cyfr) |
|---|---|---|---|
| G0 | 0.2274467649228 | rzeczywista, prosta | 0.2274467649228 |
| G1 | 0.1973203106030 | rzeczywista, prosta | 0.1973203106030 |
| G2 | 0.2586681479535 | PARA ZESPOLONA | 0.258668147953 |
| G3 | 0.2601601257282 | rzeczywista, prosta | 0.2601601257282 |
| G4 | 0.2189668817942 | rzeczywista, prosta | 0.2189668817942 |

- G2: lambda_2,3 = 0.2574671279198 ± 0.02489756627531·i, kąt ±5.52343772 stopnia (cel: 0.257467127920 ± 0.024897566275·i, 5.5234377: zgodne).
- Weryfikacja typologii tymi samymi czterema metodami dla każdej konfiguracji (okręgi o promieniach na średnich geometrycznych między sąsiednimi modułami; Sturm w pierścieniu; rezidua 1.8·10^-61 do 3.6·10^-61; ranga Kryłowa 13 z 13 dla wszystkich): G0, G1, G3, G4: pierścień zawiera dokładnie 1 pierwiastek i jest on rzeczywisty (0 nierzeczywistych), więc subdominanta rzeczywista i prosta. G2: pierścień (0.194744; 0.508594) zawiera 2 pierwiastki, 0 rzeczywistych, 2 nierzeczywiste; blok 2×2: ślad 0.51493425584, wyznacznik 0.0669092107657, dyskryminant −0.00247956 < 0. W żadnej konfiguracji nie ma pierwiastka rzeczywistego o module między |lambda_2| a 0.9999 (poza lambda_1 = 1).
- Rozstrzygnięcie typologii: 4 konfiguracje z subdominantą rzeczywistą i 1 (G2) z parą zespoloną: POTWIERDZONE.
- Następny (różny) moduł za subdominantą: G0 0.1821037; G1 0.1155943; G2 0.1466166; G3 0.1486407; G4 0.1453733; odstępy są duże (iloraz co najmniej 1.4), więc rozstrzygnięcie nie leży blisko żadnej granicy.

**1.6 Zadanie 3: drugi głos formy zamkniętej (rachunek od zera, dokładny, w Q(sqr(5))).**
- Tablica przecięć {3,2,1,1,1; 1,1,1,2,3} wyznaczona wprost z grafu dwunastościanu (tabela ścian §0.3): dla wszystkich 400 par (f,h) trójki (c_d, a_d, b_d) wynoszą (0,0,3), (1,0,2), (1,1,1), (1,1,1), (2,0,1), (3,0,0) dla d = 0 do 5; czyli graf jest dystansowo-regularny z a = (0,0,1,1,0,0). Liczności kul k_d = 1, 3, 6, 6, 3, 1 (suma 20).
- Rekurencja ciągu cosinusowego: u_0 = 1, u_1 = theta/3, c_i·u_(i−1) + a_i·u_i + b_i·u_(i+1) = theta·u_i. Wielomiany jawne (theta = wartość własna przylegania = 3 − lambda):
  - u_2 = theta^2/6 − 1/2
  - u_3 = theta^3/6 − theta^2/6 − 5·theta/6 + 1/2
  - u_4 = theta^4/6 − theta^3/3 − 5·theta^2/6 + 4·theta/3
  - u_5 = theta^5/6 − theta^4/3 − 7·theta^3/6 + 5·theta^2/3 + 5·theta/3 − 1
- Warunek domknięcia (i = 5): theta·u_5 − 3·u_4 = theta·(theta − 3)·(theta − 1)·(theta + 2)·(theta^2 − 5)/6. Zerowanie się dokładnie w sześciu wartościach theta = 3, sqr(5), 1, 0, −2, −sqr(5) (lambda = 0, 3−sqr(5), 2, 3, 5, 3+sqr(5)) jest niezależnym potwierdzeniem, że tablica przecięć i widmo L_dod pochodzą z tego samego grafu (bez wolnych parametrów).
- Krotności z wzoru m = 20 / suma po d z k_d·u_d^2: 1, 3, 5, 4, 4, 3 (suma 20); ortogonalność suma po sektorach z m_a·u_d(theta_a)/20 = delta_(d,0) dla d = 0 do 5 (dokładnie).
- Wartości u_d per sektor (d = 0 do 5): T1g (theta = sqr(5)): 1, sqr(5)/3, 1/3, −1/3, −sqr(5)/3, −1. H_u (theta = 1): 1, 1/3, −1/3, −1/3, 1/3, 1. G_g (theta = 0): 1, 0, −1/2, 1/2, 0, −1. G_u (theta = −2): 1, −2/3, 1/6, 1/6, −2/3, 1. T2g (theta = −sqr(5)): 1, −sqr(5)/3, 1/3, −1/3, sqr(5)/3, −1.
- Parzystości antypodalne epsilon = u_5(theta): T1g −1, H_u +1, G_g −1, G_u +1, T2g −1; zgodne ze zleceniem. Dodatkowo dokładnie u_d = epsilon·u_(5−d) dla wszystkich sektorów i d.
- Wagi dokładne g_a(d) = (m_a/19)·u_d(theta_a) (powierzchnia), d = 1 do 5, kolejność T1g, H_u, G_g, G_u, T2g: d1: sqr(5)/19, 5/57, 0, −8/57, −sqr(5)/19. d2: 1/19, −5/57, −2/19, 2/57, 1/19. d3: −1/19, −5/57, 2/19, 2/57, −1/19. d4: −sqr(5)/19, 5/57, 0, −8/57, sqr(5)/19. d5: −3/19, 5/19, −4/19, 4/19, −3/19. Sumy: −1/19 dla każdego d (wyciek powierzchni 1/361).
- Wagi wnętrza g_a,int(d) = (lambda_a/3)·(m_a/20)·u_d(theta_a): d1: −1/12 + sqr(5)/20, 1/18, 0, −2/9, −1/12 − sqr(5)/20 (suma −1/3, wyciek 1/9). d2: 1/20 − sqr(5)/60, −1/18, −1/10, 1/18, 1/20 + sqr(5)/60. d3 (znak względem d2 odwrócony w T1g, G_g, T2g, czyli w sektorach z epsilon = −1, bez zmiany w H_u i G_u): −1/20 + sqr(5)/60, −1/18, 1/10, 1/18, −1/20 − sqr(5)/60. d4: 1/12 − sqr(5)/20, 1/18, 0, −2/9, 1/12 + sqr(5)/20. d5: −3/20 + sqr(5)/20, 1/6, −1/5, 1/3, −3/20 − sqr(5)/20. Sumy: 0 dla d2 do d5. (Sprawdzone: wszystkie wartości zgodne z 50 wagami z uzupełnienia v0.3 w zaokrągleniu do 4 cyfr i z rachunkiem na 60 cyfr z rundy v0.3.)
- Stosunek kanałów: g_a,int / g_a = 19·lambda_a/60 = 0.2419, 0.6333, 0.9500, 1.5833, 1.6581 (T1g, H_u, G_g, G_u, T2g).

**1.7 Proweniencja dawnego fingerprintu (rho = 0.174758932129, tr = 1.2889685345212).** Przeszukałem wszystkie 48 kombinacji: 24 permutacje kolejności aktywacji wewnątrz tetry razy 2 kierunki montażu zewnętrznego. Dawny fingerprint (tr 1.2889685345212, rho 0.1747589321287) odtwarza DOKŁADNIE jedna kombinacja: kolejność wewnętrzna P0, c, b, a (P0 aktywowane pierwsze, czyli R_tetr = M_a · M_b · M_c · M_P0) przy TYM SAMYM montażu zewnętrznym R_f19 · ... · R_f0. Odwrócony montaż zewnętrzny (R_f0 · ... · R_f19) przy nowej kolejności wewnętrznej daje coś innego: tr 1.119264738318, subdominanta rzeczywista 0.0777029354, i nie odtwarza dawnego fingerprintu.

## POLE 2: znaleziska i erraty

**F1 (adnotacja §0.2).** Zlecenie mówi, że proweniencją dawnego fingerprintu jest „montaż odwrócony". Wynik 1.7 wskazuje na odwrócony porządek czynników WEWNĄTRZ tetry (aktywacja P0 pierwsza; w v0.2 wycofane określenie „apex-first"), a nie odwrócony montaż zewnętrzny. Zalecenie: poprawić adnotację na „odwrócony porządek czynników wewnątrz tetry (M_a · M_b · M_c · M_P0)". Zastrzeżenie: to jedyne dopasowanie wśród 48 kombinacji, ale nie widziałem kodu, który wytworzył stary fingerprint, więc inna równoważna konwencja nie jest wykluczona; do potwierdzenia przez autora.
**F2 (znaczenie parzystości).** Epsilon (T1g −1, H_u +1, G_g −1, G_u +1, T2g −1) to wartość własna permutacji antypodalnej na znacznikach ścian (u_5 = epsilon). Etykiety g i u w nazwach sektorów odnoszą się do reprezentacji ścianowej z twistem det(g), więc parzystość g/u jest przeciwna do znaku epsilon (epsilon = −1 odpowiada g, +1 odpowiada u). Spec powinien to powiedzieć jawnie, bo zapis „parzystość antypodalna" bez wskazania reprezentacji można odczytać odwrotnie.
**F3 (słownictwo typologii).** „4 realne + para G2" jest poprawne dla SUBDOMINANT. W G1, G3 i G4 występują pary zespolone na trzecim poziomie widma (np. G1: 0.10767 ± 0.04206·i, moduł 0.1155943; G3: moduł 0.1486407; G4: moduł 0.1453733). Zalecam sformułowanie „typ subdominanty", żeby nie sugerować, że pozostałe konfiguracje nie mają modów zespolonych.
**F4 (metoda referencyjna rho w §3).** v0.3 §3 nakazuje „wielomian charakterystyczny + Durand-Kerner", a zlecenie zakazuje Durand-Kernera stopnia 13. Zalecenie: zmienić metodę referencyjną na jedną z użytych tu (diagonalizacja Hessenberg-QR w wysokiej precyzji, plus kontrola dokładnym ciągiem Sturma i zliczeniem okrężnym), z jawnym wymogiem dokładnej arytmetyki wymiernej przy budowie R.
**F5 (kryterium zespolonosci).** Do bramki kwalifikacji warto dopisać kryterium, które tu zastosowałem: ciąg Sturma plus zasada argumentu dają dowód jakościowy (typ subdominanty) bez potrzeby żadnej liczby zmiennoprzecinkowej poza lokalizacją okręgów.
**F6 (poza zakresem).** Nie sprawdziłem tekstu v0.4 (sekcja 6, §0.1, §0.2, §0.3), więc ewentualne rozbieżności między tekstem a rachunkiem w tych miejscach nie są wykryte. Jeśli Leszek wklei treść sekcji 6 i §0.1/§0.2 jednym blokiem, wykonam diff.

## POLE 3: teza fizyczna (odrębnie; poziom pewności jawnie)

1. **Obserwacja o operatorze (algebra, pewność wysoka):** relaksacja Węzła-0 do stanu stacjonarnego ma subdominantę zespoloną: skurcz 0.0662 na rundę z obrotem fazy 30.44 stopnia na rundę, czyli zbliżanie się z oscylacją (zmiany znaku), nie monotoniczne. Wśród pięciu konfiguracji tylko G2 ma ten charakter (kąt 5.52 stopnia, skurcz 0.2587); w pozostałych czterech subdominanta jest rzeczywista i prosta (zbliżanie bez oscylacji w modzie wiodącym).
2. **Czego to nie dowodzi:** nie wiem, czy ta jakościowa różnica ma jakikolwiek odpowiednik fizyczny (np. pamięć fazowa), ani czy G2 jest wyróżniona poza własnością widmową; żadne rachunki tej rundy nie testowały hipotezy transportowej (K6). Są to własności zamrożonych operatorów, nie wyniki o nośniku. Interpretację należy odłożyć do etapu b, po zamrożeniu v1.0.

## Dostawa

Plik: docs/audyt/mvp-02-claude-kwalifikacja-v0_4-2026-11-22.md. Gałąź: audit/claude-mvp02-v04-qual-2026-11-22 (do utworzenia przez Leszka; konektor GitHub nie jest jeszcze połączony, więc nie wykonałem commita i nie deklaruję SHA commita). Skrypty rachunkowe nie są dostarczane (Z3); dostępne na życzenie.
