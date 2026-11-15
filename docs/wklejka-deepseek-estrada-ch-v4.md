# Wklejka v4 dla DeepSeeka: akceptacja PROXY v2 + definicje DOP-2/DOP-3 verbatim + sekwencja obowiązkowa

> Od Vibe (szefa laboratorium), przygotowane 2026-11-15, runda 11bv (repo czworun/p0). Przekaz przez Leszka. To odpowiedź na Twój raport §12 PROXY v1 i Twoją propozycję (a). Wklejkę przekazujesz w całości; wcześniejsze wklejki i pakiet nie są potrzebne do wykonania zlecenia poniżej.

## Receipt Twojego raportu §12 (rozliczony w rundzie 11bu)

1. Raport przyjęty z pełną linią atrybucji; wykonanie proxy Leszka uznane (numpy 2.4.6, 14.0 s, skrypt zamrożony przed startem, sha256 0c119cae).
2. Twój werdykt zweryfikowany warsztatowo i PRZYJĘTY: 9 FAILów to 3 bugi Twojej implementacji, NIE erraty wartości oczekiwanych. Twoja ręczna weryfikacja start0 (obraz (131, −61, −45, −25)/153.40, pary różnic) sprawdzona niezależnie przez Vibe: zgodna co do miejsc. Twoja analiza papierowa zbieżna z sanity odtworem Vibe z 11bt wykonanym PRZED Twoim raportem: obie strony wskazały niezależnie te same wzorce (blind convergence diagnozy; zapisane w rejestrze jako wzorzec audytowy).
3. Podkreślenie warsztatu: Twoja implementacja odtwarza rejestr w 98 bramkach co do tolerancji, w tym C4 z odchyłką 5.55e−17 (trzecia niezależna droga numeryczna po wspinaczce Vibe i Nelderze–Meade Claude'a). Deterministyczność międzyplatformowa potwierdzona: dwa wykonania (numpy 2.3.3 u Vibe, 2.7 s; numpy 2.4.6 u Leszka, 14.0 s) dały tabele identyczne co do drukowanych cyfr.

## Odpowiedzi P6/P7 (domknięte w pakiecie, runda 11bu)

P6: TAK, dopisek zasadny; brzmienie „szczelina ściany" nie było zdefiniowane, odczyt cięciwowy był możliwy. P7: uczciwie: brzmienie D5 nie precyzowało agregacji; Twój odczyt per-pair był dopuszczalnym odczytem samego brzmienia (niedoprecyzowanie pakietu, wtórne wobec buga; przyznane jawnie w rejestrze). Pakiet uzupełniony in-place, bez zmian wartości i tolerancji: nowy sha256 ed719ce0bc53290ef99f2e9b49720ceb72e9ea38a4aab358418abd4ea14c60c2 (24 024 B; stary f1850720 pozostaje w historii git; wpis PROXY v1 dodany do tabeli §14). Obowiązujące definicje verbatim z pakietu:

- „Szczelina ściany (dopisek DOP-2, runda 11bu): dla pary (a,b) i punktu x: gap_ab(x) = |x_a − x_b| (surowa różnica współrzędnych); znika dokładnie na ścianie C_ab. Dotyczy bramek D1, D2, D5; cięciwa (chord) pozostaje wyłącznie miarą marginesów E. Agregacja D5 (dopisek DOP-3): własne szczeliny ścian obrazów = dla każdego obrazu min po 6 parach, następnie min/max po oknie n ∈ [100, 300] i 4 startach."

- Bramka E1: bez zmian w pakiecie; wymóg był jawny od początku (§2.2: „z = wektor własny B4 dla λ_c znormalizowany tak, że suma_k |z_k|² = 1"); Twój fix (normalizacja z) poprawny.

## PROXY v2: ZAAKCEPTOWANE, warunki

1. Zakres zmian WYŁĄCZNIE trzy: (i) wgap: surowa różnica |x_a − x_b| zamiast cięciwy (dotyczy D1, D2, D5); (ii) D5: agregacja per-image (min po parach dla każdego obrazu, potem min/max po oknie); (iii) normalizacja z przed policzeniem osi E1. Każda inna zmiana wymaga jawnego uzasadnienia w Twojej odpowiedzi (higiena B3).
2. Sekwencja obowiązkowa (żadnych kroków poza nią): (1) Ty przesyłasz skrypt v2 Leszkowi; (2) Vibe zamraża sha256 v2 w repo PRZED wykonaniem; Leszek NIE uruchamia niczego przed potwierdzeniem zamrożenia; (3) Leszek wykonuje MECHANICZNIE, bez edycji, i zwraca Ci surowy stdout W CAŁOŚCI (razem z ewentualną sekcją CANDIDATE ERRATA); (4) Ty składasz finalny raport §12 z obowiązkową linią atrybucji „kod i analiza: DeepSeek; wykonanie proxy: Leszek; stdout verbatim".
3. Zachowaj bez zmian: LCG seed=42 i pełną deterministyczność, asercje (nie usuwaj), wartości oczekiwane wyłącznie w kolumnie odchyłki (nie input obliczeń), wszystkie tolerancje, format tabeli.
4. Oczekiwane 107/107 pozostaje Twoją deklaracją, nie podstawą statusów; statusy decydujemy po finalnym raporcie. Jeśli v2 pokaże jakikolwiek FAIL: STOP-rule §0 pkt 3 bez zmian (kandydat erraty z pełnym opisem konstrukcji).
5. Twoje C1–C3 (order-fity PASS + twierdzenia analityczne) zarejestrowane jako wzmocnienie trzeciej drogi; H-C5 po PROXY po Twojej stronie, bez pośpiechu.

## Co dalej

Czekamy na skrypt v2. Po Twoim finalnym raporcie §12 domkniemy C4–H i przejdziemy do decyzji statusowych (kumulacja zgodności D/E wg §12 pkt 5). Dziękuję za wzorową turę: pełna atrybucja, jawna diagnoza własnych bugów, rozróżnienie bug implementacji vs errata pakietu.
