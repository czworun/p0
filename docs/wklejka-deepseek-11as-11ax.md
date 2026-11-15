# Wklejka dla DeepSeeka: rundy 11as–11ax (materiał do pełnego A1–F3)

Wycinek pliku docs/zlecenia.md (repo czworun/p0, branch main, commit 1b0662c4a73f193281170b3f34078c70640a37a8, md5 7e5fc26cde0bdab066582610a86ea77b, stan na 2026-11-15): sekcje od „## Runda 11as.” do końca pliku, bez żadnych zmian treści. Cel: przegląd A1–F3 logów 11as/11at/11au/11av/11aw (11ax = rejestracja rechecku DeepSeeka i decyzje). Plik pomocniczy; kanoniczne źródło: docs/zlecenia.md.

---
## Runda 11as. Przeglądy 11ar; zamknięcie N46; decyzja S5 droga (a); prerejestracja re-runu baterii; jawna diagnostyka pre-run

**Data (UTC):** 2026-11-14T23:29Z
**Narzędzia:** bez zmian względem 11ar: K17f-v2, sha256 `f92f8152c417d84baba400188c9027f449adc4f526587330f469c1e7d4d2e2e3` (potwierdzony ponownie systemowym sha256sum w tej rundzie, przed diagnostyką).
**Artefakty wejściowe:** bez zmian; pełne hasze potwierdzone ponownie systemowym sha256sum w tej rundzie: cRAB `b15812f1e8008700b531c7e5f13fe174d9b9768181d22094f7a462d1545f7040`, pNat `9862d44492a87a56dc4db2fccb36caa8d6e8df8de82cf4f5c8d15a5380b3194f`, pRev `0d47971478824a997a3ab3783d732f9e83040f3f30f20ba77511e9b1f2aa4f93`, pCut `feb2924424b70847c0c969051edb13bca2459611e002f5bb6eaf98b4a0ae2352`, gammasRAB `a1688893677ef3cff2936400cc390d1cb03482e87e0ffbce99c3c279b34eb4ca`.

### 1. Rejestracja przeglądów 11ar

1. **GPT/Asterion:** 11ar wyraźny postęp względem 11aq (rozdzielenie Jacobi/GS, jawna luka S5, populacja nietknięta). Stanowisko S5: droga (a), re-run odziedziczonej baterii na finalnym kodzie (hasz wiążący `f92f8152...`), bo w łańcuchu wersji są już rozbieżności implementacyjne i haszowe. Wymagania raportu re-runu, przyjęte do protokołu: dla każdego testu nazwa i wersja narzędzia, hasz kodu, identyfikator obiektu kontrolnego, kryterium zaliczenia, wynik rzeczywisty, status PASS/FAIL bez dziedziczenia z 11an; 4b′ jawnie oznaczone jako errata, nie test pierwotny; re-run nie zmienia historii prerejestracji. Zakres: t1–t7, sanity SHA-256, S1–S4, (6a)–(6d), 4a, 4b′. Zasada: jeśli którykolwiek test nie przejdzie, zapisujemy FAIL i rozliczamy osobno; nie poprawiamy wyników, progów ani kryteriów w trakcie re-runu. Po re-runie Asterion żąda końcowego przeglądu: zgodność kompletnego zakresu z §1.10, przypisanie hashy do wszystkich testów, rozliczenie dawnej rozbieżności pNat/pRev/pCut z 11aq, zgodność E2 i Rouché z literalną ścieżką v1.0. E18b nadal HOLD.
2. **DeepSeek:** PASS warunkowy 11ar. S1 przyjęte z zastrzeżeniem rejestrowym (PASS rechecku 11an oznaczyć jako warunkowy: konwencja cRAB zweryfikowana dopiero w 11ar). S2 przyjęte; uwaga na v1.1: wartości kontrolne zawsze w logu, nie w notatkach sesyjnych. S3 przyjęte (78/78 spójne z 11an). S4 przyjęte; drobna uwaga: obie ścieżki ewaluacji p wymienić jawnie w v1.1. S5: luka jawna, decyzja należy do Asteriona. N45 PASS przyjęte; uwaga na v1.1: jawna lista parserów i przypisanie do testów. N46: postawił kryterium: E18b może ruszyć wtedy i tylko wtedy, gdy hasze wejść 11ar są odtwarzalne z aktualnych artefaktów; prefiksy 11aq ewentualnie historyczne. Nie zgłasza STOP; pełny A1–F3 po dostępnym logu.
3. **Copilot:** blokada A3 zamknięta; 11ar PASS w zakresie A3 (R_AB: BASE 200 iter/1.87e-14 FAIL, E2 191 iter/2.06e-16 PASS; cut: BASE 200 iter/1.28e-14 FAIL, E2 184 iter/1.11e-16 PASS; nat 78/1.23e-16, rev 78/1.60e-16, BASE PASS bez E2; Perron (a) 4/4, (b) R_AB). Rekomendacja S5: droga (a) (jeden finalny hasz, jedna kompletna bateria, jeden PASS); droga (b) ponownie wymuszałaby dowodzenie nieoddziaływania zmiany DK na testy odziedziczone. Hasze 11aq nieodtwarzalne: zostawić jako nieodtworzone historyczne identyfikatory, źródłem kwalifikacyjnym są hasze finalnego runu; nie rekonstruować na siłę. Po czystym PASS pełnej baterii na finalnym haszu: brak dalszych blokerów po stronie Copilota do rachunku 361.
4. **Kimi:** potwierdzenie commita `8d999a51ee49e66419a35abd36bc089ed9e9072e` (zawartość zweryfikowana, md5 `0970c627288f694b21a87775252e71ea`, 300069 B); tabela wyników re-kwalifikacji zgodna z 11an.
5. **Claude:** przerwa; recheck odroczony, nie blokuje decyzji S5; opcjonalna kontrola Z1 po powrocie.

### 2. Zamknięcie N46 (rozbieżność hashy wejść 11aq)

Kryterium DeepSeeka spełnione: pełne hasze wejść 11ar są odtwarzalne co do bajta z aktualnych artefaktów (cRAB zgodny 11aq = 11ar: `b15812f1...`; pNat/pRev/pCut: pełne wartości 11ar odtwarzalne; prefiksy 11aq `176b6666...`/`ae0a5e79...`/`522d42a9...` nieodtwarzalne żadnym wariantem haszowania, testowanym już w 11ar). Decyzja (zgodnie z rekomendacją Copilota, zaakceptowaną w wątku przez DeepSeeka): prefiksy 11aq pozostają w rejestrze jako nieodtworzone historyczne identyfikatory; 11aq superseded przez 11ar dla zakresu DK; kanonicznym źródłem kwalifikacyjnym dla E18b są hasze finalnego runu (11ar/S5). Nie rekonstruujemy starych hashy na siłę. N46: zamknięte jako rozliczone-historyczne.

### 3. Decyzja S5: droga (a)

Leszek udzielił w tej sesji jawnej delegacji pełni decyzyjnej (cyt. za protokołem sesji): „Ty decydujesz. Jesteś szefem laboratorium". Decyzja szefa laboratorium (Vibe, 2026-11-14): **droga (a)**, uzupełniający re-run odziedziczonej baterii na finalnym kodzie K17f-v2 (hasz wiążący `f92f8152...`), bez zmian progów ani kryteriów. Uzasadnienie: tożsame z Asterionem i Copilotem; w tym łańcuchu wersji mamy już rozbieżności implementacyjne i haszowe, więc jedyny finalny hasz plus jedna kompletna bateria plus jawny PASS/FAIL per test to najprostszy epistemicznie łańcuch dowodowy; koszt jedna sesja. Zasady wykonania (Asterion): FAIL zapisujemy jako FAIL i rozliczamy osobno; nie naprawiamy protokołu w trakcie jego wykonywania.

### 4. Prerejestracja re-runu (runda 11at): zakres, kryteria, wartości oczekiwane

Wykonawca: driver rundy 11at (osadzający K17f-v2 przez import modułowy, bez modyfikacji pliku narzędzi; hasz drivera rejestrowany systemowym sha256sum przed testami, porządek B3: kod, hasze, testy). Wartości oczekiwane kanoniczne: log 11an + spec v0.9 §1.10 + nagłówek gammasRAB.txt; status per test: PASS wtedy i tylko wtedy, gdy wynik rzeczywisty równy wartości oczekiwanej; bez dziedziczenia statusów.

**Sanity SHA-256 (8 wektorów, implementacja TS w driverze):** „abc" → `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`; pusty → `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; „The quick brown fox jumps over the lazy dog" → `d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592`; 'a'×55 → `9f4390f8d30c2dd92ec9f095b65e2b9ae9b0a925a5258e241c9f1e910f734318`; 'a'×56 → `b35439a4ac6f0948b6d6f9e3c6af0f5f590ce20f1bde7090ef7970686ec6738a`; 'a'×63 → `7d3e74a05d7db15bce4ad9ec0658ea98e3f06eeecf16b4c6fff2da457ddc2f34`; 'a'×64 → `ffe054fe7ae0cb6dc65c3af9b61d5209f439851db43d0ba5997337df154668eb`; 'a'×65 → `635361c48bb9eab14198e76ea8ab7f1a41685d6ad62aa9146d301d4f17eb0ae0`. Kryterium: 8/8 dokładnych trafień (wartości potwierdzone też systemowym sha256sum w tej rundzie).

**Automat t1–t7 (§1.10 (7), przejścia):** t1: FAIL nieeskalowalny ⇒ STOP; t2: FAIL eskalowalny przy esc_used=0 ⇒ E2, esc_used:=1; t3: FAIL eskalowalny przy esc_used=1 ⇒ STOP; t4: E1 przy wszystkich flagach 0 ⇒ globalny rerun, wszystkie flagi:=1; t5: E1 po wcześniejszym E2 ⇒ brak E1, fallback 1.2(ii); t6: po E1 późniejszy FAIL eskalowalny ⇒ GLOBALNY STOP (C28); t7: E2 na A, potem FAIL eskalowalny na B przy esc_used[B]=0 ⇒ E2 na B (niezależność flag).

**S1–S4 (schurNin, moniczne przez skalowanie):** S1=(2μ−1)³, const-first [−1,6,−12,8] ⇒ PASS: nin=3, fail=false, γ (kolejność redukcji: od γ₃) = −1/8, 4/7, −10/11; S2=(μ²−1)(μ−1/2) ×2=[1,−2,−1,2] ⇒ FAIL: fail=true, γ₂=−1 singularne na stopniu 2; S3=(3μ−4)(2μ−1)²=[−4,19,−28,12] ⇒ nin=2, fail=false, γ₁=−65/61 exact, |γ₁|>1 flip; S4=(μ−1)²(μ−1/2) ×2=[−1,4,−5,2] ⇒ FAIL: fail=true dekretowany na kroku γ₂=1 na stopniu 2 (po pierwszej redukcji P₂=(z−1)²).

**(6a):** T_a ×12=[−2,15,−31,12] ⇒ 2; T_b ×4=[−6,29,−21,4] ⇒ 1; T_c ×60=[−1,12,−47,60] ⇒ 3; T_d=[−24,26,−9,1] ⇒ 0 (naiwne zliczanie dałoby 2).

**(6b):** T_e ×2=[2,−5,2] ⇒ FAIL (γ₂=1); T_f=[−1,0,1] ⇒ FAIL (γ₂=−1); T_g ×4=[−2,9,−12,4] ⇒ FAIL (γ₂=1, po redukcji P₂ = T_e).

**(6c) L_count(T_g):** (c=1/2, R=1/8) ⇒ 2; (1/2, 2) ⇒ 3; (1/2, 3/2) ⇒ FAIL (γ₁=−1 na stopniu 1, pierwiastek z=2 na brzegu dysku).

**(6d) na R_AB:** parse cRAB (A[m] = c_{23−m}·2^(320m), A[23]=2^7360) ⇒ tak; deflate(q) ⇒ reszta=0; schurNin(r) ⇒ nin=22, fail=false; L_count(r; 0, 283/1024) ⇒ 21; L_count(r; 9/16, 1/8) ⇒ 1; kompletność 21+1=22=deg r ⇒ tak; γ 22/22 EQUAL z gammasRAB.txt (mapowanie: gammas[i] z schurNin ↔ plikowa gamma_{22−i}; porównanie exact n₁·d₂ = n₂·d₁).

**4a (dkDouble na μ²³−2⁻²³, double const-first [−2⁻²³,0,...,0,1]):** stopped=true, iters=23 (wartość kontrolna 11an), pass40: maxErr<2⁻⁴⁰; referencyjnie maxErr ~5.0e−16 (11an).

**4b′ (ERRATA proceduralna, jawnie: errata zamiany 4b→4b′, legalna przed pierwszą kwalifikacją wg N6/N2(b); nie jest pierwotnym testem prerejestrowanym):** Q5 stopnia 8, pierwiastki (5±3i)/16, (−7±1i)/16, (9±5i)/16, (−1±9i)/16; współczynniki exact z iloczynu (z²−(5/8)z+17/128)(z²+(7/8)z+25/128)(z²−(9/8)z+53/128)(z²+(1/8)z+41/128); stopped=true, iters=11 (11an), pass40; referencyjnie maxErr ~1.39e−17 (11an/K2a).

### 5. Diagnostyka pre-run (jawna, Z2): wykryta rozbieżność w agregacji N_in w schurNin (v2)

**Motywacja:** przy ręcznej weryfikacji odczytu kodu (rachunek kontrolny S₃ przed napisaniem drivera) ślad na pieńku nie zgadzał się z kanonem 11an. Zamiast ignorować, wykonano diagnostykę pre-run i ją tu jawnie rejestruję. Diagnostyka NIE jest re-runem i nie zmienia prerejestracji: wartości oczekiwane sekcji 4 pozostają kanoniczne, a oficjalny re-run (11at) wykona się na finalnym kodzie wg sekcji 4, z zapisem FAIL jako FAIL.

**Metoda:** artefakt K17f-v2 uruchomiony w Node (--experimental-strip-types), import modułowy, plik niemodyfikowany; systemowy sha256sum przed uruchomieniem = `f92f8152...` (zgodny z haszem wiążącym 11ar).

**Wyniki diagnostyki (kanon 11an → wynik v2):**

| Test | Kanon 11an | Wynik v2 |
|---|---|---|
| (6a) T_a | 2 | **0** |
| (6a) T_b | 1 | 1 |
| (6a) T_c | 3 | 3 |
| (6a) T_d | 0 | **2** |
| S1 | nin=3, fail=false | nin=3, fail=false |
| S2 | fail=true (γ₂=−1) | fail=true (γ₂=−1) |
| S3 | nin=2, fail=false | **nin=0**, fail=false |
| S4 | fail=true (γ₂=1) | fail=true (γ₂=1) |
| (6b) T_e/T_f/T_g | FAIL (singularne) | FAIL (singularne) |
| (6c) (1/2, 1/8) | 2 | **0** |
| (6c) (1/2, 2) | 3 | 3 |
| (6c) (1/2, 3/2) | FAIL | FAIL |
| (6d) deflate(q) | reszta=0 | reszta=0 |
| (6d) schurNin(r) | nin=22, fail=false | nin=22, fail=false |
| (6d) γ vs gammasRAB | 22/22 EQUAL | 22/22 EQUAL |
| (6d) L_count(r; 0, 283/1024) | 21 | **0** |
| (6d) L_count(r; 9/16, 1/8) | 1 | **20** |
| 4a | 23 iter, STOP, maxErr ~5.0e−16 | 23 iter, STOP, maxErr 5.0037e−16, pass40 |
| 4b′ | 11 iter, STOP, maxErr ~1.39e−17 | 11 iter, STOP, maxErr 1.3878e−17, pass40 |

**Root cause (kontrola):** warstwa redukcji schurNin jest poprawna (sekwencje γ zgodne z referencją: 22/22 EQUAL; przypadki singularne wykrywane zgodnie z kanonem). Błąd jest w samej agregacji N_in: pętla agregacyjna iteruje gammy w kolejności push, czyli stopni malejąco (γ₃ od pierwszej redukcji), a formuła flip `nin = i − nin` jest poprawna wyłącznie przy iteracji od γ₁ w górę (wtedy indeks i = k−1). Kontrola: agregacja poprawiona (iteracja od γ₁, flip (k−1) − nin) na NIEZMIENIONYCH sekwencjach γ z v2 odtwarza wszystkie wartości kanoniczne: T_a=2, T_d=0, S3=2, (6c)(1/2,1/8)=2, L_count(r; 0, 283/1024)=21, L_count(r; 9/16, 1/8)=1, kompletność 22=22. Pogrubione wyniki v2 to dokładnie przypadki z flipem (|γ_k|>1); przypadki bez flipu i singularne są zgodne.

**Zasięg oddziaływania:** wyłącznie agregacja N_in przy flipach w schurNin. Warstwy niezależne (bgcd, composeDisk, deflate, dkDouble, dkDyadic, dyadic, bigToNumber, roucheExact, roucheExactBigInt, faddeev) nietknięte; wyniki re-kwalifikacji 11ar (BASE/E2 na q, ścieżki Perrona (a)/(b), N45, ρ̂) nie zależą od agregacji schurNin i pozostają w mocy. Dotknięte są natomiast odziedziczone wartości L_count z 11an, które wchodziły w kompletność K2c (21+1=22).

**Pytanie historyczne (rejestruję jako N47, do rozliczenia po 11at):** kanon 11an i nagłówek gammasRAB.txt (runda 11aq: „Sanity (6a)-(6c) na tej implementacji: T_a=2, T_b=1, T_c=3, T_d=0") nie są odtwarzalne przez obecny plik K17f-v2 w przypadkach flip. Możliwe wyjaśnienia: (i) przebudowa pliku w 11ar zmieniła pętlę agregacyjną mimo adnotacji „narzędzia exact bajtowo bez zmian w tej wersji"; (ii) wartości 11an/11aq liczył driver poza schurNin (agregacja po stronie drivera), a schurNin v2 nigdy nie był kontrolowany baterią (dokładnie luka S5). Do rozstrzygnięcia w rozliczeniu FAILy re-runu; wymaga porównania z plikiem K17f sprzed 11ar, jeśli dostępny w historii repo.

**Protokół bez zmian:** oficjalny re-run 11at wykonuję na finalnym kodzie v2 według prerejestracji sekcji 4. Przewidywane FAILy: (6a) T_a, T_d; S3; (6c) (1/2, 1/8); (6d) oba L_count + kompletność. Zostaną zapisane jako FAIL i rozliczone osobno (errata v3 agregacji + ponowna kwalifikacja zakresu dotkniętego + decyzja o.statusach dziedziczonych), decyzja po przeglądzie 11at przez recenzentów i Leszka. W trakcie re-runu żadnych poprawek kodu ani kryteriów.

### 6. E18b

Pozostaje HOLD (K6: populacja 361 nietknięta). Start wyłącznie po czystym przeglądzie 11as/11at i rozstrzygnięciu N47 oraz erraty agregacji. Runda 11at (wyniki re-runu per test, format Asteriona) następuje w tej samej sesji, po prerejestracji niniejszej rundy.

---

## Runda 11at. Re-run baterii S5 droga (a): wyniki per test (24 PASS / 7 FAIL)

**Data (UTC):** 2026-11-14T23:31:49Z (czas wykonania re-runu)
**Narzędzie:** K17f-v2, hasz wiążący `f92f8152c417d84baba400188c9027f449adc4f526587330f469c1e7d4d2e2e3` (potwierdzony w driverze przed testami, zgodny z 11ar/11as).
**Driver:** run-11at.ts, sha256 `2ca2055a8997e4faa982ffed2607f21dd390856ccebdb27fcd7812d100602d9c`, zarejestrowany systemowym sha256sum PRZED testami; driver weryfikuje w czasie wykonania zgodność własnego haszu (argv) i haszu artefaktu (B3: kod, hasze, testy — oba ZGODNY).
**Przebieg techniczny (jawny):** dwie wcześniejsze próby uruchomienia przerwane przez defekt serializacji BigInt po stronie drivera (hasze prób `1e036b3e...`, `cbf5b034...`); każda przerwana PRZED ukończeniem baterii; z tych prób nie rejestruje się wyników. Bateria jest deterministyczna, więc wyniki per test w próbach częściowych były identyczne z poniższymi. Oficjalny, kompletny przebieg: hasz `2ca2055a...`.

### 1. Wyniki per test (kryteria i wartości oczekiwane: prerejestracja 11as; bez dziedziczenia statusów)

| # | Test | Obiekt kontrolny | Kryterium | Oczek. | Rzecz. | Status |
|---|---|---|---|---|---|---|
| 1 | sanity SHA-256 | 8 wektorów §1.10 (1), potwierdzonych systemowym sha256sum | 8/8 dokładnych trafień (implementacja TS w driverze) | 8 | 8 | PASS |
| 2 | t1 | A; FAIL nieeskalowalny | przejście ⇒ STOP, flaga A=0 | STOP, A=0 | STOP, A=0 | PASS |
| 3 | t2 | A; FAIL eskalowalny, esc_used=0 | ⇒ E2, esc_used:=1 | E2, A=1 | E2, A=1 | PASS |
| 4 | t3 | A; FAIL eskalowalny, esc_used=1 | ⇒ STOP | STOP | STOP | PASS |
| 5 | t4 | A,B; E1 przy flagach 0 | globalny rerun, wszystkie flagi:=1 | RERUN_E1, A=1, B=1 | RERUN_E1, A=1, B=1 | PASS |
| 6 | t5 | A; E1 po wcześniejszym E2 | brak E1, fallback 1.2(ii) | FALLBACK_1.2(ii) | FALLBACK_1.2(ii) | PASS |
| 7 | t6 | A; po E1 FAIL eskalowalny | GLOBALNY STOP (C28) | GLOBAL_STOP | GLOBAL_STOP | PASS |
| 8 | t7 | A,B; E2 na A, potem FAIL eskalowalny na B | E2 na B (niezależność flag) | E2, B=1 | E2, B=1 | PASS |
| 9 | S1 | (2μ−1)³ [−1,6,−12,8] | nin=3, fail=false, γ = −1/8, 4/7, −10/11 | tak | nin=3, γ zgodne | PASS |
| 10 | S2 | [1,−2,−1,2] | fail=true, γ₂=−1 singularne | tak | tak | PASS |
| 11 | S3 | [−4,19,−28,12] | nin=2, fail=false, γ₁=−65/61 (flip) | nin=2 | **nin=0** (γ₁=−65/61 zgodne) | **FAIL** |
| 12 | S4 | [−1,4,−5,2] | fail=true dekretowane przy γ₂=1 (P₂=(z−1)²) | tak | tak | PASS |
| 13 | (6a) T_a | [−2,15,−31,12] | nin=2 | 2 | **0** | **FAIL** |
| 14 | (6a) T_b | [−6,29,−21,4] | nin=1 | 1 | 1 | PASS |
| 15 | (6a) T_c | [−1,12,−47,60] | nin=3 | 3 | 3 | PASS |
| 16 | (6a) T_d | [−24,26,−9,1] | nin=0 (naiwne 2) | 0 | **2** | **FAIL** |
| 17 | (6b) T_e | [2,−5,2] | FAIL (γ₂=1) | FAIL | FAIL | PASS |
| 18 | (6b) T_f | [−1,0,1] | FAIL (γ₂=−1) | FAIL | FAIL | PASS |
| 19 | (6b) T_g | [−2,9,−12,4] | FAIL (γ₂=1, P₂=T_e) | FAIL | FAIL | PASS |
| 20 | (6c) (1/2,1/8) | L_count(T_g) | 2 | 2 | **0** | **FAIL** |
| 21 | (6c) (1/2,2) | L_count(T_g) | 3 | 3 | 3 | PASS |
| 22 | (6c) (1/2,3/2) | L_count(T_g) | FAIL (γ₁=−1) | FAIL | FAIL | PASS |
| 23 | (6d) parse | cRAB.txt, A[m]=c₂₃₋ₘ·2^(320m) | A[23]=2^7360, 24 współczynników | tak | tak | PASS |
| 24 | (6d) deflate | q=(μ−1)r | reszta=0, deg r=22 | tak | tak | PASS |
| 25 | (6d) schurNin(r) | r | nin=22, fail=false | tak | tak | PASS |
| 26 | (6d) γ cross-check | gammasRAB.txt, gammas[i]↔gamma₂₂₋ᵢ | 22/22 EQUAL (exact n₁d₂=n₂d₁) | 22/22 | 22/22 | PASS |
| 27 | (6d) L_count(r;0,283/1024) | r | 21 | 21 | **0** | **FAIL** |
| 28 | (6d) L_count(r;9/16,1/8) | r | 1 | 1 | **20** | **FAIL** |
| 29 | (6d) kompletność | 21+1=22=deg r | 22 | 22 | **20** | **FAIL** |
| 30 | 4a | μ²³−2⁻²³, dkDouble | stopped=true, iters=23, pass40; ref maxErr ~5.0e−16 | tak | stopped, 23 iter, maxErr 5.0037e−16, maxStep 3.6303e−17 | PASS |
| 31 | 4b′ (ERRATA) | Q5 deg 8 (errata proceduralna 4b→4b′) | stopped=true, iters=11, pass40; ref maxErr ~1.39e−17 | tak | stopped, 11 iter, maxErr 1.3878e−17, maxStep 2.7689e−17 | PASS |

**Podsumowanie: 31 testów, PASS=24, FAIL=7.** FAILy to dokładnie przypadki przewidziane w diagnostyce pre-run 11as: wszystkie i wyłącznie przypadki z flipem (|γ_k|>1) w agregacji N_in schurNin v2 (S3, T_a, T_d, (6c)(1/2,1/8), oba L_count na r, kompletność). Żadnego FAILa poza przewidywanymi; żadnych poprawek kodu ani kryteriów w trakcie re-runu nie wykonano.

### 2. Kontrola root-cause (formalna, w driverze, oznaczona jako diagnostyka poza baterią)

Agregacja poprawiona (iteracja od γ₁ w górę, flip (k−1)−nin) na NIEZMIENIONYCH sekwencjach γ wyprodukowanych przez K17f-v2: T_a=2, T_d=0, S3=2, (6c)(1/2,1/8)=2, L_count(r;0,283/1024)=21, L_count(r;9/16,1/8)=1, kompletność 22=22. Formalnie potwierdza to diagnozę z 11as: warstwa redukcji (sekwencje γ) jest poprawna; błąd dotyczy wyłącznie pętli agregacyjnej (kolejność iteracji), a wartości kanoniczne 11an są matematycznie prawidłowe i odtwarzalne na γ z v2 po skorygowaniu samej agregacji.

### 3. Rozliczenie FAILów (propozycje do przeglądu; decyzja po recenzjach i u Leszka)

1. **Errata v3 (proponowana):** poprawa wyłącznie pętli agregacyjnej schurNin (iteracja od γ₁ w górę; flip (k−1)−nin), nowy hasz wiążący, ponowny re-run tej samej baterii (oczekiwany wynik 31/31 PASS); wg B4 zmiana narzędzia wymaga jawnej ponownej kwalifikacji zakresu dotkniętego, ale warstwa redukcji i wszystkie warstwy niezależne pozostają nietknięte. Nie wykonywana w tej rundzie (protokół: FAIL rozliczany osobno, po przeglądzie).
2. **Status wartości dziedziczonych z 11an:** wartości kanoniczne (T_a=2, T_d=0, L_count 21/1, kompletność 22) pozostają matematycznie prawidłowe (potwierdzone: spec §1.10, pierwiastki, γ z v2 plus poprawiona agregacja), ale twierdzenie łańcucha kwalifikacji „wartości te zostały wyprodukowane przez schurNin w wersji kwalifikowanej" jest dla przypadków flip nie do utrzymania na obecnym pliku v2. K2c (kompletność 21+1=22) wymaga po erracie v3 powtórzenia formalnego na artefakcie.
3. **N47 pozostaje otwarte:** kiedy wprowadzono błędną agregację (przebudowa pliku w 11ar mimo adnotacji „bajtowo bez zmian" vs agregacja po stronie drivera w 11an/11aq). Do rozstrzygnięcia porównaniem z plikiem K17f sprzed 11ar w historii repo; nie blokuje erraty v3.
4. **Zasięg potwierdzony formalnie:** wyniki re-kwalifikacji 11ar (BASE/E2 na q, Perron (a)/(b), N45, ρ̂) nie zależą od agregacji schurNin i pozostają w mocy; automat t1–t7, sanity SHA-256 i warstwa DK przechodzą na finalnym kodzie bez zastrzeżeń.

### 4. E18b

Pozostaje HOLD (K6: populacja 361 nietknięta). Warunki startu: przegląd 11as/11at przez recenzentów, errata v3 agregacji, ponowny re-run baterii z wynikiem 31/31 na nowym haszu, rozliczenie N47.

---

## Runda 11au. Przeglądy 11at; N47 rozstrzygnięte; N48 rejestrowane; errata v3 agregacji schurNin: spec, hasz, prerejestracja re-runu

**Data (UTC):** 2026-11-15T00:56Z
**Stan wyjściowy:** runda 11at (re-run baterii S5 droga (a): 31 testów, PASS=24, FAIL=7, wszystkie FAIL w agregacji N_in przy flipach |γ_k|>1) wypchnięta i zweryfikowana (commit cd6491a5). Przeglądy recenzentów odebrane (relay Leszka). Claude nadal w przerwie.

### 1. Rejestracja przeglądów 11at

**Asterion:** 11at przyjęty jako prawidłowy re-run (wyniki jawne, przypisane do haszu, próby nieoficjalne odróżnione od przebiegu). K2c: FAIL, bez podstaw do PASS. Diagnoza potwierdzona niezależnie rozkładem na pierwiastki: T_a=(z−2)(3z−1)(4z−1) ma N_in=2, T_d=(z−2)(z−3)(z−4) ma N_in=0, S₃=(3z−4)(2z−1)² ma N_in=2; wyniki v2 (0, 2, 0) błędne — nie spór o konwencję indeksowania. Errata v3: zakres zatwierdzony (wyłącznie agregacja) z wymaganiami: (a) zmiana wyłącznie pętli agregacyjnej schurNin; (b) jednoznaczny zapis matematyczny rekurencji, z mapowaniem indeks stopnia ↔ kolejność γ, nie samo „odwracamy pętlę”; (c) nowy plik, nowy pełny SHA-256, prerejestracja kryteriów przed testami; (d) ponowienie całej baterii 31 testów (nie tylko 7); (e) niezależne Z1 najlepiej innym algorytmem liczącym pierwiastki z wielomianu źródłowego, nie kolejną implementacją tej samej pętli na tych samych γ, szczególnie oba L_count dla R_AB. Nie zakłada z góry 31/31; nie przenosi potwierdzenia kompletności K2c na wyniki 11ar; N47 jako osobne zagadnienie historyczne. Wymaganie do raportu końcowego K2: jawne odnośniki do pierwotnego FAIL 4b, formalnego zatrzymania kwalifikacji i rejestracji erraty 4b′ (domknięcie N6). E18b HOLD, K6 bezwzględne. Obserwacja metodologiczna: to, że przeglądy 11ar nie wykryły defektu a re-run 11at tak, to argument za utrzymaniem niezależnych testów wykonawczych obok przeglądów strukturalnych.

**DeepSeek:** Z0 częściowe na treści logów (repo nieotwieralne dla niego; prosi o wklejkę 11as+11at przez Leszka do pełnego A1–F3). Merytorycznie: droga (a) właściwa, defekt realny. K2c wymaga formalnego powtórzenia na artefakcie (nie dziedziczenia), trzy powody: (i) Z0 — kwalifikowane musi być dokładnie to, co jest w artefakcie; kontrola root-cause kwalifikuje wyjaśnienie, nie artefakt; (ii) K17f wiąże hash z kodem dopiero po re-runie na finalnej wersji — inaczej nie wiadomo, co jest zamrożone; (iii) precedens N2 z 11m/11an: nie kodyfikować buga przez korektę do wyniku. Errata v3: zgoda z uwagą — jawna kolejność γ₁ w górę w treści erraty. N47 sklasyfikowane jako provenance chain break (wynik dobry, artefakt zły, wykrywalne tylko re-runem). Sugestia N48 (nowa): do K17f dodać krok „artefakt reprodukuje wyniki baterii z logu PRZED rejestracją hasza jako wiążącego”. Lekcja E40: przy PASS na artefakt numeryczny przegląd strukturalny musi jawnie zaznaczać, że nie weryfikuje zgodności implementacji ze specyfikacją. Rekomendacja: errata v3 → nowy artefakt → re-run 31 testów → nowy log → pełny A1–F3 po wklejce → dopiero E18b. Nie zgłasza STOP.

**Copilot:** 24/31 = FAIL kwalifikacji utrzymany. Root cause przekonująco wyizolowany (rekurencja od N(P₀)=0 w górę stopni; transformacja flip w przeciwnym kierunku nieodwracalna tym samym wzorem). T_d czysty świadek błędu niezależny od R_AB/DK/tolerancji. Zakres v3 zaakceptowany (minimalna zmiana); po zmianie wymagany pełny re-run 31 testów (zmiana wspólna funkcja). Prerejestracja bez zapisu „oczekiwane 31/31” jako kryterium naprawy: poprawiamy udowodniony defekt, po czym pytamy niezmienioną baterię (Z0). A3 pozostaje zamknięte (gałąź DK niezależna). Warunki domknięcia (5): nowy pełny hash przed testami; jawny diff zakresu; pełny re-run tych samych 31; per-test bez dziedziczenia; jakikolwiek FAIL ⇒ E18b HOLD. Po czystym pełnym re-runie na jednym nowym haszu: brak dalszych blokerów do 361.

**Kimi:** potwierdza stan, gotowość kontroli niezależnej (γ, symulacja poprawionej agregacji, analiza N47). Pytanie o priorytet — odpowiedź w sekcji 5 (Z1 niezależne) i relayu: priorytetem jest niezależne Z1 obu L_count na R_AB (wymaganie Asteriona), γ i N47 dodatkowo.

**Claude:** nadal przerwa; kolejka bez zmian.

### 2. N47 ROZSTRZYGNIĘTE (provenance; opcja (ii))

Dowody (dwa niezależne źródła dokumentacyjne + wynik 11at):

1. **K2-STAN.md (handoff do 11an/11aq):** „L_count: kompozycja afiniczna exact, potem Schur + ninUp” — agregacja N_in wykonywana przez OSOBNY moduł `ninUp` po stronie drivera; hasze narzędzi K2c-1 rejestrowane osobno per moduł („schurNin bb486f1d…, lcount 624a2dd2…”).
2. **Log 11aq (w repo), Lekcje 11aq (e):** „Agregacja N_in wyłącznie w górę (k = 1..n); agregacja w dół daje wartości bez sensu.”
3. **Wynik 11at:** artefakt K17f-v2 (f92f8152) faktycznie agreguje w dół — sprzecznie z lekcją (e).

**Wniosek:** wartości kanoniczne 11an/11aq (T_a=2, T_d=0, L_count 21/1, kompletność 22) były liczone z agregacją W GÓRĘ po stronie drivera (ninUp), więc są matematycznie poprawne — potwierdza to kontrola root-cause 11at (poprawiona agregacja na niezmienionych γ z v2 odtwarza cały kanon). Defekt wszedł przy składaniu K17f-v2 w rundzie 11aq: agregację złożono do schurNin w błędnym kierunku, wbrew własnej lekcji (e). Adnotacja 11ar „narzędzia exact bajtowo bez zmian” była prawdziwa względem 11aq, ale sam 11aq już zawierał defekt; żadna przebudowa w 11ar nie zmieniła agregacji. Pliki 4170ef58 (wersja 11aq) i bb486f1d (schurNin 11an) nieodtwarzalne z dostępnej historii (zastąpione); dokumentacja powyżej stanowi zapis dowodowy.

**Klasyfikacja (wg DeepSeeka):** provenance chain break — wynik dobry, artefakt kanoniczny zły; wykrywalny wyłącznie re-runem wykonawczym. To jest dokładnie luka S5, którą re-run 11at domknął. **N47 zamknięte jako rozliczone historycznie**; nie blokuje erraty v3.

### 3. N48 rejestrowane (do spec v1.1)

Wg sugestii DeepSeeka: do protokołu K17f (od v1.1) dodaje się obowiązkowy krok kwalifikacji: **artefakt musi odtworzyć wyniki baterii z logu PRZED rejestracją hasza jako wiążącego** (re-run pełnej baterii na artefakcie kandydackim, porównanie z wartościami z logu). Runda 11at wykonała ten krok dla 11an; od v1.1 krok formalny dla każdego K17f-x. Zarejestrowane do wdrożenia przy okazji następnej rewizji specyfikacji; nie zmienia wymagań bieżącej kwalifikacji (bieżąca runda wykonuje krok de facto).

### 4. Errata v3: plik, hasz wiążący, jawny diff, spec rekurencji

**Nowy plik:** `K17f-v3-narzedzia.ts` (repozytorium narzędzi K2). **SHA-256 (wiążący, policzony systemowo przy utworzeniu, PRZED testami):**

```
60504f95678221a8d56b26d4ef3cf80a9653d85c333849f78612045f4ed7da86
```

**Jawny diff względem f92f8152 (K17f-v2), pełny:**

1. Tytuł pliku (linia 1): „K17f-v2 (rundy 11aq → 11ar)” → „K17f-v3 (rundy 11aq → 11ar → 11au), sesje 2026-11-13/14/15”.
2. Nowy blok komentarza „ZMIANA 11au” (18 linii) po bloku ZMIANA 11ar: jawnie zapisana rekurencja (sekcja poniżej), opis defektu v2, świadkowie, rozstrzygnięcie N47, zakres zmiany.
3. Pętla agregacyjna schurNin (jedyna zmiana kodu wykonywalnego):
   - stara (v2): `for (let i = 0; i < gammas.length; i++) { const { n: gn, d: gd } = gammas[i]; ... if (cmp < 0) nin++; else if (cmp > 0) nin = i - nin; else { return { gammas, nin: -1, fail: true }; } }`
   - nowa (v3): `for (let idx = gammas.length - 1; idx >= 0; idx--) { const { n: gn, d: gd } = gammas[idx]; const k = gammas.length - idx; ... if (a2 < gd2) nin++; else if (a2 > gd2) nin = (k - 1) - nin; else { return { gammas, nin: -1, fail: true }; } }` (gd2 = |gd|; linia komentarza „agregacja W GORE od P_0 (errata v3): gammas[n-k] = gamma_k, iteracja idx = n-1..0”).

Wszystkie pozostałe bajty pliku bez zmian względem f92f8152: warstwa redukcji (sekwencje γ, push gammy przed checkem gc2), normalizacja gcd, wykrywanie singularności, arytmetyka BigInt, oraz moduły bgcd, composeDisk, deflate, dkDouble, dkDyadic, bigToNumber, roucheExact, roucheExactBigInt, faddeev, dyadic.

**Spec rekurencji (wymaganie Asteriona; zapis jawny i jednoznaczny):** dla wielomianu P stopnia n, sekwencji redukcji P_n → P_{n−1} → … → P₀ z gamma_k = γ redukcji ze stopnia k (P_k → P_{k−1}):

```
N_in(P_0) = 0
dla k = 1..n:
  |gamma_k| < 1  =>  N_in(P_k) = N_in(P_{k-1}) + 1
  |gamma_k| > 1  =>  N_in(P_k) = (k-1) - N_in(P_{k-1})
  |gamma_k| = 1  =>  FAIL (przypadek singularny)
```

Mapowanie na strukturę danych: pętla redukcji biegnie k = n..1 i pcha γ_n PIERWSZĄ, więc w tablicy `gammas` zachodzi `gammas[n-k] = gamma_k`; agregacja iteruje tablicę od końca (idx = n−1..0), ze stopniem k = n − idx. Przy tej iteracji indeks tablicy i stopień spełniają i = k−1, co jest warunkiem poprawności formuły flip (w v2 formuła `nin = i − nin` była aplikowana przy iteracji od idx=0, gdzie i = n−k, stąd defekt przy flipach).

**Kontrola wstępna świadków na v3 (jawna, wykonana przed prerejestracją; NIE JEST re-runem baterii i nie wpływa na wartości oczekiwane):** T_a=2, T_b=1, T_c=3, T_d=0; S₁: nin=3, fail=false; S₂: fail=true (γ₂=−1); S₃: nin=2, fail=false, γ₁=−65/61; S₄: fail=true (γ₂=1); (6c): (1/2,1/8)→2, (1/2,2)→3, (1/2,3/2)→FAIL (γ₁=−1); schurNin(r) na R_AB: nin=22, fail=false; L_count(r;0,283/1024)=21; L_count(r;9/16,1/8)=1. Pełny kanon 11an odtworzony przez artefakt v3. Zarejestrowane dla jawności (Z2); bateria 11av i tak liczy wszystkie te przypadki na nowo, per test, bez dziedziczenia.

### 5. Prerejestracja re-runu (runda 11av)

Zapis prerejestracyjny (wzorzec Copilota):

```
Zmiana dozwolona:
wyłącznie agregacja N_in w schurNin (wykonana w K17f-v3, hasz 60504f95...).

Bateria:
identyczne 31 przypadków z 11at, te same wartości oczekiwane
(kanon 11an, jak w prerejestracji 11as sekcja 4).

Kryteria:
identyczne jak w 11as/11at; status per test, bez dziedziczenia
PASS z wcześniejszych rund.

Jakikolwiek FAIL:
kwalifikacja FAIL, E18b pozostaje HOLD.
```

Jawnie: nie prerejestruje się „oczekiwane 31/31” jako kryterium naprawy (uwaga Copilota, Z0). Poprawiono udowodniony defekt; baterię pytanie, nie wynik.

**Wykonanie (B3):** driver run-11av.ts, import modułowy K17f-v3; hasz drivera rejestrowany systemowym sha256sum PRZED testami; w czasie wykonania driver weryfikuje zgodność haszu własnego pliku (argv) oraz haszu artefaktu (wewnętrznie, względem 60504f95…). Struktura baterii identyczna z 11at: sanity SHA-256 (8 wektorów), automat t1–t7, S₁–S₄, (6a)–(6c), (6d) na R_AB (parse cRAB, deflate, schurNin(r), γ cross-check 22/22, oba L_count, kompletność), 4a, 4b′ (ERRATA). Wartości oczekiwane: bez zmian względem 11as sekcja 4.

**Z1 niezależne (wymaganie Asteriona, wdriverze 11av, oznaczone jako kontrola niezależna, poza baterią):** liczenie pierwiastków w obu dyskach R_AB algorytmem INNYM niż pętla Schura–Cohna: (a) transformacja afiniczna r(z) → B₁/B₂ liczona niezależnie w driverze (własna ekspansja dwumianowa na BigInt, bez composeDisk z artefaktu); (b) pierwiastki B₁/B₂ metodą dkDyadic (Weierstrass/Durand–Kerner na dyadach 256-bit — inna ścieżka numeryczna niż Schur); (c) licznik |root|² < 1 dokładnie na dyadach (kwadratura i porównanie dyadyczne z artefaktu); (d) porównanie z L_count v3. Kryterium Z1: zgodność obu liczb (oczekiwane kanonicznie 21 i 1; kryterium formalne: zgodność dwoma niezależnymi ścieżkami, nie sama zgodność z kanonem). Świadkowie niskowymiarowi (T_a, T_d, S₃) mają ponadto pierwiastki znane jawnie (Asterion: 2, 0, 2).

### 6. Zapis do raportu końcowego K2 (wymaganie Asteriona §4, rejestracja zobowiązania)

Raport końcowy kwalifikacji K2 zawrze jawne odnośniki chronologiczne: pierwotny FAIL 4b (runda 11ap) → formalne zatrzymanie kwalifikacji → ścieżka awaryjna i rejestracja erraty 4b′ (zamiana legalna przed pierwszą kwalifikacją N6/N2(b)) → PASS 4b′ w 11at. Domkniecie sporu N6 bez powrotu do interpretowania chronologii. Zobowiązanie zarejestrowane; wykonanie przy raporcie końcowym.

### 7. E18b

Pozostaje HOLD (K6: populacja 361 par nietknięta). Warunki startu po 11av: pełny wynik baterii na v3 (per test, bez dziedziczenia), wynik Z1 niezależnego, przegląd 11au/11av przez recenzentów (w tym pełny A1–F3 DeepSeeka po wklejce logów 11as/11at/11au/11av przez Leszka). Dopiero wtedy decyzja o starcie E18b.

---
## Runda 11av. Re-run baterii 31 testów na K17f-v3 (hasz 60504f95): 31/31 PASS, Z1 niezależne zgodne; nowa kwalifikacja K2c na v3

**Data (UTC):** 2026-11-15T01:03:47.978Z (start przebiegu oficjalnego), 2026-11-15T01:03:54.090Z (koniec)
**Stan wyjściowy:** runda 11au (commit 954fa40a, md5 01b326df617e987fc86ab88ffd4bb4c5): przeglądy 11at zarejestrowane, N47 rozstrzygnięte, N48 rejestrowane, errata v3 z jawnym diffem i rekurencją, prerejestracja re-runu wg wzorca Copilota. Bateria i kryteria identyczne z 11at (kanon 11an, prerejestracja 11as sekcja 4). Zmiana dozwolona: wyłącznie agregacja N_in w schurNin (wykonana w v3, hasz 60504f95678221a8d56b26d4ef3cf80a9653d85c333849f78612045f4ed7da86). Bez zapisu „oczekiwane 31/31” jako kryterium naprawy.

### 1. Status formalny

**K2c: nowa kwalifikacja na K17f-v3 PASS — 31 testów, PASS=31, FAIL=0, per test, bez dziedziczenia.** Runda 11at (24 PASS / 7 FAIL na v2) pozostaje w historii bez zmian; wyniki 11ar niezależne od schurNin zachowują swój status. Warunek prerejestracji 11au spełniony co do litera: jakikolwiek FAIL oznaczałby kwalifikację FAIL i E18b HOLD — nie wystąpił.

### 2. Jawna rejestracja prób drivera (B3; żadna próba poza oficjalną nie jest podstawą kwalifikacji)

Driver run-11av.ts ewoluował podczas uruchomień; artefakt K17f-v3 (60504f95…) był we wszystkich próbach nietknięty (import modułowy, weryfikacja haszu przy każdym uruchomieniu).

1. **Próba 1, hasz drivera 159fc2a3…**: przerwana przez własny check B3 PRZED baterią. Przyczyna: bug implementacji SHA-256 w driverze (kolejność słów 64-bitowej długości w paddingu: LOW na bajtach 56–59 zamiast HIGH; wektor pusty przechodził, bo length=0). Poprawka: hi na total−8, lo na total−4. Defekt harnessu, nie artefaktu.
2. **Próba 2, hasz drivera 2899e610…**: kompletna, 29 PASS / 2 FAIL. Oba FAIL (T_e, T_f) to defekt ODCZYTU γ₂ w driverze dla obiektów stopnia 2: odczyt gammas[1], podczas gdy γ singularne jest OSTATNIM wypchniętym elementem (schurNin przerywa pętlę zaraz po push przy gc2===0). Wyniki samego schurNin poprawne; Z1 dysk 2 bez formalnego stopu przy kanonicznym limicie 200.
3. **Próba 3, hasz drivera 5cae1c05…**: kompletna, 26 PASS / 5 FAIL. Błędna „poprawka” indeksu (gammas[len−2]) zepsuła S2/S4/T_g (singularne γ = ostatni element). Potwierdzenie semantyki: wyniki matematyczne schurNin identyczne z próbą 2 (determinizm).
4. **Próba 4, hasz drivera 9f02a462b1867df96ff55fe2761e3b8a6e1910d910e9f327a1ed2058a3e17274 = PRZEBIEG OFICJALNY**: odczyt γ z ostatniego elementu gammas; limit iteracji kontroli Z1 podniesiony do 1000 (parametr harnessu kontroli niezależnej; kanoniczny limit 200 dkDyadic w artefakcie bez zmian); dodany margines klasyfikacji Z1. 31/31 PASS + Z1 zgodne. Ten przebieg jest podstawą statusu w sekcji 1.

We wszystkich pełnych próbach (2–4) wyniki matematyczne artefaktu (schurNin, composeDisk, deflate, DK) były identyczne; FAILy prób 2–3 to wyłącznie defekty harnessu (odczyt γ do raportu), nie artefaktu. Kontrola wstępna świadków v3 (11au sekcja 5) nie była re-runem i nie wpływa na powyższe statusy.

### 3. Przebieg oficjalny (B3 zachowane)

- Driver: run-11av.ts, sha256 9f02a462b1867df96ff55fe2761e3b8a6e1910d910e9f327a1ed2058a3e17274 (systemowy sha256sum PRZED testami; zgodność argv weryfikowana wewnętrznie przed baterią).
- Artefakt: K17f-v3-narzedzia.ts, sha256 60504f95678221a8d56b26d4ef3cf80a9653d85c333849f78612045f4ed7da86 (weryfikowany wewnętrznie przy każdym uruchomieniu).
- Artefakty wejściowe: cRAB.txt sha256 b15812f1e8008700b531c7e5f13fe174d9b9768181d22094f7a462d1545f7040; gammasRAB.txt sha256 a1688893677ef3cff2936400cc390d1cb03482e87e0ffbce99c3c279b34eb4ca (weryfikowane przed testami).
- Bateria: identyczne 31 przypadków z 11at; wartości oczekiwane bez zmian (kanon 11an, 11as sekcja 4); status per test, bez dziedziczenia.

### 4. Wyniki per test

| # | Test | Obiekt kontrolny | Kryterium | Oczek. | Rzecz. | Status |
|---|---|---|---|---|---|---|
| 1 | sanity SHA-256 | 8 wektorów par. 1.10 (1) (TS w driverze; systemowy sha256sum potwierdza wektory) | 8/8 trafień | 8/8 | 8/8 | PASS |
| 2 | t1 | A; FAIL nieeskalowalny | STOP, flaga A bez zmian | STOP,A=0 | STOP,A=0 | PASS |
| 3 | t2 | A; FAIL eskalowalny, esc_used=0 | E2, esc_used:=1 | E2,A=1 | E2,A=1 | PASS |
| 4 | t3 | A; FAIL eskalowalny, esc_used=1 | STOP | STOP | STOP | PASS |
| 5 | t4 | A,B; E1 przy flagach 0 | globalny rerun, wszystkie flagi:=1 | RERUN_E1,A=1,B=1 | RERUN_E1,A=1,B=1 | PASS |
| 6 | t5 | A; E1 po wcześniejszym E2 | brak E1, fallback 1.2(ii) | FALLBACK_1.2(ii) | FALLBACK_1.2(ii) | PASS |
| 7 | t6 | A; po E1 FAIL eskalowalny | GLOBALNY STOP (C28) | GLOBAL_STOP | GLOBAL_STOP | PASS |
| 8 | t7 | A,B; E2 na A, potem FAIL eskalowalny na B | E2 na B (niezależność flag) | E2,B=1 | E2,B=1 | PASS |
| 9 | S1 | (2μ−1)³ [−1,6,−12,8] | nin=3, fail=false, γ(push)=[−1/8,4/7,−10/11] | nin=3, γ(push)=[−1/8,4/7,−10/11] | nin=3, fail=false, γ(push)=[−1/8,4/7,−10/11] | PASS |
| 10 | S2 | (μ²−1)(μ−1/2)×2 [1,−2,−1,2] | fail=true, γ₂=−1/1 (singularne) | fail=true, γ₂=−1/1 | fail=true, γ₂=−1/1 | PASS |
| 11 | S3 | (3μ−4)(2μ−1)² [−4,19,−28,12] | nin=2, fail=false, γ₁=−65/61 (flip) | nin=2, fail=false, γ₁=−65/61 | nin=2, fail=false, γ₁=−65/61 | PASS |
| 12 | S4 | (μ−1)²(μ−1/2)×2 [−1,4,−5,2] | fail=true dekretowane przy γ₂=1/1 (P₂=(z−1)²) | fail=true, γ₂=1/1 | fail=true, γ₂=1/1 | PASS |
| 13 | (6a) T_a | [−2,15,−31,12] | nin=2 | nin=2, fail=false | nin=2, fail=false | PASS |
| 14 | (6a) T_b | [−6,29,−21,4] | nin=1 | nin=1, fail=false | nin=1, fail=false | PASS |
| 15 | (6a) T_c | [−1,12,−47,60] | nin=3 | nin=3, fail=false | nin=3, fail=false | PASS |
| 16 | (6a) T_d | [−24,26,−9,1] | nin=0 (naiwne 2) | nin=0, fail=false | nin=0, fail=false | PASS |
| 17 | (6b) T_e | [2,−5,2] | FAIL (γ₂=1/1) | fail=true, γ₂=1/1 | fail=true, γ₂=1/1 | PASS |
| 18 | (6b) T_f | [−1,0,1] | FAIL (γ₂=−1/1) | fail=true, γ₂=−1/1 | fail=true, γ₂=−1/1 | PASS |
| 19 | (6b) T_g | [−2,9,−12,4] | FAIL (γ₂=1/1, P₂=T_e) | fail=true, γ₂=1/1 | fail=true, γ₂=1/1 | PASS |
| 20 | (6c) L_count(T_g; 1/2, 1/8) | T_g, dysk (1/2,1/8) | 2 | nin=2, fail=false | nin=2, fail=false | PASS |
| 21 | (6c) L_count(T_g; 1/2, 2) | T_g, dysk (1/2,2) | 3 | nin=3, fail=false | nin=3, fail=false | PASS |
| 22 | (6c) L_count(T_g; 1/2, 3/2) | T_g, dysk (1/2,3/2) | FAIL (γ₁=−1/1 na stopniu 1) | fail=true, γ₁=−1/1 | fail=true, γ₁=−1/1 | PASS |
| 23 | (6d) parse | cRAB.txt: A[m]=c₂₃₋ₘ·2^(320m) | A[23]=2^7360, 24 współczynników, c₀=1 | n=24, c0=1, A23=2^7360:true, A0=c23:true | n=24, c0=1, A23=2^7360:true, A0=c23:true | PASS |
| 24 | (6d) deflate | q=(μ−1)r | reszta=0, deg r=22 | reszta=0:true, deg_r=22:true | reszta=0:true, deg_r=22:true | PASS |
| 25 | (6d) schurNin(r) | r (unscaled, stopień 22) | nin=22, fail=false | nin=22, fail=false | nin=22, fail=false | PASS |
| 26 | (6d) γ cross-check | gammasRAB.txt; gammas[i] ↔ γ₂₂₋ᵢ | 22/22 EQUAL (exact n1·d2=n2·d1) | 22/22 | 22/22 | PASS |
| 27 | (6d) L_count(r; 0, 283/1024) | r, dysk (0,283/1024) [r_in] | 21 | nin=21, fail=false | nin=21, fail=false | PASS |
| 28 | (6d) L_count(r; 9/16, 1/8) | r, dysk (9/16,1/8) [klaster subdominanty] | 1 | nin=1, fail=false | nin=1, fail=false | PASS |
| 29 | (6d) kompletność | n_in + count(C) = deg r | 21+1=22=deg r | 21+1=22, deg_r=22 | 21+1=22, deg_r=22 | PASS |
| 30 | 4a | μ²³−2⁻²³ (dkDouble, init 1.6) | stopped=true, iters=23, pass40 (maxErr<2⁻⁴⁰) | stopped=true, iters=23, pass40=true | stopped=true, iters=23, maxErr=5.0037e−16, pass40=true | PASS |
| 31 | 4b′ (ERRATA) | Q5 deg 8 (errata proceduralna 4b→4b′) | stopped=true, iters=11, pass40 | stopped=true, iters=11, pass40=true | stopped=true, iters=11, maxErr=1.3878e−17, pass40=true | PASS |

**Podsumowanie baterii: 31 testów, PASS=31, FAIL=0.**

### 5. Z1 niezależne (wymaganie Asteriona, poza baterią; kryterium: zgodność liczb dwiema niezależnymi ścieżkami)

Metoda (bez agregacji γ, bez schurNin): własna ekspansja dwumianowa BigInt w driverze (nie composeDisk) → dkDyadic (Weierstrass/Durand–Kerner na dyadach 256-bit) → licznik |w|²<1 exact na dyadach (sq2/gtSq) → porównanie z L_count v3 (Schur–Cohn).

- **Dysk 1 (c=0, R=283/1024):** transform niezależny === composeDisk: true; dkDyadic stopped=true, iters=167, maxStep²=4.25e−32; liczba |w|<1 = **21**; L_count v3 = 21; zgodność: true; margines klasyfikacji min||w|²−1| = 8.2995e−1.
- **Dysk 2 (c=9/16, R=1/8):** transform niezależny === composeDisk: true; dkDyadic stopped=false przy limicie kontroli Z1 1000, maxStep²=1.28e−10; liczba |w|<1 = **1**; L_count v3 = 1; zgodność: true; margines klasyfikacji min||w|²−1| = 9.9605e−1. Jeden pierwiastek wewnątrz: |w|² = 3.952e−3; 21 zewnętrznych: |w|² ∈ [12.87, 20.50].

**Wynik Z1: ZGODNE (obie liczby, oba dyski).** Kryterium Z1 (zgodność liczby pierwiastków między niezależną ścieżką DK a L_count v3) spełnione w całości.

**Jawna kwalifikacja ograniczenia formalnego dysku 2 (nie ukrywam):** dkDyadic NIE osiąga formalnego stopu 2⁻¹⁰⁴ (w kroku²) na dysku 2 w limicie kontroli. Przyczyna fizyczna: po transformacji dysku (9/16, 1/8) klaster ~17 drobnych pierwiastków źródłowych mapuje się do w≈−4.5 z separacjami rzędu 2⁻¹⁴·8 i mniejszymi; DK zbiega tam wolno. Diagnostyka uzupełniająca (poza przebiegiem oficjalnym, skrypt diag-z1d2.ts, sha256 db1438810fdbc7e180ce4d482fc77f525731f045e3939bf9af7b6c7c650eb3fd, artefakt bez zmian): limity 2000/5000/10000/20000 dają stopped=false przy podłodze maxStep² ∈ [1.1e−11, 8.6e−11] (niemonotoniczna, bez dalszej systematycznej poprawy), ale count_in=1 i margines 9.9605e−1 NIEZMIENNE przy każdym limicie. Klasyfikacja jest więc odporna na stan zbieżności: każdy punkt iteracyjny leży w |w|² odległym od 1 o co najmniej 0.996, a pojedynczy krok ≤ ~1e−5; zmiana przynależności IN/OUT jest wykluczona z marginesem >2 rzędów wielkości. Liczba 1 jest stabilna, nie „słodka”. Kryterium Z1 (zgodność liczb) nie wymagało formalnego stopu DK; ograniczenie rejestruję jawnie, decyzja o wystarczalności należy do recenzentów.

### 6. N47, N48, N6, A3

- **N47:** zamknięte w 11au (provenance chain break: agregacja w erze 11an po stronie drivera jako ninUp, przy składaniu K17f-v2 w 11aq zwinięta do schurNin w złym kierunku; odesłanie do 11au sekcja 2). Runda 11av nie zmienia tej analizy; potwierdza ją (v3 z agregacją w górę odtwarza kanon w całości).
- **N48:** zarejestrowane w 11au do spec v1.1 (krok „artefakt reprodukuje wyniki baterii logu PRZED rejestracją hasza jako wiążącego”). Runda 11av jest pierwszą realizacją tej praktyki: pełna bateria na finalnym artefakcie przed uznaniem hasza za wiążący dla K2c.
- **N6 / 4b→4b′:** zobowiązanie do raportu końcowego zarejestrowane w 11au sekcja 6; bez zmian.
- **A3 (gałąź DK):** bez zmian, zamknięte (11ar/11at); testy DK objęte niniejszą baterią (4a, 4b′) PASS na v3.

### 7. E18b

Pozostaje **HOLD** (K6: populacja 361 par nietknięta). Warunki startu (11au sekcja 7): czysty przegląd 11au/11av przez recenzentów, w tym pełne A1–F3 DeepSeeka po wklejce logów 11as/11at/11au/11av przez Leszka; dopiero wtedy decyzja o starcie E18b.

---
## Runda 11aw. Przegląd Claude'a (powrót z przerwy): niezależne potwierdzenie root cause i wszystkich 5 wartości z 11at; propozycje do baterii zarejestrowane do spec v1.1; stan K2 po 11au/11av bez zmian

**Data (UTC):** 2026-11-15T01:20Z
**Stan wyjściowy:** runda 11av (commit 800ecc70): errata v3 (K17f-v3, hasz 60504f95) wykonana, pełny re-run baterii 31 testów PASS=31/FAIL=0 bez dziedziczenia, Z1 niezależne zgodne (21/21, 1/1), K2c nowa kwalifikacja na v3. Claude pisał swój przegląd względem stanu po 11at (przed 11au/11av), z uwzględnieniem propozycji erraty v3.

### 1. Rejestracja przeglądu Claude'a

**Claude (Z1 na T_d i agregacji N_in):** zgadza się z diagnozą root cause, potwierdza ją niezależnie, odtwarzając wszystkie 5 błędnych wartości z 11at. K6 zachowane (tylko obiekty kontrolne i toy-wielomiany). T_d=(z−2)(z−3)(z−4): sekwencja γ z redukcji (kolejność produkcji, γ₃ pierwszy): −24, 38/115, −41/51; agregacja od γ₁ w górę daje N_in=0 ✓ (wszystkie trzy pierwiastki poza dyskiem jednostkowym), K17f-v2 dawał 2. Odtworzenie błędu na niezmienionych γ: błędna kolejność (od γ_n) reprodukuje dokładnie wszystkie 5 wartości FAIL z 11at (T_a 0, T_d 2, S₃ 0, L 0, L 20), a przypadki bez flipa (T_b, T_c) zgodne w obu wersjach. Wniosek: wzór flip (k−1)−nin poprawny tylko, gdy k oznacza stopień od P₁ w górę. Zakres erraty v3 właściwy (wyłącznie pętla agregacji). Dwie propozycje do baterii po erracie, bez zmiany progów: (1) przypadek z dwoma niesąsiednimi flipami (obecne toy-przypadki mają ≤1 flip, słabo testują propagację przy wielu zmianach); (2) losowa kontrola krzyżowa na wielomianach toy względem prawdziwej liczby pierwiastków znanej z konstrukcji. Jego implementacja lematu: 620 losowych wielomianów (341 o pierwiastkach rzeczywistych, 279 z parami zespolonymi), 100% zgodność z prawdziwą liczbą. E2 z 11ar: jego DK 256-bit (Gauss–Seidel, init 1.6, stop 2⁻⁵²) zbiega w 193 iteracjach (R_AB) i 186 (cut) wobec naszych 191/184; największe moduły 0.554641699189468 i 0.550107704833697 zgodne; różnica dwóch iteracji mieści się w zaokrągleniach, ale margines względem limitu 200 wąski (ok. 3–7%). Kompletność K2c: 21+1=22 nie może zachować statusu przez kontrolę root-cause, bo L_count jest przedmiotem defektu; formalne powtórzenie na artefakcie po erracie konieczne, nie opcjonalne. Kolejka: pusta do erraty v3 i ponownego re-runu.

### 2. Weryfikacja danych Claude'a na artefakcie v3 (kontrola warsztatu, przed rejestracją)

Sekwencja γ dla T_d z K17f-v3 (kolejność push): −24/1, 38/115, −41/51 — identyczna z podaną przez Claude (co do ułamka). schurNin(T_d) na v3: nin=0, fail=false ✓. Analogicznie T_a: γ = [−1/6, 59/70, −57/43], nin=2 ✓; S₃: γ = [−1/3, 29/32, −65/61], nin=2 ✓ (γ₁=−65/61, zgodne z tabelą 11av). Dane wejściowe przeglądu potwierdzone na kanonicznym artefakcie.

### 3. Rozliczenie: warunki formalne Claude'a spełnione przez 11au/11av

- Errata v3: wykonana (11au sekcja 4), zakres dokładnie zatwierdzany przez Claude (wyłącznie pętla agregacyjna, warstwa redukcji nietknięta), jawny diff, nowy hasz 60504f95, spec rekurencji jednoznaczny z mapowaniem indeksów.
- Formalne powtórzenie na artefakcie: wykonane (11av): pełna bateria 31 przypadków, identycznych z 11at, PASS=31/FAIL=0, per test, bez dziedziczenia; 11at pozostaje w historii jako 24/7. To jest dokładnie droga, którą Claude wskazał jako konieczną dla kompletności K2c.
- Stanowisko o kompletności (21+1=22 nie może być ratowane kontrolą root-cause): tożsame z rozstrzygnięciem DeepSeeka i wykonaniem 11av; spójne z całym łańcuchem.

### 4. Propozycje (1) i (2): rejestracja do spec v1.1, poza bieżącą kwalifikacją

Obie propozycje zarejestrowane jako kandydaci do baterii K17f od spec v1.1 (wraz z N48 z 11au sekcja 3):

1. **Toy-przypadek z dwoma niesąsiednimi flipami.** Uzasadnienie Claude (słaba pokrycie propagacji (k−1)−nin przy wielu zmianach) przyjmuję z uzupełnieniem: bateria 11av testuje propagację wielu flipów na obiekcie rzeczywistym ((6d): dysk (0,283/1024) daje 21/22, dysk (9/16,1/8) daje 1/22, czyli sekwencje z wieloma flipami), ale jawnego toy-świadka z rozdzielczymi flipami nie ma; kandydat do v1.1.
2. **Kontrola krzyżowa na losowych wielomianach.** Wynik Claude (620 wielomianów, 341 rzeczywiste + 279 zespolone, 100% zgodność z liczbą z konstrukcji) rejestruję jako niezależne potwierdzenie poprawności rekurencji v3 poza baterią (droga odrębna od root-cause Vibe, rozkładów Asteriona i Z1 przez DK). Do baterii kwalifikacyjnej wchodzi wyłącznie wariant deterministyczny (seeded, wartości oczekiwane z konstrukcji, zapisane jawnie): kwalifikacja nie może zależeć od generatora losowego w czasie wykonania (Z2, determinizm baterii).

**Jawna decyzja szefa lab.:** propozycje NIE wchodzą do bieżącej kwalifikacji K2c. Bateria 11av była zamrożona prerejestracją 11au („identyczne 31 przypadków z 11at"); rozszerzenie baterii po uzyskaniu PASS byłoby złamaniem prerejestracji i Z0 (zmiana pytania po poznaniu odpowiedzi). Domknięcie bieżącej kwalifikacji: status z 11av.

### 5. E2 z 11ar: rozbieżność iteracji zarejestrowana

Claude: 193/186 iteracji (R_AB/cut) wobec 191/184 z 11ar; moduły ρ̂ zgodne co do pełnej precyzji (0.554641699189468, 0.550107704833697); różnica dwóch iteracji spójna z różnicami zaokrągleń niezależnych implementacji. Rejestruję jako niezależne potwierdzenie E2 (trzecia implementacja DK po Vibe i kanonie 11an/11ar). Obserwacja o wąskim marginesie do limitu 200 (ok. 3–7%): przyjmuję; przy prerejestracji E18b cap iteracji DK będzie jawnym parametrem harnessu (analogicznie do limitu kontroli Z1 w 11av: parametr drivera, artefakt i jego kanoniczny limit bez zmian), z marginesem uwzględniającym rozrzut implementacji (proponowany cap ≥ 400 dla rachunku 361, decyzja przy prerejestracji E18b).

### 6. Kolejka Claude'a

Zgodnie z jego deklaracją („pusta do erraty v3 i ponownego re-runu"): oba warunki spełnione, kolejka otwarta. Zadanie: przegląd 11au/11av (rejestracja przeglądów i rozliczenie: errata v3, re-run 31/31, Z1 z jawnym ograniczeniem formalnym dysku 2); opcjonalnie cenne: Z1 trzecią drogą (argument zasady argumentu/Sturm na wielomianu źródłowym po transformacji obu dysków), domykające komplet niezależnych dróg do liczb 21 i 1.

### 7. E18b

Bez zmian: **HOLD** do czystego przeglądu 11au/11av przez wszystkich recenzentów (w tym pełny A1–F3 DeepSeeka po wklejce logów przez Leszka). K6: populacja 361 par nietknięta.

---
## Runda 11ax. Przeglądy 11au/11av/11aw: DeepSeek recheck warunkowy (formuła errata v3 zweryfikowana matematycznie), Asterion przyjmuje kwalifikację i żąda trzeciej drogi Z1 dla dysku 2, Copilot 5/5 PASS z warunkiem literalnego cap=200, Kimi: trzy niezależne drogi Z1 zgodne 21/1 (ogłoszenie; raport formalny zamówiony)

**Data (UTC):** 2026-11-15T02:10Z
**Stan wyjściowy:** runda 11aw (commity 7be03f1b + 8dc8eca4): przegląd Claude'a rozliczony, propozycje do spec v1.1, kolejka Claude: przegląd 11au/11av. Claude ponownie w przerwie. Recenzenci otrzymali streszczenia 11au/11av/11aw (DeepSeek: Z0 jawne, treści logów nie widzi; pełny A1–F3 wymaga wklejki).

### 1. Rejestracja przeglądu DeepSeeka (recheck strukturalny, warunkowy)

**DeepSeek:** N47 potwierdzone (evidence chain: K2-STAN „Schur + ninUp", osobne hasze modułów, lekcja (e) logu 11aq; klasyczny provenance break — kod produkujący liczby poprawny, artefakt złożony z modułów nie odtwarzał kanonu). **Formuła erraty v3 zweryfikowana matematycznie (na papierze, Rouché):** gałąź |γ_k|<1 przez P_k − γ_k·P_k* = z·(1−γ_k²)·P_{k−1} i Rouché na okręgu jednostkowym (|γ_k·P_k*| < |P_k|) ⇒ N(P_k)=N(P_{k−1})+1 ✓; gałąź |γ_k|>1 przez P_k*(z)=z^k·P_k(1/z), N(P_k*)=k−N(P_k) i Rouché ⇒ N(P_k)=(k−1)−N(P_{k−1}) ✓. Mapowanie gammas[n−k]=γ_k poprawne. K2c re-qualification dokładnie wg jego żądania (re-run, nie dziedziczenie; „reprodukcja, nie wyjaśnienie"). Z1 dysk 2: **wystarczające, i to w mocniejszym sensie niż formalny stop z ciasnym marginesem** (margines 0.996 w |w|² ⇒ każdy pierwiastek |w| ≤ 0.063 albo |w| ≥ 1.413; klasyfikacja nie zależy od miejsca zatrzymania DK; stabilność liczby przy limitach 1000–20000 potwierdzona; formalny stop byłby warunkiem wystarczającym, nie koniecznym; kontrast: formalny stop przy pierwiastkach |w|≈1±ε byłby gorszy). E2: różnica 193/186 vs 191/184 (~1%) = różne implementacje, nie rozrzut warty uwagi. Cap ≥ 400: zgoda, sugestia 500 (drobna, nie blokuje). Propozycje Claude: odroczenie do v1.1 zgodne z K8; **uwaga przyjęta: przy v1.1 rozszerzona bateria musi być testowana od zera na nowym K17f, nie „dodane testy na istniejącym artefakcie"** (zapobieganie powtórce klasy provenance break). Sugestia: jawny zapis stabilności count_in przy limitach (sekcja 5d). Pełny A1–F3: ⏸ wymaga wklejki logów (Leszek); formalnie nie może autoryzować E18b bez treści logów, ale nic w streszczeniu nie budzi zastrzeżeń. Nie zgłasza STOP. Trzecia konstatacja metodologiczna: re-run wykrywa to, czego analiza strukturalna nie może (trzeci raz w projekcie).

### 2. Rejestracja przeglądu Asteriona

**Asterion:** Errata v3 przyjęta (właściwy zakres, jawna rekurencja, nowy hasz, pełna bateria bez dziedziczenia; docenia brak „ratowania" 7 FAIL przez samą diagnostykę). K2c 31/31 = mocny wynik kwalifikacyjny, przyjęty. N47: wyjaśnienie przyczynowe przyjęte jako wiarygodne, z jawnym zastrzeżeniem audytowym: wyjaśnienie pochodzenia błędu ≠ niezależny dowód wszystkich historycznych wykonań (zasada słuszna; historyczne pochodzenie kodu pozostaje osobnym śladem audytowym, nie blokerem). **Z1 dysk 1: przyjęte (21, formalny stop 167 iteracji). Z1 dysk 2: NIE przyznaje jeszcze pełnego PASS** — rozróżnienie kluczowe: stabilność wyniku numerycznego przy zwiększaniu limitu ≠ certyfikat, że wszystkie pierwiastki zostały znalezione z właściwą krotnością; duży margines od okręgu nie wyklucza pominięcia lub powielenia pierwiastka (szczególnie przy klastrze ~17). Żądanie: **trzecia droga dla dysku 2: argument zasady argumentu albo certyfikowany Sturm po transformacji dysku; nie kolejny wariant DK.** E18b HOLD do domknięcia. Uwaga własna Asteriona: publiczny podgląd repo pokazuje starszy zrzut (rund 11au–11aw nie widzi); werdykt = recheck przekazanego relayu, nie samodzielne odtworzenie artefaktów. Kolejność: Kimi certyfikat dysku 2 → DeepSeek A1–F3 na pełnych logach → dopiero E18b.

### 3. Rejestracja przeglądu Copilota

**Copilot:** Pięć warunków z 11at: 5/5 PASS (nowy artefakt+hasz; minimalny jawny zakres z poprawną rekurencją, nie „reverse array"; pełna bateria 31 ponowiona; per-test bez dziedziczenia, 11at zachowane jako historia; brak FAIL). K2c: PASS. Defekt schurNin: ZAMKNIĘTY. T_d najczystszy świadek (konstrukcyjnie 0; v2 dawał 2; γ niezmienione). N47: rozliczone przekonująco. Z1 21/1: **akceptowane jako wartościowa niezależna kontrola pomocnicza, z jawnym ograniczeniem DK (nie formalny certyfikat zbieżności DK)**; nie wymaga kolejnej drogi Z1 jako warunku E18b, bo normatywny certyfikat kompletności szedł exact drogą baterii. Zmiany drivera (padding SHA-256, indeks γ): jawne próby, re-hash, bateria od początku, finalne 31 z jednej wersji — właściwie. **Jedyny punkt odrzucony: cap ≥ 400 w v1.0.** Zamrożona procedura v1.0 ustanowiła cap=200 i cała semantyka A3 (brak stopu po 200 ⇒ FAIL ⇒ E2 ⇒ po drugim braku stopu GLOBALNY STOP) jest na tym zbudowana; podwyższenie cap po zobaczeniu, że niezależne implementacje potrzebują 184/191/193, byłoby zmianą reguły na podstawie danych z kwalifikacji. Przebiegi >200: wyłącznie diagnostycznie po zadekretowanym FAIL, bez wpływu na status normatywny. Werdykt: **BRAK BLOKERA DO E18b pod warunkiem literalnego v1.0 z cap=200 na każdą normatywną próbę DK**; jeżeli plan zakłada cap>200, blokada K6 pozostaje po jego stronie. Kandydaci do v1.1: większy cap, toy-testy z wieloma flipami, testy generowane deterministycznie, wzmocnione Z1, formalniejsze kryterium zbieżności pomocniczego DK.

### 4. Rejestracja wyniku Kimiego (trzy drogi Z1, ogłoszenie; raport formalny zamówiony)

**Kimi:** wykonał komplet trzech niezależnych dróg Z1, niezależnych od artefaktu K17f-v3 i od siebie nawzajem:
- **Droga A (zasada argumentu, winding number):** dysk 1 (|z|<283/1024): N=21.000000 ✓; dysk 2 (|z−9/16|<1/8): N=1.000000 ✓.
- **Droga C (dyskretna zasada argumentu):** dysk 1: N=21.000000 ✓; dysk 2: N=1.000000 ✓.
- **Droga B (sekwencja Sturma, pierwiastki rzeczywiste):** dysk 1: 9 pierwiastków rzeczywistych; pozostałe 12 = 6 par sprzężonych (Sturm liczy wyłącznie rzeczywiste; 9+12=21 spójne z profilem widma r: subdominanta 0.5546… rzeczywista, reszta w parach).
- **Kompletność:** 21+1=22=deg r, potwierdzona trzema drogami.

Zgodność z L_count v3 (21/1) i z Z1 Vibe (DK: 21/1). Kimi deklaruje rozstrzygnięcie ograniczenia jawnego Z1 dysku 2 i pyta, czy przygotować formalny raport do rejestracji. **Odpowiedź szefa lab.: TAK** (sekcja 5c). Status: ogłoszenie przez relay; formalna rejestracja wymaga raportu (sekcja 5c).

### 5. Decyzje szefa laboratorium

**a. Cap E18b: przyjmuję stanowisko Copilota, moja propozycja cap ≥ 400 (11aw sekcja 5) WYCOFANA.** E18b wyłącznie literalnie wg v1.0: cap=200 dla BASE i E2; brak stopu po 200 ⇒ FAIL ⇒ E2 (esc_used:=1); ponowny brak stopu ⇒ GLOBALNY STOP. Uzasadnienie: Z0 i dyscyplina prerejestracji — nie zmieniamy reguły po zobaczeniu danych kontrolnych; informacja „201 iteracji" jest prerejestrowanym wynikiem proceduralnym, nie awarią badania. Sugestia DeepSeeka (500) i moja dawna (400) przechodzą do rejestru kandydatów v1.1. Przebiegi powyżej 200 iteracji: wyłącznie diagnostyka po zadekretowanym FAIL, bez wpływu na status normatywny.

**b. Z1 dysk 2: trzecia droga Kimiego adresuje dokładnie żądanie Asteriona.** Drogi A i C (zasada argumentu ciągła i dyskretna po transformacji dysku) to metody, których poprawność nie zależy od zbieżności iteracyjnego lokalizowania pierwiastków; droga B (Sturm) kontroluje część rzeczywistą widma. To nie jest „kolejny wariant DK". Formalne domknięcie Z1 dysku 2 nastąpi po rejestracji raportu formalnego Kimi; wtedy prośba do Asteriona o formalne potwierdzenie sufficiency.

**c. Raport formalny Kimi (zamówienie):** zawrzeć per dysk: metodę (zdefiniować transformację, na jakim wielomianie liczona zasada argumentu; siatkę/gęstość dla drogi C; konstrukcję sekwencji Sturma dla drogi B), liczby z wartościami pełnymi (nie tylko 6 miejsc), ocenę błędu/marginesu (np. odległość obrazu kręgu od 0, kontrola windingu na podsiatkach), oraz kompletność 21+1=22. Raport będzie zarejestrowany jako Z1-dysk2 certyfikat trzecią drogą; jeżeli raport ujawni rozjazd z 1, natychmiastny STOP i wstrzymanie E18b bez wyjątków.

**d. Sugestia DeepSeeka przyjęta jako uzupełniający zapis dokumentacyjny (bez edycji zamrożonej 11av):** stabilność count_in dysku 2 przy limitach {1000, 2000, 5000, 10000, 20000} = {1, 1, 1, 1, 1}, margines klasyfikacji 0.996 stały przy każdym limicie. Źródła: 11av sekcja 5 (przebieg oficjalny: limit 1000, count_in=1; diagnostyka: limity 2000–20000, count_in=1, skrypt diag-z1d2.ts sha256 db143881…, artefakt nietknięty). To dokumentacja istniejącej diagnostyki, nie nowe kryterium.

**e. Uwaga DeepSeeka o v1.1 przyjęta jawnie:** przy rozszerzaniu baterii (toy z flipami, testy generowane) nowa wersja baterii testowana od zera na nowym K17f (nowy hasz, pełna kwalifikacja), nie „dodane testy na istniejącym artefakcie" — zapobieganie klasie provenance break z 11at→11av. Rejestr kandydatów v1.1: N48 (re-run przed rejestracją hasza), toy-dwa-niesąsiednie-flipy (Claude), deterministyczne testy generowane (Claude/DeepSeek), cap DK > 200 (DeepSeek/Vibe, wycofane z v1.0), wzmocnione Z1 jako krok formalny (Copilot), ewentualnie formalniejsze kryterium zbieżności pomocniczego DK.

### 6. E18b: warunki startu (aktualizacja)

**HOLD** (K6: populacja 361 par nietknięta). Start wyłącznie po łącznym spełnieniu:
1. Raport formalny Kimi (Z1 dysk 2 trzecią drogą) zarejestrowany w repo i zgodny z 1.
2. Formalne potwierdzenie Asteriona (sufficiency Z1 dysku 2 po raporcie Kimiego).
3. Pełny A1–F3 DeepSeeka na treści logów 11as/11at/11au/11av/11aw — **wklejka: Leszek** (bez tego DeepSeek formalnie nie autoryzuje).
4. Copilot: warunek spełniony z urzędu przy literalnym v1.0 (cap=200, sekcja 5a).
5. Claude: opcjonalnie (przerwa); jego przegląd 11at rozliczony w 11aw, brak otwartych żądań z jego strony.

---
