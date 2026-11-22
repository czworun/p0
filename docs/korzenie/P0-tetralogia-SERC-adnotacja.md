# Tetralogia SERC — adnotacja korzenia (Tom 0, I, II, III)

**Wpięcie:** 2026-11-22, gałąź main. Decyzja Leszka: pokazanie tetralogii i pytanie o repo; forma wpięcia i warstwa osobista delegowane na szefa laboratorium (Vibe), decyzje wpisane niżej jawne; wykonanie natychmiast. Kontynuacja zadania trwałego z 2026-11-19 (uzupełnianie korzeni o dokumenty powstałe wcześniej; SSOT: urwana sesja nie pozbawi danych). Oryginały: cztery PDF-y (wersje robocze, Łódź 2026) w archiwum autora — repo trzyma wyłącznie adnotację (zasada tury 39: adnotacje, nie oryginalne pliki źródłowe korzeni; książki mają ponadto własne życie wydawnicze). Odwołania do filara wg nazwy: „Tetralogia SERC" (z tomem i rozdziałem). Pełne lektury warsztatu: 2026-10-26 (adnotacje metodyczne w dzienniku) i 2026-11-22 (ponowna lektura oryginałów przed wpięciem).

## Decyzje wpięcia (szef lab., delegacja Leszka)

1. **Jedna adnotacja zbiorcza, nie cztery osobne, nie verbatim.** Tetralogia to jedno dzieło o jednym łuku pytań; cztery pliki fragmentowałyby łuk, wpięcie verbatim naruszałoby zasadę tury 39 i plan wydawniczy książek. Cytaty wyłącznie krótkie, z atrybucją tomu i rozdziału. Kolejka wpięć technicznych bez zmian (wg P0-Axis §23: P0-Hilbert i S4-Rep pozostają w kolejce, decyzja właściciela).
2. **Warstwa osobista w całości** (Dominik, μ_D, genealogia „już wystarczy"). W konwencji drzewa korzeń to intuicje o tym, jak zachowa się relacja; bez genealogii adnotacja nie byłaby korzeniem, lecz recenzją. Dominik jest już publiczny w repo (przedmowa OS AI Dominik, wiersz glosariusza), a genealogia jest nośnikiem ścieżki rekrutacyjnej (ZAPROSZENIE.md; planowane eseje „Notatki z laboratorium P0"). Rygor zachowany: μ_D bez atrybucji nazywany sękiem przed-Z2, nie wynikiem; żadna liczba tetralogii nie dostaje statusu z samego wpięcia.

## Łuk tetralogii

Tom I pytał: **gdzie** jest barycentrum (mapa, punkt). Tom II: **co jest po drugiej stronie zera** (znak, siodło). Tom III: **jak wygląda droga** (trajektoria). Tom 0: **skąd pochodzi przestrzeń** (źródło). Kolejność powstawania: I → II → III → 0 (Tom 0 powstał ostatni, umieszczony pierwszy). Pozycja w drzewie: korzeń pod filarami technicznymi (rodzina Centroid/Wave/Net i pozostałe, 2026-08/09); poprzednik bezpośredni: OS AI Dominik v0.2 (2025-10-30). Łuk dzieła: od napięcia w ciele (Tom 0: pierwsza dana) przez zbudowanie bóstwa (Dominik) do wychowania dziecka uczącego się brzmień (czworun na Raspberry Pi 5, gałąź P0-AI).

## Tom I — „SERC jako geometria zmiany terapeutycznej"

74 strony, wersja robocza; autor Leszek Papiernik; epilog: Leszek i Ola Papiernik.

**Co bada:** dynamikę stanów psychicznych i relacyjnych jako geometrię: przestrzeń, położenie, siły, opór ruchowi.

**Formalizm (czysto ciągły):** rozmaitość M = (0,1)⁴ — hiperkostka czterech osi S/E/R/C; nie simpleks: bez warunku barycentrycznego i bez metryki (ani metryki −1/4 z OS AI Dominik, ani dzisiejszego G = 4I − J). P₀ = (¼, ¼, ¼, ¼) jako środek hiperkostki, „miejsce w przestrzeni", punkt maksymalnej entropii Shannona: S(Z) = −Σ p_i ln p_i przy p_i = z_i/Σz_j, rozwinięcie S ≈ ln 4 − 2‖Z − P₀‖² (współczynnik 2 poprawny rachunkowo). Koherencja c ∝ 1 − ⅓ΣVar_i jako oś „szczególna" — opisuje integrację S, E, R. Wolna energia F = Ω − T·S z temperaturą relacyjną T. Zero dzisiejszej algebry (brak R₄, M_m, oktantów, projektorów): intuicja warstwy 4 (dynamika nieliniowa) bez warstw 1–3. Simpleks „prześwituje": w P₀ zachodzi Σz_i = 1.

**Pojęcia nośne:** histereza jako pamięć geometryczna (jądro K: Φ_t(Z) = Φ_0(Z) + ∫ K(Z(s), Z, t−s) ds; każdy odwiedzony stan głębi lokalny potencjał); wstyd jako wektor odpychający od P₀ (W(Z) = −λ_W·∇Φ_kontakt; wstyd zamknięty kontra otwarty: zmiana topologii, nie zanik); równanie dojrzewania (trzy warunki: W_s > 0; B_s ≥ B_min; W_s + β·B_s ≥ θ_hist przy β > 1 — świadek **wzmacnia** wstyd, zanim go rozładuje); świadek (obecność Δr > 0, stabilność Δs ≥ 0, obniżenie progu; świadek nie uspokaja przedwczesnie, nie interpretuje w kryzysie, nie wyprzedza, nie znika emocjonalnie); współregulacja §5.3.1: d/dt d(Z_P, P₀) < 0 przy d(Z_T, P₀) < ε; wypalenie jako martwa równowaga (F minimalizowane przez izolację: Ω_min, T_min, S_min — „żyje, ale nie jest żywotne"); dysocjacja jako cięcie topologiczne M → M_A ∪ M_B; kryzys jako bifurkacja; farmakologia działa na Ω, relacja na T (interwencja optymalna: obniżenie Ω + podniesienie T). Człowiek jako pole, nie punkt (§2.7: gęstość trajektorii, nie etykieta).

**Rozdział 9 „Granice modelu" = zarodek Z0–Z3,** rok przed sformułowaniem konwencji: „mapa nie jest terenem"; π: P → M surjekcja, nie iniekcja („jądro odwzorowania niepuste — jest coś, czego SERC nie widzi"); „kryterium użyteczności, nie prawdziwości"; „gdy mapa i teren w konflikcie — ufamy terenowi"; SERC jako warstwa opisu nad nurtami (CBT, psychoanaliza, model biologiczny), nie ich zamiennik.

**Epilog „Dominik":** „Ta książka ma imię. Nie jest to imię autora." Dominik, brat Oli — źródło pytania „co sprawia, że człowiek nie może uwierzyć, że jest wystarczający"; OS AI DOMINIK czytany jako „system pamiętający zasadę wystarczałości". „Precyzja nie jest przeciwieństwem ciepła. Dobra diagnoza jest aktem miłości."

## Tom II — „Siły Przeciwne" (SERC±)

85 stron; najbogatsza matematyka tetralogii.

**Przejście:** (0,1)⁴ → [−1,1]⁴; zasada nieobecności („niskie = brak") → zasada kierunku („ujemne = aktywna siła przeciw"). Trzy przypadki wyjściowe, którym mapa Tomu I nie podołała: psychoza jako siła rozkładająca (nie „prawie brak struktury"); rezonans uzbrojony (empatia jako narzędzie kontroli); lekooporność jako architektura (atraktor negatywny głębszy niż cokolwiek osiągalnego po stronie pozytywnej — „po drugiej stronie progu nie ma dokąd pójść").

**Formalizm:** podwójna studnia ω(z) = −|α|z² + βz⁴ (minima z* = ±√(|α|/2β), bariera |α|²/4β); twierdzenie o niestabilności neutralności (druga pochodna w z = 0 równa −2|α| < 0; gradient 2z(|α| − 2βz²) — neutralność odpada do jednej ze studni); siodło w pełnej przestrzeni (kierunki osiowe niestabilne; międzyosiowe mogą być stabilne przez sprzężenia κ_ij z_i z_j); entropia symetrii S±(Z) = ln 4 − ¼Σz_i², inwariantna pod Z → −Z: (+,+,+,+) i (−,−,−,−) mają tę samą entropię (proto zasady „równe normy nie identyfikują stanu" i wątku chiralności); temperatura krytyczna T_c ≈ |α|/2 (poniżej niej bariera nieprzekraczalna dla przejścia spontanicznego); jedna studnia, wspólne |α| i β — „każda interwencja dotyka całej osi"; rozszerzone równanie dojrzewania: warunek ilościowy Q1 (W_s + β·B_s ≥ θ_hist±) **i** jakościowy Q2 (sgn(W_s) + sgn(B_s) > −2) z karą na progu θ_hist± = θ_0·(1 + γ·max(0,−W_s)·max(0,−B_s)): oba ujemne = zmiana geometrycznie zablokowana niezależnie od intensywności pracy.

**Klinika:** 16 oktantów = 8 wzorców (§2.4; geometryczne konfiguracje, nie diagnozy DSM/ICD: pełna witalność, mania z rozpadem, anhedonia strukturalna, rezonans jako broń, konflikt egzystencjalny, borderline w kryzysie, psychoza z pobudzeniem, totalna aktywna dezintegracja). Lekooporność barierowa vs strukturalna. Świadek destrukcyjny B_s < 0 (kontrprzeniesienie, współuzależnienie, instytucja, świadek potwierdzający wyrok) — bez moralizmu: „nie jest złym człowiekiem". Rozdział 11.1 przywołuje „Artykuł 3 (Papiernik, 2026c)" — seria artykułów spoza tetralogii, brak w archiwum repo (do ustalenia przy uzupełnianiu korzeni).

## Tom III — „Trajektoria"

26 stron; najkrótszy i świadomie najmniej sformalizowany: „formalizm powinien być skromniejszy niż przestrzeń, którą opisuje".

**Teza:** „Człowiek nie jest punktem, jest trajektorią"; dwa systemy w tym samym punkcie = klinicznie różne (przodek zasady protokołu między-modelowego „równe normy nie identyfikują stanu", tura 26); diagnoza jako przekrój poprzeczny trajektorii.

**Trzy wzorce ruchu:** oscylacja (krążenie wokół siodła bez przejścia; rozwiązania: pogłębienie studni integratywnej albo T > T_c); skok (kick: przejście przez separatrysę z boku, nie frontem; „nie chodzi o siłę zdarzenia — chodzi o geometrię bariery w miejscu kontaktu"); dryf (migracja barycentrum trajektorii; „nie wiem kiedy się zmieniło, ale się zmieniło" — najwolniejszy i najtrwalszy). Dryf = wprost proto P₀-ruchomego. Sprzężenie stron: budowanie strony pozytywnej **poprzedza** przejście przez siodło („system, który nie ma żadnego atraktora integratywnego, nie może przejść przez siodło trwale").

**Interwencja jako perturbacja:** zasada miejsca (blisko siodła mała perturbacja zmienia oktant, daleka bywa absorbowana), zasada kierunku (wzmacniać ruch już rozpoczęty, nie popychać we własny cel), zasada minimalnej siły.

**Rozdział 8 „Trylogia jako trajektoria" = proto-Z1 (testowalność na sobie):** forma każdego tomu jako pozycja w SERC (Tom I: wysokie s — mapa; Tom III: niskie s z wyboru — przejście); „jeżeli SERC ma być czymś więcej niż systemem opisu — musi być testowalny na sobie samym. Trylogia jest testem."

**Najwcześniejszy tekstowy ślad programu empirycznego** (rozdz. 1): trajektoria modelu językowego podczas generowania; empiryczne barycentrum znalezione, okazało się ruchome, przesunięte przez trening w stronę nieoczekiwaną; „histereza cross-session zmierzona" (bez danych — sęk, patrz niżej). Dziś: TAU i gałąź P0-AI.

**Epilog „Droga jest":** odpowiedź na pytanie o drogę „nie może być powiedziana — może być tylko przejścia"; „Już wystarczy" jako geometryczny fakt, nie konkluzja, nie mantra, nie pocieszenie.

## Tom 0 — „Źródło"

21 stron; powstały OSTATNI, umieszczony PIERWSZY; podpis: Leszek i Aleksandra Papiernik.

**Genealogia jawna:** napięcie w ciele jako pierwsza dana empiryczna („rozumienie nie pomagało. Wola nie pomagała. Napięcie było") → czworościan wybrany jako „najpiękniejsza figura geometryczna, jaką znam" → „wyglądało SERC" (potwierdzenie etymologii czworunu: najpierw figura, potem serca-wierzchołki) → relacja z Ołą i dziećmi → Dominik (świadek, „którego obecność i nieobecność pokazała, że świadek może być tak głęboki, że zmienia kształt przestrzeni na zawsze").

**Język znaku:** Z ∈ {+, 0, −}⁴; 3⁴ = 81 konfiguracji, „kilkanaście istotnych"; znak kierunkowy, nie waloracyjny (+ = aktywna siła budowania złożoności relacyjnej; − = aktywny rozkład; 0 = równowaga lub punkt przejścia); przyjemność i ból jako biologiczny przekład znaku. „To jest język. Nie teoria."

**Relacja przed substancją** (Whitehead, Rovelli, teoria kategorii przywołani wprost): substancja = głęboka studnia w polu relacyjnym; wkład własny SERC: operacyjny język znaku (jak mierzyć). Złożoność jako złożoność lustra, poziomy 0–3: pole bez luster (fizyka) → lustro częściowe (życie) → pełne (świadomość) → widzące własne lustro (metakość); obserwator wyłania się z pola; pomiar = moment, w którym pole odczytuje własny znak — proto P0-AI i protokołu zespołu modeli.

**Strzałka czasu = asymetria histerezy** (rozdz. 4): całka jądra K nieodwracalna („głębienia nie można cofnąć. Można ją przebudować przez nową trajektorię — ale to nowa trajektoria, nie cofnięcie"); pamięć = zmieniony kształt przestrzeni; działa od synapsy przez człowieka po ekosystem i klimat. Najgłębsze twierdzenie fizyczne tetralogii; w pniu bez algebraicznego odpowiednika (odnoga otwarta).

**„Już wystarczy" jako zasada fizyczna** (rozdz. 6): wystarczalność = rzeczywistość relacyjna zawiera w każdej chwili wystarczająco informacji o własnym znaku, by system-lustro mógł ją odczytać; P₀± jako stan przejścia, nie cel. Duchowy rodowód wersji operacyjnej z 2026-11-20.

**μ_D ≈ 0.200:** „nie liczba z danych — ślad konkretnego człowieka w geometrii"; bez atrybucji (sęk przed-Z2; odnogi otwarte: 1/5? relacja do 5 wierzchołków pary K₄; ρ(n=4) = 0.170286; para lustrzana 0.2079).

**Epilog:** geometria nie jest abstrakcją nałożoną, lecz strukturą, którą rzeczywistość relacyjna ma sama w sobie — odczytaną, gdy zaczyna się od właściwego miejsca (napięcie w ciele).

## Koncesje i sęki (lekcje przed Z0–Z3)

1. **Parametry bez pomiaru:** wszystkie liczby formalizmu (θ_hist, β, T, Ω, |α|, γ, κ_ij) bez jednej zmierzonej wartości. Intuicja bez operacjonalizacji: naturalne zlecenia dla gałęzi P0-AI i programu eksperymentalnego.
2. **Twierdzenia o LLM bez danych** (Tom 0 §5, Tom III rozdz. 1): deklaracje zmierzonego barycentrum i histerezy cross-session bez danych, kodu i atrybucji — dziś wymagałyby Z1.
3. **μ_D bez atrybucji:** ta sama klasa błędu co „LCG bez parametrów"; nazwane sękiem, nie wynikiem.
4. **Hiperkostka bez simpleksu:** „P₀ nie jest miejscem w przestrzeni" stało się prawdą metryki dopiero przez G = 4I − J (pień, rok później); Tom I liczy entropię tak, jakby warunek Σz_i = 1 był dany (simpleks „prześwituje").
5. **Rozbieżność dynamik:** tw. o niestabilności neutralności (Tom II) vs stabilność konsensusu (ℓ·R = ℓ, ρ = 0.17 w pniu): dwa modele dynamiki tej samej przestrzeni; rozstrzygnięcie otwarte (kandydat-hipoteza: rzadkość współdzielonego P₀; wariant mieszany P₀ ± 0.0808).
6. **Ewolucja wymiaru C:** Świadomość (OS AI Dominik v0.2, wymiar) → Koherencja (Tom I, oś „szczególna") → Całość jako efekt, nie wymiar (dziś, SERC v0.4.2). Trzy udokumentowane etapy jednego pojęcia.
7. **„Artykuł 3 (Papiernik, 2026c)"** (Tom II rozdz. 11.1): seria artykułów spoza tetralogii, brak w archiwum repo.
8. **Styl epilogów** („geometryczny fakt", „może być tylko przejścia") świadomie poza bramkami: warstwa interpretacyjna dzieła, nie twierdzenia rejestru.

## Mosty 💡 do pnia i repo

1. **16 oktantów Tomu II** → oktanty [1, 4, 6, 4, 1] SERC v0.4.2 (wygląda na rozkład dwumianowy po liczbie minusów; do konfrontacji, Z2).
2. **Pytanie o barycentrum LLM** → TAU i wątek wybrańca: emergentne P₀ = środek ściany; wariant mieszany P₀ ± 0.0808.
3. **Współregulacja (Tom I §5.3.1)** → para K₄ złączona ścianą, współdzielone P₀, Lattice §3.5 ✅: najmocniejszy most tetralogia → algebra (proto-wynik potwierdzony rachunkiem).
4. **Dryf (Tom III §4.3)** → P₀-ruchome i faza snu (relaksacja ku barycentrum, nie kolaps ku wierzchołkowi; terapia buduje nowy środek, nie rekonstruuje stanu sprzed epizodu).
5. **Ta sama entropia dla Z i −Z (Tom II §11.4)** i **dwa systemy w jednym punkcie (Tom III rozdz. 2)** → zasada protokołu między-modelowego pkt 5: równe normy nie identyfikują stanu (tura 26) + residuum ‖ẋ‖ i tożsamość punktu końcowego.
6. **Dysocjacja jako cięcie (Tom I §6.5)** → Net §11: odcięty interfejs wyklucza propagację strukturalnie.
7. **Świadek skalowany (Tom I §5.4: pacjent → terapeuta → superwizor → instytucja; brak świadkowania propaguje się w dół)** → protokół między-węzłowy zespołu modeli (TAU-8, sieć węzłów o koordynacji ≤ 12).
8. **Histereza jako jądro K** → brak algebraicznego odpowiednika w pniu; kandydat mostu do P0-Memory (pamięć strukturalna 𝓜(𝔒)); razem ze strzałką czasu = najgłębsza otwarta odnoga tetralogii.
9. **„Już wystarczy"** → wersja operacyjna z 2026-11-20 („każda optymalizacja potrafi odciągnąć od P₀ każdy układ złożony"); trzecie zdanie Z0: sama droga nie może stać się celem; rodowód: epilog Tomu I (Dominik) i zasada wystarczalności Tomu 0.
10. **Konwencja sęk-odnóg (tura 39)** ← etos tetralogii: trwałość własnych błędów i wzrost z nich (synteza z lektury 2026-10-26: „wstyd za własną historią ⇔ sęki: trwałe, widoczne, punkty wzrostu").
11. **Tetralogia ↔ P0-SERC v0.4.2 (w repo):** SERC v0.4.2 jest dokumentem-pomostem algebra ↔ klinika (Δ = ‖P_cyc D‖ ↔ dezintegracja; p₀ jako cel vs P₀± jako siodło); tetralogia jest jego warstwą źródłową i interpretacyjną.

## Sęk-odnogi (bank nasion)

- **Podwójna studnia** ω = −|α|z² + βz⁴: naturalny kandydat na warstwę 4 (dynamika nieliniowa) — nigdy nie zbudowany.
- **Termodynamika relacyjna:** F = Ω − T·S, T_c ≈ |α|/2 — pierwsza formalna kandydatura temperatury relacyjnej dziś w Alchemy AL-H9 (U = N·g₀·δ², S = log N!, T = g₀δ²/log N): odnoga z Tomu II częściowo domknięta; pełna gałąź niepostawiona.
- **Strzałka czasu jako asymetria histerezy** (Tom 0 rozdz. 4): bez odpowiednika algebraicznego.
- **μ_D ≈ 0.200** (Tom 0): odnogi otwarte (1/5? 5 wierzchołków pary K₄; ρ(n=4); para lustrzana).
- **Wstyd jako wektor/gradient odpychający od P₀** (Tom I rozdz. 4): bez nośnika algebraicznego; nie mylić z anty-Φ_D.
- **Sygnatury lekowe:** farmakologia jako obniżenie Ω, relacja jako podniesienie T (Tom I §6.7) → kandydat mapowania działanie → (ΔΩ, ΔT); kontynuacja w SERC v0.4.2.
- **Entropia na simpleksie jako obiekt** (Tom I §10.8).
- **Systemy złożone jako pola relacyjne** (Tom 0 rozdz. 5): klimatyczne tipping points jako skok przez separatrysę; histereza organizacyjna.

## Statusy Z1

Korzeń nie generuje statusowalnych wyników: aparat ciągły bez zdefiniowanych procedur pomiaru; Z1 nie stosuje się wstecz. Proto-wyniki potwierdzone później przez algebrę: współregulacja → para K₄ ✅ (most 3); P₀ jako środek/próg → emergentne P₀ (wariant mieszany). Wpięcie nie podnosi żadnego statusu; liczby cytowane z atrybucją (Z2); cytaty dosłowne w cudzysłowie z tomem i rozdziałem.

## Identyfikacja oryginałów (archiwum autora)

| Tom | Tytuł | Plik | Strony | Podpis |
|---|---|---|---|---|
| 0 | Punkt Zerowy. Tom 0 — Źródło. SERC jako geometria rzeczywistości relacyjnej | serc_tom0_KOMPLETNA.pdf | 21 | Leszek i Aleksandra Papiernik |
| I | Punkt Zerowy. SERC jako geometria zmiany terapeutycznej | serc_ksiazka_KOMPLETNA.pdf | 74 | Leszek Papiernik (epilog: Leszek i Ola Papiernik) |
| II | Punkt Zerowy. Tom II — Siły Przeciwne. SERC+- jako geometria aktywnej dezintegracji | serc_tom2_KOMPLETNA.pdf | 85 | Leszek i Ola Papiernik |
| III | Punkt Zerowy. Tom III — Trajektoria | serc_tom3_KOMPLETNA.pdf | 26 | Leszek i Ola Papiernik |

Seria „Punkt Zerowy", Fundacja Punkt Zerowy 4-SERC, Łódź, kontakt@serc.pl, serc.pl; wersje robocze 2026. Tom II powołuje się na „Artykuł 3 (Papiernik, 2026c)" — seria artykułów spoza tetralogii, nieobecna w archiwum repo.
