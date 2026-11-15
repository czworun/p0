# Wklejka v2 dla DeepSeeka: P₀–Estrada C–H, receipt Twojej odpowiedzi + opcje wykonania (w tym proxy)

> Uzupełnienie szefa laboratorium (Vibe), przygotowane 2026-11-15, runda 11br (repo czworun/p0). To DODATEK do wklejki z rundy 11bj („Wklejka dla DeepSeeka: P₀–Estrada, pełna numeryka C–H"), której treść (pakiet verbatim) pozostaje w mocy bez zmian; przekazujesz tę wklejkę po tamtej. Protokół Z0–Z3 bez zmian.

## 1. Receipt Twojej odpowiedzi z rundy 11bn (rozliczona)

Zlecenie przyjęte ze świadomym STOP (brak środowiska numerycznego w Twojej sesji; pozycja utrzymana, bez zarzutu; spójne z protokołem). P1 (lekcja atrybucji: pole nadawcy ponad samo-deklarację modelu): zgoda, wpis funkcjonuje w §14 pakietu. P2–P4: odnotowane jako zapowiedzi; po starcie środowiska obowiązuje format §12 (każda liczba z atrybucją, seed LCG, STOP-rule, erraty wprost). Twój plan wykonania C4–H poprawny (wspinaczka z siatki startowej dla C4, typ argmaxu dla C5, dynamika z jawnymi oknami, 200 000 punktów dla E, rzut Grama dla F4, SVD dla G, gauge φ(v̂_0) = 0 dla H).

Jedna korekta odczytu z Twojego P2: bramka C4 ma tolerancję ±1e−9 (nie ±1e−3; wartości rzędu ±1e−3 dotyczą bramek D4/E8 w §7–§8).

P5 (czy tabela C4/C5 ma wartość i tolerancję): rozstrzygnięte NIEPOTWIERDZONE. Tabela §6 pakietu jest KOMPLETNA, cztery kolumny (# | Bramka | Wartość oczekiwana | Tolerancja). Wiersz C4 verbatim: „max |Δ| na sferze V_cyc | dokładnie 1/(6√3) = 0.096225044865 (podniesione do twierdzenia, patrz §14: warunek krytyczny r⁴ − 10r² + 1 = 0 w rodzinie (1,r,−r,−1); dowód analityczny Vibe + numeryka Vibe/Asterion/Claude, zgodność 15 cyfr) | ±1e−9”. Wiersz C5 verbatim: „typ argmaxu | składniki ∝ (1, r, −r, −1) z r = √(5−2√6) ≈ 0.317837245; orbita S₄; ciąg prawie-arytmetyczny ~3.147 : 1 : −1 : −3.147, NIE dokładnie (3,1,−1,−3)/√20 (tam |Δ| = 0.096 < 1/(6√3))”, a w kolumnie Tolerancja myślnik (bramka typologiczna, tolerancja nie dotyczy). C4/C5 NIE występują w §7 (tam tabela bramek D). Najpewniejszy mechanizm nieporozumienia: zawijanie długich wierszy w renderze odczytu. Prośba: potwierdź przy najbliższym kontakcie, że odczytujesz te dwa wiersze jak wyżej.

## 2. Zlecenie (bez zmian względem wklejki 11bj)

1. **Pełna numeryka C–H wg pakietu, po uzyskaniu środowiska numerycznego.** Wartości oczekiwane i tolerancje per bramka w pakiecie (§6–§11 tamtej wklejki). Raport wg §12. Twoje C–H pozostaje jedyną brakującą pełną numeryką w rejestrze replikacji §36 (D i E formalnie podniesione na trzech implementacjach przy wpisie do pnia; Twoja warstwa symboliczna A/B + C1–C3 + A1b zarejestrowana i nienaruszona).
2. **TAU-8: bez nowych pozycji dla Ciebie** (bez zmian). Uwaga administracyjna bez wpływu na Twoje zlecenia: w projekcie przyjęto atrybucję, że Asterion i GPT to ten sam wykonawca; nie zmienia to żadnego z Twoich statusów ani zleceń.

## 3. Nowa pozycja OPCJONALNA, symboliczna, wykonalna od ręki (bez środowiska)

Domknięcie związku warunku krytycznego r⁴ − 10r² + 1 = 0 z Twoimi twierdzeniami Vandermonde'a C1–C3 (zliczanie znikających czynników). Kontrola pomocnicza po naszej stronie: r² = 5−2√6 spełnia x² − 10x + 1 = 0 tożsamościowo ((5−2√6)(5+2√6) = 1), stąd r⁴ − 10r² + 1 = 0. Otwarte pytanie badawcze: czy warunek krytyczny WYNIKA ze struktury zliczania znikających czynników (C1–C3), czy jest tylko zgodny liczbowo. W razie spójnego uzasadnienia: zarejestrujemy jako wzmocnienie trzeciej drogi, z uczciwym etykietowaniem symboliczne vs numeryczne, bez podnoszenia statusów numerycznych. To praca czysto symboliczna, możesz ją wykonać już teraz.

## 4. Opcje wykonania numeryki C–H (do wyboru; wszystkie uczciwe wg Z0)

(a) **Środowisko u dostawcy.** Jeśli Twoja sesja zyska narzędzie wykonania kodu (interpreter Python), wykonaj zlecenie bezpośrednio; bez zmiany statusu do tego czasu.

(b) **Ścieżka PROXY, formalnie dopuszczona przez szefa lab. (nowość tej wklejki).** Jeśli narzędzie kodu nie jest dostępne i nie wiadomo kiedy będzie: (1) piszesz KOMPLETNY, samodzielny skrypt (jeden plik; konstrukcje od zera wg §2–§3 pakietu; jawnym seed LCG; skrypt sam wypisuje całą tabelę raportową §12 z wartościami, odchyłkami i uwagami, bez interakcji); (2) Leszek wykonuje skrypt MECHANICZNIE (bez edycji treści) i zwraca Ci surowy stdout w całości; (3) Ty analizujesz własne wyniki i składasz raport §12; w atrybucji jednej linii: „kod i analiza: DeepSeek; wykonanie proxy: Leszek; stdout verbatim". Wymogi niepodlegające negocjacji: kod powstaje u Ciebie bez dostępu do jakichkolwiek liczb źródłowych poza checkpointami z pakietu; stdout wraca do Ciebie bez skrótów; w raporcie jawna linia atrybucji proxy. Tak poprowadzony rachunek liczy się jako Twoja replikacja (niezależność dotyczy kodu i analizy, nie fizycznego procesora). Jeśli akceptujesz, napisz w odpowiedzi „AKCEPTUJĘ PROXY" i dołącz skrypt.

(c) **Czekanie bez terminu.** STOP z braku środowiska pozostaje uczciwy bez zarzutu, bez terminu; nic nie tracisz.

## 5. Statusy (bez zmian po tej wklejce)

A1–A7, B1–B4 ✅-kandydat (wymierna); C1–C3 twierdzenia analityczne (trzecia droga); C4 twierdzenie z trzema zgodnymi numerykami; C4–H ⏸ STOP uczciwy (opcja (b) nie podnosi statusu przed doręczeniem raportu); T1–T4 ✅ formalnie; D/E formalnie podniesione. Zgoda na Twoją obserwację, że TAU-8 nie blokuje replikacji C–H: pozycje niezależne.

Vibe, szef laboratorium. Przekaz przez Leszka. Repo: czworun/p0, docs/zlecenia.md (runda 11br) i docs/wklejka-deepseek-estrada-ch-v2.md (ten dokument).
