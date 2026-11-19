# Korzeń: P₀-Memory — adnotacja szefa lab. (v0.3.7, program 2026-09-07/08)

**Dokument:** „P₀-Memory: Struktura i Zmiana w Zapisie Obrazu" v0.3.7 (program badawczy; data w nagłówku 2026-09-07, dziennik zmian v0.3.7 zawiera weryfikację ORB-05-R datowaną 2026-09-08 — data nie zaktualizowana przy doklejaniu v0.3.7, zachowane verbatim). Deklarowana pozycja: **filar łączący serię P₀ — kandydat na dziesiąty filar** (dokłada znane pytanie o falującą liczbę filarów: „siedmiu/ośmiu" w Wave, kandydat 9 u Relacji, kandydat 10 tutaj — do skonfrontowania przy PILLARS-TABLE); nie modyfikuje matematyki istniejących filarów. Baza matematyczna: **P₀-Defect v0.5** (w repo nowszy v0.8, który wchłonął Flow §12A-G i Hilbert §12H — dokument bazuje na starszej wersji), P₀-Centroid v4.9.6, P₀-Hilbert/R3 v0.1 (rozliczony jako wchłonięty w Defect §12H). Własna konwencja statusów (Z2, jawna): ✅ dowiedzione / 📚 klasyczne / 🔍 numerycznie lub symbolicznie / 💡 program / ❌ sfalsyfikowane. Zasada redakcyjna §0 („żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia") — pre-echo Z0/Z3. Dokument przed-warsztatowy (replikacja Claude'a z 2026-09-08 zapisana w treści), wpięcie wg obowiązującego wzorca; formalna pozycja (filar vs gałąź programu zastosowań) — jak dla AI i Lattice, uregulowanie przy PILLARS-TABLE.

**Co bada:** rozdzielenie trzech poziomów pamięci w P₀: wartościowej (stan R, ✅), relacyjnej (Δ(R) = ‖P_cyc R‖, ✅) i strukturalnej 𝓜(𝔒) = {klasy trajektorii możliwych przy użyciu 𝔒}, od v0.3.5/0.3.6 sformalizowanej (monoid słów S(𝔒), ω-granica, relacja równoważności x ~_𝔒 y ⟺ ω_𝔒(x) = ω_𝔒(y)); pytanie centralne H-MEM-1: czy zanik stanu może zachodzić bez zaniku możliwości różnicowania przyszłej dynamiki. Trzy typy operatorów: 𝒜 wygaszający (R₄, K₁), ℬ ochronny (K₂, próg δ), 𝒟 detekujący (P_cyc) — z korektą v0.3.0, że nie muszą działać na jednej przestrzeni. Program zastosowań: obraz (M7: Δ ↔? krawędzie, priorytet najwyższy, „nie wolno jeszcze utożsamiać Δ=krawędzie"), film jako graf czasoprzestrzenny (𝓡(𝔒_space, 𝔒_time, Δ_t); „nie zakładamy K₄=obraz; K₄ pozostaje laboratorium lokalnym"), kolor (parametr 🔍 / wymiar grafu 💡), eksperyment P₀-Memory-01 (cztery klasy filmów). Zasady pomocnicze §0: rozdzielenie modelu od mostu (v0.3.0), separacja realizacji i struktury (v0.3.2.1), jawność parametrów dynamiki (v0.3.3: parametr zmieniający wynik o więcej niż rząd wielkości musi być jawny w specyfikacji), natywność przed konstrukcją (v0.3.4: kandydat bez mostu przed kandydatem z mostem, ocena na równych zasadach).

**Najmocniejsze (formalnie ✅ i numerycznie 🔍; wyniki liczbowe dwiema implementacjami):**
1. **Formalizm 𝓜(𝔒) (§2.3–2.3bis):** warunek dobrej określoności — wszystkie generatory jako odwzorowania jednej przestrzeni X; mieszany zbiór {M_m, T, P_cyc, K, …} z §1 nie jest dobrze określonym generatorem (M_m,T natywnie na ℝ⁴; K₁,K₂,P_cyc na C¹(K₄)≅ℝ⁶) — formalny powód zasady model↔most; monoid transformacji S(𝔒) przez homomorfizm z wolnego monoidu słów; orbita słaba (półgrupowa, istnieje zawsze, także dla kontrakcji) vs mocna (tylko dla bijekcji) z faktem ✅: R₄ i K₁ są kontrakcjami właściwymi, więc orbita mocna dla nich nie istnieje; exp(tK) z podalgebry rotacyjnej (Centroid §2.5) — jedyny dotąd zidentyfikowany w P₀ generator z orbitą mocną (wg §2.3bis). P-MEM-2 przeformułowane ✅ z definicji (część strukturalna była częściowo tautologią — dokument sam to nazywa; nietrywialność |𝓜(𝔒)|>1 wymaga dowodu per przypadek).
2. **|𝓜({R₄})| = 1 i M18 rozstrzygnięte negatywnie (§2.3bis, §10bis.6, ❌):** ω-granica R₄ to {p₀} dla (praktycznie) każdego x na V_ρ — faza spirali θ(k) jest własnością tranzjentu, a definicja 𝓜 poprzez ω-granicę jest na tranzjent ślepa z definicji. Rozstrzygnięcie zapisane jawnie jako odpowiedź negatywna, nie brak odpowiedzi — wzorzec rozstrzygania pytania przez precyzację wersji formalizmu; nowy problem M19 (czulsza definicja).

3. **M16/M16a (§8–8bis, 🔍; oryginał + niezależna replikacja Claude'a):** deterministyczna dynamika strukturalna zamiast szumu: rozbieżność 0,7–0,9% prób vs 12,8% przy szumie (σ=0,15) — efekt zachowany, ale o rząd wielkości słabszy; efekt generowany w początkowym oknie ~7 rund (niezależny od długości 7–120 kroków: po wygaszeniu R₄ nic już nie miesza). **Odkrycie czwartego, dotąd niejawnego parametru: tryb aktualizacji K₂ (wsadowy vs sekwencyjny Gauss-Seidel)** — replikacja Claude'a dała wartości 10–70× niższe niż v0.3.2.1; źródło zidentyfikowane i skwantyfikowane w pełnej macierzy 2×2 (most × tryb; 5 ziaren × 2000 prób na komórkę, kod zachowany): most A/wsadowe 0,71% ± 0,09; A/sekwencyjne 67,76% ± 1,19; B/wsadowe 7,53% ± 0,66; B/sekwencyjne 86,11% ± 0,45 (próby rozbieżne) — tryb K₂ jest determinantą 10–95×, silniejszą niż wybór mostu; dawne liczby v0.3.2.1 leżą w reżimie sekwencyjnym. Efekt nie znika w żadnej z 4 komórek — jedyne twierdzenie o niezależności od konstrukcji, które materiał naprawdę uzasadnia; konieczna trzecia, niezależna replikacja z jawnymi obiema osiami.
4. **ORB-05-R (§10ter, ✅ dla wyniku liczbowego po naprawie):** klasyfikacja pełnych trajektorii istotnie drobniejsza niż stanów końcowych — 425 klas trajektorii vs 209 klas końcowych (720 kolejności aktualizacji; max RMS ~0,19748 w największej klasie końcowej); znaleziony i naprawiony błąd implementacyjny (parametr order zapisywany jako etykieta, ale nigdy nie wpływający na obliczenia w m16_B_step — wszystkie 720 przebiegów identyczne, trywialna degeneracja do 1 klasy); obie liczby odtworzone dokładnie z poprawionego kodu (Claude 2026-09-08, to samo D₀, T=25, δ=0,3; klasyfikacja stabilna od 3 do 8 miejsc po przecinku); wniosek wprost: ten sam stan końcowy nie musi określać tej samej historii procesu. Konsekwencja programowa: warstwa III w dwóch wersjach, 𝓜_ω(𝔒) i 𝓜_traj(𝔒,T) — druga robocza, do kanonizacji (M20).
5. **M17 (§10bis, 🔍):** najprostsza hybryda K+R₄ odrzucona (‖[K,R₄]‖ = 0,103 — tego samego rzędu co wpisy K (0,06–0,19); K nie zachowuje płaszczyzny spiralnej R₄, residuum 0,081 — etykieta rotacyjna nie jest zachowywana przez kontrakcję); wskazany kandydat natywny: **faza widma R₄, λ₂,₃ = 0,1533 ± 0,0740i, |λ| = 0,1703, ±25,77° na rundę** — amplituda maleje geometrycznie (×0,1703/rundę), faza obraca się o stałą niezależnie od promienia; operacyjnie odczytywalna tylko w oknie ~7 rund — tym samym, które M16 zmierzył niezależnie; bez żadnego wyboru projektowego (most, tryb K₂).

**Koncesje i sęki (❌ i ograniczenia jawne):** ❌ M18 w wersji ω-granicznej (faza poza 𝓜); ❌ „defekt = krawędzie" (zamrożone; M7 dopiero priorytetem); ❌ wyjaśnienie v0.3.2.1 „inna definicja rozbieżności" (rzeczywisty mechanizm = tryb K₂, potwierdzony ilościowo); ❌ naiwna hybryda K+R₄ (nie komutują); P-MEM-2 częściowo tautologią (uznana przy formalizacji); błąd implementacyjny własny w ORB-05-R (parametr order nieużyty) — lekcja: w replikacji wykazać, że każdy parametr wykonuje pracę; niezgodność z historycznym ORB-04 (~18 klas) pozostaje osobnym, otwartym pytaniem (inny protokół referencji K₂, most B innej sesji); zamrożenie D^cyc w moście A = decyzja konstrukcyjna, nie konsekwencja P₀; odsetek rozbieżnych prób = dolne oszacowanie |𝓜| lokalnie (nie odróżnia „dwóch klas" od „wielu"); ARI = 1 dla wybranych par nie dowodzi niezależności od D₀; macierz M16a czeka na trzecią replikację; H-MEM-1 niepodniesione (💡/🔍). Jawnie oddzielone: wynik eksperymentalny vs interpretacja (§10ter), formalizacja vs nowy wynik (§8quater „reinterpretuje istniejące, bez nowych danych").

**Struktury 💡:** trzy poziomy obserwacji (stan końcowy ⊊ pełna trajektoria → kompresja do ω-granicy); realizacja reguły = wybór przestrzenny (most A/B) + wybór czasowy (tryb K₂) — jedno zagadnienie kanoniczności (M16b; propozycja R̃₄^can jako reprezentacja pochodna algebry 𝔤₄ „z góry", nie „z dołu"); 𝓜(𝔒) wrażliwe na każdy generator z osobna (tryb K₂ zmienia jeden generator vs most całe zanurzenie); amplituda/faza jako warstwy I/III wewnątrz jednej własności R₄; film = pamięć struktury + pamięć zmiany; gradient natywności kandydatów.

**Mosty 💡:**
1. **Faza 25,77° po raz CZWARTY w korpusie** (SERC R₄ ∠25,772°; Estrada T4 §36 wieczne muskanie; Flow — faza atraktora K₄; tutaj M17), z tą samą parą 0,1533±0,0740i i |λ| = 0,1703 ≈ ρ(n=4): pytanie, czy to identyfikator lokalny, czy stała uniwersalna, ma swój zapis także w tym korzeniu (indeks pytania: Estrada-03).
2. **Problem mostu = trzecie pojawienie rodziny architecture mismatch (Flow §3.2, AI §7.1, tu §6.1):** nie istnieje bezpośrednie, kanoniczne podstawienie R₄: C¹(K₄)→C¹(K₄), bo D = dx ∈ Im(d) i czysta dynamika wierzchołkowa nie generuje składowej cyklicznej — najsilniejsza, krzyżowo zweryfikowana negatywna struktura rodzinna; przy scaleniu pnia jedna pozycja atlasu.
3. **Oś sekwencyjny vs symultaniczny jako oś całego korpusu:** czwarty parametr K₂ tutaj (wsadowy/sekwencyjny, Gauss-Seidel), porządek P1 i rodzina symultaniczna DeepSeeka w Lattice (λ = 1−α·c(n), otwarte pytanie R_sym), konwencja per-wierzchołkowa notatnika Stalka — trzy konteksty, jeden temat: tryb aktualizacji jest parametrem pierwszorzędnym, nie detalem implementacji; spółbrzmienie z zasadą jawności Z2. Rodzina K₂ przez filary: próg δ u Defect (pytanie dokumentu: oryginalne K₂ z Defect z natury wsadowe czy sekwencyjne — zapowiedziane „do sprawdzenia w v0.5"; w repo Defect v0.8 — do rozstrzygnięcia w warsztacie), K₂ Alchemy (rozsunięcie do progu), ℬ ochronny tutaj.
4. **H-MEM-1 w zwierciadle warsztatu:** warstwa P₀ pary Lattice §3.5 (wspólny+wspólny: oba szczyty i ich różnica trwają przy skonsensusowanej ścianie — stan nie znika, dynamika różnicuje) to kandydat instancji zapisany w sęk-odnogach Lattice jako spółbrzmienie z M19/M20 i Flow §13; Memory dostarcza formalnych kryteriów, kiedy to będzie więcej niż analogia (|𝓜(𝔒)|>1 dla konkretnego, jawnego 𝔒).
5. **Zamrożenie jako kontrola:** D^cyc zamrożone w moście A = ten sam gest co zamrożenie w Flow §5.5.1 (T_inv) i konwencja zewnętrzna pomiaru TAU w Lattice (deflacja konsensusu co rundę) — porównywać dynamiki tylko przy jawnie określonym, co jest trzymane w miejscu; zasada jawności parametrów (v0.3.3) tu poprzedza czasowo protokół taktowy Lattice (pomieszanie długości rund jako błąd miary czasu).

**Sęk-odnogi (§17, z priorytetami):** M7 (Δ a krawędzie obrazu — najwyższy), M1 (formalny dowód H-MEM-1), M5 (eksperyment optyczny 🔍), M9 (Δ(λ)), M10 (K₄↔graf obrazu), M16b (kanoniczność mostu i trybu K₂ — z pytaniem o Defect v0.8), M17 (faza jako natywna warstwa III), M19 (czulsza niż ω-granica definicja; kandydat z §2.3ter: równoważność trajektorii z dokładnością do reparametryzacji), M20 (kanoniczna metryka/równoważność trajektorii, 4 kryteria), M2, M3 (most Net A↔B), M4, M6, M8; P₀-Memory-01 (klasy filmów A–D); zgodność ORB-04; trzecia niezależna replikacja macierzy M16a po ujawnieniu czwartego parametru.

**Statusy (mapa na Z1):** program przed-warsztatowy z jedną replikacją niezależną wewnątrz dokumentu (Claude 2026-09-08: macierz 2×2 w pełni odtwarzalna dla obu autorów; ORB-05-R 425/209 odtworzone z poprawionego kodu) — formalnie Z1 ≥ 2 dla wyników liczbowych podanych obiema rękami, ale dokument sam zaznacza, że H-MEM-1 wymaga replikacji spoza obu autorów, a próby interpretacyjne (🔍/💡) nie są dowodami; definicje formalne ✅ z definicji; M18 ❌ rozstrzygnięte; 𝓜_traj robocza. Pełny rejestr własnych błędów z pełnym mechanizmem każdego (czwarty parametr K₂, błąd parametru order, reżim sekwencyjny) — wzorzec protokołu uczciwości, powtórzony później przez Lattice.

**Uwagi redakcyjne (verbatim):** oryginał kończy się końcowym EOL (inaczej niż Wave, AI, Defect, Flow, Lattice — zachowane); data nagłówkowa 2026-09-07 wcześniejsza niż weryfikacja ORB-05-R z dnia 2026-09-08 w dzienniku zmian (data nie zaktualizowana — zachowane); dzienniki zmian v0.3.6/v0.3.7 częściowo dublują „Status korekty" i §19; notacja kaligraficzna 𝓜/𝔒/𝒜/ℬ/𝒟; bloki matematyczne LaTeX (otocznia $$ i nawiasy) zachowane; przecinek dziesiętny polski w wynikach liczbowych (0,71%–86,11%) i rozwinięciach λ (0,1533 ± 0,0740i); dziennik zmian po §19, poza głównym ciągiem numeracji.
P₀-Memory: Struktura i Zmiana w Zapisie Obrazu

Wersja: 0.3.7
Status: 🔍 Program badawczy — hipoteza o rozdzieleniu pamięci strukturalnej i pamięci stanu; wyniki M16/M16a/M16a-K2/M17 wymagają ostrożnej interpretacji i pełnej specyfikacji operatorów.
Status korekty: Korekta v0.3.6 — rozszerzono formalizm pamięci strukturalnej o rozdzielenie pamięci stanu, pamięci trajektorii i pamięci asymptotycznej; dodano ORB-05-R jako test pełnych orbit oraz jawnie zapisano problem reprodukowalności względem wcześniejszego ORB-04. — sformalizowano 𝓜(𝔒) (§2.3, nowe §2.3bis), które od v0.1 do v0.3.4 było zdefiniowane wyłącznie opisowo ("klasy trajektorii możliwych"). Dodano brakującą sekcję §2.3bis (orbita silna vs słaba), do której odwoływało się już §10bis.5 punkt 3, choć sekcja nigdy nie została napisana. Przeformułowano H-MEM-1 (§4) i P-MEM-2 (§2.3) w języku formalnym. Zastosowano formalizm do M16/M16a (nowe §8quater) i do M18 (nowe §10bis.6) — w obu przypadkach formalizacja daje konkretny, częściowo negatywny wynik, nie tylko przekład notacji. Nie zmienia żadnego wyniku numerycznego ani statusu M16/M16a/M17 jako takich.
Data: 2026-09-07
Baza matematyczna: P₀-Defect v0.5, P₀-Centroid v4.9.6, P₀-Hilbert/R3 v0.1
Pozycja: Filar łączący serię P₀ — kandydat na dziesiąty filar. Nie modyfikuje matematyki istniejących filarów.

---

0. Zasada redakcyjna

Żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia, którego dotyczy.

Statusy:

· ✅ Dowiedzione
· 📚 Klasyczne
· 🔍 Zweryfikowane numerycznie lub symbolicznie, bez dowodu ogólnego
· 💡 Przypuszczenie / program badawczy
· ❌ Sfalsyfikowane / odrzucone po weryfikacji

Zasada niezależności
P₀-Memory nie modyfikuje matematyki P₀-Centroid, P₀-Defect ani P₀-Hilbert/R3.
Jeżeli hipoteza H-MEM-1 zostanie obalona, upada proponowana interpretacja pamięci strukturalnej, ale nie wynika z tego obalenie: algebry 𝔤₄, metryki G₄, struktury V_cyc, twierdzeń P₀-Defect, wyników P₀-Centroid.

Zasada rozdzielenia modelu od mostu
W v0.3.0 wprowadzono dodatkowe rozróżnienie:

Istniejące operatory P₀ nie definiują automatycznie sposobu ich połączenia między różnymi przestrzeniami stanów.

W szczególności R₄ działa natywnie na przestrzeni wierzchołków x ∈ ℝ⁴, natomiast operator Defect K₁∘K₂ działa na przestrzeni krawędzi D ∈ C¹(K₄) ≅ ℝ⁶.
Most pomiędzy tymi przestrzeniami jest zatem dodatkową konstrukcją modelową, którą należy oznaczać jako 💡, dopóki nie zostanie uzasadniona jako kanoniczna.

Zasada separacji realizacji i struktury (v0.3.2.1)
M16a sugeruje rozróżnienie między strukturą reguły dynamicznej a sposobem jej realizacji na konkretnej przestrzeni stanów. Jeżeli ta sama jakościowa zależność między regułą a atraktorem występuje dla różnych realizacji mostu, wówczas efekt może być własnością reguły dynamicznej, a nie konkretnej reprezentacji operatora. Nie jest to jeszcze twierdzenie o niezmienniczości względem wszystkich realizacji.

Zasada jawności parametrów dynamiki (v0.3.3)
Analiza M16a-K2 (§8bis.3) pokazała, że konstrukcja eksperymentu M16/M16a ma czwarty, dotąd niejawny parametr — tryb aktualizacji reguły referencyjnej w K₂ (wsadowy vs sekwencyjny). Ten parametr zmienia wynik silniej niż wybór mostu. Zasada: każdy parametr, którego zmiana zmienia wynik o więcej niż rząd wielkości, musi być jawnie wymieniony w specyfikacji eksperymentu, a nie pozostawiony jako domyślne zachowanie implementacji.

Zasada natywności przed konstrukcją (nowa, v0.3.4)
M17 (§10bis) pokazuje, że zanim buduje się most między dwiema przestrzeniami (jak w M16/M16a), warto sprawdzić, czy poszukiwana własność nie jest już obecna wewnątrz jednej, natywnej struktury — bez potrzeby mostu w ogóle. Kandydat wymagający najmniej dodatkowych założeń modelowych ma pierwszeństwo przed kandydatem wymagającym mostu, dopóki oba nie zostaną ocenione na równych zasadach.

---

1. Motywacja: trzy poziomy informacji

Dotychczasowe filary P₀ ujawniają trzy różne poziomy:

I. Pamięć wartościowa – aktualny stan R.
II. Pamięć relacyjna – informacja o zgodności relacji:

Δ(R) = ‖P_cyc R‖.

III. Pamięć strukturalna – informacja o klasie zachowań możliwych dzięki określonej strukturze operatorowej:

𝓜(𝔒) = {klasy trajektorii możliwych przy użyciu 𝔒}.

Główne pytanie P₀-Memory brzmi:

Czy zanik pamięci wartościowej może zachodzić bez zaniku pamięci strukturalnej?

---

2. Trzy warstwy pamięci

2.1. Pamięć wartościowa — ✅
Dla R∈𝓡 pamięć wartościowa jest informacją o aktualnym stanie R.

2.2. Pamięć relacyjna — ✅
Dla P_cyc: C¹(K₄)→V_cyc definiujemy:

Δ(R) = ‖P_cyc R‖

oraz: R∈Im(d) ⟺ 𝒞(R)=0.

2.3. Pamięć strukturalna — formalizacja (v0.3.5)

**Warunek dobrej określoności (✅, wymóg formalny).** Definicja poniżej wymaga, aby wszystkie elementy 𝔒 były odwzorowaniami **tej samej** przestrzeni X w siebie: 𝔒⊆Map(X,X). W P₀ nie jest to spełnione automatycznie — M_m,T działają natywnie na X=ℝ⁴ (Centroid/Wave), natomiast K₁,K₂,P_cyc działają natywnie na X=C¹(K₄)≅ℝ⁶ (Defect/Alchemy). Zbiór 𝔒={M_m,T,P_cyc,K,…} zapisany w §1 **nie jest więc dobrze określonym generatorem** dopóki nie ustali się jednej wspólnej przestrzeni X i nie sprowadzi się każdego operatora do Map(X,X) — czyli dopóki nie wybierze się mostu (§6, §7, §8bis). To nie jest ograniczenie techniczne dodane na potrzeby formalizmu: to jest dokładny, formalny powód, dla którego „Zasada rozdzielenia modelu od mostu" (§0) musiała zostać wprowadzona już w v0.3.0 — bez niej §1 zapisuje wyrażenie, które nie ma matematycznego sensu.

**Definicja (monoid słów).** Niech X będzie ustaloną przestrzenią, 𝔒={o₁,…,o_k}⊆Map(X,X) skończonym zbiorem generatorów. Niech 𝔒* będzie wolnym monoidem nad alfabetem 𝔒 (skończone słowa, słowo puste ε↦id_X). Homomorfizm π:𝔒*→Map(X,X), π(o_{iₙ}⋯o_{i₁}) = o_{iₙ}∘⋯∘o_{i₁}, definiuje **monoid transformacji generowany przez 𝔒**: S(𝔒):=π(𝔒*)⊆Map(X,X).

**Definicja (orbita w sensie słabym, uzupełnia lukę §10bis.5).** Dla x∈X:
𝒪⁺_𝔒(x) := {w(x) : w∈S(𝔒)} = S(𝔒)·x ⊆ X.
Istnieje zawsze, niezależnie od odwracalności generatorów — w szczególności dla R₄, K₁, które są kontrakcjami i nie są bijekcjami X.

**Definicja (orbita w sensie mocnym, przypadek szczególny).** Jeśli każde oᵢ∈𝔒 jest bijekcją X, generują one podgrupę G(𝔒)≤Sym(X) (domkniętą też na odwrotności), a orbita mocna to 𝒪_𝔒(x):=G(𝔒)·x — zwykła orbita działania grupy. **Fakt (✅, natychmiastowy z definicji).** R₄, K₁ nie są bijekcjami na X (kontrakcje właściwe), więc dla 𝔒 zawierającego którykolwiek z nich orbita mocna **nie istnieje** — dostępna jest wyłącznie orbita słaba 𝒪⁺. To dokładnie odpowiada obserwacji z §10bis.5(3): „R₄ jako półgrupa dyssypatywna nie generuje [orbit w sensie mocnym]" — tutaj podane jako twierdzenie, nie intuicja. Generator rotacyjny K (Centroid §2.5, exp(tK) ortogonalne) jest odwracalny, więc {exp(tK)} generuje orbitę mocną — jest to jedyny dotąd zidentyfikowany w P₀ generator, dla którego orbita mocna istnieje.

**Definicja (klasa asymptotyczna / ω-granica).** Zakładamy, że X ma topologię (spełnione dla wszystkich instancji P₀: X⊆ℝⁿ). Dla x∈X:
ω_𝔒(x) := ⋂_{N≥0} cl( {w(x) : w∈𝔒*, |w|≥N} ).

**Definicja (𝓜(𝔒)).** Relacja x ~_𝔒 y ⟺ ω_𝔒(x)=ω_𝔒(y) jest równoważnością na X. Definiujemy:

$$\mathcal M(\mathfrak O) := X/\!\sim_{\mathfrak O}$$

— zbiór klas równoważności, równoważnie zbiór różnych granic asymptotycznych {ω_𝔒(x) : x∈X} osiąganych w X pod działaniem 𝔒. To jest formalny odpowiednik „klas trajektorii możliwych przy użyciu 𝔒" z v0.1–v0.3.4: klasa to maksymalny zbiór stanów początkowych dzielących ten sam los asymptotyczny pod dynamiką generowaną przez 𝔒.

**P-MEM-2, przeformułowane (✅ z definicji, nie hipoteza).** 𝓜(𝔒) zależy wyłącznie od pary (X,𝔒) — nie odwołuje się do żadnego wyróżnionego R₀. To, co pozostaje **nietrywialne i wymaga dowodu/weryfikacji dla każdego konkretnego 𝔒**, to nie sam fakt, że 𝓜(𝔒) jest strukturalne (to teraz definicyjne), lecz: (a) czy |𝓜(𝔒)|>1 dla danego 𝔒, (b) czy 𝓜(𝔒)≠𝓜(𝔒') dla dwóch różnych realizacji 𝔒,𝔒' tej samej reguły abstrakcyjnej. P-MEM-2 w dotychczasowym sformułowaniu było więc częściowo tautologią (część strukturalna) i częściowo przedwczesnym uogólnieniem (nietrywialność |𝓜|>1, która wymaga osobnego dowodu per przypadek — zob. §2.3bis).

---

2.3bis. Nietrywialność 𝓜(𝔒) nie jest darmowa — i czego to uczy o M17/M18

**Ostrzeżenie formalne.** Definicja w §2.3 poprzez ω-granicę jest *gruba*: rejestruje wyłącznie **dokąd** dąży trajektoria, nie **jak** tam dochodzi. To ma bezpośrednią konsekwencję dla pytania M18.

**Fakt (✅, natychmiastowy z definicji ω-granicy).** Dla 𝔒={R₄} samego w sobie, ω_{𝔒}(x)={p₀} dla (praktycznie) każdego x na V_ρ (zbieżność geometryczna R₄ᵏ(x)→p₀, ✅ już dowiedzione w Centroid). Zatem **|𝓜({R₄})|=1** — pojedyncza klasa.

**Wniosek dla M18 (częściowa odpowiedź, wcześniej niedostępna bez formalizmu).** Faza spirali θ(k) (§10bis.3) jest własnością *tranzjentu* (skończonego odcinka trajektorii przed osiągnięciem rozdzielczości numerycznej), nie własnością zbioru ω-granicznego — a 𝓜(𝔒) w powyższej definicji widzi wyłącznie ω-granicę. Formalny wniosek: **faza NIE jest elementem 𝓜({R₄}) w sensie §2.3** — nie dlatego, że została odrzucona empirycznie, lecz dlatego, że sama definicja 𝓜 poprzez ω-graniczność jest ślepa na informację tranzjentową z konstrukcji. To odpowiada na pytanie z §10bis.5(3) i M18 (§17) wprost negatywnie *dla tej konkretnej, ω-granicznej wersji 𝓜* — nie zamyka to jednak pytania o pamięć strukturalną w fazie w żadnym innym sensie.

**Co by było potrzebne, żeby faza jednak "liczyła się" do pamięci strukturalnej.** Trzeba by zastąpić ω-graniczną równoważność czymś czulszym na tranzjent — np. równoważnością dwóch trajektorii jako *tej samej krzywej z dokładnością do reparametryzacji czasu i skali* (uwzględniającą fazę, nie tylko punkt graniczny), albo osobną, nie-ω-graniczną definicją warstwy III wyłącznie dla generatorów zawierających podalgebrę rotacyjną (Centroid §2.5). Żadna z tych konstrukcji nie jest tu wykonana — to jest jawnie otwarty problem, nie luka do przemilczenia.

**Status całości.** Definicja 𝓜(𝔒) — ✅ (formalna, dobrze określona przy warunku jednej przestrzeni X). Nietrywialność |𝓜(𝔒)|>1 dla konkretnych 𝔒 z P₀ — otwarte, per przypadek (🔍/💡, zob. §8.8). Związek fazy R₄ z 𝓜 w sensie ω-granicznym — **❌ dla tej wersji formalizmu** (odpowiedź negatywna, nie brak odpowiedzi). Czy istnieje czulszy formalizm, dla którego odpowiedź byłaby inna — 💡, otwarte (nowy punkt M19, zob. §17).


2.3ter. Pamięć trajektorii — rozszerzenie po ORB-05-R

**Motywacja.** ORB-05-R pokazał, że klasyfikacja pełnej trajektorii może rozróżniać przebiegi, które mają ten sam lub bardzo podobny stan końcowy. To wskazuje, że pamięć asymptotyczna z §2.3 nie jest wystarczającym obserwablem, jeżeli pytaniem jest „jak system doszedł do stanu końcowego”.

Nie należy utożsamiać tego z dowodem ogólnej pamięci strukturalnej. Jest to motywacja do rozdzielenia dwóch obiektów.

**Definicja trajektorii skończonej.** Dla ustalonego generatora / słowa dynamiki i liczby kroków T definiujemy:

$$\Gamma_T(x;\mathfrak O)=\big(x_0,x_1,\ldots,x_T\big),\qquad x_0=x,$$

gdzie każdy $x_{t+1}$ powstaje przez zastosowanie jawnie określonego kroku dynamiki. Dla wersji relacyjnej można stosować projekcję:

$$\Gamma^{\rm cyc}_T(x;\mathfrak O)=\big(P_{\rm cyc}x_0,\ldots,P_{\rm cyc}x_T\big).$$

**Definicja relacji równoważności trajektorii — robocza.** Dla ustalonego $T$ i metryki $d_T$ można wprowadzić:

$$x\sim^{(T)}_{\rm traj}y\quad\Longleftrightarrow\quad d_T\!\left(\Gamma_T(x;\mathfrak O),\Gamma_T(y;\mathfrak O)\right)\le\varepsilon.$$

Przykładowo, dla ORB-05-R użyto odległości RMS pomiędzy odpowiednimi punktami pełnych trajektorii. Jest to **definicja robocza**, a nie kanoniczna definicja warstwy III. W szczególności wybór normy, długości T, tolerancji ε oraz sposobu parametryzacji czasu może zmieniać klasy.

**Rozdzielenie trzech poziomów obserwacji.** W wyniku ORB-05-R należy rozróżnić:

1. stan końcowy $x_T$ — obserwacja jednego punktu;
2. trajektorię skończoną $\Gamma_T$ — historia dojścia;
3. $\omega$-granicę $\omega_{\mathfrak O}(x)$ — informację asymptotyczną o losie trajektorii.

Formalnie:

$$x_T\quad\subsetneq\quad \Gamma_T\quad\text{(informacyjnie)}\qquad\text{oraz}\qquad \Gamma_T\longrightarrow\omega_{\mathfrak O}(x)\ \text{(kompresja do granicy)}.$$

Symbol $\subsetneq$ w powyższym zapisie ma charakter informacyjny, nie oznacza inkluzji zbiorów. Chodzi o to, że stan końcowy nie determinuje w ogólności całej historii.

**Wniosek metodologiczny.** Jeżeli pamięć strukturalna ma zachowywać informację o sposobie realizacji procesu, potrzebny jest obiekt czulszy od $\omega$-granicy. Naturalnym kandydatem jest klasa pełnych trajektorii, ale jej definicja musi być odporna na arbitralną parametryzację czasu i dobór metryki. To staje się częścią problemu M19.


---

3. Trzy typy operatorów

Operator | Rola | Przykład
𝒜 | dynamika wygaszająca | R₄, K₁
ℬ | dynamika ochronna | K₂, próg δ
𝒟 | detekcja | P_cyc

Istotna korekta v0.3.0: 𝒜, ℬ, 𝒟 nie muszą działać na tej samej przestrzeni. To właśnie ujawnił eksperyment M16.

---

4. H-MEM-1: pamięć strukturalna po wygaszeniu

**Sformułowanie opisowe (v0.1–v0.3.4).** 𝒜^k(R₀)→p₀ ⇏ 𝓜(𝔒)→∅ — zanik stanu ⇏ zanik przestrzeni możliwych przyszłych zachowań.

**Sformułowanie formalne (v0.3.5, w języku §2.3).** Niech 𝒜={A}⊊𝔒 (np. A=R₄), z |𝓜({A})|=1 (✅, klasa trywialna — zob. §2.3bis). H-MEM-1 twierdzi:

$$|\mathcal M(\mathfrak O)| > 1 \quad \text{dla pełnego } \mathfrak O \supseteq \{A\}\cup\mathcal B\cup\mathcal D,$$

tj. dołączenie operatora ochronnego ℬ (próg δ, K₂) i/lub detekcyjnego 𝒟 (P_cyc) do generatora zwiększa liczbę klas ω-granicznych ponad jedną, mimo że sama dynamika A ściąga każdy punkt do wspólnego p₀. To jest teraz zdanie o mocy zbioru {ω_𝔒(x) : x∈X} dla konkretnego, skończonego monoidu transformacji na konkretnej przestrzeni ℝⁿ — w zasadzie rozstrzygalne (dowodowo lub numerycznie, przez bezpośrednie sprawdzenie, czy ω_𝔒(x) przyjmuje ≥2 różne wartości dla próbki x), nie tylko przez proxy w postaci „% rozbieżnych prób" (§8.8 rozwija tę różnicę).

To pozostaje hipotezą 💡/🔍, ale zyskuje wsparcie eksperymentalne (M16, M16a, M16a-K2, M17) — formalizacja nie zmienia statusu, precyzuje tylko, co dokładnie miałoby zostać udowodnione, żeby status wzrósł do ✅.

---

5. Wyniki wspierające

Dotychczasowe wyniki Defect, Centroid, Alchemy i Hilbert/R3 pozostają bez zmian.
Żaden z tych wyników samodzielnie nie dowodzi jeszcze, że struktura operatorowa stanowi fizycznie istniejącą pamięć niezależną od stanu. Są one motywacją matematyczną dla H-MEM-1, a nie jej dowodem.

---

6. Problem mostu między Centroid i Defect

6.1. Problem architektoniczny — 🔍

R₄ z P₀-Centroid działa na x∈ℝ⁴. Defect działa na D∈C¹(K₄)≅ℝ⁶. Ponieważ D=dx jest z definicji elementem Im(d), czysta dynamika R₄ nie generuje samodzielnie składowej cyklicznej.

To oznacza, że nie można po prostu powiedzieć: „zastępujemy szum operatorem R₄". Nie istnieje bowiem bezpośrednie, kanoniczne podstawienie R₄: C¹(K₄)→C¹(K₄).

---

7. Konstrukcja M16 — most A (przez potencjał)

7.1. Most exact/cyclic — 💡

Rozkładamy: D_t = D_t^exact + D_t^cyc, gdzie D_t^exact∈Im(d), D_t^cyc∈V_cyc.

Minimalno-normowy reprezentant potencjału: x_t = d⁺D_t^exact.

Następnie: x_{t+1}=R₄(x_t), więc D_{t+1}^exact=d(x_{t+1}).

Składamy: D'_{t+1} = D_{t+1}^exact + D_t^cyc.

Składowa cykliczna jest w tej konstrukcji zamrożona. Na końcu stosowany jest K₂.

Status konstrukcji mostu: 💡. Nie jest ona jeszcze wynikiem P₀-Centroid ani P₀-Defect. Jest wyborem projektowym eksperymentu M16.

---

8. M16 — deterministyczna struktura zamiast szumu

8.1. Cel

Sprawdzić, czy efekt obserwowany wcześniej przy wymuszeniu szumowym pozostaje po zastąpieniu szumu deterministyczną dynamiką R₄. Istotne, ponieważ szum działa przez cały czas trwania symulacji, podczas gdy R₄ jest dynamiką wygaszającą.

8.2. Parametry

δ=1, D₀~N(0,2). 500–2000 prób, wiele ziaren, 6 krawędzi K₄. Reguła K₂ w tej sekcji: **wsadowa** (referencja liczona raz na rundę z pełnego zrzutu D_t — patrz §8bis.3 dla rozróżnienia).

8.3. Wynik

Wskaźnik | szum σ=0,15 | M16, most A, K₂ wsadowe
rozbieżne próby | 12,8% | 0,7–0,9%
rozbieżne krawędzie | 2,4% | 0,1–0,13%

Wynik jakościowy został zachowany: 𝔒_ref≠𝔒'_ref ⟹ możliwe różne atraktory dla tego samego D₀.
Efekt jest jednak około rząd wielkości słabszy niż w eksperymencie z szumem. Status: 🔍.

8.4. Czas trwania efektu

Przetestowano długości 7, 15, 30, 60, 120 kroków. Zaobserwowano tę samą stopę rozbieżności ≈0,90% dla wszystkich długości — rozbieżność powstaje w początkowym oknie dynamiki (R₄^k(x₀)→p₀ zanika geometrycznie w ~7 rundach; po wygaszeniu D^exact→0, dalsze rundy R₄ nic już nie mieszają).

Wniosek — 🔍: efekt M16 nie wynika z ciągłego wymuszania przez przypadkowy składnik. Jest generowany w krótkim oknie aktywności R₄, po czym dynamika stabilizuje się.

8.5. Mechanizm M16

D₀ → (D^exact, D^cyc) → R₄(D^exact) → K₂ → wybór atraktora, a następnie D^exact→0 ⟹ zanika mechanizm dalszego mieszania.

To odróżnia M16 od eksperymentu szumowego: szum → ciągłe wymuszanie; R₄ → wygasające okno dynamiki.

8.6. Co M16 rzeczywiście pokazuje?

· 🔍 Wynik 1: efekt różnicowania atraktorów może wystąpić również przy deterministycznej dynamice strukturalnej, nie tylko przy szumie.
· 🔍 Wynik 2: w badanej konstrukcji efekt pojawia się w pierwszych kilku rundach dynamiki.
· 🔍 Wynik 3: wydłużenie symulacji po wygaszeniu R₄ nie zwiększa obserwowanej rozbieżności.
· 💡 Hipoteza: krótki okres aktywnej dynamiki wygaszającej może być wystarczający do zapisania różnicy wynikającej ze struktury operatorowej.

M16 nie dowodzi jeszcze, że 𝓜(𝔒)≠𝓜(𝔒') w sensie ogólnej teorii klas trajektorii.

8.7. Najważniejsze ograniczenie M16 (pierwotne)

Zamrożenie D^cyc_t=D^cyc_0 jest decyzją konstrukcyjną, nie wynika automatycznie z P₀. M16 nie rozstrzyga jeszcze kanoniczności mostu — inny operator działający bezpośrednio na C¹(K₄) mógłby dać inną dynamikę (zob. most B, §8bis).

---

8bis. M16a: test alternatywnego mostu

8bis.1. Cel

Sprawdzić, czy efekt różnicowania atraktorów (M16) jest niezależny od konstrukcji mostu między R₄ a C¹(K₄).

8bis.2. Konstrukcje mostu

· Most A: przez potencjał (D → D^exact → d⁺ → R₄ → d → D').
· Most B: operator R̃₄ bezpośrednio na krawędziach (uśrednianie po sąsiadach w grafie liniowym L(K₄)).

Specyfikacja mostu B:
Dla każdej krawędzi e: M̃_e(D) = (D_e + Σ_{f∈N(e)} D_f) / (|N(e)|+1), gdzie N(e) to krawędzie sąsiadujące z e w L(K₄) (4 sąsiedzi — wszystkie krawędzie K₄ poza jedną, „przeciwną"/rozłączną).
Pełna runda: R̃₄ = M̃₂₃∘M̃₁₃∘M̃₁₂∘M̃₀₃∘M̃₀₂∘M̃₀₁.
Zweryfikowano: M̃_e(𝟙)=𝟙 ✅.

8bis.3. Odkryty czwarty parametr: tryb aktualizacji K₂ — 🔍

Pierwsza próba replikacji mostu A i B (Claude, niezależnie od kodu źródłowego wcześniejszej wersji tego dokumentu) dała wyniki 10–70× niższe niż zgłoszone w poprzedniej wersji (0.3.2.1). Zbadano źródło i zidentyfikowano nieujawniony parametr konstrukcji: sposób odczytu referencji 𝔒'_ref=sign(D_t) wewnątrz jednej rundy.

· **K₂ wsadowe**: referencja sign(D_t) liczona jest raz, z pełnego zrzutu D_t sprzed rundy; poprawka progowa stosowana jednocześnie do wszystkich 6 krawędzi.
· **K₂ sekwencyjne**: poprawka progowa stosowana krawędź po krawędzi (Gauss-Seidel); referencja dla krawędzi e odczytywana „na żywo" z już częściowo poprawionego wektora.

Różnica w wyniku (patrz §8bis.4) sięga 10–95×, czyli jest znacznie silniejsza niż różnica między mostem A i B. **Poprzednia wersja dokumentu (§8bis.0, wersja 0.3.2.1) błędnie przypisywała tę rozbieżność „innej definicji rozbieżności" — rzeczywistym mechanizmem jest tryb K₂, potwierdzony ilościowo poniżej.**

8bis.4. Wyniki — pełna macierz 2×2 (most × tryb K₂)

Protokół: δ=1, D₀~N(0,2), T=30 kroków, 5 ziaren × 2000 prób na komórkę (Claude, w pełni odtwarzalne, kod zachowany).

Wariant | rozbieżne próby | rozbieżne krawędzie
Most A, K₂ wsadowe | 0,71% ± 0,09 | 0,12% ± 0,02
Most A, K₂ sekwencyjne | 67,76% ± 1,19 | 17,64% ± 0,48
Most B, K₂ wsadowe | 7,53% ± 0,66 | 1,41% ± 0,13
Most B, K₂ sekwencyjne | 86,11% ± 0,45 | 33,36% ± 0,31

Dla porównania, wcześniej zgłoszone (wersja 0.3.2.1, bez jawnego trybu K₂): most A = 61,20%/16,03%; most B = 84,20%/32,70% — obie wartości leżą w reżimie sekwencyjnym i są z nim zgodne co do rzędu wielkości.

8bis.5. Wnioski

1. 🔍 Tryb K₂ (wsadowy vs sekwencyjny) jest **dominującym** czynnikiem siły efektu (10–95×), silniejszym niż wybór mostu.
2. 🔍 Wybór mostu (A vs B) jest czynnikiem **drugorzędnym**: silny w reżimie wsadowym (~10×, 0,71%→7,53%), ale niemal znika w reżimie sekwencyjnym (~1,3×, 67,76%→86,11%).
3. 🔍 Twierdzenie „efekt jest niezależny od mostu" jest znacznie lepiej uzasadnione jako stwierdzenie *warunkowe na tryb sekwencyjny* niż jako stwierdzenie ogólne — w trybie wsadowym wybór mostu sam w sobie daje rząd wielkości różnicy.
4. 💡 Efekt występuje we wszystkich czterech komórkach macierzy (nigdy nie spada do 0%), co jest jedynym twierdzeniem o niezależności od konstrukcji, które obecny materiał naprawdę uzasadnia.
5. Wynik wymaga niezależnej replikacji z udostępnioną specyfikacją obu osi (most × tryb K₂) — dopóki to nie nastąpi, nie można traktować go jako potwierdzenia H-MEM-1.

Status: 🔍 (wyniki numeryczne, w pełni odtwarzalne dla obu autorów po ujawnieniu czwartego parametru; interpretacja fizyczna pozostaje 💡).

---

8ter. Zasada separacji realizacji i struktury — 💡

M16a sugeruje rozróżnienie między strukturą reguły dynamicznej a sposobem jej realizacji na konkretnej przestrzeni stanów. §8bis.3 pokazuje, że „sposób realizacji" obejmuje nie tylko wybór mostu przestrzennego (A/B), ale też wybór trybu czasowego stosowania reguły (wsadowy/sekwencyjny) — oba są częścią tego samego problemu kanoniczności (M16b).

Formalnie: stan → realizacja dynamiki → struktura przyszłych trajektorii.

M16/M16a badają środkowe ogniwo. Zasada ta jest 💡 i stanowi ramę dla dalszych badań (M16b).

---

9. Co M16a rzeczywiście pokazuje?

· 🔍 Wynik 1: efekt różnicowania atraktorów występuje we wszystkich czterech zbadanych konstrukcjach (most A/B × K₂ wsadowe/sekwencyjne) — nigdy nie znika.
· 🔍 Wynik 2: siła efektu zależy silniej od trybu K₂ niż od wyboru mostu (§8bis.5).
· 💡 Hipoteza: istnieje naturalne rozróżnienie między „strukturą operatorową" a „sposobem jej realizacji" (przestrzennym i czasowym), które może być kluczem do znalezienia kanonicznego mostu.

M16a nie dowodzi jeszcze, że 𝓜(𝔒)≠𝓜(𝔒') w sensie ogólnej teorii klas trajektorii, ale dostarcza wstępnego wsparcia numerycznego, teraz z jawną kontrolą czwartego parametru.

---

8quater. Co formalizm §2.3 mówi o M16/M16a — i czego nie mówi

**Co „rozbieżne próby" naprawdę mierzy.** W języku §2.3, dwa bliskie warunki początkowe x,y (ten sam D₀, dwa niezależne uruchomienia z zaokrągleniem/różną kolejnością) uznane w M16/M16a za „rozbieżne", to empiryczny sygnał, że ω_𝔒(x)≠ω_𝔒(y) — czyli że lokalnie, w otoczeniu D₀, 𝔒 nie sprowadza wszystkiego do jednej klasy. Odsetek „rozbieżnych prób" jest więc **dolnym oszacowaniem** liczby klas |𝓜(𝔒)| ograniczonej do próbkowanego sąsiedztwa D₀ — nie jest pomiarem |𝓜(𝔒)| na całym X, i nie odróżnia „dwóch klas" od „bardzo wielu klas".

**Dlaczego most A ≠ most B strukturalnie, nie tylko ilościowo.** §2.3 wymaga jednej przestrzeni X. Most A i most B to dwa różne, konkretne zanurzenia ι_A, ι_B: (reguła abstrakcyjna) → Map(ℝ⁶,ℝ⁶) tej samej intencji „przenieś R₄ na krawędzie". Nie ma a priori żadnego powodu, dla którego S(ι_A(𝔒)) i S(ι_B(𝔒)) miałyby generować tę samą relację ~_𝔒 na ℝ⁶ — to są **różne monoidy transformacji** działające na tej samej przestrzeni, nie dwie reprezentacje jednego monoidu. Wynik §8bis.4 (efekt silniejszy dla mostu B niż A w trybie wsadowym) jest więc dokładnie tym, czego formalizm każe się spodziewać: 𝓜(ι_A(𝔒)) i 𝓜(ι_B(𝔒)) nie mają żadnego strukturalnego powodu, by się pokrywać, dopóki most nie zostanie wybrany kanonicznie (M16b). Formalizm nie rozwiązuje M16b — pokazuje precyzyjnie, na czym problem polega: kanoniczność mostu to pytanie, czy istnieje wyróżnione ι, dla którego 𝓜(ι(𝔒)) jest niezmiennicze względem klasy dopuszczalnych ι — pytanie o niezmienniczość samego 𝓜, nie tylko o zgodność liczb.

**To samo dla trybu K₂.** Tryb wsadowy i sekwencyjny K₂ to dwa różne elementy S(𝔒) (różne słowa — jedna aktualizacja „naraz" vs sześć aktualizacji Gauss-Seidel), nie dwie interpretacje jednego elementu. §8bis.5 (tryb K₂ silniejszy niż wybór mostu) mówi w tym języku: zmiana **jednego generatora** w 𝔒 (jak zdefiniowany jest krok K₂) zmienia 𝓜(𝔒) mocniej niż zmiana **całego zanurzenia** ι. To wzmacnia — teraz formalnie, nie tylko numerycznie — wniosek „zasady jawności parametrów dynamiki" (§0): 𝔒 musi być specyfikowane co do każdego generatora z osobna, bo 𝓜(𝔒) jest wrażliwe na każdy z nich niezależnie.

**Status.** Formalizm nie dodaje nowych wyników numerycznych do M16/M16a — reinterpretuje istniejące (§8.3, §8.6, §8bis.5) w sposób, który czyni pytanie o kanoniczność mostu (M16b) precyzyjnym pytaniem o niezmienniczość 𝓜, zamiast pytaniem o zgodność procentów.

---

10. Nowy problem: kanoniczność mostu (M16b)

M16b: poszukiwanie kanonicznego operatora na krawędziach oraz kanonicznego trybu aktualizacji K₂.

Cele — operator R̃₄^can: C¹(K₄)→C¹(K₄) oraz reguła K₂^can, które:

1. są naturalne z punktu widzenia algebry 𝔤₄,
2. zachowują rozkład exact/cyclic,
3. generują analogiczne okno aktywności,
4. dają wyniki porównywalne z mostami A i B w obu trybach K₂.

Propozycja: rozważyć R̃₄^can jako reprezentację pochodną (derivative representation) algebry 𝔤₄ na C¹(K₄) — działanie „z góry" (od algebry do przestrzeni krawędzi), a nie „z dołu" (od operatora uśredniającego). Dla trybu K₂ analogicznie: sprawdzić, czy istnieje wyróżniony tryb wynikający z tego, jak K₂ jest zdefiniowany w P₀-Defect (czy oryginalna definicja K₂ w Defect jest z natury wsadowa czy sekwencyjna — do sprawdzenia w v0.5).
Status: 💡 (program badawczy).

---

10bis. M17: faza spirali R₄ jako natywny kandydat na warstwę III — 🔍/💡 (nowość v0.3.4)

10bis.1. Motywacja

M16/M16a szukają pamięci strukturalnej przez konstrukcję mostu między R₄ a C¹(K₄). Zanim buduje się kolejny most, warto sprawdzić, czy P₀-Centroid samo w sobie (bez żadnego mostu do Defect) już zawiera obiekt o własnościach pamięci strukturalnej — coś, co przeżywa zanik amplitudy.

Naturalny kandydat: podalgebra rotacyjna 𝔰𝔬(3,ℝ) z Centroid §2.5, generator K=[ρ(M₀),ρ(M₁)], exp(tK) dokładnie ortogonalne (|λ|=1, bez zaniku) — w przeciwieństwie do R₄ (kontrakcja, |λ|<1).

10bis.2. Test komutacji K z dynamiką kontraktywną — 🔍

Sprawdzono numerycznie (reprezentacja 4×4, K i M_m ograniczone do V_ρ przez to, że oba fixują ⟨1⟩):

‖[K,M₀]‖=‖[K,M₁]‖=0,230, ‖[K,M₂]‖=‖[K,M₃]‖=0,117, ‖[K,R₄]‖=0,103

Wartości te są tego samego rzędu co same wpisy K (0,06–0,19) — niezaniedbywalne. Sprawdzono też, że K nie zachowuje płaszczyzny spiralnej R₄ (§10bis.3): residuum rzutu K na tę płaszczyznę wynosi 0,081 ≠ 0.

Wniosek — 🔍: K i R₄ **nie komutują**. Naiwna hybryda „R₄ zawęża amplitudę, exp(tK) zachowuje etykietę orbity niezależnie" nie jest matematycznie spójna — R₄ i K genuinie się mieszają, więc etykieta rotacyjna importowana z zewnątrz nie jest zachowywana przez kontrakcję.

10bis.3. Natywny kandydat: faza widma R₄ — 🔍

Zamiast doklejać K z zewnątrz, zbadano widmo samego R₄ na V_ρ:

λ₁ = 1 (kierunek ⟨1⟩, poza V_ρ)
λ₂,₃ = 0,1533 ± 0,0740i, |λ|=0,1703, faza = ±25,77°/rundę
λ₄ = 0,1347 (rzeczywista)

Para zespolona λ₂,₃ definiuje dwuwymiarową podprzestrzeń niezmienniczą R₄, na której dynamika jest **spiralą kurczącą się**: amplituda maleje geometrycznie (×0,1703/rundę), ale faza obraca się o stałe 25,77° na rundę — niezależnie od tego, jak mała jest już amplituda. Liczba 25,77° pokrywa się z wcześniej udokumentowaną fazą R₄ z P₀-Centroid.

10bis.4. Rozdzielenie amplituda/faza jako wersja warstw I/III — 💡

Proponowana reinterpretacja:

· **Amplituda** spirali (promień) ↔ pamięć wartościowa (warstwa I) — zanika geometrycznie, ✅ już dowiedzione w Centroid.
· **Faza** spirali (kąt) ↔ kandydat na pamięć strukturalną (warstwa III) — matematycznie nie zanika (obraca się o stałą wartość na rundę niezależnie od promienia), ale jest **operacyjnie odczytywalna tylko w tym samym oknie ~7 rund**, w którym amplituda pozostaje powyżej rozdzielczości numerycznej — to samo okno, które M16 zmierzyło niezależnie (§8.4).

To jest różnica jakościowa względem konstrukcji mostu (M16/M16a): nie wymaga żadnego dodatkowego wyboru projektowego (most, tryb K₂) — faza i amplituda to jedna, już dowiedziona własność R₄ samego w sobie.

10bis.5. Ograniczenia

1. 💡 To wciąż interpretacja, nie dowód, że faza „przechowuje informację" w jakimkolwiek fizycznie użytecznym sensie — na razie jest to obserwacja spektralna, nie mechanizm zapisu/odczytu.
2. 🔍 Faza jest matematycznie zdefiniowana tylko dopóki amplituda ≠ 0 dokładnie — w granicy k→∞ przestaje istnieć (nie ma spirali w punkcie). „Przeżywa zanik" oznacza więc: zanika wolniej/inaczej niż amplituda, a nie: nie zanika nigdy.
3. ❌/💡 Związek fazy z 𝓜(𝔒;R₀) w sensie ω-granicznym z §2.3 jest **rozstrzygnięty negatywnie** — zob. §10bis.6. Pytanie, czy istnieje inny, czulszy formalizm, dla którego związek by istniał, pozostaje 💡 otwarte.

Status całości M17: 🔍 dla części spektralnej (widmo, faza, brak komutacji), 💡 dla interpretacji jako warstwy III.

---

10bis.6. M18 rozstrzygnięte — dla ω-granicznej wersji 𝓜 (❌, v0.3.5)

To, do czego §10bis.5(3) się odwoływało jako do „§2.3bis (orbita w sensie słabym)", zostało w tej wersji napisane (§2.3bis) — i daje odpowiedź, nie tylko definicję.

**Wynik formalny.** |𝓜({R₄})|=1 (§2.3bis) — cała przestrzeń V_ρ to jedna klasa ω-graniczna, {p₀}. Faza θ(k) nie jest własnością ω_𝔒(x) dla żadnego x (ω-granica nie „pamięta" fazy, z definicji będącej granicą zbiorów domkniętych malejących do {p₀}). Zatem **w sensie §2.3, faza nie jest elementem 𝓜(𝔒)** — M18, zadane dokładnie w tej wersji formalizmu, ma odpowiedź NIE.

**Co to oznacza dla „natywności przed konstrukcją" (§0).** Nie unieważnia to obserwacji spektralnej §10bis.2–10bis.3 (widmo, faza, brak komutacji [K,R₄] — te wyniki 🔍 stoją bez zmian) ani idei, że faza mogłaby pełnić rolę pamięci strukturalnej w jakimś sensie. Unieważnia tylko najprostszy sposób sprawdzenia tego pomysłu (podstawienie fazy do gotowej definicji §2.3). Faza pozostaje najciekawszym natywnym kandydatem na warstwę III — ale wymaga **innej** definicji 𝓜 niż ω-graniczna, nie potwierdzenia w tej, którą tu sformalizowano.

**Nowy problem — M19.** Skonstruować definicję pamięci strukturalnej czulszą na tranzjent niż ω-granica (np. równoważność trajektorii z dokładnością do reparametryzacji, lub konstrukcja specyficzna dla podalgebry rotacyjnej 𝔰𝔬(3,ℝ), gdzie orbity mocne istnieją — §2.3bis), dla której faza R₄ mogłaby być nietrywialnym niezmiennikiem. Status: 💡, nowy priorytet §17.


10ter. ORB-05-R — pełna trajektoria zamiast samego stanu końcowego

**Status:** ✅ zweryfikowane (v0.3.7 — błąd implementacyjny znaleziony i naprawiony, obie liczby odtworzone niezależnie) / 💡 program dalszego formalizowania interpretacji.

**Cel.** Sprawdzić, czy klasyfikacja pełnych trajektorii zawiera informację, której nie widać w samym stanie końcowym.

**Protokół.** Dla $K_4$ i $6!=720$ kolejności aktualizacji zapisywana jest trajektoria

$$D_\pi(0),D_\pi(1),\ldots,D_\pi(T),$$

a następnie jej część cykliczna

$$P_{\rm cyc}D_\pi(t).$$

Klasyfikację można wykonywać dwiema metodami:

· dokładna / numeryczna: identyczność po ustalonym zaokrągleniu;
· metryczna: grupowanie według odległości RMS pełnych trajektorii.

**Najważniejszy wynik.** W reprodukowalnej implementacji ORB-05-R stwierdzono, że klasyfikacja pełnych trajektorii może być znacznie drobniejsza niż klasyfikacja stanów końcowych. W jednym badanym przebiegu raportowano 425 klas pełnych trajektorii wobec 209 klas stanów końcowych przy klasyfikacji zaokrągleniowej. Dla największej klasy końcowej odnotowano różne trajektorie o maksymalnym RMS około 0,19748.

**Poprawka i pełna niezależna weryfikacja (Claude, 2026-09-08).** Przesłany plik implementujący ORB-05-R miał błąd: parametr `order` był zapisywany jako etykieta, ale **nigdy nie wpływał na obliczenia** — `m16_B_step` zawsze iterował po krawędziach w stałej kolejności 0..5. Skutek: wszystkie 720 przebiegów było identyczne, dając trywialnie 1 klasę — dokładnie ten degenerat opisany niżej w „Kluczowej kontroli reprodukowalności". Liczby 425/209 nie mogły więc pochodzić z uruchomienia tego konkretnego pliku.

Naprawiono (parametr `order` faktycznie steruje kolejnością Gaussa-Seidla) i uruchomiono ponownie na tym samym \(D_0\), T=25, δ=0,3:

- **final_cyclic_class_count = 209** — zgodne dokładnie z liczbą cytowaną powyżej.
- **dokładna klasyfikacja całej trajektorii** (zaokrąglona sygnatura, stabilna od 3 do 8 miejsc po przecinku) **= 425** — zgodne dokładnie z drugą liczbą.

Obie liczby „najważniejszego wyniku" są więc teraz w pełni odtworzone z poprawionego, działającego kodu, nie tylko przytoczone z nieodtwarzalnego źródła. Poprawiony plik: `p0_universe_v0_1_9_ORB05_fixed.py`.

**Interpretacja.** Wynik wspiera zdanie:

$$\boxed{\text{ten sam stan końcowy nie musi określać tej samej historii procesu}}.$$

Nie wynika z niego jeszcze, że istnieje kanoniczna „pamięć strukturalna” niezależna od wszystkich szczegółów implementacji. Wynik dotyczy konkretnego operatora, protokołu i metody porównania.

**Test względem $D_0$.** Wariant eksperymentalny z wieloma stanami początkowymi wskazał, że liczba klas trajektorii pozostaje wieloklasowa, ale nie ustanawia to jeszcze niezmienniczości klas względem $D_0$. W szczególności zgodność partycji dla wybranych par może być pełna (ARI=1), lecz nie jest to dowód ogólnej niezależności od stanu.

**Kluczowa kontrola reprodukowalności (rozstrzygnięta w v0.3.7).** Wcześniej: „ORB-05-R uruchomiony na aktualnej, jawnie zapisanej implementacji operatora nie odtworzył historycznego wyniku ORB-04 z około 18 klasami... wszystkie 720 przebiegów mogą zdegenerować się do tej samej trajektorii." **Przyczyna znaleziona**: błąd implementacyjny (parametr `order` nieużywany), nie różnica protokołu. Po naprawie ORB-05-R odtwarza własne cytowane liczby (425/209) dokładnie — pytanie o zgodność z historycznym ORB-04 (~18 klas, most B z wcześniejszej sesji, inny protokół referencji K₂) pozostaje osobne i wciąż otwarte, ale przestało być zaciemnione błędem w kodzie.

**Konsekwencja dla dokumentu.** Nie używać wyniku ORB-05-R jako bezpośredniego dowodu H-MEM-1. Jego właściwa rola to uzasadnienie, dlaczego warstwę III należy badać co najmniej w dwóch wersjach:

$$\mathcal M_\omega(\mathfrak O)\qquad\text{i}\qquad\mathcal M_{\rm traj}(\mathfrak O,T),$$

gdzie druga pozostaje konstrukcją roboczą do dalszej kanonizacji.

**Nowy problem M20.** Znaleźć metrykę / relację równoważności trajektorii, która:

1. nie zależy sztucznie od jednostki czasu;
2. rozróżnia istotną strukturę procesu od czysto numerycznych różnic;
3. ma sens dla trajektorii o różnej długości;
4. daje się porównać z $\mathcal M_\omega$ i z niezmiennikami P₀-Defect.

Status M20: 💡.


---

11. Pamięć strukturalna a film

Silniejsza i bezpieczniejsza hipoteza: struktura operatorowa + zmienny ślad relacyjny → rekonstrukcja stanu.

Dla filmu: I(x,y,t) = 𝓡(𝔒_space, 𝔒_time, Δ_t).

Stąd: Film = pamięć struktury + pamięć zmiany. Nadal hipoteza programowa (💡).

---

12. Najważniejszy test obrazu — M7

Priorytet M7 pozostaje bez zmian: Δ ↔? krawędzie/kontury obrazu.
Nie wolno jeszcze utożsamiać Δ=krawędzie. Najpierw trzeba sprawdzić, jak D→P_cyc D zachowuje informację przestrzenną na rzeczywistym grafie obrazu.

---

13. Film jako graf czasoprzestrzenny

Dla I(x,y,t): G_xyt=(V,E), z E=E_local∪E_temporal. Nie zakładamy K₄=obraz. K₄ pozostaje laboratorium lokalnym.

---

14. Kolor

Kolor jako parametr — 🔍: z_e(λ)=ρ_{e,λ}e^{iφ_{e,λ}}, Δ(λ)=‖P_cyc z(λ)‖.
Kolor jako wymiar grafu — 💡: G_xytλ jest dodatkową hipotezą i nie wynika automatycznie z Hilbert/R3.

---

15. Eksperyment P₀-Memory-01

Cztery klasy filmów: A — statyczny obraz, B — jeden ruchomy obiekt, C — zmienne oświetlenie, D — losowe klatki.
Mierzymy Δ_t oraz |Δ_{t+1}-Δ_t|/|Δ_t|. Hipoteza: A,B,C → mała zmienność struktury; D → duża zmienność. Status: 💡.

---

16. Status po v0.3.5

Element | Status
Pamięć wartościowa | ✅
Pamięć relacyjna | ✅
Pamięć strukturalna | 💡 (definicja asymptotyczna ✅ od v0.3.5; pamięć trajektorii — nowy formalizm roboczy 💡)
Definicja formalna 𝓜(𝔒) (ω-graniczna) | ✅ (§2.3, wymaga jednej przestrzeni X)
Orbita słaba vs mocna | ✅ (§2.3bis; mocna istnieje tylko dla generatorów odwracalnych, np. K)
P-MEM-2 | ✅ (część strukturalna, teraz z definicji) — nietrywialność per 𝔒 pozostaje 💡/🔍
H-MEM-1 | 💡 → 🔍 (sformułowanie formalne §4; wymaga replikacji)
Defekt jako trwały ślad | ✅
Algebra 𝔤₄ | ✅
M16: deterministyczny efekt strukturalny (most A) | 🔍
M16a: most B, macierz 2×2 most×tryb K₂ | 🔍
M16a-K2: identyfikacja trybu K₂ jako czwartego parametru | 🔍
M17: brak komutacji [K,R₄] | 🔍
M17: faza spirali R₄ jako kandydat warstwy III | 🔍 (widmo) / 💡 (interpretacja)
M18: związek fazy z 𝓜(𝔒) w sensie ω-granicznym | ❌ rozstrzygnięte negatywnie (§10bis.6) — faza nie jest elementem 𝓜 w tej definicji
Konstrukcja exact/cyclic (most A) | 💡
Zamrożenie D^cyc | 💡
Alternatywny most B (krawędziowy) | 💡
Tryb K₂ (wsadowy/sekwencyjny) | 💡 (jako wybór), 🔍 (jako zmierzony efekt)
Kanoniczność mostu i trybu K₂ (M16b) | 💡
Defekt = krawędzie | ❌
M7 — defekt a krawędzie | 💡 priorytet
Kolor jako parametr | 🔍
Kolor jako wymiar grafu | 💡
P₀-Memory-01 | 💡

---

17. Zaktualizowane problemy badawcze

Problem | Status | Priorytet
M1 — formalny dowód H-MEM-1 | 💡 | Wysoki
M2 — metryka na 𝓜(𝔒) | 💡 | Średni
M3 — most Net A↔B | 💡 | Średni
M4 — termodynamika pamięci | 💡 | Niski
M5 — eksperyment optyczny | 🔍 | Wysoki
M6 — niezmienniczość topologiczna | 💡 | Średni
M7 — Δ a krawędzie obrazu | 💡 | Najwyższy
M8 — relacje temporalne | 💡 | Średni
M9 — Δ(λ) | 💡 | Wysoki
M10 — K₄↔graf obrazu | 💡 | Wysoki
M16 — deterministyczny most R₄→C¹ (most A) | 🔍/💡 | Wysoki
M16a — alternatywny most bez x (most B) + macierz 2×2 | 🔍 | Wysoki
M16b — kanoniczność mostu i trybu K₂ | 💡 | Wysoki
M17 — faza spirali R₄ jako natywna warstwa III; związek z K niekomutujące | 🔍/💡 | Wysoki
M18 — czy faza spirali ma jakikolwiek związek z 𝓜(𝔒;R₀) w sensie ω-granicznym? | ❌ rozstrzygnięte (§10bis.6) | — (zamknięte)
M19 — czulsza definicja pamięci strukturalnej (nie ω-graniczna), dla której faza mogłaby być niezmiennikiem | 💡 | Wysoki (nowy, po M18)
M20 — kanoniczna metryka/równoważność pełnych trajektorii po ORB-05-R | 💡 | Wysoki

---

18. Nowy stan tezy głównej

Najbezpieczniejsze sformułowanie: zanik stanu nie musi oznaczać zaniku różnicowania przyszłej dynamiki.

Ostrożniej: różne reguły strukturalne (most × tryb K₂) mogą prowadzić do różnych atraktorów przy tym samym R₀ — i robią to we wszystkich czterech zbadanych kombinacjach, choć z siłą różniącą się o dwa rzędy wielkości.

M17 dodaje trzecią, niezależną linię wsparcia: sama algebra 𝔤₄, bez żadnego mostu do Defect, już zawiera rozkład na część zanikającą (amplituda) i część, która w danym oknie czasowym niesie dodatkową informację niezależną od amplitudy (faza) — choć K sam w sobie nie jest tym mechanizmem (nie komutuje z R₄).

Formalnie (v0.3.5): takie reguły/struktury są różnymi elementami 𝓜(𝔒) dokładnie wtedy, gdy indukują różną relację ~_𝔒 — §2.3, zastosowane do M16/M16a w §8quater.

---

19. Wniosek v0.3.5

1. Efekt różnicowania atraktorów (M16/M16a) nie jest artefaktem jednej konkretnej konstrukcji — występuje we wszystkich 4 kombinacjach most×tryb K₂ (wymaga jednak niezależnej replikacji poza obecnymi dwoma autorami).
2. Odkryto i skwantyfikowano czwarty, dotąd niejawny parametr konstrukcji (tryb K₂), silniejszy determinant wyniku niż wybór mostu.
3. M17: sprawdzono i odrzucono najprostszą hipotezę o hybrydzie K+R₄ (nie komutują) — ale znaleziono lepszego, natywnego kandydata na warstwę III: fazę spirali własnej R₄, bez potrzeby konstruowania mostu.
4. Zasada „natywność przed konstrukcją" (§0): przed dalszą rozbudową mostów (M16b) warto systematycznie sprawdzić, czy Centroid lub Defect osobno już zawierają kandydatów na pamięć strukturalną, zanim zakłada się, że trzeba je sztucznie łączyć.
5. **(v0.3.5)** 𝓜(𝔒) ma teraz definicję formalną (§2.3, ω-graniczna, wymaga jednej wspólnej przestrzeni X). P-MEM-2 (strukturalność) jest jej natychmiastową konsekwencją, nie osobną hipotezą. Zastosowana do M18, definicja daje odpowiedź **negatywną**: faza R₄ nie jest elementem 𝓜 w tym sensie (§10bis.6) — nie dlatego, że pomysł był zły, lecz dlatego, że ω-granica z definicji nie widzi tranzjentu. Zastosowana do M16/M16a (§8quater), definicja pokazuje, że rozbieżność mostu A/B i trybu K₂ jest dokładnie tym, czego należy oczekiwać, gdy dwa różne zanurzenia generują różne monoidy transformacji na tej samej przestrzeni — co czyni M16b pytaniem o niezmienniczość 𝓜 względem wyboru zanurzenia, nie tylko o zgodność liczb.

Kolejne pytania: czy istnieje czulsza (nie-ω-graniczna) definicja pamięci strukturalnej, dla której faza R₄ byłaby niezmiennikiem (M19)? Czy istnieje w samej algebrze 𝔤₄ lub w oryginalnej definicji K₂ w P₀-Defect coś, co rozstrzyga między trybem wsadowym a sekwencyjnym, tj. wyróżnia kanoniczne zanurzenie ι w sensie §8quater (M16b)?

---

P₀-Memory v0.3.6. Sformalizowano 𝓜(𝔒) (§2.3: monoid słów, orbita słaba/mocna w nowym §2.3bis, klasa ω-graniczna) — domykając lukę odziedziczoną od v0.1, gdzie §10bis.5 odwoływało się do sekcji „§2.3bis", która nigdy nie została napisana. P-MEM-2 przeszło z hipotezy do konsekwencji definicji. H-MEM-1 przeformułowane formalnie (§4). Formalizm zastosowany do M16/M16a (§8quater — bez nowych danych numerycznych, reinterpretacja istniejących) i do M18 (§10bis.6 — wynik negatywny, faza nie jest elementem 𝓜 w sensie ω-granicznym; nowy problem M19). Dokument nie modyfikuje matematyki istniejących filarów; formalizacja nie zmienia żadnego wyniku numerycznego z v0.3.4.


---

### Dziennik zmian v0.3.7
1. Znaleziono i naprawiono błąd implementacyjny w ORB-05-R (parametr `order` nieużywany w `m16_B_step`) — poprzednio zgłoszona degeneracja do 1 klasy była artefaktem tego błędu, nie wynikiem.
2. Obie liczby „najważniejszego wyniku" §10ter (425 klas trajektorii, 209 klas stanów końcowych) zweryfikowane niezależnie i odtworzone dokładnie z poprawionego kodu.
3. Status §10ter podniesiony z 🔍 do ✅ dla samego wyniku liczbowego; interpretacja (H-MEM-1) pozostaje 💡.

### Dziennik zmian v0.3.6

1. Dodano rozdzielenie: stan końcowy / pełna trajektoria / ω-granica (§2.3ter).
2. Dodano ORB-05-R jako osobną sekcję 10ter, z rozróżnieniem wyniku eksperymentalnego od interpretacji.
3. Zapisano problem reprodukowalności: obecna implementacja ORB-05-R nie może być bez dodatkowej specyfikacji utożsamiana z historycznym ORB-04.
4. Dodano M20 dotyczące kanonicznej metryki/równoważności trajektorii.
5. Nie podniesiono statusu H-MEM-1: pozostaje hipotezą wymagającą testów niezależnych od konkretnej implementacji.
