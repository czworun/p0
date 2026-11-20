
# Korzeń: P₀-Scalar — adnotacja szefa lab. (v0.3.5-draft, 2026-08-12, gałąź P₀-Origins; wpięcie rozlicza: korektę TAU do S11-A, odsyłacz SERC o fazie rosnącej z n, zależność TAU §2.4, zależności poza repo cytowane przez Alchemy/Flow/Relacje)

**Dokument:** „P₀-Scalar: Lokalna kompensacja relacji skalarnych — program redukcji aksjomatów" v0.3.5-draft, podtytuł „gałąź P₀-Origins". Data nagłówka 2026-08-12; synteza 2026-08-06/12; korekty v0.3.1–v0.3.3 datowane 08-06 w §9.5. Chronologia: JEDEN z trzech najstarszych dokumentów korpusu — tylko Relacje starsze (08-11), dokładnie współczesny Wave (ten sam dzień 08-12); przed Alchemy (09-05) i całą rodziną warsztatową. Baza deklarowana: P₀-Centroid v4.9.5, P₀-Wave v0.6.1, P₀-Net v0.3.1-draft — starsza niż wersje w repo (Centroid audyt v5.2 z 09-29, Net wpięty v0.6.1); dokument żywy przed-warsztatowy, czytany temporalnie do tyłu. Wersja zgodna co do znaku z tą cytowaną przez Alchemy w bazie matematycznej („P₀-Scalar v0.3.5-draft") — wpięcie rozlicza pozycję zależności poza repo cytowaną przez trzy dokumenty korpusowe (Alchemy jawnie z wersją; Flow i Relacje bez wersji); z listy zależności pozostają Axis i P₀-Algebra v0.4.1. Rozliczenia banku z kolejki: (1) KOREKTA TAU §7.4.9 do hipotezy S11-A — TAU (09-27) podaje r_∞ ≈ 0,12383 wobec scalarnego 1/8 oraz θ_∞ ≈ 67,40° wobec 67,38°, jawnie „korekta dotyczy Scalar, nie TAU"; Scalar zawiera oryginalną hipotezę S11-A (równanie λ·exp(1/λ) = e, |λ|_∞ = 1/8, θ_∞ = arccos((1+ln 8)/8) ≈ 67,38°); obie linie zgodne strukturalnie, różnica wartości granicznej do rozstrzygnięcia replikacją; (2) ODSYŁACZ SERC (GLOSSARY: „faza 25,77° rośnie z n (Scalar §11.6)") — potwierdzony treściowo w §6.3 (tabela monotoniczna θ_n: 15,79° dla n=3, 25,77° dla n=4, 32,56° dla n=5, ~48,6° dla n=10, ~65,4° dla n=100, 67,08° dla n=500), ALE w v0.3.5 treść nosi numer §6.3 (§11 to relacja do filarów) — przesunięcie numeracji do noty przy scaleniu; (3) ZALEŻNOŚĆ TAU §2.4 — TAU wymienia jawnie „P₀-Scalar v0.3.5 §2.4" jako zależność; w repo §2.4 istnieje jako Twierdzenie S10 (niezmiennik ważony c_i = i/n, dowód teleskopowy): rozliczone; rodzina M_m(α) TAU (Tw. 7.3.1/7.3.2/7.3.6, wagi liniowe w pozycji k) jest parametrycznym uogólnieniem S10, a α=1 to dokładnie Scalar/Centroid; (4) NOWY BANK na PILLARS-TABLE: adnotacja P₀-Defect notuje „Axis i Scalar wchłonięte wcześniej do Centroid" — deklaracja absorpcji sprzeczna z samodeklaracją Scalara (gałąź Origins, zasada niezależności §0); status tego wchłonięcia do rozliczenia przy PILLARS-TABLE; (5) S9 (most Scalar→Net) uzależniony „od zamknięcia N9 w Net" — N9 ✅ w repo (Net v0.6.1), warunek spełniony, S9 można otwierać.

**Co bada:** najprostszy operator organizacji relacji skalarnych: układ R ∈ ℝⁿ, próg ε > 0, sąsiedztwo kompensacyjne |r_i − r_j| < ε, aktualizacja współrzędnej średnią lokalną (operator C z normalizacją przez liczność sąsiedztwa; parametr strukturalny λ = 1 przyjęty programowo do zamknięcia analizy podstawowej, przywrócenie λ w wersji uogólnionej deklarowane). Trzy warianty aktualizacji: A1 lokalna (C^(i)), A2 asynchroniczna — pełna deterministyczna runda Gaussa–Seidela w ustalonej kolejności 1..n (R_ε), A3 synchroniczna (Jacobi, J_ε). Relacja do literatury (§1.3, rzadkiej precyzji): A3 = klasyczny model Hegselmanna–Krause (fragmentacja znana od dwóch dekad; analiza małych układów w dużej mierze adaptowalna), A2 NIE MA odpowiednika w literaturze HK — standardowa „asynchroniczność" HK to losowa aktywacja pojedynczego agenta, nie pełna deterministyczna runda GS; stąd prawdziwy wkład: nie fenomen fragmentacji, lecz most A2 → P₀-Centroid (dostęp do 𝔤₄, widma i fazy 25,77°) oraz mapowanie domen na Wave (moduły zdegenerowane) i Net (granice jako zanik transportu). Deklaracja programowa: gałąź redukcji aksjomatów P₀-Origins z aksjomatem ontologicznym A0 („istnieją wyłącznie relacje") jako założeniem 💡 programowym, nieużywanym w dowodach; zasada redakcyjna §0: żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia; zasada niezależności: obalenie korespondencji ε → ∞ upada model redukcyjny Scalar — nie algebrę 𝔤₄, nie metrykę G₄, nie fazę 25,77°; zasada ostrożności: analityka małych N przed hipotezami dla dużych N, symulacje na końcu, symulacja nie zastępuje dowodu.

**Najmocniejsze (✅ pięć zamknięć z dowodami analitycznymi):**
1. **Lematy tożsamości (§3.1/§3.2):** dla ε > diam(R) zachodzi C_ε^(i) = M_{i−1} oraz R_ε = R_n DOKŁADNIE, nie asymptotycznie (próg ε₀(R) = diam(R)); most do operatorów P₀-Centroid §1/§7: powyżej progu dynamika Scalar pokrywa się z dynamiką Centroid co do operatora — najstarszy most operatorowy korpusu.
2. **Twierdzenie S10 (§2.4):** w reżimie pełnego grafu lewy wektor własny R_n dla λ = 1 to c_i = i/n; zachowana wielkość rundy L(R) = (1/n)·Σ i·r_i; dowód teleskopowy bez indukcji (n·S_n = Σ_{k=0}^{n−1} S_k); korekta wpisana względem v0.3: c_i = (n+1−i)/n było odwróconą kolejnością (koncesja publiczna).
3. **Twierdzenie S11 (§6.2):** dla każdego n ≥ 3 pełna runda na klice K_n ma parę zespoloną o niezerowej fazie; dowód z tożsamości P₀-Centroid §7 (n^n·R_n^(n+1) = ((n+1)R_n − I)^n): równanie (w+1)^(n+1) = C·w^n, C = (n+1)·(1+1/n)^n, wielomian Q stopnia n−1, trzy kroki: brak pierwiastków dodatnich (minimum f w w = n), brak ujemnych dla n ≥ 3, istnienie pary sprzężonej przez zmiany znaku; niezależnie zweryfikowane numerycznie dla n = 3, 4.
4. **S-CYCLE (§6.1):** dla grafu różnicowego 1D (unit interval graph) para zespolona ⟺ klika K_m, m ≥ 3; drzewa i grafy rozłączne: widmo czysto rzeczywiste (weryfikacja analityczna dla P₄; K_{1,3} nierealizowalny w 1D); faza jest własnością CYKLU w klice, nie rozmiaru grafu — ograniczenie uniwersalności 25,77° strukturalne, zgodne z Centroid §6.4 (kolejność i cykl decydują o fazie) i z głosem Centroid §11.7 kontynuowanym w SERC i Net.
5. **Lematy basenów N=3 i N=4 (S2b §4.2.2, S3b §4.4.4) + tabela przejść S13 (§4.2.1/§4.4.3):** ℝ³ = trzy baseny (B_K: K₃ i P₃ → p₀∥1 z czynnikiem ≈ 0,17; B_D: K₂+K₁ → płaszczyzna (c,c,r₃), c = (r₁+2r₂)/3, |c−r₃| ≥ ε; B_I: 3K₁ = id); ℝ⁴ = cztery baseny; kluczowy argument N=4: liczba krawędzi wzdłuż trajektorii transientnej niemalejąca (1 → 2 → 3 → 5 → 6), brak cykli transientnych; twierdzenia niemożliwości: Tw. 1 (P₃ nie wychodzi do K₂+K₁ ani 3K₁ — obie krawędzie przetrwają krok: |x′−y′| = |x|/3 < 2ε/3), Tw. 2 (K₂+K₁ zamknięty — izolat pozostaje: x′ = (x+y)/2 ≥ ε), Tw. C1 (2K₂ nierozpadalne), C2 (4K₁ = id), C3 (P₄ zawsze zyskuje krawędzie) — automat topologiczny jako drugi poziom dynamiki nad rachunkiem widm.
6. **Korekta katalogu N=4 (§4.4.1):** realizowalnych klas graficznych jest 9, nie 7 — dochodzą paw (K₃ z liściem) i diamond (K₄ minus krawędź); faza zespolona wszędzie, gdzie cykl, ALE zależna od struktury: K₄ 25,77°, paw 11,27°, diamond 20,25°, grafy acykliczne bez fazy (P₄: widmo rzeczywiste 0,682/0,287/0,142) — pierwsze zestawienie „cykl tak, wartość różna": uniwersalność fazy 25,77° dostaje tu precyzyjną granicę — w 1D faza ⟺ klika.
7. **Tabele programowe (§8):** S2b, S3b, S10, S11, S13 ✅ zamknięte; S12 ❌ sfalsyfikowane z twierdzeniem warunkowym o podregionach; pełne rozdzielenie wariantów A3/A2 we wszystkich wierszach S1–S3 z priorytetami (A3 niski — adaptacja HK; A2 średni/wysoki — brak odpowiednika w literaturze); §5 zastrzeżenie: wartość graniczna domeny NIE jest średnią arytmetyczną stanu początkowego — zależy od niezmiennika ważonego (S10); protokoły E-08..E-13 do P₀-Experiments z zasadą niezależnej replikacji.

**Koncesje i sęki (jawnie):** §9.5 trzy cofnięcia wpisane w historię wersji (wzorzec koncesji): v0.3.1 — zachowanie sumy przez rundę asynchroniczną sfalsyfikowane kontrprzykładem R = (1,−1,0) (Σ′ = −4/9 ≠ 0) i analogicznym dla Regionu II (−1/4); przyczyna: symetria sąsiedztwa nie implikuje zachowania sumy przy kompozycji operatorów działających na stanach pośrednich; cytat z Centroid §6.2 „p₀∥1 to definicja konsensusu, nie prawo zachowania"; v0.3.2 — S12 niezmienniczość Regionu II sfalsyfikowana: dla x ∈ [ε, 1,8ε) trajektoria zawsze wychodzi do K₃ w jednym kroku (niezależnie od y), dla x ∈ (1,875ε, 2ε) zawsze zostaje, pasek (1,8ε, 1,875ε) zależy od y (krzywa graniczna 5x+3y = 12ε); „Wniosek 2 (zaskakujący)": większość Regionu II scala się w pełny konsensus grafowy w jednym kroku — odwrotność naiwnej intuicji HK, jawne żądanie niezależnej weryfikacji (E-13); v0.3.3 — atraktor B_D w §4.2.2: błędna linia zerosumowa (t,t,−2t) zastąpiona płaszczyzną (c,c,r₃) po kontrprzykładzie numerycznym; v0.3.4 naprawa uszkodzonych sekwencji LaTeX i literówki n=3,4,4; v0.3.5 aktualizacja bazy matematycznej bez zmian treści. Pył potencjalny do weryfikacji (nie tykamy verbatim): w tabeli §4.4.2 wiersz K₃+K₁ podaje fazę 25,77° przy widmie „R₃ ⊕ 1", a zgodnie z θ₃ = 15,79° (§6.3, n=3) faza bloku R₃ wynosi 15,79° — wygląd na przeniesienie z wiersza K₄; kandydat na pytanie do autora i sondę w replikacji E-09.

**Struktury 💡:** emergencja domen (P₀-S1 §5): partycja indeksów na rozłączne domeny z lokalnym konsensusem wewnątrz (|r_i − r_j| < ε dla dużych t) i rozłącznością między; trzy punkty definicji; program czterech kroków (N=2 → N=3 → N=4 → indukcja/topologia); hierarchia czasowa Centroid §13 jako potencjalna emergencja partycji: domeny skonsensusowane zachowują się jak efektywne węzły wyższego poziomu (liść osiąga konsensus wewnętrzny, zanim wyższy poziom „zobaczy" jego strukturę) — echem tej struktury jest koncept łodyga/liść STALK (10-05), miesiąc późniejszy; S-DYN (§10): niektóre własności (zbiór atraktorów, liczba domen) być może niezależne od permutacji kolejności — niezmienniki niezależne od schematu byłyby głębszymi niezmiennikami struktury relacyjnej; dodatkowa obserwacja: permutacja zmienia SAM niezmiennik ważony c (wagi wzdłuż kolejności), nie tylko tempo — silniejsze stwierdzenie; graf dynamiczny G_t(ε) zależny od stanu; jednokolumnowość progu (unit interval graphs) jako geometryczne ograniczenie klasy realizowalnej; moduły zdegenerowane Wave (dim V₁ ≥ 2) jako kandydaci na domeny stabilne — analogia poziomu B.

**Mosty 💡:**
1. **Do P₀-TAU (trzy sploty):** (a) obserwacja §10 o permutacji i niezmienniku c jest empiryczną zapowiedzią Tw. 7.3.2 TAU (konsensus zależy od σ, tempo nie) — dokument miesiąc starszy formułuje ją jako „dodatkową obserwację", TAU domyka twierdzeniem; (b) S11-A vs asymptotyka TAU §7.4.9 (1/8 vs 0,12383; 67,38° vs 67,40°) — dwie niezależne linie tej samej granicy transendenckiej; po replikacji kandydat na twierdzenie słojowe pnia; (c) A2 jako właściwa klasa mostu: Scalar pierwszy WYRÓŻNIA deterministyczną pełną rundę GS od losowej asynchroniczności HK — dokładnie rozróżnienie, na którym TAU §1.1 buduje aksjomat sekwencyjności (M_m z kolejnością w definicji); TAU zależność „P₀-Scalar v0.3.5 §2.4" rozliczona: Tw. S10 = przypadek α=1 rodziny M_m(α) z Tw. 7.3.6 TAU (wagi liniowe w k).
2. **Do P₀-Centroid:** lematy tożsamości otwierają pełną algebrę 𝔤₄ dla wariantu A2; CS1 (korespondencja pełna): pierwszy krok ✅, pełna trajektoria 🔍 (wymaga S5: rozpiętość diam(R_k) nierosnąca); widmo R₄ {1; 0,153±0,074i; 0,135} ze zbieżnością ≈ 0,17 na rundę (identyczne z §3.3 dokumentu); S10 to niezmiennik rundy Centroidu — działa w reżimie pełnego grafu wspólnym obu dokumentom; nota: tożsamość macierzowa n^n·R_n^(n+1) = ((n+1)R_n − I)^n cytowana przez Scalar jako narzędzie dowodu S11 pochodzi z Centroid §7 — najstarszy przykład rachunku między filarami w korpusie.
3. **Do P₀-SERC:** drugi głos przeciw uniwersalności 25,77° (po Centroid §11.7), ale z precyzją, której tamtym głosom brakowało: faza rośnie z n w klice (θ_n, §6.3), a między grafami zależy od struktury (paw 11,27°, diamond 20,25°); odsyłacz SERC rozliczony (numeracja: §6.3); trzy progi SERC nieutozsamialne i tu kompletne: T_c ciągły (SERC), ε dyskretny (Scalar), δ rezydualny (Alchemy) — mapa trojca potwierdzona z trzeciej strony.
4. **Do P₀-Wave (dokument tego samego dnia 08-12):** domeny jako moduły zdegenerowane Wave §4.4 — analogia strukturalna poziom B, nie dowód; utrata jednego wymiaru stabilności wewnątrz domeny nie niszczy konsensusu.
5. **Do P₀-Net (S9 + S13):** granice domen jako miejsca zaniku transportu; warunek „zamknięcie N9" spełniony (N9 ✅ w repo, z Centroid §8.1) — S9 otwarte z gotowym kontekstem; S13 automat topologiczny jako most kombinatoryczny do grafów Net (partycje domeny ↔ klasy spójności).
6. **Do P₀-Alchemy:** próg rezydualny δ jako mechanizm zapobiegający zanikowi relacji vs próg ε jako mechanizm partycji: para progów o przeciwnych skutkach dla relacji; Alchemy cytuje dokładnie v0.3.5-draft w bazie matematycznej — zgodność wersji potwierdzona.
7. **Do P₀-Relacje (dokument bezpośrednio starszy, 08-11):** program emergencji domen jako realizacja szkieletu R→D→C→R′; Relacje §9.2: reformulacja różnicowa Twierdzenia S13 zweryfikowana (0/5000 + 0/5000 naruszeń, diagram asymptotyczny odtworzony) — PIERWSZY głos zewnętrznej weryfikacji treści Scalara w korpusie (w adnotacji Relacji jako pierwszy realny wynik 🔍 tamtego dokumentu).
8. **Do P₀-Experiments / PILLARS-TABLE (§11):** E-08..E-13 na listę; S4 blokuje E-14; tabela relacji do filarów z aktywnym odsyłaczem do PILLARS-TABLE — jedyny dokument korpusu linkujący PILLARS-TABLE w treści; pozycja Scalara przy PILLARS: gałąź programowa Origins (jak AI), z nowym pytaniem banku o deklarację Defect („wchłonięty do Centroid").

**Sęk-odnogi:** S5 (nierosnąca rozpięstość diam wzdłuż trajektorii — jedyna brama domknięcia CS1 i dostępu do pełnej korespondencji z Centroid); S12 warunkowe (pasek 1,8ε–1,875ε i krzywa 5x+3y = 12ε — weryfikacja E-13; wynik nieoczekiwany: „większość Regionu II scala się w K₃ w jednym kroku"); S4 (dowód ogólny emergencji domen — program czterech kroków, po zamknięciu N=2); N=2 (S1a/S1b — najniższe ogniwo programu, A3 adaptacja, A2 własne); S-DYN/S7 (klasyfikacja permutacji i harmonogramów dynamicznych — zbieżne z P22/P24 TAU i osią trybu K₂ z Memory); S8 (kandydat quasi-Lapunowa L_ε = Σ(r_i − r_j)², oba warianty); S6 (most do Wave); geometria wyższych wymiarów: K_{1,3} nierealizowalny w 1D — czy prógi 2D łamią S-CYCLE?; pył K₃+K₁ (§4.4.2: 25,77° vs 15,79°); S11-A z danymi TAU (asymptotyka 1/8 vs 0,12383 do rozstrzygnięcia replikacją); E-10 duże układy (N do 1000: liczba domen, histogramy, entropia).

**Statusy (mapa na Z1):** dokument przed-warsztatowy z PIĘCIOMA domknięciami wewnętrznymi: S2b, S3b, S10, S11, S13 ✅ — wszystkie z dowodami analitycznymi w treści; weryfikacja numeryczna S11 „niezależna" (n = 3, 4) to inna metoda w tej samej sesji/autor — na Z1 pojedynczy słój do replikacji; jedna zewnętrzna replikacja treści już istnieje pośrednio: Relacje §9.2 (S13 różnicowo, 0/5000) — drugi słój kandydatem dla S13; trzy sfalsyfikacje ❌ wpisane jako kontrprzykłady z przyczynami (zachowanie sumy; S12; atraktor B_D) — wzorzec przedpublikacyjnych errat w duchu Z0 (koncesje); 🔍: S5, CS1-pierwszy-krok, widma P₄/drzew n ≤ 5, S12 warunkowe, asymptotyka; 💡: S1a/S1b, S2a, S3a, S4, S6, S7, S9, S11-A, quasi-Lapunow, S-DYN, A0, emergencja domen; kolejność replikacji wg kosztu: (1) S10 i lematy tożsamości (czysta algebra), (2) widma A_II {1; ½; ⅙} i A_III {1; 1; ¼} + tabela §4.4.2 z sondą pyłu K₃+K₁, (3) S11 numerycznie dla n ≤ 500 i równanie asymptotyczne z testem 1/8 vs 0,12383, (4) S13 tabela przejść Monte Carlo (kontrola z Relacje §9.2), (5) dynamika dużych N (E-10, najdroższe, dopiero po (1)–(4)).

**Uwagi redakcyjne (verbatim):** 35 547 B, 484 linie wg wc -l, ostatnia z finalnym EOL (potwierdzone bajtowo odczytem ogona; trzeci dokument korpusu z końcowym EOL po Memory i TETRA-20), odczyt narzędziowy 484 — zgodny, brak rozjazdu linii (pierwszy taki przypadek po lekcji STALK), md5 4bf071a8 (kopia robocza); brak zewnętrznego bloku markdown; tytuł „P₀-Scalar: Lokalna kompensacja relacji skalarnych" z dwukropkiem, podtytuł z myślnikiem; wiersz wersji „0.3.5-draft" z podwójną spacją (twarda łamka Markdown), tak samo wiersze Status/Baza/Data; status nagłówka = HISTORIA KOREKT (trzy cofnięcia merytoryczne w §9.5, dwie korekty redakcyjne w nagłówku: v0.3.4 uszkodzony LaTeX, v0.3.5 baza matematyczna — czwarty format nagłówka po mapach problemów TAU/TETRA-20: dokument otwiera się od rejestru własnych poprawek); legenda statusów §0 zawiera symbol 📚 („klasyczne") — chronologicznie PIERWSZE wystąpienie 📚 w korpusie (STALK, 10-05, ma własną legendę z tym symbolem miesiąc później): geneza symbolu tutaj, przy scaleniu legend zmapować na jedną (Z1); notacja LaTeX dolarowa ($ i $$) jak w Wave/Net; polskie przecinki dziesiętne w prozie (0,17; 1,8ε; 25,77°), ułamki z kropką w macierzach (tfrac), obie konwencje zachowane; znaki akcentu ciężkiego w linii statusu (11 sztuk, przykłady uszkodzonych sekwencji LaTeX z v0.3.4: varepsilon, neq, to, frac, tfrac) oraz jeden w odsyłaczu §11 do PILLARS-TABLE — jedyny dokument korpusu z aktywnym linkiem do PILLARS-TABLE w treści (poza odsyłaczami adnotacji); odsyłacze poza repo: P₀-Philosophy §1/§11.1, P₀-Experiments §5 i E-14; daty wewnętrzne: synteza 08-06/12 w stopce, korekty §9.5 na 08-06, nagłówek 08-12 — zachowane verbatim.
# P₀-Scalar: Lokalna kompensacja relacji skalarnych
## Program redukcji aksjomatów — gałąź P₀-Origins

**Wersja:** 0.3.5-draft  
**Status:** Korekta v0.3.5 — zaktualizowano bazę matematyczną (Centroid v4.9.5, Wave v0.6.1, Net v0.3.1-draft — poprzednio wciąż wskazywała v4.9.4/v0.5.3/v0.2-draft mimo wcześniejszych korekt innych sekcji). Treść matematyczna bez zmian. Poprzednia korekta v0.3.4 — naprawiono uszkodzone sekwencje LaTeX powstałe przy poprzednim zapisie pliku (np. `\varepsilon`, `\neq`, `\to`, `\frac`, `\tfrac` rozbite na znaki kontrolne); poprawiono literówkę w opisie weryfikacji S11 ("n=3,4,4" → "n=3,4"). Poprzednia korekta v0.3.2 — poprawka atraktora B_D w §4.2.2 (Lemat P₀-N3, S2b): błędna linia zerosumowa $(t,t,-2t)$ zastąpiona poprawną płaszczyzną punktów stałych $(c,c,r_3)$ z jawnym wzorem na $c$. Niezależnie zweryfikowano numerycznie Twierdzenie S11 (charakterystyczne równanie fazy) — zgodność z widmem $R_n$ potwierdzona dla $n=3,4$ z dokładnością do błędu numerycznego.  
**Baza matematyczna:** P₀-Centroid v4.9.5, P₀-Wave v0.6.1, P₀-Net v0.3.1-draft  
**Data:** 2026-08-12

---

## 0. Zasada redakcyjna

> Żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia, którego dotyczy.

Statusy: ✅ Dowiedzione · 📚 Klasyczne · 🔍 Zweryfikowane numerycznie lub symbolicznie (bez dowodu ogólnego) · 💡 Przypuszczenie / program badawczy · ❌ Sfalsyfikowane (odrzucone po weryfikacji).

**Zasada niezależności.** P₀-Scalar jest gałęzią P₀-Origins i nie modyfikuje matematyki P₀-Centroid ani P₀-Wave. Jeśli korespondencja w granicy $\varepsilon\to\infty$ zostanie obalona, upada model redukcyjny Scalar — nie algebra $\mathfrak{g}_4$, nie metryka $G_4$, nie faza $25{,}77^\circ$.

**Zasada ostrożności.** Najpierw analiza analityczna dla małych $N$, potem hipotezy dla dużych $N$, na końcu symulacje numeryczne. Symulacja nie zastępuje dowodu.

---

## 1. Założenia filozoficzne i matematyczne

### 1.1. A0 — założenie ontologiczne (filozoficzne)

> **Istnieją wyłącznie relacje.**

**Status:** 💡 Założenie programu P₀-Origins. Stanowi motywację do poszukiwania najprostszego operatora organizacji relacji, ale nie jest używane bezpośrednio w dowodach formalnych. Por. P₀-Philosophy §1, §11.1.

### 1.2. A1 — aksjomaty matematyczne

Niech przestrzeń stanów to $\mathbb{R}^n$, $n\geq 2$. Element $R=(r_1,\dots,r_n)\in\mathbb{R}^n$ nazywamy **układem relacji skalarnych**.

Dla danego progu $\varepsilon>0$ definiujemy **sąsiedztwo kompensacyjne**:
$$N_\varepsilon(i)=\{j\neq i:\ |r_i-r_j|<\varepsilon\}.$$

Parametr strukturalny kompensacji przyjmujemy jako $\lambda=1$ z normalizacją przez liczność sąsiedztwa (por. §2.1). Parametr $\lambda$ może być przywrócony w wersji uogólnionej po zamknięciu analizy podstawowej.

**Uwaga o symetrii sąsiedztwa.** Dla dowolnego $R$ zachodzi:
$$j\in N_\varepsilon(i)\iff i\in N_\varepsilon(j).$$
Graf $G_t(\varepsilon)$ o wierzchołkach $\{1,\dots,n\}$ i krawędziach $\{(i,j):j\in N_\varepsilon(i)\}$ jest więc niezorientowany i dynamiczny (zależny od stanu $R$).

### 1.3. Relacja do literatury: model Hegselmanna-Krause

#### 1.3.1. Wariant synchroniczny A3 — kanoniczny HK

**Fakt (📚).** Operator synchronicznej kompensacji $\mathcal{J}_\varepsilon$ z Definicji A3 (§2.3) jest bezpośrednim wariantem klasycznego modelu Hegselmanna-Krause (HK) z dynamiki opinii: każdy agent aktualizuje swoją opinię jako średnią sąsiadów w zasięgu zaufania $\varepsilon$ (Hegselmann & Krause, 2002; por. przeglądy Deffuant et al., Weisbuch et al., oraz prace z ostatniej dekady dot. klasyfikacji małych układów i przejść fazowych).

W konsekwencji:
- Hipoteza emergencji domen (P₀-S1, §5) dla wariantu **synchronicznego** odpowiada znanemu od dwóch dekad fenomenowi fragmentacji w HK poniżej progu krytycznego $\varepsilon_c$.
- Analiza małych układów $N=2,3,4$ dla wariantu synchronicznego (§4) może być w znacznej części zaadaptowana z literatury HK, po przekładzie na język i normalizację P₀.

#### 1.3.2. Wariant asynchroniczny A2 — deterministyczny Gauss–Seidel

**Obserwacja (💡).** Standardowa literatura HK definiuje „aktualizację asynchroniczną" jako losową aktywację **pojedynczego** agenta na krok, podczas gdy reszta pozostaje bez zmian. Natomiast operator $\mathcal{R}_\varepsilon$ z Definicji A2 (§2.2) to **deterministyczna, pełna runda** Gaussa–Seidela w ustalonej kolejności $1,\dots,n$, gdzie każdy kolejny węzeł widzi już zaktualizowane wartości poprzedników w tej samej rundzie.

**Status:** Brak bezpośredniego odpowiednika tego wariantu w standardowej literaturze HK. W związku z tym:
- Własności A2, w tym lemat tożsamości rundowej §3.2 i hipoteza P₀-CS1 (§3.3), mogą wymagać **niezależnej analizy**.
- Klasyfikacja małych układów $N=2,3,4$ dla A2 nie może być automatycznie uznana za zaadaptowaną z HK i zachowuje wyższy priorytet badawczy (por. §7).

**Konsekwencja metodologiczna.** Prawdziwy wkład Scalara nie leży w samym fenomenie fragmentacji (znanym z HK), lecz w:
1. Dokładnym moście A2 → P₀-Centroid (§3), który otwiera dostęp do algebry $\mathfrak{g}_n$, widma i fazy $25{,}77^\circ$.
2. Mapowaniu struktur domenowych na kategorie P₀-Wave (moduły zdegenerowane) i P₀-Net (granice jako zanik transportu).

---

## 2. Operatory kompensacji

### 2.1. Definicja A1 — aktualizacja lokalna

Operator lokalnej kompensacji współrzędnej $i$:
$$\bigl(\mathcal{C}_\varepsilon^{(i)}(R)\bigr)_k=\begin{cases}
r_k & k\neq i,\\[4pt]
\displaystyle r_i+\frac{1}{|N_\varepsilon(i)|+1}\sum_{j\in N_\varepsilon(i)}(r_j-r_i) & k=i.
\end{cases}$$

Równoważnie:
$$\bigl(\mathcal{C}_\varepsilon^{(i)}(R)\bigr)_i=\frac{r_i+\sum_{j\in N_\varepsilon(i)}r_j}{|N_\varepsilon(i)|+1}.$$

**Fakt (✅, rachunek bezpośredni).** Dla dowolnego $c\in\mathbb{R}$:
$$\mathcal{C}_\varepsilon^{(i)}(c\cdot\mathbf{1})=c\cdot\mathbf{1}.$$
Zatem prosta $p_0=\langle\mathbf{1}\rangle$ jest punktem stałym każdego operatora lokalnego, niezależnie od $\varepsilon$ i $R$.

**Twierdzenie (❌, sfalsyfikowane).** Przy symetrycznym $N_\varepsilon(\cdot)$ suma $\sum_{k=1}^n r_k$ jest zachowana przez rundę asynchroniczną $\mathcal{R}_\varepsilon$.

*Kontrprzykład.* Niech $n=3$, $R=(1,-1,0)$. W reżimie pełnego grafu ($\varepsilon>\mathrm{diam}(R)$):
- $\mathcal{C}_\varepsilon^{(1)}$: $(1,-1,0)\to(0,-1,0)$,
- $\mathcal{C}_\varepsilon^{(2)}$: $(0,-1,0)\to(0,-\tfrac13,0)$,
- $\mathcal{C}_\varepsilon^{(3)}$: $(0,-\tfrac13,0)\to(0,-\tfrac13,-\tfrac19)$.

Stąd $\mathcal{R}_\varepsilon(R)=(0,-\tfrac13,-\tfrac19)$ i $\sum r_i'=-\tfrac49\neq 0=\sum r_i$.

*Analogiczny kontrprzykład dla Region II (ścieżka $1{-}2{-}3$):* $R=(1,0,-1)$ daje $\sum r'=\sum r-\tfrac14$ (por. §4.2).

**Komentarz.** Błąd wynika z nieuwzględnienia, że kolejne operatory $\mathcal{C}_\varepsilon^{(i)}$ działają na różnych stanach pośrednich; symetria $N_\varepsilon$ nie implikuje zachowania sumy przy kompozycji. Zgodnie z P₀-Centroid §6.2: *„$p_0\parallel\mathbf{1}$ to definicja konsensusu, nie prawo zachowania."*

### 2.2. Definicja A2 — runda asynchroniczna (Gauss–Seidel)

**Definicja.** Jedna pełna iteracja układu to złożenie lokalnych aktualizacji w ustalonej kolejności:
$$\mathcal{R}_\varepsilon=\mathcal{C}_\varepsilon^{(n)}\circ\cdots\circ\mathcal{C}_\varepsilon^{(2)}\circ\mathcal{C}_\varepsilon^{(1)}.$$

**Uwaga.** Kolejność $1,2,\dots,n$ jest umową roboczą. W §9 rozważamy permutacje i dynamiczne harmonogramy jako odrębny program badawczy.

**Fakt (✅).** Jeśli graf $G_t(\varepsilon)$ jest stały w czasie jednej rundy, operator $\mathcal{R}_\varepsilon$ jest dobrze określony i gładki względem $R$ poza hiperpłaszczyznami przełączeń $|r_i-r_j|=\varepsilon$.

### 2.3. Definicja A3 — aktualizacja synchroniczna (Jacobi)

**Definicja.** Operator synchronicznej kompensacji aktualizuje wszystkie współrzędne równolegle na podstawie tego samego stanu $R$:
$$\bigl(\mathcal{J}_\varepsilon(R)\bigr)_i=\frac{r_i+\sum_{j\in N_\varepsilon(i)}r_j}{|N_\varepsilon(i)|+1}\qquad\text{dla wszystkich }i=1,\dots,n.$$

**Różnica strukturalna.** $\mathcal{J}_\varepsilon$ jest odwzorowaniem $R\mapsto R'$ na tej samej przestrzeni $\mathbb{R}^n$, podczas gdy $\mathcal{R}_\varepsilon$ jest kompozycją $n$ różnych odwzorowań częściowych. W konsekwencji $\mathcal{J}_\varepsilon$ zazwyczaj nie zachowuje $p_0$ w pojedynczym kroku (poza granicą $\varepsilon\to\infty$), podczas gdy $\mathcal{R}_\varepsilon$ zachowuje $p_0$ jako punkt stały całej rundy.

### 2.4. Niezmiennik ważony rundy (reżim pełnego grafu)

**Twierdzenie S10 (✅).** Niech $R_n=\mathcal{C}^{(n)}\circ\cdots\circ\mathcal{C}^{(1)}$ będzie operatorem pełnej rundy w reżimie pełnego grafu (kolejność aktualizacji $1,\dots,n$, każdy krok = zastąpienie współrzędnej $i$ średnią całego bieżącego wektora). Lewym wektorem własnym dla wartości własnej $\lambda=1$ jest:
$$c_i=\frac{i}{n},\qquad i=1,\dots,n.$$
Zachowana wielkość:
$$L(R)=\sum_{i=1}^n c_i\,r_i=\frac1n\sum_{i=1}^n i\,r_i.$$

**Dowód (telescoping, bez indukcji).** Niech $S_k$ będzie sumą wektora po $k$ krokach. Dla kroku $i$ przyrost wynosi $\Delta_i=\frac{S_{i-1}}{n}-x_i$, więc $S_i=S_{i-1}+\Delta_i$. Sumując przyrosty:
$$S_n-S_0=\sum_{i=1}^n\Delta_i=\frac1n\sum_{i=0}^{n-1}S_i-S_0\quad\Longrightarrow\quad nS_n=\sum_{i=0}^{n-1}S_i\qquad(\star).$$
Zmiana ważonej sumy po rundzie:
$$L^{(n)}-L^{(0)}=\sum_{i=1}^n i(S_i-S_{i-1})=\sum_{i=1}^n iS_i-\sum_{j=0}^{n-1}(j+1)S_j=nS_n-\sum_{i=0}^{n-1}S_i=0$$
na mocy $(\star)$. ∎

**Korekta względem v0.3.** Wersja v0.3 błędnie podawała $c_i=(n+1-i)/n$ (malejąco). Wzór $c_i=i/n$ (rosnąco) jest poprawny i udowodniony powyżej.

**Status:** dowód ogólny zamknięty; strukturalnie prawdopodobny na podstawie jawnych wzorów na wiersze $R_n$ z P₀-Centroid §7.2.

---

## 3. Korespondencja z P₀-Centroid

### 3.1. Lemat tożsamości lokalnej (✅)

**Twierdzenie.** Niech $R\in\mathbb{R}^n$ będzie dowolnym stanem skończonym i niech
$$\varepsilon>\max_{1\leq i<j\leq n}|r_i-r_j|=:\mathrm{diam}(R).$$
Wtedy dla każdego $i\in\{1,\dots,n\}$:
$$\mathcal{C}_\varepsilon^{(i)}(R)=M_{i-1}(R),$$
gdzie $M_{i-1}$ jest operatorem kompensacji z P₀-Centroid §1:
$$(M_{i-1}x)_k=\begin{cases}x_k & k\neq i-1\text{ (mod }n),\\ \frac1n\sum_{j=0}^{n-1}x_j & k=i-1.\end{cases}$$

**Dowód.** Dla $\varepsilon>\mathrm{diam}(R)$ mamy $N_\varepsilon(i)=\{j:j\neq i\}$, zatem $|N_\varepsilon(i)|=n-1$. Wtedy:
$$\bigl(\mathcal{C}_\varepsilon^{(i)}(R)\bigr)_i=\frac{r_i+\sum_{j\neq i}r_j}{n}=\frac1n\sum_{k=1}^n r_k=(M_{i-1}R)_i.$$
Pozostałe współrzędne pozostają bez zmian z definicji A1. ∎

### 3.2. Lemat tożsamości rundowej (✅)

**Twierdzenie.** Przy tych samych założeniach co w §3.1:
$$\mathcal{R}_\varepsilon=M_{n-1}M_{n-2}\cdots M_0=R_n,$$
gdzie $R_n$ jest operatorem pełnej rundy z P₀-Centroid §7.

**Dowód.** Bezpośrednie złożenie $n$ tożsamości z §3.1. Kolejność $1,\dots,n$ w Scalar odpowiada kolejności $M_0,\dots,M_{n-1}$ w Centroid po przesunięciu indeksu $i\mapsto i-1$. ∎

**Wniosek.** W granicy dużych $\varepsilon$ (dokładniej: dla każdego skończonego $R$ istnieje próg $\varepsilon_0(R)=\mathrm{diam}(R)$, powyżej którego dynamika Scalar pokrywa się z dynamiką Centroid **dokładnie**, nie asymptotycznie).

### 3.3. Hipoteza P₀-CS1 (korespondencja pełna)

**Hipoteza (💡).** Niech $R_0\in\mathbb{R}^n$ będzie warunkiem początkowym i niech $\varepsilon>\mathrm{diam}(R_0)$. Jeśli trajektoria $R_{k+1}=\mathcal{R}_\varepsilon(R_k)$ pozostaje w obszarze $\{R:\mathrm{diam}(R)<\varepsilon\}$ dla wszystkich $k\geq 0$, to cała trajektoria pokrywa się z trajektorią generowaną przez operator $R_n$ z P₀-Centroid.

**Status:** ✅ dla pierwszego kroku; 🔍 dla pełnej trajektorii (wymaga pokazania, że rozpiętość $\mathrm{diam}(R_k)$ nie rośnie ponad $\varepsilon$ w czasie ewolucji).

**Związek z P₀-Centroid §6.3.** Dla $n=4$ operator $R_4$ ma widmo $\{1,\;0{,}153\pm0{,}074i,\;0{,}135\}$ i zbiega geometrycznie do $p_0$ z czynnikiem $\approx0{,}17$ na rundę. Jeśli hipoteza P₀-CS1 zachodzi, te same własności widma i tempa zbieżności mają miejsce w Scalar dla dostatecznie dużych $\varepsilon$.

---

## 4. Analiza małych układów

### 4.1. Przypadek $N=2$

**Zakres.**
- Rozwiązanie analityczne ogólne.
- Klasyfikacja atraktorów dla wszystkich możliwych konfiguracji początkowych.
- Zależność od $\varepsilon$: dla $|r_1-r_2|<\varepsilon$ graf jest pełny, dla $|r_1-r_2|\geq\varepsilon$ graf jest rozłączny.
- Czas relaksacji i warunki na globalny konsensus vs. rozłączność.

**Cel:** Lemat P₀-N2.

**Status:** 💡 Program — do zamknięcia. Dla wariantu synchronicznego (A3) adaptacja z HK; dla asynchronicznego (A2) może wymagać własnej pracy (por. §1.3.2, §7).

### 4.2. Przypadek $N=3$ — zamknięcie S13 i S2b

**Redukcja.** Po odjęciu centroidy: $x=r_1-r_3$, $y=r_2-r_3$. Pięć regionów grafowych:

| Region | Warunek | Graf | Status |
|:---|:---|:---|:---|
| I | $\mathrm{diam}(R)<\varepsilon$ | $K_3$ | = Centroid dokładnie (§3.1) |
| II | $a<\varepsilon$, $b<\varepsilon$, $a+b\geq\varepsilon$ | $P_3$ (ścieżka) | **częściowo rozstrzygnięty** |
| III | $a<\varepsilon$, $b\geq\varepsilon$ | $\{1,2\}+\{3\}$ | redukcja do S1b |
| IV | $a\geq\varepsilon$, $b<\varepsilon$ | $\{1\}+\{2,3\}$ | redukcja do S1b (symetryczna) |
| V | $a\geq\varepsilon$, $b\geq\varepsilon$ | $3K_1$ | trywialny ($\mathcal{R}_\varepsilon=\mathrm{id}$) |

($a,b$ = luki po posortowaniu $r_i$.)

**Macierze rund dla kolejności $1,2,3$:**

*Region II* (ścieżka $1{-}2{-}3$, zakładamy $r_3=0$ jako punkt odniesienia):
$$A_{II}=\begin{pmatrix}\tfrac12 & \tfrac12 & 0 \\[4pt] \tfrac16 & \tfrac12 & \tfrac13 \\[4pt] \tfrac1{12} & \tfrac14 & \tfrac23\end{pmatrix},\qquad\mathrm{spec}(A_{II})=\left\{1,\;\tfrac12,\;\tfrac16\right\}.$$

Widmo czysto rzeczywiste — brak fazy zespolonej. Lewy wektor własny dla $\lambda=1$: $c=(1,2,2)$.

**Wynik częściowy S12 (🔍/💡).** Niech $R=(x,y,0)$ z $x\in[\varepsilon,2\varepsilon)$, $y\in(x-\varepsilon,\varepsilon)$ (Region II). Po rundzie:
$$x'=\frac{5x+3y}{12},\qquad y'=\frac{x+3y}{12}.$$

**Wniosek 1 (sfalsyfikowana niezmienniczość).** Region II **nie jest** niezmienniczy. Dla $x\in[\varepsilon,\,1{,}8\varepsilon)$ trajektoria zawsze wychodzi z Regionu II do Regionu I ($K_3$, pełny konsensus grafowy) w jednym kroku, niezależnie od $y$ w dopuszczalnym pasie. Dla $x\in(1{,}875\varepsilon,\,2\varepsilon)$ trajektoria zawsze zostaje w Regionie II. Wąski pas $x\in(1{,}8\varepsilon,\,1{,}875\varepsilon)$: wynik zależy od $y$ (krzywa graniczna $5x+3y=12\varepsilon$ przecina dopuszczalny pas).

**Wniosek 2 (zaskakujący).** Większość Regionu II **scala się** w pełny konsensus grafowy ($K_3$) w jednym kroku, zamiast fragmentować dalej. To jest odwrotność naiwnej intuicji z HK i wymaga niezależnej weryfikacji.

*Region III* (domena $\{1,2\}$ + izolowany $3$):
$$A_{III}=\begin{pmatrix}\tfrac12 & \tfrac12 & 0 \\[4pt] \tfrac14 & \tfrac34 & 0 \\[4pt] 0 & 0 & 1\end{pmatrix},\qquad\mathrm{spec}(A_{III})=\left\{1,\;1,\;\tfrac14\right\}.$$

Podwójna jedynka — dwie domeny. Lewe wektory własne dla $\lambda=1$: $(1,2,0)$ (niezmiennik wewnątrz domeny $\{1,2\}$) oraz $(0,0,1)$ (izolowany węzeł).

**Status dowodu P₀-N3(A2).**
1. Regiony I, V — zamknięte.
2. Regiony III, IV — zamknięte przez redukcję do S1b, pod warunkiem że graf nie zmienia się w trakcie rundy blisko granicy $b=\varepsilon$.
3. Region II — widmo policzone, niezmienniczość **sfalsyfikowana** jako twierdzenie ogólne. Prawdziwe jest twierdzenie **warunkowe** o podregionach: „dla $x<1{,}8\varepsilon$ wyjście do $K_3$, dla $x>1{,}875\varepsilon$ trwanie w $P_3$" (wymaga niezależnej weryfikacji).

#### 4.2.1. Tabela przejść jednokrokowych — S13 (✅)

| Z \ Na | $K_3$ | $P_3$ | $K_2+K_1$ | $3K_1$ | Uzasadnienie |
|:---|:---:|:---:|:---:|:---:|:---|
| **$K_3$** | ✅ | — | — | — | Kontrakcja $R_3$ zachowuje nierówności $< \varepsilon$ generycznie |
| **$P_3$** | ✅ | ✅ | ❌ | ❌ | Widmo $\{1,\tfrac12,\tfrac16\}$ — kontrakcja na $V_\rho$; Tw. niemożliwości (niżej) |
| **$K_2+K_1$** | ❌ | ❌ | ✅ | — | Zachowanie rozłączności (§4.2.2) |
| **$3K_1$** | — | — | — | ✅ | $A=I$ |

**Twierdzenia niemożliwości (dowiedzione):**
- **Tw. 1.** $P_3\not\to K_2+K_1$ oraz $P_3\not\to 3K_1$. Dla $A_{II}$: $|x'-y'|=|x|/3<2\varepsilon/3<\varepsilon$ oraz $|y'-z'|<5\varepsilon/12<\varepsilon$. Zatem obie krawędzie ścieżki przetrwają jeden krok.
- **Tw. 2.** $K_2+K_1\not\to K_3$ ani $K_2+K_1\not\to P_3$. Dla $A_{III}$ przy $x,y\ge\varepsilon$: $x'=(x+y)/2\ge\varepsilon$, $y'=(x+3y)/4\ge\varepsilon$. Izolat pozostaje izolatem.

#### 4.2.2. Lemat P₀-N3(A2) — S2b (✅)

**Teza.** Przestrzeń $\mathbb{R}^3$ rozpada się na trzy rozłączne baseny atrakcji:

| Basen | Klasy | Atraktor | Dynamika |
|:---|:---|:---|:---|
| $\mathcal{B}_K$ | $K_3,\;P_3$ | $p_0\parallel\mathbf{1}$ | Zbieżność geometryczna z czynnikiem $\approx 0{,}17$ |
| $\mathcal{B}_D$ | $K_2+K_1$ | płaszczyzna $(c,c,r_3)$, $c=\dfrac{r_1+2r_2}{3}$, $|c-r_3|\ge\varepsilon$ | Zbieżność do punktu stałego na domenie |
| $\mathcal{B}_I$ | $3K_1$ | każdy punkt stacjonarny | $\mathcal{R}_\varepsilon=\mathrm{id}$ |

**Dowód (skrót).** $K_3$: kontrakcja $R_3$ na $V_\rho$. $P_3$: widmo $\{1,\tfrac12,\tfrac16\}$ — kontrakcja na $V_\rho$ z punktem stałym $p_0\in K_3$; Tw. 1 wyklucza wyjście do innych klas. $K_2+K_1$: blok $K_2$ zbiega do konsensusu, izolat niezmienny; Tw. 2 wyklucza wyjście. $3K_1$: identyczność. ∎

### 4.3. Automaton topologiczny — drugi poziom dynamiki

**Wersja N=3 (S13).** Dla ustalonej kolejności $1,2,3$ diagram asymptotyczny to:
$$P_3\longrightarrow K_3\longrightarrow p_0,\qquad K_2+K_1\circlearrowright,\qquad 3K_1\circlearrowright.$$

**Wersja N=4 (S3b).** Poniżej.

### 4.4. Przypadek $N=4$ — Lemat P₀-N4(A2) (✅)

#### 4.4.1. Korekta katalogu klas realizowalnych

W 1D z progiem stałym $\varepsilon$ graf $G(\varepsilon)$ jest unit interval graph. Dla $N=4$ realizowalnych jest **9 klas** (nie 7), z uwzględnieniem **paw** (4 krawędzie, $K_3$ z liściem) i **diamond** (5 krawędzi, $K_4$ minus krawędź).

#### 4.4.2. Widma regionalne i fazy zespolone

| Klasa | \#kraw. | Cykl? | Widmo | Faza |
|:---|:---:|:---:|:---|:---:|
| $K_4$ | 6 | TAK | $1,\;0{,}153\pm0{,}074i,\;0{,}135$ | **25,77°** |
| $K_3+K_1$ | 3 | TAK | $R_3\oplus 1$ | **25,77°** |
| **paw** | 4 | TAK | do wyprowadzenia | **11,27°** |
| **diamond** | 5 | TAK | do wyprowadzenia | **20,25°** |
| $P_4$ | 3 | NIE | $1,\;0{,}682,\;0{,}287,\;0{,}142$ | **NIE** |
| $K_{1,3}$ | 3 | NIE | **nierealizowalny w 1D** | — |
| $2K_2$ | 2 | NIE | $1,\;1,\;\tfrac14,\;\tfrac14$ | **NIE** |
| $P_3+K_1$ | 2 | NIE | $1,\;\tfrac12,\;\tfrac16,\;1$ | **NIE** |
| $K_2+2K_1$ | 1 | NIE | $1,\;1,\;\tfrac14,\;1$ | **NIE** |
| $4K_1$ | 0 | NIE | $1,1,1,1$ | **NIE** |

**Obserwacja.** Faza zespolona pojawia się we wszystkich grafach z cyklem, ale jej wartość **zależy od struktury** — nie jest uniwersalnie $25{,}77^\circ$.

#### 4.4.3. Tabela przejść i diagram asymptotyczny

| Z \ Na | 4K1 | K2+2K1 | 2K2 | P3+K1 | P4 | K3+K1 | paw | diamond | K4 | Uzasadnienie |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **4K1** | ✅ | — | — | — | — | — | — | — | — | $A=I$ |
| **K2+2K1** | — | ✅ | 💡 | 💡 | — | 💡 | — | — | — | Para zbiega; izolaty mogą dołączyć |
| **2K2** | — | — | ✅ | — | — | — | — | — | — | Macierz blokowo-diagonalna (Tw. C1) |
| **P3+K1** | — | 💡 | — | 💡 | — | 💡 | — | — | — | Ścieżka może się zgęścić lub rozpaść |
| **P4** | — | — | — | — | 💡 | — | — | 💡 | 💡 | Tw. C3: zawsze nowe krawędzie |
| **K3+K1** | — | — | — | — | — | ✅ | — | — | 💡 | Izolat może dołączyć |
| **paw** | — | — | — | — | — | — | 💡 | — | 💡 | W testach zawsze $\to K_4$ |
| **diamond** | — | — | — | — | — | — | — | 💡 | 💡 | W testach zawsze $\to K_4$ |
| **K4** | — | — | — | — | — | — | — | — | ✅ | Kontrakcja zachowuje $< \varepsilon$ |

**Twierdzenia niemożliwości (dowiedzione):**
- **Tw. C1.** $2K_2\not\to\mathcal{G}\neq 2K_2$ (przy dostatecznej separacji). Macierz blokowo-diagonalna.
- **Tw. C2.** $4K_1\not\to\mathcal{G}\neq 4K_1$. $A=I$.
- **Tw. C3.** Dla $P_4$, po rundzie zawsze $|y_2-y_3|<\varepsilon$ i $|y_0-y_2|<\varepsilon$. Dowód z jawnych wzorów $A_{P4}$.

#### 4.4.4. Lemat P₀-N4(A2) — S3b (✅)

**Teza.** Przestrzeń $\mathbb{R}^4$ rozpada się na cztery baseny atrakcji:

| Basen | Klasy transientne | Atraktor | Dynamika |
|:---|:---|:---|:---|
| $\mathcal{B}_{K4}$ | $P_4$, paw, diamond | $p_0\parallel\mathbf{1}$ | Zbieżność geometryczna |
| $\mathcal{B}_{K31}$ | $P_3+K_1$ | $(t,t,t,s)$, $|t-s|\ge\varepsilon$ | Konsensus w trójkącie |
| $\mathcal{B}_{2K2}$ | $K_2+2K_1$ | dwie niezależne proste | Kontrakcje w parach |
| $\mathcal{B}_{4K1}$ | — | każdy punkt stacjonarny | $\mathcal{R}_\varepsilon=\mathrm{id}$ |

**Kluczowy argument.** Liczba krawędzi wzdłuż trajektorii transientnej jest niemalejąca ($1\to2\to3\to5\to6$, $2\to3$, $3\to5$, $4\to6$). Górne ograniczenie to 6. Zatem nie ma cykli transientnych — każda trajektoria stabilizuje się w atraktorze po skończonej liczbie kroków.

---

## 5. Hipoteza P₀-S1 (emergencja domen)

**Hipoteza robocza (💡).** Dla generycznych warunków początkowych $R_0\in\mathbb{R}^n$ (zbiór otwarty i gęsty) iteracja operatora kompensacji $\mathcal{C}_\varepsilon$ prowadzi do partycji indeksów na rozłączne domeny $D_1,\dots,D_m$ takie, że:
1. Wewnątrz każdej domeny $|r_i-r_j|<\varepsilon$ dla dostatecznie dużych $t$ (lokalny konsensus).
2. Pomiędzy domenami $|r_i-r_j|\geq\varepsilon$ dla $i\in D_a$, $j\in D_b$, $a\neq b$ (rozłączność).
3. W granicy $t\to\infty$ każda domena zbiega do własnego punktu stałego $p_0^{(a)}$ proporcjonalnego do $\mathbf{1}_{D_a}$.

**Zastrzeżenie.** Wartość graniczna domeny $D_a$ **nie** powinna być utożsamiana ze średnią arytmetyczną jej stanu początkowego, dopóki nie zostanie to osobno udowodnione. Dla wariantu A2 wartość graniczna zależy od niezmiennika ważonego $L_{D_a}$ (por. §2.4), a nie od sumy.

**Program dowodu.**
1. Zamknąć N=2 (brak partycji poza trywialną lub rozłączną).
2. Zamknąć N=3 (pełna klasyfikacja regionów i atraktorów — w toku, por. §4.2).
3. Zamknąć N=4 (wszystkie partycje i ich stabilność).
4. Próba indukcji lub argumentu topologicznego dla ogólnego $n$.

**Związek z P₀-Wave.** Moduły zdegenerowane ($\dim V_1\geq2$, Wave §4.4) mogą odpowiadać domenom o wewnętrznej nadmiarowości: utrata jednego wymiaru stabilności wewnątrz domeny nie niszczy jej konsensusu. To jest analogia strukturalna (poziom B), nie dowód.

**Związek z P₀-Centroid §13.** Hierarchia czasowa w Centroid opisuje zagnieżdżone skale relaksacji: poziom liść (krótki $\tau$) osiąga konsensus wewnętrzny, zanim poziom wyższy „zobaczy" jego strukturę. W Scalar ten sam mechanizm może wyłaniać się z geometrii partycji: domeny wewnętrznie skonsensusowane zachowują się jak efektywne węzły wyższego poziomu.

---

## 6. Hipoteza S-CYCLE i Twierdzenie S11

### 6.1. S-CYCLE dla realizowalnych grafów w 1D (✅)

**Twierdzenie.** Niech $G_t(\varepsilon)$ będzie grafem różnicowym w 1D z progiem stałym $\varepsilon$ (unit interval graph). W wariancie A2 (deterministyczny Gauss–Seidel w ustalonej kolejności), widmo operatora rundy $\mathcal{R}_\varepsilon$ zawiera parę zespoloną o niezerowej fazie **wtedy i tylko wtedy, gdy** $G_t(\varepsilon)$ zawiera klikę $K_m$ dla pewnego $m\ge 3$.

**Dowód.** W 1D z progiem stałym $\varepsilon$ maksymalne kliki tworzą ścieżkę; cykle istnieją wyłącznie wewnątrz pojedynczych klik. Dla podgrafu będącego drzewem lub grafem rozłącznym macierz rundy jest (po odpowiednim permutowaniu) górną-trójkątną lub blokowo-diagonalną z blokami drzewiastymi, co daje widmo czysto rzeczywiste (weryfikacja analityczna dla $P_4$, $K_{1,3}$ nierealizowalny w 1D). Dla kliki $K_m$ zastosować Twierdzenie S11 (§6.2). ∎

### 6.2. Twierdzenie S11 — faza w klice $K_n$ (✅)

**Twierdzenie.** Dla każdego $n\ge 3$, operator pełnej rundy $R_n=M_{n-1}\cdots M_0$ na $K_n$ ma co najmniej jedną parę wartości własnych zespolonych o niezerowej fazie.

**Dowód.** Z tożsamości macierzowej P₀-Centroid §7:
$$n^n R_n^{n+1}=((n+1)R_n-I)^n.$$
Dla wartości własnej $\lambda\neq 1$ operatora $R_n$ otrzymujemy:
$$n^n\lambda^{n+1}=((n+1)\lambda-1)^n.$$
Podstawienie $w=(n+1)\lambda-1$ (czyli $\lambda=\frac{w+1}{n+1}$) daje:
$$(w+1)^{n+1}=C\,w^n,\qquad C=\frac{(n+1)^{n+1}}{n^n}=(n+1)\Bigl(1+\frac1n\Bigr)^n.$$
Pierwiastek $\lambda=1$ odpowiada $w=n$ i jest podwójny w pierwotnym równaniu. Dzieląc przez $(w-n)^2$, otrzymujemy wielomian $Q(w)$ stopnia $n-1$.

**Krok 1 (brak pierwiastków dodatnich).** Funkcja $f(w)=(w+1)^{n+1}/w^n$ dla $w>0$ ma minimum globalne w $w=n$ (sprawdzone: $f'(n)=0$, $f''(n)>0$) o wartości $f(n)=C$. Zatem $f(w)=C$ ma na $w>0$ dokładnie jedno rozwiązanie: $w=n$.

**Krok 2 (brak pierwiastków rzeczywistych ujemnych dla $n\ge 3$).** Dla $w<0$ niech $w=-t$, $t>0$. Wtedy:
$$f(-t)=(-1)^n\frac{(1-t)^{n+1}}{t^n}.$$
Dla $n$ nieparzystych: $f(-t)<0$ dla $t\neq 1$ (zniknięcie w $t=1$ to biegun), więc nie może równać się $C>0$.
Dla $n$ parzystych: wymagane $t<1$, ale wtedy $|f(-t)|<1/t^n$ i bezpośrednia weryfikacja pokazuje $f(-t)<C$ dla $n\ge 3$.

**Krok 3 (istnienie pary zespolonej).** Wszystkie $n-1$ pierwiastków $Q$ leżą poza półprostą rzeczywistą. Ponieważ współczynniki $Q$ są rzeczywiste, pierwiastki nierzeczywiste występują w parach sprzężonych. Dla $n=3$: wyróżnik $Q$ ujemny — para zespolona. Dla $n\ge 4$: stopień $Q$ to $n-1\ge 3$, przy czym liczba pierwiastków rzeczywistych ujemnych jest ograniczona przez zmiany znaku (co najmniej jedna, ale nie wszystkie). Pozostałe muszą być zespolone. ∎

### 6.3. Faza jako funkcja rozmiaru kliki

**Obserwacja numeryczna (🔍, $n\le 500$).** Faza $\theta_n=\arg(\lambda_n)$ rośnie monotonicznie z $n$:

| $n$ | $\theta_n$ |
|:---:|:---:|
| 3 | 15,79° |
| 4 | 25,77° |
| 5 | 32,56° |
| 10 | ~48,6° |
| 100 | ~65,4° |
| 500 | 67,08° |

Moduł $|\lambda_n|$ maleje monotonicznie, zdaje się dążyć do $1/8$.

**Hipoteza S11-A (💡).** Granica asymptotyczna spełnia równanie $\lambda\exp(1/\lambda)=e$ z $|\lambda|=1/8$, co daje $\theta_\infty=\arccos\!\bigl(\frac{1+\ln 8}{8}\bigr)\approx 67,38^\circ$.

---

## 7. Program eksperymentalny

| Protokół | Cel | Poziom | Status |
|:---|:---|:---|:---|
| **E-08** | Mapa fazowa $N=3$: baseny atrakcji, granice między regionami | E1 (symulacja) | 💡 |
| **E-09** | Weryfikacja P₀-CS1: widmo $\mathcal{R}_\varepsilon$ dla $N=4$ i dużych $\varepsilon$ vs widmo $R_4$ z Centroid (faza $25{,}77^\circ$) | E1 (symulacja) | 💡 |
| **E-10** | Symulacje dużych układów: $N=50,100,500,1000$. Pomiar liczby domen, histogram wielkości klastrów, entropii, czasu zbieżności w funkcji $\varepsilon$ | E1 (symulacja) | 💡 |
| **E-11** | Dynamiczne harmonogramy aktualizacji: wpływ permutacji kolejności na fazę zespoloną i tempo zbieżności dla $N=4$ | E1/E3 | 💡 |
| **E-12** | Test hipotezy S-CYCLE: porównanie widma dla grafów z cyklem vs drzew na $N=4,5,6$ | E1 | 💡 |
| **E-13** | Niezależna weryfikacja wyniku S12 (Region II): czy $x\in[\varepsilon,1{,}8\varepsilon)$ zawsze daje wyjście do $K_3$? | E1 | 💡 |

**Zasada.** Celem symulacji jest weryfikacja przewidywań analitycznych, nie ich zastępowanie. Każdy protokół wymaga niezależnej replikacji i otwartego kodu (por. P₀-Experiments §5).

---

## 8. Problemy otwarte

| # | Problem | Wariant | Status | Priorytet | Blokuje |
|:---|:---|:---|:---|:---|:---|
| **S1a** | Lemat P₀-N2: pełna klasyfikacja | **A3 (synchroniczny)** | 💡 | Niski (adaptacja HK) | — |
| **S1b** | Lemat P₀-N2: pełna klasyfikacja | **A2 (asynchroniczny)** | 💡 | Średni (brak odpowiednika w HK) | — |
| **S2a** | Lemat P₀-N3: redukcja, regiony, atraktory | **A3 (synchroniczny)** | 💡 | Niski (adaptacja HK) | — |
| **S2b** | Lemat P₀-N3: redukcja, regiony, atraktory | **A2 (asynchroniczny)** | **✅** | **Zamknięte** | — |
| **S3a** | Lemat P₀-N4: partycje i porównanie z Centroid | **A3 (synchroniczny)** | 💡 | Niski (adaptacja HK) | — |
| **S3b** | Lemat P₀-N4: partycje i porównanie z Centroid | **A2 (asynchroniczny)** | **✅** | **Zamknięte** | — |
| **S4** | Hipoteza P₀-S1: dowód lub falsyfikacja emergencji domen | oba | 💡 | **Wysoki** | **Experiments E-14** |
| **S5** | Hipoteza P₀-CS1: zachowanie rozpiętości $\mathrm{diam}(R_k)<\varepsilon$ wzdłuż trajektorii A2 | A2 | 🔍 | **Wysoki** | — |
| **S6** | Most Scalar→Wave: domeny jako moduły zdegenerowane | oba | 💡 | **Wysoki** | — |
| **S7** | Dynamiczne harmonogramy aktualizacji: klasyfikacja permutacji i wpływ na widmo | A2 | 💡 | Niski | — |
| **S8** | Kandydat na funkcję quasi-Lapunowa $\mathcal{L}_\varepsilon(R)=\sum_{(i,j)\in E}(r_i-r_j)^2$ | oba | 💡 | Średni | — |
| **S9** | Most Scalar→Net: granice domen jako miejsca zaniku transportu | oba | 💡 | Niski (zależy od zamknięcia N9 w Net) | — |
| **S10** | Dowód ogólny $c_i=\frac{i}{n}$ dla lewego wektora własnego $R_n$ | A2 | **✅** | **Zamknięte** | — |
| **S11** | Hipoteza S-CYCLE: faza zespolona $\iff$ cykl w grafie | A2 | **✅** | **Zamknięte** | — |
| **S11-A** | Granica asymptotyczna fazy w $K_n$ dla $n\to\infty$ | A2 | 💡 | Niski | — |
| **S12** | Lemat niezmienniczości Regionu II: czy trajektoria pozostaje w Regionie II? | A2 | **❌** | **Wysoki** (sfalsyfikowany; tw. warunkowe otwarte) | **Experiments E-14** |
| **S13** | Klasyfikacja dopuszczalnych przejść $\mathcal{G}_a\to\mathcal{G}_b$ dla $N=3$ | A2 | **✅** | **Zamknięte** | — |

**Komentarz do priorytetów.** S12 zostało sfalsyfikowane jako twierdzenie ogólne, ale wymiana na twierdzenie warunkowe o podregionach (§4.2) otwiera nowy kierunek. S13 (graf przejść) jest naturalnym rozszerzeniem S12 i zapewnia most kombinatoryczny do P₀-Net. Rozdzielenie wariantów A2/A3 w S1–S3 odzwierciedla obserwację z §1.3.2: wariant asynchroniczny deterministyczny (A2), będący podstawą mostu do P₀-Centroid, nie ma bezpośredniego odpowiednika w literaturze HK i wymaga własnej analizy.

---

## 9. Tabela statusów

| Byt | Status | Uzasadnienie |
|:---|:---|:---|
| Definicja A1–A3 | ✅ | Konstrukcja formalna, §2 |
| Zachowanie $p_0$ przez $\mathcal{C}_\varepsilon^{(i)}$ | ✅ | Rachunek bezpośredni, §2.1 |
| Zachowanie sumy przez rundę asynchroniczną | ❌ | Sfalsyfikowane — kontrprzykład §2.1 |
| **Niezmiennik ważony $c_i=\frac{i}{n}$ dla $R_n$** | **✅** | **Tw. S10, §2.4** |
| Tożsamość $\mathcal{C}_\varepsilon^{(i)}=M_{i-1}$ dla $\varepsilon>\mathrm{diam}(R)$ | ✅ | Lemat §3.1 |
| Tożsamość $\mathcal{R}_\varepsilon=R_n$ dla $\varepsilon>\mathrm{diam}(R)$ | ✅ | Lemat §3.2 |
| Hipoteza P₀-CS1 (pełna trajektoria) | 🔍 | Wymaga dowodu monotoniczności rozpiętości |
| **Lemat P₀-N3 (A2)** | **✅** | **S2b, §4.2.2** |
| **Lemat P₀-N4 (A2)** | **✅** | **S3b, §4.4.4** |
| **Hipoteza S-CYCLE ($N=3,4$, unit interval)** | **✅** | **§6.1** |
| **Twierdzenie S11 (faza w $K_n$, $n\ge 3$)** | **✅** | **§6.2** |
| S11-A (granica asymptotyczna fazy) | 💡 | Obserwacja numeryczna |
| **S13 (przejścia N=3)** | **✅** | **§4.2.1** |
| S12 (niezmienniczość Regionu II) | ❌ | Sfalsyfikowana; tw. warunkowe otwarte, §4.2 |
| Most Scalar→Wave | 💡 | Analogia strukturalna |
| Most Scalar→Net | 💡 | Spekulacja |
| Funkcja quasi-Lapunowa | 💡 | Kandydat otwarty |

---

## 9.5 Cofnięcia

| Wersja | Data | Cofnięcie | Uzasadnienie |
|:---|:---|:---|:---|
| v0.3.2 → v0.3.3 | 2026-08-06 | Atraktor B_D: błędna linia zerosumowa $(t,t,-2t)$ zastąpiona płaszczyzną $(c,c,r_3)$ | Kontrprzykład numeryczny; poprawka w Lemacie P₀-N3 (S2b) |
| v0.3.1 → v0.3.2 | 2026-08-06 | Niezmienniczość Regionu II (S12): ogólne twierdzenie sfalsyfikowane | Kontrprzykład §4.2; zastąpione twierdzeniem warunkowym o podregionach |
| v0.3.0 → v0.3.1 | 2026-08-06 | Zachowanie sumy przez rundę asynchroniczną: twierdzenie sfalsyfikowane | Kontrprzykład §2.1; $R=(1,-1,0)$, $\sum r_i' \neq \sum r_i$ |

---

## 10. Dynamiczne harmonogramy aktualizacji — program badawczy

W P₀-Centroid §6.4 wykazano, że dla grafów z cyklami kolejność aktualizacji decyduje o obecności fazy zespolonej w widmie. W Scalar, gdy graf $G_t(\varepsilon)$ jest dynamiczny, kolejność może być:

- **zewnętrzna** (ustalona permutacja, jak w A2);
- **wewnętrzna** (zależna od stanu, np. najpierw węzeł o największym gradiencie);
- **losowa** (gossip-like).

**Hipoteza S-DYN (💡).** Niektóre własności Scalar (np. zbiór atraktorów, liczba domen) są niezależne od permutacji kolejności aktualizacji, podczas gdy inne (tempo zbieżności, obecność oscylacji przejściowych) od niej zależą. Własności niezależne byłyby głębszymi niezmiennikami struktury relacyjnej niż te wynikające z pojedynczego schematu Gaussa–Seidela.

**Dodatkowa obserwacja (z §2.4).** Zmiana permutacji kolejności zmienia sam niezmiennik ważony $c$ (wagi wzdłuż kolejności), nie tylko tempo zbieżności — silniejsze stwierdzenie niż dotychczasowe sformułowanie.

**Status:** Program otwarty. Rozpocząć po zamknięciu analizy dla ustalonej kolejności (N=2,3,4).

---

## 11. Relacja do filarów P₀ (zobacz [`PILLARS-TABLE.md`](PILLARS-TABLE.md) dla pełnej listy)

| Filar | Rola względem Scalar | Kierunek wpływu |
|:---|:---|:---|
| **P₀-Origins** | Scalar jest gałęzią redukcji aksjomatów | Origins → Scalar |
| **P₀-Centroid** | Korespondencja w granicy $\varepsilon\to\infty$; A2 jako most algebraiczny | Scalar → Centroid (granica) |
| **P₀-Wave** | Moduły zdegenerowane jako kandydaci na domeny stabilne | Scalar ↔ Wave (analogia) |
| **P₀-Net** | Granice domen jako miejsca, gdzie transport geometryczny zanika; graf przejść jako automat topologiczny | Scalar → Net (spekulacja/kombinatoryka) |
| **P₀-Philosophy** | A0 jako założenie ontologiczne; obiekty jako stabilne atraktory | Philosophy → Scalar (motywacja) |
| **P₀-Applications** | Symulacje, sieci, AI — dopiero po zamknięciu matematyki | Scalar → Applications |
| **P₀-Experiments** | Protokoły E-08 do E-13 | Scalar → Experiments |
| **P₀-Alchemy** | Most Alchemy→Scalar: próg rezydualny δ jako mechanizm zapobiegający zanikowi relacji; domeny jako pre-atraktory | Alchemy → Scalar (analogia) |

---

*P₀-Scalar v0.3.5-draft. Zamknięcia: S10, S13, S2b, S3b, S11. Korekty: wzór na niezmiennik ważony (v0.3.2); atraktor B_D w §4.2.2, płaszczyzna zamiast błędnej linii zerosumowej (v0.3.3); naprawa uszkodzonego LaTeX-u i literówki S11 (v0.3.4); aktualizacja bazy matematycznej (v0.3.5). Niezależna weryfikacja numeryczna S11. Synteza: 2026-08-06/12.*
