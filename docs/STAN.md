# P0: Tabela stanu projektu

v1.6 (errata zapisu fazy i rozliczenie kontroli), 2026-11-28. v1.5 (aktualizacja po wykonaniu E-01), 2026-11-28. v1.4 (erraty), 2026-11-27. v1.3 (erraty), 2026-11-27. v1.2 (erraty), 2026-11-27. v1.1 (erraty), 2026-11-27. v1.0 zamrożona na rozkaz właściciela i opublikowana jako docs/STAN.md w repo czworun/p0 (czubek publikacji: main 79179b0, punkt odniesienia zamrożenia: main e0f38ab0). Erraty v1.1 wprowadzone na rozkaz właściciela po audytach zewnętrznych (Asterion), rozliczonych niezależną kontrolą (Vibe, 2026-11-27). Weryfikacja 2026-11-26 (mapa) = kontrola mapy i obecności dokumentów (lustracja korzeni 24 plików, kontrola fraz w repo), **nie** niezależna ponowna weryfikacja treści twierdzeń.

**Stan empiryczny projektu: 1 z 8 zaprojektowanych protokołów wykonanych (E-01, 2026-11-28: predykcja potwierdzona numerycznie, hipoteza nie sfalsyfikowana).** Dotychczasowe weryfikacje miały charakter formalno-matematyczny albo obliczeniowy. Dojrzałość matematyczna linii i walidacja empiryczna P0 to dwa różne osiągnięcia; ta tabela ma pozwalać odczytać tę różnicę bez znajomości historii projektu.

**Bilans epistemiczny (przybliżenie, nie zliczenie):** rzędu 25 wspartych, 10 znanych dziś sfalsyfikowanych w korzeniach (wszystkie podtypu rachunkowego, jeszcze żadna empiryczna; dwie dalsze falsyfikacje w serii H-DEF poza bilansem korzeni), rzędu 90 nieprzetestowanych: mniej więcej jedna piąta, jedna dziesiąta i dwie trzecie. Liczby dotyczą **twierdzeń, hipotez i predykcji** (obiektów z treścią twierdzenia, po atomizacji), nie linii ani plików; **pytania i testy są ewidencjonowane w rejestrze, ale nie wchodzą do tych liczników**.

**Stan w pigułce:** prace teoretyczne w liniach Centroid i Wave zamknięte (pozostają w nich jawnie wskazane pytania i zależności, patrz sekcja B), warstwa eksperymentalna rozpoczęta (1 z 8 protokołów, E-01 wykonane 2026-11-28: para zespolona potwierdzona, faza 25,7721°, odchylenie 0,0021° od 25,77°, wewnątrz marginesu 5°), 10 znanych falsyfikacji rachunkowych w korzeniach (dalsze przypadki H-DEF i częściowy S12 pozostają poza tym licznikiem, patrz sekcja E), E-01 wykonane 2026-11-28 na rozkaz właściciela (rachunek niezależny Vibe, hipoteza nie sfalsyfikowana), dwie decyzje właściciela w kolejce (relay ataku P0-AI, symulacja H-DEF A vs B przed zamrożeniem v1.0 KOMÓRKA).

Symbole w skrócie: ✅ wspiera, ❌ falsyfikuje, ⚪ nierozstrzygnięta, 💡 nieprzetestowana, 🔍 brak potwierdzonej niezależnej replikacji. Pełne zasady i legenda: **Aneks na końcu dokumentu**.

## A. Kamienie milowe i kolejki

| Linia | Status | Weryfikacja | Następny krok | Właściciel |
|---|---|---|---|---|
| MVP-01 | prace: zamknięte; hipotezy wg rejestru | 2026-11-25 (INDEKS) | brak | zamknięte |
| MVP-02 | prace: 🚫 zamknięte decyzją właściciela; K3: ⚪ wynik bez mocy rozstrzygającej (test transportowy F_r = 0/20, trzy zgodne implementacje; kwalifikacja niezależności trzech implementacji bez wpływu na ⚪); teza H_b: 🚫 odrzucona decyzją, NIE ❌ sfalsyfikowana | 2026-11-25 | erraty W-2/W-3 śpią do v1.5 | zamknięte |
| P0-AI / KOMÓRKA | DRAFT v0.1, atakowany | 2026-11-25 | relay 3 wklejek ataku (osobno do trzech wykonawców, zero konsultacji między nimi) | 🟢 Leszek |
| H-DEF | otwarte A vs B | 2026-11-25 | symulacja dwupoziomowa A vs B na hasło; decyzja nośnika P0 przed zamrożeniem v1.0 | na hasło |
| E18c | ⏸ uśpiony (status poznawczy bez zmian) | 2026-11-22 | bez zmian | ⏸ |
| Rejestr repo (wyniki.md, zlecenia.md) | ZAMROŻONE na erze 11cs | 2026-11-25 | żywy rejestr = baza wiedzy; INDEKS = mapa repo | archiwum |
| INDEKS | żywa mapa repo | 2026-11-26 | erratum do rozkazu: korzenie mają 24 pliki, INDEKS podaje 25 w dwóch miejscach | na rozkaz |

## B. Stan linii badawczych i najważniejszych hipotez (mapa, nie pełny rejestr)

Kolumna „Cykl życia" opisuje stan dokumentu (aktywny, zamrożony, zamknięty, archiwum), nie status epistemiczny; wyniki poznawcze siedzą w kolumnie „Najważniejsze wyniki", hipotezy w „Wiszące". Weryfikacja wszystkich wierszy: **2026-11-26 (mapa)**. Odpowiedzialny to wykonawca następnej akcji; właścicielem projektu i wszystkich hipotez pozostaje Leszek.

| Linia (plik) | Cykl życia | Najważniejsze wyniki | Wiszące | Następna najtańsza akcja | Odpowiedzialny |
|---|---|---|---|---|---|
| TAU v1.7.2 | aktywny | 7 twierdzeń z dowodami formalnymi ✅🔍 (jednotorowe) | 💡 P22, P24, P26 (P26 gotowe, priorytet 1), P10-alt, P14, P15; ✅🔍 P23, asymptotyka 0,12383; τ_relation niezmierzone | replikacja Tw. 7.8.7.2 (czysta algebra) | warsztat |
| SERC v0.4.2 | zamrożony świadomie | brak rachunków domkniętych; brak walidacji empirycznej (docelowy zakres walidacji: kliniczny) | 💡 H-SERC-1..6; ✅🔍 H-SERC-7 (redukcja 16 do 5 klas); **warunek odmrożenia:** dostęp do danych klinicznych o ustalonej formie (źródło i format: pytanie otwarte do właściciela) | walidacja kliniczna, nie rachunek | dane zewnętrzne |
| TETRA-20 v0.2.4 | aktywny | dekompozycja algebry ✅🔍 (wielometodowa, ale jedna sesja; Z1 zewnętrzna brak) | ✅🔍 dynamika (r 0,932, plateau ~4,5); 💡 T1 klaster Mackaya, T6, T13..T15, T16b (priorytet 1, wymaga setupu), E-TETRA-10..12 | replikacja Z1 dekompozycji algebry | wykonawcy |
| Estrada v0_8 (SSOT; v0_7 warstwa historyczna) | aktywny | równoważność S4 ✅🔍 (480 przypadków, jedna strona) | R-1b dowód otwarty; 💡 H-P0E2 antykul; propozycja P0-Estrada-03 (predykcje P-03a..c) | powtórzenie 480 przypadków S4; decyzja o P0-Estrada-03 | 🟢 decyzja Leszka |
| Defect v0.8 | aktywny | Tw. A, klasyfikacja podgrup, Tw. 4a, Δ(L) = λL·δ, klasyfikacja remisów ✅🔍 (formalne, jednotorowe) | 💡 16 pytań (Wysokie: 3 operator W, 4 addytywność, 7 T_b i G2, 8 podgrupy, 9 so); ✅🔍 kompleksyfikacja minimum; 💡 H-Bridge v0.3 | pytanie 4 (addytywność defektu) | warsztat |
| Lattice v0.1.2 | aktywny | kanały 0→5→11→24, bramki 8/20, para K4, Φ_D, lemat jąder ✅🔍 (3 do 4 implementacje; niezależność wykonawców, osobnych sesji i brak wspólnego kodu do potwierdzenia wg definicji przy budowie rejestru, wtedy znacznik znika) | tabela S_v (w toku); N1 trzeci rachunek GPT; transformacja nośnika pod −I (GO: Claude i DeepSeek); 💡 P0-Szachy, T-K4-3, dychotomia 5/11 | dokończenie tabeli S_v | warsztat |
| Memory v0.3.7 | aktywny | formalizm ✅🔍; M18 ❌ (faza poza ω-granicą); ✅🔍 M16a (0,71 / 67,76 / 7,53 / 86,11 proc., dwie ręce zgodne) | 💡 M19, M20, M1, M7; ✅🔍 M17, M5 (wyniki jedną ręką) | trzecia replikacja M16a | wykonawcy |
| Flow v0.5.3 | zamrożony świadomie | Tw. A ✅🔍 (aparat wielu metod: EGF, Bell, Poisson, Fraction; niezależność wykonawców do potwierdzenia wg definicji); wynik główny negatywny domknięty: nie NS, obiekt trzeci | 💡 granica continuum z T_b (G2, E6, Kähler), równanie dla T_a+T_b, H-MEM-1 operatorowo; **warunek odmrożenia:** identyfikacja granicy continuum, w której T_b przeżywa, albo decyzja właściciela; treść wchłonięta przez Defect §12A do §12G, plik pozostaje korzeniem źródłowym | bramka kowariancji §5.5.1 przed każdą dynamiką | warsztat |
| Stalk v1.2 | aktywny (rejestr notatnika) | N1 rozkład {0, 1, 2, 4} ✅🔍 jedną ręką (zakres: 56 trójek silnych wachlarzy; 27, 6, 19, 4; N1 = 3 nie istnieje); chiralność globalna ✅🔍 | 💡 P1, P2, P8 (Wysokie) | sonda N1 (algebra 12 na 12, tania) | warsztat |
| Axis v0.3 | aktywny (warstwa 0) | osie wyprowadzone ✅🔍; V_ρ i V_cyc nieizomorficzne (standardowa vs standardowa⊗znak) ✅🔍; pytanie 2 rozstrzygnięte 2026-11-27 dwiema rękami (kierunki K_ij = osie półobrotów grupy obrotów oktaedru, półobroty generują grupę 24 ≅ S4, konwencja exp(4√2 π K_ij); kandydat lematu AXIS-DEF-01 w bazie wiedzy) | 💡 pytania 1, 3..6; P0-Hilbert i S4-Rep zadeklarowane, NIEOBECNE | wyprowadzenie K_ij z definicji M_i, związek z S4 z Centroid §8.1 (propozycja Asteriona) | warsztat |
| Scalar v0.3.5 | zamknięta teoria (po śladzie) | S12 częściowo ❌: status pozostaje CZĄSTKOWY do czasu prerejestracji kryterium rozbioru; czy protokół S12 zawiera już niezależnie ustalony podział na człony, sprawdzić przy budowie rejestru; jeśli nie, prerejestracja PRZED rozbiciem (rozbiór post-hoc po poznaniu wyniku nieważny wg zasady 9); asymptota 0,12383 ✅🔍 | 💡 S1 otwarte | E-01 rozstrzyga o fazie | zależne od E-01 |
| Relacje v0.3 | kandydat (po śladzie) | ✅🔍 R-01; Test A §9.2 częściowo ⚪ | brak nowych | nie podnosić do filara | ⏸ |
| Wave v0.6.1 | zamknięta teoria (po śladzie) | teoria zamknięta, Lemat W ✅🔍 | 💡 automat projektorowy §5; katalog słów L>12 (zależny od E-04, E-05) | protokół E-04 | zależne od Experiments |
| Centroid v5.2-zmiany | zamknięta teoria (po śladzie) | teoria zamknięta | dowód ogólny hierarchii §13 otwarty (PYTANIE, nie hipoteza) | papier, nie rachunek | ⏸ |
| Alchemy v0.4.4 | aktywny program | ❌ KKT; ❌ kontrakcyjność globalna (26,6 proc.); ✅🔍 orbita 24; ✅🔍 tau AL-H10, rho 0,2726 | 💡 AL-H7..H9 | most do Net na orbicie 24 sygnatur | warsztat |
| Net v0.6.1 | aktywny program | N9 ✅🔍, B3 ✅🔍, ORB-05-R ✅🔍, M18 ❌ (ten sam obiekt co w Memory, liczony raz; kwalifikacja niezależności przy budowie rejestru) | 💡 Wysokie: N1, N2, N4, N10, B2, B5, M3, M16b, M19, M20, M1 | replikacje typu E0 (N1, N2, B5, M3, M16b) | wykonawcy |
| AI-synthesis v0.3.1 | aktywny program | ✅🔍 P_cyc·D = 0 (kandydat niezależnej replikacji); ✅🔍 REL-09; ❌ REL-10 soft gating; ❌ filtr P_cyc | 💡 REL-12 transfer K4 na K5 (priorytet A), REL-08b, REL-10b | replikacja tożsamości P_cyc·D = 0 | wykonawcy |
| Experiments v0.3.4 (erraty E-01/E-02; nazwa pliku pozostaje P0_Experiments_v0_3_2.md dla stabilności odnośników, wersja treści jawna w Status korekty) | aktywny program | **1 z 8 protokołów wykonanych (E-01 🔍, 2026-11-28)** | 🔍 E-01 wykonany, nie sfalsyfikowany; 💡 E-02..E-07, E-14 (zaprojektowane, E-02 wstrzymane do prerejestracji) | E-01 wykonany: faza potwierdzona (25,7721°) | warsztat |
| Applications v0.5.2 | aktywny program | A7 ✅🔍 (jedyny z częściowym wsparciem) | 💡 A1..A11 poza A7; A8 zależna od C2; A11 czeka na E-14 | po E-01 | zależne od Experiments |
| PILLARS-TABLE-1 | archiwum (ramowa) | pokrywa 10 z 24 pozycji | nieobecni: Origins, Hilbert, S4-Rep; pozycje Stalk i Axis do uregulowania | decyzja struktury tabeli | 🟢 Leszek |
| tetralogia-SERC, os-ai-dominik, Philosophy v0.6.2 | adnotacje i interpretacja | bez rachunków | 💡 MOST (11 pozycji, histereza do Memory); ✅🔍 4-simpleks, woda 104,48 stopnia (druga opinia wskazana) | drugie oko dla 4-simpleksu | wykonawcy |

## C. Ranking najtańszych testów

Tytuł mówi o testach, nie o falsyfikacjach: **pozycje o charakterze testów falsyfikacyjnych to 1, 11 i 12** (żadna z nich nie została jeszcze wykonana, więc żadnej hipotezy nie obalono); reszta to replikacje, rozstrzygnięcia i kontrola jakości (kolumna Rodzaj pracy). Koszt w tabeli = **pierwszy etap** (rachunek własny); pełna niezależna replikacja wg definicji legendy dodaje sesję innego wykonawcy na własnej implementacji.

| # | Cel | Rodzaj pracy | Kryterium porażki (co zabija hipotezę) | Koszt | Co rozstrzyga |
|---|---|---|---|---|---|
| 1 | E-01 faza 25,77 stopnia | falsyfikacja | WYKONANE 2026-11-28, NIE SFALSYFIKOWANE (rachunek niezależny Vibe: widmo rundy GS na K4 = {1; 0,1347106; 0,153348 ± 0,074039i}, argument pary 25,7721°, odchylenie od 25,77° równe 0,0021°, wewnątrz progu 5 stopni; gałąź rzeczywista nie spełniona, para zespolona istnieje; wykonane wg brzmienia v0.3.4): falsyfikacja dwiema gałęziami protokołu E-01 w pliku P0_Experiments_v0_3_2.md (próg i sekcję cytuję przy wykonaniu): gałąź fazowa, argument pary zespolonej operatora rundy poza przedziałem wokół 25,77 stopni z marginesem ponad 5 stopni przy precyzji poniżej 1e-6, LUB gałąź rzeczywista, wszystkie wartości własne operatora rundy rzeczywiste, brak pary zespolonej: upada przewidywanie fazowe K4 (zakres: system czterech podsystemów w kolejności cyklicznej 0,1,2,3; rozjazd zakresu E-01 usunięty erratami v0.3.3 i v0.3.4 pliku Experiments: predykcja, hipoteza i warunek falsyfikacji zawężone do K4 i kolejności 0,1,2,3, inne grafy z cyklem jako osobne hipotezy i predykcje do zaprojektowania) | minuty (E1) | TAK: faza K4 realna poza rachunkiem autora (rachunek Vibe 2026-11-28; kontrola porównawcza Asterion z rekonstrukcji z raportu, potwierdzenie co do cyfry; pełna replikacja Z1 jeszcze nie wykonana, status 🔍 utrzymany) |
| 2 | Tw. 7.8.7.2 TAU | replikacja | twierdzenie nie odtwarza się w niezależnym dowodzie lub rachunku | pierwszy rachunek: jedna sesja; niezależna replikacja: dodatkowa sesja innego wykonawcy | czy Tw. 7.8.7.2 jest replikowalny (uniwersalność c_m = 4/3 dla mK4, m co najmniej 3, mnożnik zaniku różnicy na wspólnej osi; nie cały kręgosłup TAU) |
| 3 | Stabilizator S4 Applications §4.1 w bazie osiowej Axis | replikacja | stabilizator zbioru δ(M0..M3) w O(3) nie jest izomorficzny z S4 (v1.1: kryterium izomorfizmu, nie samego rzędu 24; stabilizator bramek 8/20 w Lattice to inny obiekt, T_h ≅ A4 x C2, grupy nieizomorficzne) | jedna sesja | wspólny blok E-01, 1/8, znakowana reprezentacja |
| 4 | Axis pytanie 2a: czy 6 kierunków K_ij to osie półobrotów właściwej grupy obrotów oktaedru | rozstrzygnięcie | wynik binarny co do geometrii osi; v1.1: ROZSTRZYGNIĘTE 2026-11-27, kierunki to osie półobrotów, nie wierzchołki oktaedru (iloczyny znormalizowane ze zbioru {0, ±1/2}, zero par antypodalnych), dwie ręce: Asterion i Vibe | algebra 3 na 3 (wykonane) | geometria bloków interakcji |
| 5 | Axis pytanie 2b: czy półobroty o osiach K_ij generują grupę rzędu 24 izomorficzną z S4 | rozstrzygnięcie | wynik binarny co do struktury grupowej; v1.1: ROZSTRZYGNIĘTE 2026-11-27, domknięcie półobrotów daje dokładnie 24 macierze permutacji ze znakiem o wyznaczniku +1, klasy sprzężoności 1+6+8+3+6, grupa obrotów oktaedru ≅ S4; konwencja jawna: półobrót = exp(4√2 π K_ij) | algebra 3 na 3 (wykonane) | struktura algebraiczna bloków |
| 6 | Równoważność S4 Estrady (480 przypadków) | replikacja | rozjazd poza precyzję maszynową w choć jednym przypadku | tania numerika | most Estrada a algebra pnia |
| 7 | Stalk N1 rozkład {0, 1, 2, 4} | replikacja | rozkład inny niż 27, 6, 19, 4 albo istnienie trójki z N1 = 3 (zakres: te same 56 trójek silnych wachlarzy; odtworzenie, nie twierdzenie uniwersalne) | algebra 12 na 12 | scalenie N1: Lattice i Stalk |
| 8 | Flow bramka kowariancji §5.5.1 | kontrola jakości | odchylenie od wzorców γ: błąd setupu, nie wynik naukowy | wzorce gotowe | sanity każdej przyszłej dynamiki |
| 9 | Memory M16a, trzecia replikacja | replikacja | trzecia ręka poza tolerancją dwóch poprzednich: wynik ⚪, do wyjaśnienia | jedna sesja | most×tryb K2 (0,71 / 67,76 / 7,53 / 86,11) |
| 10 | TETRA-20, replikacja zewnętrzna: algebra i dynamika rozdzielone | replikacja | dekompozycja algebraiczna (22 niezmienniki kubiczne 7+15, 82 kwartyczne 15+67) albo pakiet 22 atraktorów (dynamika, wymaga odtworzenia setupu core_reconstruction.py poza repo) nie odtwarza się; wspólny rozkład 7+15 nie scala obu obiektów w jedno twierdzenie | jedna sesja (algebra); dodatkowa sesja z setupem (dynamika) | 22 tryby i 22 atraktory jako dwa obiekty |
| 11 | E-05 zanik koherencji | falsyfikacja | zanik nie-eksponencjalny (potęgowy, oscylacyjny, brak zaniku) albo dekrement inny niż 0,085 na literę; protokół E-05 w P0_Experiments_v0_3_2.md | symulacja E1 (10 000 słów); dane zewnętrzne dopiero E2, opcjonalnie | koherencja 0,085 na literę, zanik eksponencjalny |
| 12 | E-02 hierarchia czasowa z pierwszymi liczbami | falsyfikacja | kryterium operacyjne protokołu E-02 (plik P0_Experiments_v0_3_2.md, po erratach v0.3.3 i v0.3.4): konfiguracja (A) gładka, τ_T = 32·τ_L i τ_Z = 256·τ_L = 8·τ_T, versus konfiguracja (B) pierwsza, τ_T = 29·τ_L i τ_Z = 899·τ_L = 31·τ_T; szum gaussowski σ = 0,05 w momentach coincydencji (sic, brzmienie protokołu); odchylenie standardowe trajektorii poziomu T w oknie 20 000 taktów, N = 100; wynik p powyżej 0,05 w teście t-Studenta w co najmniej trzech niezależnych konstrukcjach symulacyjnych oznacza NIEPOTWIERDZENIE predykcji, nie automatyczne obalenie (nieodrzucenie hipotezy zerowej to nie dowód braku różnicy); obalenie wymaga testu równoważności lub przedziału ufności wobec prerejestrowanej minimalnej istotnej redukcji; NIE URUCHAMIAĆ przed prerejestracją (wartość minimalnej redukcji, decyzja o sparowaniu realizacji szumu, definicja jednostki niezależnej konstrukcji); trzy niezależne konstrukcje to wymóg protokołu, NIE pełna niezależna replikacja Z1 w rozumieniu aneksu (walidacja Z1 wymaga innego wykonawcy, osobnej sesji i własnej implementacji); jednostką analizy niezależna realizacja symulacji, nie takty trajektorii (pseudoreplikacja wykluczona); E1, symulacja N=100, niska trudność | symulacja E1 (N=100) | czy pierwsze liczby dają hierarchię czasową ponad gładkie rozkłady |

Pełne progi i przedziały żyją w protokołach (Experiments) i plikach linii; tabela je wskazuje, nie zastępuje. Tam, gdzie kryterium porażki nie jest spisane w pliku, dopisuje je właściciel przy budowie rejestru.

## D. Co jest nieaktualne (nie czytać po raz drugi)

| Źródło | Stan |
|---|---|
| wyniki.md, zlecenia.md | zamrożone na erze 11cs; żywy rejestr to baza wiedzy |
| PILLARS-TABLE-1 | ramowa, pokrywa 10 z 24 pozycji; liczby brać z adnotacji plików; druga częściowa tabela stanu: ryzyko rozjazdu z tym dokumentem |
| INDEKS | erratum 25 na 24 (dwa miejsca) do rozkazu |
| Estrada v0_7 | warstwa historyczna; SSOT = v0_8 |
| SERC v0.4.2, Flow v0.5.3 | zamrożone świadomie; warunki odmrożenia w ich wierszach sekcji B; nie oczekiwać nowej treści |
| Origins, P0-Hilbert, S4-Rep | zadeklarowane, NIEOBECNE w repo: Origins opisany tylko w PILLARS-TABLE-1 (filar 7, program spekulacyjny, nigdy nie napisany), Hilbert i S4-Rep w kolejce wg Axis §23; zero plików, zero spisanych hipotez; to zobowiązania, nie treść; bilans E słusznie ich nie obejmuje |

Rekomendacja na rozkaz: PILLARS-TABLE-1 pozostaje nienaruszona jako warstwa historyczna (Z0); ten dokument przejmuje rolę żywej tabeli stanu; jedno zdanie w INDEKS wskaże STAN.md jako nadrzędną mapę stanu.

Trzy liczby, których nie wolno mylić: **24 pliki** w korzenie, około **20 linii badawczych** (niektóre pliki to adnotacje lub warstwy historyczne), hipotezy liczone są **w rejestrze, nie w plikach**.

## E. Bilans pokrycia (wszystkie liczby przybliżone, do skorygowania przy budowie rejestru)

Liczniki obejmują **tylko korzenie**; seria H-DEF (około 21 pozycji) pozostaje poza bilansem do audytów.

| Pytanie | Odpowiedź dziś |
|---|---|
| Wyniki zgodne z twierdzeniem albo formalnie udowodnione (✅) | rzędu 25 (twierdzenia TAU, dekompozycja TETRA-20, Tw. A Flow, wyniki Lattice, ORB-05-R, P_cyc·D = 0, REL-09) |
| Z nich niezależnie zreplikowane (bez znacznika 🔍) | **żadne potwierdzone wg pełnej definicji**; kandydaci do kwalifikacji przy budowie rejestru: wyniki Lattice (3 do 4 implementacje), Tw. A Flow (aparat wielu metod), ORB-05-R; „w locu" = replikacje zapisane w samym pliku linii; czy przez różnych wykonawców w osobnych sesjach bez wspólnego kodu: potwierdzić przy budowie rejestru |
| ❌ sfalsyfikowane | 10 znanych dziś, wymienionych jawnie: (1) KKT, (2) kontrakcyjność globalna, (3) M18, (4) REL-10 soft gating, (5) filtr P_cyc, (6) synergia T_a+T_b, (7) związek 7,35 z 25,77, (8) H-LIGHT-1 3D, (9) mechanizm VII, (10) harmoniczna k=5; wszystkie podtypu rachunkowego ❌(r), falsyfikacje w określonych zakresach, nie rozstrzygnięcia empiryczne; lista z pełnej lustracji 24 plików; S12 częściowo ❌ pozostaje poza licznikiem do czasu rozbicia wg zasady 9; dwie dalsze poza bilansem korzeni (H-DEF-15, H-DEF-17); ❌(e) empirycznych: zero |
| ⚪ nierozstrzygnięte | 1 (K3 wynik typowy); M16a dołączy, jeśli trzecia replikacja się rozjedzie |
| 💡 nieprzetestowane | rzędu 90 |
| 🚫 odrzucone decyzją | 1 (teza H_b z MVP-02) |
| ⏳ do kwalifikacji (wątki spoza repo) | nieznane do audytów; pusty licznik nie oznacza zera |
| Weryfikacja empiryczna | **1 z 8 protokołów wykonanych (E-01, 2026-11-28: predykcja potwierdzona numerycznie)**; „zaprojektowany" = protokół spisany z metodą, predykcją i bramką w Experiments v0.3.2 (wszystkie osiem spełnia tę definicję, gotowe do wykonania); wszystkie ❌ powyżej pochodzą z rachunków wewnętrznych: projekt nie miał jeszcze kontaktu z danymi zewnętrznymi |
| Data weryfikacji wierszy | 2026-11-26 = kontrola mapy i obecności dokumentów, nie ponowna weryfikacja treści |

**Zasada jawnej niekompletności**: brak wpisu w rejestrze nie jest potwierdzeniem hipotezy ani brakiem problemu. Licznik wpisów niepełnych jest jawny dopóki rejestr nie zostanie domknięty.

## F. Rejestr hipotez P0 (warstwa druga, do budowy na rozkaz)

Architektura trójwarstwowa:

1. **Tabela stanu** (ten dokument): mapy linii, priorytetów, właścicieli.
2. **Rejestr hipotez**: jeden rekord na obiekt epistemiczny; status, zakres, dowód, historia.
3. **Baza wiedzy plus pliki linii**: rachunki, protokoły, wyniki, uzasadnienia.

**Typy wpisów** (rejestr ma je rozróżniać; testy nie są hipotezami):

| Typ | Przykład | Rola |
|---|---|---|
| HIPOTEZA | H-SERC-3 | twierdzenie oczekujące na rozstrzygnięcie |
| TWIERDZENIE | TAU-P26 | twierdzenie formalne |
| PREDYKCJA | faza 25,77 stopni | konkretny wynik przewidywany |
| TEST | EXP-E01 | procedura sprawdzająca |
| PYTANIE | DEF-Q4 | nierozstrzygnięty problem |
| KONTROLA | Flow §5.5.1 | kontrola poprawności setupu |

Relacja: **hipoteza → predykcja → test → wynik → dowód**. E-01 nie jest hipotezą tylko dlatego, że ma kryterium porażki: jest testem powiązanym z predykcją, którą sprawdza.

Rejestr jest **wskaźnikiem, nie drugim źródłem treści**: pole treść cytuje plik linii wraz z sekcją, nigdy nie parafrazuje ani nie redaguje treści.

Schemat rekordu: ID, typ wpisu, linia, treść (z odsyłaczem do sekcji), predykcja, **kryterium falsyfikacji** (najpierw wykorzystać istniejący protokół; właściciel dopisuje tylko tam, gdzie naprawdę go brakuje), zakres (założenia obowiązywania, w tym liczba implementacji dla wyników numerycznych), rodzaj twierdzenia (algebraiczne, empiryczne, interpretacyjne), status wyniku, znacznik walidacji, status organizacyjny, ostatni wynik, dowód (plik, sekcja, commit albo protokół), data weryfikacji, **powód ostatniej zmiany statusu** (pełna historia zmian z powodami żyje w bazie wiedzy), data zmiany statusu, następny test, właściciel.

Wątki spoza repo (np. z pamięci wykonawców): wchodzą jako ⏳ do kwalifikacji; treść, zakres i predykcję ustala się wspólnie z właścicielem w trakcie audytów, a status obowiązuje na dzień ustalenia (załatwia to data weryfikacji). Bez osobnego pola pochodzenia (decyzja właściciela, 2026-11-26).

Konwencja ID: prefiks linii plus istniejący numer, bez nowej numeracji (przykłady: TAU-P26, MEM-M16a, AL-KKT, SERC-H3, TETRA-T16b, DEF-Q4, EXP-E01).

Budowa fazowana, na rozkaz, po ustabilizowaniu semantyki statusów (błąd w tej warstwie powieliłby się w całym rejestrze):

- **Faza 1** (około 40 wpisów): ranking C powyżej plus wszystkie pozycje Wysokie, wraz z powiązanymi testami; testy nie liczą się jako hipotezy.
- **Faza 2**: pozostałe obiekty z korzeni (w tym ❌ domknięte, dla historii falsyfikacji).
- **Faza 3**: seria H-DEF i hipotezy interpretacyjne (z rodzajem twierdzenia i sposobem rozstrzygania); przed fazą 2 audyty pamięci wykonawców.

Audyt źródła (2026-11-26): baza wiedzy zawiera kompletny wykaz obiektów per plik (lustracja 24), więc szkielet rejestru da się z niej wygenerować; pola treść, zakres, predykcja i dowód wymagają powrotu do plików liniowych punktowo, sekcjami, bez pełnej ponownej lektury. Kryterium falsyfikacji uzupełnia właściciel tam, gdzie brakuje go w protokołach.

Kontrola fraz spoza main (2026-11-26): H-ORB-1, H-PIEZO-1, H-COIL-1 nieobecne na main (wyszukiwanie skalibrowane frazami kontrolnymi ORB-05-R, H-SERC-1, AL-H7, wszystkie trafienia pozytywne); status ⏳ do kwalifikacji w audytach. Predykcja lipofilowości (usunięta z rankingu w v1.1; fraza obecna wyłącznie w STAN, brak protokołu i źródła w 24 korzeniach, kontrola 2026-11-27): status ⏳ do kwalifikacji, pochodzenie do rozstrzygnięcia przez właściciela.

**Propozycja do rozkazu (DeepSeek, S1; popiera Claude): snapshot rejestru w repo.** Zasada 1 mówi, że prawda żyje w bazie wiedzy, ale baza wiedzy jest poza repo: audytor czytający tylko repo widzi zamrożoną erę 11cs i obiecuje mu się źródło prawdy, którego nie może sprawdzić. Rozwiązanie: publikacja kuratorowanego snapshota rejestru w repo (np. docs/baza-wiedzy/snapshot/) z jawną datą i SHA-256, aktualizowana przy zamknięciu każdej rundy. Do decyzji właściciela: zakres snapshota (pełny rejestr czy eksport kuratorowany) i częstotliwość.

**Propozycja do rozkazu (Claude): pierwszy krok audytów = kwalifikacja replikacji Lattice.** To jedyny punkt, w którym status ✅ bez 🔍 mógłby się faktycznie pojawić; od jego rozstrzygnięcia zależy, czy bilans „niezależnie zreplikowane" przestanie być zerem.

## Aneks: zasady i legenda (Z2, jawna konwencja)

1. Tabela jest **mapą**, nie źródłem prawdy. Prawda per linia żyje w bazie wiedzy (żywy rejestr roboczy od 2026-11-22) i w pliku linii. Tabela odpowiada na jedno pytanie: **w którym miejscu jest projekt**.
2. Każdy wiersz ma: status, datę ostatniej weryfikacji, następny krok, właściciela. Data weryfikacji przy wierszach oznacza kontrolę mapy i obecności dokumentów, nie ponowną weryfikację treści; metoda zapisana przy dacie: **(mapa)** kontrola obecności dokumentów, **(treść)** pełna lektura, **(replikacja)** powtórzenie rachunku. Daty w sekcji A to daty konkretnej kontroli albo decyzji wpisanej do rejestru bazy wiedzy (bez wspólnego mapowania, bo dotyczą zdarzeń, nie wierszy); wspólna data w sekcji B dotyczy wyłącznie mapowania wierszy B.
3. Dokumenty z epoki 11cs lub starszą to **archiwum**: ich liczby mogą być nieaktualne. Stan sprawdzasz tu i w bazie wiedzy, nie ponowną lekturą całych plików.
4. **Status poznawczy zmienia się na podstawie dowodu formalnego, wyniku testu albo pomiaru zgodnego z ustalonym protokołem, albo niezależnej replikacji. Decyzja właściciela zmienia status organizacyjny i nie zastępuje wyniku poznawczego.**
5. **Status prac i status hipotez są rozdzielone.** Każda hipoteza ma jawny zakres; dziedziczenie statusów nie jest automatyczne (falsyfikacja przypadku szczególnego nie obala ogółu, potwierdzenie szczególnego nie potwierdza ogółu, odrzucenie modelu nie jest falsyfikacją zjawiska).
6. **Dwie daty**: ostatnia weryfikacja (tabela) oraz ostatnia zmiana statusu z powodem (baza wiedzy).
7. **Nowa hipoteza dostaje wpis w rejestrze przy narodzinach**, żeby rejestr nie gnił.
8. **Weryfikacje dotąd wykonane były formalno-matematyczne albo obliczeniowe; żaden z ośmiu protokołów empirycznych nie został wykonany.** Hipotezy interpretacyjne, jeszcze nieoperacjonalizowane, nie są objęte żadnym z tych rodzajów weryfikacji.
9. **Atomowość**: jedna hipoteza to jedno twierdzenie. Kryterium rozbioru jest **pre-registrowane w protokole hipotezy**: koniunkcja (A i B i C) rozpada się na człony, zakres kwantyfikowany (dla x z X) rozpada się po podziale dziedziny X. Rozbiór post-hoc, dobrany po wyniku, jest nieważny. Hipoteza częściowo sfalsyfikowana (np. S12) przy budowie rejestru rozpada się na części: która część ❌, która ⚪, jaki zakres wciąż obowiązuje.
10. **Kwalifikacja przed statusem**: wątek bez ustalonej treści, zakresu i predykcji dostaje status „do kwalifikacji"; nie wiadomo wtedy, co miałoby być replikowane, więc żadnego statusu wyniku mu się nie przypisuje.

### Legenda

Symbole są skrótami. Nie ukrywają trzech wymiarów:

| Wymiar | Wartości |
|---|---|
| Wynik względem hipotezy | wspiera / falsyfikuje / nierozstrzygający / nieprzetestowany |
| Walidacja | jedna ścieżka / wiele metod w jednej sesji / niezależna replikacja |
| Organizacja | aktywna / uśpiona / zamknięta / odrzucona decyzją |

**Status wyniku (poznawczy):**

| Symbol | Znaczenie |
|---|---|
| ✅ | wspiera (w zakresie i z dowodem jawnym) |
| ❌ | falsyfikuje (wynik sprzeczny z konkretną treścią); podtypy: ❌(r) rachunkowa, dotąd jedyna obecna (możliwa do rewizji jak każdy rachunek), i ❌(e) empiryczna, z danych zewnętrznych, cięższa epistemicznie; jeszcze żadna nie powstała |
| ⚪ | nierozstrzygnięta: test wykonany, ale **bez mocy rozstrzygającej**; wynik zgodny z przewidywaniem przy obu wariantach hipotezy (K3: F_r = 0/20 w zakresie typowym niezależnie od tezy), albo rozbieżne replikacje wymagające wyjaśnienia; powód nierozstrzygnięcia zapisany w rekordzie |
| 💡 | nieprzetestowana (brak rozstrzygającego testu) |

**Znacznik walidacji** (doklejany do statusu wyniku, nie samodzielny status):

| Symbol | Znaczenie |
|---|---|
| 🔍 | brak niezależnej replikacji (jedna ścieżka albo wiele metod w jednej sesji); niezależna replikacja zmienia walidację, nie treść twierdzenia |
| brak znacznika | wynik niezależnie zreplikowany |

**Niezależna replikacja** = inny wykonawca, w osobnej sesji, na własnej implementacji (nie ten sam kod, nie ta sama rozmowa), ze zgodnością w granicach bramki tolerancji z protokołu. Wiele metod w jednej sesji to nadal znacznik 🔍; status wyniku nie zależy od liczby metod, tylko od zgodności wyniku z treścią twierdzenia. **Zasada ostrożności:** dopóki warunki definicji nie są potwierdzone dla konkretnego wyniku (kwalifikacja przy budowie rejestru), wynik nosi znacznik 🔍; brak znacznika wymaga potwierdzenia wszystkich czterech warunków.

Dla wyników numerycznych znacznik 🔍 wchodzi do pola zakres („w jednej implementacji"): wynik jednotorowy jest wskazówką, nie wiedzą rejestrową (Z1).

**Status organizacyjny:** ⏸ uśpiona (bez zmiany statusu poznawczego), 🚫 odrzucona lub zamknięta decyzją właściciela (bez twierdzenia o falsyfikacji), 🟢 u właściciela (marker własności, nie status), ⏳ do kwalifikacji (wątek bez ustalonej treści; bez receiptu w repo). **Na hasło** = czeka na sygnał właściciela: bloker decyzyjny, nie hasło techniczne ani dostęp; decyzja konkretnie: w H-DEF wybór symulacji A vs B przed zamrożeniem v1.0 KOMÓRKA.

## Instrukcja obsługi

Żeby sprawdzić stan linii: (1) przeczytaj wiersz tutaj; (2) jeśli data weryfikacji jest starsza niż ostatni wpis bazy wiedzy, rozstrzyga baza wiedzy; (3) pełną lekturę pliku liniowego wykonuje się raz, przy włączaniu linii lub przy podejrzeniu błędu, nie rutynowo. Stan konkretnego obiektu epistemicznego sprawdzasz w rejestrze hipotez (sekcja F), nie w tabeli linii; różnicę między dojrzałością matematyczną a walidacją empiryczną odczytasz z nagłówka i bilansu E.

## Historia wersji

v0.1 szkic mapy (warsztat), v0.2 statusy poznawcze vs organizacyjne (Asterion), v0.3 kryteria porażki, cykl życia, bilans pokrycia (Claude, Asterion), v0.4 model trójwymiarowy wynik, walidacja, organizacja (Asterion), v0.5 bilans w nagłówku, podtypy ❌, warunki odmrożenia (DeepSeek), v0.6 rachunek nagłówka, definicja niezależnej replikacji (Claude), v0.7 spójność końcowa: wersje nagłówków, prerejestracja S12, kwalifikacja replikacji Lattice, definicja ⚪ z powodem, wskaźniki protokołów, pole powodu zmiany statusu (Asterion), v0.8 domknięcie spójności: numerowana lista falsyfikacji, znacznik 🔍 konsekwentnie do czasu kwalifikacji, wstęp rankingu bez sugestii dokonanych falsyfikacji, koszt jako pierwszy etap, zakres liczników jawny (Asterion), v0.9 czytelność dla nowego czytelnika: stan w pigułce w nagłówku, zasady i legenda przeniesione do aneksu, historia wersji na końcu, S12 jawnie poza licznikiem, M18 odsyłacz między liniami, 10 znanych dziś zamiast co najmniej, warunki odmrożenia w wierszach linii (Claude), v0.10 precyzja sformułowań: pigułka nie sugeruje zamknięcia otwartych pytań teoretycznych, pigułkowy licznik 10 zgodny z bilansem E, koszt pozycji 2 rozróżnia pierwszy rachunek i niezależną replikację (Asterion), v1.0 zamrożenie na rozkaz właściciela (Leszek) i publikacja jako docs/STAN.md, treść v0.10 bez zmian merytorycznych. v1.1 erraty na rozkaz właściciela (Leszek) po audytach zewnętrznych rozliczonych niezależną replikacją (Vibe): pozycja 12 E-02 zastąpiona rzeczywistym protokołem (hierarchia czasowa z pierwszymi liczbami, symulacja E1 N=100; predykcja lipofilowości bez źródła w korzeniach, status ⏳ do kwalifikacji), pozycja 11 E-05 koszt E1 (10 000 słów) i dwie gałęzie kryterium, pozycja 3 stabilizator S4 odseparowany od T_h bramek 8/20 (kryterium izomorfizmu), pozycja 1 E-01 zakres K4 jawny (errata kandydacka do samego protokołu zgłoszona właścicielowi), pozycja 2 zawężona do Tw. 7.8.7.2, pozycja 10 algebra i dynamika TETRA rozdzielone, SERC brak walidacji empirycznej, Stalk zakres 56 trójek jawny, pozycje 4 i 5 przeformułowane i rozstrzygnięte dwiema rękami (osie półobrotów, grupa 24 ≅ S4); kandydat lematu AXIS-DEF-01 zapisany w bazie wiedzy do rejestru fazy 1. v1.2 erraty na rozkaz właściciela (Leszek) po drugim audycie zewnętrznym (Asterion), rozliczonym niezależną weryfikacją brzmień protokołów w repo (Vibe): pozycja 1 E-01 kryterium rozszerzone do obu gałęzi protokołu (gałąź fazowa: argument pary zespolonej poza przedziałem wokół 25,77 stopni z marginesem ponad 5 stopni; gałąź rzeczywista: wszystkie wartości własne operatora rundy rzeczywiste, brak pary zespolonej; w skrócie tabeli była dotąd tylko gałąź fazowa), pozycja 12 E-02 kryterium zastąpione operacyjnym brzmieniem protokołu (konfiguracja gładka 32/256 versus pierwsza 29/899, σ = 0,05, okno 20 000 taktów, N = 100, falsyfikacja przy p powyżej 0,05 w teście t-Studenta w co najmniej trzech niezależnych konstrukcjach symulacyjnych), dopisek sprawozdawczy: opis klas grupy 24 skorygowany, raport Vibe liczył elementy według śladów jako 1+6+8+9, klasy sprzężoności to 1+6+8+3+6, dziewięć elementów rzędu 2 dzieli się na klasy 3 i 6 (korekta Asteriona przyjęta). v1.3 erraty na wolną rękę właściciela (Leszek) po audycie v1.2 (Asterion) rozliczonym niezależną weryfikacją verbatim (Vibe): pozycja 12 jednostki skal spójne (τ_Z = 256·τ_L = 8·τ_T i τ_Z = 899·τ_L = 31·τ_T; errata wobec Vibe: transkrypcja v1.2 przypisywała trzeciemu poziomowi jednostkę τ_T, czego w protokole nie ma, konflacja liczby z kroku symulacji z jednostką z predykcji), pozycja 12 semantyka wyniku: p powyżej 0,05 to niepotwierdzenie predykcji, nie automatyczne obalenie, obalenie wymaga testu równoważności lub przedziału ufności wobec prerejestracji, E-02 nieuruchamialne przed prerejestracją (wartość minimalnej istotnej redukcji, sparowanie realizacji szumu, definicja jednostki niezależnej konstrukcji), pozycja 1 rozjazd zakresu usunięty w samym protokole; erraty v0.3.3 pliku Experiments wprowadzone na tej samej podstawie (jednostki E-02 w predykcji i krokach, przeklasyfikowanie p powyżej 0,05, zawężenie predykcji E-01 do K4, przedłużenie na inne grafy z cyklem jako osobna predykcja do zaprojektowania). v1.4 erraty po ponownym audycie (Asterion) na wolnej ręce właściciela: errata v0.3.4 pliku Experiments ujednolica zakres E-01 w całym protokole (hipoteza i warunek falsyfikacji zawężone do K4, zgodnie z rekomendacją audytu) i doprecyzowuje jednostkę analizy E-02 (niezależna realizacja symulacji, pseudoreplikacja wykluczona); errata redakcyjna wiersza 12: trzy niezależne konstrukcje to wymóg protokołu, nie pełna replikacja Z1 z aneksu; decyzja świadoma: nazwa pliku Experiments pozostaje P0_Experiments_v0_3_2.md dla stabilności odnośników, wersja treści jawna w Status korekty i stopce; E-02 pozostaje zablokowane do prerejestracji (decyzje właściciela: minimalna istotna redukcja, sparowanie realizacji szumu, definicja jednostki niezależnej konstrukcji). v1.5 aktualizacja po wykonaniu E-01 (2026-11-28, rozkaz właściciela, pierwszy protokół Experiments wykonany kiedykolwiek): widmo pełnej rundy GS na K4 = {1; 0,1347106; 0,153348 ± 0,074039i}, rachunek niezależny Vibe (wielomian charakterystyczny 256λ⁴ − 369λ³ + 131λ² − 19λ + 1 Newtonem na liczbach całkowitych, pierwiastki bisekcją z deflacją do kwadratu, kontrola krzyżowa iteracją QR, tożsamość 256R⁵ = (5R−I)⁴ z residuum zero, widmo niezależne od kolejności podsystemów), argument pary 25,7721°, odchylenie od 25,77° równe 0,0021°, obie gałęzie falsyfikacji nie spełnione, hipoteza nie sfalsyfikowana, predykcja potwierdzona numerycznie (🔍), licznik protokołów 0/8 do 1/8; errata kandydacka do protokołu spójności cyfr rozliczona: errata v0.3.5 wprowadzona 2026-11-28 (hipoteza rozdziela fazę z zaokrąglonych współczynników 25,811° od fazy dokładnego widma 25,772°, obie wewnątrz marginesu 5°); kontrola porównawcza Asterion (rekonstrukcja z raportu, potwierdzenie R, wielomianu i pierwiastków co do cyfry) odnotowana, nie jest pełną replikacją Z1, status 🔍 utrzymany; niezależność widma od kolejności sprawdzona rachunkowo dla wszystkich 24 permutacji (identyczny wielomian charakterystyczny, arytmetyka całkowita), jednotorowo, do walidacji Z1 przy okazji rejestru.