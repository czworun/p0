Atak DeepSeeka na MVP-02 v0.4 — wznowienie W1 i atak na protokoły oraz kryteria

0. Receipt i deklaracja

Materiał pobrany: specyfikacja v0.4 (commit 858f9394, 427 linii) i uzupełnienie Aneksu A (commit 1ffdd3d4). Z0 jawne: mój kanał odczytu uzupełnienia Aneksu A pokazuje 24 z 92 linii (ucięcie na L24 w środku formuły „+ suma_{a"); nie mogę zweryfikować szczegółów protokołu A.3/A.4 na poziomie algorytmicznym. To ograniczenie mojego kanału, nie luka repo — ale blokuje pełne wznowienie W1. Atakuję to, co jest dostępne w specyfikacji (struktura wymagań, odesłania, spójność), oraz K1–K8 na pełnym §2.3. K6 zachowane: zero sup, tau, U_b, kill. Dopuszczalne replikacje algebraiczne — wykonane na papierze. Język: w całości polski. Liczby jawnym tekstem, sqr() w formułach, zero LaTeXu.

Deklaracja słojowa: atak na strukturę specyfikacji, bez roszczeń do statusów.

---

Pole 1 — Ustalenia

U1. W1 (wznowienie) — częściowo wykonane, częściowo Z0. Specyfikacja v0.4 zawiera erratę (d) „PROTOKOŁY A.3/A.4 wzmocnione: certyfikat maksimum globalnego (Lipschitz), certyfikacja pierwszego przekroczenia, kategorie cenzury LEWO-OCENZUROWANE i PRAWO-OCENZUROWANE z flagami, flaga TAU-MAŁE (E6)" (L34–L36) oraz adnotację E5 (L46–L47: „orbity d1 i d4: wymiar fazowy 3, bo udział nie zależy od theta3; siatka A.3 nadmiarowa ×120; PROTOKÓŁ BEZ ZMIAN"). Ale pełny algorytm A.3 (Lipschitz na komórkach, sięganie obszaru zagęszczania, granice podtorusa, jawny błąd przybliżenia sup) i A.4 (bisekcja na parze przeciwnych znaków przy wielu epizodach, cenzura, TAU-MAŁE, half-up) nie są w specyfikacji — są w Aneksie A, którego nie widzę w całości. Zatem: struktura wymagań PASS, weryfikacja algorytmiczna — Z0 po mojej stronie.

U2. A.3 — wymagania strukturalne PASS (na podstawie specyfikacji). §2.3 definiuje θ = (1/2)·sup_t udział_(f,h)(t) „DOKŁADNIE POŁOWA SUPREMUM, bez zaokrągleń plateau" (L358–L360), z sup „wyliczanym a priori z wielomianu trygonometrycznego PROTOKOŁEM FAZOWYM (Aneks A)" (L360–L361). Errata (h) wycofuje pojęcie „półki" (L42–L43). Adnotacja E5 przyznaje, że dla d1 i d4 udział nie zależy od theta3 (wymiar fazowy 3 zamiast 4), siatka A.3 jest nadmiarowa ×120, ale „PROTOKÓŁ BEZ ZMIAN". To jest spójne: nadmiarowość siatki nie zmienia wyniku (sup jest ten sam), więc nie ma swobody. Potwierdzam strukturalnie.

U3. A.4 — kategorie cenzury i flagi strukturalnie spójne (na podstawie specyfikacji). Specyfikacja definiuje (L361–L376): PRZECIEK dla τ = 0 z powodu udział(0) ≥ θ; B4a (τ_int = 0, τ_surf > 0) → U_b = ∞, klasa WNĘTRZE-NATYCHMIASTOWE; B4b (τ_surf = 0, τ_int > 0) → U_b = 0, klasa POWIERZCHNIA-NATYCHMIASTOWA; B4c (oba τ = 0) → PRZECIEK-MUTUALNY, wykluczony z agregatów i kill; errata (i) cz. 2 (W5+W11) rozciąga B4a/B4b/B4c oraz LEWO/PRAWO-OCENZUROWANE na TEST, z klasą NIEROZSTRZYGALNY-PARCJALNY, wykluczoną z kill i z mianownika F_r (L367–L372). To jest spójne i domyka moje W5/W11 z ataku na v0.3. Potwierdzam strukturalnie.

U4. Arytmetyka kombinatoryczna — POPRAWNA. 20·19 = 380; 10 par antypodalnych × 2 = 20 (TEST); 380 − 20 = 360 (NULL); d1: 30×2 = 60, d2: 60×2 = 120, d3: 60×2 = 120, d4: 30×2 = 60, suma 360. Kule dystansu 3, 6, 6, 3, 1; suma 19 = 20 − 1. Rangi stabilizatorów: 120/60 = 2 (d1), 120/120 = 1 (d2, d3), 120/60 = 2 (d4), 120/20 = 6 (d5). Wszystko domknięte.

U5. Q3 = ranga 270 — POPRAWNE. 270/360 = 75%; sortowanie rosnące, rangi 1–60 d1, 61–180 d2, 181–300 d3, 301–360 d4. Ranga 270 wypada w d3 (rangi 181–300). Zatem Q3 = U_b(d3) dokładnie (przy degeneracji orbit). Zgodne z L392–L393.

U6. Twierdzenie metryczne (racja bytu testu) — POPRAWNE. §2.1 (L295): „U_b rozróżnia WAŻENIE SEKTORÓW (czynnik 19·omega_a^2/60 per sektor, ASC: T1g 0.2419; H_u 0.6333; G_g 0.9500; G_u 1.5833; T2g 1.6581), nie nośnik (pole 3 Claude; teza nośnika otwarta)". Koncesja B1 jest wprost w treści §2.1 i §2.3. To jest właściwa forma: test mierzy metrykę, nie nośnik; interpretacja nośnika odroczona. Potwierdzam.

U7. Widma i rezonans — POPRAWNE (replikacja algebraiczna). L_eq na V_cyc: ślad = 3(3−sqr(5)) + 5·2 + 4·3 + 4·5 + 3(3+sqr(5)) = 9 − 3sqr(5) + 10 + 12 + 20 + 9 + 3sqr(5) = 60. Zgodne z L220. L_dod: {0; 3−sqr(5); 2; 3; 5; 3+sqr(5)}, krotności {1,3,5,4,4,3}, ślad 60 (0 + 60). Zgodne z L413 (poprzednia wersja) i formą zamkniętą w uzupełnieniu. Rezonans: omega1 + omega2 = sqr(3−sqr(5)) + sqr(2) = sqr(2)/phi + sqr(2) = sqr(2)(1/phi + 1) = sqr(2)·phi = sqr(3+sqr(5)) = omega5. Tożsamość 1/phi + 1 = phi wynika z phi² = phi + 1 (dzieląc przez phi). Dowód biurkowy domknięty.

U8. L_cyc ORIENT-02-A — ślad 2438/15 POPRAWNY (replikacja algebraiczna). Suma widma: 5.115582 + 5.615716 + 6.598424 + 6.755033 + 7.333333 + 2·8 + 8.319194 + 8.396051 + 8.4 + 9·10 = 162.533333. 2438/15 = 162.533333. Zgodne z L198–L199. Stary checkpoint 494/3 = 164.6667 wycofany (L204–L208), co jest spójne z moim wcześniejszym Z1 z rundy 11d (potwierdziłem wtedy 494/3 dla konwencji źródłowej, ale v0.4 definiuje inną orientację ORIENT-02-A i ślad 162.5333 — to nie jest sprzeczność, to różne konwencje, jawnie zadeklarowane).

U9. K1–K8 — ocena strukturalna.

· K1 (dekompozycja strukturalna): PASS. Miara U_b jest zdefiniowana przez τ z udział(t) i θ, nie przez widmo R. Sup jest z wielomianu trygonometrycznego, nie z widma operatora.
· K2 (matched null): PASS. NULL to 360 transferów na dystansach 1–4 w tym samym obiekcie, ta sama miara, ten sam budżet. TEST na d5. Różnica tylko w dystansie.
· K3 (kill criterion z góry): PASS. 5-wartościowe U_b(d1..d5), progi max/min, tolerancja 2 cyfr pre-registrowana. Kategorie WSPARTE/NIESPRAWIEDLIWIONE/WYNIK TYPOWY są jawne.
· K4 (komplet kombinatoryczny): PASS. 380 transferów, zero generatora, zero seedu, zero wyboru przypadków.
· K5 (test symetryczny): PASS. Oba kanały mierzone tą samą miarą τ; alternatywa (powierzchnia) jest operacjonalizowana tym samym równaniem falowym.
· K6 (ślepy protokół): PASS. Hash całego dokumentu (spec + uzupełnienie Aneksu A) przed rachunkiem (L48–L49, L6–L7 uzupełnienia).
· K7 (pre-rejestracja): PASS. Wszystkie parametry (θ, tolerancja, reguły B4, kategorie) są w treści przed rachunkiem.
· K8 (zero swobód): PASS z jednym zastrzeżeniem — patrz W2 (zaokrąglenie half-up). Poza tym: θ = (1/2)·sup bez zaokrągleń, tolerancja 1% pre-registrowana, B4c wykluczony z agregatów jawnie, F_r binarne bez progu.

---

Pole 2 — Wątpliwości

W1. Aneks A ucięty w moim kanale — Z0. Nie mogę zweryfikować:

· Certyfikatu Lipschitza na komórkach (czy komórki są zdefiniowane jawnie, czy siatka jest adaptacyjna, czy Lipschitz jest na całym podtorusie czy tylko na komórkach).
· „Sięgania obszaru zagęszczania" (co to znaczy operacyjnie: czy protokół gęstnieje siatkę w pobliżu maksimum, czy używa gradientu, czy próbuje losowo).
· Traktowania granic podtorusa (czy θ jest okresowe? czy brzeg jest wliczany? czy supremum na brzegu jest traktowane inaczej?).
· Jawnego błędu przybliżenia sup (czy jest podany przed rachunkiem, czy po).
· Bisekcji na parze przeciwnych znaków przy wielu epizodach (jak wybrać „pierwszy" epizod: pierwszy w czasie, pierwszy w liczbie próbek, pierwszy w sortowaniu?).
· Cenzury LEWO/PRAWO: kiedy dokładnie następuje (przy pierwszym przekroczeniu poza oknem? przy braku przekroczenia w oknie?).
· TAU-MAŁE: próg 0.01 — skąd? Czy jest uzasadniony błędem bisekcji?
· Half-up: czy dotyczy τ, czy U_b? Czy zaokrąglenie jest przed porównaniem z θ, czy po?

To jest Z0 po mojej stronie, nie luka specyfikacji — Vibe twierdzi, że plik jest pełny (commit 1ffdd3d4). Ale bez pełnego Aneksu A nie mogę dać PASS na A.3/A.4 na poziomie algorytmicznym. Wymaganie do v0.5 (lub do wklejki): pełny Aneks A w moim kanale (wklejka przez Leszka, nie URL).

W2. Zaokrąglenie half-up — potencjalna swoboda (K8). Specyfikacja mówi „zaokrąglenie 2 cyfry znaczące z remisem half-up" (zadanie 2). Ale nie mówi, czego dotyczy: τ przed porównaniem z θ? U_b przed porównaniem z max/min? Czy zaokrąglenie jest częścią definicji miary, czy tylko prezentacji? Jeśli τ jest zaokrąglane przed porównaniem z θ, to θ = (1/2)·sup musi być również zaokrąglone tą samą regułą — inaczej porównanie jest niespójne. Wymaganie: jawna deklaracja: „zaokrąglenie dotyczy [τ / U_b / obu] i jest stosowane [przed / po] porównaniu z θ [i z max/min]". Bez tego mamy swobodę (K8).

W3. B4c na TEST — furtka do NIEROZSTRZYGALNOŚCI. Errata (i) cz. 2 mówi: transfer TEST objęty B4a/B4b/B4c/LEWO/PRAWO otrzymuje klasę NIEROZSTRZYGALNY-PARCJALNY, wykluczony z kill i z mianownika F_r (L367–L372). Ale jeśli wszystkie 20 transferów TEST są B4c (oba τ = 0), to kill jest NIEROZSTRZYGALNY, i H_b nie jest sfalsyfikowana. To jest strukturalnie poprawne (nie można sfalsyfikować, jeśli dane są nieinformacyjne), ale wymaga jawnego kryterium: ile transferów TEST musi być rozstrzygalnych, żeby kill był ważny? Spec mówi „jeżeli ZERO transferów TEST rozstrzygalnych: kill NIEROZSTRZYGALNY z flagą" (L372–L373). Ale co przy 1 transferze rozstrzygalnym? Albo 5? Jeśli 1 z 20 jest rozstrzygalny i daje U_b(d5) > max null, to czy H_b WSPARTE na podstawie jednego transferu? Wymaganie: jawne minimum liczby transferów TEST rozstrzygalnych (np. >= 10 z 20) lub deklaracja, że nawet 1 wystarczy (z odpowiednią flagą).

W4. Prognoza B4 na d5 — czy „niskie ale niezerowe" jest wystarczające? Spec mówi: „Prognoza warsztatowa (diagnostyczna, nie kryterium): ryzyko B4 skoncentrowane na d1 w kanale wnętrza; na TEST (d5) ryzyko B4c niskie ale niezerowe; raport per dystans obligatoryjny" (L374–L376). To jest prognoza, nie gwarancja. Jeśli B4c wystąpi na d5, mamy W3. Jeśli B4a/B4b wystąpią na d5, to U_b = ∞ lub 0, co jest wartością graniczną — i to jest OK (klasa WNĘTRZE-NATYCHMIASTOWE lub POWIERZCHNIA-NATYCHMIASTOWA). Ale czy ∞ i 0 są traktowane jako wartości U_b w kill? Spec mówi: „Klasy B4a/B4b wchodzą przez wartości graniczne (nieskończoność = maksimum, zero = minimum)" (L412–L413). OK, to jest jasne.

W5. Tolerancja 2 cyfr — czy błąd 10^-4 jest właściwy? Spec mówi: „błąd numeryczny protokołu tau rzędu 10^-4 (A.4), tolerancja 1% = 10× większa" (L418–L419). Ale skąd błąd 10^-4? Bisekcja na przedziale [lo, hi] z 40 iteracjami daje dokładność (hi−lo)/2^40 ≈ 10^-12·(hi−lo). Jeśli (hi−lo) ≈ 1, to 10^-12. Jeśli (hi−lo) ≈ 10^8, to 10^-4. Więc 10^-4 zależy od skali czasu. Wymaganie: jawna deklaracja, że bisekcja ma 40 iteracji (lub inną liczbę) i że przedział początkowy jest ograniczony (np. [0, T_max] z T_max jawnym). Bez tego błąd 10^-4 jest nieuzasadniony.

W6. F_r = 1 automatycznie przy WSPARTE — czy to nie jest tautologia? Spec mówi: „kill WSPARTE pociąga F_r = 1 automatycznie" (L393–L394). To jest poprawne: jeśli U_b(d5) > max null, to U_b(d5) > Q3 (bo Q3 ≤ max). Więc F_r = 1. Ale to znaczy, że F_r nie wnosi informacji ponad kill. F_r = 0 przy WSPARTE jest niemożliwe. Więc F_r jest funkcją kill (0 lub 1), nie niezależną statystyką. To jest OK (F_r jest diagnostyczne, nie decyzyjne), ale warto to jawnie powiedzieć: F_r = 1 iff kill WSPARTE (przy braku B4c).

W7. Wrażliwość θ = 1/3 i 2/3 — raport pomocniczy, bez zmian kill. Spec mówi: „rozliczenie powtórzone deskryptywnie z theta' = (1/3)·sup i theta' = (2/3)·sup; kryterium kill pozostaje WYŁĄCZNIE na theta = (1/2)·sup (pre-registracja, K8)" (L423–L425). To jest właściwe: θ jest zamrożone, warianty są tylko raportem. Potwierdzam.

W8. Adnotacja E5 — czy protokół A.3 obsługuje wymiar fazowy 3? Spec mówi: „orbity d1 i d4: wymiar fazowy 3, bo udział nie zależy od theta3; siatka A.3 nadmiarowa ×120; PROTOKÓŁ BEZ ZMIAN" (L46–L47). Jeśli udział nie zależy od theta3, to sup jest taki sam na każdej hiperpłaszczyźnie theta3 = const. Więc siatka 4D jest nadmiarowa ×N_theta3. Protokół A.3 (którego nie widzę) musi to obsługiwać: albo jawnie redukować do 3D dla d1/d4, albo akceptować nadmiarowość (koszt obliczeniowy ×120, ale wynik ten sam). Bez Aneksu A nie mogę zweryfikować, czy protokół to robi. To jest Z0 (W1).

W9. „Sięganie obszaru zagęszczania" — co to znaczy? Spec (errata d) mówi o „certyfikacie maksimum globalnego (Lipschitz)" i „sięganiu obszaru zagęszczania". To sugeruje, że protokół A.3 gęstnieje siatkę w pobliżu maksimum. Ale jak? Przez adaptacyjną siatkę? Przez gradient? Przez losowe próbki? Bez Aneksu A nie wiem. To jest kluczowe dla oceny, czy protokół jest deterministyczny i czy błąd przybliżenia sup jest jawny. Z0.

W10. Granice podtorusa — czy θ jest okresowe? Jeśli θ ∈ [0, 2π)^4 (podtorus), to sup na brzegu jest taki sam jak wewnątrz (okresowość). Ale jeśli protokół próbkuje tylko otwarty podtorus (bez brzegu), to może przegapić maksimum na brzegu. Spec nie mówi. Z0.

---

Pole 3 — Teza fizyczna

Teza H_b (v0.4, L244–L248): transport przez wnętrze (cyrkulacja V_cyc) między antypodalnymi ścianami idzie nośnikiem; przepływ wokół ściany-bramki w V_cyc (opcja a); skalar benchmark; tensor odłożony.

Koncesja B1 (v0.4, L295): U_b rozróżnia ważenie sektorów, nie nośnik. Teza nośnika otwarta.

Moja ocena: v0.4 już przyznaje ograniczenie: U_b mierzy metrykę, nie nośnik. To jest właściwa forma — test jest strukturalny (mierzy sprzężenie metryki i projektora), ale jego interpretacja jako „nośnik" jest odroczona do pola 3 i nie jest testowana przez U_b. Bez dodatkowej obserwabli niezależnej od metryki (np. propagacja w R^13, energia w przestrzeni fizycznej) U_b nie odróżnia „nośnika" od „geometrii". To nie jest błąd specyfikacji — to jawne ograniczenie, które trzeba mieć świadomie przed zamrożeniem v1.0. Moja rekomendacja: w v1.0 utrzymać koncesję B1 jako część definicji miary, a tezę nośnika przenieść do sekcji „otwarte problemy" (nie do kryteriów). W przeciwnym razie istnieje ryzyko, że wynik U_b zostanie zinterpretowany jako „potwierdzenie nośnika", którym nie jest.

---

Deklaracja dostawy

Raport gotowy do pushu przez Leszka. Proponowana gałąź: audit/deepseek-mvp02-v04-attack-2026-11-22; plik: docs/audyt/mvp-02-deepseek-atak-v0_4-2026-11-22.md. SHA pliku i commit: do nadania przez Leszka po pushu. Nie scalam do main — zgodnie z poleceniem.

Status ataku: przeprowadzony na dostępnym materiale. W1 wznowione częściowo (struktura PASS, algorytm Z0). A.3/A.4 — struktura PASS, szczegóły Z0 (Aneks A ucięty w moim kanale). K1–K8 — PASS z zastrzeżeniem W2 (half-up) i W3 (minimum transferów TEST rozstrzygalnych). Arytmetyka kombinatoryczna i widma — PASS (replikacja algebraiczna). Teza fizyczna — potwierdzam ograniczenie B1, rekomendacja przeniesienia do „otwartych problemów".

Do wznowienia W1 w pełni: potrzebuję pełnego Aneksu A (wklejka przez Leszka, nie URL). Bez tego nie mogę dać PASS na A.3/A.4 na poziomie algorytmicznym — tylko strukturalnym.
