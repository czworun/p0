# MVP-02 v1.4: formalny rerun rachunku zerowego Claude'a (zlecenie A; wariant theta half; certyfikat drugiej pochodnej, absorpcja stref)

> Bind: docs/mvp-02-spec-v1_4.md (commit 3b885670cace22f79b8f399ef18e6e58c434b01d, blob 901dec3c4e03f6e5ce1d453a75ca5908f5ec3ce0, 95184 B, SHA-256 1240d31aaccd6f8be20f7750535924abd394f743d7cd43786a74ca4e54e13409) + docs/mvp-02-spec-v0_4-aneks-a-uzupelnienie.md (blob e68906bed162eb6f0aecec416c6bba9e1b655482, 16196 B, SHA-256 820231b0197a081bf498b2c4b36b95bbb381175f313724491f32d61ce5d10151). Data: 2026-11-24. Gałąź docelowa: audit/claude-mvp02-v14-rerun-2026-11-24; nie scalać do main.
> Konwencje: po polsku; liczby jawnym tekstem; potęgi a^b; sqr() dla pierwiastków; zero LaTeXu; zero kodu w dostawie (Z3). Pole 3 PUSTE. Pełne wartości (40 cyfr, w tym A, B, C, H_t) w tabeli: docs/audyt/mvp-02-claude-rerun-v1_4-tabela-2026-11-24.csv.

## (0) KOTWICE, POBÓR, METODA, ZASTRZEŻENIA

**Pobór i kotwice (jednostka: bajty UTF-8).** Oba pliki pobrane z main po linkach raw; SHA-256 i blob SHA-1 zgodne bajtowo ze zleceniem (wartości wyżej), rozmiary 95184 B i 16196 B zgodne. K1: tytuł 286 B, zaczyna się "# MVP-02: specyfikacja v1.4 (etap b programu transportowego;" (zgodne). K2: ostatnia niepusta linia 2245 B, kończy się "K6 łamane wyłącznie dla rachunku referencyjnego szefa lab).*" (zgodne). K3: blok zaczyna się "> **Status v1.4 (2026-11-24): DECYZJA WARSZTATU = erraty (ap) i (aq)" (zgodne); KOŃCÓWKA W PLIKU TO "wg par. 2.5.**", a zlecenie podaje "wg paragrafu 2.5.**" (rozwinięcie skrótu "par."; rozbieżność brzmieniowa bez znaczenia merytorycznego, SHA-256 całego pliku zgodny, więc nie STOP). K4: zaczyna się "> **ERRATA ZBIORCZA v1.4 (2026-11-24; punkty (ap) i (aq);" i kończy "przypis wyłącznie do przyszłych raportów.**" (zgodne). K5: stopka v1.4 zaczyna się "*Wersja v1.4, 2026-11-24. Autor: Vibe (szef laboratorium P0, delegacja Leszka)." i kończy "(16196 B, 820231b0197a081bf498b2c4b36b95bbb381175f313724491f32d61ce5d10151), par. 2.5.*"; bezpośrednio po niej stopka "*Wersja v1.3, 2026-11-23." (zgodne).
**Narzędzia (atrybucja).** Python 3.12; mpmath 1.3.0 (50 cyfr; margines błędu 10^-30 na zewnątrz dla decyzji, H_t użyte z dodatkiem 10^-40 na zewnątrz); mp.iv (45 cyfr) do PEŁNEGO audytu przedziałowego wszystkich decyzji certyfikacyjnych (patrz 2.2); numpy float64 do kontroli niezależnych (gęsty skan). Implementacja moja, z treści bindu; żadnego kodu warsztatu nie znam ani nie używam. Wagi WYŁĄCZNIE z formy zamkniętej Aneksu A sekcja 6.
**Budżet (jawny).** Rachunek rdzenia (30 przebiegów: 10 konfiguracji x 3 progi) 12.6 s; audyt przedziałowy mp.iv 81 s (342283 decyzje); kontrole gęstym skanem kilka minut; zero przerwań, zero częściówek. Warunek stopu: koniec skanu chronologicznego (pierwsze przekroczenie albo 8·T_sk = 57.51, 32000 kroków siatki) i kryterium szerokości 10^-4.
**ZASTRZEŻENIE: rachunek NIE jest ślepy co do wyniku.** Jestem tym samym wykonawcą, który w Z1 (v1.3) wykonał ścieżkę diagnostyczną "Q" (certyfikat drugiej pochodnej) i znał jej wyniki (zero stref, brackety identyczne z półprzedziałami finalnymi). Rerun v1.4 jest więc rachunkiem tej samej linii implementacyjnej z nowym tekstem (ap)/(aq), nie niezależnością osobową; niezależność względem warsztatu zachowana (kod własny). KOLEJNOŚĆ PRACY: najpierw napisałem silnik wg brzmienia v1.4 i wykonałem JEDEN pełny przebieg 30 przebiegów (rdzeń), dopiero potem spisałem pre-rejestrację poniżej; pre-rejestracja nie zmienia żadnej reguły względem wykonanego rachunku (reguły (ap) i (aq) są w bindzie jawne; pozostałe pre-rejestracje P3, P5, P6 przejęte bez zmian z Z1).

## (1) PRE-REJESTRACJA

- **Certyfikat (aq):** g = max(udział w końcach) + H_t·w^2/8 na każdym poziomie (w = szerokość przedziału), H_t = 2·A^2 + 2·B·C (A = suma |g_a|·omega_a, B = suma |g_a|, C = suma |g_a|·omega_a^2), globalne w t, liczone w pełnej precyzji; użyte H_t = wartość dokładna + 10^-40 (zaokrąglenie na zewnątrz); człon Lipschitza L_t·Δt/2 NIE występuje w rachunku.
- **Absorpcja (ap):** gdy pierwsza strefa nierozstrzygnięta przylega do węzła przekraczającego i wszystkie wcześniejsze przedziały są certyfikowane: lo = początek strefy, hi = pierwszy oceniony węzeł z udział >= theta; strefa nie jest certyfikowana jako wolna. RESOLVED wyłącznie przy łącznym spełnieniu: szerokość [lo, hi] < 10^-4, arytmetyka (al) (margines decyzji, brak przypadków |F − theta| <= 10^-30), certyfikat wszystkich chwil przed lo (brak stref izolowanych); w przeciwnym razie NIEROZSTRZYGALNY-PARCJALNY. Poziom finalny (a) jest zgodny z DOPISEM WARSZTATU (Z2): RESOLVED = PIERWSZE PRZEKROCZENIE CERTYFIKOWANE.
- **P1:** bisekcja (ak) i limit 5 poziomów pokrywają się (krok dt = T_sk/4000 = 0.00179718390049431; po 4 podziałach 1.1232·10^-4 >= 10^-4, po 5 podziałach 5.6162·10^-5 < 10^-4), brak wrażliwości.
- **P3:** prawy koniec półprzedziału finalnego z udział >= theta jest węzłem przekraczającym w sensie (a) (czytanie przeciwne unieważniałoby (a) dla każdego przekroczenia).
- **P5 (nie ma w bindzie):** "ponad tolerancję 2 cyfr znaczących": R1 = rozdzielność przedziałów bez zaokrągleń; R2 = rozróżnialność po half-up 2 cyfr znaczących. Raportuję obie.
- **P6 (nie ma w bindzie):** ranga Q3 = ceil(0.75·N) po rozstrzygniętych wartościach null; mediana null = średnia z rang floor(N/2) i floor(N/2) + 1.
- **Oczekiwana konsekwencja (znana z Z1, patrz zastrzeżenie):** strefa w sensie (ap) może powstać tylko tam, gdzie F zbliża się do theta na odległość mniejszą niż H_t·w^2/8 <= 6.2·10^-9 na węźle poprzedzającym przekroczenie, więc klauzula (ap) powinna pozostać uśpiona, a wszystkie konfiguracje RESOLVED.

## (2) POLE 1: RACHUNEK FORMALNY

### 1.1 Bramki wagowe (krok 1): wszystkie PASS
- Macierz dystansów z Aneksu (400 wpisów) zgodna z BFS z tabeli ścian par. 0.3 (parsowanej z bindu); pary uporządkowane 60/120/120/60/20 (suma 380); 10 par antypodalnych: (0,19), (1,15), (2,12), (3,11), (4,14), (5,18), (6,13), (7,16), (8,10), (9,17).
- Rekurencja u_d z tablicy przecięć zgodna z wielomianami jawnymi u_2 do u_5 (różnica 1.9·10^-62); parzystości epsilon (T1g −1, H_u +1, G_g −1, G_u +1, T2g −1; u_(5−d) = epsilon·u_d dokładnie); wagi powierzchni i wnętrza z formy zamkniętej.
- Wycieki: powierzchnia suma wag = −1/19 (kwadrat 1/361 = 0.00277008310249307) na wszystkich d; wnętrze d1 suma = −1/3 (kwadrat 1/9 = 0.111111111111111); wnętrze d2 do d5 suma < 10^-60 (zero). Rezonans omega5 − omega1 − omega2 = 0 na 60 cyfr.
- Częstości: omega1 = 0.874032048897642; omega2 = 1.4142135623731; omega3 = 1.73205080756888; omega4 = 2.23606797749979; omega5 = 2.28824561127074. T_sk = 2·pi/omega1 = 7.18873560197723; dt = T_sk/4000 = 0.00179718390049431; półprzedział finalny dt/32 = 5.61619968904471·10^-5.

### 1.2 A.3 (krok 2) i BRAMKA H_t
sup F = (suma |g_a|)^2; świadek na kątach 0 lub pi z sigma = sgn(g1·g2·g5) (sigma = −1 dla d1 do d4, +1 dla d5); kontrola F(sw) = sup w arytmetyce przedziałowej (mp.iv, 45 cyfr): przecięcie niepuste dla wszystkich 10 konfiguracji, szerokość F(sw) poniżej 2·10^-44. theta = sup/2 dokładnie (zgodne z DOKŁADNĄ TABELĄ (aj) do 60 cyfr).

BRAMKA H_t (errata (aq), warunki (i) do (iv)): (i) wagi wyłącznie z formy zamkniętej: spełnione; (ii) przypisanie częstości wg par. 0.4(ii) (sektory T1g, H_u, G_g, G_u, T2g do omega1 = sqr(3−sqr(5)), omega2 = sqr(2), omega3 = sqr(3), omega4 = sqr(5), omega5 = sqr(3+sqr(5))): spełnione; (iii) globalność: H_t policzone wprost jako 2·A^2 + 2·B·C, bez wartości zaokrąglonych w dół; (iv) kierunek zaokrąglenia: wartość użyta = dokładna + 10^-40; dodatkowo przebiegi z wartościami BEZPIECZNYMI 6 cyfr (zaokrąglonymi na zewnątrz, kolumna ostatnia tabeli) dają wyniki IDENTYCZNE we wszystkich 30 przebiegach. Zgodność z wartościami referencyjnymi (aq): różnice nie większe niż 4.9·10^-15 (granularność referencji 14 miejsc po przecinku), np. d1 i d4 powierzchnia 2.779925608641902 wobec 2.77992560864190; d5 wnętrze 15.68260375168060 (różnica 8.9·10^-17).

| konfiguracja | sup (dokładnie) | sup (12 cyfr) | theta = sup/2 (12 cyfr) | H_t (16 cyfr) | H_t użyte, zaokr. na zewnątrz (6 cyfr znaczących) |
|---|---|---|---|---|---|
| d1 powierzchnia | ((13+6·sqr(5))/57)^2 | 0.214781965063 | 0.107390982532 | 2.779925608641902 | 2.77993 |
| d2 powierzchnia | 1/9 | 0.111111111111 | 0.0555555555556 | 1.262766113372465 | 1.26277 |
| d3 powierzchnia | 1/9 | 0.111111111111 | 0.0555555555556 | 1.262766113372465 | 1.26277 |
| d4 powierzchnia | ((13+6·sqr(5))/57)^2 | 0.214781965063 | 0.107390982532 | 2.779925608641902 | 2.77993 |
| d5 powierzchnia | 1 | 1.0 | 0.5 | 12.1425445048903 | 12.1426 |
| d1 wnętrze | (sqr(5)/10+95/342)^2 | 0.251386492577 | 0.125693246289 | 4.463893184774149 | 4.46390 |
| d2 wnętrze | 196/2025 | 0.0967901234568 | 0.0483950617284 | 1.407720752872853 | 1.40773 |
| d3 wnętrze | 196/2025 | 0.0967901234568 | 0.0483950617284 | 1.407720752872853 | 1.40773 |
| d4 wnętrze | (sqr(5)/10+95/342)^2 | 0.251386492577 | 0.125693246289 | 4.463893184774149 | 4.46390 |
| d5 wnętrze | 1 | 1.0 | 0.5 | 15.6826037516806 | 15.6827 |

### 1.3 A.4 wg v1.4 (krok 3): przekroczenie theta = sup/2 per konfiguracja
Przedział lokalizacji [lo, hi] to ostatni półprzedział finalny z przekroczeniem (STREF PRZYLEGŁYCH BRAK, więc lo = lewy koniec półprzedziału, hi = pierwszy oceniony węzeł z udział >= theta). Wszystkie 10 konfiguracji: RESOLVED, szerokość 5.6162·10^-5 (< 10^-4), zero stref (przyległych i izolowanych), certyfikat wszystkich chwil przed lo. Klauzula (ap) UŚPIONA (nie była wywołana ani razu w 30 przebiegach). B4: udział(0) < theta w każdej konfiguracji przy theta half (najbliższy: d1 wnętrze, 1/9 = 0.1111 wobec theta = 0.1257), więc PRZECIEK nie występuje; brak LEWO-OCENZUROWANYCH i PRAWO-OCENZUROWANYCH przy theta half; brak NIEROZSTRZYGNIĘTY-ROUNDING (half-up lo = half-up hi dla wszystkich 10); TAU-MAŁE nie występuje. Okna: okno 1 = (0, T_sk], 3 = (2·T_sk, 4·T_sk], 4 = (4·T_sk, 8·T_sk].

| konfiguracja | przedział lokalizacji [lo, hi] (12 cyfr) | szerokość | strefy | okno | half-up 2 cyfr (lo / hi) | status |
|---|---|---|---|---|---|---|
| d1 powierzchnia | [2.43215143734 , 2.43220759933] | 5.6162e-5 | 0 | 1 | 2.4 / 2.4 | RESOLVED |
| d2 powierzchnia | [3.6645702971 , 3.6646264591] | 5.6162e-5 | 0 | 1 | 3.7 / 3.7 | RESOLVED |
| d3 powierzchnia | [27.0459328425 , 27.0459890045] | 5.6162e-5 | 0 | 3 | 27 / 27 | RESOLVED |
| d4 powierzchnia | [28.2692534588 , 28.2693096208] | 5.6162e-5 | 0 | 3 | 28 / 28 | RESOLVED |
| d5 powierzchnia | [30.8733729306 , 30.8734290926] | 5.6162e-5 | 0 | 4 | 31 / 31 | RESOLVED |
| d1 wnętrze | [1.11414169431 , 1.11419785631] | 5.6162e-5 | 0 | 1 | 1.1 / 1.1 | RESOLVED |
| d2 wnętrze | [3.72449514778 , 3.72455130978] | 5.6162e-5 | 0 | 1 | 3.7 / 3.7 | RESOLVED |
| d3 wnętrze | [26.9367539206 , 26.9368100826] | 5.6162e-5 | 0 | 3 | 27 / 27 | RESOLVED |
| d4 wnętrze | [28.428135748 , 28.42819191] | 5.6162e-5 | 0 | 3 | 28 / 28 | RESOLVED |
| d5 wnętrze | [30.8972417793 , 30.8972979413] | 5.6162e-5 | 0 | 4 | 31 / 31 | RESOLVED |

### 1.4 Klasyfikacja (krok 4), theta half

| dystans | U_b = [tau_s_lo/tau_i_hi , tau_s_hi/tau_i_lo] (12 cyfr) | uwaga |
|---|---|---|
| d1 | [2.18287212057 , 2.18303256377] | — |
| d2 | [0.983895774903 , 0.983925690245] | — |
| d3 | [1.00405106468 , 1.00405524304] | — |
| d4 | [0.994409125571 , 0.994413065682] | — |
| d5 | [0.999225660098 , 0.999229294095] | — |

Klasa K3 (tolerancja R1, przedziały bez zaokrągleń): **WYNIK TYPOWY**. Klasa K3 (tolerancja R2, rozróżnialność po half-up 2 cyfr): **WYNIK TYPOWY**. F_r i statystyki pomocnicze: N null = 360; uporządkowanie rosnące orbit: d2, d4, d3, d1; ranga 270 wypada w orbicie d3, Q3 = [1.00405106468 , 1.00405524304]; F_r = 0/20; M = 20; mediana null (rangi 180 i 181, orbity d4 i d3) = [0.999230095126 , 0.999234154363].

**H_b: WYNIK TYPOWY (R1 i R2 zgodne; kill K3 rozstrzygnięty klasą wspólną na całości przedziałów).** Powód strukturalny, niewrażliwy na szerokości przedziałów: U_b(d1) = 2.18 leży wielokrotnie powyżej U_b(d5) = 0.9992 (więc (i) WSPARTE niemożliwe), a U_b(d2) = 0.9839 jest poniżej U_b(d5) (więc (ii) NIESPRAWIEDLIWIONE niemożliwe). M = 20, F_r = 0/20 (diagnostyczne, binarne); mediana null leży o 8.0·10^-7 powyżej górnego końca U_b(d5) (statystyka pomocnicza, nie kryterium). Monotoniczność U_b po dystansie: niemonotoniczna (2.183, 0.984, 1.004, 0.994, 0.9992). Degeneracja orbitowa: jedna wartość U_b na orbitę (wagi orbitowe zgodne z bramką).

### 1.5 Wrażliwość konwencji (krok 5; NIEWIĄŻĄCA, deskryptywna; zero wpływu na kill)
Przedziały lokalizacji przy theta = (1/3)·sup i theta = (2/3)·sup (wszystkie RESOLVED poza zaznaczonymi):

| konfiguracja | theta = (1/3)·sup: [lo, hi] | theta = (2/3)·sup: [lo, hi] |
|---|---|---|
| d1 powierzchnia | [1.06634783496 , 1.06640399696] okno 1 | [2.56519920797 , 2.56525536997] okno 1 |
| d2 powierzchnia | [3.52674875673 , 3.52680491873] okno 1 | [3.83367406974 , 3.83373023174] okno 1 |
| d3 powierzchnia | [10.6685329293 , 10.6685890913] okno 2 | [48.982247208 , 48.98230337] okno 4 |
| d4 powierzchnia | [28.1016098981 , 28.1016660601] okno 3 | [42.1645177575 , 42.1645739195] okno 4 |
| d5 powierzchnia | [6.78420073838 , 6.78425690037] okno 1 | PRAWO-OCENZUROWANE (brak przekroczenia do 8·T_sk = 57.51) |
| d1 wnętrze | tau = 0, PRZECIEK (udział(0) = 1/9 >= theta) | [2.510497423 , 2.510553585] okno 1 |
| d2 wnętrze | [2.26192442476 , 2.26198058676] okno 1 | [3.86282214612 , 3.86287830812] okno 1 |
| d3 wnętrze | [25.4208293005 , 25.4208854625] okno 3 | [48.9710148086 , 48.9710709706] okno 4 |
| d4 wnętrze | [26.8092661876 , 26.8093223496] okno 3 | [42.1449733825 , 42.1450295445] okno 4 |
| d5 wnętrze | [29.4260782707 , 29.4261344327] okno 4 | [45.0046299402 , 45.0046861022] okno 4 |

**theta = (1/3)·sup:**

| dystans | U_b = [tau_s_lo/tau_i_hi , tau_s_hi/tau_i_lo] (12 cyfr) | uwaga |
|---|---|---|
| d1 | [inf , inf] | B4a: tau_int = 0, U_b = nieskończoność |
| d2 | [1.55914192075 , 1.55920546245] | — |
| d3 | [0.419675897798 , 0.419679034275] | — |
| d4 | [1.04820291731 , 1.04820720804] | — |
| d5 | [0.230550185036 , 0.230552533639] | — |

Klasa K3 (tolerancja R1, przedziały bez zaokrągleń): **NIESPRAWIEDLIWIONE**. Klasa K3 (tolerancja R2, rozróżnialność po half-up 2 cyfr): **NIESPRAWIEDLIWIONE**. F_r i statystyki pomocnicze: N null = 360; uporządkowanie rosnące orbit: d3, d4, d2, d1; ranga 270 wypada w orbicie d2, Q3 = [1.55914192075 , 1.55920546245]; F_r = 0/20; M = 20; mediana null (rangi 180 i 181, orbity d4 i d2) = [1.30367241903 , 1.30370633524].

**theta = (2/3)·sup:**

| dystans | U_b = [tau_s_lo/tau_i_hi , tau_s_hi/tau_i_lo] (12 cyfr) | uwaga |
|---|---|---|
| d1 | [1.02176636392 , 1.02181159258] | — |
| d2 | [0.992439772612 , 0.992468740913] | — |
| d3 | [1.00022822122 , 1.00023051516] | — |
| d4 | [1.00046240833 , 1.00046507413] | — |
| d5 | nierozstrzygnięte (TEST lub null wyłączone) | — |

Klasa K3 (tolerancja R1, przedziały bez zaokrągleń): **NIEROZSTRZYGALNY (TEST nierozstrzygalny: M=0)**. Klasa K3 (tolerancja R2, rozróżnialność po half-up 2 cyfr): **NIEROZSTRZYGALNY (TEST nierozstrzygalny: M=0)**. F_r i statystyki pomocnicze: N null = 360; uporządkowanie rosnące orbit: d2, d3, d4, d1; ranga 270 wypada w orbicie d4, Q3 = [1.00046240833 , 1.00046507413]; F_r = nie dotyczy (TEST wykluczony); M = 0; mediana null (rangi 180 i 181, orbity d3 i d3) = [1.00022822122 , 1.00023051516].

Podsumowanie wrażliwości: theta = (1/3)·sup daje klasę NIESPRAWIEDLIWIONE (U_b(d5) = 0.2306 poniżej minimum null 0.4197; B4a na d1 wnętrze), theta = (2/3)·sup daje NIEROZSTRZYGALNY (TEST d5 powierzchnia PRAWO-OCENZUROWANE, M = 0). Kill K3 pozostaje WYŁĄCZNIE na theta half (pre-registracja K8).

## (3) POLE 2: KONTROLA I DIAGNOSTYKA

### 2.1 Test regresyjny i zgodność z Z1
Półprzedziały finalne dla theta half zgadzają się z 7 bracketami diagnostyki v1.1 co do 5 cyfr: d1 powierzchnia [2.43215, 2.43221], d1 wnętrze [1.11414, 1.11420], d2 powierzchnia [3.66457, 3.66463], d2 wnętrze [3.72450, 3.72455], d3 wnętrze [26.9368, 26.9368], d4 powierzchnia [28.2693, 28.2693], d5 powierzchnia [30.8734, 30.8734] (7/7). Półprzedziały finalne ze wszystkich 28 przebiegów z przekroczeniem są IDENTYCZNE (te same indeksy półkroków) z przebiegiem ścieżki Q z Z1 (silnik v1.3 z certyfikatem drugiej pochodnej): 28/28.

### 2.2 Kontrole niezależne i przedziałowe
1. **Audyt przedziałowy całości (al):** wszystkie 342283 decyzje certyfikacyjne z przebiegów (przedziały certyfikowane wolne od przekroczenia: górne oszacowanie z H_t górnym końcem przedziału < dolny koniec theta; półprzedziały przekraczające: F(hi) >= theta i F(lo) < theta na przedziałach rygorystycznych) POTWIERDZONE w mp.iv (45 cyfr) bez wyjątku (0 niepotwierdzonych).
2. **Gęsty skan float64** (krok 2·10^-6, od t = 0): w KAŻDYM z 28 przebiegów z przekroczeniem pierwsza chwila F >= theta leży wewnątrz przedziału lokalizacji (maksymalne odchylenie poza przedziałem 0), czyli [lo, hi] zawiera rzeczywiste pierwsze przekroczenie.
3. **Bound H_t:** gęsty skan sup|F''| na [0, 70] (krok 2·10^-4) daje wartości od 0.38 do 0.52 H_t (d1 powierzchnia 1.3657 wobec 2.7799; d5 wnętrze 7.0019 wobec 15.6826), czyli ograniczenie jest poprawne i zawyżone o czynnik 1.9 do 2.6.
4. **Odporność na zaokrąglenie H_t:** 30/30 przebiegów identycznych przy H_t sześciocyfrowych bezpiecznych (zaokrąglonych na zewnątrz).

### 2.3 Lekcje i sprostowania
1. **Sprostowanie do mojego raportu Z1 (zgodnie z adnotacją prezentacyjną (aq)):** sześciocyfrowe wartości H_t w moim raporcie Z1 były zapisane niepoprawnie (2.77990, 1.26280, 1.40770; poprawne wartości sześciocyfrowe do najbliższej to 2.77993, 1.26277, 1.40772) albo zaokrąglone do najbliższej zamiast na zewnątrz (12.1425 i 15.6826; wartości bezpieczne 12.1426 i 15.6827); bezpieczne wartości na zewnątrz dla wszystkich konfiguracji są w tabeli 1.2. NIE wpłynęło to na rachunek (kod używał pełnej precyzji); do certyfikacji służą wartości z tabeli 1.2.
2. Klauzula (ap) jest w v1.4 UŚPIONA przy tych wagach: certyfikat kwadratowy zamyka strefę przyległą, więc status RESOLVED wynika bezpośrednio z poziomu finalnego (a). To zachowanie, nie usterka.
3. Lekcja procesowa: ten rerun nie jest ślepy względem własnych wcześniejszych wyników (zastrzeżenie w (0)); ostateczną niezależność wnosi porównanie z silnikiem warsztatu.

### 2.4 ERRATA-WNIOSKI (oddzielnie; bez cichych poprawek)
**W-1 (kotwica K3).** Brzmienie końcówki w zleceniu ("wg paragrafu 2.5.**") różni się od pliku ("wg par. 2.5.**"); sugestia: kotwice brzmieniowe podawać dosłownie albo wyłącznie przez SHA-256.
**W-2 (dziury definicyjne wciąż otwarte z Z1: E-3, E-4, E-5).** Bind v1.4 nadal nie definiuje: (a) "ponad tolerancję 2 cyfr znaczących (Z2-EXT)" (użyłem R1 i R2, wynik odporny); (b) reguły rangi Q3 przy wykluczeniach null (użyłem ceil(0.75·N), P6; w tym rachunku N = 360 i nie ma wykluczeń przy theta half); (c) zdanie "ranga 270 wypada w orbicie d3, Q3 = U_b(d3) dokładnie" jest prawdziwe w moim rachunku przy theta half (uporządkowanie U_b(d2) < U_b(d4) < U_b(d3) < U_b(d1)), ale przy theta (1/3)·sup Q3 pochodzi z orbity d2 (a przy (2/3)·sup z d4); zdanie warto zawęzić do "w rachunku theta half".
**W-3 (uwaga o (ap)).** Skoro (ap) nie jest w ogóle wywoływana przy (aq), warto zaznaczyć w bindzie, że klauzula jest zabezpieczeniem na wypadek zmiany wag lub miary (zakres ważności lematu (aj) podobnie), żeby nie była mylnie czytana jako stosowana w tym rachunku.

### 2.5 Czego nie wykonałem
Opcjonalne bramki par. 3 poza krokiem 1 (R_4, L_cyc, rho_gate, R_węzeł, L_eq, L_dod, s_G/a_G); zlecenie dopuszcza pominięcie. Nie porównywałem wyników z rachunkiem warsztatu (to po stronie rejestru).

## (4) POLE 3: TEZA FIZYCZNA

PUSTE (interpretacja należy do właściciela).

## Dostawa
Pliki: docs/audyt/mvp-02-claude-rerun-v1_4-2026-11-24.md (raport) i docs/audyt/mvp-02-claude-rerun-v1_4-tabela-2026-11-24.csv (tabela 40 cyfr, w tym A, B, C, H_t i H_t użyte, T_sk, dt, przedziały lokalizacji, statusy, okna, half-up). Konektor GitHub nie jest u mnie połączony: nie wykonałem commita ani nie deklaruję SHA commita; pliki do dodania ręcznie na gałąź audytową audit/claude-mvp02-v14-rerun-2026-11-24 (nie scalać do main). Skrypty niedostarczane (Z3).
