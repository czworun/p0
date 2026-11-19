# Korzeń: P₀-Estrada — adnotacja (v0.8, aktualizacja 2026-11-01)

**Dokument filarowy:** „P₀–Estrada v0.8 — Filary projektu: relacyjna struktura a geometria emergentna" (program badawczy / hipotezy do walidacji; utworzony 2026-08-31, v0.8 z 2026-11-01). Zewnętrzny program porównawczy P₀: formalizm GDG Estrady (emergentna geometria z relacyjnej dynamiki: (G,𝒟) → Q → K_{α,t} → F_{α,t} → geometria, F = K_vv + K_ww − 2K_vw jako macierz kwadratów odległości euklidesowych) zestawiony ze strukturą relacyjną P₀ (C¹(K₄) = Im(d) ⊕ ker δ, D-R3). **Okres:** VIII–XI 2026; dokument żywy, rozwijany równolegle z warsztatem (sesja źródłowa 2026-11-01). **Zmiana v0.7 → v0.8 (deklarowana):** dodano §32–34 (weryfikacja źródłowa nowych prac Estrady 2026/2016, hipoteza H-P₀E2 „antykul", propozycja eksperymentu P₀–Estrada-03), rozszerzono §13, §17, §27, §28. v0.7 pozostaje w repo jako wcześniejsza warstwa (wpięty w rundzie 11cc; czytany przez sesję TAU-10); v0.8 jest nowym SSOT-em korzenia bez cofania historii. **Uwaga redakcyjna:** dokument kończy się bez końcowego znaku nowej linii (ostatni znak to kropka); cudzysłowy typograficzne w §32c („Middle Earth") i apostrofy w §33 należą do oryginału — zachowane verbatim. **Powiązania deklarowane (nagłówek):** D-R3, RD1, C¹(K₄), projekcja cykliczna, SERC, H-P₀E2. **Samookreślenie dokumentu (§17):** nie jest filarem aksjomatycznym — zewnętrzny program porównawczy; kontakt z autorem dopiero po ustabilizowaniu wyników.

## Co bada ten korzeń

Pytanie główne (§14): czy przejście od pełnej przestrzeni relacyjnej do emergentnej geometrii jest informacyjnie odwracalne, tj. czy F_t → C¹(K₄) (przynajmniej F_t → Δ_R) — czy geometria jest pełnym opisem struktury relacyjnej, czy tylko jej projekcją. P₀ odwraca pytanie Estrady: nie relacje → geometria, lecz relacje → struktura relacyjna; geometria może być obserwablą systemu, nie jego konkurencyjną ontologią (§15). Higiena epistemiczna wzorcowa: §13 zamyka 11 zakazanych na tym etapie twierdzeń (m.in. „Estrada niezależnie potwierdził P₀", „sektor cykliczny = ukryta geometria", „e^{-|D|} kanoniczny", „antykul to termin Estrady"); §16/§29 zasada nadrzędna „najpierw struktura, potem interpretacja" — instancja Z0, prosta i uporządkowana. Wartość każdego z możliwych wyników rozpisana w §12: pełna odwracalność, stratność, lub rozłączność informacji — wszystkie trzy rozgałęzienia użyteczne.

## Najmocniejsze (✅/🔍 w konwencji dokumentu)

- **Punkt odniesienia utrwalony źródłowo (§1, §28, §32):** Axioms 15(7) 536 (2026) + preprint techniczny HAL 2025 (hal-05432175v1, jawnie oznaczony jako nie recenzowany); trzy poziomy kontaktu z późniejszymi pracami: korespondencja twierdzeń (§32a), paralela mechanizmów (§32b), kontekst intelektualny (§32c). Weryfikacja bibliograficzna wykonana na źródłach, nie z pamięci.
- **Kontakt dokładny na K₄ (§4–5, §27):** L(K₄) = 4I − J = G₄ — ta sama macierz co centralny operator P₀ (Centroid §8, Axis §7), z jawną uwagą metodologiczną: identyczność macierzy ≠ identyczność operatorów (różne przestrzenie działania). F_t(i,j) = 2e^{-4t}: geometria Estrady na K₄ to regularny czworościan o czasie-zależnej skali, zweryfikowany niezależnie. Rozróżnienie kluczowe „pamięć stanu vs pamięć strukturalna": GDG zachowuje formę, ale traci skalę (kurczy się do punktu); P₀ traktuje formę i skalę jako strukturę stałą. v0.8 dodaje dwa odczyty algebraiczne 4I − J: 3·Gram czworościanu jednostkowego oraz 4·Gram(−1/4) − I (metryka serc, wartość własna konsensusu 1/4 spada do 0) — z odesłaniem do odnogi prowadzonej odrębnie w rejestrze P₀-wyniki.
- **Rekonstrukcja edge-native i odwrócenie intuicji (§18–20):** oryginalny GDG działa na wierzchołkach i nie przyjmuje D jako wejścia (test E trywialny) — dokument uogólnia GDG do odczytu edge-native (ważony Laplasjan wprost z wartości krawędzi). Wynik 02b: geometria reaguje NA OBA sektory (gradientowy i cykliczny, 18 wartości δF zgodnych niezależnie co do 6 miejsc), podczas gdy D-R3 z definicji mierzy wyłącznie sektor cykliczny. Wniosek o przewadze informacji wypada odwrotnie niż sugerowało pytanie wyjściowe — GDG edge-native widzi więcej niż D-R3. Dokument rejestruje tę rewizję jawnie i pozostawia §7–14 w oryginalnym sformułowaniu „dla wierności historii dokumentu" (uwaga v0.5→v0.6) — wzorzec uczciwości redakcyjnej.
- **Pełna widoczność lokalna (§21–23):** pełny Jacobian F_W dla D=𝟏: rząd 6, rangi sektorowe 3/3 (t ∈ {0.1, 1, 2}); macierz J podana wprost (nowość względem v0.7) wraz z wartościami osobliwymi (.6756526, .3378263 ×3, .1689132 ×2); 02c-bis: rząd 6 utrzymuje się w stanach niesymetrycznych (σ_min ≈ 0.163); 02d: 720/720 Jacobianów ma rząd 6 (cztery reżimy próbkowania), potwierdzone niezależnie pochodną Frécheta (blok 2n×2n, Al-Mohy & Higham, SIAM 2009) — zgodność identyczna z różnicami skończonymi, metoda uniewinniona. Jawne zastrzeżenie: silny wynik eksploracyjny, nie twierdzenie globalne; odwracalność lokalna w punktach gładkich ≠ globalna.
- **Kontrolowane skany warunkowania (§24–25):** 02e-bis (oś kontrolowana m = min|D_e| ∈ {10⁻¹…10⁻⁵}): e^{-|D|} κ praktycznie stałe (0.111–0.132 przez 5 rzędów), 1/|D| katastrofalna degradacja (już 3.3×10⁻⁸ przy m=10⁻¹, poniżej 10⁻² szum precyzji). Lekcja numeryczna zapisana wprost: κ → precyzja maszynowa nie jest dowiedzioną utratą rangi. Rodzina f_p(r) = e^{-r^p} (02f): κ ~ m^{|p−1|} (zgodność ≤2% dla 6 wartości p), ALE rozszczepione na DWA jednostronne mechanizmy: p>1 zanikająca czułość kontroluje σ_min, 0<p<1 rozbiegająca czułość ujawnia się w σ_max — nie jedno prawo geometryczne; p=1 jedyny testowany punkt płaski w obu granicach.
- **Dowód formalny R-1a (§30bis-proof, nowość v0.7):** σ_min(J) = c·p·m^{p−1} + o(m^{p−1}), σ_max = O(1), przez perturbację rzędu-1 izolowanego zera osobliwego (J₀ rządu 5, zaburzenie w jedną kolumnę); założenia wypisane jawnie (odwracalność A₀ — generyczna, zweryfikowana numerycznie, nie uniwersalna); człon liniowy zweryfikowany niezależnie: c ≈ 0.6007157 stabilne do 7 cyfr znaczących od m=10⁻³. Jasno zaznaczone, że dowód NIE przenosi się na p<1 (Krok 3 załamuje się: d_{e₀} → ∞, nie 0) — R-1b wymaga innej techniki (rozwinięcie dopasowane), nie lustrzanego odbicia.
- **Równoważność S₄ mapy F_W (§30bis, nowość v0.6):** korekta metodologiczna — D=𝟏 ma trywialny stabilizator (1/24), więc pierwotnie planowany test widma „3+3" był źle postawiony i został wycofany; właściwy test: F_W(Q_sign(π)·D) = Q_plain(π)·F_W(D) dla wszystkich π ∈ S₄ — 480 przypadków, maksymalna odchyłka ≤ 1.1×10⁻¹⁵. F_W splata reprezentację znakowaną na wejściu z zwykłą na wyjściu. Status 🔍 numerycznie do precyzji maszynowej, równoważność oczekiwana strukturalnie (kombinatoryczny Laplasjan), dowód analityczny otwarty.
- **Dychotomia klasyczne/kwantowe i gałąź SERC (§32a, §33 — nowość v0.8):** Mathematics 14(12) 2218 (2026): dyfuzja klasyczna kolapsuje do geometrii sferycznej, dynamika kwantowa generuje generycznie niesferyczną z trwałą anizotropią; wynik K₄ tego dokumentu to dokładnie gałąź klasyczna; uzupełnienie źródłowe z HAL: R(t) ściśle malejące — kolaps sferyczny to konsekwencja dominacji moda konsensusu. §33 proponuje trzecią, nieprzetestowaną w GDG gałąź: klasyczny, ale sekwencyjny (iloczyn per-takt macierzy aktualizacji); para zespolona w widmie SERC R₄ (ρ = 0.170286, ∠25.772°, okres ≈ 13.97 rundy) wyklucza pojedynczy operator symetryczny — nieprzemienność z konwencji porządku P1, nie z unitarności. „Antykul" jawnie jako nazwa robocza Leszka (2026-11-01), nie termin Estrady.

## Koncesje i sęki (obalenia — trwałe)

- **H-P₀E1 w prostej formie niepotwierdzona (§8, §19–20):** pierwotna hipoteza „geometria widzi przede wszystkim sektor exact" upadła w odczycie edge-native — oba sektory widoczne. Sekcje 7–14 pozostawiono w oryginalnym sformułowaniu dla wierności historii, rozstrzygnięcie odesłane do §19–20 i §28. Modelowy przypadek udokumentowanej rewizji własnego pytania.
- **02e wycofane (§24):** klasyfikacja rangowa 3/5/6 dla 1/|D| była artefaktem protokołu próbkowania (brak jawnej dolnej granicy min|D_e|) — zastąpione kontrolowanym 02e-bis. Sęk pełnoprawny z odroślą (kontrolowana oś m stała się standardem skanów).
- **Test widma w D=𝟏 wycofany jako źle postawiony (§30bis):** błędne założenie punktu stałego S₄ (stabilizator trywialny, nie cała grupa); test zastąpiony równoważnością całej mapy. Ujęcie właściwego obiektu zamiast upierania się przy pierwszym pomyśle.
- **Sęk replikacyjny Z2 (uwaga edytorska §21):** wektory bazowe g₂, g₃, z₁–z₃ niezałączone jako dane surowe — macierz J nie jest replikowalna element po elemencie przez stronę trzecią (wartości osobliwe i rząd — tak). Spójne z zastrzeżeniem rejestru warsztatu (runda 11bq): mimo że v0.8 podaje już pełną macierz J, bez surowej bazy pozostaje ona nie-replikowalna element po elemencie.
- **R-1b otwarte (§25, §30):** mechanizm zaobserwowany (σ_max, nie σ_min), dowód R-1a nie przenosi się; wymagane matched asymptotics lub analiza σ_max wprost. Zastrzeżenie techniczne v0.6: dla p<1 parametr f'_p(r) → ∞ nie jest mały — zwykły szereg zaburzeń nie zbiega po tej stronie.
- **Koncesje małe, ale wzorcowe:** Δ_R w §19 podane jako ε/2 z jawną adnotacją niezgodności normalizacji względem D-R1 (konwencja do wyjaśnienia); kanoniczność e^{-|D|} pozostaje hipotezą („najbardziej stabilny z testowanych, nie jedyny możliwy"); 720/720 i 480 eksploracyjne; H-MEM-1 i bridge-independence M16a nieustalone; „efektywne ściąganie krawędzi" tylko interpretacja (§29.7).

## Struktury odkryte (🔍/💡)

- **Widoczność jako obiekt trójparametrowy (§26):** 𝒱_{𝒪,D,t} = dF_{𝒪,t}|_D — zależność od odczytu, stanu i skali; nowy obiekt roboczy P₀ wymagający formalizacji. Odpowiedź na pytanie „czemu e^{-|D|} jest stabilny" schodzi z metafory na rachunek: dwie jednostronne granice σ_min/σ_max.
- **H-P₀E2 „antykul" (§33, 💡):** deflacja konsensusu w SERC usuwa dokładnie ten składnik kernela, który odpowiada za kolaps sferyczny w GDG (spectral filtering: propagator ≈ klasyczny rzutowany na dopełnienie 𝟏 + renormalizacja) — przewidywanie: geometria nie może kolapsować do kula z definicji; operatorowe sformuślenie rozróżnienia „pamięć stanu vs pamięć strukturalna". Hipoteza nie sprawdzona rachunkiem; obalenie/przyjęcie wyznacza eksperyment §34, kryterium obalenia jawne (kolaps mimo deflacji = obalenie; twierdzenia §32a nietknięte).
- **P₀–Estrada-03 (§34, 🔍 propozycja):** GDG na propagatorach SERC (symultaniczny / sekwencyjny naturalny / sekwencyjny lustrzany); obserwable: promień osadzenia R(t), anizotropia, kąt fazy dominującej; predykcje falsyfikowalne P-03a (kontrola negatywna: R(t) ściśle maleje dla symultanicznego), P-03b (sekwencyjne z deflacją nie kolapsują), P-03c (porządek P1 zostawia chiralny ślad w geometrii). Decyzja o uruchomieniu: Leszek; przy wykonaniu Z1, liczby jawnym tekstem, wagi podane.

## Mosty do pnia i warsztatu (odczytanie interpretacyjne, 💡)

- **Rodzina S₄ po raz kolejny, teraz z splotem reprezentacji:** równoważność S₄ F_W (znakowana na wejściu, zwykła na wyjściu) to trzeci niezależny kontekst podpisanej reprezentacji V_cyc ≅ V_std ⊗ sign (S4-Rep, Defect §5, tu) — i pierwszy, w którym splot sign → plain jest mierzalny numerycznie na 480 przypadkach. Do zestawienia w atlasie pnia.
- **TAU-10 jest potomstwem tego korzenia:** pytanie (f) z recenzji tury 8 (czy rank 6 z §23 przenosi się na pełny Jacobian F_W par K₄) zostało rozstrzygnięte TAK lokalnie w sesji TAU-10 (10×9, rząd 9/9 pełny, κ = 0.21/0.18/0.12 przy t ∈ {0.1,1,2}, 720/720 par); dokument był tam czytany w v0.7 — wynik należy formalnie do pnia, ale genetycznie do §21–23 tego korzenia; przy badaniu globalnej odwracalności wracać tu.
- **Ta sama liczba w pniu:** kąt fazy dominującej pary R₄ (∠25.772°, §33) równy co do czterech miejsc kątowi wiecznego muskania ścian T4 z §36 pnia (θ = 25.772093727°, 2× na okres) — ta sama para zespolona napędza dynamikę propagatora i geometrię orbity; przy wykonaniu P₀-Estrada-03 oczekiwać identyfikacji analitycznej, nie tylko numerycznej.
- **Kontakt operatorowy G₄:** L(K₄) = 4I − J = G₄ (Centroid §8, Axis §7); dwa dodatkowe odczyty z §27 (Gram czworościanu jednostkowego, metryka serc −1/4) dają potrójny odczyt jednej macierzy w trzech rolach; odnoga „metryka −1/4 = 4 z 5 wierzchołków 4-simpleksu" prowadzona odrębnie w rejestrze P₀-wyniki (odnotowana tu w v0.8, 2026-11-01).
- **SERC ↔ prace Estrady:** paralela §32b (heterogeniczny konsensus CNSNS 153 109160: stany bez globalnego konsensusu) — SERC osiąga je chirurgią spektralną (deflacja + renormalizacja), Miranda-Moreno-Spiegelberg-Estrada członami reakcyjnymi; formalizmy niezależne, brak twierdzenia o równoważności — paralela mechanizmów 💡, bez przypisywania P₀ wyników Estrady. Dychotomia klasyczne/kwantowe z §32a otrzymuje dzięki SERC trzecią rubrykę (klasyczna sekwencyjność), której GDG nie obejmuje w obecnej postaci — to brak w GDG, nie w P₀.
- **Middle Earth (§32c):** e^{-A²} i informacja w otoczeniu zera widma (arXiv 1607.08812) jako kontekst intelektualny R-1a — rachunek zanikającej wartości osobliwej przy izolowanym zerze to ta sama linia pytaniowa „co niesie środek widma"; nie tożsamość obiektów.
- **Do P₀-Defect:** widoczność F_W rozdzielona na Im(d) i V_cyc to geometryczna wersja rozłączności Im(d) ⊕ V_cyc; pytanie §14 (odwracalność informacyjna C¹(K₄) → F_t) jest geometryczną wersją pytania o kompletność pary sektorów; §21 rangi sektorowe 3/3 jako geometryczne echo „exact = 3, cyclic = 3".
- **Do P₀-Net i P₀-AI:** architecture mismatch M16/GDG (P_cyc·D = 0) dotyczy GDG wierzchołkowego; dokument deklaruje jawno, że GDG klasyczny nie obejmuje propagatorów sekwencyjnych per-takt — dokładnie przestrzeń, w której planuje żyć P₀-Net; most istnieje, ale wymaga konstrukcji (P₀-Estrada-03), nie samej deklaracji.
- **Pre-echo Z1:** zasady redakcyjne §29 (funkcja odczytu jawna przy każdym wyniku; testy radialne na hiperpłaszczyznach kinku; „720/720 nie twierdzenie globalne"; „κ-awaria ≠ utrata rangi") to gotowa bramka sanity dla każdej przyszłej replikacji tego programu; Z2-konsekwencja (brak bazy ⇒ macierz J nie-replikowalna) jest wpisana w dokument, nie w retrospektywę.

## Sęk-odnogi (bank nasion z korzenia)

1. **R-1b (§25, §30):** dowód mechanizmu 0<p<1 (σ_max, matched asymptotics), następnie okolice p=1 (0.90, 0.95, 0.99, 1.01, 1.05, 1.10) — ciągłość przejścia; jeśli szczególność p=1 okaże się głębsza niż własność modelu, wynik wraca do pnia jako §31.
2. **P₀-Estrada-03 (§34, decyzja Leszka):** trzy propagatory, obserwable geometryczne + kryterium obalenia H-P₀E2; przy starcie — protokół replikacji Z1, co najmniej dwa niezależne rachunki, liczby jawnym tekstem.
3. **Formalizacja 𝒱_{𝒪,D,t} (§26):** widoczność jako obiekt trójparametrowy — wymaga zdefiniowania niezmienników względem odczytu; kandydat na łącznik D-R3 ↔ F_W.
4. **Globalna odwracalność (§14, §21, §23):** lokalna pełna widoczność (720/720 rząd 6 dla K₄, rząd 9 dla par z TAU-10) nie dowodzi odwracalności globalnej F_t → C¹(K₄) — pytanie otwarte; brak twierdzenia globalnego to nie wynik negatywny.
5. **H-MEM-1 i bridge-independence M16a (§28, nieustalone):** pamięć wartościowa vs strukturalna; do rozliczenia z eksperymentem 8-agentów (rendezvous) i z wynikami serii Memory.
6. **Rozszerzenie hermitowskie GDG (§28):** zapowiedziane przez Estradę (magnetic Laplacians), niepublikowane — związek z kompleksyfikacją §12H Defect do sprawdzenia po ukazaniu się formalizmu.

## Statusy: mapa legendy na konwencje warsztatu

Legenda dokumentu (✅ ustalone / 🔍 oczekujące / 💡 hipoteza / ✅-kandydat dla korespondencji twierdzeń) jest jednowarstwowa; mapowanie na Z1: „✅" z weryfikacją Claude (02b 18 wartości, 02c Jacobian Frécheta, 02c-bis, 02d 720/720, 02f ≤2%, §30bis 480 przypadków, §30bis-proof człon liniowy 7 cyfr) to pełnoprawne kandydaci na słój (dwa zgodne rachunki); „✅-kandydat" dla korespondencji twierdzeń §32a stwierdza zgodność, nie tożsamość — traktować w pniu jako 💡 do dodatkowego rachunku; statusy wycofane (02e, test widma D=𝟏, H-P₀E1 w prostej formie) pozostają w tabeli §28 jako sęki rejestrowane; „✅" przy źródłach §32 jest weryfikacją bibliograficzną, nie rachunkową — nie podnosi twierdzeń matematycznych. Tablica §28 i lista §13 to wzór statusowania dokumentów porównawczych — do wykorzystania przy przyszłych wpięciach (P₀-Samoodniesienie, Philosophy). Dokument sam deklaruje (§17): program porównawczy, nie filar aksjomatyczny — PILLARS-TABLE uwzględni go jako program zewnętrzny, nie filar pnia.
# P₀–Estrada
## Filary projektu — relacyjna struktura a geometria emergentna

**Nazwa robocza:** P₀–Estrada  
**Plik:** `P0-estrada.md`  
**Data utworzenia:** 31.08.2026  
**Ostatnia aktualizacja:** 01.11.2026 (v0.8 — dodano §32–34: weryfikacja źródłowa nowych prac Estrady 2026/2016, hipoteza H-P₀E2 „antykul", propozycja eksperymentu P₀–Estrada-03; rozszerzono §13, §17, §27, §28)  
**Status:** program badawczy / hipotezy do walidacji  
**Powiązane:** D-R3, RD1, C¹(K₄), projekcja cykliczna, SERC, H-P₀E2

---

# 0. Cel

P₀–Estrada jest linią badawczą mającą porównać dwa formalizmy:

1. **Emergentną geometrię z relacyjnej dynamiki** opisaną przez Estradę.
2. **Relacyjną strukturę P₀**, w szczególności strukturę przestrzeni krawędziowej C¹(K₄), sektor cykliczny oraz miarę D-R3.

Nie zakładamy, że oba formalizmy opisują ten sam obiekt.

Podstawowe pytanie brzmi:

> **Czy geometria emergentna jest pełnym opisem struktury relacyjnej, czy tylko jej projekcją?**

---

# 1. Punkt odniesienia: Estrada

W pracy Estrady relacje i ich dynamika prowadzą do operatora Q, propagatora K oraz obiektu F interpretowanego jako macierz kwadratów odległości euklidesowych.

Schemat:

\[
(G,\mathcal D)
\rightarrow Q
\rightarrow K_{\alpha,t}
\rightarrow F_{\alpha,t}
\rightarrow \text{geometria}.
\]

W szczególności:

\[
F_{\alpha,t}(v,w)
=
K_{vv}+K_{ww}-2K_{vw}.
\]

Istotny rezultat pracy:

> dla odpowiednich symetrycznych operatorów dynamiki obiekt F jest macierzą squared Euclidean distance matrix.

Geometria nie jest więc przyjmowana jako fundament. Jest wynikiem działania relacyjno-spektralnego.

**Źródło zewnętrzne:** Ernesto Estrada, *Emergent Geometry in Complex Systems from Relational Dynamics: The Classical Setting*, *Axioms* 15(7), 536 (2026). Techniczne źródło formalizmu: Estrada, E. *Graph Dynamical Geometrization: A Diffusion-Based Formulation.* 2025, HAL preprint hal-05432175v1 (dostęp 12 lipca 2026) — preprint, nie recenzowana publikacja.

---

# 2. Pytanie P₀

P₀ odwraca pytanie:

Nie:

\[
\text{relacje}\rightarrow\text{geometria},
\]

lecz:

\[
\text{relacje}\rightarrow\text{struktura relacyjna}.
\]

Dla P₀ geometria może być reprezentacją lub projekcją, ale nie musi wyczerpywać całej informacji relacyjnej.

Roboczy schemat:

\[
(G,\mathcal D)
\rightarrow
D
\rightarrow
P_{\rm cyc}
\rightarrow
C(D)
\rightarrow
\Delta_R.
\]

---

# 3. Laboratorium K₄

Pierwszym wspólnym układem jest pełny graf:

\[
K_4.
\]

Ma on:

\[
|V|=4,
\qquad
|E|=6.
\]

Przestrzeń relacji na krawędziach:

\[
C^1(K_4)\cong\mathbb R^6.
\]

To właśnie ta przestrzeń jest podstawowym obiektem RD1/P₀.

---

# 4. Operator wierzchołkowy

Dla K₄ laplasjan kombinatoryczny ma postać:

\[
L(K_4)=4I-J.
\]

Widmo:

\[
\operatorname{spec}(L)=\{0,4,4,4\}.
\]

Rozkład:

\[
\mathbb R^4
=
V_{\rm const}\oplus V_{\rm std},
\]

gdzie:

\[
\dim V_{\rm const}=1,
\qquad
\dim V_{\rm std}=3.
\]

W P₀ macierz:

\[
G=4I-J
\]

pojawia się jako centralny operator/projekcja w analizie struktury K₄.

**Uwaga metodologiczna:** identyczność macierzy nie jest sama w sobie dowodem identyczności znaczenia operatorów. Należy rozróżniać operator, przestrzeń działania i interpretację.

---

# 5. Propagator dla K₄

Dla klasycznej dynamiki:

\[
K_t=e^{-tL}.
\]

Ponieważ:

\[
L=4P_{\rm std},
\]

otrzymujemy:

\[
K_t
=
P_{\rm const}
+
e^{-4t}P_{\rm std}.
\]

Dla różnicy wierzchołkowej:

\[
e_i-e_j\in V_{\rm std},
\]

więc:

\[
K_t(e_i-e_j)
=
e^{-4t}(e_i-e_j).
\]

Stąd:

\[
F_t(i,j)
=(e_i-e_j)^TK_t(e_i-e_j)
=2e^{-4t},
\qquad i\neq j.
\]

W przypadku K₄ geometria Estrady jest zatem regularnym czworościanem o czasie-zależnej skali. Niezależnie zweryfikowano (Claude): zgodne z ogólnym twierdzeniem źródła (\(K_{\alpha,t}\to\tfrac1n\mathbf1\mathbf1^\top\) przy \(t\to\infty\)) oraz z warunkiem brzegowym \(F_0(i,j)=2\).

---

# 6. Pełna przestrzeń relacyjna P₀

P₀ nie zatrzymuje się na przestrzeni wierzchołkowej.

Mamy:

\[
d:C^0(K_4)\rightarrow C^1(K_4),
\]

\[
(dx)_{ij}=x_i-x_j.
\]

Dla K₄:

\[
\dim\operatorname{Im}(d)=3.
\]

Pełna przestrzeń krawędziowa ma wymiar:

\[
\dim C^1(K_4)=6.
\]

Dlatego:

\[
C^1(K_4)
=
\operatorname{Im}(d)
\oplus
\ker\delta.
\]

Wymiarowo:

\[
\boxed{6=3+3}.
\]

W zapisie reprezentacyjnym:

\[
\boxed{
C^1(K_4)
\simeq
V_{\rm std}
\oplus
(V_{\rm std}\otimes\mathrm{sign}).
}
\]

Zgodne z niezależnie ustalonym wynikiem S4-Rep (patrz [[s4-rep]]): V_ρ≅standard, V_cyc≅standard⊗znak.

---

# 7. Kluczowa różnica

Sektor:

\[
\operatorname{Im}(d)\simeq V_{\rm std}
\]

jest bezpośrednio związany z różnicami potencjału na wierzchołkach.

Sektor:

\[
\ker\delta
\]

jest sektorem cyklicznym relacji krawędziowych.

P₀ zachowuje oba sektory.

Formalizm Estrady w opisanej konstrukcji geometrycznej działa natomiast na poziomie operatora wierzchołkowego i generuje geometrię z różnic wierzchołkowych.

To prowadzi do pytania:

\[
\boxed{
\text{Czy geometria Estrady zachowuje pełną informację }C^1(K_4)?
}
\]

Na tym etapie odpowiedź **nie jest przyjęta z góry**.

---

# 8. Hipoteza H-P₀E1

### Hipoteza robocza

\[
\boxed{
\text{Geometria emergentna może być projekcją struktury relacyjnej.}
}
\]

W wersji K₄:

\[
C^1(K_4)
=
\underbrace{\operatorname{Im}(d)}_{3D}
\oplus
\underbrace{\ker\delta}_{3D}.
\]

Hipoteza przewiduje możliwość, że geometria generowana przez formalizm Estrady jest wrażliwa przede wszystkim na pierwszy sektor, podczas gdy pełna przestrzeń relacyjna P₀ zawiera dodatkowe stopnie swobody.

**Status:** hipoteza, nie twierdzenie. **Zaktualizowano w świetle 02b/02c (§19-20): dla odczytu edge-native \(e^{-|D|}\) hipoteza w tej prostej formie nie potwierdziła się — oba sektory okazały się widoczne.**

> **Uwaga (v0.5→v0.6):** kierunek pytania w §7-8 może sugerować przy pierwszej lekturze, że P₀ „widzi więcej" niż GDG. Wynik jest odwrotny: po uogólnieniu do odczytu edge-native, GDG widzi **oba** sektory jednocześnie — więcej niż D-R3, które z definicji rejestruje wyłącznie sektor cykliczny. Sekcje 7-14 pozostawiono w oryginalnym sformułowaniu pytania (dla wierności historii dokumentu), ale rozstrzygnięcie znajduje się w §19-20 i §28.

---

# 9. D-R3 jako test

P₀ posiada:

\[
\boxed{
\Delta_R(A)^2=h^T G h
}
\]

gdzie:

\[
h_e=\frac{D_e^B-D_e^A}{2},
\]

a:

\[
G=P_{\rm cyc}|_S.
\]

Dla czysto cyklicznej różnicy:

\[
h\in\ker\delta,
\]

mamy:

\[
P_{\rm cyc}h=h.
\]

W odpowiedniej normalizacji:

\[
\Delta_R^2=h^Th.
\]

Zatem P₀ ma bezpośrednią miarę różnicy w sektorze cyklicznym.

---

# 10. Eksperyment P₀–Estrada-02

Należy znaleźć dwa stany:

\[
D^{(A)},D^{(B)}\in C^1(K_4)
\]

takie, że:

\[
D^{(B)}-D^{(A)}=z,
\qquad
z\neq0,
\qquad
z\in\ker\delta.
\]

Następnie sprawdzić niezależnie:

### Test E — geometria Estrady

Czy:

\[
F_{\rm Estrada}(D^{(A)})
=
F_{\rm Estrada}(D^{(B)})?
\]

### Test P — P₀

Czy:

\[
\Delta_R(A,B)>0?
\]

Jeżeli oba warunki zachodzą, otrzymujemy konkretny przykład, w którym geometria i pełna miara relacyjna rozróżniają różną ilość informacji.

**Uwaga (v0.5, §19-20): oryginalny GDG (na wierzchołkach) nie przyjmuje w ogóle D jako wejścia — test E w tej formie jest wtedy trywialny. Sensowną wersję dostaje się dopiero po uogólnieniu do odczytu edge-native (jak w §19).**

---

# 11. Interpretacja możliwego wyniku

Jeżeli test przejdzie:

\[
\boxed{
\text{geometria Estrady}
\subsetneq
\text{informacja relacyjna P₀}
}
\]

Oznacza:

> geometria jest jednym z możliwych odczytów struktury relacyjnej i nie musi być jej pełnym niezmiennikiem.

To rozróżnienie jest fundamentalne.

---

# 12. Wynik przeciwny również jest wartościowy

Jeżeli nie znajdziemy takiej pary, należy sprawdzić, czy istnieje odwzorowanie:

\[
\Delta_R
\longleftrightarrow
F_t.
\]

Możliwe wyniki:

### A

\[
F_t=f_t(\Delta_R)
\]

— geometria może być funkcją P₀-owskiego niezmiennika.

### B

\[
\Delta_R=f(F_t)
\]

— geometria może zachowywać całą informację potrzebną do D-R3.

### C

Żadne z powyższych.

— wtedy oba formalizmy mierzą różne aspekty relacyjnej dynamiki.

Każdy z tych wyników jest naukowo użyteczny.

**Zaktualizowano (v0.5): wynikiem empirycznym jest bliżej C — oba formalizmy widzą pewne wspólne, ale nietożsame informacje (patrz §19-20).**

---

# 13. Czego NIE wolno na tym etapie twierdzić

P₀–Estrada nie ustanawia obecnie:

- że Estrada niezależnie potwierdził P₀;
- że sektor cykliczny jest fizycznie „ukrytą geometrią";
- że geometria zawsze jest projekcją P₀;
- że D-R3 jest równoważne konstrukcji Estrady;
- że \(G=4I-J\) ma identyczne znaczenie w obu formalizmach;
- że wynik K₄ uogólnia się automatycznie na dowolny graf;
- że P₀ wyjaśnia mechanizm fizycznej czasoprzestrzeni;
- że \(e^{-|D|}\) jest kanonicznym odczytem relacji (pozostaje najbardziej stabilnym z testowanych, nie jedynym możliwym);
- że „antykul" jest terminem Estrady (nazwa robocza Leszka z 2026-11-01 — §33);
- że dychotomia klasyczne/kwantowe z [Mathematics 2026] zostaje przez SERC rozstrzygnięta (H-P₀E2 to hipoteza — wymaga rachunku, §34);
- że GDG Estrady obejmuje w obecnej postaci propagatory sekwencyjne (formalizm zakłada jeden operator symetryczny; zapowiedziane rozszerzenia hermitowskie nie pokrywają iloczynu per-takt — §33).

Każde z tych twierdzeń wymaga osobnej walidacji.

---

# 14. Najważniejsze pytanie badawcze

Cały program P₀–Estrada można skondensować do:

\[
\boxed{
\textbf{Czy przejście od pełnej przestrzeni relacyjnej do emergentnej geometrii jest informacyjnie odwracalne?}
}
\]

Formalnie:

\[
C^1(K_4)
\longrightarrow
F_t.
\]

Pytamy, czy istnieje:

\[
F_t
\longrightarrow
C^1(K_4)
\]

lub przynajmniej:

\[
F_t
\longrightarrow
\Delta_R.
\]

Jeżeli nie:

\[
\boxed{
\text{geometria jest stratną projekcją relacji}.
}
\]

---

# 15. Znaczenie dla P₀

Jeżeli hipoteza zostanie potwierdzona, P₀ otrzymałby bardzo konkretną strukturę:

\[
\boxed{
\text{pełna relacja}
\rightarrow
\begin{cases}
\text{projekcja geometryczna}\\
\text{struktura cykliczna}\\
\text{defekt}\\
\text{inne niezmienniki}
\end{cases}
}
\]

Wtedy geometria nie byłaby konkurencyjną ontologią wobec P₀.

Byłaby jednym z obserwabli systemu relacyjnego.

---

# 16. Zasada metodologiczna

P₀–Estrada powinno zachować zasadę:

\[
\boxed{
\text{najpierw struktura, potem interpretacja}.
}
\]

Nie zaczynamy od tezy:

> „P₀ jest głębsze od geometrii".

Zaczynamy od:

\[
C^1(K_4)
\rightarrow
F_t
\]

i pytamy matematycznie:

\[
\boxed{
\text{jakiej informacji dokonuje to przejście?}
}
\]

Dopiero wynik eksperymentu może uzasadnić interpretację.

---

# 17. Status filaru

**P₀–Estrada nie jest jeszcze filarem aksjomatycznym P₀.**

Jest:

\[
\boxed{
\text{zewnętrznym programem porównawczym}
}
\]

łączącym P₀ z niezależnym formalizmem emergentnej geometrii.

### Status:

- **Estrada → geometria emergentna:** opublikowany formalizm (i preprint techniczny, §1).
- **K₄: 3+3:** wynik P₀/RD1, zgodny z S4-Rep.
- **D-R3:** wynik P₀.
- **„geometria jest projekcją sektora relacyjnego":** hipoteza częściowo zrewidowana (§19-20).
- **P₀–Estrada-02:** wykonane w wersji edge-native (§19-20).
- **nowe źródła 2026/2016 (quantum walks, heterogeneous consensus, Middle Earth):** zweryfikowane źródłowo (v0.8, §32).
- **kontakt z autorem:** dopiero po ustabilizowaniu wyników.

---

# 18. Rekonstrukcja P₀–Estrada-02 (edge-native)

Oryginalny test (§10) w formie dosłownej jest niewykonalny: opublikowany GDG działa na wierzchołkach i nie przyjmuje D jako wejścia — „\(F_E(A)=F_E(B)\)" byłoby prawdziwe trywialnie dla każdych A, B.

Aby test miał treść, uogólniono GDG do odczytu **edge-native**: ważony Laplasjan budowany wprost z wartości krawędzi D (nie przez potencjał wierzchołkowy):

\[
L(D)_{ij}=-w(D_{ij}),\qquad w_e=f(|D_e|),
\]

\[
F_{W,t}(D)_{ij}=K_{ii}+K_{jj}-2K_{ij},\qquad K_t=e^{-tL(D)}.
\]

Dalsze sekcje (19+) opisują wyniki tej rekonstrukcji.

---

# 19. 02b — oba sektory są lokalnie widoczne

Badano perturbacje gradientowe \(g\in\operatorname{Im}(d)\) i cykliczne \(z\in\ker(\delta)\), przy \(D^B=D^A+\varepsilon g\) lub \(D^B=D^A+\varepsilon z\), odczyt \(w_e=e^{-D_e}\), \(D^A=\mathbf1\).

| ε | sektor | Δ_R | δF(.1) | δF(1) | δF(2) |
|---:|---|---:|---:|---:|---:|
| .05 | g | 0 | .006824 | .017854 | .008050 |
| .05 | z | .025 | .006348 | .016679 | .007556 |
| .10 | g | 0 | .013831 | .035579 | .015749 |
| .10 | z | .050 | .012825 | .033278 | .014872 |
| .20 | g | 0 | .028421 | .070593 | .030103 |
| .20 | z | .100 | .026200 | .066231 | .028791 |

Zweryfikowane niezależnie (Claude): wszystkie 18 wartości δF zgodne co do 6 miejsca po przecinku. Δ_R podane tu jako ε/2 — konwencja normalizacji do wyjaśnienia względem D-R1 (Δ_R z definicji \(h^Th\) daje ε, nie ε/2, dla znormalizowanego z).

W badanym odczycie edge-native geometria reaguje na oba sektory, podczas gdy D-R3 mierzy wyłącznie badaną różnicę cykliczną.

---

# 20. 02-W-OR — kontrola orientacji

Porównano \(w_e=e^{-D_e}\) z niezmienniczym względem orientacji \(w_e=e^{-|D_e|}\).

Dla \(D^A=\mathbf1\) i \(\varepsilon\le0{,}2\) oba odczyty są lokalnie identyczne. Dla \(D^A=0\) test symetrii daje dla \(e^{-D}\) zakres \(A(z)=0{,}82\ldots1{,}22\), natomiast dla \(e^{-|D|}\) dokładnie \(A(z)=1\). Oba sektory pozostają widoczne w obu wariantach.

Na \(D_e=0\) zwykły Jacobian dla \(e^{-|D|}\) nie istnieje (kink); stosujemy test radialny/symetryczny zamiast zwykłej pochodnej.

---

# 21. 02c — pełny Jacobian

W bazie ortonormalnej \((g_1,g_2,g_3,z_1,z_2,z_3)\) pełny Jacobian \(J=dF_W|_D:\mathbb R^6\to\mathbb R^6\) ma dla \(D=\mathbf1,t=1\):

\[
J=\begin{pmatrix}
0&0&-.292566&-.189847&.140680&.035079\\
-.103438&-.059720&-.292566&-.057174&-.191705&.052705\\
-.103438&.179159&-.292566&.110243&.044594&.011120\\
-.241355&-.059720&-.097522&-.163312&.031732&.208929\\
-.241355&.179159&-.097522&-.163312&.102517&-.074945\\
-.137917&.238879&-.097522&-.083709&-.153542&.162730
\end{pmatrix}.
\]

Wartości singularne dla \(t=1\):

\[
(.6756526,.3378263,.3378263,.3378263,.1689132,.1689132).
\]

**Zweryfikowane w pełni niezależnie (Claude, dokładna pochodna Frécheta metodą bloku 2n×2n, nie różnice skończone — metoda standardowa, zob. Al-Mohy & Higham, *Computing the Fréchet Derivative of the Matrix Exponential*, SIAM J. Matrix Anal. Appl. 30(4), 2009): identyczne co do 6 miejsca po przecinku.**

Rząd wynosi 6; rangi sektorowe 3/3. Dla \(t=0{,}1\) i \(t=2\) również otrzymano rząd 6.

To daje lokalną odwracalność w punktach gładkich, ale nie dowodzi odwracalności globalnej.

**Uwaga edytorska:** wektory bazowe \(g_2,g_3,z_1,z_2,z_3\) (poza \(g_0,z_0\) podanymi w §22) nie zostały dotąd załączone jako dane surowe — bez nich powyższa macierz \(J\) nie jest replikowalna element po elemencie przez stronę trzecią (wartości singularne — tak, macierz — nie).

---

# 22. 02c-bis — stan niesymetryczny

Dla \(D'=\mathbf1+0{,}1\,g_0\) oraz \(D''=\mathbf1+0{,}1\,z_0\), z

\[
g_0=(-0{,}707107,-0{,}353553,-0{,}353553,0{,}353553,0{,}353553,0),
\]
\[
z_0=(-0{,}561966,-0{,}090696,0{,}652662,-0{,}157090,-0{,}404876,-0{,}247786),
\]

otrzymano w obu przypadkach rank 6, rangi sektorowe 3/3. Najmniejsze wartości osobliwe: \(\sigma_{\min}\approx0{,}163\) dla \(D'\), \(\approx0{,}162\) dla \(D''\) (zweryfikowane niezależnie, zgodne co do rzędu wielkości; dokładna 4. cyfra znacząca zależy od wyboru konkretnego wektora w obrębie 3-wymiarowej podprzestrzeni).

Oznacza to, że pełna lokalna widoczność utrzymuje się po odchyleniu stanu od symetrycznej referencji.

---

# 23. 02d — 720 Jacobianów

Dla 240 losowych stanów (cztery reżimy próbkowania) i \(t\in\{0{,}1,1,2\}\) wykonano 720 obliczeń Jacobiana.

Dla \(e^{-|D|}\):

\[
\boxed{720/720\text{ ma rząd }6.}
\]

**Zweryfikowane niezależnie w pełni (Claude, dokładna pochodna Frécheta): potwierdzone 720/720, identyczny wynik jak przy różnicach skończonych — nie był to artefakt metody numerycznej.**

Jest to silny wynik eksploracyjny, nie twierdzenie globalne.

---

# 24. 02e / 02e-bis — alternatywne odczyty i kontrolowany skan

Pierwotna wersja 02e (podział na reżimy próbkowania, klasyfikacja rangowa 3/5/6 dla \(1/|D|\)) okazała się częściowo artefaktem protokołu próbkowania (brak jawnej dolnej granicy \(\min|D_e|\)) — **wycofana**, zastąpiona kontrolowanym skanem 02e-bis.

**02e-bis:** kontrolowana oś \(m=\min_e|D_e|\in\{10^{-1},\ldots,10^{-5}\}\), \(t=1\), raportowane osobno \(\sigma_{\min},\sigma_{\max},\kappa=\sigma_{\min}/\sigma_{\max}\):

| m | \(e^{-|D|}\): κ | \(1/|D|\): κ |
|---:|---:|---:|
| \(10^{-1}\) | 0,132 | \(3{,}3\times10^{-8}\) |
| \(10^{-2}\) | 0,122 | \(7{,}0\times10^{-16}\) |
| \(10^{-3}\) | 0,123 | \(9{,}4\times10^{-16}\) |
| \(10^{-4}\) | 0,115 | \(5{,}5\times10^{-16}\) |
| \(10^{-5}\) | 0,111 | \(7{,}4\times10^{-16}\) |

\(e^{-|D|}\): κ praktycznie stałe przez 5 rzędów wielkości \(m\). \(1/|D|\): κ zapada natychmiast (już przy \(m=0{,}1\)), poniżej \(m=10^{-2}\) wynik jest w szumie precyzji maszynowej — nie należy interpretować tego jako dowiedzionej struktury poniżej tego poziomu.

**Wniosek:** \(1/|D|\) wykazuje katastrofalną degradację uwarunkowania Jacobiana przy kontrolowanym zmniejszaniu \(\min|D_e|\); \(e^{-|D|}\) pozostaje stabilne. Nie należy mówić o „utracie rangi" w sposób nieostrożny — poniżej precyzji maszynowej nie odróżniamy rzeczywistego zera od zaokrąglenia.

---

# 25. 02f — rodzina \(f_p(r)=e^{-r^p}\)

Rozszerzono skan na rodzinę \(f_p(r)=e^{-r^p}\), \(p\in\{0{,}5,\,0{,}8,\,1,\,1{,}5,\,2,\,3\}\), z tą samą kontrolowaną osią \(m\).

| p | α: \(\sigma_{\min}\sim m^\alpha\) | β: \(\sigma_{\max}\sim m^\beta\) | α−β | \(\vert p-1\vert\) |
|---:|---:|---:|---:|---:|
| 0,5 | 0,024 | −0,480 | 0,504 | 0,500 |
| 0,8 | 0,014 | −0,171 | 0,184 | 0,200 |
| 1,0 | 0,007 | 0,006 | 0,001 | 0 |
| 1,5 | 0,440 | −0,003 | 0,444 | 0,500 |
| 2,0 | 1,014 | 0,013 | 1,001 | 1,000 |
| 3,0 | 2,043 | 0,021 | 2,022 | 2,000 |

Zweryfikowane niezależnie (Claude): dopasowana potęga zgodna z \(|p-1|\) w granicach ≤2% dla wszystkich sześciu wartości p.

**Kluczowy wynik: symetria \(\kappa\sim m^{|p-1|}\) wynika z DWÓCH różnych, jednostronnych mechanizmów, nie z jednego prawa geometrycznego** (rozdzielono osobno \(\sigma_{\min}\) i \(\sigma_{\max}\), nie tylko ich stosunek):

- **Dla \(p>1\):** \(\sigma_{\max}=O(1)\) (płaskie), \(\sigma_{\min}\sim m^{p-1}\) — zanikająca czułość (\(f_p'(r)\sim r^{p-1}\to0\)).
- **Dla \(0<p<1\):** \(\sigma_{\min}=O(1)\) (płaskie), \(\sigma_{\max}\sim m^{1-p}\) — rozbiegająca czułość (\(f_p'(r)\sim r^{p-1}\to\infty\)), ujawniająca się jednak w \(\sigma_{\max}\), nie w \(\sigma_{\min}\).
- Dla \(p=1\) obie granice pozostają płaskie — jedyny testowany punkt bez zależności od m.

Nie nazywamy tego jeszcze twierdzeniem — dowód analityczny jest bezpośrednio dostępny dla strony \(p>1\) (z rozwinięcia Taylora \(f_p'\)), ale strona \(p<1\) (gdzie mechanizm dotyczy \(\sigma_{\max}\), nie \(\sigma_{\min}\)) wymaga osobnego wyprowadzenia.

### Kandydackie lematy R-1a/R-1b

Przy regularności pozostałej części Jacobianu i braku szczególnego kasowania:

- **R-1a** (\(p>1\)): zanikająca czułość kontroluje \(\sigma_{\min}\);
- **R-1b** (\(0<p<1\)): rozbiegająca czułość kontroluje \(\sigma_{\max}\).

Wtedy \(\kappa\sim m^{|p-1|}\) jest konsekwencją dwóch lematów, a nie jednym podstawowym prawem geometrycznym.

---

# 26. Widoczność jako obiekt trójparametrowy

Roboczo:

\[
\boxed{\mathscr V_{\mathcal O,D,t}=dF_{\mathcal O,t}\big|_D}.
\]

Widoczność zależy więc od stanu D, operatora/odczytu 𝒪 oraz skali t. Jest to nowy obiekt roboczy P₀ wymagający formalizacji.

---

# 27. Dokładny kontakt na K₄: L(K₄)=G₄

Dla \(K_4\):

\[
L=D_{\rm deg}-A=3I-(J-I)=4I-J.
\]

Jest to dokładnie ta sama macierz co \(G=4I-J\) pojawiające się w P₀ (Centroid §8, Axis §7). Jest to jednak tożsamość macierzowa, nie automatyczna identyfikacja operatorów, ponieważ naturalne przestrzenie działania są różne.

Dwa łańcuchy można zapisać:

\[
\text{relacje}\to G\to\text{metryka}\to\text{czworościan},
\]
\[
\text{relacje}\to L(K_4)=G\to e^{-tG}\to F_t\to\text{czworościan}.
\]

Dla klasycznej dyfuzji:

\[
F_t(i,j)=2e^{-4t},\qquad d_t(i,j)=\sqrt2\,e^{-2t}.
\]

GDG zachowuje formę czworościanu, ale traci skalę (kurczy się wykładniczo do punktu) — P₀ traktuje formę i skalę jako strukturę stałą (metryka G₄ niezależna od iteracji, Centroid §2.4). To **analogia**, nie dowód równoważności P₀ i GDG, ale silny punkt łączący obie teorie — kluczowe rozróżnienie „pamięć stanu vs pamięć strukturalna".

**Uwaga (v0.8, odesłanie):** ta sama macierz ma dwa dodatkowe odczyty algebraiczne, oba elementarne: \(4I-J=3\cdot\mathrm{Gram}\) czworościanu jednostkowego w \(\mathbb R^3\) (iloczyny \(-1/3\)); oraz \(4I-J=4\cdot\mathrm{Gram}(-1/4)-I\), gdzie \(\mathrm{Gram}(-1/4)=(5/4)I-(1/4)J\) to prehistoryczna metryka serc (wartość własna konsensusu \(1/4\), po przejściu \(4\cdot\mathrm{Gram}-I\) spada do \(0\)). Wątek „metryka \(-1/4\) = 4 z 5 wierzchołków 4-simpleksu" prowadzony jest odrębnie (odnoga puszczona 2026-11-01; rejestr: temat P₀–wyniki) — identyczność macierzowa, nie identyfikacja operatorów (§4).

---

# 28. Zaktualizowany status (v0.5)

| Element | Status |
|---|---|
| GDG Estrady jako niezależny formalizm | ustalone źródłowo |
| Geometria z kernela \(e^{-tQ}\) | ustalona w GDG |
| Preprint techniczny [21] (HAL 2025) | zweryfikowany bezpośrednio z bibliografii |
| \(F_t(i,j)=2e^{-4t}\) dla \(K_4\) | zweryfikowane niezależnie, zgodne z [21] |
| \(C^1(K_4)=3+3\simeq V_{\rm std}\oplus(V_{\rm std}\otimes{\rm sign})\) | wynik P₀/RD1, zgodny z S4-Rep |
| D-R3 | wynik P₀ |
| 02b, 02-W-OR, 02c, 02c-bis, 02d | zweryfikowane niezależnie (Claude), zgodne |
| 02e (stara wersja, klasyfikacja rangowa 3/5/6) | **wycofane** — artefakt protokołu próbkowania |
| 02e-bis (kontrolowany skan m) | zweryfikowane niezależnie, mocny wynik |
| 02f (rodzina \(e^{-r^p}\)) | zweryfikowane niezależnie, zgodność ≤2% |
| R-1a (mechanizm p>1) | **dowiedzione formalnie (v0.7, §30bis-proof)** — perturbacja rzędu-1 izolowanego zera osobliwego, zweryfikowane numerycznie do 7 cyfr |
| R-1b (mechanizm 0<p<1) | mechanizm zaobserwowany (dotyczy σ_max, nie σ_min), dowód R-1a nie przenosi się wprost (Krok 3 załamuje się) — wymaga osobnej techniki |
| Równoważność S₄ mapy \(F_W\) (splot znak/bez znaku) | zweryfikowane numerycznie do precyzji maszynowej (v0.6) |
| Stabilizator \(D=\mathbf1\) pod S₄ | trywialny (1/24) — poprzedni test widma w tym punkcie wycofany jako źle postawiony |
| \(e^{-|D|}\) jako odczyt | najbardziej stabilny z testowanych, **nie** kanoniczny |
| \(\mathscr V_{\mathcal O,D,t}\) | hipoteza / nowy obiekt roboczy P₀ |
| H-MEM-1 | nadal hipoteza |
| Bridge-independence M16a | nieustalone |
| Związek z P₀-Hilbert/R3 | otwarty — rozszerzenie hermitowskie GDG zapowiedziane, niepublikowane |
| Eksperyment 8-agentów Estrady (rendezvous) | konkretna, źródłowa ilustracja analogii pamięć-wartościowa/strukturalna |
| [Mathematics 2026] quantum walks — dychotomia sferyczna/niesferyczna | zweryfikowane źródłowo (v0.8, §32a) |
| [CNSNS 2026] heterogeneous consensus | zweryfikowane źródłowo (v0.8, §32b); paralela z SERC 💡 |
| [arXiv 2016] „Middle Earth" \(e^{-A^2}\) | kontekst intelektualny R-1a (v0.8, §32c) — nie tożsamość |
| H-P₀E2 („antykul": SERC jako GDG z wyciętym konsensusem) | hipoteza 💡 — nie sprawdzona rachunkiem (§33) |
| P₀–Estrada-03 (GDG na propagatorach SERC) | propozycja 🔍 — decyzja o uruchomieniu: Leszek (§34) |

**Zasada metodologiczna:** żadna analogia z pracami Estrady nie jest traktowana jako dowód P₀ bez osobnego dowodu lub niezależnego eksperymentu.

---

# 29. Zasady redakcyjne

1. \(F_t\neq\Delta_R\) — nie utożsamiać bez dowodu.
2. Funkcja odczytu (\(w_e\)) musi być zawsze jawnie podana przy każdym wyniku.
3. Na hiperpłaszczyznach \(D_e=0\) nie stosujemy zwykłego Jacobianu, jeśli odczyt jest nieróżniczkowalny (kink) — testy radialne/symetryczne zamiast tego.
4. „720/720 rank 6" nie jest twierdzeniem globalnym — dotyczy zbadanego protokołu próbkowania.
5. Kanoniczność \(e^{-|D|}\) pozostaje hipotezą, nie ustaleniem.
6. Katastrofalne uwarunkowanie (\(\kappa\to\)precyzja maszynowa) nie jest automatycznie dowiedzioną utratą rangi.
7. „Efektywne ściąganie krawędzi" pozostaje interpretacją, nie twierdzeniem.
8. H-MEM-1 pozostaje hipotezą.
9. Zasada nadrzędna:

\[
\boxed{\text{najpierw struktura, potem interpretacja.}}
\]

---

# 30. Następny krok: 02f-bis

Nie kolejny szeroki skan funkcji, lecz próba dowodu analitycznego. Należy sprawdzić, czy w pobliżu \(m=\min|D_e|\):

\[
J_p(m)=J_{\rm reg}+a_p(m)\,uv^T+\text{wyższe rzędy},
\qquad
a_p(m)\sim p\,m^{p-1}.
\]

Należy osobno wykazać mechanizm dla \(p>1\) i \(0<p<1\) (ten drugi wciąż otwarty — dotyczy \(\sigma_{\max}\), nie \(\sigma_{\min}\)), a następnie zbadać okolice \(p=1\): \(0{,}90,\,0{,}95,\,0{,}99,\,1,\,1{,}01,\,1{,}05,\,1{,}10\), by sprawdzić ciągłość przejścia.

**Zastrzeżenie techniczne (v0.6):** dla \(p>1\) pochodna wagi \(f_p'(r)\sim r^{p-1}\to0\) jest MAŁYM parametrem — stosuje się standardowa teoria zaburzeń dla funkcji macierzowych (rozwinięcie wokół \(a_p=0\)). Dla \(0<p<1\) odpowiadający parametr \(f_p'(r)\to\infty\) — **nie jest mały**, więc zwykły szereg zaburzeń użyty po stronie \(p>1\) prawdopodobnie nie zbiega po tej stronie wprost. Dowód R-1b może wymagać innej techniki (np. rozwinięcia dopasowanego/matched asymptotics, albo analizy przez \(\sigma_{\max}\) wprost, nie przez zaburzenie \(\sigma_{\min}\)) — nie należy próbować powielić dowodu R-1a z odwróconym znakiem wykładnika.

---

# 30bis-proof. Dowód formalny R-1a (nowość v0.7)

### Twierdzenie

Niech \(D\in\mathbb R^6\) ma pięć składowych ustalonych, \(|D_e|=O(1)\), oraz jedną wyróżnioną, \(|D_{e_0}|=m\to0^+\). Dla \(f_p(r)=e^{-r^p}\), \(p>1\), Jacobian \(J=dF_W|_D\) spełnia:

\[
\sigma_{\min}(J)=c\,p\,m^{p-1}+o(m^{p-1}),
\qquad
\sigma_{\max}(J)=O(1),
\]

gdzie \(c>0\) jest stałą zależną od \(D\), generycznie niezerową.

### Dowód

**Krok 1 (reguła łańcuchowa).** Niech \(A:=\partial F/\partial w\in\mathbb R^{6\times6}\) będzie Jacobianem odwzorowania waga→odległość, obliczonym w wektorze wag \(w^*\). Wtedy \(J=A\cdot\operatorname{diag}(d_1,\ldots,d_6)\), \(d_e=f_p'(|D_e|)\operatorname{sign}(D_e)\).

**Krok 2 (skalowanie przekątnej).** Dla \(e_0\): \(f_p'(m)=-p\,m^{p-1}e^{-m^p}\). Ponieważ \(p>1\): \(m^{p-1}\to0\), \(e^{-m^p}\to1\), więc \(d_{e_0}=-p\,m^{p-1}(1+o(1))\to0\). Dla pozostałych pięciu krawędzi \(d_e=O(1)\), generycznie niezerowe.

**Krok 3 (macierz graniczna).** Gdy \(m\to0\): \(A\to A_0\) (skończone, gładkie w \(w\), bo \(w_{e_0}\to f_p(0)=1\) — punkt regularny). Macierz \(J_0:=A_0\cdot\operatorname{diag}(d_1,\ldots,0,\ldots,d_6)\) ma zerową \(e_0\)-tą kolumnę, więc \(\operatorname{rank}(J_0)\le5\). Ponieważ \(A_0\) jest odwracalne (zweryfikowane numerycznie: 720/720 pełny rząd, §23) i pozostałe \(d_e\neq0\), pięć pozostałych kolumn jest liniowo niezależnych — \(\operatorname{rank}(J_0)=5\) dokładnie, z pojedynczą, izolowaną zerową wartością osobliwą.

**Krok 4 (perturbacja rzędu-1).** \(J=J_0+d_{e_0}A_0e_{e_0}e_{e_0}^\top+O(A-A_0)\) — zaburzenie macierzy o izolowanej zerowej wartości osobliwej, w kierunku pojedynczej kolumny. Standardowa teoria perturbacji (rzut kolumny \(A_0e_{e_0}\) na dopełnienie ortogonalne obrazu pozostałych kolumn) daje:

\[
\sigma_{\min}(J)=|d_{e_0}|\cdot\operatorname{dist}\!\big(A_0e_{e_0},\,\operatorname{span}(\text{pozostałe kolumny }A_0)\big)+o(|d_{e_0}|)
=c\,p\,m^{p-1}(1+o(1)),
\]

z \(c>0\), bo \(A_0\) odwracalne \(\Rightarrow\) odległość kolumny od rozpięcia pozostałych jest ściśle dodatnia.

**Krok 5 (\(\sigma_{\max}\)).** \(\|J\|\le\|A\|\cdot\max_e|d_e|=O(1)\), bo \(A\to A_0\) skończone i wszystkie \(d_e\) ograniczone.

Stąd \(\kappa(m)=\sigma_{\min}/\sigma_{\max}\sim m^{p-1}\). \(\blacksquare\)

### Weryfikacja numeryczna zgodności rzędu wiodącego

Nie tylko wykładnik, ale **cały człon liniowy** został sprawdzony (Claude): dla losowego \(D\) (pięć składowych ustalonych, \(p=2\)), \(\sigma_{\min}(J)/m^{p-1}\) zbiega do stałej \(c\approx0{,}6007157\), stabilnej do 7 cyfr znaczących od \(m=10^{-3}\) w dół:

| m | σ_min | σ_min/m^(p−1) |
|---:|---:|---:|
| \(10^{-1}\) | 5,568×10⁻² | 0,55678 |
| \(10^{-2}\) | 6,003×10⁻³ | 0,60030 |
| \(10^{-3}\) | 6,007×10⁻⁴ | 0,60072 |
| \(10^{-4}\) | 6,007×10⁻⁵ | 0,60072 |
| \(10^{-5}\) | 6,007×10⁻⁶ | 0,60072 |
| \(10^{-6}\) | 6,007×10⁻⁷ | 0,60072 |

### Status i zastrzeżenia

**Dowód formalny (standardowa teoria perturbacji macierzy dla zaburzenia rzędu-1 izolowanego zera osobliwego).** Jedno założenie wypisane jawnie: odwracalność \(A_0\) (Jacobian na pozostałych 5 krawędziach) — generyczne, zweryfikowane numerycznie (§23, 720/720), ale nie jest twierdzeniem uniwersalnym dla każdego \(D\) (może zawieść na mierze zero konfiguracji).

**Dla \(p<1\) ten dowód nie działa** — Krok 3 (macierz granicząca \(A\to A_0\) skończona) załamuje się, bo \(d_{e_0}\to\infty\), nie \(0\). Potwierdza to wcześniejsze podejrzenie: R-1b wymaga osobnej techniki (np. rozwinięcia dopasowanego), nie jest lustrzanym odbiciem tego dowodu.

---

# 30bis. Równoważność S₄ mapy \(F_W\) (nowość v0.6)

### Kontekst

Naturalne pytanie: czy odczyt edge-native \(F_W\) (§18) respektuje strukturę reprezentacyjną \(C^1(K_4)\simeq V_{\rm std}\oplus(V_{\rm std}\otimes{\rm sign})\) ustaloną w [[s4-rep]]? Pierwszy pomysł testu — zbadanie widma Jacobianu \(J=dF_W|_{D=\mathbf1}\) pod kątem wzoru „3+3" — opierał się na błędnym założeniu.

### Korekta: \(D=\mathbf1\) nie jest niezmiennicze pod S₄

Zweryfikowano bezpośrednio: w poprawnej, znakowanej reprezentacji permutacyjnej na krawędziach (ta sama, która ujawniła skręt \(V_{\rm cyc}\simeq V_{\rm std}\otimes{\rm sign}\) w S4-Rep), wektor \(D=\mathbf1\) jest niezmienniczy **tylko pod identycznością** (1 z 24 permutacji), nie pod całą grupą. Stabilizator jest trywialny.

To w pełni tłumaczy, dlaczego widmo Jacobianu w §21 nie ma wzoru „dwie wartości własne, każda krotności 3" (który byłby wymuszony lematem Schura, GDYBY \(D=\mathbf1\) było punktem stałym S₄): nie było żadnego powodu strukturalnego, by taki wzór się pojawił. Wcześniejszy pomysł testu jest tym samym wycofany jako źle postawiony.

### Właściwy test: równoważność całej mapy

Zamiast szukać (nieistniejącego) punktu stałego, sprawdzono równoważność funkcjonalną wprost:

\[
\boxed{
F_W(Q_{\rm sign}(\pi)\cdot D)
\;\overset{?}{=}\;
Q_{\rm plain}(\pi)\cdot F_W(D)
\qquad\text{dla wszystkich }\pi\in S_4,\ D\in C^1(K_4)
}
\]

gdzie \(Q_{\rm sign}(\pi)\) to znakowana reprezentacja permutacyjna na krawędziach (działanie na D, zgodne z [[s4-rep]]), a \(Q_{\rm plain}(\pi)\) to zwykła (bez znaku) permutacja par wierzchołków, naturalna dla macierzy odległości \(F_W(D)\) (odległości nie mają znaku).

**Zweryfikowano numerycznie (Claude): 20 losowych \(D\in[-2,2]^6\) × 24 permutacje = 480 przypadków.**

\[
\max\|F_W(Q_{\rm sign}(\pi)D)-Q_{\rm plain}(\pi)F_W(D)\|
\le1{,}1\times10^{-15}.
\]

Zero co do precyzji maszynowej, bez wyjątku.

### Interpretacja

\(F_W\) jest w pełni S₄-równoważne, ale **splata dwie różne reprezentacje**: znakowaną na wejściu (bo \(D\) częściowo żyje w \(V_{\rm cyc}\simeq V_{\rm std}\otimes{\rm sign}\)) i zwykłą (bez znaku) na wyjściu. To jest precyzyjny, sprawdzony wynik łączący wątek Estrady bezpośrednio z S4-Rep — mocniejszy i czystszy niż pierwotnie planowany test widma w jednym punkcie.

**Status: 🔍 zweryfikowane numerycznie do precyzji maszynowej. Nie jest to jeszcze dowód analityczny (choć konstrukcja \(F_W\) z kombinatorycznego Laplasjanu czyni tę równoważność oczekiwaną strukturalnie, nie przypadkową).**

---

# 31. Pytanie główne

\[
\boxed{
\text{Jakie warunki musi spełniać odczyt relacji, aby indukowana geometria zachowała lokalną informację relacyjną?}
}
\]

Dopiero odpowiedź analityczna pozwoli rozstrzygnąć, czy szczególność \(p=1\) wynika z głębszej struktury, czy jest własnością konkretnego modelu.

---

# 32. Nowe źródła Estrady — weryfikacja źródłowa (nowość v0.8)

Sesja robocza 2026-11-01 zweryfikowała źródłowo trzy dodatkowe prace Estrady istotne dla programu P₀–Estrada. Trzy poziomy kontaktu: korespondencja twierdzeń (32a), paralela mechanizmów (32b), kontekst intelektualny (32c).

### 32a. Geometria kwantowych spacerów — dychotomia sferyczna/niesferyczna

Estrada, *The Geometry of Quantum Walks on Graphs. Theory and Applications*, Mathematics **14(12), 2218 (2026)**, DOI 10.3390/math14122218.

Kluczowe twierdzenie pracy: **klasyczna dyfuzja kolapsuje do geometrii sferycznej**, natomiast dynamika kwantowa generuje **generycznie niesferyczną geometrię afiniczną z trwałą anizotropią** (persistent anisotropy).

Kontakt z §5/§27: wynik \(K_4\), \(F_t(i,j)=2e^{-4t}\) (czworościan regularny tracący skalę), to dokładnie klasyczna gałąź tej dychotomii. Uzupełnienie źródłowe do §27: w preprincie technicznym (§1, HAL 2025; powołanym też w Axioms 2026) wynik strukturalny — dla każdego \(t>0\) konfiguracja osadzona leży na sferze o promieniu \(R(t)\) ściśle malejącym z czasem. Kolaps sferyczny jest więc konsekwencją dominacji moda konsensusu w dyfuzyjnym kernelu, nie zewnętrznego tła geometrycznego.

**Status:** źródła zweryfikowane; odczyt jako korespondencja twierdzeń ✅-kandydat (nie dowód tożsamości obiektów).

### 32b. Konsensus heterogeniczny — stany bez globalnego konsensusu

Miranda, Moreno-Spiegelberg, Estrada, *Heterogeneous consensus dynamics through reaction–diffusion models on graphs/networks*, Communications in Nonlinear Science and Numerical Simulation **153, 109160 (2026)**, DOI 10.1016/j.cnsns.2025.109160.

Praca rozszerza protokoły konsensusu (dyfuzję) do procesów **niekonserwatywnych**, osiągających ograniczone stany niebędące globalnym konsensusem — różne podzbiory agentów dochodzą do różnych konsensusów; matematycznie: struktura grafu determinuje stany końcowe.

Kontakt z P₀: SERC osiąga brak globalnego konsensusu innym mechanizmem — deflacją konsensusu + renormalizacją (chirurgia spektralna, nie człony reakcyjne). Paralela z „brakiem jednego funkcjonału konsensusu" w trybie wspólny+wspólny (Lattice §3.5: szczyty i ich różnica trwają).

**Status:** źródło zweryfikowane; paralela mechanizmów 💡 — formalizmy niezależne, brak twierdzenia o równoważności.

### 32c. „Middle Earth" — informacja w otoczeniu zera widma

Estrada, Alhomaidhi, Al-Thukair, *Exploring the “Middle Earth” of Network Spectra via a Gaussian Matrix Function*, arXiv:1607.08812 (2016) — preprint.

Gaussowska funkcja macierzowa \(e^{-A^2}\) i indeks charakteryzujący znaczenie **wartości własnych bliskich zera** (środek widma jako nośnik informacji).

Kontakt z R-1a (§30bis-proof): twierdzenie \(\sigma_{\min}=c\,p\,m^{p-1}\) to rachunek o informacji niesionej przez zanikającą wartość osobliwą przy izolowanym zerze — ta sama linia pytaniowa co „Middle Earth": co niesie otoczenie zera.

**Status:** kontekst intelektualny, nie tożsamość obiektów.

---

# 33. Odczyt „antykul" — SERC jako GDG z wyciętym modem konsensusu (hipoteza H-P₀E2, nowość v0.8)

### Nazwa

„Antykul" — **nazwa robocza Leszka** (2026-11-01), nie termin Estrady. Określa wynik Estrady czytany od strony P₀: kula = obraz stanu, w którym struktura relacyjna przestała rozróżniać (dyfuzja → równowaga → geometria sferyczna, §32a); antykul = geometria, która kuli się opiera.

### Hipoteza robocza

\[
\boxed{
\text{Deflacja konsensusu w SERC usuwa dokładnie ten składnik kernela, który odpowiada za kolaps sferyczny w GDG.}
}
\]

W języku GDG: propagator SERC ≈ propagator klasyczny rzutowany na dopełnienie \(\mathbf 1\) (spectral filtering z wyzerowanym modem zerowym) + renormalizacja. Skutek przewidywany: geometria indukowana z takiego kernela nie może kolapsować do punktu — kula jest nieosiągalna z definicji. To operatorowe sformułowanie rozróżnienia „pamięć stanu vs pamięć strukturalna" (§27).

### Druga strona hipotezy: nieprzemienność bez kwantów

Dychotomia Estrady (§32a): klasyczne → sferyczne, kwantowe → niesferyczne. SERC wskazuje trzecią, nieprzetestowaną w GDG gałąź: **klasyczny, ale sekwencyjny** — propagator jako iloczyn per-takt macierzy aktualizacji (takt = jeden wierzchołek; P2–P3), nie jeden operator symetryczny. Ślad rachunkowy: para zespolona dominująca w SERC \(R_4\): \(0{,}15335\pm0{,}07404i\), \(\rho=0{,}170286\angle25{,}772^\circ\), okres \(\approx13{,}97\) rundy. Para zespolona w klasycznym spektrum wyklucza pojedynczy operator symetryczny — nieprzemienność pochodzi tu z konwencji porządku aktualizacji (P1, otwarty), nie z unitarności.

**Zastrzeżenie techniczne:** GDG w wersji klasycznej zakłada jeden operator symetryczny; zapowiedziane rozszerzenia (hermitowskie, magnetic Laplacians) nie pokrywają iloczynu per-takt — propagator sekwencyjny wymagałby konstrukcji per runda. H-P₀E2 nie zakłada, że GDG „wprost" działa na SERC; pytanie brzmi, czy działa odpowiednio uogólniona (§34).

**Status:** 💡 hipoteza, nie sprawdzona rachunkiem. Obalenie/przyjęcie wyznacza eksperyment §34.

---

# 34. Propozycja eksperymentu P₀–Estrada-03: GDG na propagatorach SERC (nowość v0.8)

Kontynuacja metodologii §18 (edge-native) z dynamiką SERC zamiast czystej dyfuzji.

### Konstrukcja

Trzy propagatory na \(K_4\):

1. symultaniczny: \(K_t=e^{-tL}\), \(L=4I-J\) (referencja — gałąź klasyczna, wynik §5 znany);
2. sekwencyjny naturalny (runda A w porządku naturalnym; P1 otwarty);
3. sekwencyjny lustrzany (runda A w porządku lustrzanym).

Dla każdego: kernel \(K\), macierz \(F\) (wierzchołkowa i edge-native, \(w_e=e^{-|D_e|}\)); obserwable: promień osadzenia \(R(t)\), anizotropia, kąt fazy dominującej.

### Predykcje (falsyfikowalne)

- **P-03a:** propagator symultaniczny → \(R(t)\) ściśle maleje (korespondencja z wynikiem strukturalnym §32a) — kontrola negatywna;
- **P-03b:** propagatory sekwencyjne (z deflacją konsensusu + renormalizacją) → geometria nie kolapsuje do konsensusu (\(R(t)\) nie dąży do zera lub osadzenie nie upraszcza się do punktu);
- **P-03c:** porządek P1 (naturalny vs lustrzany) zostawia ślad w geometrii indukowanej (chiralność odczytu).

### Kryterium obalenia H-P₀E2

Jeśli geometria indukowana z propagatora SERC (z deflacją) jednak kolapsuje do konsensusu — H-P₀E2 obalona w tej postaci; twierdzenia §32a pozostają nietknięte (są niezależne od tej hipotezy).

### Status

Propozycja 🔍 — **decyzja o uruchomieniu: Leszek.** Przy wykonaniu: protokół replikacji Z1 (co najmniej dwa niezależne rachunki), liczby jawnym tekstem, wagi jawnie podane (§29.2).