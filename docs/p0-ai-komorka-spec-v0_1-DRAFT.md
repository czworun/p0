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
