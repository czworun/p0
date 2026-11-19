# Korzeń: P₀-AI — adnotacja (v0.3.1-synthesis, 2026-09-10)

**Dokument programowy:** „P₀-AI: Synteza po korektach" v0.3.1-synthesis (2026-09-10) — program badawczy ML testujący hipotezę H-REL-1; synteza pełnego cyklu: v0.1 (17 eksperymentów) → samodzielna krytyka metodologiczna (12 problemów, w tym 6 krytycznych) → przebudowa (p0_common.py v0.3 + sanity_check.py + REL-08..11, korekta Bonferroniego, minimum 30 seedów). **Okres:** IX 2026, przed warsztatem. **Zależności zadeklarowane w dokumencie:** P₀-Centroid, P₀-Defect, P₀-Axis, P₀-SERC (most filozoficzny), P₀-Memory (M16/GDG). **Pozycja w drzewie:** formalnie bliżej gałęzi (operacjonalizacja — glosariusz: „gałęzie = operacjonalizacje i zastosowania, np. model AI"); wpięty do docs/korzenie/ jako dokument przed-warsztatowy zgodnie z obowiązującym wzorcem wpięć; ostateczne miejsce (korzeń vs gałąź) do rozstrzygnięcia przy wpięciu PILLARS-TABLE i konwencji katalogów. **Uwaga redakcyjna:** dokument kończy się bez końcowego znaku nowej linii; verbatim zachowany.

## Co bada ten korzeń

Hipotezę **H-REL-1:** dla niektórych zadań istnieje reprezentacja relacyjna, która zachowuje informację istotną dla zadania bez dostępu do wartości absolutnych. Operacjonalizacja: zestaw reprezentacji konfiguracji K₄ (surowe R; różnice D; projekcja cykliczna P_cyc; cechy iloczynowe P_products; axis; center) × 4 targety niezależne od testowanej reprezentacji (value, volume, moment, radius — żaden nie używa D ani P w konstrukcji) × kontrola architektury i wielokrotne seedy. P_cyc = I₆ − P_{Im(d)}, rzut ortogonalny (ranga 3, tr = 3), gdzie d: C⁰(K₄) → C¹(K₄) to incydencja 6×4.

## Najmocniejsze (w konwencji statusów dokumentu)

- **Aparat przed interpretacją:** sanity_check.py weryfikuje własności algebraiczne (symetria, idempotencja P² = P, P·d = 0, tr = 3) i niezmienniczość (translacja, skala, obrót) **przed** jakimkolwiek wnioskiem z danych — dokładnie bramka sanity warsztatu, odkryta niezależnie przed jego ustanowieniem.
- **Tożsamość P_cyc·D = 0 dla D = dR:** tożsamość algebraiczna, nie wynik eksperymentu — czyste dane leżą w Im(d), więc projektor je zeruje. Konsekwencje jawnie wyprowadzone: P_cyc nie może być featurem na czystych danych; może być regularizerem, detektorem szumu, constraintem.
- **Podwójne niezależne potwierdzenie architecture mismatch:** ten sam wzorzec odkryty niezależnie w wątku M16/GDG (P₀-Memory) i tutaj — R₄ działa na wierzchołkach, D = dx zawsze exact. Dokument sam wskazuje to jako najważniejsze osiągnięcie syntezy.
- **REL-09 ✅:** P_cyc jako prior strukturalny — model bez regularizera nie spełnia constraintu (‖P_cyc·D_pred‖² = 8–15); poprawa −37% (small data), −2,7% (noise); po korekcie Bonferroniego (α = 0,05/12 ≈ 0,0042) istotne tylko scenariusze B i C, nie clean (p = 0,0497).
- **REL-11 Test 1 ✅:** ‖P_cyc·D‖ liniowo mierzy szum w D (ratio ∝ noise_std: 2× szum → 2× defekt; korelacja Spearman ρ = 0,92).

## Koncesje i sęki (obalenia — trwałe)

- **Właśna lista 12 problemów v0.1 (6 krytycznych):** circular reasoning (target zawierał P), błędny zestaw krawędzi w P[:,2], P_products ≠ P_cyc·D, AI-05 bez modelu P₀, AI-08 bez faktycznego K₄ → K₅, shuffle nie niszczył informacji testowej — wzorzec kultury erraty sprzed warsztatu (proto-Z0).
- **REL-08 częściowo tautologiczny (🔍 z zastrzeżeniem):** sukces center dla moment i radius to deterministyczna zależność kolumn center_features — „tożsamość matematyczna w przebraniu eksperymentu", nazwana jawnie przez sam dokument.
- **REL-10 ❌:** soft gating zawodzi dla targetów relacyjnych (gating uśrednia zamiast wybierać; MSE do 48× gorsze od oracle); wynik 4/4 przy N=10 okazał się artefaktem statystycznym (1/4 przy N=30) — trwała lekcja: wynik przy N=10 nie oznacza stabilności.
- **REL-11 Testy 2 i 3 ❌:** P_cyc·D nie przewiduje błędu predykcji (Pearson = 0,033); filtrowanie treningu po P_cyc·D szkodi (+205%, +1054%) — diagnoza ≠ terapia.
- **„P₀ = model bez wartości absolutnych" (v0.1) ❌:** była to hybryda R+D+P+axis+center — główna nadinterpretacja v0.1, skorygowana jawnie.

## Struktury odkryte (🔍)

- **Tabela naturalnych reprezentacji:** value → R (absolutny); volume → axis; moment → center; radius → center — nie istnieje uniwersalnie najlepsza reprezentacja; wybór zależy od struktury targetu.
- **P_cyc jako prior indukcyjny:** constraint strukturalny pomaga najbardziej przy mało danych — klasyczny mechanizm indukcyjnego obciążenia skonkretyzowany strukturą P₀.
- **Stan wiedzy liczony jawnie:** ✅ 6 · 🔍 4 · ❌ 5 · 💡 5; H-REL-1 jako całość: 🔍 częściowo wsparta.

## Mosty do pnia i warsztatu (odczytanie interpretacyjne, 💡)

- **SERC w działaniu:** empiryczna realizacja rozróżnienia stan (wartość) / geometria relacji (struktura) z SERC — reprezentacje relacyjne wygrywają dla targetów geometrycznych, przegrywają z absolutnymi dla value; P₀-SERC figuruje w zależnościach jako „most filozoficzny" — do rozliczenia przy wpięciu SERC do drzewa.
- **Projektor jako obiekt rodzinny:** P_cyc = projekcja (tu: pomiar/regularizer; P₀-Defect: V_cyc = ker dᵀ; Wave §5: stan = projektor, nie widmo) — trzeci kontekst projektorów w rodzinie; kandydat na wspólny wątek „projektor jako obiekt pierwotny" do atlasu pnia (obok trzeciej rodziny S₄).
- **Wave ↔ P₀-AI:** most skręcony znakiem (V_ρ → V_cyc przez standard ⊗ sign) wymieniony w dokumencie jako potencjalne obejście architecture mismatch — wspólna odnoga z Wave/Net, do rozliczenia przy wpięciu Net.
- **Pre-echo bramki sanity i Z2/Z3:** sanity_check.py (porównanie z własnościami referencyjnymi przed rachunkami własnymi) oraz zasada redakcyjna §0 („żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia") — obie praktyki sprzed warsztatu, pokrywają się z zasadami Z2 (jawna konwencja) i Z3 (specyfikacja, nie kod).
- **Z0 przed warsztatem:** wyliczenie 12 własnych problemów + korekta Bonferroniego + wymóg N ≥ 30 — kultura jawnej erraty i statystyki zanim warsztat ją skodyfikował.
- **Axis potwierdzone praktycznie:** osie emergujące z par przeciwległych krawędzi K₄ (P₀-Axis) okazały się najlepszą reprezentacją dla volume (geometria).

## Sęk-odnogi (bank nasion z korzenia)

1. **REL-12 (priorytet A):** prawdziwy transfer K₄ → K₅ (AI-08 v0.1 nie implementował go wcale — dług techniczny v0.1).
2. **REL-08b (priorytet B):** target złożony (proponowany wprost: volume · sign(moment − 3) + log(radius)) — likwiduje tautologię REL-08.
3. **REL-10b (priorytet C):** hard gating (Gumbel-Softmax, MoE, meta-learning ze zadaniami wspierającymi).
4. **Ponowna weryfikacja AI-01–AI-10 w nowym aparacie** — cała faza v0.1 wymaga powtórzenia.
5. **Most skręcony znakiem** (V_ρ → V_cyc, ⊗ sign) oraz powiązanie M16/GDG (architecture mismatch w pamięci) — do rozliczenia przy wpięciach P₀-Net i P₀-Memory.

## Statusy: mapa legendy na konwencje warsztatu

Legenda dokumentu: ✅ Dowiedzione · 📚 Klasyczne · 🔍 Zweryfikowane numerycznie lub symbolicznie · 💡 Przypuszczenie / program · ❌ Sfalsyfikowane, rozszerzona o 🟡 Mieszany (REL-11) — symbol spoza legendy warsztatu, zachowany jako własność dokumentu. Mapowanie na Z1: „✅" dokumentu to wyniki pojedynczego aparatu kodowego → w warsztacie 🔍 (do niezależnej replikacji); jedyna pełna teza = tożsamość P_cyc·D = 0 (twierdzenie, do replikacji Z1); REL-09/10/11 to pojedyncze seedy i jeden aparat → 🔍 warsztatowe przy przenoszeniu do pnia; H-REL-1 jako całość = 🔍 częściowo wsparta. Zasada redakcyjna §0 to antycypacja zasady „status w prozie nie przewyższa statusu twierdzenia" (Z2). Dokument zamyka cykl i deklaruje punkt wyjścia dla dalszych eksperymentów: REL-12 / REL-08b / REL-10b.

## Dokument verbatim (v0.3.1-synthesis, bez zmian)

P₀-AI: Synteza po korektach

Wersja: 0.3.1-synthesis
Data: 2026-09-10
Status: Program badawczy z częściowo domkniętymi wynikami; aparat pomiarowy zweryfikowany; interpretacja v0.1 skorygowana.
Bazuje na: P₀-AI v0.1 (pierwotny), P₀-AI v0.2 (program), P₀-AI v0.3 (korekta metodologiczna), eksperymenty AI-01–AI-10 (v0.1), REL-01–REL-11 (v0.3).
Zależności: P₀-Centroid, P₀-Defect, P₀-Axis, P₀-SERC (most filozoficzny), P₀-Memory (wątek M16/GDG).

---

0. Zasada redakcyjna

Żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia, którego dotyczy.

Statusy: ✅ Dowiedzione · 📚 Klasyczne · 🔍 Zweryfikowane numerycznie lub symbolicznie · 💡 Przypuszczenie / program badawczy · ❌ Sfalsyfikowane.

---

1. Cel i zakres

P₀-AI jest programem badawczym testującym hipotezę:

H-REL-1: Dla niektórych zadań istnieje reprezentacja relacyjna, która zachowuje informację istotną dla zadania bez dostępu do wartości absolutnych.

Program operacjonalizuje tę hipotezę poprzez:

1. Definiowanie reprezentacji relacyjnych (D, P_cyc, P_products, axis, center).
2. Definiowanie niezależnych targetów geometrycznych (value, volume, moment, radius).
3. Porównywanie wydajności modeli na różnych reprezentacjach przy kontroli parametrów i wielokrotnych seedach.
4. Testowanie P_cyc w różnych rolach (feature, regularizer, detektor szumu).

Zakres: dokument obejmuje kompletny cykl po korekcie metodologicznej – od weryfikacji aparatu pomiarowego, przez cztery eksperymenty REL, po syntezę wyników i powiązań z resztą P₀.

---

2. Historia projektu

2.1. Faza 1 – v0.1 (implementacja pierwotna)

Napisano 17 eksperymentów (AI-01 do AI-10, REL-01 do REL-05b) testujących hipotezę H-REL-1. Wyniki były obiecujące, ale zawierały błędy implementacyjne i nadinterpretacje.

2.2. Faza 2 – krytyka metodologiczna

Zidentyfikowano 12 problemów, w tym 6 krytycznych:

# Problem Waga
1 Błędny zestaw krawędzi w P[:,2] (mieszał trójkąty) krytyczny
2 P_products ≠ P_cyc·D (ręczna cecha zamiast projekcji) krytyczny
3 Target zawierał P (circular reasoning) krytyczny
4 AI-05 nie implementował modelu P₀ krytyczny
5 AI-08 nie robił K₄ → K₅ krytyczny
6 P shuffle nie niszczył informacji testowej krytyczny
7 Brak kontroli parametrów między reprezentacjami średni
8 Brak testów niezmienniczości średni
9 AI-07 źle zdefiniowany (kąty bez okresowości) średni
10 Nadinterpretacja "P₀ bez wartości absolutnych" redakcyjny
11 Nazwa center_optimal bez uzasadnienia redakcyjny
12 Target zależny od testowanej reprezentacji krytyczny

2.3. Faza 3 – przebudowa (obecny stan)

Wprowadzono:

· p0_common.py v0.3 – z prawdziwym operatorem P_cyc (macierz projekcji ortogonalnej).
· sanity_check.py – weryfikacja własności algebraicznych.
· REL-08 do REL-11 – cztery nowe eksperymenty w zweryfikowanym aparacie.
· Korekta Bonferroniego dla porównań wielokrotnych.
· N=30 seedów dla testów stabilności.

---

3. Aparat pomiarowy

3.1. Prawdziwy operator cykliczny P_cyc

Definicja:
P_{\text{cyc}} = I_6 - P_{\text{Im}(d)}

gdzie d: C⁰(K₄) → C¹(K₄) to macierz incydencji 6×4.

Własności (zweryfikowane w sanity_check.py):

Własność Wynik Status
Symetria max\|P − Pᵀ\| 0.00e+00 ✅
Idempotencja max\|P² − P\| 5.96e-08 ✅
Trace tr(P) 3.0000 ✅
P·d = 0 max\|P·d\| 3.66e-07 ✅

3.2. Testy niezmienniczości

Transformacja Test Wynik Status
Translacja max\|D(R+a) − D(R)\| 9.54e-07 ✅
Skala max\|P_cyc(sR) − s·P_cyc(R)\| 1.79e-06 ✅
Obrót max\|\|P_cyc(QR)\| − \|P_cyc(R)\|\| 3.65e-07 ✅

3.3. Tożsamość algebraiczna: P_cyc·D = 0 dla D = dR

Twierdzenie: Dla każdej konfiguracji R ∈ ℝ^{4×3}:
D = d \cdot R \implies P_{\text{cyc}} \cdot D = 0

Konsekwencja: P_cyc·D jest tożsamościowo zerem dla czystych danych. Dlatego:

· ❌ P_cyc nie może być użyty jako feature na czystych danych.
· ✅ P_cyc może być użyty jako:
  · regularizer strukturalny (kara za P_cyc·D̂ ≠ 0),
  · detektor szumu (przy D_noisy),
  · constraint w world modelu.

---

4. Zestaw targetów (niezależne od reprezentacji)

Target Definicja Charakter
value mean(R) – średnia współrzędnych absolutny
volume \|det([R₁−R₀, R₂−R₀, R₃−R₀])\| / 6 geometryczny
moment Σ‖Rᵢ − c‖² (moment bezwładności) relacyjny
radius max‖Rᵢ − c‖ (promień) relacyjny

Żaden z nich nie używa D ani P w konstrukcji. To eliminuje circular reasoning v0.1.

---

5. Eksperymenty po korekcie

5.1. REL-08 – Information Sufficiency

Cel: Sprawdzić, która reprezentacja zachowuje informację o którym targetcie.

Setup: 4 targety × 10 reprezentacji × 10 seedów, kontrolowana architektura.

Wyniki:

Target Najlepsza reprezentacja MSE vs R
value R 0.00064 (baseline)
volume axis 0.43590 −50.2%
moment center 0.00038 −98.5%
radius center 0.00025 −99.9%

Wnioski:

1. Każdy target ma swoją naturalną reprezentację.
2. Dla targetów relacyjnych reprezentacje relacyjne są lepsze niż R.
3. Dla targetu absolutnego (value) R jest niezbędne.

Zastrzeżenie (metodologiczne): sukces center dla moment i radius jest częściowo tautologiczny. moment = Σ‖Rᵢ − c‖² i radius = max‖Rᵢ − c‖ to deterministyczne funkcje kolumn z center_features. To nie jest "odkrycie reprezentacji", lecz tożsamość matematyczna w przebraniu eksperymentu. Wartościowa wersja wymaga targetu, którego żadna pojedyncza reprezentacja nie rozwiązuje wprost.

Status: 🔍 Pozytywny (z zastrzeżeniem).

---

5.2. REL-09 – P_cyc jako regularizer

Cel: Sprawdzić, czy constraint P_cyc·D = 0 poprawia uczenie dynamiki.

Setup: World = zamrożony MLP; model w przestrzeni różnic D z karą λ·‖P_cyc·D_pred‖²; 3 scenariusze (clean, noise σ=0.5, small data n=200); 10 seedów.

Wyniki (MSE mean ± std):

Model A (clean) B (noise) C (small)
Baseline 0.000135±6.1e-5 0.263679±1.1e-3 0.031505±2.5e-3
D-model λ=0.1 0.000087±2.7e-5 0.258382±2.5e-3 0.019838±1.8e-3
D-model λ=1.0 0.000090±1.7e-5 0.256495±2.4e-3 0.020304±2.1e-3

Poprawa vs Baseline (z korektą Bonferroniego α=0.05/12=0.0042):

Scenariusz Najlepszy Poprawa p-value Istotne?
A (clean) λ=0.1 −35.9% 0.0497 ❌ NIE
B (noise) λ=1.0 −2.72% 0.0000 ✅ TAK
C (small) λ=0.1 −37.0% 0.0000 ✅ TAK

Kluczowe odkrycie: ‖P_cyc·D_pred‖² bez regularizera = 8–15. Model nie spełnia constraintu sam z siebie. Regularizer redukuje do 10⁻²–10⁻³.

Wnioski:

1. P_cyc jest nietrywialnym constraintem – model nie spełnia go sam.
2. Regularizer pomaga najbardziej przy mało danych (−37%).
3. Efekt jest specyficzny dla scenariuszy z rzeczywistą niespójnością danych (noise, small data); scenariusz clean nie przechodzi korekty Bonferroniego.

Status: ✅ Pozytywny (dla B i C po korekcie).

---

5.3. REL-10 – Auto-wybór reprezentacji (gating)

Cel: Sprawdzić, czy sieć potrafi sama odkryć właściwą reprezentację (soft gating).

Setup: 5 reprezentacji × 4 targety × 30 seedów; gating softmax; porównanie argmax(weight) z optymalną reprezentacją z REL-08.

Wyniki (N_SEEDS=30):

Target argmax trafień Oczekiwana Status
value 30/30 (100%) R ✅
volume 5/30 (17%) axis ❌
moment 10/30 (33%) center ❌
radius 12/30 (40%) center ❌

Kluczowe wagi:

Target Waga R Waga D Waga axis Waga center
value 1.0000 0.0000 0.0000 0.0000
volume 0.3535 0.1608 0.2058 0.2647
moment 0.2284 0.1955 0.2297 0.3385
radius 0.0996 0.1269 0.3615 0.4075

Porównanie MSE (Gated vs Oracle):

Target Gated Oracle Różnica
value 0.00037 0.00049 Gated lepsze
volume 0.3419 0.4143 Gated lepsze
moment 0.01151 0.00024 Gated 48× gorsze
radius 0.00577 0.00020 Gated 29× gorsze

Wnioski:

1. Soft gating działa tylko dla targetu o jednoznacznym sygnale (value) – bo tylko tu jedna reprezentacja (R) jest jednoznacznie najlepsza.
2. Dla targetów relacyjnych gating uśrednia zamiast wybierać – MSE gorsze niż oracle.
3. Wynik N_SEEDS=10 (4/4) był artefaktem statystycznym. Przy N=30 – tylko 1/4 stabilne.

Status: ❌ Negatywny (dla targetów relacyjnych).

---

5.4. REL-11 – P_cyc jako detektor szumu

Cel: Sprawdzić trzy role P_cyc w kontekście zaszumionych danych.

Setup: D = dR + noise; 3 testy; 10 seedów.

Test 1 – estymator szumu:

noise_std mean \|\|P_cyc·D\|\| ratio vs clean
0.00 2.3e-06 (baseline)
0.10 0.199 86,704
0.30 0.598 260,111
0.50 0.996 433,518
1.00 1.993 867,036

Korelacja Pearson = 0.8647, Spearman = 0.9187.

Test 2 – predyktor błędu: Pearson = 0.033 (trywialna korelacja).

Test 3 – filtr treningowy:

Wariant n_train MSE vs all
all 3000 0.006540 –
top_50 1500 0.019957 +205%
top_20 600 0.075439 +1054%

Wnioski:

1. Test 1 (✅): P_cyc·D liniowo mierzy szum w D. Ratio rośnie proporcjonalnie do noise_std (2× noise → 2× defekt). To algebraiczna tożsamość, ale użyteczna jako narzędzie diagnostyczne.
2. Test 2 (❌): P_cyc·D nie przewiduje błędu predykcji (Pearson=0.033). Model trenowany na szumie uczy się być odporny, więc wysoki defekt w próbce testowej nie oznacza wysokiego błędu.
3. Test 3 (❌): Filtrowanie po P_cyc·D szkodzi (+205%, +1054%). Redukcja danych jest zbyt kosztowna, a selekcja nie daje korzyści.

Status: 🟡 Mieszany – Test 1 pozytywny, Testy 2 i 3 negatywne.

---

6. Stan wiedzy po całym cyklu

6.1. Udowodnione (✅)

Fakt Źródło
P_cyc to prawdziwa projekcja ortogonalna (P² = P, P·d = 0, tr = 3) sanity_check
P_cyc·D = 0 dla D = dR (tożsamość algebraiczna) sanity_check
Testy niezmienniczości przechodzą (translacja, skala, obrót) sanity_check
P_cyc·D liniowo mierzy szum w D REL-11 Test 1
P_cyc jako regularizer pomaga przy mało danych (−37%) REL-09 C
P_cyc jako regularizer pomaga przy szumie (−2.7%) REL-09 B

6.2. Wsparte empirycznie (🔍)

Hipoteza Wsparcie
Każdy target ma swoją naturalną reprezentację REL-08
Reprezentacje relacyjne wygrywają dla targetów geometrycznych REL-08 (volume, moment, radius)
Dla targetu absolutnego (value) R jest niezbędne REL-08
Soft gating działa dla jednoznacznego sygnału REL-10 (value)

6.3. Sfalsyfikowane (❌)

Hipoteza Powód
P_cyc jako feature poprawia wyniki P_cyc·D = 0 dla czystych danych
Soft gating automatycznie wybiera reprezentację Zawodzi dla targetów relacyjnych (REL-10)
P_cyc·D przewiduje błąd predykcji Pearson = 0.033 (REL-11 Test 2)
Filtrowanie po P_cyc·D poprawia generalizację +205%, +1054% gorsze (REL-11 Test 3)
"P₀ = model bez wartości absolutnych" (v0.1) Była to hybryda R+D+P+axis+center

6.4. Otwarte (💡)

1. Auto-wybór reprezentacji dla targetów relacyjnych – soft gating zawodzi; wymaga lepszej architektury (hard gating, MoE, meta-learning).
2. Transfer K₄ → K₅ – nieprzetestowane w nowym aparacie.
3. Target złożony – którego żadna pojedyncza reprezentacja nie rozwiązuje wprost.
4. Weryfikacja eksperymentów AI-01–AI-10 w nowym aparacie – wymaga powtórzenia.
5. Powiązanie z M16/GDG – architecture mismatch ma tę samą strukturę.

---

7. Kluczowe odkrycia i ich interpretacja

7.1. Tożsamość P_cyc·D = 0 dla D = dR

To jest to samo zjawisko co architecture mismatch w wątku M16/GDG:

· R₄ działa na wierzchołkach.
· D = dx jest zawsze exact (leży w Im(d)).
· Więc P_cyc·D = 0 dopóki nie zbuduje się mostu skręconego znakiem (V_ρ → V_cyc przez standard ⊗ sign).

To, że ten sam wzorzec pojawił się niezależnie w ML, wzmacnia zaufanie, że to realna własność formalizmu P₀, nie artefakt implementacji.

Konsekwencja dla AI: każdy eksperyment używający P_cyc musi być jawnie zaprojektowany tak, by P_cyc·D ≠ 0 (szum, predykcja, iteracja). Inaczej badamy zero.

7.2. P_cyc jako prior strukturalny

REL-09 pokazał, że P_cyc działa jako prior – najbardziej pomaga przy mało danych (−37%). To jest klasyczne działanie indukcyjnego biasu: gdy danych jest mało, constraint strukturalny jest kluczowy; gdy danych jest dużo, model sam sobie radzi.

Konsekwencja dla AI: P_cyc może być użyteczny w uczeniu z małą liczbą danych. To praktyczne zastosowanie.

7.3. Granice soft gatingu

REL-10 pokazał, że soft gating działa tylko wtedy, gdy jedna reprezentacja jest jednoznacznie lepsza. Gdy kilka jest konkurencyjnych, gating uśrednia zamiast wybierać.

Konsekwencja dla AI: "Auto-wybór struktury" nie jest trywialny. Wymaga albo:

· Hard gating (Gumbel-softmax),
· Mixture of Experts,
· Meta-learning z zadaniami wspierającymi.

7.4. Diagnoza ≠ terapia

REL-11 pokazał, że P_cyc·D mierzy szum (Test 1), ale nie przewiduje jego wpływu na błąd (Test 2) i nie pomaga w filtrowaniu (Test 3). To ważne rozróżnienie metodologiczne: narzędzie diagnostyczne nie jest tym samym co metoda.

Konsekwencja dla AI: P_cyc·D może być używany do kontroli jakości danych przed treningiem, ale nie do selektywnego treningu.

7.5. Targety relacyjne mają różne naturalne reprezentacje

REL-08 pokazał, że:

· value → R (absolutny),
· volume → axis (geometryczny),
· moment → center (relacyjny),
· radius → center (relacyjny).

To wspiera tezę, że nie ma uniwersalnie najlepszej reprezentacji – wybór zależy od struktury targetu.

---

8. Powiązania z resztą P₀

8.1. P₀-Defect – P_cyc jako kluczowa konstrukcja

P₀-Defect definiuje P_cyc jako projekcję na V_cyc = ker(dᵀ). P₀-AI używa tego samego operatora w zupełnie innym kontekście (ML zamiast algebry operatorowej). To wzmacnia spójność formalizmu.

8.2. P₀-Axis – struktura K₄

P₀-Axis pokazuje, że osie (u_X, u_Y, u_Z) emergują z par przeciwległych krawędzi K₄. P₀-AI używa axis_features jako reprezentacji, która okazała się najlepsza dla volume. To zgodne z intuicją, że axis koduje geometrię.

8.3. SERC – struktura vs wartość

SERC w Tomie I rozróżnia stan (wartość) od geometrii relacji (struktura). P₀-AI pokazuje to samo w kontekście AI: reprezentacje relacyjne wygrywają dla targetów geometrycznych, ale nie dla absolutnych.

8.4. M16/GDG – architecture mismatch

Wątek M16 zidentyfikował, że R₄ działa na wierzchołkach, a D = dx jest zawsze exact. P₀-AI odkrył ten sam wzorzec niezależnie. To dwa niezależne potwierdzenia tej samej własności formalizmu P₀.

---

9. Wnioski metodologiczne

9.1. Aparat przed interpretacją

Zanim zaczęliśmy interpretować wyniki, musieliśmy zweryfikować aparat pomiarowy (sanity_check.py). To pozwoliło uniknąć fałszywych wniosków z v0.1.

9.2. Target nie może zależeć od testowanej reprezentacji

Target structural_target = f(D, P) był częściowo tautologiczny. Nowe targety są niezależne, ale wciąż istnieją przypadki tautologiczne (center dla moment).

9.3. Wynik przy N=10 nie oznacza stabilności

REL-10 pokazał, że przy N=10 mieliśmy 4/4 trafień argmax. Przy N=30 – tylko 1/4. Zawsze trzeba sprawdzać stabilność przy większej liczbie seedów.

9.4. Korekta Bonferroniego dla porównań wielokrotnych

REL-09 miał 12 testów istotności. Bez korekty – jedno p=0.0497 wydawało się istotne. Po korekcie (α=0.0042) – tylko efekty z p<0.001 przetrwały.

9.5. Kontrola parametrów

Model GatedModel (49,990 parametrów) był znacznie większy niż SimpleMLP (~5,000). To utrudnia bezpośrednie porównanie. W przyszłych eksperymentach należy kontrolować architekturę.

---

10. Rekomendacje

10.1. Co robić dalej

Priorytet A: REL-12 – Prawdziwy transfer K₄ → K₅

Zdefiniować K₅ (5 wierzchołków, 10 krawędzi) i operator cykliczny dla K₅. Sprawdzić, czy reprezentacje transferują się lepiej niż R.

Priorytet B: REL-08b – Target złożony

Zdefiniować target, którego żadna pojedyncza reprezentacja nie rozwiązuje wprost: np. target = volume · sign(moment − 3) + log(radius). Sprawdzić, czy reprezentacje muszą być złożone, żeby rozwiązać problem.

Priorytet C: REL-10b – Hard gating

Zamienić softmax na Gumbel-Softmax. Sprawdzić, czy wymuszenie koncentracji poprawia auto-wybór reprezentacji.

10.2. Czego nie robić

1. Nie używać P_cyc jako feature na czystych danych – jest tożsamościowo zerem.
2. Nie filtrować treningu po P_cyc·D – szkodzi bardziej niż pomaga.
3. Nie wyciągać wniosków z N=10 seedów – minimalna liczba to 30.
4. Nie porównywać modeli o różnych architekturach bez kontroli parametrów.

10.3. Co wymaga uwagi metodologicznej

1. Tautologia w REL-08 – moment i radius są deterministycznymi funkcjami center_features. Wartościowa wersja wymaga targetu złożonego.
2. Kontrola parametrów – w przyszłych eksperymentach używać identycznej architektury dla wszystkich reprezentacji.
3. Weryfikacja eksperymentów v0.1 – eksperymenty AI-01–AI-10 wymagają powtórzenia w nowym aparacie.

---

11. Podsumowanie

11.1. Stan ogólny

P₀-AI v0.3.1 to program badawczy z zweryfikowanym aparatem pomiarowym i czterema eksperymentami w nowym aparacie. Wyniki są mieszane, ale każdy z nich jest naukowo wartościowy:

Eksperyment Wynik Kluczowe odkrycie
REL-08 🔍 Pozytywny (z zastrzeżeniem) Każdy target ma swoją naturalną reprezentację
REL-09 ✅ Pozytywny P_cyc jako prior pomaga przy mało danych (−37%)
REL-10 ❌ Negatywny Soft gating działa tylko dla jednoznacznego sygnału
REL-11 🟡 Mieszany P_cyc·D to detektor szumu, nie predyktor błędu

11.2. Hipoteza H-REL-1

Status: 🔍 Częściowo wsparta.

· Dla targetów relacyjnych istnieją reprezentacje relacyjne, które są lepsze niż R (REL-08).
· P_cyc jako regularizer działa w obecności rzeczywistej niespójności danych (REL-09).
· Ale auto-wybór reprezentacji (REL-10) i filtr szumu (REL-11) nie działają.

11.3. Najważniejsze osiągnięcie

Odkrycie, że P_cyc·D = 0 dla D = dR to ta sama architecture mismatch co w M16. To wzmacnia spójność formalizmu P₀ i pokazuje, że ten sam problem pojawia się niezależnie w różnych kontekstach.

11.4. Co dalej

Synteza jest punktem zwrotnym. Mamy:

· Zweryfikowany aparat.
· Jasny podział wyników (pozytywne, negatywne, otwarte).
· Zidentyfikowane problemy metodologiczne.

Następne kroki to REL-12 (transfer K₅), REL-08b (target złożony) lub REL-10b (hard gating). Wybór zależy od tego, którą lukę chcemy najpierw zaadresować.

---

12. Załączniki

12.1. Struktura kodu

```
p0_ai/
├── p0_common.py                    # ✅ Aparat pomiarowy v0.3
├── sanity_check.py                 # ✅ Weryfikacja własności algebraicznych
├── rel_08_information_sufficiency.py  # ✅ 4 targety × 10 reprezentacji
├── rel_09_pcyc_regularizer.py      # ✅ P_cyc jako regularizer
├── rel_10_auto_selection.py        # ✅ Gating, 30 seedów
├── rel_11_noise_detector.py        # ✅ P_cyc jako detektor szumu
└── [historyczne, do przepisania]:
    ├── ai_01 do ai_10
    └── rel_01 do rel_05b
```

12.2. Statusy wg zasady redakcyjnej

Kategoria Liczba
✅ Udowodnione 6
🔍 Wsparte empirycznie 4
❌ Sfalsyfikowane 5
💡 Otwarte 5

12.3. Otwarte pytania

1. Czy transfer K₄ → K₅ zachowuje przewagę reprezentacji relacyjnych?
2. Czy target złożony ujawni ukrytą wartość reprezentacji relacyjnych?
3. Czy hard gating rozwiązuje problem auto-wyboru?
4. Czy architecture mismatch (P_cyc·D = 0) można obejść przez most skręcony znakiem?
5. Czy eksperymenty v0.1 potwierdzą się w nowym aparacie?

---

P₀-AI v0.3.1-synthesis. Synteza po korekcie metodologicznej. Wszystkie wyniki zweryfikowane w nowym aparacie pomiarowym. Dokument stanowi punkt wyjścia dla dalszych eksperymentów.