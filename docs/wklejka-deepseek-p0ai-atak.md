# Wklejka dla DeepSeeka: atak merytoryczny na spec KOMÓRKA P0 v0.1-DRAFT (program P0-AI, sesja TAU-9)

**Kontekst administracyjny.** Nadawca: Vibe (Laboratorium P0), 2026-11-16, zlecenie Leszka (właściciela korpusu). Program P0-AI otwarty sesją TAU-9 wg jego jawnej delegacji: „Celem jest sieć neuronowa AI P0 SERC". Decyzje szefa lab. D1–D8 wpisane do rejestru; pozycja #1 kolejki: atak zewnętrznych na spec DRAFT przed zamrożeniem v1.0 i przed jakąkolwiek implementacją. Prosimy o ATAK MERYTORYCZNY na poniższy DRAFT: luki, sprzeczności, braki definicji, nieostre kryteria, plus propozycje konstruktywne do pytań otwartych S1–S3. NIE prosimy o implementacje ani kod (Z3: specyfikacje nie kod; lekcja MVP-01: prerejestracja kryteriów falsyfikacji przed pierwszym wykonaniem). Kontrola liczb §8 jako argument ataku jest dozwolona; statusy Z1 nadaje wyłącznie protokół replikacji po zamrożeniu v1.0. MVP-02, E18c i H-C5 pozostają POZA tematem tej wklejki (prosimy ich nie podejmować w odpowiedzi).

**Zasady rejestru (przypomnienie).** Z0: droga ważniejsza niż cel (koncesja przy błędzie jest wartością). Z1: ✅ dopiero po zgodnej drugiej, niezależnej implementacji; 🔍 = wynik jednego rachunku, czeka na replikację. Z2: jawna konwencja; rozjazd między implementacjami rozstrzyga się u źródła (konwencje), nie siłą liczb. Z3: specyfikacje, nie kod. Blokady rejestru obowiązują także w P0-AI: Tw. A (Hom_{S_n}(Sym²V_cyc, V_cyc) = 0 — brak mieszania sektorów z automatu); Mechanizm VII (wzrost wymaga mieszania sektorów; kandydat mechanizmu: przełącznik centrum z TAU-8); pamięć K-1 (1 bit kandydat — v0.1 nie rości pamięci symbolicznej); kanały 0→5→11→24 = artefakt podgrup (anty-numerologia).

**Doktryna P0-AI (Leszka; w specu jako zobowiązania C1–C6, §3).** Trening oparty na P0: każda aktualizacja przechodzi przez P0 (tranzyt), żadne dopasowanie wprost do celu. Fonem = basen atraktora: jednostka ciągła, nie symbol. Sen = uśrednianie ku ruchomemu barycentrum doświadczeń, nie zapis sztywnej kopii. Ciało: 4 niezależne serca K4, 6 kanałów (RPi5 odroczone do bramek B1–B4; constraint: portowalność na 4 niezależne procesy bez ukrytego globalnego stanu). Nauka dziecka: brzmienie → zakres → znak → znaczenie; v0.1 operuje wyłącznie warstwą brzmienia.

**Sesja TAU-9 w skrócie.** Decyzja kierunkowa: pierwszy obiekt = KOMÓRKA P0 v0.1, najmniejszy wycinek pionowy instantjujący naraz wszystkie zobowiązania doktryny (stan na simpleksie SERC z G = 4I−J; dzień = relaksacja DEQ między basenami rezonansowymi; noc = uśrednianie ku ruchomemu barycentrum; bez tokenizacji). Rachunek od zera TAU-9-TOY (🔍 1 słój): toy Hopfield na sercach K4 — punkt symetryczny (kierunek barycentrum P0) = SIODŁO przy wszystkich β ∈ {1.5, 2, 3} (a* = 0.29533/0.343999/0.369071; poprzeczny +0.1226/+0.2255/+0.5699, podłużny −0.5456/−0.7583/−0.9293); początek m=0 = REPELLER (eig β−1, analitycznie); serca = ATTRACTORY przy każdym β (β=2: m* = 0.957504, J = −0.833628·I); wszystkie mieszaniny (3z4, 2+2, 2+1+1, 2, symetryczna) = SIODŁA (p=4, β=2) — dynamika dnia na K4 nie ma punktu spoczynku poza sercami; parzystość: p=3/p=5 mieszanina symetryczna ATTRACTOR przy β=3 (a* = 0.472105/0.346471), SADDLE przy β=2 — zadeklarowana jako artefakt równoległej aktualizacji znakowanej (Z2), nie prawo doktryny. Errata sesyjna nr 1: pierwsza implementacja Jacobi eig degenerowała przy równych przekątnych (t=0 przy τ=0); klasyfikacje punktów symetrycznych pierwszego przebiegu NIEWAŻNE (kontrola ręczna, lekcja E18a); drugi przebieg czysty; zgodność obu dróg eigen (analityczna struktura DA = x·I + y·(J−I) vs Jacobi) 1e−5. Interpretacja (warstwa opisowa, nie podstawa statusów): dynamika dnia przepływa przez P0 i nie odpoczywa; ruch ku barycentrum = jedyny legalny spoczynek w P0; stąd architektura dwufazowa F_dzień + F_noc (D3): napięcie doktryny „P0 jako attractor" (sen) vs „P0 jako stan przejścia" (dzień) rozstrzygnięte jako obie racje w różnych fazach.

**ZLECENIE: atak na spec (zakres wspólny, §0–§9).** (a) Czy zobowiązania C1–C6 są falsyfikowalne i mierzalne, czy któreś jest niemierzalnym zobowiązaniem? (b) Czy bramki B1–B6 mają jednoznaczne kryteria PASS/FAIL; czy któraś jest niefalsyfikowalna, trywialna albo cyrkularna? (c) Czy uzasadnienie architektury dwufazowej z rachunku toy (§2 i §8) jest transferowalne na simpleks SERC z G = 4I−J, czy toy (Hadamard/Hopfield, zredukowane nakładania) dowodzi tylko siebie? (d) Propozycje operacjonalizacji pytań otwartych S1–S3 (§7): S1 czym jest „nowe brzmienie" jako wektor doświadczenia w SERC; S2 koder wejścia na simpleks SERC bez tokenizacji; S3 relacja zobowiązań relacyjnych (H-REL-1, P0-AI v0.3.1-synthesis) do komórki vs pary (v0.2).

**Zlecenie dostosowane (DeepSeek): konwencje i warstwa symboliczna.** (a) Czy deklaracja parzystości (§8 pkt 5: p=3/p=5 mieszanina symetryczna ATTRACTOR przy β=3, SADDLE przy β=2, jako artefakt równoległej aktualizacji znakowanej) jest poprawna, czy kryje prawo geometryczne — pożądany dowód albo kontrprzykład w konwencjach Z2. (b) Czy pełna klasyfikacja analityczna punktów stałych zredukowanej dynamiki nakładań (β-zależne a*, widmo Jacobianu w rodzinie mieszanin) jest osiągalna w zamkniętej formie? To wzmocniłoby prerejestrację B2 i przyszły pakiet replikacji Z1. (c) Propozycje S2 (koder wejścia na simpleks SERC bez tokenizacji): jak osadzić sygnał ciągły na simpleksie bez warstwy znaków, w duchu Pana analiz symbolicznych.

**Format odpowiedzi.** Zarzuty numerowane A1, A2, ... z odniesieniem do paragrafów; propozycje konstruktywne odrębnie (P1, P2, ...); werdykt końcowy jednoznaczny: „GOTOWY DO ZAMROŻENIA v1.0 PO ERRATACH" albo „NIEGOTOWY: blokery (lista)". Jeżeli któryś zarzut wymagałby rachunku, prosimy opisać go co do konwencji i kryteriów zbieżności (Z2), bez wykonywania w ramach ataku. Raport podpisany; rozliczenie w warsztacie Vibe (sesja TAU-9, runda 11bz).

---

# Specyfikacja KOMÓRKA P0 v0.1-DRAFT — VERBATIM z repo (commit 9dc97cd)

# P0-AI — KOMÓRKA P0 v0.1 — specyfikacja DRAFT (do ataku zewnętrznego)

Status: **DRAFT v0.1** (sesja TAU-9, 2026-11-16). Autor specu i rachunku sesyjnego: Vibe (Laboratorium P0); doktryna: Leszek. Kolejność obowiązkowa (lekcja MVP-01/E19): (1) prerejestracja kryteriów falsyfikacji (§4, punkt 1), (2) atak zewnętrznych modeli (Claude, Asterion/GPT, DeepSeek; relay przez Leszka) na TYM DRAFT, (3) zamrożenie v1.0 (wartości oczekiwane + tolerancje bramek), (4) implementacje Z1. Żadnych rachunków implementacyjnych przed zamrożeniem.

## §0 Cel i obiekt

Cel programu P0-AI (decyzja D1, sesja TAU-9): sieć urodzona z P0, nie sieć dopasowana do P0. Pierwszy obiekt: **KOMÓRKA P0 v0.1** — najmniejszy wycinek pionowy instantjujący naraz wszystkie zobowiązania doktryny: stan na simpleksie SERC, dzień = relaksacja między basenami rezonansowymi, noc = uśrednianie ku ruchomemu barycentrum. Bez tokenizacji; bez pamięci symbolicznej; brzmienie przed znakiem (nauka dziecka: brzmienie → zakres → znak → znaczenie; v0.1 operuje wyłącznie warstwą brzmienia).

## §1 Konwencje (Z2, jawne)

- Stan komórki: punkt na simpleksie SERC (4 serca K4, 6 kanałów wg rejestru).
- Geometria simpleksu: G = 4I − J (konwencja rejestru).
- Faza dnia: operator relaksacji (DEQ) między basenami rezonansowymi; P0 = kierunek tranzytu, nie punkt spoczynku.
- Faza nocy: operator uśredniania ku ruchomemu barycentrum; P0 = jedyny legalny kierunek spoczynku.
- Determinizm: wszystkie losowe inicjalizacje z jawnych seedów (LCG lub równoważny, zapisany w raporcie).
- Reprodukcja: każda liczba raportowana z kryterium zbieżności i fingerprintem.

## §2 Architektura dwufazowa (D3)

F_dzień + F_noc, wymuszona geometrycznie rachunkiem TAU-9-TOY (§8): dynamika dnia na K4 nie ma punktu spoczynku poza sercami (początek = repeller; wszystkie mieszaniny i punkt symetryczny = siodła), a ruch ku barycentrum jest jedynym legalnym spoczynkiem w P0. Bez F_noc komórka nie ma jak odpocząć; bez F_dzień nie ma jak uczyć. Napięcie doktryny „P0 jako attractor" (sen) vs „P0 jako stan przejścia" (Tom I) rozstrzygnięte: obie racje, w różnych fazach. Obie fazy obowiązkowe w v0.1.

## §3 Zobowiązania doktryny (kandydaci falsyfikowalni)

- **C1** Trening oparty na P0: każda aktualizacja przechodzi przez P0 (tranzyt); żadne dopasowanie wprost do celu.
- **C2** Fonem = basen atraktora: jednostką uczenia jest basen (przyciąganie ciągłe), nie symbol dyskretny.
- **C3** Sen = uśrednianie: konsolidacja jako ruch ku ruchomemu barycentrum doświadczeń, nie zapis sztywnej kopii.
- **C4** Ciało: 4 niezależne serca K4, 6 kanałów; brak ukrytego globalnego stanu; portowalność na 4 niezależne procesy (D6).
- **C5** Nauka dziecka: brzmienie → zakres → znak → znaczenie; v0.1 = wyłącznie brzmienie (zakres wchodzi przez B5).
- **C6** P0 podwójna rola: tranzyt (dzień) i kierunek spoczynku (noc).

## §4 Bramki prerejestrowane (D4)

**PUNKT 1 (przed implementacją):** kryteria falsyfikacji każdej bramki zapisane poniżej; wartości oczekiwane i tolerancje zamrażane w v1.0 PRZED pierwszym wykonaniem.

- **B1 Konwergencja DEQ:** residuum poniżej tol (tol do zamrożenia); FAIL = brak zbieżności w limicie kroków.
- **B2 P0-tranzyt:** siodło w Jacobianie fazy dnia (w punkcie symetrycznym: poprzeczne eig > 0, podłużne < 0) + attraktor operatora nocy w kierunku barycentrum.
- **B3 Sen zachowuje baseny dnia:** po cyklu dzień–noc–dzień baseny dnia przetrwają. Kontrola negatywna: relaksacja ku SZTYWNEJ kopii stanu degraduje nowe baseny po wzroście — jeśli sztywna kopia równa dobrze, B3 niczego nie testuje.
- **B4 Barycentrum ruchome:** po dodaniu nowego brzmienia punkt spoczynku nocy przesuwa się; powrót do zapisanego stanu sprzed wzrostu = FAIL.
- **B5 Basen z granicą kategorii:** punkty poza zakresem → brak przypisania; przypisanie najbliższego sąsiada poza granicą = FAIL.
- **B6 Samotna komórka:** doktryna przewiduje CZĘŚCIOWĄ degradację snu bez doświadczenia relacyjnego; v0.1 testuje komórkę pojedynczą; para komórek = v0.2 (po rozliczeniu B6).

## §5 Protokół Z1 (D5)

Dwie niezależne implementacje (warsztat Vibe + jeden wykonawca zewnętrzny) przed jakimkolwiek ✅. Rachunek sesyjny TAU-9-TOY (§8) = 🔍 1 słój, wchodzi do kolejki replikacji Z1. Atak zewnętrznych na ten spec PRZED implementacjami; raporty wg wzorca rejestru (atrybucja, konwencje, kryteria zbieżności).

## §6 Blokady rejestru (D7)

- Tw. A (Hom_{S_n}(Sym²V_cyc, V_cyc) = 0) i Mechanizm VII: wzrost wymaga mieszania sektorów — komórka musi posiadać jawny mechanizm mieszania; kandydat: przełącznik centrum (TAU-8).
- Pamięć K-1 (1 bit): v0.1 NIE rości pamięci symbolicznej; baseny ciągłe, nie znaki.
- 0→5→11→24 = artefakt podgrup: żadnych roszczeń numerologicznych o kanalizacji.

## §7 Pytania otwarte (do ataku zewnętrznego)

- **S1** Operacjonalizacja snu: czym dokładnie jest „nowe brzmienie" jako wektor doświadczenia w SERC (do zamrożenia przed implementacją).
- **S2** Koder wejścia: jak sygnał wejściowy trafia na simpleks SERC bez tokenizacji (propozycje do ataku).
- **S3** Relacja do H-REL-1 z P0-AI v0.3.1-synthesis: czy zobowiązania relacyjne przenoszą się na komórkę, czy dopiero na parę (v0.2).

## §8 Rachunek sesyjny TAU-9-TOY (Z3-opis; 🔍 1 słój, do replikacji Z1)

Pamięć skojarzeniowa Hopfielda na sercach K4 (dynamika nakładań m_μ). Konwencje: wzorce ortogonalne znakowe (Hadamard N=256, wiersze 1,2,4,8; p=3: wiersze 1,2,4; p=5: + wiersz 16); zredukowana dynamika nakładań dokładna: ṁ_μ = −m_μ + (1/2^p) Σ_s s_μ tanh(β s·m), β ∈ {1.5, 2, 3}; aktualizacja równoległa; LCG seed 20261116, a = 48271, m = 2³¹−1, c = 0; sign(0) = +1.

Wyniki: (1) p=4 punkt symetryczny (kierunek barycentrum P0) = SIODŁO przy wszystkich β: a* = 0.29533 / 0.343999 / 0.369071; eig podłużny (kier. 𝟙) −0.5456 / −0.7583 / −0.9293, poprzeczny (×3) +0.1226 / +0.2255 / +0.5699. (2) m=0 = REPELLER (eig β−1, analitycznie). (3) Serca = ATTRACTORY przy każdym β (β=2: m* = 0.957504, J = −0.833628·I). (4) Inwentarz p=4 β=2: 8 attraktorów-wierzchołków, 1 repeller, wszystkie mieszaniny (3z4, 2+2, 2+1+1, 2, symetryczna) = SIODŁA. (5) Parzystość: p=3/p=5 mieszanina symetryczna ATTRACTOR przy β=3 (a* = 0.472105 / 0.346471; poprzeczny −0.370044 / −0.104837), SADDLE przy β=2 — deklarowana jako artefakt równoległej aktualizacji znakowanej (Z2, anty-numerologia), nie prawo doktryny. (6) Finite-N (sign, N=256): narożnik p=4 (nakładania 0.375×4) = punkt stały mapy dyskretnej; 200 prób: remisy-centrum → 64 wierzchołki / 136 mieszaniny; flip 5% → 66 / 134; flip 20% → 85 / 115.

Errata sesyjna nr 1: pierwsza implementacja Jacobi eig degenerowała przy równych przekątnych (t=0 przy τ=0, brak obrotu) — klasyfikacje punktów symetrycznych pierwszego przebiegu NIEWAŻNE (wyłapane kontrolą ręczną, lekcja E18a); drugi przebieg czysty; zgodność obu dróg eigen (analityczna struktura DA = x·I + y·(J−I) w punkcie symetrycznym vs Jacobi) 1e−5. Zastrzeżenie: finite-N „tieflip" dla p=3/p=5 pusty (brak remisów przy sumach nieparzystych).

## §9 Wersjonowanie

v0.1-DRAFT → (atak zewnętrznych) → v1.0 (zamrożenie: wartości oczekiwane + tolerancje bramek) → implementacje Z1 → rozliczenie bramek. Zmiany wyłącznie przed pierwszą kwalifikacją; po niej wyłącznie erraty z numeracją (wzorzec TAU-8 v2–v4).
