# Korzeń: P₀-Alchemy — adnotacja (v0.4.4-alpha, 2026-09-05)

**Dokument filarowy:** „P₀-Alchemy: Atraktor relacyjny z progiem rezydualnym" v0.4.4-alpha (2026-09-05); kod źródłowy `p0_alchemy_source.py` (v0.3-alpha, 2026-08-07) — wszystkie ✅/🔍 z audytu v0.4.4 zweryfikowane bezpośrednim uruchomieniem kodu, nie na słowo. **Baza matematyczna:** P₀-Centroid v4.9.6, P₀-Wave v0.6.1, P₀-Net v0.4.2-draft, P₀-Scalar v0.3.5-draft, P₀-Experiments v0.3.2 (odwołania do dalszych filarów; pełna lista w PILLARS-TABLE.md). **Okres:** prace VIII–IX 2026, sprzed warsztatu (audyt v5.2 Centroidu z 2026-09-29 jest późniejszy niż baza v4.9.6 tego dokumentu). **Zasada repo:** jak w korzeniu Centroidu — adnotacja szefa lab. + dokument verbatim (dostarczony przez autora 2026-11-19); kod pozostaje poza drzewem (Z3, szopa odroczona).

## Co bada ten korzeń

Gałąź P₀-Alchemy: operator kompensacji K z progiem rezydualnym δ > 0 (mechanizm A0': relacja = różnica, próg zapobiegający kolapsowi do p₀). Dwa kroki: K₁ kompensacja centroidalna (dᵢⱼ' = (1−α)dᵢⱼ dokładnie — tożsamość algebraiczna), K₂ korekta progowa (symetryczne rozsunięcie par poniżej δ do dokładnie δ, formuła jawna w §1). Dokument bada atraktor iteracji K na układach 4 punktów w (ℝ³)⁴.

## Co najmocniejsze (wg legendy dokumentu)

- **G₄ = ¾Σᵢ<ⱼdᵢⱼ², ∇G₄ = 6(pᵢ−C)** (✅, dwie niezależne drogi rachunkowe).
- **Hipoteza KKT ❌ sfalsyfikowana analitycznie:** minimum G₄ na zbiorze dopuszczalnym {dᵢⱼ ≥ δ} to (9/2)δ² (sympleks regularny, tetraedr foremny — osiągalny), a stała atraktora g₀ = 4,8649δ² (sygnatura S₀ z §4). Atraktor NIE jest minimalizatorem problemu statycznego — różnica ~8%, bez marginesu numerycznego; mechanizm A0' jest z natury dynamiczny. Droga do wzorów analitycznych S₀ przez optymalizację zamknięta; zostają równania punktu stałego K₂.
- **Atraktor = orbita obrotowa, nie punkt (✅, Procrustes, 200 tys. kroków):** macierz odległości jest punktem stałym (6 cyfr zgodności z kroku 300), konfiguracja rotuje ~3,3·10⁻³ rad/krok, det = +1. „Z dokładnością do izometrii O(3)" jest dosłowne, nie retoryczne.
- **Stabilizator S₀ w S₄ trywialny, orbita = 24 (✅, 24/24 permutacje):** żadna nieidentycznościowa permutacja etykiet nie zachowuje sygnatury; ewentualny transport działa na klasie 24 sygnatur. N9 (stabilizator {δ(M_m)} w O(3) = dokładnie S₄) ✅ domknięte w Centroid §8.1 (2026-08-25) — zależność między korzeniami, śledzona jawnie.
- Kolejność korekty sekwencyjnej (combinations) decyduje, która para wypada na progu — lokalna asymetria to artefakt implementacji, nie własność K (🔍; hipoteza globalnej symetrii S₄ (AL-H7) zostaje 💡).

## Sęki i lekcje metodologiczne (najbogatszy w rodzinie korzeni)

- **Kontrakcyjność K globalna ❌:** raport „25 000 prób potwierdza D(KR,KS) ≤ (1−α)D(R,S)" testował wyłącznie K₁ — w dobieranych parach próg δ nie aktywował się ANI RAZ (0% aktywacji), a dla samego K₁ nierówność jest tożsamością algebraiczną, nie odkryciem. Kontrprzykład w reżimie aktywacji (2528–3956 z 5000): ratio 1,2027 — naruszenie 26,6% ponad deklarowaną stałą. Argument Banacha na jednoznaczność upada.
- **Błąd jednego znaku w niezależnej reimplementacji K₂:** pozorny „cykl graniczny" i „złamanie A0'" okazały się artefaktem; po korekcie — zgodność. Wniosek autora: opis słowny wystarcza do zrozumienia, nie do bezbłędnej reimplementacji; stąd formuła jawna w §1. Dokładnie lekcja „liczby/formuły jawnym tekstem" (protokół między-modelowy, zasada 1) avant la lettre — potwierdzona w projekcie po fakcie.
- **Wzory analityczne S₀ przez √3, √5 ❌ wycofane** (niezgodne z symulacją); wartości numeryczne (a ≈ 1,0844, e ≈ 1,0177 …) zostają 🔍.
- **Świadome pominięcie trzech zgłoszonych twierdzeń** (warianty reguły K₂: symetryczny/jednopunktowy/symultaniczny): jeden wariant był artefaktem błędu znaku, dwa nie przeszły niezależnej weryfikacji — nie włączone, traktować jako 💡. Wzorzec uczciwej restrykcji przy zależnych wynikach.
- **Zalecenia metodologiczne dokumentu:** jawny odsetek aktywacji progu w każdym teście (wynik przy 0% mówi tylko o K₁); jawna konwencja R₀ (rozbieżność γ(N) w replikacji τ rosnąca z N wskazuje na niepodaną konwencję losowania); rozkład/skala/seed przy każdym raporcie numerycznym. To jest Z2 i zasada atrybucji (tura 28) sformułowane niezależnie, przed warsztatem — silne potwierdzenie kierunku metodyki.

## Mosty do pnia i gałęzi (odczytanie interpretacyjne, 💡)

- **A0' jako mechanizm anty-kolapsowy:** próg δ utrzymuje różnicę (relacja nie zanika, ale też nie maksymalizuje odległości — atraktor nad minimum 4,5δ²): relacyjny odpowiednik zasady „uśrednianie ku barycentrum zamiast kolapsu ku wierzchołkowi" (faza snu) i komplementarność z konsensusem Centroidu: czysta średnia zbiega do punktu, próg zostawia strukturę.
- **Atraktor jako ruch, nie stan:** orbita obrotowa SO(3) zamiast punktu stałego — echo zasady „równe normy ≠ ten sam stan" (tura 26), P₀-ruchomego i atraktorów jako trajektorii (Tom III dryf).
- **Kolejność daje strukturę lokalną:** para na progu zależy od kolejności korekty — kolejność (konwencja) kształtuje atraktor, pre-echo C2 (faza/kierunek z porządku rund).
- **Termodynamika relacyjna AL-H9 (💡):** U = N·g₀·δ², S = log N!, T = g₀δ²/log N, p(δ) = −2g₀/(3δ) — pierwsza formalna kandydatura „temperatury relacyjnej" w korpusie; sęk-odnoga z tetralogii (Tom II: termodynamika relacyjna — gałąź niepostawiona) do postawienia właśnie stąd.
- **Most Alchemy↔Net:** pytanie o transport klasy 24 sygnatur pod S₄ jest teraz skończone i obliczeniowo trywialne — czeka na sformułowanie warunku „zachowania klasy" (💡).

## Sęk-odnogi (bank nasion z korzenia)

1. **Wzory analityczne S₀** (a, b, c, d, e) z równań punktu stałego K₂ (droga przez KKT zamknięta).
2. **AL-2bis:** funkcja V(R) ściśle monotoniczna wzdłuż trajektorii K (Lyapunov) — globalnie otwarte; lokalnie wsparte przez kontrakcję w przestrzeni kształtu.
3. **Dekompozycja spektralna Jakobianu K w przestrzeni kształtu:** ρ ≈ 0,2726 (pełna dekompozycja, nie odtworzona w v0.4.4) — do domknięcia ✅ z dowodem.
4. **Bateria wariantów K₂** (symetryczny/jednopunktowy/symultaniczny) z rygorem §6.2 (uruchomienie właściwego kodu, nie reimplementacja z opisu).
5. **AL-H8 (jednoznaczność w basenie):** dziś tylko 8 seedów 🔍 + mechanizm lokalny; brak dowodu globalnego.
6. **Replikacja τ (AL-H10) z ujednoliconą konwencją R₀** — rozbieżność systematyczna rosnąca z N do zamknięcia.
7. **Granica N → ∞:** stabilność atraktora przy dużej liczbie relacji; termodynamika AL-H9 do uzasadnienia mikroskopowego.

## Statusy: mapa legendy dokumentu na konwencje warsztatu

Dokument ma własną legendę (✅ Dowiedzione · 📚 Klasyczne · 🔍 Zweryfikowane numerycznie/symbolicznie · 💡 Przypuszczenie · ❌ Sfalsyfikowane) i już bardzo warsztatowe zasady: redakcyjną („żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia"), niezależności (upada Alchemy → nie upada algebra 𝔤₄, metryka G₄, faza 25,77°) i ostrożności (wynik 🔍 na jednym reżimie nie przenosi się na inny). Mapowanie na Z1: „✅ rachunek bezpośredni/dowód" = twierdzenia; „✅ zweryfikowane uruchomieniem kodu" w duchu Z1 to 🔍 (jedna implementacja); obalenia = sęki trwałe (Z0). Dokument sam głosi dokładnie tę hierarchię, którą warsztat później przyjął jako metodę — filar metodyki przed metodą.

## Dokument verbatim (v0.4.4-alpha, bez zmian)

# P₀-Alchemy: Atraktor relacyjny z progiem rezydualnym

**Wersja:** 0.4.4-alpha
**Status dokumentu:** 🔍 Program badawczy z częściowo domkniętymi wynikami. Zastępuje v0.3-alpha, raport korekcyjny v0.3.1-alpha-k1 oraz v0.4.0-alpha (scalone; dodaje §8bis). Korekta v0.4.4 — cztery zmiany, wszystkie zweryfikowane niezależnie przez uruchomienie `p0_alchemy_source.py` (nie tylko przyjęte na słowo z drugiej analizy): (1) §3 KKT zamknięte ❌ dowodem analitycznym, nie tylko numerycznie; (2) §1 formuła Kroku 2 podana jawnie; (3) §7 test 24 izometrii S₄ na S₀ wykonany — stabilizator trywialny, orbita 24; (4) nowe §6.2 — dokładna struktura atraktora (orbita obrotowa + kontrakcja lokalna w przestrzeni kształtu). Świadomie **pominięto** trzy dodatkowe twierdzenia zgłoszone razem z powyższymi (wariant symetryczny/jednopunktowy/symultaniczny reguły K₂) — wariant symetryczny okazał się artefaktem błędu znaku w niezależnej reimplementacji, pozostałe dwa nie zostały ponownie zweryfikowane po znalezieniu tego błędu; zob. §6.2 uwaga na końcu i §9 pkt 4. Poprzednia korekta v0.4.3 — status N9 podniesiony z 🔍 do ✅ (Centroid §8.1).
**Pozycja:** gałąź P₀-Alchemy — zobacz [`PILLARS-TABLE.md`](PILLARS-TABLE.md) dla pełnej listy filarów.
**Baza matematyczna:** P₀-Centroid v4.9.6, P₀-Wave v0.6.1, P₀-Net v0.4.2-draft, P₀-Scalar v0.3.5-draft, P₀-Experiments v0.3.2.
**Data:** 2026-09-05
**Kod źródłowy:** `p0_alchemy_source.py` (v0.3-alpha, 2026-08-07) — wszystkie wyniki numeryczne w tej wersji zweryfikowane przez bezpośrednie uruchomienie tego pliku.

---

**Zasada redakcyjna.**

> Żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia, którego dotyczy.

Statusy: ✅ Dowiedzione · 📚 Klasyczne · 🔍 Zweryfikowane numerycznie lub symbolicznie (bez dowodu ogólnego) · 💡 Przypuszczenie / program badawczy · ❌ Sfalsyfikowane (odrzucone po weryfikacji).

**Zasada niezależności.** Ten dokument nie modyfikuje matematyki P₀-Centroid ani P₀-Wave. Jeśli własności atraktora zostaną obalone, upada model Alchemy — nie algebra 𝔤₄, nie metryka G₄, nie faza 25,77°.

**Zasada ostrożności.** Symulacja nie zastępuje dowodu. Wszystkie własności oznaczone jako 🔍 lub 💡 wymagają niezależnej replikacji lub formalnego zamknięcia. Wynik oznaczony 🔍 na jednym reżimie parametrów **nie przenosi się automatycznie** na inny reżim — zob. §6.1.

---

## 0. Status i zakres

Dokument opisuje własności atraktora operatora kompensacji K z progiem rezydualnym δ > 0 (mechanizm A0': relacja = różnica, próg zapobiegający kolapsowi do p₀), zidentyfikowane w symulacjach numerycznych i częściowo sformalizowane. Nie zawiera twierdzeń zamkniętych w pełnej algebrze 𝔤₄ — jest raportem z realizacji programu badawczego, nie formalnym filarem na poziomie Centroid/Wave.

Ta wersja scala i zastępuje dwa poprzednie dokumenty: v0.3-alpha (błędy rachunkowe i logiczne — patrz Appendix A) oraz raport korekcyjny v0.3.1-alpha-k1 (poprawił większość błędów, ale nie uwzględniał obalenia kontrakcyjności K z §6.1 poniżej, i miał kolizję etykiet AL-H7 — obie luki zamknięte w tej wersji).

---

## 1. Operator K i jego struktura

**Definicja (założenie konstrukcyjne, 💡).** Relacja to układ 4 punktów R = (p₀, p₁, p₂, p₃) w (ℝ³)⁴. Operator kompensacji K działa w dwóch krokach:

1. **Krok skalowania (kompensacja centroidalna), K₁:**
   pᵢ' = (1 − α) pᵢ + α C, gdzie C = (1/4) Σⱼ pⱼ.
   W odległościach: dᵢⱼ' = (1 − α) dᵢⱼ **dokładnie** — to jest tożsamość algebraiczna (K₁ jest liniowe, centroid znosi się w różnicy), nie wynik numeryczny.

2. **Krok korekty progowej (A0'), K₂:**
   Dla każdej pary (i,j), jeśli dᵢⱼ' < δ:

   correction = (δ − dᵢⱼ')/2, u = (pᵢ' − pⱼ')/dᵢⱼ'
   pᵢ'' = pᵢ' + correction·u,  pⱼ'' = pⱼ' − correction·u

   Rozsunięcie jest symetryczne: środek pary (pᵢ'+pⱼ')/2 jest zachowywany, każdy punkt przesuwa się o połowę deficytu. **Jawnie:** dᵢⱼ'' = δ dokładnie (weryfikacja algebraiczna natychmiastowa: ‖(pᵢ'+correction·u)−(pⱼ'−correction·u)‖ = dᵢⱼ' + 2·correction = δ).

**Uwaga (✅, lekcja metodologiczna, 2026-09-05).** Niezależna reimplementacja tego kroku w innej sesji przypisała punktom wzór pᵢ=m−½δu (przerzucenie na przeciwną stronę środka zamiast rozsunięcia od niego) — błąd jednego znaku. Skutkiem był pozorny „cykl graniczny" i „złamanie A0'", które okazały się artefaktem tej pomyłki, nie własnością modelu; po korekcie znaku wyniki są zgodne z opisem powyżej (§6.2). Wniosek praktyczny: opis słowny bez jawnej formuły (jak w tej sekcji przed niniejszą korektą) był wystarczający do zrozumienia, ale niewystarczający do bezbłędnej reimplementacji — stąd formuła powyżej.

**Uwaga implementacyjna (🔍).** W kodzie źródłowym p0_alchemy_source.py krok 2 jest stosowany sekwencyjnie w kolejności danej przez `combinations(range(4), 2)`, tj. (0,1), (0,2), (0,3), (1,2), (1,3), (2,3). Kolejność ta ma wpływ na strukturę atraktora (por. §5).

---

## 2. Punkt stały — układ równań

**Fakt (✅, rachunek bezpośredni).** W atraktorze (stabilnym punkcie stałym operatora K) co najmniej jedna para znajduje się dokładnie na progu δ. W przeciwnym razie krok skalowania zmniejszałby wszystkie odległości, a krok 2 nie korygowałby żadnej — co prowadziłoby do zanikania relacji, sprzecznie z A0'.

**Obserwacja numeryczna (🔍).** W symulacjach z parametrami δ = 0,15, α = 0,15 dokładnie jedna para (w implementacji sekwencyjnej zawsze para (2,3), ostatnia w kolejności combinations) ma d₂₃ = δ. Pozostałe odległości są większe od δ i parami różne.

---

## 3. Warunki równowagi — KKT

**Twierdzenie (✅, rachunek bezpośredni).** Niech G₄(R) = Σᵢ ‖pᵢ − C‖² + (1/2) Σᵢ<ⱼ ‖pᵢ − pⱼ‖². Wtedy:

∇ₚᵢ G₄ = 6(pᵢ − C).

*Dowód.* Część centroidalna: ∇ Σₖ ‖pₖ − C‖² = 2(pᵢ − C). Część parowa: ∇ (1/2) Σₖ<ₗ ‖pₖ − pₗ‖² = Σⱼ≠ᵢ (pᵢ − pⱼ) = 4(pᵢ − C), bo Σⱼ≠ᵢ pⱼ = 4C − pᵢ. Razem: 2(pᵢ − C) + 4(pᵢ − C) = 6(pᵢ − C). ∎

**Hipoteza KKT — ❌ SFALSYFIKOWANA (2026-09-05, dowód analityczny, nie tylko numeryczny)**

**Tożsamość (✅, oś równoległa).** Dla 4 punktów: Σᵢ‖pᵢ−C‖² = ¼ Σᵢ<ⱼ dᵢⱼ². Podstawiając do definicji G₄ (§2, ta sekcja):

G₄ = Σᵢ‖pᵢ−C‖² + ½Σᵢ<ⱼdᵢⱼ² = ¼Σdᵢⱼ² + ½Σdᵢⱼ² = **¾ Σᵢ<ⱼ dᵢⱼ²**

(zgodne z gradientem 6(pᵢ−C) dowiedzionym wyżej: ∇Σᵢ‖pᵢ−C‖²=2(pᵢ−C) daje G₄=3Σᵢ‖pᵢ−C‖²=3·¼Σd²=¾Σd² — dwie niezależne drogi rachunkowe, ta sama stała).

**Wniosek (✅).** Na zbiorze dopuszczalnym {dᵢⱼ≥δ ∀i<j}, ¾Σd² jest sumą sześciu wyrazów rosnących niezależnie w każdym dᵢⱼ — minimum na tym zbiorze osiągane jest dokładnie, gdy każde dᵢⱼ=δ, tj. na sympleksie regularnym o krawędzi δ:

min G₄ = ¾·6δ² = **(9/2)δ²**

Sympleks regularny o krawędzi δ istnieje w ℝ³ (tetraedr foremny), więc to minimum jest osiągalne, nie tylko formalne dolne ograniczenie.

**Porównanie z atraktorem (✅, zweryfikowane bezpośrednio uruchomieniem `p0_alchemy_source.py`, δ=0,15, α=0,15, seed=42, 300 kroków).** Sygnatura S₀ (§4) daje Σdᵢⱼ²/δ² = 6,4865 (sześć wartości parami różne, żadna nie równa się drugiej poza d₂₃=δ), stąd g₀ := G₄(atraktor)/δ² = ¾·6,4865 = **4,8649**. Ponieważ 4,8649 > 4,5, **atraktor nie jest minimalizatorem problemu ograniczonego** — leży ściśle powyżej dolnej granicy, i to bez marginesu błędu numerycznego (różnica ~8%, nie ~10⁻⁶).

**Konsekwencja dla hipotezy KKT.** Warunki KKT wyprowadzone wcześniej w tej sekcji (6(pᵢ−C)=0 dla i nieaktywnych) opisywałyby *jakiś* punkt stacjonarny problemu ograniczonego — ale atraktor operatora K nie jest tym punktem. Hipoteza „atraktor = rozwiązanie KKT" jest fałszywa nie dlatego, że układ równań się nie domyka (jak sugerowała poprzednia wersja), lecz dlatego, że **wartości energii się nie zgadzają** — silniejszy, prostszy powód do odrzucenia. Droga do wzorów analitycznych na a,b,c,d,e (§4, §9 pkt 3) przez optymalizację ograniczoną jest zamknięta; jedyna pozostała droga to równania punktu stałego samego K₂ (dynamika, nie statyka).

**Status:** ❌ Sfalsyfikowane w pełni analitycznie. Zamyka §9 pkt 3 w obecnej formie (patrz zaktualizowany §9).

---

## 4. Macierz S₀ — sygnatura odległościowa

**Fakt numeryczny (🔍).** Dla δ = 0,15, α = 0,15, po 300 krokach kompensacji, wszystkie relacje (N = 3, różne warunki początkowe, seed = 42) zbiegają do identycznej sygnatury odległościowej z dokładnością do izometrii O(3):

S₀ =
[[0,  a,  b,  c],
 [a,  0,  d,  e],
 [b,  d,  0,  1],
 [c,  e,  1,  0]] · δ

gdzie (przeskalowane do δ = 1): a ≈ 1,0844 · b ≈ 1,0597 · c ≈ 1,0331 · d ≈ 1,0415 · e ≈ 1,0177 · d₂₃ = 1,0000

**Wycofane (❌, v0.3-alpha).** Poprzednia wersja podawała wzory analityczne a = (3+√5)/(2√3) itd. Wzory te są niepoprawne — dają wartości niezgodne z symulacją. Wartości numeryczne pozostają poprawne i zweryfikowane. Wzory analityczne wymagają osobnego wyprowadzenia.

**Status:** Sygnatura numeryczna jest zweryfikowana. Wzory analityczne na a, b, c, d, e pozostają otwarte.

---

## 5. Symetria i artefakt kolejności korekty

**Obserwacja numeryczna (🔍).** W implementacji sekwencyjnej (kolejność combinations) para (2,3) jest zawsze ostatnia. Korekta tej pary jest stosowana po korektach wszystkich poprzednich par, co powoduje, że to ona „wypada” dokładnie na progu δ. Pozostałe pary są różne i nie tworzą symetrii C₂ × C₂.

**Weryfikacja numeryczna (🔍).** Po permutacji punktów [1,2,3,0] (cykl) para na progu zmienia się na (0,3) — czyli znowu „ostatnią” w kolejności combinations po permutacji.

**Wniosek.** Lokalna struktura atraktora (która para jest na progu) jest **artefaktem implementacji sekwencyjnej**, nie własnością samego operatora K. W modelu symultanicznym (wszystkie korekty jednocześnie) struktura mogłaby być inna.

**Hipoteza AL-H7 (symetria globalna, 💡).** Dla N ≥ 2 relacji, każda relacja może mieć inną parę na progu (w zależności od warunków początkowych). Globalna symetria S₄ jest przywracana na poziomie zbioru relacji — permutacje między relacjami mogą wyrównać asymetrię lokalną.

**Status:** Obserwacja o artefakcie kolejności jest zweryfikowana numerycznie. Hipoteza AL-H7 o globalnej symetrii S₄ pozostaje otwarta.

---

## 6. Jednoznaczność atraktora

**Hipoteza AL-H8 (jednoznaczność w basenie, 💡).** W ramach danego basenu warunków początkowych operator K zbiega do tej samej sygnatury odległościowej (z dokładnością do izometrii O(3)), niezależnie od warunków początkowych.

**Uzasadnienie numeryczne (🔍).** Przeprowadzono symulacje dla 8 różnych seedów (1, 7, 13, 42, 99, 123, 777, 2024). Wszystkie zbiegły do identycznej sygnatury (posortowane odległości zgodne na 5 miejscach po przecinku).

**Błąd logiczny wycofany (❌, v0.3-alpha).** Poprzednia wersja twierdziła, że jednoznaczność wynika ze ścisłej wypukłości G₄ na podprzestrzeni wycentrowanej. To jest nieprawda — zbiór dopuszczalny D = {R : dᵢⱼ ≥ δ} jest **nie-wypukły** (dopełnienie kuli), więc ścisła wypukłość funkcji nie gwarantuje jednoznaczności globalnego minimum. Jednoznaczność wymagałaby dowodu kontrakcyjności K lub innego argumentu dynamiki — zob. §6.1, gdzie ta droga zamyka się negatywnie.

**Status:** Jednoznaczność jest hipotezą wspartą numerycznie w reżimie testowanym (§6.1 pokazuje, że to wsparcie jest węższe, niż wcześniej sądzono), nie twierdzeniem zamkniętym.

### 6.1. Kontrakcyjność K — SFALSYFIKOWANA (❌, 2026-08-10)

Osobny raport ("RAPORT_Kontrakcyjnosc_K_Alpha") twierdził, że D(K(R),K(S)) ≤ (1−α)D(R,S) zachodzi **dokładnie**, dla wszystkich R,S, na podstawie 25 000 losowych prób (5 wartości α, metryka D = norma Frobeniusa różnicy macierzy odległości). Weryfikacja niezależna wykazała, że ten wynik jest **artefaktem doboru próby**, nie właściwością operatora K.

**Przyczyna.** Testowane pary R, S losowano ze skalą ~2,0 przy δ = 0,05. W tym reżimie odległości między losowymi punktami niemal nigdy nie spadają poniżej δ po jednym kroku — **Krok 2 (próg A0', jedyny nieliniowy, nietrywialny element operatora) nie aktywował się ani razu w 25 000 prób.** Raport w istocie testował wyłącznie K₁, dla którego D(K₁R,K₁S)=(1−α)D(R,S) jest tożsamością algebraiczną (§1) — nie odkryciem numerycznym.

**Kontrprzykład (reprodukowalny, seed=42, α=0,05, δ=0,05).** Przy próbkowaniu R, S blisko progu (skala ~0,06, tam gdzie Krok 2 faktycznie aktywuje się w 2528–3956 z 5000 prób, zależnie od α):

```
D(R,S) przed   = 0,077580
D(K(R),K(S))   = 0,093308
stosunek       = 1,202734   (twierdzone ograniczenie: ≤ 0,95)
naruszenie o 26,6% ponad deklarowaną stałą
```

**Wniosek.** K **nie jest** kontrakcją ze stałą (1−α) na całej przestrzeni (ℝ³)⁴ w sensie ogólnym, wbrew wcześniejszemu twierdzeniu. Nierówność pęka dokładnie w reżimie, gdzie działa próg δ — czyli dokładnie tam, gdzie leży istota mechanizmu A0'. Argument Banacha na rzecz jednoznaczności atraktora (który miał wynikać z tej kontrakcyjności) **upada**. Jednoznaczność (§6, AL-H8) pozostaje hipotezą wspartą **wyłącznie** obserwacją zbieżności z wielu punktów startowych (8 seedów) — nie ma dziś żadnego dowodu teoretycznego.

**Zalecenie metodologiczne.** Każdy przyszły test numeryczny hipotez o Kroku 2/progu δ musi jawnie raportować **odsetek prób, w których próg faktycznie się aktywował** — wynik przy 0% aktywacji testuje tylko K₁ i nie mówi nic o A0'. Zob. też P₀-Przegląd_Całości, §9 (Wzorzec W9 — pewność empiryczna vs mechanizm), gdzie ten sam błąd metodologiczny jest omówiony jako przykład negatywny.

---

### 6.2. Dokładna struktura atraktora: orbita obrotowa i kontrakcja lokalna (🔍, 2026-09-05)

§6.1 zamknęło drogę globalną (Banach); §9 pkt 5 wcześniej wskazywał, że jedyna pozostała droga to kontrakcja **lokalna**, blisko atraktora. Test bezpośredni (uruchomienie do 200 000 kroków, δ=0,15, α=0,15, seed=42):

**Fakt (✅, zweryfikowane).** Macierz odległości jest dokładnie punktem stałym: po 200 000 krokach wartości identyczne do 6 cyfr z wartościami po 300 krokach (§4); d₂₃=δ z precyzją maszynową. Konfiguracja punktów **nie** jest punktem stałym — każdy krok po zbiegnięciu macierzy odległości jest czystą rotacją: dopasowanie Prokrustesa między kolejnymi krokami daje residual rzędu maszynowego (10⁻¹⁶) i kąt obrotu ≈3,3·10⁻³ rad/krok, det=+1 (rotacja właściwa, nie odbicie). **Zdanie z §4 „z dokładnością do izometrii O(3)" jest więc dosłowne, nie retoryczne**: atraktor to orbita jednoparametrowej podgrupy SO(3) działającej na ustalonym kształcie, nie punkt.

**Wynik (🔍, kontrakcja lokalna w przestrzeni kształtu).** Po odjęciu tej rotacji (wyrównanie Prokrustesa na każdym kroku, przestrzeń kształtu 9-wymiarowa: 4 punkty × 3 wymiary, minus 3 translacji, minus 3 rotacji), mała perturbacja atraktora zanika geometrycznie z obserwowanym współczynnikiem rzędu 0,27–0,28 na krok (test niezależny, jedno zaburzenie losowe, 15 kroków — nie pełna dekompozycja spektralna Jakobianu). To **wsparcie mechanizmu dla AL-H8** (jednoznaczność w basenie, §6): w przestrzeni kształtu K zachowuje się jak kontrakcja z widocznym, silnym współczynnikiem, mimo że globalna kontrakcja na całym (ℝ³)⁴ jest sfalsyfikowana (§6.1). To pogodzenie, nie sprzeczność — §6.1 obala kontrakcję *na całej przestrzeni ze stałą (1−α)*; nic nie stało na przeszkodzie, by lokalna kontrakcja *w przestrzeni kształtu* istniała z inną stałą.

**Czego ten wynik NIE ustala (pominięte świadomie).** Wraz z powyższym zgłoszono w tej samej turze trzy dalsze twierdzenia porównujące warianty reguły K₂ (symetryczny/jednopunktowy/symultaniczny) z konkretnymi liczbami (m.in. ρ=0,625 dla wariantu jednopunktowego, złamanie A0' dla symultanicznego). **Nie są tu włączone.** Wariant „symetryczny" z tego zestawu okazał się artefaktem błędu znaku w reimplementacji (§1, uwaga) — sam autor się z niego wycofał. Pozostałe dwa warianty nie zostały ponownie zweryfikowane po znalezieniu tego błędu i nie zostały zweryfikowane niezależnie w tej wersji dokumentu. Traktować jako 💡, nie 🔍, dopóki nie przejdą tej samej niezależnej weryfikacji co powyższe fakty (zob. §9 pkt 4).

**Status:** Rotacja + fixed shape ✅ (zweryfikowane, Procrustes). Wartość liczbowa ρ 🔍 (rząd wielkości potwierdzony niezależnie, dokładna wartość 0,2726 z pełnej dekompozycji spektralnej — nie odtworzona tutaj w tej dokładności). Warianty reguły K₂ — nie włączone, 💡, wymagają osobnej weryfikacji.

---

## 7. Co wynika — most do P₀-Net

**Obserwacja (🔍).** Atraktor jest niezależny od topologii sieci (dla izolowanych relacji). Dla N ≥ 2 relacji połączonych transportem (P₀-Net §4) struktura produktu zależy od siły wiązania między-relacyjnego (por. AL-3 w p0_alchemy_source.py).

**Hipoteza (💡).** Atraktor lokalny jest stabilnym fundamentem dla transportu R w P₀-Net: jeśli R zachowuje p₀, V_ρ, G₄ (warunki 1–3 Net §4), to sygnatura atraktora jest przenaszalna między węzłami sieci.

**Aktualizacja (2026-08-26).** N9 (transport geometryczny vs algebraiczny, warunek opcjonalny (4) w Net §4) jest **✅ zamknięte dokładnie**: stabilizator {δ(M_m)} w O(3,ℝ) to dokładnie S₄, dowód dwukrokowy w Centroid §8.1 (2026-08-25), potwierdzony w Net (tabela N9). To *nie* jest już „wstępna weryfikacja numeryczna" — jest to dowód, nie obserwacja. Poprzednie sformułowanie w tym dokumencie („most pozostaje otwarty, ale N9 nie jest już całkowicie nietknięty") było poprawne w chwili pisania (2026-08-12, przed domknięciem 08-25) i jest tu skorygowane retrospektywnie.

**Co się z tego zmienia, a co nie.** Domknięcie N9 mówi, które transporty R∈O(3,ℝ) zachowują dokładnie *algebrę* M_m — odpowiedź: wyłącznie 24 elementy S₄. Nie mówi nic wprost o tym, czy *sygnatura atraktora Alchemy* (S₀, §4) jest przez te transporty rzeczywiście zachowywana — to osobne twierdzenie, którego N9 nie dowodzi automatycznie. Hipoteza mostu w tym paragrafie pozostaje więc **💡 otwarta**, ale teraz w ostrzejszej formie: kandydatem na grupę transportu nie jest już mgliście „O(3,ℝ) spełniające warunki 1–3", tylko dokładnie S₄ (rząd 24) — pytanie testowalne wprost (sprawdzić działanie tych 24 izometrii na S₀ numerycznie, zamiast przeszukiwać cały O(3,ℝ)).

**Test wykonany (✅, 2026-09-05).** Sprawdzono bezpośrednio (24/24 permutacje, uruchomienie kodu) działanie S₄ na S₀: **stabilizator S₀ w S₄ jest trywialny** ({e} — wszystkich sześć odległości parami różnych, więc żadna nieidentycznościowa permutacja etykiet nie zachowuje macierzy odległości), stąd **orbita S₀ pod S₄ ma dokładnie 24 elementy** — maksymalna możliwa. Konsekwencja: żadna nieidentycznościowa izometria z S₄ nie zachowuje S₀ jako pojedynczej sygnatury (π·S₀ ≠ S₀ dla π≠e). Hipoteza mostu z akapitu wyżej musi więc dotyczyć **orbity 24 sygnatur jako całości**, nie niezmienniczości pojedynczego S₀ — S₀ jest jednym reprezentantem klasy, most (jeśli istnieje) działa na poziomie tej klasy.

**Status:** Program badawczy. N9 ✅ zamknięte (Centroid §8.1). Stabilizator S₀ w S₄ ✅ trywialny, orbita ✅ = 24 (zweryfikowane bezpośrednio). Most Alchemy↔Net (czy *klasa* 24 sygnatur transportuje się spójnie pod S₄) pozostaje 💡 — pytanie jest teraz w pełni skończone i obliczeniowo trywialne do zadania (sprawdzić, czy P₀-Net traktuje orbitę S₄ jako jeden obiekt), ale nikt jeszcze nie sformułował, co miałoby znaczyć „transport zachowuje klasę".

---

## 8. Termodynamika relacyjna — hipoteza programowa

**Hipoteza AL-H9 (termodynamika relacyjna, 💡).** Niech g₀ ≈ 4,8649 będzie stałą geometryczną atraktora (G₄(atraktor) = g₀ · δ²). Postulujemy następujące wielkości efektywne:

- U(N, δ) = N · g₀ · δ²
- S(N) = log N!
- T(N, δ) = g₀ · δ² / log N
- p(δ) = −2g₀ / (3δ)

**Uzasadnienie heurystyczne.** U jest sumą energii lokalnych. S = log N! liczy permutacje relacji jako mikrostany. T i p są postulowane z analogii termodynamicznej, nie wyprowadzone z mikroskopii.

**Status:** Czysta hipoteza programowa. Wymaga: (a) mikroskopowego uzasadnienia entropii, (b) dowodu, że S = log N! odpowiada liczbie dostępnych mikrostanów w modelu relacyjnym, (c) niezależnej weryfikacji numerycznej związków termodynamicznych.

---

## 8bis. Czas relaksacji τ (AL-H10, 🔍, 2026-08-11)

**Definicja formalna.** Dla ciągu R_{k+1} = K_{α,δ}(R_k) startującego z R₀, czas relaksacji τ to najmniejsze k spełniające |G₄(R_{k+1}) − G₄(R_k)| < ε, ε = 10⁻⁶ (tolerancja bezwzględna). Jeśli warunek nie jest osiągnięty po k_max=500 krokach, τ = 500.

**Hipoteza AL-H10 (skalowanie czasu relaksacji).**

τ(N, α, δ) ≈ C(N) · α^(−γ(N)) · f(δ)

z empirycznym dopasowaniem γ(N) ≈ 1,04 · N^(−0,035), C(N) ≈ 3,5 · N^(0,65), oraz **τ niezależne od δ** (korelacja < 0,01 w zakresie δ∈[0,02; 0,30]).

| N | γ(N), raport źródłowy | γ(N), replikacja niezależna |
|---|---|---|
| 2 | 1,014 | 1,018 |
| 3 | 0,977 | 0,955 |
| 4 | 0,975 | 0,928 |
| 5 | 0,910 | 0,881 |
| 6 | 0,961 | 0,927 |
| 7 | 0,916 | 0,850 |
| 8 | 0,900 | 0,756 |

**Replikacja niezależna (🔍, ta wersja).** Kierunek i skala efektu (γ malejące z N, od ~1,0 do ~0,75–0,90) potwierdzone niezależnie, z własną implementacją operatora K i tym samym protokołem (ε=10⁻⁶, 30 seedów na punkt). Punkt N=3, α=0,15: τ≈31,8 (replikacja) vs τ≈32 (raport źródłowy) — zgodność bardzo dobra. Dla większych N (6–8) replikacja daje systematycznie niższe γ niż raport źródłowy — rozbieżność rosnąca z N, nie losowa.

**Luka do domknięcia.** Rozbieżność wskazuje najprawdopodobniej na różnicę w konwencji warunku początkowego (skala/rozkład losowania R₀), niepodaną w definicji formalnej — `RelationalAlchemyModel.__init__` nie specyfikuje jej jawnie. Dopóki ta konwencja nie zostanie ujednolicona i podana explicite, dokładne wartości liczbowe C(N), γ(N) są odtwarzalne tylko jakościowo, nie co do cyfry.

**Zalecenie metodologiczne.** Każdy raport numeryczny w Alchemy powinien od tej pory podawać: (a) dokładną definicję mierzonej wielkości z tolerancją, (b) rozkład i skalę warunku początkowego, (c) liczbę seedów uśrednionych. Trzy z czterech dotychczasowych raportów numerycznych w tym dokumencie (S₀ §4, jednoznaczność §6, τ §8bis) tego nie robiły przy pierwszym zgłoszeniu — dopiero pytanie o replikację to ujawniało.

**Analogia (💡, luźna, nie formalny most).** γ(N) bliskie 1 dla N=2, malejące z N, przywołuje obraz efektywnego rzędu reakcji malejącego z liczbą reagentów. To jest inspiracja nazewnicza, nie przekład na aparat kinetyki chemicznej — w kinetyce rząd reakcji wiąże szybkość ze stężeniem, nie czas relaksacji ze stałą szybkości. Traktować jako heurystykę do dalszego zbadania (por. przegląd chemii, dogłębnie #1/#2), nie jako ustalone mapowanie.

**Status:** 🔍 — kierunek i skala efektu potwierdzone niezależnie; dokładne wartości C(N), γ(N) czekają na ujednoliconą konwencję warunku początkowego.

---



## 9. Następne kroki

1. **AL-2bis:** Znaleźć funkcję V(R) = f(G₄, S), która jest ściśle monotoniczna wzdłuż trajektorii K — **częściowa odpowiedź w §6.2**: w przestrzeni kształtu (mod SO(3)) taka funkcja prawdopodobnie istnieje lokalnie (kontrakcja ρ≈0,27 zaobserwowana), ale globalnie na (ℝ³)⁴ wciąż otwarte; V(R) pozostaje jedyną realną ścieżką do jednoznaczności w sensie §6.1.
2. **AL-3bis:** Zbadać pełną algebrę reakcji: czy Aᵢ ⊕ Aⱼ = Aₖ zależy tylko od sygnatur, czy też od historii?
3. **Wzory analityczne S₀:** ❌ droga przez KKT zamknięta (§3); wzory muszą pochodzić z równań punktu stałego K₂ sprecyzowanego jawnie (§1), nie z optymalizacji ograniczonej.
4. **Model symultaniczny i warianty reguły K₂:** Zgłoszono (poza tym dokumentem) wstępne wyniki porównujące warianty symetryczny/jednopunktowy/symultaniczny — **nie włączone tu** (§6.2, uwaga), bo jeden wariant już okazał się artefaktem błędu implementacji, a pozostałe nie przeszły niezależnej weryfikacji. Priorytet: powtórzyć tę baterię z tym samym rygorem co §6.2 (uruchomienie właściwego kodu, nie reimplementacja z opisu słownego) przed wpisaniem liczb do dokumentu.
5. ~~Kontrakcyjność K~~ — **sfalsyfikowana globalnie (§6.1)**, ale **wsparta lokalnie w przestrzeni kształtu (§6.2, 🔍)** — kierunek dalszej pracy: dekompozycja spektralna pełnego Jakobianu K w przestrzeni kształtu, żeby zamienić 🔍 (rząd wielkości) na ✅ (dokładna wartość i dowód).
6. **Granica N → ∞:** Sprawdzić stabilność atraktora dla dużej liczby relacji.

---

## Appendix A. Errata (v0.3-alpha → v0.3.1-alpha-k1 → v0.4.0-alpha)

| Sekcja | Błąd | Poprawka | Status | Wersja korekty |
|---|---|---|---|---|
| §3 | Gradient G₄ = 8(pᵢ − C) | Gradient G₄ = **6**(pᵢ − C) | ❌ Sfalsyfikowane | v0.3.1-alpha-k1 |
| §4 | Wzory analityczne S₀ przez √3, √5 | Wzory niepoprawne; wartości numeryczne poprawne | ❌ Sfalsyfikowane | v0.3.1-alpha-k1 |
| §5 | Symetria C₂ × C₂ | Symetria jest łamana do trywialnej przez kolejność korekty | ❌ Sfalsyfikowane | v0.3.1-alpha-k1 |
| §6 | Jednoznaczność ze ścisłej wypukłości | Jednoznaczność to hipoteza numeryczna, nie twierdzenie | ❌ Sfalsyfikowany argument | v0.3.1-alpha-k1 |
| §9 | Termodynamika jako „pełny formalizm” | Termodynamika to hipoteza programowa | ❌ Sfalsyfikowany status | v0.3.1-alpha-k1 |
| §6 | Kontrakcyjność K ze stałą (1−α), „potwierdzona na 25 000 prób" | **Sfalsyfikowana** — próba nie aktywowała Kroku 2; kontrprzykład z naruszeniem 26,6% | ❌ Sfalsyfikowane | **v0.4.0-alpha** |
| — | Etykieta AL-H7 użyta dwukrotnie (symetria globalna §5 i jednoznaczność §6) | Jednoznaczność przenumerowana na AL-H8; termodynamika (była H8) na AL-H9 | poprawka redakcyjna | **v0.4.0-alpha** |
| §7 | N9 opisane jako „wstępna weryfikacja numeryczna 🔍, most otwarty" | N9 jest ✅ zamknięte dokładnie (Centroid §8.1, 2026-08-25) — status podniesiony z 🔍 do ✅; hipoteza mostu Alchemy pozostaje 💡, ale z grupą kandydacką zawężoną do S₄ | korekta aktualności (nie była błędem w chwili napisania — dowód powstał później) | **v0.4.3-alpha** |
| §3 | Hipoteza KKT status „otwarte" (💡), falsyfikacja wcześniej podawana ustnie z błędną stałą 3δ² | ❌ Sfalsyfikowana dowodem analitycznym: min G₄=(9/2)δ²<g₀=4,8649δ² | zamknięcie hipotezy | **v0.4.4-alpha** |

---

## Appendix B. Tabela statusów

| Byt | Status | Uzasadnienie |
|---|---|---|
| Gradient G₄ = 6(pᵢ − C) | ✅ | Rachunek bezpośredni, §3 |
| Tożsamość G₄ = ¾Σᵢ<ⱼdᵢⱼ² | ✅ | Oś równoległa + zgodność z gradientem, dwie drogi rachunkowe, §3 |
| **Hipoteza KKT (atraktor = minimalizator ograniczony)** | **❌** | **Sfalsyfikowana analitycznie: min G₄=(9/2)δ² < g₀=4,8649δ², §3** |
| K₁ zmniejsza odległości dokładnie o (1−α) | ✅ | Tożsamość algebraiczna, §1 |
| Wartości numeryczne S₀ | 🔍 | Zweryfikowane numerycznie dla 8 seedów, §4 |
| Wzory analityczne S₀ | 💡 | Otwarte; droga przez KKT zamknięta (§3), wymaga równań punktu stałego K₂, §4, §9 |
| Jedna para na progu (sekwencyjnie) | 🔍 | Obserwacja numeryczna, §2, §5 |
| Symetria lokalna (sekwencyjnie) | ❌ | Tylko identyczność; C₂×C₂ sfalsyfikowane, §5 |
| Stabilizator S₀ w S₄ | ✅ | Trywialny — sześć odległości parami różnych, 24/24 permutacje sprawdzone, §7 |
| Orbita S₀ pod S₄ | ✅ | 24 elementy (maksymalna), §7 |
| Jednoznaczność w basenie (AL-H8) | 💡 | Hipoteza; teraz z mechanizmem lokalnym (§6.2), globalnie bez dowodu, §6 |
| **Kontrakcyjność K (globalna, stała 1−α)** | **❌** | **Sfalsyfikowana kontrprzykładem, §6.1** |
| Kontrakcja lokalna w przestrzeni kształtu (ρ≈0,27) | 🔍 | Rząd wielkości zweryfikowany niezależnie; dokładna wartość spektralna nie odtworzona, §6.2 |
| Atraktor = orbita obrotowa (nie punkt) | ✅ | Procrustes: residual ~10⁻¹⁶, rotacja właściwa det=+1, §6.2 |
| Warianty reguły K₂ (symetryczny/jednopunktowy/symultaniczny) | 💡 | Zgłoszone, nie zweryfikowane niezależnie po znalezieniu błędu w wariancie symetrycznym; nie włączone, §6.2, §9 |
| Globalna symetria S₄ dla N≥2 (AL-H7) | 💡 | Hipoteza; bez dowodu, §5 |
| Termodynamika relacyjna (AL-H9) | 💡 | Hipoteza; bez mikroskopowego uzasadnienia, §8 |
| Skalowanie czasu relaksacji τ (AL-H10) | 🔍 | Replikowane niezależnie kierunkowo; dokładne C(N)/γ(N) zależą od nieustalonej konwencji R₀, §8bis |
| N9 (stabilizator {δ(M_m)} w O(3,ℝ)) | ✅ | Dokładnie S₄, dowód dwukrokowy — Centroid §8.1 (2026-08-25), §7 |
| Most Alchemy↔Net (transport orbity 24 sygnatur pod S₄) | 💡 | Program badawczy; pytanie teraz w pełni skończone, ale niesformułowane precyzyjnie co do warunku „zachowania klasy", §7 |

---

*P₀-Alchemy v0.4.4-alpha. Buduje na v0.4.3-alpha. Cztery zmiany, wszystkie zweryfikowane bezpośrednim uruchomieniem `p0_alchemy_source.py` (δ=0,15, α=0,15, seed=42), nie przyjęte na słowo: §3 KKT zamknięte ❌ dowodem analitycznym (min G₄=(9/2)δ² < g₀=4,8649δ²); §1 formuła Kroku 2 podana jawnie; §7 test 24 izometrii S₄ wykonany (stabilizator trywialny, orbita 24); nowe §6.2 (atraktor = orbita obrotowa SO(3) + kontrakcja lokalna w przestrzeni kształtu ρ≈0,27). Świadomie pominięto trzy dodatkowe zgłoszone wyniki (warianty reguły K₂) — jeden okazał się artefaktem błędu znaku w reimplementacji, pozostałe nie przeszły niezależnej weryfikacji; zob. §6.2, §9 pkt 4. Synteza: 2026-08-10/2026-09-05.*
