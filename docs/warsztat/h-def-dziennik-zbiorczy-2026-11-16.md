# Dziennik laboratoryjny P0 — seria H-DEF (zbiorczo), stan na 2026-11-16

Statusy: ✅ pewne (rachunek/twierdzenie) · 🔍 wynik numeryczny w konkretnym modelu · 💡 hipoteza/interpretacja · ❌ obalone

| ID | Wynik | Status |
|---|---|---|
| H-DEF-1 | Pierścień 5K₄ (abelowy): szczelina δ = 2π − 5·arccos(1/3) = 7,3561°. Σe = 2πw − 5θ zachowane tożsamościowo; ładunkiem jest nawinięcie w (sektory k, 41% przebiegów z losowego startu utknęło w k ≠ 0). Koszt zapadnięcia rośnie z ε (E/E_min ≈ 60 przy ε=0,1; ≈1 poniżej 1e-4). Brak histerezy przy jednym progu. | ✅ 🔍 |
| H-DEF-2 | Odkształcenie sprężyste: E_min = δ²/(2N)·k/(1+k). Plastyczne: kąt → 72°, defekt znika. Trwałość = wyścig plastyczności z zapadaniem. | 🔍 💡 |
| H-DEF-5 | ρₙ₊₁ = c·ρₙ; c = (ścieżki kąta)/(ścieżki ramek): A c=1 płasko, B c=1/3 miękko (kąt → 72°), C c=3 sztywnieje. Liczby ścieżek założone, nie wyprowadzone. | 💡 |
| H-DEF-5b–d | Model sprężynowy 3D: kąt przy wspólnej krawędzi = 72° z konieczności (nie jest obserwablem); energia na czworościan nasyca się (5,07e-4), addytywność; wspólny wierzchołek 0, wspólna krawędź −1,5%/krawędź. | 🔍 |
| H-DEF-6 | Łatwość uśredniania λ₂ pary: ściana 1,043 / krawędź 0,789 / wierzchołek 0,448; łańcuchy λ₂ ∝ m^(−1,9…−2) (dyfuzja). | 🔍 |
| H-DEF-7 | Układ 1+8 ikosaedrów (cube): 93 węzły, 180 czworościanów, bez przenikania; dwa dualne K₄ wokół P₀; 12 styków wierzchołkowych; E −4,1% względem sumy (z 8 styków ścian); λ₂=0,579. | ✅ 🔍 |
| H-DEF-8 | K₄ = gwiazda + trójkąt; L_gwiazda/L_trójkąt = sin72° = 0,9511 niezależnie od sztywności; odkształcenie bierze miększy kanał. | 🔍 💡 |
| H-DEF-9 | Tetrahelisa BC: skręt 131,8103°, przesunięcie 0,3162; reszta domknięcia r = Nθ − 2πm (N=30: −5,69°; 71: −1,47°; 254: −0,18°); w ℝ⁴ E≈1e-17 (ikosaedr+środek; pierścienie N=30,31). | ✅ 🔍 |
| H-DEF-10 | Rozgałęzienia ×3: w ℝ³ pierwsza kolizja przy n=6 (3/81 = pierścień 5); c₁₁=15438, stosunek ≈2,86; pełne drzewo mieści się do poziomu 2 (17 czworościanów). | 🔍 |
| H-DEF-11 | Płaska sieć czworościenna: średnio 360°/70,53° = 5,104 K₄ na krawędź; 10,4% krawędzi 6-krotnych; defekt 6-krotny kompensuje 8,59 pięciokrotnych. | ✅ |
| H-DEF-12 | Zamknięta powierzchnia (sfera): Σ(6−z)=12; defekty migrują i anihilują parami, ładunek stały; otwarty płat: ładunek ucieka brzegiem. Ładunek = 12(1−g). | ✅ 🔍 |
| H-DEF-13/14 | 600-komórkowiec: 120 wierzchołków, 600 komórek, 5 na krawędź, figura wierzchołkowa = ikosaedr; łańcuch BC zamyka się po 30, T = obrót (12°, 132°), T³⁰=I; 131,81° vs 132° × 30 = 5,69°. Pierścień leży na torusie o promieniach² 0,103/0,897, **nie** na torusie Clifforda (korekta). Przypisanie (użytkownik): ikosaedr = sfera, pętla K₄ = torus. | ✅ 💡 |
| H-DEF-4 | Nieprzemienność (SO(3)), 2026-11-16: patrz niżej. | 🔍 |

## H-DEF-4 (2026-11-16) — holonomia nieprzemienna gwiazdy ikosaedru

Model: 12 pierścieni 5 czworościanów wokół promieni gwiazdy; holonomia każdego = rotacja o δ = 7,3561° wokół osi wierzchołka ikosaedru (12 osi, orientacja na zewnątrz).

- Złożenie dwóch pętli: osie 63,43° → kąt 12,51° (suma abelowa 14,71°); osie 116,57° → 7,73°; osie antypodyczne → 0 (znoszą się dokładnie).
- Komutator [g_i, g_j] (osie sąsiednie): 0,844° (≈0,115 δ; drugi rząd).
- Iloczyn wszystkich 12 w losowych kolejnościach (20 000): kąt całkowitej holonomii 0–6,13° (mediana 1,54°), zależny od kolejności; suma wektorów δ·uᵢ = 0 (cancellation pierwszego rzędu), zamiast naiwnego 88,3°.
- Najmniejszy niezerowy kąt słów długości ≤ 4: 0,844° (komutator); 276 słów długości 4 daje tożsamość.
- Model sprężynowy 3D: E(klaster) = 0,01055 vs niezależne pierścienie 12 × 0,00032 = 0,00384 → ×2,75 (frustracje wzmacniają się, choć kąty holonomii się częściowo znoszą — napięcie do rozstrzygnięcia).

Wniosek: model abelowy nie wystarcza. Niezmiennikiem jest holonomia pętli (klasa sprzężenia, niezmiennik cechowania), a nie suma kątów; „ładunek całkowity" zależy od kolejności.
Ograniczenia: holonomie liczone z geometrii sztywnych foremnych czworościanów (bez dynamiki relaksacji); porównanie energii 2,75× przy założeniu niezależnych pierścieni jest przybliżeniem (krawędzie współdzielone).

Otwarte: histogram K₄ na krawędź w prototypie (5/6/7?); wpływ na E dynamiki kolejności zapadania w SO(3); weryfikacja przez inne modele: tożsamość Σe = 2πw − Nθ, wzór E_min, wartości w tabeli H-DEF-4.

## H-DEF-15 (2026-11-16) — histogram K₄ na krawędź bez prototypu

Brak prototypu użytkownika ⇒ histogram wyznaczony na własnych konstrukcjach.
- 1 ikosaedr + środek: 42 krawędzie: 30 × 2 K₄ (krawędzie zewnętrzne, nie tworzą pierścienia), 12 × 5 K₄ (pierścienie zamknięte).
- Układ 1+8: 354 krawędzie: 222 × 2, 24 × 4 (otwarte wachlarze), 108 × 5 (wszystkie zamknięte pierścienie; 108 = 9 × 12). Brak krawędzi 6-krotnych ⇒ brak ładunku ujemnego w tej rodzinie sieci.
- Domknięcie samopodobne (każdy węzeł środkiem własnej gwiazdy ikosaedralnej) ⇒ 600-komórkowiec: V=120, E=720, F=1200, C=600, χ=0; każda krawędź ma 5 K₄; średnica 5, λ₂ = 2,2918 (globalne uśrednianie szybkie i skończone, w przeciwieństwie do łańcuchów ∝ m²).
Wniosek: kompensacja ładunkiem ujemnym (krawędzie 6-krotne, 5,104 średnio) jest niedostępna w tej rodzinie; zostają przemieszczenie, rozłożenie sprężyste, rozpuszczenie plastyczne i domknięcie topologiczne (S³). Hipoteza (💡): reguła „węzeł = środek własnej gwiazdy na niższym poziomie” ⇒ 600-komórkowiec.

## H-DEF-16 (2026-11-16) — poziomy bez wspólnych węzłów: ℝ⁴ i „przeciek” między poziomami

Dana od użytkownika: poziomy nie mają wspólnych węzłów ⇒ hipoteza H-DEF-15 (węzeł = środek własnej gwiazdy ⇒ 600-komórkowiec jako globalne domknięcie P₀) odrzucona jako model P₀ (❌); 600-komórkowiec zostaje wyłącznie jako odniesienie geometryczne (lokalna gwiazda i helisa są jego fragmentami).
- Układ 1+8 (93 węzły, 180 K₄, krawędzie jednostkowe): ℝ³ E = 0,09109; ℝ⁴ E ≈ 1e-17 dla wszystkich 256 wzorców znaków podniesienia środków (🔍). Cały defekt tego poziomu znika z jednym dodatkowym wymiarem; uwaga: ℝ⁴ jest dla tego grafu bardzo permisywne, więc to słabe ograniczenie.
- Przeciek między poziomami: relaksacja napięcia niższego poziomu zmienia odległości P₀–P₀ wyższego o +1,48% jednakowo (środek–sąsiedzi 1,5115 → 1,5339; krawędzie sześcianu 1,7454 → 1,7712); promień gwiazdy 0,9511 → 0,9712. Kształt (sześcian) zachowany z symetrii Th, zmienia się tylko skala (🔍; „tylko skala” wynika częściowo z symetrii). 💡 Konflikt poziomu n widać na n+1 jako zmianę skali, nie kształtu.
- Otwarte: czy P₀ przekazuje wyżej tylko położenie (średnią), czy też holonomię/napięcie.

## H-DEF-17 (2026-11-16) — scenariusz „węzły poziomów się nakładają” (wariant do testowania, nie stan faktyczny)

Użytkownik nie wie, czy węzły poziomów mogą się nałożyć ani czy P₀ przekazuje wyżej tylko położenie czy też napięcie/holonomię. Oba punkty traktowane jako otwarte aksjomaty; baza robocza: poziomy rozłączne.
- Nałożenie (węzeł = środek własnej gwiazdy i wierzchołek wyższej) ⇒ 600-komórkowiec (120 węzłów, 720 krawędzi, χ=0, średnica 5): wszystkie 720/720 krawędzi to zamknięte pierścienie 5 (w układach rozłącznych ok. 30%: 12/42, 108/354); strukturalnie brak napięcia (E≈2e-24 w ℝ⁴/S³), ale po wciśnięciu w ℝ³ E = 7,534 (0,01046 na krawędź, ok. 42× więcej niż 0,00025 na krawędź dla ikosaedru ze środkiem); λ₂ = 2,29 ⇒ globalne uśrednianie szybkie i skończone ⇒ teza „globalnie nigdy” fałszywa wewnętrznie (artefakt osadzenia). (🔍; wartość E(ℝ³) = najlepsza z 12 startów, górne ograniczenie)
- Przekaz wyżej: wariant A (tylko położenie) = zmiana skali +1,48% (H-DEF-16). Wariant B (też holonomia) = do każdej pętli wyższego poziomu dochodzi zależna od kolejności rotacja resztkowa niższego poziomu: mediana 1,54°, maks. 6,13° (≈0,21 δ i 0,83 δ, δ=7,36°; z H-DEF-4) (💡 oszacowanie).

## H-DEF-18 (2026-11-16) — decyzja użytkownika: nałożenie węzłów poziomów = błąd

Reguła (użytkownik): wierzchołek jednego ikosaedru jako środek drugiego jest błędem konfiguracji; poziomy mają rozłączne węzły (z H-DEF-16 ta rozłączność przestaje być bazą roboczą, a staje się aksjomatem).
Skutki: scenariusz 600-komórkowca (H-DEF-15/17) wykluczony jako model P₀ (zostaje geometrycznym odniesieniem); teza „globalnie nigdy” spójna z aksjomatem. Otwarte: przekaz wyżej (A: położenie → +1,48% skali; B: także holonomia → rotacja resztkowa 1,5° mediana, 6,1° maks.).
Następny rachunek (do wykonania na hasło): dwupoziomowa symulacja A kontra B, gdzie węzły wyższego poziomu to uśrednione środki klastrów niższego.

## H-DEF-19 (2026-11-16) — dwa poziomy, przekaz A kontra B (wersja holonomiczna)

Model (zabawkowy, jawne założenia): pętla 5 jednostek poziomu wyższego ma z samopodobieństwa holonomię δ = 7,3561° wokół osi pierścienia; reszty niższego poziomu pochodzą z puli H-DEF-4 (iloczyn 12 obrotów w losowej kolejności: mediana 1,55°, maks. 6,19°), z losową orientacją względem osi. Nie jest to dynamika uśredniania, tylko rachunek holonomii (dynamika = otwarte).
- A (tylko położenie): kąt pętli = δ dokładnie (+1,48% skali nie zmienia kątów).
- B-węzeł (reszta = przesunięcie ramki węzła): kąt pętli = δ z dokładnością 1e-10 (to cechowanie: sprzężenie znosi się na pętli) ⇒ brak efektu. (✅ rachunek analityczny + 🔍 numerycznie)
- B-krawędź (reszta dołączona do transportu przez jednostkę, zależna od drogi): 1 reszta/krok × 5: kąt mediana 8,10° (5–95%: 4,43–12,01°), E_B/E_A mediana 1,21 (0,36–2,66); 3 reszty/krok: kąt 9,54° (4,05–15,78°), E_B/E_A 1,68 (0,30–4,60); P(E_B < 0,5 E_A) = 0,10. (🔍 przy założeniach)
Wniosek: o wpływie niższego poziomu na wyższy rozstrzyga to, czy reszta jest własnością węzła (orientacja, cechowanie, brak efektu), czy transportu przez jednostkę (zależy od drogi; łamie samopodobność, defekt wyższego poziomu staje się rozmytą wersją niższego i bywa częściowo zneutralizowany).

## H-DEF-20 (2026-11-16) — rozdzielenie P₀ właściwego i „fałszywego” (zmiana terminologii)

Rozróżnienie (użytkownik): P₀ właściwe = punkt w środku K₄ (średnia jego 4 wierzchołków); P₀ w środku ikosaedru = „fałszywe”.
Geometria (ikosaedr z krawędzią 1, 🔍): 20 prawdziwych P₀ (środki ciężkości 20 K₄) leży w odległości 0,5668 od środka O i tworzy dodekaedr; graf sąsiedztwa K₄ (wspólna ściana) = graf dodekaedru: stopień 3, 30 krawędzi, rozkład odległości od jednego K₄: 1, 3, 6, 6, 3, 1 (średnica 5); odległość między sąsiednimi prawdziwymi P₀ 0,4045. Średnia 20 prawdziwych P₀ = O (z symetrii) ⇒ O jest P₀ drugiego rzędu (💡 interpretacja do potwierdzenia). Droga „przez 4 K₄” = 3 kroki: łączy K₄ z 6 z 20; przeciwległy wymaga 5 kroków (6 K₄).
Skutki dla wcześniejszych wpisów: H-DEF-1…19 (energie, holonomie) bez zmian (O to zwykły węzeł grafu); do korekty interpretacji: (a) H-DEF-7 („centralny ikosaedr = P₀ dwóch dualnych K₄”): centroid czworościanu środków sąsiadów leży pozycyjnie w O centralnego ikosaedru, ale to dwa różne obiekty (prawdziwe P₀ wyższego K₄ kontra fałszywe P₀ ikosaedru); (b) H-DEF-16/19 („jedna orientacja P₀ jednostki”): jednostka ma 20 prawdziwych P₀, więc B-węzeł jako „jedna orientacja jednostki” nie ma zastosowania; transport przez ikosaedr to ścieżka po grafie dodekaedru ⇒ bliżej B-krawędź.
Otwarte: co jest węzłem wyższego poziomu (O, jeden z 20 prawdziwych P₀, albo inny obiekt).

## H-DEF-21 (2026-11-17) — P₀ orbituje w ikosaedrze (nie może być w 20 miejscach naraz)

Dana (użytkownik): P₀ nie może być jednocześnie w 20 miejscach ikosaedru przez brak dopełnienia (odczytane: kątowego, tj. szczelina δ = 7,3561°); P₀ powinno w nim orbitować. (Odczyt „kątowego” do potwierdzenia.)
- Orbita = zamknięta droga po grafie dodekaedru prawdziwych P₀ (H-DEF-20). 12 ścian pięciokątnych dodekaedru = 12 pierścieni 5 K₄ wokół promieni gwiazdy; obieg jednego pierścienia wraca obrócony o δ = 7,3561° wokół osi promienia (precesja, liczba obrotu δ/360 = 0,020434; 360/δ = 48,94). Bliskie domknięcia: 49 obiegów (reszta +0,449°), 783 (−0,171°), 1615 (+0,107°), 2398 (−0,065°); dokładnie nigdy. (🔍)
- Pętle obejmujące więcej pierścieni precesują inaczej (z H-DEF-4): dwa sąsiednie 12,51°, dwa o osiach 116,57° 7,73°, antypodyczne 0 (g_i·g_{−i} = I dokładnie). (✅/🔍)
- Reguła „zębatkowa” (po wierzchołkach; w drugim takcie wierzchołek i jego antypod jednocześnie): para antypodyczna znosi holonomię dokładnie, więc cały cykl 6 par daje tożsamość niezależnie od kolejności par, wobec 0–6,13° (mediana 1,55°) dla przypadkowych kolejności pojedynczych obrotów. 💡 Zgodne z regułą antypodów; związek (aktualizacja kontra holonomia) jest hipotezą.
- O (fałszywe P₀) = styk 12 linii defektu; tam skupia się nieprzemienna reszta holonomii. 💡
Otwarte: odczyt „dopełnienia”; czy orbita = obieg pierścienia 5 K₄, czy dowolna zamknięta droga.
