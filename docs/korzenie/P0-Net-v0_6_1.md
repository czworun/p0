# Korzeń: P₀-Net — adnotacja szefa lab. (v0.6.1, program 2026-09-13)

**Dokument:** „P₀-Net: Globalizacja lokalnej teorii relacji — z pamięcią strukturalną w sieci" v0.6.1-formal-draft (program badawczy; data nagłówka 2026-09-13; wg §30 cztery wersje tego samego dnia: v0.5 — B3 domknięte, v0.5.1 — uproszczenia §3/§10/§16, v0.6 — wchłonięcie P₀-Memory jako Część C, v0.6.1 — przywrócenie brakujących sekcji z Memory i scalenie numeracji §18+§19, §22+§23, §24+§25, §29 jako odsyłacze). Deklarowana pozycja: **filar globalizujący — trzy warstwy pod jedną nazwą** (§1.1): Część A transport lokalnych modeli ℝ⁴ (kopia Centroid) w reżimie izometrycznym, Część B sieć relacyjna kopii C¹(K₄) (kopia Defect) w reżimie dyssypatywnym — sprzężenie uśrednianiem na wspólnej krawędzi, Część C pamięć strukturalna w sieci (operator 𝔒). Seria P₀ składa się z filarów; tabela filarów wskazana w P₀-Relacja §7.0 jako jedno źródło prawdy (odsyłacz „P₀-Relacja" w liczbie pojedynczej; w repo dokument nazywa się P₀-Relacje — do pogodzenia przy PILLARS-TABLE). Baza: P₀-Centroid, P₀-Defect, P₀-Flow, P₀-Alchemy, P₀-Wave, wszystkie bez numerów wersji (własna zasada odsyłaczy §0; w repo Defect v0.8). Zasada redakcyjna §0 identyczna jak w Memory („żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia, którego dotyczy") — pre-echo Z0/Z3; statusy ✅/📚/🔍/💡/❌. Nagłówek deklaruje: „N9 ✅ zamknięte. B3 ✅ — most przez T_b. Memory wchłonięte jako Część C." Kolejka przewidywała v0.4.2 (fundament §1–11); dostarczono wersję o trzy generacje dalej — wpięcie wg obowiązującego wzorca; formalna pozycja (kandydatura na filar, rozliczenie liczby filarów, status korzenia Memory po wchłonięciu, nazwa Relacja/Relacje) — uregulowanie przy PILLARS-TABLE.

**Co bada:** globalizację lokalnej teorii P₀: czy struktura wypracowana dla jednej relacji rozciąga się na sieć wielu węzłów, i to na trzech skalach naraz (tabela §1.1 skala: model↔model / relacja↔relacja / klasa trajektorii). (A) Transport modeli bez deformacji: R: ℝ⁴_X → ℝ⁴_Y zachowujące p₀, V_ρ i metrykę G₄ (warunki 1–3 = transport geometryczny) albo dodatkowo sprzęgające generatory {M_m} koniugacją (warunek 4 = transport algebraiczny, R ∈ S₄); sieć 𝒩 = (V,E): transport na krawędzi (strukturalny, odwracalny) vs dynamika w węźle (słowo ρ_v(w), lokalna historia, zwykle nieodwracalna). (B) Sieć relacyjna kopii C¹(K₄): węzeł z aparatem Defect (V_ρ ⊕ V_cyc, P_cyc, T_a, T_b), sprzężenie uśrednianiem na wspólnej krawędzi (D-R1: Δ_R = |D_e^B − D_e^A|/(2√2)), warunek strukturalny transportu (P_cyc(e,f) = 0 dla przeciwległych ⟹ propagacja strukturalnie niemożliwa), macierz kanału M_ef = ∂(K₂D)_f/∂D_e, trzy warianty (Net-L diagonalny ❌; Net-G sektorowy + twardy próg, wszystko-albo-nic; Net-I ciągły F_λ, proporcjonalnie do λ). (C) Po wchłonięciu Memory: czy zanik pamięci wartościowej może zachodzić bez zaniku pamięci strukturalnej (𝓜(𝔒), H-MEM-1) — pytanie sieciowe: struktura, która przeżywa zanik stanu, niezależna od stanu początkowego. Drabina Części B (§14): K₄ →(geometria) M_ef →(kanał) R_e →(sprzężenie) F →(nieliniowość) propagacja.

**Najmocniejsze (formalnie ✅ i numerycznie 🔍; wyniki liczbowe Części C dwiema implementacjami):**
1. **B3 ✅ (§16) — most A↔B domknięty jako rozstrzygnięcie o tożsamości:** most nie polega na dosłownym utożsamieniu R^(A) ↔ R_e; Część A działa w reżimie izometrycznym (O(3,ℝ)), Część B w dyssypatywnym (uśrednianie); konsekwencje jawne (K1–K4): „Część A i Część B nie są dwiema reprezentacjami tego samego obiektu"; transport A nie transportuje kanału T_b; konkretna konstrukcja mostu 💡 otwarta (K4, zbieżne z M16b/M3); uzasadnienie przez Flow §8 (T_a = Euler–Arnold; T_b nie ma odpowiednika w 𝔤₄). Wzorzec Z0: pytanie „czy to ten sam obiekt" rozstrzygnięte precyzją definicji reżimów, nie eksperymentem; nagłówkowe „most przez T_b" = kierunek pewny, postać otwarta.
2. **Artefakt twardego progu (§13, ✅ dla wniosku):** efekt „wszystko-albo-nic" wariantu Net-G znika przy ciągłej aktywacji F_λ (Net-I, proporcjonalnie do λ); wniosek ✅: „Efekt wszystko-albo-nic = artefakt twardego progu" — pozorne zjawisko generowane przez konwencję implementacji; przejście binarne β 🔍; interferencja impulsów 🔍 (nieliniowy wzorzec przy spotkaniu). Spółbrzmienie z lekcją czwartego parametru K₂ (Część C): konwencja może wyglądać jak fizyka.
3. **N9 ✅ przeniesione z Centroid §8.1 (jedyny ✅ Części A):** stabilizator {δ(M_m)} w O(3,ℝ) to S₄. Uczciwość metodologiczna Części A wzorcowa: cały świeży materiał jawny jako 💡 (C1–C4, N1–N8, N10) — w tym C3 (klasy transportu: kontinuum O(3,ℝ) z wyróżnioną S₄) i C4 (T jako wyróżniony transport).
4. **Część C = P₀-Memory wchłonięte bez zmiany wyników (§17–§28):** definicja 𝓜(𝔒) ✅ (monoid słów S(𝔒), orbita słaba vs mocna, ω-granica; warunek dobrej określoności: jedna przestrzeń X — bez mostu zbiór 𝔒 nie jest dobrze określonym generatorem; R₄, K₁ kontrakcje ⇒ tylko orbita słaba; exp(tK) jedyny z orbitą mocną wg §2.3bis/§18); P-MEM-2 ✅ z definicji; M18 ❌ (faza poza ω-graniczną 𝓜 — definicja ślepa na tranzjent; odpowiedź negatywna, nie brak odpowiedzi; M19 otwarte); macierz most×tryb K₂ 🔍 (0,71% ± 0,09 / 67,76% ± 1,19 / 7,53% ± 0,66 / 86,11% ± 0,45; tryb K₂ determinant 10–95×, silniejszy niż wybór mostu; efekt we wszystkich 4 komórkach; okno ~7 rund; M16: szum 12,8%/2,4% vs 0,7–0,9%/0,1–0,13%); M17 🔍 (λ₂,₃ = 0,1533 ± 0,0740i, |λ| = 0,1703, ±25,77°/rundę, λ₄ = 0,1347; K nie komutuje z R₄: ‖[K,R₄]‖ = 0,103, ‖[K,M₀]‖ = ‖[K,M₁]‖ = 0,230, ‖[K,M₂]‖ = ‖[K,M₃]‖ = 0,117); ORB-05-R ✅ (425 klas trajektorii vs 209 klas końcowych, 720 kolejności, max RMS ~0,19748; naprawiony błąd order w m16_B_step). Zgodność wszystkich liczb z wpiętym poprzednio korzeniem P0-Memory-v0_3_7.md potwierdzona przy lekturze — spójność SSOT.
5. **Nowości redakcyjne v0.6.1 względem Memory (restauracja):** §17.1 typy 𝒜 (wygaszający: R₄, K₁) / ℬ (ochronny: K₂, próg δ) / 𝒟 (detekcja: P_cyc) z kluczową obserwacją, że nie muszą działać na jednej przestrzeni (R₄ na ℝ⁴; K₂, P_cyc na C¹(K₄)) — to źródło problemu dobrej określoności 𝓜; §17.2 zasada separacji realizacji i struktury (💡 program, nie twierdzenie o niezmienniczości); §17.3 zasada natywności przed konstrukcją; §21.1 stan tezy (najbezpieczniejsze sformułowanie: „zanik stanu nie musi oznaczać zaniku różnicowania przyszłej dynamiki"); §22.3 wyjaśnienie strukturalne: most A i B to dwa zanurzenia ι_A, ι_B generujące różne monoidy transformacji — brak a priori powodu, by 𝓜(ι_A(𝔒)) i 𝓜(ι_B(𝔒)) się pokrywały; tryb K₂ to dwa różne słowa w S(𝔒) — „zmiana jednego generatora w 𝔒 zmienia 𝓜(𝔒) mocniej niż zmiana całego zanurzenia ι" (formalne wzmocnienie zasady jawności parametrów); §18.2 pamięć trajektorii: Γ_T(x; 𝔒), robocza równoważność d_T, trzy poziomy obserwacji (stan końcowy ⊊ trajektoria → kompresja do ω-granicy) — kierunek M20; §26 konsekwencja: nie używać ORB-05-R jako dowodu H-MEM-1; warstwa III w dwóch wersjach 𝓜_ω(𝔒) i 𝓜_traj(𝔒,T).

**Koncesje i sęki (❌ i ograniczenia jawne):** most A↔B istnieje w v0.6.1 jako rozstrzygnięcie kierunku (przez T_b), nie konstrukcja — K4/M16b/M3 otwarte; Część A bez nowych wyników liczbowych i bez własnych ✅ (cały świeży materiał 💡: C1–C4, N1–N8, N10); jedyne świeże liczby to Część B (β, λ, interferencja 🔍 jedną ręką — do replikacji w warsztacie); Net-L ❌; R_full nie jest izometrią ✅ sfalsyfikowane (uśrednianie nie zachowuje normy G₄); zamrożenie D^cyc w moście A nadal decyzja konstrukcyjna (nie wynika z P₀); M16 nie rozstrzyga kanoniczności mostu; odsetek rozbieżnych prób = dolne oszacowanie |𝓜| lokalnie (nie pomiar na całym X); H-MEM-1 pozostaje 💡; M18 ❌ rozstrzygnięte negatywnie; N5: niezmienniczość fazy 25,77° względem transportu 💡 (priorytet niski) z jawnym komentarzem „Centroid §11.7: nie jest uniwersalna" — pierwszy głos w korpusie przeciwko uniwersalności fazy; B2 (addytywność defektu na łańcuchu >2 węzłów) 💡 wysoki; B4 (interpretacja 1/(2√2)) 💡 niski; B5 (redukcja Net→Wave: operator W na V_cyc) 💡 wysoki; dyskrepancja odsyłaczy wewnętrznych: §0 cytuje „wyjaśnienie strukturalne §8quater" (numeracja źródłowa Memory), §30 — „§22.3" (numeracja Net) — dwa systemy odsyłaczy w jednym dokumencie, zachowane verbatim.

**Struktury 💡:** trzy warstwy pod jedną nazwą (izometryczny / dyssypatywny / pamięć strukturalna) — tabela §1.1 jako mapa programu, ze skalą model↔model / relacja↔relacja / klasa trajektorii; transport vs dynamika (odwracalna struktura na krawędzi vs nieodwracalna historia w słowie) — rozróżnienie krzyżujące się z parą orbita mocna/słaba z Części C; drabina Części B: symetria K₄ → macierz kanału M_ef → sprzężenie R_e → nieliniowość F → propagacja — pięciostopniowa hierarchia od symetrii do zjawiska; klasy transportu geometrycznego: kontinuum O(3,ℝ) z wyróżnioną S₄ (algebraiczną); rozkład exact/cyclic jako warunek konstrukcyjny propagacji (P_cyc(e,f)); trzy poziomy obserwacji (stan końcowy ⊊ trajektoria → ω) i dwie wersje warstwy III (𝓜_ω, 𝓜_traj) z ORB-05-R jako uzasadnieniem rozdzielenia.

**Mosty 💡:**
1. **Faza 25,77° — piąty kontekst, pierwszy głos przeciw uniwersalności:** cztery wystąpienia wartości (SERC R₄ ∠25,772°; Estrada T4 §36; Flow — faza atraktora K₄; Memory M17, tu §24 wchłonięte) kontra jawne zastrzeżenie N5 z komentarzem Centroid §11.7 („nie jest uniwersalna"). N5 czyta się jako pytanie, czy faza jest cechą pojedynczego modelu (identyfikator lokalny), czy klasy modeli powiązanych transportem algebraicznym S₄ — pytanie Estrada-03 (identyfikator lokalny czy stała uniwersalna) ma teraz obie streszczone strony w jednym filarze; do rozliczenia przy Estrada.
2. **Architecture mismatch czwarty raz i najdalej sformalizowany:** Flow §3.2, AI §7.1, Memory §6.1, tu §22.3/M16b — brak kanonicznego podstawienia R₄: C¹(K₄)→C¹(K₄) podniesiony do pytania o niezmienniczość 𝓜(ι(𝔒)) względem klasy zanurzeń ι; przy scaleniu pnia jedna pozycja atlasu, z Net jako filarem referencyjnym formalizacji.
3. **Dwa reżimy jednej rodziny (B3) spółbrzmiące z Lattice:** rozstrzygnięcie „nie dwie reprezentacje, dwa reżimy" i rejestr Lattice (rodzina Defect/Flow/TETRA-20/Lattice = jeden obiekt na różnych podgrupach) razem dają mapę: co scala obiekty P₀ (podgrupa), a co je rozdziela (reżim dynamiczny: izometryczny vs dyssypatywny) — do zebrania przy PILLARS-TABLE.
4. **Oś trybu aktualizacji jako parametr pierwszorzędny korpusu:** czwarty parametr K₂ (wsadowy/sekwencyjny, tu jako różne słowa monoidu S(𝔒), nie interpretacje jednego słowa), 720 kolejności Gauss-Seidel w ORB-05-R, P1/R_sym rodzina symultaniczna DeepSeeka w Lattice, konwencja per-wierzchołkowa notatnika Stalka — cztery konteksty, jedna oś; Net daje jej podbudowę formalną (𝓜 wrażliwe na każdy generator z osobna).
5. **Trzecia absorpcja w korpusie i pierwsza z przekazaniem dalej:** Flow §12A-G i Hilbert §12H w Defect, Memory jako Część C w Net v0.6 — wzorzec: korzeń źródłowy zostaje wpięty jako źródło (SSOT), treść programowa żyje w absorberze; aplikacje Memory (obraz, film, kolor, M5/M7/M9/M10) przekazane do P₀-Applications, most Centroid↔Defect (Memory §6) przeniesiony do Defect §12 (H-Bridge) — łańcuch promocji treści w dół kolejki; status korzenia Memory przy PILLARS-TABLE uregulować tak jak Flow (źródło zamrożone, kontynuator żyje).
6. **Hierarchia poziomów Centroid/Wave/Net (§7):** Centroid = lokalna algebra, Wave = lokalna dynamika, Net Część A = transport — B5 (operator W na V_cyc) jako hipoteza zamknięcia hierarchii od dołu.

**Sęk-odnogi (§6, §15, §27, z priorytetami):** wysokie: N1 (klasyfikacja transportów), N2 (złożenie), N4 (klasa propagacyjna), N10 (transport słowa T_e), B2, B5, M1 (dowód H-MEM-1), M3 (konkretny most A↔B), M16b (kanoniczność mostu i trybu K₂), M19 (czulsza definicja), M20 (metryka trajektorii); średnie/niskie: C1–C4, N3, N6, N7, N8, B4, M2, M4, M6, M8; przeniesione do P₀-Applications: M5, M7, M9, M10 (deklaracja §27, odsyłacze Applications §3.7 i §6); zamknięte w v0.6.1: N9 ✅ (§6), B3 ✅ (§16), B1 ✅ (Defect §9.1), M17 spektralna 🔍 (§24), M18 ❌ (§18.1), ORB-05-R ✅ (§26); z Memory nadal aktualne: trzecia niezależna replikacja macierzy M16a, pytanie M16b o oryginalny tryb K₂ z Defect (v0.5/v0.8), zgodność z historycznym ORB-04.

**Statusy (mapa na Z1):** dokument programowo integracyjny: jedynymi świeżymi liczbami są wyniki Części B (β, λ, interferencja, 🔍 jedną ręką — do replikacji w warsztacie); ✅ dziedziczone: N9 (Centroid §8.1), D-R1/D-R3/D-R2 (Defect §9/§14), B1 (Defect §9.1), Część C (dwie ręce w korzeniu źródłowym Memory: oryginał + Claude); wniosek o artefakcie progu ✅ dedukowany z 🔍. Część C liczbowo tożsama z korzeniem P0-Memory-v0_3_7.md (różnice skrótowe bez sprzeczności: brak residuum 0,081 i porównania z v0.3.2.1 w treści Net). Net nie podnosi żadnego statusu komponentów i deklaruje to wprost („formalizm nie dodaje nowych wyników numerycznych", §22.3) — wzorzec uczciwości Z2.

**Uwagi redakcyjne (verbatim):** oryginał kończy się bez końcowego EOL (jak Wave, AI, Defect, Flow, Lattice; inaczej niż Memory — zachowane); 29 800 B, 523 linie, md5 0778d84383dd157fa5d9301be23401d3 (kopia robocza); data nagłówkowa 2026-09-13 wspólna czterem wersjom (§30); dyskrepancja odsyłaczy §0 („§8quater" — numeracja Memory) vs §30 („§22.3" — numeracja Net); sekcje zarezerwowane widoczne jako ślady scalenia: §19 „(zarezerwowane — scalone do §18)", §20 „(zarezerwowane — odsyłacz do §26)", §25 „(zarezerwowane — scalone do §24)"; odsyłacz „tabela filarów w P₀-Relacja §7.0" w lp. vs repo P₀-Relacje l.mn.; notacja kaligraficzna 𝒩/𝓜/𝔒/𝒜/ℬ/𝒟 i bloki LaTeX; polski przecinek dziesiętny (0,71%–86,11%; 0,1533 ± 0,0740i); ostatni wiersz dokumentu: „P₀-Net v0.6.1-formal-draft. Część A (transport modeli ℝ⁴) + Część B (sieć relacyjna C¹(K₄)) + Część C (pamięć strukturalna w sieci). Odwołania do innych filarów bez numeru wersji. Synteza: 2026-09-13."
P₀-Net v0.6.1

Globalizacja lokalnej teorii relacji — z pamięcią strukturalną w sieci

Wersja: 0.6.1-formal-draft
Status: Program badawczy. N9 ✅ zamknięte. B3 ✅ — most przez T_b. Memory wchłonięte jako Część C.
Data: 2026-09-13
Baza: P₀-Centroid, P₀-Defect, P₀-Flow, P₀-Alchemy, P₀-Wave
Zmiana v0.6 → v0.6.1: przywrócono brakujące sekcje z Memory (𝒜/ℬ/𝒟, zasada separacji realizacji i struktury, zasada natywności, stan tezy, wyjaśnienie strukturalne §8quater). Usunięto redundancje (§18+§19 scalone, §20→§26, §22+§23 scalone, §29→odsyłacze). Wszystkie odwołania do filarów bez numeru wersji.

---

0. Zasada redakcyjna

Żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia, którego dotyczy.

Statusy: ✅ Dowiedzione · 📚 Klasyczne · 🔍 Zweryfikowane numerycznie · 💡 Przypuszczenie · ❌ Sfalsyfikowane.

Uwaga o odsyłaczach. Wszystkie odwołania do innych filarów używają nazwy filaru i numeru sekcji (np. „Centroid §8"), bez numeru wersji.

---

1. P₀ jako trylogia i fundament filarów

Seria P₀ składa się z filarów — zob. tabela filarów w P₀-Relacja §7.0 (jedno źródło prawdy).

Zasada niezależności. Każdy filar może ewoluować autonomicznie.

1.1. Uwaga architektoniczna — trzy warstwy Net

P₀-Net rozwija trzy warstwy pod jedną nazwą:

 Część A Część B Część C
Lokalny węzeł kopia ℝ⁴ (Centroid) kopia C¹(K₄) (Defect) operator 𝔒
Transport izometria R ∈ O(3,ℝ) uśrednianie na wspólnej krawędzi —
Skala model ↔ model relacja ↔ relacja klasa trajektorii
Reżim izometryczny dyssypatywny pamięć strukturalna

§16 domyka most A ↔ B. §17–§28 (Część C) formalizuje pamięć strukturalną w sieci.

---

CZĘŚĆ A — Transport modeli ℝ⁴

2. Motywacja

P₀-Centroid i P₀-Wave operują na pojedynczej przestrzeni ℝ⁴. Ta przestrzeń opisuje lokalny układ odniesienia relacji, nie wymiar globalny.

3. Lokalny model P₀

Definicja lokalnego modelu z Centroid §1:
X = (\mathbb{R}^4, p_0, \mathfrak{g}_4, G_4, \{M_0, M_1, M_2, M_3, T\}).

Szczegółowe definicje: zob. Centroid §1–§8.

4. Transport między modelami

Definicja (💡). R: ℝ⁴_X → ℝ⁴_Y spełniający:

1. R(p_0^(X)) = p_0^(Y),
2. R(V_ρ^(X)) ⊆ V_ρ^(Y),
3. R jest izometrią względem G₄ na V_ρ.

Warunek opcjonalny (4) — N9. R{M_m^(X)}R⁻¹ = {M_k^(Y)}. Warunki (1)–(3) definiują transport geometryczny; warunek (4) zawęża do transportu algebraicznego (R ∈ S₄).

Cel Pytanie Status
C1 Czy (1)–(3) wymuszają sprzężenie generatorów? 💡 — twierdząco tylko dla R ∈ S₄
C2 Czy złożenie transportów jest transportem? 💡
C3 Ile jest klas transportu? 💡 — kontinuum O(3,ℝ), S₄ wyróżniona
C4 Czy T jest wyróżnionym transportem? 💡

5. Sieć lokalnych modeli

Definicja (💡). 𝒩 = (V, E), węzły = modele X_v, krawędzie = transport R_e: X_u → X_v.

Ruch Odwzorowanie Charakter
Transport (krawędź) R_e: X_u → X_v Strukturalny, odwracalny
Dynamika (słowo) ρ_v(w): X_v → X_v Lokalna historia, zazwyczaj nieodwracalna

6. Otwarte problemy Części A

# Problem Status Priorytet
N1 Klasyfikacja transportów 💡 Wysoki
N2 Zamknięcie złożenia 💡 Wysoki
N3 Zachowanie projektorów 💡 (dla izometrii: ✅ algebraicznie) Średni
N4 Zachowanie klasy propagacyjnej 💡 Wysoki
N5 Niezmienniczość fazy 25,77° 💡 (Centroid §11.7: nie jest uniwersalna) Niski
N6 Drzewo czy cykle/siatki? 💡 Średni
N7 Przestrzeń graniczna dla nieskończonej sieci 💡 Niski
N8 Status operatora T 💡 Średni
N9 Stabilizator {δ(M_m)} w O(3,ℝ) to S₄ ✅ (Centroid §8.1) Wysoki
N10 Transport słowa T_e zgodny z R_e 🔍/💡/❌ Wysoki

7. Relacja Części A do Centroid/Wave

Poziom Dokument Co opisuje
1 Centroid Lokalna algebra i geometria
2 Wave Lokalna dynamika
3 Net, Część A Transport modeli ℝ⁴

8. Podsumowanie Części A

Intuicja Sformalizowana wersja Status
„ℝ⁴ to nie wymiar świata" Lokalny model jako kod relacji 💡
„Transport bez deformacji" R_e zachowujący p_0, V_ρ, G₄ 💡
„Transport geometryczny vs algebraiczny" O(3,ℝ) vs S₄ 💡, N9 ✅

---

CZĘŚĆ B — Sieć relacyjna C¹(K₄)

9. Baza i status

Ta część nie duplikuje algebry Defect — odwołuje się do niej. Węzeł sieci to kopia C¹(K₄) z aparatem Defect: V_ρ ⊕ V_cyc, V_cyc ≅ Λ²(V_ρ), P_cyc, T_a, T_b.

10. Operator sprzężenia R_e

Dla dwóch węzłów A, B dzielących jedną wspólną krawędź e:
R_e(D_e^A, D_e^B) = \left(\tfrac{D_e^A+D_e^B}2, \tfrac{D_e^A+D_e^B}2\right).

Twierdzenie D-R1 (✅, Defect §9). Δ_R(A) = |D_e^B − D_e^A|/(2√2).

Szczegółowe definicje D-R1, D-R3 i dowody: zob. Defect §9.

11. Warunek strukturalny transportu

Fakt (✅, Defect §7). P_cyc(e,f) = 0 dla krawędzi przeciwległych, ≠ 0 dla sąsiednich.

Konsekwencja dla topologii sieci (✅). Para przeciwległa interfejsów → propagacja strukturalnie niemożliwa.

12. Trzy warianty modelu

Wariant K₂ Propagacja?
Net-L diagonalny ❌
Net-G sektorowy + twardy próg ✅ wszystko-albo-nic
Net-I ciągły F_λ ✅ proporcjonalnie do λ

Macierz kanału (✅). M_ef = ∂(K₂D)_f/∂D_e: M_ef = 0 ⟹ brak kanału pierwszego rzędu.

13. Wyniki eksperymentalne

Parametr β (🔍). Przejście binarne przy twardym progu.
Parametr λ (🔍). Efekt „wszystko-albo-nic" znika przy ciągłej aktywacji.
Wniosek (✅). Efekt wszystko-albo-nic = artefakt twardego progu.
Interferencja (🔍). Nieliniowy wzorzec przy spotkaniu dwóch impulsów.

14. Trzy poziomy architektury

K_4 \xrightarrow{\text{geometria}} M_{ef} \xrightarrow{\text{kanał}} R_e \xrightarrow{\text{sprzężenie}} F \xrightarrow{\text{nieliniowość}} \text{propagacja}.

Twierdzenie D-R2 (✅). Pełna synchronizacja redukuje się do uśredniania potencjałów: Δ_R ≡ 0. Defekt = zjawisko częściowego współdzielenia.

R_full nie jest izometrią (✅, sfalsyfikowane). Uśrednianie potencjałów nie zachowuje normy G₄.

15. Otwarte problemy Części B

# Problem Status Priorytet
B1 Uogólnienie D-R1 na współdzielenie wierzchołka ✅ (Defect §9.1) —
B2 Addytywność defektu na łańcuchu >2 węzłów 💡 Wysoki
B3 Most Część A ↔ Część B ✅ (§16) —
B4 Interpretacja 1/(2√2) 💡 Niski
B5 Redukcja Net → Wave: operator W na V_cyc 💡 Wysoki

16. Most Część A ↔ Część B

Twierdzenie (✅). Most nie polega na dosłownym utożsamieniu R^(A) ↔ R_e. Część A działa w reżimie izometrycznym (O(3,ℝ)), Część B — w reżimie dyssypatywnym (uśrednianie). Most, jeśli istnieje, musi być nietrywialny.

Uzasadnienie: zob. Flow §8 (identyfikacja T_a = Euler–Arnold; T_b nie ma odpowiednika w 𝔤₄).

Konsekwencje dla Net:

· (K1) Część A i Część B nie są dwiema reprezentacjami tego samego obiektu.
· (K2) Transport Części A nie transportuje kanału T_b.
· (K3) Net opisuje dwa różne reżimy: izometryczny i dyssypatywny.
· (K4) Konkretna konstrukcja mostu — 💡 otwarta.

---

CZĘŚĆ C — Pamięć strukturalna w sieci

17. Motywacja i zakres

Cel. Część B opisuje propagację defektu w sieci. Część C pyta: czy istnieje struktura, która przeżywa zanik stanu — informacja o klasie możliwych zachowań, niezależna od konkretnego stanu początkowego.

Uwaga kontekstowa. Podczas gdy §2 motywuje Część A przez potrzebę transportu lokalnych modeli, §17 motywuje Część C przez pytanie o pamięć strukturalną: czy zanik amplitudy pociąga za sobą zanik informacji o strukturze dynamiki?

Trzy poziomy informacji w P₀ (z Memory §1):

Poziom Obiekt Rola
I. Pamięć wartościowa aktualny stan R stan chwilowy
II. Pamięć relacyjna Δ(R) = ‖P_cyc R‖ miara defektu
III. Pamięć strukturalna 𝓜(𝔒) klasa możliwych zachowań

Główne pytanie Części C:

Czy zanik pamięci wartościowej może zachodzić bez zaniku pamięci strukturalnej?

Zakres. Wchłonięto z Memory: definicja 𝓜(𝔒) (§18), H-MEM-1 (§21), eksperymenty M16/M16a/M16b/M17 (§22–§25), ORB-05-R (§26), problemy M19/M20 (§27).

Uwaga o zakresie. Aplikacje Memory (film, kolor, przetwarzanie obrazu) przeniesione do P₀-Applications. Most Centroid↔Defect (Memory §6) przeniesiony do Defect §12 (kontekst H-Bridge).

17.1. Trzy typy operatorów

W Memory §3 rozróżniono trzy typy operatorów:

Typ Rola Przykład
𝒜 dynamika wygaszająca R₄, K₁
ℬ dynamika ochronna K₂, próg δ
𝒟 detekcja P_cyc

Kluczowa obserwacja metodologiczna. 𝒜, ℬ, 𝒟 nie muszą działać na tej samej przestrzeni. 𝒜 = R₄ działa na ℝ⁴ (Centroid). ℬ = K₂ działa na C¹(K₄) (Defect/Alchemy). 𝒟 = P_cyc działa na C¹(K₄). To jest źródło problemu dobrej określoności 𝓜(𝔒) (§18) — bez mostu (§16) zbiór 𝔒 nie jest dobrze określonym generatorem.

17.2. Zasada separacji realizacji i struktury

Zasada (💡). Istnieje rozróżnienie między strukturą reguły dynamicznej a sposobem jej realizacji na konkretnej przestrzeni stanów. Jeżeli ta sama jakościowa zależność między regułą a atraktorem występuje dla różnych realizacji mostu, wówczas efekt może być własnością reguły dynamicznej, a nie konkretnej reprezentacji operatora.

Formalnie: stan → realizacja dynamiki → struktura przyszłych trajektorii. To środkowe ogniwo jest przedmiotem M16/M16a.

Status: 💡. Nie jest to twierdzenie o niezmienniczości względem wszystkich realizacji — jest to program badawczy wskazujący, gdzie szukać niezmienniczości.

17.3. Zasada natywności przed konstrukcją

Zasada (💡). Przed dalszą rozbudową mostów (M16b) warto systematycznie sprawdzić, czy Centroid lub Defect osobno już zawierają kandydatów na pamięć strukturalną, zanim zakłada się, że trzeba je sztucznie łączyć.

Uzasadnienie. M17 (§25) pokazuje, że zanim buduje się most między dwiema przestrzeniami (jak w M16/M16a), warto sprawdzić, czy poszukiwana własność nie jest już obecna wewnątrz jednej, natywnej struktury — bez potrzeby mostu w ogóle.

Kandydat wymagający najmniej dodatkowych założeń modelowych ma pierwszeństwo przed kandydatem wymagającym mostu, dopóki oba nie zostaną ocenione na równych zasadach.

18. Definicja formalna 𝓜(𝔒)

Warunek dobrej określoności (✅). Definicja wymaga, aby wszystkie elementy 𝔒 były odwzorowaniami tej samej przestrzeni X w siebie: 𝔒 ⊆ Map(X,X). W P₀ nie jest to spełnione automatycznie — M_m, T działają na X = ℝ⁴, natomiast K₁, K₂, P_cyc działają na X = C¹(K₄). Zbiór 𝔒 = {M_m, T, P_cyc, K, …} nie jest dobrze określonym generatorem dopóki nie wybierze się jednej wspólnej przestrzeni X i nie sprowadzi każdego operatora do Map(X,X) — czyli dopóki nie wybierze się mostu (§16).

To jest dokładny, formalny powód, dla którego „Zasada rozdzielenia modelu od mostu" musiała zostać wprowadzona. Bez niej 𝔒 zapisuje wyrażenie, które nie ma matematycznego sensu.

Definicja (monoid słów). Niech X będzie ustaloną przestrzenią, 𝔒 = {o₁,…,o_k} ⊆ Map(X,X). Niech 𝔒* będzie wolnym monoidem nad alfabetem 𝔒. Homomorfizm π: 𝔒* → Map(X,X), π(o_{i_n}⋯o_{i_1}) = o_{i_n}∘⋯∘o_{i_1}, definiuje monoid transformacji generowany przez 𝔒: S(𝔒) := π(𝔒*) ⊆ Map(X,X).

Definicja (orbita słaba). Dla x ∈ X:
\mathcal{O}^+_{\mathfrak{O}}(x) := \{w(x) : w \in S(\mathfrak{O})\} = S(\mathfrak{O})·x \subseteq X.


Istnieje zawsze, niezależnie od odwracalności generatorów.

Definicja (orbita mocna, przypadek szczególny). Jeśli każde oᵢ ∈ 𝔒 jest bijekcją X, generują one podgrupę G(𝔒) ≤ Sym(X), a orbita mocna to 𝒪_𝔒(x) := G(𝔒)·x.

Fakt (✅). R₄, K₁ nie są bijekcjami na X (kontrakcje właściwe), więc dla 𝔒 zawierającego którykolwiek z nich orbita mocna nie istnieje — dostępna jest wyłącznie orbita słaba 𝒪⁺. Generator rotacyjny K (Centroid §2.5, exp(tK) ortogonalne) jest odwracalny, więc {exp(tK)} generuje orbitę mocną — jest to jedyny dotąd zidentyfikowany w P₀ generator, dla którego orbita mocna istnieje.

Definicja (klasa asymptotyczna / ω-granica). Zakładamy topologię na X. Dla x ∈ X:
\omega_{\mathfrak{O}}(x) := \bigcap_{N\geq 0} \operatorname{cl}\bigl(\{w(x) : w \in \mathfrak{O}^*, |w| \geq N\}\bigr).

Definicja (𝓜(𝔒)). Relacja x ∼_𝔒 y ⟺ ω_𝔒(x) = ω_𝔒(y) jest równoważnością na X:
\mathcal{M}(\mathfrak{O}) := X/\!\sim_{\mathfrak{O}}.

To zbiór różnych granic asymptotycznych {ω_𝔒(x) : x ∈ X}. Klasa = maksymalny zbiór stanów początkowych dzielących ten sam los asymptotyczny.

P-MEM-2 (✅ z definicji). 𝓜(𝔒) zależy wyłącznie od pary (X, 𝔒) — nie odwołuje się do żadnego wyróżnionego R₀. To, co pozostaje nietrywialne, to: (a) czy |𝓜(𝔒)| > 1, (b) czy 𝓜(𝔒) ≠ 𝓜(𝔒') dla dwóch różnych realizacji tej samej reguły abstrakcyjnej.

18.1. Konsekwencje dla M18

Fakt (✅). Dla 𝔒 = {R₄} samego w sobie, ω_𝔒(x) = {p₀} dla (praktycznie) każdego x na V_ρ (zbieżność geometryczna R₄ᵏ(x) → p₀, Centroid §4). Zatem |𝓜({R₄})| = 1 — pojedyncza klasa.

Wniosek dla M18 (❌). Faza spirali θ(k) (§25) jest własnością tranzjentu (skończonego odcinka trajektorii przed osiągnięciem rozdzielczości numerycznej), nie własnością zbioru ω-granicznego — a 𝓜(𝔒) w definicji §18 widzi wyłącznie ω-granicę.

Formalny wniosek. Faza nie jest elementem 𝓜({R₄}) w sensie §18 — nie dlatego, że została odrzucona empirycznie, lecz dlatego, że sama definicja 𝓜 poprzez ω-graniczność jest ślepa na informację tranzjentową.

Co by było potrzebne, żeby faza jednak liczyła się do pamięci strukturalnej. Trzeba by zastąpić ω-graniczną równoważność czymś czulszym na tranzjent — np. równoważnością dwóch trajektorii jako tej samej krzywej z dokładnością do reparametryzacji czasu i skali, albo osobną, nie-ω-graniczną definicją warstwy III dla generatorów zawierających podalgebrę rotacyjną. Żadna z tych konstrukcji nie jest tu wykonana — to jest jawnie otwarty problem (M19).

18.2. Pamięć trajektorii — rozszerzenie po ORB-05-R

Motywacja. ORB-05-R (§26) pokazał, że klasyfikacja pełnej trajektorii może rozróżniać przebiegi, które mają ten sam lub bardzo podobny stan końcowy. Pamięć asymptotyczna z §18 nie jest wystarczającym obserwablem dla pytania „jak system doszedł do stanu końcowego".

Definicja trajektorii skończonej. Dla ustalonego generatora i liczby kroków T:
\Gamma_T(x; \mathfrak{O}) = (x_0, x_1, \ldots, x_T), \qquad x_0 = x,


gdzie każdy x_{t+1} powstaje przez jawnie określony krok dynamiki. Dla wersji relacyjnej można stosować projekcję Γ^cyc_T(x; 𝔒) = (P_cyc x_0, …, P_cyc x_T).

Definicja równoważności trajektorii — robocza. Dla ustalonego T i metryki d_T:
x \sim^{(T)}_{\rm traj} y \Longleftrightarrow d_T(\Gamma_T(x; 𝔒), \Gamma_T(y; 𝔒)) \leq \varepsilon.

To definicja robocza, nie kanoniczna.

Rozdzielenie trzech poziomów obserwacji. Należy rozróżnić:

1. stan końcowy x_T — obserwacja jednego punktu;
2. trajektorię skończoną Γ_T — historia dojścia;
3. ω-granicę ω_𝔒(x) — informację asymptotyczną o losie trajektorii.

Formalnie: x_T ⊊ Γ_T (informacyjnie), Γ_T → ω_𝔒(x) (kompresja do granicy).

Wniosek metodologiczny. Jeżeli pamięć strukturalna ma zachowywać informację o sposobie realizacji procesu, potrzebny jest obiekt czulszy od ω-granicy. Naturalnym kandydatem jest klasa pełnych trajektorii, ale jej definicja musi być odporna na arbitralną parametryzację czasu i dobór metryki. To jest problem M20.

19. (zarezerwowane — scalone do §18)

20. (zarezerwowane — odsyłacz do §26)

21. H-MEM-1 — pamięć strukturalna po wygaszeniu

Sformułowanie opisowe. A^k(R₀) → p₀ ⇏ 𝓜(𝔒) → ∅ — zanik stanu nie implikuje zaniku przestrzeni możliwych przyszłych zachowań.

Sformułowanie formalne (w języku §18). Niech A = {A} ⊊ 𝔒 (np. A = R₄), z |𝓜({A})| = 1 (klasa trywialna). H-MEM-1 twierdzi:
|\mathcal{M}(\mathfrak{O})| > 1 \quad \text{dla pełnego } \mathfrak{O} \supseteq \{A\} \cup \mathcal{B} \cup \mathcal{D},


tj. dołączenie operatora ochronnego ℬ (próg δ, K₂) i/lub detekcyjnego 𝒟 (P_cyc) do generatora zwiększa liczbę klas ω-granicznych ponad jedną, mimo że sama dynamika A ściąga każdy punkt do wspólnego p₀.

Status: 💡 hipoteza, wsparta eksperymentalnie przez M16/M16a/M16a-K2/M17.

21.1. Stan tezy po Memory

Najbezpieczniejsze sformułowanie. Zanik stanu nie musi oznaczać zaniku różnicowania przyszłej dynamiki.

Ostrożniej. Różne reguły strukturalne (most × tryb K₂) mogą prowadzić do różnych atraktorów przy tym samym R₀ — i robią to we wszystkich czterech zbadanych kombinacjach, choć z siłą różniącą się o dwa rzędy wielkości.

Trzecia linia wsparcia (M17). Sama algebra 𝔤₄, bez żadnego mostu do Defect, już zawiera rozkład na część zanikającą (amplituda) i część, która w danym oknie czasowym niesie dodatkową informację niezależną od amplitudy (faza). Choć K sam w sobie nie jest tym mechanizmem (nie komutuje z R₄).

Formalnie. Takie reguły/struktury są różnymi elementami 𝓜(𝔒) dokładnie wtedy, gdy indukują różną relację ∼_𝔒 (§18).

22. M16/M16a — eksperymenty na moście

22.1. M16 — deterministyczny efekt strukturalny (most A)

Cel. Sprawdzić, czy efekt różnicowania atraktorów (obserwowany wcześniej przy wymuszeniu szumowym) pozostaje po zastąpieniu szumu deterministyczną dynamiką R₄.

Parametry. δ = 1, D₀ ∼ N(0,2), 500–2000 prób, wiele ziaren, 6 krawędzi K₄. K₂ wsadowe.

Wynik (🔍).

Wskaźnik szum σ=0,15 M16, most A, K₂ wsadowe
rozbieżne próby 12,8% 0,7–0,9%
rozbieżne krawędzie 2,4% 0,1–0,13%

Wynik jakościowy zachowany: 𝔒_ref ≠ 𝔒'_ref ⟹ możliwe różne atraktory dla tego samego D₀. Efekt ~rząd wielkości słabszy.

Czas trwania efektu (🔍). Przetestowano długości 7, 15, 30, 60, 120 kroków. Ta sama stopa rozbieżności ≈0,90% dla wszystkich długości — rozbieżność powstaje w początkowym oknie dynamiki (R₄^k(x₀) → p₀ zanika geometrycznie w ~7 rundach).

Ograniczenie. Zamrożenie D^cyc_t = D^cyc_0 jest decyzją konstrukcyjną, nie wynika automatycznie z P₀. M16 nie rozstrzyga kanoniczności mostu.

22.2. M16a — most B + macierz 2×2 (most × tryb K₂)

Cel. Sprawdzić, czy efekt różnicowania atraktorów jest niezależny od konstrukcji mostu.

Mosty. Most A: przez potencjał. Most B: operator R̃₄ bezpośrednio na krawędziach (uśrednianie po sąsiadach w grafie liniowym L(K₄)).

Odkryty czwarty parametr (🔍). Sposób odczytu referencji 𝔒'_ref = sign(D_t) wewnątrz jednej rundy:

· K₂ wsadowe: referencja sign(D_t) liczona raz, z pełnego zrzutu D_t sprzed rundy.
· K₂ sekwencyjne: poprawka progowa stosowana krawędź po krawędzi; referencja dla krawędzi e odczytywana „na żywo" z już częściowo poprawionego wektora.

Różnica w wyniku sięga 10–95×, czyli jest znacznie silniejsza niż różnica między mostem A i B.

Wynik — macierz 2×2 (🔍). Protokół: δ = 1, D₀ ∼ N(0,2), T = 30 kroków, 5 ziaren × 2000 prób na komórkę.

Wariant rozbieżne próby rozbieżne krawędzie
Most A, K₂ wsadowe 0,71% ± 0,09 0,12% ± 0,02
Most A, K₂ sekwencyjne 67,76% ± 1,19 17,64% ± 0,48
Most B, K₂ wsadowe 7,53% ± 0,66 1,41% ± 0,13
Most B, K₂ sekwencyjne 86,11% ± 0,45 33,36% ± 0,31

22.3. Dominacja trybu K₂ i interpretacja strukturalna

Wnioski (🔍).

1. Tryb K₂ jest dominującym czynnikiem siły efektu (10–95×), silniejszym niż wybór mostu.
2. Wybór mostu jest czynnikiem drugorzędnym: silny w reżimie wsadowym (~10×), niemal znika w reżimie sekwencyjnym (~1,3×).
3. Twierdzenie „efekt jest niezależny od mostu" jest lepiej uzasadnione jako stwierdzenie warunkowe na tryb sekwencyjny.
4. Efekt występuje we wszystkich czterech komórkach macierzy (nigdy nie spada do 0%).

Co „rozbieżne próby" naprawdę mierzy. W języku §18, dwa bliskie warunki początkowe x,y uznane za „rozbieżne", to empiryczny sygnał, że ω_𝔒(x) ≠ ω_𝔒(y) — czyli że lokalnie, w otoczeniu D₀, 𝔒 nie sprowadza wszystkiego do jednej klasy. Odsetek „rozbieżnych prób" jest więc dolnym oszacowaniem liczby klas |𝓜(𝔒)| ograniczonej do próbkowanego sąsiedztwa D₀ — nie jest pomiarem |𝓜(𝔒)| na całym X.

Dlaczego most A ≠ most B strukturalnie. §18 wymaga jednej przestrzeni X. Most A i most B to dwa różne, konkretne zanurzenia ι_A, ι_B: (reguła abstrakcyjna) → Map(ℝ⁶,ℝ⁶) tej samej intencji „przenieś R₄ na krawędzie". Nie ma a priori żadnego powodu, dla którego S(ι_A(𝔒)) i S(ι_B(𝔒)) miałyby generować tę samą relację ∼_𝔒 na ℝ⁶ — to są różne monoidy transformacji działające na tej samej przestrzeni, nie dwie reprezentacje jednego monoidu. Wynik M16a (efekt silniejszy dla mostu B niż A w trybie wsadowym) jest więc dokładnie tym, czego formalizm każe się spodziewać: 𝓜(ι_A(𝔒)) i 𝓜(ι_B(𝔒)) nie mają żadnego strukturalnego powodu, by się pokrywać, dopóki most nie zostanie wybrany kanonicznie (M16b).

To samo dla trybu K₂. Tryb wsadowy i sekwencyjny K₂ to dwa różne elementy S(𝔒) (różne słowa — jedna aktualizacja „naraz" vs sześć aktualizacji Gaussa-Seidela), nie dwie interpretacje jednego elementu. Wniosek §22.3 pkt 1 mówi w tym języku: zmiana jednego generatora w 𝔒 zmienia 𝓜(𝔒) mocniej niż zmiana całego zanurzenia ι. To wzmacnia — teraz formalnie — wniosek „zasady jawności parametrów dynamiki".

Status. Formalizm nie dodaje nowych wyników numerycznych do M16/M16a — reinterpretuje istniejące w sposób, który czyni pytanie o kanoniczność mostu (M16b) precyzyjnym pytaniem o niezmienniczość 𝓜, zamiast pytaniem o zgodność procentów.

23. M16b — kanoniczność mostu i trybu K₂

Problem (💡). Poszukiwanie kanonicznego operatora R̃₄^can: C¹(K₄) → C¹(K₄) oraz reguły K₂^can, które:

1. są naturalne z punktu widzenia algebry 𝔤₄,
2. zachowują rozkład exact/cyclic,
3. generują analogiczne okno aktywności,
4. dają wyniki porównywalne z mostami A i B w obu trybach K₂.

Propozycja. Rozważyć R̃₄^can jako reprezentację pochodną algebry 𝔤₄ na C¹(K₄) — działanie „z góry" (od algebry do przestrzeni krawędzi), a nie „z dołu" (od operatora uśredniającego). Dla K₂ analogicznie: sprawdzić, czy istnieje wyróżniony tryb wynikający z tego, jak K₂ jest zdefiniowany w Defect.

Status: 💡 (program badawczy).

Interpretacja w języku §18. Kanoniczność mostu to pytanie, czy istnieje wyróżnione ι, dla którego 𝓜(ι(𝔒)) jest niezmiennicze względem klasy dopuszczalnych ι — pytanie o niezmienniczość samego 𝓜, nie tylko o zgodność liczb.

24. M17 — faza spirali R₄ jako natywny kandydat na warstwę III

Motywacja. Zamiast doklejać K z zewnątrz, zbadać widmo samego R₄ na V_ρ.

Test komutacji (🔍). ‖[K,M₀]‖ = ‖[K,M₁]‖ = 0,230, ‖[K,M₂]‖ = ‖[K,M₃]‖ = 0,117, ‖[K,R₄]‖ = 0,103. Wartości tego samego rzędu co same wpisy K — niezaniedbywalne.

Wniosek (🔍). K i R₄ nie komutują. Naiwna hybryda „R₄ zawęża amplitudę, exp(tK) zachowuje etykietę orbity niezależnie" nie jest matematycznie spójna.

Natywny kandydat (🔍). Widmo R₄ na V_ρ:

· λ₁ = 1 (kierunek ⟨1⟩, poza V_ρ),
· λ₂,₃ = 0,1533 ± 0,0740i, |λ| = 0,1703, faza = ±25,77°/rundę,
· λ₄ = 0,1347 (rzeczywista).

Para zespolona definiuje dwuwymiarową podprzestrzeń niezmienniczą R₄, na której dynamika jest spiralą kurczącą się: amplituda maleje geometrycznie, ale faza obraca się o stałe 25,77° na rundę — niezależnie od tego, jak mała jest już amplituda.

Rozdzielenie amplituda/faza (💡).

· Amplituda spirali (promień) ↔ pamięć wartościowa (warstwa I) — zanika geometrycznie.
· Faza spirali (kąt) ↔ kandydat na pamięć strukturalną (warstwa III) — matematycznie nie zanika, ale jest operacyjnie odczytywalna tylko w tym samym oknie ~7 rund, w którym amplituda pozostaje powyżej rozdzielczości numerycznej.

Ograniczenia.

1. 💡 To wciąż interpretacja, nie dowód.
2. 🔍 Faza jest zdefiniowana tylko dopóki amplituda ≠ 0 dokładnie.
3. ❌/💡 Związek fazy z 𝓜(𝔒; R₀) w sensie ω-granicznym jest rozstrzygnięty negatywnie (§18.1). Pytanie, czy istnieje czulszy formalizm, pozostaje 💡 otwarte (M19).

Status całości M17: 🔍 dla części spektralnej, 💡 dla interpretacji jako warstwy III.

25. (zarezerwowane — scalone do §24)

26. ORB-05-R — pełna trajektoria zamiast samego stanu końcowego

Cel. Sprawdzić, czy klasyfikacja pełnych trajektorii zawiera informację, której nie widać w samym stanie końcowym.

Protokół. Dla K₄ i 6! = 720 kolejności aktualizacji zapisywana jest trajektoria D_π(0), D_π(1), \ldots, D_π(T), a następnie jej część cykliczna P_cyc D_π(t). Klasyfikacja metodami: dokładna (zaokrąglenie) lub metryczna (RMS).

Wynik (✅, zweryfikowane). W reprodukowalnej implementacji ORB-05-R:

· final_cyclic_class_count = 209 — liczba klas stanów końcowych.
· exact full-trajectory classes = 425 — liczba klas pełnych trajektorii (zaokrąglone sygnatury, stabilne od 3 do 8 miejsc po przecinku).

Dla największej klasy końcowej odnotowano różne trajektorie o maksymalnym RMS około 0,19748.

Poprawka i niezależna weryfikacja. Przesłany plik implementujący ORB-05-R miał błąd: parametr order był zapisywany jako etykieta, ale nigdy nie wpływał na obliczenia — m16_B_step zawsze iterował po krawędziach w stałej kolejności 0..5. Skutek: wszystkie 720 przebiegów było identycznych. Po naprawie (parametr order faktycznie steruje kolejnością Gaussa-Seidela) obie liczby (425/209) są w pełni odtworzone z poprawionego kodu.

Interpretacja. Wynik wspiera zdanie:
\boxed{\text{ten sam stan końcowy nie musi określać tej samej historii procesu}.}

Nie wynika z niego jeszcze, że istnieje kanoniczna „pamięć strukturalna" niezależna od wszystkich szczegółów implementacji.

Konsekwencja. Nie używać ORB-05-R jako bezpośredniego dowodu H-MEM-1. Jego właściwa rola to uzasadnienie, dlaczego warstwę III należy badać co najmniej w dwóch wersjach:
\mathcal{M}_\omega(\mathfrak{O}) \qquad \text{i} \qquad \mathcal{M}_{\rm traj}(\mathfrak{O}, T).

27. Problemy otwarte Części C

# Problem Status Priorytet
M1 Formalny dowód H-MEM-1 💡 Wysoki
M2 Metryka na 𝓜(𝔒) 💡 Średni
M3 Most Net A↔B (konkretna konstrukcja) 💡 Wysoki
M4 Termodynamika pamięci 💡 Niski
M6 Niezmienniczość topologiczna 💡 Średni
M8 Relacje temporalne 💡 Średni
M16b Kanoniczność mostu i trybu K₂ 💡 Wysoki
M19 Czulsza definicja pamięci strukturalnej (nie ω-graniczna) 💡 Wysoki
M20 Kanoniczna metryka/równoważność pełnych trajektorii 💡 Wysoki

Problemy przeniesione do P₀-Applications: M5 (eksperyment optyczny), M7 (Δ a krawędzie obrazu), M9 (Δ(λ) dla koloru), M10 (K₄ ↔ graf obrazu). Zob. Applications §3.7 (przetwarzanie obrazu) i Applications §6 (lista hipotez).

Problemy zamknięte:

# Problem Status Sekcja
M17 Faza spirali — część spektralna 🔍 §24
M18 Faza w sensie ω-granicznym ❌ §18.1
ORB-05-R Pełne trajektorie ✅ §26

28. Podsumowanie Części C

Domknięte:

· Definicja formalna 𝓜(𝔒) (§18) — ✅ przy warunku jednej przestrzeni X.
· Orbita słaba vs mocna (§18) — ✅.
· M17 — część spektralna (brak komutacji K z R₄) — 🔍.
· ORB-05-R — pełne trajektorie (425/209) — ✅.
· M18 — faza w ω-granicznym sensie — ❌ rozstrzygnięte negatywnie.

Otwarte:

· H-MEM-1 jako hipoteza formalna — 💡 (§21).
· Konkretna konstrukcja mostu A↔B — 💡 (§16, §23).
· M16b — kanoniczność mostu i trybu K₂ — 💡 (§23).
· M19 — czulsza definicja pamięci strukturalnej — 💡 (§27).
· M20 — kanoniczna metryka trajektorii — 💡 (§27).

---

29. Podsumowanie v0.6.1

Domknięte:

· N9 ✅ (stabilizator w O(3,ℝ) = S₄) — §6.
· B3 ✅ (most A ↔ B nietrywialny) — §16.
· D-R1, D-R3, D-R2 ✅ — §10, §14.
· 𝓜(𝔒) — definicja formalna ✅ — §18.
· ORB-05-R ✅ (425/209) — §26.
· M18 ❌ — §18.1.

Otwarte:

· Konkretna konstrukcja mostu A ↔ B — 💡 (§16).
· N1–N8, N10 — §6.
· B2, B4, B5 — §15.
· M1, M2, M3, M4, M6, M8, M16b, M19, M20 — §27.

Kluczowa zmiana względem v0.6:

· Przywrócono §17.1 (𝒜/ℬ/𝒟), §17.2 (separacja realizacji), §17.3 (natywność), §21.1 (stan tezy), §22.3 (wyjaśnienie strukturalne).
· Scalono §18+§19, §22+§23, §24+§25.
· §29 zamieniony na odsyłacze.

---

30. Historia wersji

Wersja Data Zmiana
v0.4.2-draft 2026-08-23 Część A + Część B, D-R2, otwarte B3
v0.5 2026-09-13 §16 (B3) domknięte — most przez T_b
v0.5.1 2026-09-13 Uproszczenia §3, §10, §16
v0.6 2026-09-13 Wchłonięto P₀-Memory jako Część C (§17–§28)
v0.6.1 2026-09-13 Przywrócono §17.1 (𝒜/ℬ/𝒟), §17.2 (separacja realizacji), §17.3 (natywność), §21.1 (stan tezy), §22.3 (wyjaśnienie strukturalne). Scalono §18+§19, §22+§23, §24+§25. §29 → odsyłacze. Wszystkie odwołania do filarów bez numeru wersji.

---

P₀-Net v0.6.1-formal-draft. Część A (transport modeli ℝ⁴) + Część B (sieć relacyjna C¹(K₄)) + Część C (pamięć strukturalna w sieci). Odwołania do innych filarów bez numeru wersji. Synteza: 2026-09-13.