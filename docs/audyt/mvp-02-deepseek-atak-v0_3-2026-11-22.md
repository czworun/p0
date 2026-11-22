Atak DeepSeeka na MVP-02 v0.3

0. Receipt i deklaracja

Dokumenty pobrane: spec v0.3 (commit 6bc55f66, 430 linii) i uzupełnienie Aneksu A (92 linie wg metadanych GitHuba, 22 linie w renderze — ucięte). Z0–Z3 zachowane. Żadnych rachunków transportowych (K6). Dopuszczalne replikacje algebraiczne z §3 — wykonane na papierze. Liczby jawnym tekstem, potęgi jako a^b, zero LaTeXu, zero kodu.

Deklaracja słojowa: atak na strukturę specyfikacji, bez roszczeń do statusów.

---

Pole 1 — Ustalenia

A1. Kompletność 380/20/360 — POPRAWNA. 20 ścian × 19 = 380 uporządkowanych par. TEST: 10 nieuporządkowanych par d5 × 2 = 20. NULL: 180 nieuporządkowanych (d1–d4) × 2 = 360. Suma 20 + 360 = 380. Rozkład: d1 = 60, d2 = 120, d3 = 120, d4 = 60 uporządkowanych (suma 360). Arytmetyka domknięta.

A2. Kule dystansu — POPRAWNE. 3, 6, 6, 3, 1 na dystansach 1–5; suma 19 = 20 − 1. Zgodne z grafem 3-regularnym o średnicy 5.

A3. Wykaz par antypodalnych — POPRAWNY. 10 par wymienionych konkretnie. Sprawdzenie pośrednie: {f0, f19} = {[0,1,2], [9,10,11]}; antypodalność potwierdzona przez BFS warsztatu (Asterion B-06 domknięte). Zakładam poprawność.

A4. Bramki G0–G4 — POPRAWNE. Każda ściana w 2 konfiguracjach; każda para konfiguracji współdzieli 2 ściany antypodalne; N_sąs = 12; Gram ⟨s_G, s_G'⟩ = 6 − 12 = −6. Zgodne z L268 i L136.

A5. ρ_gate — DEFINICJA ZAMKNIĘTA. |λ₂| operatora R_gate = 32 aktywacje M_local na ℝ¹³. Wartości zamrożone z etapu a. Det = 4^-32 = 256^-8. Zgodne z moim A1 z ataku na v0.1.

A6. Widmo L_dod — POPRAWNE. {0; 3−√5; 2; 3; 5; 3+√5}, krotności {1, 3, 5, 4, 4, 3}, suma 20. Ślad = 3(3−√5) + 10 + 12 + 20 + 3(3+√5) = 60. Zgodne z L413.

A7. Widmo L_eq — POPRAWNE (z niejasnością notacyjną). {3×(3−√5); 5×2; 4×3; 4×5; 3×(3+√5)}, krotności 3+5+4+4+3 = 19. Ślad = 60. Ale char poly podany jako x^11·(x−5)^4·(x−3)^4·(x−2)^5·(x^2−6x+4)^3 ma stopień 30 (na C_1), nie 19 (na V_cyc). Niejasność: spec nie mówi, na której przestrzeni jest char poly. Patrz W2.

A8. Rezonans ω5 = ω1 + ω2 — POTWIERDZONY. ω1 = √2/φ = 0.874032, ω2 = √2 = 1.414214, suma = √2(1/φ + 1) = √2·φ = ω5 = 2.288246. Tożsamość 1/φ + 1 = φ (z φ² = φ + 1). Dowód biurkowy domknięty.

A9. Twierdzenie metryczne — POPRAWNE. U = B·L_dod^(−1/2) jest izometrią z soma-zero (19-dim) na V_cyc. Wymiary: B: 30×20, L_dod^(−1/2): 20×20 (na soma-zero), U: 30×20 działające na soma-zero → V_cyc. Sprawdzone wymiarowo.

A10. Wejścia — POPRAWNE. ω_f/√3: norma 1 (‖ω_f‖² = 3, ω_f ∈ V_cyc). q_f/√(19/20): norma 1 (‖q_f‖² = 19/20). Zgodne z L255–L256.

A11. Udział(0) — POPRAWNE. Powierzchnia: 1/361 = 0.0028 (⟨q_f, q_h⟩ = −1/20, normy 19/20 → (1/400)/(361/400) = 1/361). Wnętrze: 1/9 = 0.1111 na d1 (⟨ω_f, ω_h⟩ = −1, normy 3); 0 na d2–d5. Zgodne z L319–L321.

A12. Kill criterion 5-wartościowe — STRUKTURALNIE POPRAWNE. U_b(d5) > max{U_b(d1..d4)} → WSPARTE; U_b(d5) < min → NIESPRAWIEDLIWIONE; pozostałe → WYNIK TYPOWY. Ale tolerancja 2 cyfr jest swobodą (K8) — patrz W3.

A13. F_r z Q3 null — STATYSTYCZNIE POPRAWNE. F_r = #{d5: U_b > Q3}/20, Q3 na randze 270 z 360. Pod null (wszystkie d5 z tego samego rozkładu co null): P(U_b > Q3) = 0.25. F_r = 1 pod null ma p ≈ 0.25^20 ≈ 9×10^-13 (bardzo silne). F_r = 0.5 pod null ma p ≈ 0.0098 (istotne na 1%). Ale brak jawnego progu istotności — patrz W4.

A14. Bramki sanity §3 — ALGEBRAICZNIE POPRAWNE. Wszystkie (SERC R_4, L_cyc 494/3, ρ_gate, L_eq/L_dod, Gram 24/−6, N_sąs = 12, cos² dla s/a, tabela ścian, rozkład par) są sprawdzalne algebraicznle. Kolejka replikacji algebraicznej (1)–(8) z §3 jest wykonalna przed bindem — zgodnie z K6.

---

Pole 2 — Wątpliwości

W1. Aneks A (główny) jest niedostępny — KRYTYCZNE. URL-e ze zlecenia nie zawierają Aneksu A; plik mvp-02-spec-v0_3-aneks-a.md nie istnieje (404); uzupełnienie mvp-02-spec-v0_3-aneks-a-uzupelnienie.md jest ucięte w renderze (22 z 92 linii, kończy się w środku formuły „+ suma_a"). Bez Aneksu A nie mogę zweryfikować protokołu fazowego, który jest krytyczny dla θ = (1/2)·sup. Atak na θ i protokół fazowy jest wstrzymany do czasu dostarczenia pełnego Aneksu A. To jest luka w materiale ataku, nie w specyfikacji — ale blokuje weryfikację K1–K8 w zakresie θ.

W2. Char poly L_eq — stopień 30 vs 19. Spec podaje char poly x^11·(x−5)^4·(x−3)^4·(x−2)^5·(x^2−6x+4)^3 (stopień 30, na C_1) oraz widmo {3×(3−√5); 5×2; 4×3; 4×5; 3×(3+√5)} (stopień 19, na V_cyc). Niejasność: która przestrzeń jest operatorem modalnym? L_eq = B·B^T na C_1 (30-dim), obcięte do V_cyc (19-dim). Char poly na C_1 ma jądro 11-wym. (A_u). Wymaganie: jawna deklaracja, że char poly jest na C_1 (przed obcięciem), a widmo na V_cyc (po obcięciu). Drobna niejasność notacyjna, nie błąd.

W3. Tolerancja 2 cyfr — swoboda (K8). Kill criterion wymaga różnicy > 2 cyfr znaczących (≈ 1%). Pytanie: czy to jest realistyczne dla numeryki τ? Błąd numeryczny ~10^-3 (z protokołu), więc 1% jest 10× większe — OK, ale arbitralne. Wymaganie: uzasadnienie, dlaczego 2 cyfry, a nie 1 lub 3. Alternatywnie: tolerancja jako funkcja błędu numerycznego (np. 10× błąd), nie stała.

W4. F_r — brak jawnego progu istotności. F_r = 1 jest silne (p ≈ 9×10^-13), ale F_r = 0.5 ma p ≈ 0.0098. Pytanie: jaki jest próg F_r, przy którym uznajemy H_b WSPARTE? Spec mówi „dodatkowo frakcja rangowa F_r = 1 publikowana obligatoryjnie" (L362), ale nie mówi, czy F_r < 1 wyklucza WSPARTE. Wymaganie: jawny próg F_r (np. F_r ≥ 0.5 przy p < 0.01) lub deklaracja, że F_r jest tylko diagnostyczne, a kill opiera się wyłącznie na 5-wartościowym U_b.

W5. B4c na d5 — ryzyko numeryczne. Prognoza: d5 nie powinno mieć B4c (wnętrze: ortogonalne → τ > 0; powierzchnia: udział(0) = 1/361 → τ > 0 chyba że sup < 2/361). Ale: jeśli sup jest bardzo małe dla d5 (np. projektor P_h prawie ortogonalny do wszystkich modów), θ może być < 1/361, i udział(0) = 1/361 > θ → τ_surf = 0 → B4b lub B4c. To jest realne ryzyko numeryczne. Wymaganie: zabezpieczenie (np. minimalne θ = 1/361 lub jawna deklaracja, że B4c na d5 jest możliwy i jak jest raportowany).

W6. „Półka sup" vs „połowa sup" — niejasność terminologiczna. Spec mówi θ = (1/2)·sup (L323). „Półka" sugeruje plateau, nie połowę. Pytanie: czy θ = (1/2)·sup dokładnie, czy θ = sup/2 zaokrąglone do plateau (np. jeśli sup jest osiągane na przedziale, to θ = połowa tego przedziału)? Wymaganie: jawna definicja: θ = (1/2)·sup_t udział(t), bez zaokrągleń.

W7. Kill criterion na 5 wartościach — zbyt restrykcyjny? Wymaga, żeby U_b(d5) była większa od wszystkich U_b(d1..d4) (max), nie od mediany. Alternatywa: porównanie z medianą null (360). Ale: spec wybrał max/min 4, co jest bardziej rygorystyczny. To jest decyzja projektowa, nie błąd — ale wymaga uzasadnienia, dlaczego max/min, a nie mediana. Jeśli U_b(d1..d4) są bliskie siebie, max/min ≈ mediana, więc różnica jest mała. Jeśli są rozproszone, max/min jest trudniejszy do spełnienia.

W8. Jednostki czasu — czy porównywalne? τ w jednostkach równania falowego. Oba kanały mają różne operatory (L_dod vs L_eq), ale widma identyczne po cechowaniu (twierdzenie metryczne). Więc τ jest porównywalne. Ale: czy amplitudy są porównywalne? Wejścia znormalizowane do 1. Cele 1-wym. rzuty. OK. Ale: czy „czas do progu" ma tę samą interpretację w obu kanałach? Tak, bo równanie falowe jest to samo. Potwierdzam porównywalność.

W9. Koncesja B1 — czy test ma sens? Twierdzenie metryczne mówi, że kanały są izometryczne. Test porównuje sprzężenia metryki i położenia projektora, nie niezależne prawa propagacji. U_b mierzy metrykę, nie nośnik. H_b mówi „nośnik fizyczny", ale U_b tego nie testuje. Niespójność między H_b a U_b. Spec wpisał koncesję B1 wprost (L243–L250), ale nadal mówi w H_b "idzie nośnikiem" (L200–L201). Wymaganie: albo H_b przeformułować na „test sprzężenia metryki", albo U_b uzupełnić o obserwablę niezależną od metryki (np. propagacja w przestrzeni fizycznej R^13). Bez tego test jest strukturalnie poprawny, ale jego interpretacja jako test nośnika jest nadinterpretacją.

W10. Degeneracja orbit — 5 wartości U_b. Miara parzysta + równowariantność I_h ⇒ U_b stałe na orbitach. Spodziewane dokładnie 5 wartości (po jednej na dystans). To jest właściwość designu (koncentruje statystykę), nie blokada. Ale: czy 5 wartości wystarczy do statystyki? F_r = #{d5: U_b > Q3}/20 — to jest 20 testów, ale wszystkie z tej samej orbity (jeśli d5 jest jedną orbitą). Więc F_r jest funkcją jednej wartości U_b(d5) i Q3. Przy 20 testach z tej samej wartości, F_r może być tylko 0 lub 1 (albo 0.5, jeśli U_b(d5) = Q3 dokładnie). To jest poważny problem: F_r traci sens przy degeneracji orbit. Wymaganie: albo F_r zdefiniować inaczej (np. na 360 null, nie na 20 d5), albo jawnie przyznać, że F_r = 0 lub 1 (binarne), i raportować jako takie.

W11. B4c — wykluczenie z agregatów. B4c (τ_int = τ_surf = 0) jest wykluczony z agregatów (L331–L332). Ale: jeśli B4c występuje na d5 (co jest mało prawdopodobne, ale możliwe — W5), to d5 jest wykluczony z testu, i F_r jest liczony na mniejszej próbie (nie 20, ale 20 - #B4c). Wymaganie: jawna deklaracja, jak B4c na d5 wpływa na F_r (czy mianownik się zmienia, czy B4c jest traktowany jako „nie-test").

---

Pole 3 — Teza fizyczna

Teza H_b: transport przez wnętrze (cyrkulacja V_cyc) między antypodalnymi ścianami jest szybszy niż przez powierzchnię (propagacja ścian).

Operacjonalizacja: U_b = τ_surf/τ_int. H_b WSPARTE, jeśli U_b(d5) > max{U_b(d1..d4)} (wnętrze szybciej, bo τ_int mniejsze ⇒ U_b większe). H_b NIESPRAWIEDLIWIONE, jeśli U_b(d5) < min (powierzchnia szybciej). W przeciwnym razie WYNIK TYPOWY.

Koncesja B1: U_b mierzy metrykę, nie nośnik. Teza o nośniku fizycznym pozostaje wyłącznie w tym polu, nie jest testowana przez U_b. Test jest strukturalny (mierzy sprzężenie metryki), ale jego interpretacja jako „nośnik" jest nadinterpretacją, którą spec jawnie wpisał w koncesji B1. Wymaganie: albo H_b przeformułować na „test sprzężenia metryki", albo uzupełnić U_b o obserwablę niezależną od metryki.

Moja ocena: test jest strukturalnie poprawny (mierzy coś realnego — sprzężenie metryki i projektora), ale jego związek z tezą o nośniku jest słaby. Bez dodatkowej obserwabli (np. propagacja w R^13, energia w przestrzeni fizycznej), U_b nie odróżnia „nośnika" od „geometrii". To nie jest błąd specyfikacji — spec jawnie to przyznaje (koncesja B1). Ale to jest ograniczenie testu, które trzeba mieć świadomie przed zamrożeniem v1.0.

---

Deklaracja dostawy

Raport gotowy do pushu przez Leszka. Nie mam narzędzia do zapisu w repo. Zawartość raportu: powyższe trzy pola. Plik docelowy: docs/audyt/mvp-02-deepseek-atak-v0_3-2026-11-22.md, gałąź audit/deepseek-mvp02-v03-attack-2026-11-22 (do utworzenia przez Leszka). SHA pliku: do nadania przez Leszka po pushu. Commit: do nadania przez Leszka. Nie scalam do main — zgodnie z poleceniem.

Status ataku: przeprowadzony na dostępnym materiale. Atak na θ i protokół fazowy wstrzymany do dostarczenia pełnego Aneksu A (W1). Atak na pozostałe elementy (kompletność, B4, kill, F_r, wrażliwość, twierdzenie metryczne) — złożony.
