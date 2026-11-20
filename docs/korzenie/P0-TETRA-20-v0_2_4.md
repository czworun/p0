
# Korzeń: P₀-TETRA-20 — adnotacja szefa lab. (v0.2.4, wątek 2026-09-15..18, integracja stopnia 4)

**Dokument:** „P₀-TETRA-20 v0.2.4 — Sieć ikosaedryczna, kanały nieliniowe i mechanizm VII" (status nagłówka: mapa problemów — 22 tryby potwierdzone niezależnie, hipoteza harmoniczna sfalsyfikowana, ω = f(‖x‖) kandydat, plateau ~ ‖T‖^4.5 kandydat, T16(b) otwarte z gotowym narzędziem). Data: 2026-09-18; historia §15: 09-15 audyt notatnika światło, 09-16 v0.1 (sieci, Hodge, I_h, Sym²), 09-17 baza 7 niezmienników, 09-18 PIĘĆ wersji jednego dnia (v0.2/0.2.1/0.2.2/0.2.3/0.2.4). Zależności: P₀-Centroid, P₀-Defect, P₀-Flow (w repo), P₀-Relacje jako kandydat (w repo v0.3); w rekomendacjach cel dopisków P₀-Algebra v0.4.1 (poza repo — nowy kandydat zależności). Powiązania: notatniki światło.ipynb i 7atraktorow.ipynb, ścieżka równoległa E-TETRA-06/06b/06c, skrypt e_tetra_08_quartic_scaling.py. Recenzja Claude W TREŚCI: niezależne implementacje 22/7/15 i 82 = 15 + 67 (zgodność co do jedności), przyznanie się do błędu pomieszania ω i plateau (§11.7), cofnięcie wątpliwości co do korelacji próg↔plateau (§11.8). Zależność rozliczona: TAU wymieniał P₀-TETRA-20 v0.2.4 jako zależność poza repo; rodzina Defect/Flow/Lattice wskazywała ten sam obiekt (ikosaedr). Deklarowana pozycja (§14.1): kandydat na filar/podprojekt ŁĄCZĄCY P₀-Defect, P₀-Flow, P₀-Relacje.

**Co bada:** mechanizm VII (nieliniowość generująca asymetrię) POZA K₄: na K₄ algebraicznie zablokowany (Tw. A P₀-Defect, Hom_{S₄}(Sym²V_cyc, V_cyc) = 0; ORB-LIGHT potwierdza porażkę empirycznie), na ikosaedrze aktywny. Wątek: (1) audyt notatnika światło — LIGHT-01..04 falsyfikują naiwną H-LIGHT-1 (czysta propagacja: d95 = 10, brak 3D; CENTROID: triangle violations = 0 ale d95 = 14) — trwały wkład metodologiczny: METRYCZNOŚĆ ≠ EUKLIDESOWOŚĆ ≠ 3D; (2) budowa sieci 20-czworościanów (v0.1: rozłączne tetra, defect energy 21 660 — daleko od P₀) z obserwacją Eulera linku: F = 20 → E = 30 → V = 12, link wierzchołka stopnia 20 = ikosaedr; (3) odkrycie, że ASE.cluster.Icosahedron NIE buduje klastra Mackaya (buduje FCC przecięty ikosaedrycznie; klaster Mackaya = koordynacja 12, sąsiedzi tworzą ikosaedr, każdy atom rdzenia w 20 czworościanach); (4) pełny Hodge na linku: C¹(K₁₂) = Im(d) ⊕ V_cyc, dim 11 + 19; (5) kanały nieliniowe i konstrukcje Φ; (6) dynamika: 7 atraktorów I_h + 15 chiralnych A₅; (7) algebra stopnia 4.

**Najmocniejsze (✅, wielometodowe, z tabelą statusów §13):**
1. **Negatywna tożsamość algebraiczna (§3.3, jawna negacja):** na ikosaedrze V_cyc ≇ Λ²(V_ρ) (19 ≠ 55) — ikosaedrowy V_cyc NIE jest algebrą Liego; Tw. A P₀-Defect nie jest kontrprzykładem ani brakiem zastosowania, tylko twierdzeniem o INNEJ KLASIE obiektów. Pierwsza jawna negacja tożsamości korpusu.
2. **Rozkład V_cyc (§4.2):** V_cyc = T_1g ⊕ T_2g ⊕ G_g ⊕ G_u ⊕ H_u (3+3+4+4+5 = 19 ✓); każdy irrep dokładnie raz, brak A_g i A_u (sektor cykliczny w 100% nietrywialny), mieszanka g/u 3/2; weryfikacja numeryczna trace = 19.0000; signed reprezentacja M_σ z err 3.4e-15.
3. **Kanały nieliniowe (§5):** Hom_{I_h}(Sym²V_cyc, V_cyc) = 24, Λ²: 30, tensor razem: 54 — wobec K₄: 0, 1, 1. Mechanizm VII na ikosaedrze ma 24 symetryczne kanały; dekompozycje Sym² (190 ✓) i Λ² (171 ✓) pełne.
4. **22 niezmienniki kubiczne (§5.5):** dim Sym³(V_cyc)^{A₅} = 22 (charaktery, 1320/60), I_h = 7, CHIRALNE = 22 − 7 = 15; trzy niezależne metody (charaktery, Gram-Schmidt z cond(G) = 1.27, SVD rank residuów 15), ortogonalność do I_h 9.4e-14; niezależne potwierdzenie Claude alternatywnym sumowaniem po elementach det = +1 — zgodność co do jedności. Interpretacja: pseudoskalary (niezmiennicze obrotowo, nie inwersyjnie).
5. **Algebra stopnia 4 (§5.5.7, NOWE v0.2.4):** dim Sym⁴(V_cyc)^{I_h} = 82 = 15 (iloczyny par znanych kwadratowych) + 67 genuinie nowych (pierwotnych); Φ_quartic eq-err 6.5e-16; dekompozycja przez rangę iloczynów; wzrost z 3 do 4 stopnia nieliniowy (wiele „kombinacji" stopnia 3).
6. **22 tryby dynamiczne (§9.4):** 7 (I_h) + 15 (chiralnych) = 22 atraktorów, 14/15 chiralnych stabilnych (CV < 0.05; c13 na granicy 0.0556); chamfer między rodzinami 0.76–1.03 (strukturalnie nowe), wewnątrz chiralnych 105 par > 0.3 (min 0.411); nowość chiralnych GEOMETRYCZNA nie czasowa (FFT: ω chiralnych węższe niż I_h i w całości wewnątrz ich zakresu); nowy kanał T_1g: chiralne (c3, c10) jako jedyne dominują w T_1g, baza I_h nigdy (0/7, strukturalne). Blowup realny (T_c zbiega przy dt → 0). Brak spontanicznego złamania I_h → A₅ (kowariancja po pełnej grupie 120; poprzedni test inwersji pojedynczej był niepełną diagnostyką).
7. **Sprzężenie amplituda–częstotliwość (§11.6):** r(‖x‖_attr, ω_top1) = +0.932 (n = 15, stabilne bez outliera c13); hipoteza harmonicznej k = 5 sfalsyfikowana (ω/2 pokrycia z widmem brak); kandydat ω = c·‖x‖, ω/‖x‖ ≈ 0.55 ± 0.03 stałe wzdłuż skanu ε — zasada skalowania amplitudowego v0.2.2.
8. **Dwa prawa skalowania (§11.7/§11.8):** ω ↔ ‖T‖ słaba (−0.11 na n = 15; na n = 7 było +0.825 — artefakt outliera k = 5), plateau ↔ ‖T‖ silna (+0.92, n = 11, dwie niezależne ścieżki interpolacji E-TETRA-06c: +0.91 i +0.96, próg −0.89); fit potęgowy plateau ~ ‖T‖^n, n ≈ 4.5, R² = 0.82. Rozróżnienie trzech zmiennych (ω, plateau, próg) — zasada v0.2.3.
9. **Degeneracja widma L_cyc (§9.4.7):** 19 wartości, tylko 5–6 unikatowych; 11 z 19 przy √λ = 3.1623 = √10 — konsekwencja dla kaskady dekoherencji: mody znikają grupami, 5–6 skoków, nie 19.

**Koncesje i sęki (jawnie):** historie korekt W TREŚCI — wzorzec przedpublikacyjnych errat: §8.4 (v0.1 twierdziła „hierarchię selekcji" późniejszych niezmienników; k = 5 okazuje się outsiderem w TRZECH niezależnych miarach — ‖T‖ 5.27 vs 4.67–4.88, ω_top1 4.97 vs 1.97–3.20, CV 0.0392 vs 0.0015–0.0205; stwierdzenie nieuprawnione na n = 7, prawdopodobnie ślad ortogonalizacji GS); §11.3 (korelacja ‖T‖↔ω +0.825 na n = 7 to artefakt k = 5: bez niego −0.223, bez k = 5,6: −0.738; potwierdzenie niezależne na n = 15: −0.103); §9.3 (rodziny „miękkie": grupują po kanale spektralnym, nie mechanizmie — k = 5 i k = 6 oba G_g, a różne prawa: dω/dε 0.303 vs 0.101, ω/‖x‖ rośnie vs maleje); §10.4.4 (test inwersji pojedynczej sugerował SSB — pełna grupa 120 pokazuje brak; zasada pełnej grupy v0.2.1); §11.7 (v0.2.4: pomieszanie ω i plateau w dyskusji z Claude — przyznanie się do błędu, korekta pozostaje w mocy). Sęki: cała dynamika za setupem poza repo (core_reconstruction.py: ikosaedr, I_h, P_cyc, L_cyc, Ms_all, P_irrep — skrypt quartic nie jest samodzielny); skrypt Claude buduje tylko 3 z 67 (find_new_quartic(3, seed = 777)), do fitu potrzeba ≥ 10; T16(b) otwarte: Claude nie domknął w limicie 300 s, przy 3000 krokach brak zbiegu do plateau; plateau nie jest czystą funkcją ‖T‖ (reszty ±1 na plateau 4–9, kierunek interpolacji znaczący, ścieżka (1,3) ciaśniejsza niż (1,5)); c13 na granicy stabilności; korelacje na próbkach n = 7 wymagane testy bez outsiderów (zasada v0.2). Dokument kończy: „Wyniki wymagają niezależnej replikacji" — mimo potwierdzeń wewnątrzsesyjnych, replikacja zewnętrzna Z1 nie wykonana.

**Struktury 💡:** chiralność jako własność algebraiczna (pseudoskalary: niezmienniczość obrotowa A₅ bez inwersyjnej I_h — odpowiednik algebraiczny rozróżnienia obraz/odbicie); klaster Mackaya jako fizyczny kandydat sieci P₀ (koordynacja 12 = ikosaedryczny link; ASE daje złą strukturę — lekcja narzędziowa); kanały nieliniowe jako FUNKCJA GRUPY (liczba kanałów zależy od podgrupy — por. rozpoznanie Lattice: rodzina bada jeden obiekt na różnych podgrupach); elementwise product fundamentalnie niezgodny z signed permutation reps — kanały VII wymagają tensorów wyższego rzędu (boxed); degeneracja √10 (krotność 11 z 19) jako strukturalne wyjaśnienie skokowych kaskad.

**Mosty 💡:**
1. **Do P₀-Defect (w obie strony):** jawna negacja V_cyc ≅ Λ²(V_ρ) (Defect §2) na niezupełnym grafie; dokument sam rekomenduje §12I „Przypadek niezupełny: ikosaedr" do Defect v0.9 — do rozliczenia przy przyszłej wersji Defect; Tw. A zyskuje jawne granice stosowalności (S₄/K_n), a nie kontrprzykład.
2. **Do P₀-Lattice (drabina podgrup):** Lattice prowadzi drabinę S₄→D₃h→C₃v→I_h — TETRA-20 to pełny etap I_h tej samej drabiny; bramkowy ikosaedr z Lattice (8 z 20 ścian, stabilizator T_h) to ten sam obiekt; nazwa dokumentu (TETRA-20) pochodzi od 20 ścian i 20 czworościanów linku, a wynik to 22 tryby.
3. **Do P₀-TAU (identyczne widmo):** widmo L_cyc tu: √λ = {2.2312, 2.4495^×2, 2.7080^×3, 2.7568, 2.8440, 3.1623^×11} — po spłaszczeniu λ = {4.9784, 6^×2, 7.3333^×3, 7.6, 8.0883, 10^×11} DOKŁADNIE widmo cytowane w TAU §4 (dim 19), z którego TAU liczy τ_period ikosaedra 0.448 = 1/√4.978. TAU P22 (blok GS 4×3 ikosaedru) i SERC χ'(iko) = 5: ten sam obiekt dostaje tu trzeci głos — TETRA-20 wnosi mu dynamikę nieliniową.
4. **Do P₀-Flow (czwarty obiekt):** rekomendacja §14.4: dodać §12.2a — ikosaedr jako czwarty obiekt (po Eulera-Arnolda, NS, T_b); T6 otwarte: T_a/T_b na ikosaedrze (wstępny punkt styku z Flow); P₀-Flow to w repo korzeń źródłowy, częściowo wchłonięty w Defect §12A-G — rekomendacja §12.2a dotyczy kontynuatora.
5. **Do P₀-SERC (asymetria):** chiralność jako trzeci typ asymetrii obok znaku i sekwencyjności (taksonomia 8 P₀); „terapeuta wybiera tryb = wybiera niezmiennik" (§11.4 realizacja §21 Relacji) ma odbicie w kanałach chiralnych — asymetria nieinwersyjna dostępna dynamicznie.
6. **Do P₀-Relacje:** jawna realizacja §16 (atraktor relacyjny), §17 (stabilność wzorca), §20 (zniewolenie relacyjne: tryby = baseny), §21 (terapia jako zmiana dynamiki), §33 (teza główna: algebra 5 irrepów → konstrukcja 22 niezmienników → dynamika 22 atraktorów) — pierwszy dokument z gotową tabelą realizacji Relacji; P₀-Relacje w repo jako kandydat.
7. **Do P₀-Experiments / P₀-Algebra:** E-TETRA-01..12 na listę (w tym planowane E-TETRA-12: dynamika stopnia 4); dopiski do P₀-Algebra v0.4.1 (klasyfikacja dynamiczna widma, struktura sprzężeń, algebra obserwowalności, algebra stopnia 4) — Algebra poza repo, przy wpięciu rozliczyć cztery pozycje.

**Sęk-odnogi:** T1 prawdziwy klaster Mackaya (nie ASE/FCC) na N = 7 powłok; T4 analiza spektralna quasi-periodyczna; T6 T_a/T_b na ikosaedrze (most do Flow); T7 rozszerzenie R4 → R12; T10/T11/T12 skale większych klastrów i interpretacja fizyczna 22 modów (test na N = 13); T13: czy istnieje G ⊃ I_h z Hom_G(Sym²V_cyc, V_cyc) = 0 — naturalne uogólnienie Tw. A; T14 postać funkcyjna ω(‖x‖) (trzy fity R² ≈ 0.87 bez poprawy); T15 test γ (czy ω/‖x‖ ≈ const przy zmianie γ — rozdzielenie mechanizmu od amplitudy); T16(b) prawo stopnia: czy wykładnik plateau zależy od stopnia (kandydaci: 2·(stopień−1) = 6, stopień+1 = 5, stopień·1.5 = 6 — jeśli niezależny, 4.5 uniwersalne).

**Statusy (mapa na Z1):** poziom algebraiczny ✅ i to wielometodowo (charaktery + Gram-Schmidt + SVD; Claude niezależna implementacja strony A₅; Φ_cubic/Φ_quartic eq-err na poziomie 1e-15/1e-16) — dla rachunków spełnia bramkę „≥ 2 zgodne rachunki", ale WSZYSTKO w jednej sesji 09-15..18 (potwierdzenia wewnątrzsesyjne, nie replikacje zewnętrzne); dynamika 🔍 (22 atraktory, chamfery, ω/‖x‖ ≈ 0.55, plateau ~ ‖T‖^4.5, brak SSB, nowy kanał T_1g) — wprost: wyniki wymagają niezależnej replikacji; ❌ domknięte: LIGHT 3D, mechanizm VII na K₄, hipoteza harmoniczna. Kolejność replikacji warsztatowej wg kosztu: (1) dekompozycja V_cyc rachunkiem charakterów (czysto algebraiczna, bez setupu), (2) 22/7/15 i 82 = 15 + 67 (charaktery, weryfikowalne analitycznie), (3) dekompozycje Sym²/Λ², (4) dynamika (droga: wymaga odtworzenia core_reconstruction.py — jednoczesny sprawdzian, czy opis dokumentu wystarcza do niezależnej odbudowy setupu, dobra bramka replikowalności Z1).

**Uwagi redakcyjne (verbatim):** 36 229 B, 1006 linii wg wc -l (odczyt narzędziowy 1007 — ostatnia Z finalnym EOL, drugi dokument korpusu z końcowym EOL po Memory), md5 266b6036 (kopia robocza); tytuł „P₀-TETRA-20 v0.2.4", podtytuł „Sieć ikosaedryczna, kanały nieliniowe i mechanizm VII"; status nagłówka jako mapa problemów (format RZADKI, drugi po TAU — dokument otwiera się od stanu problemów); pięć wersji jednego dnia 09-18; idiom autorski „genuinie" (spolszczone genuine) konsekwentnie w 8 miejscach — zachowany verbatim; kropka dziesiętna w rachunkach i dynamice (0.55, 6.5e-16, R² = 0.82) — inaczej niż TAU z polskim przecinkiem w prozie; notacja LaTeX dolarowa + 11 wystąpień boxed; bloki kodu z backtickami (8) — verbatim jak w SERC §18 i blokach programistycznych; polskie i angielskie nazwy eksperymentów mieszane (LIGHT/ORB-LIGHT vs światło); zależność od plików poza repo nie do rozliczenia z korpusu (notatniki, E-TETRA-06c, core_reconstruction.py); kończy się zdaniem „Wyniki wymagają niezależnej replikacji." z EOL.
P₀-TETRA-20 v0.2.4

Sieć ikosaedryczna, kanały nieliniowe i mechanizm VII

Wersja: 0.2.4 (integracja algebraicznych wyników stopnia 4, niezależne potwierdzenie 22/7/15)
Status: 🔍 22 tryby dynamiczne potwierdzone niezależnie; hipoteza harmonicznej k=5 sfalsyfikowana; ω = f(‖x‖) kandydat; plateau ~ ‖T‖^4.5 kandydat; T16(b) jawnie otwarte z gotowym narzędziem
Data: 2026-09-18
Zależności: P₀-Centroid, P₀-Defect, P₀-Flow, P₀-Relacje (kandydat)
Powiązane: notatnik światło.ipynb, Kopia notatnika 7atraktorow.ipynb, E-TETRA-06/06b/06c (ścieżka równoległa), e_tetra_08_quartic_scaling.py
Zmiana v0.2.3 → v0.2.4: dodano §5.5.7 (algebra stopnia 4: 82 = 15 + 67); zaktualizowano T16 (a) ✅ z niezależnym potwierdzeniem, (b) 💡 z gotowym narzędziem; dopisano do §11.8 niezależne potwierdzenie z równoległego wątku; dodano zasadę niezależnej implementacji do §16; zweryfikowano skrypt e_tetra_08_quartic_scaling.py (logika poprawna, wymaga setupu core_reconstruction.py).

---

0. Cel dokumentu

Dokument podsumowuje wątek badawczy zapoczątkowany analizą notatnika światło.ipynb i rozszerzony przez własne eksperymenty TETRA-20:

1. Audyt notatnika światło pod kątem spójności z konceptem P₀.
2. Próbę zbudowania sieci regularnych czworościanów z linkiem ikosaedrycznym.
3. Odkrycie, że ASE.cluster.Icosahedron nie buduje klastra Mackaya.
4. Pełną analizę algebraiczną linku ikosaedrycznego.
5. Konstrukcję jawnie G-ekwivariantnej nieliniowości na V_cyc.
6. Odkrycie 22 niezależnych trybów dynamicznych (7 I_h + 15 A₅-chiralnych).
7. Rozpoczęcie analizy niezmienników stopnia 4 (82 = 15 + 67, T16).

Główny wynik v0.1: Na sieci ikosaedrycznej mechanizm VII jest aktywny — w przeciwieństwie do K₄, gdzie jest algebraicznie zablokowany (Tw. A P₀-Defect). Rezultat: 7-wymiarowa przestrzeń trybów.

Główny wynik v0.2: Rozszerzenie A₅ ⊃ I_h daje 15 dodatkowych trybów chiralnych — dynamicznie niezależnych od 7 bazowych. Łącznie 22 tryby na ikosaedrze.

Główny wynik v0.2.1: Sprzężenie amplituda–częstotliwość — r(‖x‖_attr, ω) = 0.932 (n=15, identyczne bez outliera c13).

Główny wynik v0.2.2: Hipoteza harmonicznej k=5 sfalsyfikowana. Nowy kandydat: ω = c·‖x‖ — c ≈ 0.55 (k=5). Widmo L_cyc ma 5–6 unikatowych wartości (nie 19).

Główny wynik v0.2.3: Rozróżnienie dwóch niezależnych korelacji — ω ↔ ‖T‖ (słabe, my) vs plateau ↔ ‖T‖ (silne, ścieżka równoległa). Plateau ~ ‖T‖^4.5 (n≈4.5, R²=0.82, n=11 punktów).

Główny wynik v0.2.4: Algebra stopnia 4 — dim Sym⁴(V_cyc)^{I_h} = 82 = 15 + 67, gdzie 15 to iloczyny znanych kwadratowych, a 67 to genuinie nowe. Niezależne potwierdzenie 22/7/15 (dwie implementacje co do jedności). T16(b) jawnie otwarte z gotowym narzędziem.

---

1. Audyt notatnika światło

1.1. Struktura notatnika

Rodzina Eksperymenty Cel
LIGHT-01…04 Propagacja relacyjna → geometria Czy z dynamiki relacyjnej wyłania się 3D euklidesowa?
ORB-LIGHT-01…10 Mechanizm VII na K₄ Czy nieliniowość może wewnętrznie generować asymetrię?

1.2. Wyniki LIGHT — sfalsyfikacja naiwnej H-LIGHT-1

Eksperyment Kluczowy wynik
LIGHT-01 v_graph = 1.59, R² = 0.935 — ale używa ukrytych współrzędnych
LIGHT-02 Czysta propagacja bez współrzędnych: d95 = 10, d99 = 12 — brak 3D
LIGHT-03 Błąd metodologiczny (N=1055 zamiast N=1687)
LIGHT-04 CENTROID: triangle violations = 0, ale d95 = 14 — metryczność ≠ euklidesowość ≠ 3D

```
METRYCZNOŚĆ ≠ EUKLIDESOWOŚĆ ≠ 3D
```

Wniosek: H-LIGHT-1 sfalsyfikowana w wersji naiwnej.

1.3. Wyniki ORB-LIGHT — porażka mechanizmu VII na K₄

Eksperyment Wynik
ORB-LIGHT-05 SB_H skaluje się z ε → 0 — brak spontanicznego złamania
ORB-LIGHT-06 Jacobian: brak przejścia przez zero w H−
ORB-LIGHT-08 Poprawne projektory V₄ — H− sektory stabilne dla wszystkich β
ORB-LIGHT-09/10 ΔΓ ≈ 0 dla wszystkich β

Wniosek: Mechanizm VII nie działa na K₄ — zgodne z Tw. A P₀-Defect (Hom_{S₄}(Sym²V_cyc, V_cyc) = 0).

1.4. Wnioski z audytu

1. Notatnik metodologicznie dojrzały (sam wykrywa i naprawia błędy).
2. Wyniki negatywne dla najmocniejszych tez.
3. Rozróżnienie metryczność/euklidesowość/3D — trwały wkład metodologiczny.
4. Punkt wyjścia: mechanizm VII na innej strukturze — ikosaedrze.

---

2. TETRA-20 — próba budowy sieci 20-tetra

2.1. Pierwsza próba (v0.1)

20 tetraedrów dzielących centralny wierzchołek, pozostałe rozłączne. Defect energy = 21 660 — daleko od P₀. Ale kod zawierał obserwację:

```
F = 20 (trójkąty w linku)
E = 3F/2 = 30
V = E − F + 2 = 12
```

Link wierzchołka stopnia 20 w regularnej sieci czworościanów musi być ikosaedrem.

2.2. Odkrycie: Klaster Mackaya

Klaster Mackaya to dokładnie sieć, w której każdy atom rdzenia ma koordynację 12, a jego sąsiedzi tworzą ikosaedr. Ikosaedr ma 20 trójkątnych ścian → każdy atom rdzenia należy do 20 czworościanów.

2.3. Problem z ASE

Rozmiar Tetra-degree 8 (FCC) Tetra-degree 20 (Mackay)
N=147 80 1
N=309 110 1
N=923 500 1

ASE.cluster.Icosahedron NIE buduje klastra Mackaya — buduje FCC przecięty ikosaedrycznie.

---

3. Link ikosaedryczny — pełna analiza Hodge'a

3.1. Prawdziwy ikosaedr

```python
phi = (1 + sqrt(5)) / 2
ico_vertices = [
    [0, 1, phi], [0, 1, -phi], [0, -1, phi], [0, -1, -phi],
    [1, phi, 0], [1, -phi, 0], [-1, phi, 0], [-1, -phi, 0],
    [phi, 0, 1], [phi, 0, -1], [-phi, 0, 1], [-phi, 0, -1],
]
d_edge = 2 / sqrt(2 + phi) ≈ 1.0515
```

· V = 12, E = 30, F = 20, χ = 2 (sfera S²)

3.2. Kluczowa poprawka d_edge

Pierwsza wersja używała odległości między drugimi sąsiadami (iloczyn skalarny = −1/√5), nie sąsiadami (+1/√5) → graf distance-2 zamiast ico. Poprawka:

```python
d_edge = 2 / np.sqrt(2 + phi)  # prawdziwa długość krawędzi
```

3.3. Rozkład Hodge'a na linku

C^1(K_{12}) = \operatorname{Im}(d) \oplus V_{\text{cyc}}

· dim Im(d) = V_ρ = 11
· dim V_cyc = 30 − 11 = 19

Rozszerzenie v0.2 — jawna negacja tożsamości algebraicznej. W P₀-Defect §2 dla grafu zupełnego K_n zachodzi:

V_{\rm cyc} \cong \Lambda^2(V_\rho) \cong \mathfrak{so}(V_\rho).

Na ikosaedrze tożsamość ta NIE zachodzi:

\dim \Lambda^2(V_\rho) = \binom{11}{2} = 55, \qquad \dim V_{\rm cyc} = 19 \neq 55.

Konsekwencje strukturalne:

Własność K_n Ikosaedr
V_cyc ≅ Λ²(V_ρ) ✓ ✗
Struktura algebry Liego na V_cyc 𝔰𝔬(V_ρ) brak naturalnej
Bracket [A,B] istnieje nie istnieje
Tw. A (m_n = 1) ✓ dla S_n poza zakresem

Ikosaedrowy V_cyc nie jest algebrą Liego. To jakościowo inny typ struktury niż K_n. Dlatego Tw. A P₀-Defect nie jest kontrprzykładem ani nie ma zastosowania — jest twierdzeniem o innej klasie obiektów.

---

4. Grupa I_h i rozkład V_cyc

4.1. Grupa I_h

· A₅ (60 elementów, obroty, det = +1)
· I_h (120 elementów, obroty + odbicia)

Klasy sprzężenia (10 klas):

Klasa \|klasa\| χ_{V_cyc} χ_V(g²)
E 1 19 19
C2 15 −1 19
C3 20 1 1
C5 12 −1 −1
C5² 12 −1 −1
i 1 1 19
iC2 15 −3 19
iC3 20 1 1
iC5 12 1 −1
iC5² 12 1 −1

4.2. Rozkład V_cyc

\boxed{V_{\text{cyc}} = T_{1g} \oplus T_{2g} \oplus G_g \oplus G_u \oplus H_u}

Wymiar: 3 + 3 + 4 + 4 + 5 = 19 ✓

Własności:

· Każdy irrep dokładnie raz
· Brak A_g ani A_u — sektor cykliczny w 100% nietrywialny
· Mieszanka g/u (3 gerade, 2 ungerade)

Weryfikacja numeryczna: sum(trace(P_irrep)) = 19.0000 — dokładna zgodność.

4.3. Signed reprezentacja

(M_\sigma)_{e_\sigma, e} = \text{sign}(\sigma, e)

Weryfikacja:

· M_σ @ d = d @ P_vertex(σ) — err = 0
· M_σ @ P_cyc = P_cyc @ M_σ — err = 3.4e-15

---

5. Kanały nieliniowe — Hom(Sym²V_cyc, V_cyc)

5.1. Rozkłady

\text{Sym}^2 V_{\text{cyc}} = 5A_g \oplus A_u \oplus 2T_{1g} \oplus 5T_{1u} \oplus 2T_{2g} \oplus 5T_{2u} \oplus 7G_g \oplus 6G_u \oplus 11H_g \oplus 7H_u

Wymiar: 190 ✓

\Lambda^2 V_{\text{cyc}} = A_u \oplus 6T_{1g} \oplus 5T_{1u} \oplus 6T_{2g} \oplus 5T_{2u} \oplus 5G_g \oplus 6G_u \oplus 5H_g \oplus 7H_u

Wymiar: 171 ✓

5.2. Kanały nieliniowe

\boxed{\text{Hom}_{I_h}(\text{Sym}^2 V_{\text{cyc}}, V_{\text{cyc}}) = 24}


\boxed{\text{Hom}_{I_h}(\Lambda^2 V_{\text{cyc}}, V_{\text{cyc}}) = 30}


\boxed{\text{Hom}_{I_h}(V_{\text{cyc}} \otimes V_{\text{cyc}}, V_{\text{cyc}}) = 54}

Rozkład per irrep:

irrep sym. antysym.
T1g 2 6
T2g 2 6
G_g 7 5
G_u 6 6
H_u 7 7
razem 24 30

5.3. Porównanie z K₄

 K₄ (S₄) Ikosaedr (I_h)
V_cyc 3-wym nieprzywiedlna 19-wym, 5 irrepów
Sym² kanał 0 24
Λ² kanał 1 (bracket) 30
Razem 1 54

Jakościowa różnica: na K₄ mechanizm VII algebraicznie zablokowany (Tw. A). Na ikosaedrze istnieje 24 symetrycznych kanałów.

---

5.5. Rozszerzenie A₅-symetryczne i algebra stopnia 4

5.5.1. Motywacja

Niezmienniki kubiczne I_h są podprzestrzenią niezmienników A₅:

\text{Sym}^3(V_{\text{cyc}})^{I_h} \subseteq \text{Sym}^3(V_{\text{cyc}})^{A_5}.

Pytanie: ile wymiarów ma przestrzeń A₅-niezmiennicza i ile z nich jest chiralnych (A₅-niezmienniczych, ale nie I_h)?

5.5.2. Rachunek charakterów

Dla A₅ (60 elementów, 5 klas) i V = V_cyc:

Klasa \|klasa\| χ_V(g) χ_V(g²) χ_V(g³) χ_{Sym³V}(g)
E 1 19 19 19 1330
C2 15 −1 19 −1 −10
C3 20 1 1 19 7
C5 12 −1 −1 −1 0
C5² 12 −1 −1 −1 0

\dim V^{A_5} = \frac{1}{60}(1330 - 150 + 140) = \frac{1320}{60} = 22.

5.5.3. Wynik

\boxed{\dim \text{Hom}_{A_5}(\text{triv}, \text{Sym}^3 V_{\text{cyc}}) = 22}


\boxed{\dim \text{Hom}_{I_h}(\text{triv}, \text{Sym}^3 V_{\text{cyc}}) = 7}


\boxed{\text{chiralne} = 22 - 7 = 15}

Dekompozycja:

\text{Sym}^3(V_{\text{cyc}})^{A_5} = \text{Sym}^3(V_{\text{cyc}})^{I_h} \oplus \text{(15 chiralnych)}.

5.5.4. Weryfikacja numeryczna

Trzy niezależne metody:

1. Rachunek charakterów: 22 (analityczne, wzór sumowania po klasach)
2. Gram-Schmidt z rzutowaniem na I_h: 15 chiralnych (cond(G) = 1.27)
3. SVD rank residuali: 15 (rank(residuals) = 15)

Kontrola: max |<chiralne, I_h>| = 9.4e-14 — pełna ortogonalność.

Niezależna weryfikacja z równoległego wątku (v0.2.4): Sumowanie charakteru Sym³ po podgrupie A₅ wyłącznie z elementów o det=+1 (Claude, metoda alternatywna) daje 22/7/15 — zgodność co do jedności. Dwie różne implementacje, ten sam wynik.

5.5.5. Interpretacja strukturalna

15 chiralnych niezmienników to funkcje $I: V_{\text{cyc}} \to \mathbb{R}$ spełniające:

· $I(g \cdot x) = I(x)$ dla wszystkich $g \in A_5$ (obroty),
· $I(g \cdot x) \neq I(x)$ dla niektórych $g \in I_h \setminus A_5$ (inwersja).

Są to funkcje niezmiennicze obrotowo, ale nie inwersyjnie — algebraiczne odpowiedniki „pseudoskalarów" na V_cyc.

5.5.6. Nowy kanał T1g

W bazie I_h żaden niezmiennik nie dominuje kanału T1g. W bazie chiralnych c3 i c10 dominują T1g. To pierwsza dynamicznie istotna różnica między obiema rodzinami.

5.5.7. Algebra stopnia 4 (NOWE w v0.2.4)

Pytanie: ile jest niezmienników stopnia 4 w Sym⁴(V_cyc)^{I_h} i ile z nich to genuinie nowe (nie iloczyny znanych stopnia niższego)?

Wynik (Claude, niezależna weryfikacja numeryczna):

\dim \text{Sym}^4(V_{\text{cyc}})^{I_h} = 82

Dekompozycja przez rangę iloczynów znanych niezmienników kwadratowych:

\underbrace{15}_{\text{iloczyny par znanych kwadratowych}} + \underbrace{67}_{\text{genuinie nowe (pierwotne)}} = 82

Weryfikacja:

· Ranga iloczynów par znanych niezmienników kwadratowych = 15 (dokładnie)
· Niezmiennik testowy: eq-err = 6.5e-16 dla Φ_quartic
· Φ_quartic: $\Phi_4(x) = 4 \cdot T_{ijkl} x_j x_k x_l$ (gradient sześcienny)

Znaczenie: Sama algebra stopnia 4 jest znacznie bogatsza niż stopnia 3 (82 vs 22). Ale liczba genuinie nowych niezmienników (67) już nie jest tak dramatycznie większa niż chiralnych stopnia 3 (15). To sugeruje, że wzrost wymiaru z 3 do 4 nie jest liniowy — przestrzeń niezmienników stopnia 4 zawiera dużo „kombinacji" stopnia 3.

Status: ✅ algebraiczny. Dynamiczne wykorzystanie 67 nowych niezmienników — 💡 (T16b).

Uwaga metodologiczna: Claude podaje, że w skrypcie e_tetra_08_quartic_scaling.py buduje 3 nowe niezmienniki stopnia 4 przez find_new_quartic(3, seed=777). To nie jest pełna baza 67 — to 3 reprezentatywne. Dla pełnej bazy stopnia 4 trzeba uruchomić iterację find_new_quartic(67, ...).

---

6. Konstrukcje Φ — cztery podejścia

6.1. Elementwise product

\Phi_{30}(x,y) = P_{\text{cyc}}(x \odot y)

Wynik: ‖Φ_30(x,x)‖ ~ 1e-19 — trywialnie zero. Elementwise square gubi znaki signed permutation.

6.2. Cross-terms

Wynik: ‖Φ_cross(x,x)‖ ~ 3e-17 — trywialnie zero.

6.3. Coboundary D^T((Dx) ⊙ (Dx))

Wynik: ‖Φ_D(x,x)‖ ~ 1.5-2.1 — niezerowa. Ale eq-err = 1.9 — Φ_D nie jest G-ekwivariantna.

6.4. Wniosek

\boxed{\text{Elementwise product fundamentalnie niezgodny z signed permutation reps.}}

Żadna konstrukcja oparta na $x \odot x$ nie da G-ekwivariantnej Φ. Kanały VII wymagają tensorów wyższego rzędu.

---

7. Φ_cubic — gradient niezmiennika kubicznego

7.1. Konstrukcja

Niezmiennik kubiczny $I: V_{\text{cyc}} \to \mathbb{R}$:

I(g \cdot x) = I(x) \quad \forall g \in I_h

Gradient zachowuje symetrię: $\nabla I(gx) = g \nabla I(x)$.

Forma biegunowa:
\Phi_{\text{cubic}}(x,y)_i = 6 \cdot T_{ijk} x_j y_k

7.2. Konstrukcja numeryczna

1. Losowy tensor 30³
2. Rzutowanie na $V_{\text{cyc}}^{\otimes 3}$
3. Symetryzacja
4. Rzutowanie na A_g (uśrednianie po 120 elementach I_h)
5. Gram-Schmidt

7.3. Wyniki

· eq-err = 5.9e-16 ✓ — Φ_cubic JEST G-ekwivariantna
· ‖Φ_cubic(x,x)‖ ~ 0.7-1.4 ✓ — niezerowa

Bifurkacja:
· ε < 15: bounded
· ε = 20: BLOWUP (bez γ)
· ε = 20 z γ=ε: GROWING z saturacją ‖x‖ ≈ 2.2

7.4. Selekcja kanałów

Analiza wzorca dla ε=γ=5:

irrep frakcja ratio
T2g 25.6% 1.62
H_u 23.6% 0.90
T1g 22.0% 1.39
G_g 21.7% 1.03
G_u 7.2% 0.34

Słaba selekcja pojedynczego niezmiennika.

7.5. Φ_quartic (NOWE w v0.2.4)

Dla stopnia 4:

\Phi_{\text{quartic}}(x)_i = 4 \cdot T_{ijkl} x_j x_k x_l

Gradient sześcienny w x (dla porównania: Φ_cubic — kwadratowy).

Weryfikacja: eq-err = 6.5e-16 (Φ_quartic jest G-ekwivariantna).

Uwaga numeryczna: dynamika z Φ_quartic może być bardziej sztywna numerycznie niż z Φ_cubic. Rozważyć damping_order = 3 (domyślnie) lub 5 (bezpiecznik) w integracji.

---

8. 7 niezmienników kubicznych I_h — baza

8.1. Wymiar

\text{Sym}^3 V_{\text{cyc}} \supset A_g \text{ z krotnością 7}

7 niezależnych niezmienników kubicznych $I_k: V_{\text{cyc}} \to \mathbb{R}$.

8.2. Baza przez Gram-Schmidt

k \|T\| w bazie eq_err ∇I scale
0 4.83 2.1e-15 0.95
1 4.68 2.2e-15 1.01
2 4.88 2.2e-15 1.01
3 4.67 3.6e-15 0.93
4 4.79 9.2e-15 0.93
5 5.27 3.3e-14 0.99
6 4.68 1.5e-13 1.03

8.3. Selekcja per niezmiennik

k T1g T2g G_g G_u H_u dominant max ratio
0 0.037 0.170 0.168 0.207 0.419 H_u 1.59
1 0.024 0.030 0.343 0.056 0.547 H_u 2.08
2 0.181 0.042 0.137 0.425 0.215 G_u 2.02
3 0.004 0.004 0.432 0.528 0.032 G_u 2.51
4 0.281 0.297 0.287 0.066 0.070 T2g 1.88
5 0.001 0.001 0.897 0.049 0.052 G_g 4.26
6 0.034 0.031 0.853 0.046 0.036 G_g 4.05

Rozkład dominujących:

· H_u: 2/7 (k=0, 1)
· G_u: 2/7 (k=2, 3)
· G_g: 2/7 (k=5, 6)
· T2g: 1/7 (k=4)
· T1g: 0/7 — nigdy nie dominuje (strukturalne)

8.4. Hierarchia selekcji — KOREKTA v0.2

Wersja v0.1: „k=5, 6 (prawie czyste G_g): ratio 4.0-4.3 — najsilniejsza selekcja, niezmienniki późniejsze w bazie są coraz czystszymi generatorami konkretnych kanałów".

Korekta v0.2:

k=5 jest jednocześnie outlierem w trzech niezależnych miarach:

Miara Wartość k=5 Reszta k=0..4, 6
\|T\| 5.27 4.67–4.88
ω_top1 (B2) 4.97 1.97–3.20
CV atraktor (B1) 0.0392 0.0015–0.0205

Trzy osobne miary, ten sam punkt. To nie „hierarchia selekcji" — to jeden ekscentryczny punkt w bazie. Prawdopodobna przyczyna: k=5 był znaleziony jako 6. z rzędu w procedurze Grama-Schmidta i może nosić ślad ortogonalizacji (mniejsza „przypadkowość" niż k=0–4).

Konsekwencja: stwierdzenie „niezmienniki późniejsze w bazie są czystszymi generatorami" jest nieuprawnione na n=7.

---

9. 7 atraktorów, 4 rodziny

9.1. Porównanie atraktorów

para rel_dist
0-3 0.80
3-5 0.92
0-5 0.94
1-4 0.86
5-6 0.83

Wszystkie > 0.80 — atraktory strukturalnie różne.

9.2. Rodziny

Rodzina Niezmienniki Dominant Czystość (ratio)
G_g k=5, 6 G_g 4.26, 4.05
G_u k=2, 3 G_u 2.02, 2.51
H_u k=0, 1 H_u 1.59, 2.08
T2g k=4 T2g 1.88
T1g — (żaden) zawsze drugi

9.3. Test wewnątrz rodzin

para rel_dist std
0-1 (H_u) 0.699 0.108
2-3 (G_u) 0.874 0.038
5-6 (G_g) 0.534 0.167

Wszystkie pary > 0.5 — rodziny są miękkie. Grupują po dominującym kanale spektralnym, ale każdy niezmiennik ma własny atraktor.

Korekta v0.2.2 — rodzina G_g zawiera dwa różne mechanizmy. Skan ε dla k=5 i k=6 (oba G_g) pokazuje różne prawa skalowania:

 k=5 k=6
dω/dε +0.303 +0.101
ω(ε=40) / ω(ε=10) 5.02× 3.83×
ω/‖x‖ trend rośnie (0.54 → 0.59) maleje (0.55 → 0.48)

„Rodzina" grupuje po dominującym kanale spektralnym, nie po typie dynamiki.

---

9.4. 22 tryby na ikosaedrze

9.4.1. Dynamika 15 chiralnych

Każdy z 15 chiralnych niezmienników (§5.5) został znormalizowany jak baza I_h i uruchomiony w dynamice $\ddot x = -L_{\text{cyc}} x + \varepsilon \Phi_k(x,x) - \gamma \|x\|^2 x$ dla ε = γ = 20, n_seeds = 3.

id \|x\| CV dominant stabilny
c0 3.644 0.0013 G_u ✓
c1 6.157 0.0348 H_u ✓
c2 5.693 0.0021 H_u ✓
c3 4.261 0.0051 T1g ✓
c4 3.949 0.0002 G_g ✓
c5 3.892 0.0022 H_u ✓
c6 3.704 0.0004 T2g ✓
c7 3.912 0.0017 G_u ✓
c8 5.424 0.0140 G_u ✓
c9 5.180 0.0075 H_u ✓
c10 4.036 0.0050 T1g ✓
c11 4.143 0.0020 H_u ✓
c12 4.532 0.0068 G_g ✓
c13 4.436 0.0556 H_u ✗ (granica)
c14 5.294 0.0055 G_u ✓

14/15 stabilnych (CV < 0.05), c13 na granicy (0.0556).

9.4.2. Rozkład dominujących irreps

irrep I_h (7) chiralne (15)
H_u 2 6
G_u 2 4
G_g 2 2
T2g 1 1
T1g 0 2

Nowy kanał T1g: chiralne jako jedyne dominują w T1g (c3, c10).

9.4.3. Chamfer między rodzinami

Min chamfer każdego chiralnego do wszystkich 7 atraktorów I_h (RMS-znormalizowane):

Zakres Wartość
min 0.76 (c12 ↔ k3)
max 1.03 (c0)
średnia 0.936

Wszystkie 15 chiralnych jest daleko od wszystkich 7 I_h. Są to strukturalnie nowe atraktory.

9.4.4. Chamfer wewnątrz chiralnych

Macierz 15 × 15 (RMS-znormalizowane):

Statystyka Wartość
mean (off-diag) 1.066
min 0.411 (c1 ↔ c13)
max 1.404

Klasteryzacja aglomeracyjna:

· próg 0.2 → 15 klastrów
· próg 0.3 → 15 klastrów
· próg 0.4 → 15 klastrów
· próg 0.5 → 14 klastrów (c1 i c13 się łączą)
· próg 0.7 → 14 klastrów

Wszystkie 105 par > 0.3.

9.4.5. Wniosek

\boxed{\text{7 (I}_h\text{)} + \text{15 (chiralnych)} = \text{22 niezależne tryby dynamiczne na ikosaedrze.}}

Wszystkie stabilne, wszystkie wzajemnie odległe o chamfer > 0.4.

9.4.6. FFT chiralnych — nowość geometryczna, nie czasowa

Dla każdego z 15 chiralnych atraktorów policzono FFT + autokorelację normy trajektorii:

Zakres ω_top1 I_h (7) Chiralne (15)
min 2.067 2.067
max 4.933 3.600
mean 2.943 2.707
std 0.890 0.410

Rozkład ω chiralnych jest węższy niż I_h. Wszystkie 15 chiralnych mają ω wewnątrz zakresu wyznaczonego przez I_h (margines 0.05 — 15/15 wewnątrz).

Wniosek: nowość 15 chiralnych jest geometryczna (Chamfer 0.76–1.03), nie czasowa.

9.4.7. Widmo L_cyc — degeneracja modów

Widmo L_cyc ma 19 niezerowych wartości własnych, ale tylko 5–6 unikatowych:

√λ Krotność
2.2312 1
2.4495 2
2.7080 3
2.7568 1
2.8440 1
3.1623 11

Ponad połowa modów (11 z 19) siedzi przy dokładnie tej samej częstości √λ = 3.1623 = √10.

Konsekwencja dla kaskady dekoherencji: przy T rosnącym od zera mody znikają nie pojedynczo, ale grupami. Kaskada ma 5–6 skoków, nie 19.

---

10. Stabilność atraktorów

10.1. Test 10 seedów per niezmiennik I_h

k \|x\| mean \|x\| std CV dominant
0 3.6062 0.0106 0.0029 H_u
1 4.0877 0.0062 0.0015 H_u
2 4.1625 0.0162 0.0039 G_u
3 5.6260 0.1151 0.0205 G_u
4 3.8895 0.0179 0.0046 T2g
5 8.6951 0.3410 0.0392 G_g
6 3.9737 0.0425 0.0107 G_g

Wszystkie CV < 0.05.

10.2. Podsumowanie stabilności

Kategoria Niezmienniki
Bardzo stabilne (CV < 0.005) k = 0, 1, 2, 4
Stabilne (0.005 ≤ CV < 0.02) k = 3, 6
Umiarkowanie stabilne (0.02 ≤ CV < 0.05) k = 5

10.3. Korelacja z siłą selekcji — KOREKTA v0.2

Wersja v0.1: „Brak prostej korelacji — najsilniejsza selekcja (k=5) ma najwyższe CV."

Korekta v0.2: k=5 jest outlierem w trzech miarach jednocześnie (§8.4). Do rozstrzygnięcia: powtórzyć budowę bazy z ≥ 20 niezależnymi seedami lub użyć interpolacji liniowej (v0.2.3).

Dopisek v0.2.1: Na 15 chiralnych r(CV, ω) = +0.791 po usunięciu c13.

10.4. Kowariancja po pełnej I_h

10.4.1. Protokół

Dla każdego atraktora (7 I_h + 15 chiralnych) policzono:

\text{min\_chamfer}(x^*) = \min_{g \in I_h \setminus \{e\}} \text{chamfer}(x^*, g \cdot x^*)

10.4.2. Wyniki

Zbiór mean min_chamfer min max
I_h (7) 0.408 0.202 0.567
Chiralne (15) 0.392 0.249 0.657

Obie rodziny zachowują się identycznie w teście kowariancji.

10.4.3. Test A₅ vs I_h — rozstrzygnięcie

Zbiór A5_min − Ih_min
I_h (7) 0.000–0.042
Chiralne (15) 0.000–0.000

10.4.4. Interpretacja

Nie ma spontanicznego złamania I_h → A₅. Dynamika zachowuje typ symetrii niezmiennika.

Konsekwencja metodologiczna: poprzedni test (inwersja pojedynczego elementu) dawał chamfer ≈ 1.0 dla wszystkich — i sugerował złamanie. Pełny test po 120 elementach pokazuje, że to była niepełna diagnostyka.

---

11. Wnioski dla P₀

11.1. Cztery poziomy wyników

Algebraiczny (✅):

· $V_{\text{cyc}} = T_{1g} \oplus T_{2g} \oplus G_g \oplus G_u \oplus H_u$
· $\text{Hom}_{I_h}(\text{Sym}^2 V_{\text{cyc}}, V_{\text{cyc}}) = 24$
· $\dim V^{A_5} = 22$, chiralne = 15
· V_cyc ≇ Λ²(V_ρ) — ikosaedr nie jest algebrą Liego
· Widmo L_cyc: 5–6 unikatowych wartości
· $\dim \text{Sym}^4(V_{\text{cyc}})^{I_h} = 82 = 15 + 67$

Konstrukcyjny (✅):

· 7 niezależnych niezmienników I_h stopnia 3
· 15 niezależnych niezmienników chiralnych stopnia 3
· 67 genuinie nowych niezmienników stopnia 4 (Φ_quartic eq-err = 6.5e-16)
· Jawnie G-ekwivariantna Φ_cubic (eq-err ~ 1e-15)

Dynamiczny (🔍):

· 22 niezależne atraktory (7 + 15)
· Wszystkie stabilne (CV < 0.05 poza c13)
· Chamfer między rodzinami: 0.76–1.03
· Chamfer wewnątrz chiralnych: średnia 1.066
· Brak spontanicznego złamania I_h → A₅
· ω = c·‖x‖, c ≈ 0.55 dla k=5
· Plateau ~ ‖T‖^4.5 (n=11, dwie ścieżki)

Nowy kanał (🔍):

· T1g dominuje w c3, c10

11.2. Porównanie z K₄

Właściwość K₄ (S₄) Ikosaedr (I_h)
V_cyc 3-wym nieprzywiedlna 19-wym, 5 irrepów
V_cyc ≅ Λ²V_ρ ✓ ✗
Hom(Sym², V_cyc) 0 24
Mechanizm VII algebraicznie zablokowany aktywny
Niezmienniki kubiczne 1 (e₃) 7 (I_h) + 15 (chiralnych)
Atraktory nieliniowe 1 (bracket) 22 tryby

11.3. Korekta §11.3 v0.1 — korelacja ‖T‖ ↔ ω

Wersja v0.1: sugerowała, że „próg wzbudzenia jest lepszym, bardziej informacyjnym deskryptorem niż sama norma końcowa" na podstawie korelacji r(‖T‖, plateau) ≈ 0.95.

Korekta v0.2: na n=7 korelacje są artefaktem k=5:

Korelacja Pełna (n=7) Bez k=5 (n=6) Bez k=5,6 (n=5)
r(‖T‖, ω_top1) +0.825 −0.223 −0.738

Potwierdzenie na n=15 (v0.2.1). Na niezależnej próbce 15 chiralnych niezmienników:

Korelacja Pełna (n=15) Bez outliera c13 (n=14)
r(‖T‖, ω_top1) −0.112 −0.103

Brak związku ‖T‖ ↔ ω potwierdzony niezależnie.

Uwaga kluczowa (v0.2.3): to NIE znaczy, że wszystkie korelacje z ‖T‖ są artefaktami. Zmienna ω nie koreluje z ‖T‖. Ale plateau koreluje silnie — zob. §11.7 i §11.8.

11.4. Realizacja idei P₀-Relacje

· §16 (Atraktor relacyjny): ✓ — atraktor zależy od niezmiennika; teraz 22 tryby.
· §17 (Stabilność wzorca): ✓ — lokalna zmienność + globalna niezmienniczość.
· §20 (Zniewolenie relacyjne): ✓ — różne tryby = różne baseny.
· §21 (Terapia jako zmiana dynamiki): ✓ — wybór trybu = wybór niezmiennika.
· §33 (Główna teza): ✓ — wielopoziomowa struktura: algebra (5 irrepów), konstrukcja (22 niezmienniki), dynamika (22 atraktory).

11.5. Metafora dla P₀

\boxed{\text{K}_4 \text{ ma } 1 \text{ kanał nieliniowy, ikosaedr ma } 22.}

11.6. Sprzężenie amplituda–częstotliwość

Na 15 chiralnych atraktorach:

Korelacja Pełna (n=15) Bez c13 (n=14)
r(‖x‖_attr, ω_top1) +0.932 +0.932
r(CV, ω_top1) +0.386 +0.791
r(‖T‖, ω_top1) −0.112 −0.103

Hipoteza harmonicznej — sfalsyfikowana.

ε ω_top1 ω/2 Blisko √λ?
10 2.267 1.13 poza widmem
20 5.267 2.63 blisko 2.708, ale nie =
40 11.383 5.69 daleko od wszystkiego

Nowy kandydat: ω = f(‖x‖), niezależnie od ε.

ε ω ‖x‖ ω/‖x‖
10 2.267 4.231 0.536
15 3.700 6.970 0.531
20 5.267 9.501 0.554
30 8.133 14.175 0.574
40 11.383 19.287 0.590

ω/‖x‖ ≈ 0.55 ± 0.03 — stałe wzdłuż ε.

11.7. Rozróżnienie korelacji — ω ↔ ‖T‖ vs plateau ↔ ‖T‖

Kluczowa klaryfikacja v0.2.3. Dwie różne korelacje z ‖T‖, które łatwo pomylić:

Korelacja Zmienna zależna Źródło Wynik
r(‖T‖, ω_top1) częstość oscylacji TETRA-20 §11.3/§11.6 słaba (−0.11 na n=15)
r(‖T‖, plateau) amplituda atraktora E-TETRA-06c silna (+0.92 na n=11)
r(próg, plateau) — E-TETRA-06c silna ujemna (−0.89 na n=11)

Interpretacja fizyczna:

· ω — jak szybko atraktor oscyluje wewnątrz swojego basenu. Zależy od amplitudy ‖x‖ (r=0.932), nie od skali niezmiennika ‖T‖.
· plateau — jak duży jest atraktor. Zależy silnie od ‖T‖.
· próg — jaka energia startowa jest potrzebna. Maleje z plateau.

ω rośnie z ‖T‖ pośrednio, przez plateau: ‖T‖ ↑ → plateau ↑ → ‖x‖ ↑ → ω ↑. Ale r(‖T‖, ω) bezpośrednio może być słabe.

Konsekwencja dla §11.3: korekta „korelacja ‖T‖ ↔ ω_top1 jest artefaktem k=5" dotyczy tylko ω.

Uwaga o pomieszaniu zmiennych (v0.2.4). W dyskusji z równoległym wątkiem (Claude) wystąpiło pomieszanie ω i plateau — sformułowanie „korelacja ‖T‖↔ω jest realna" w odniesieniu do wyniku, który w rzeczywistości dotyczył plateau. Claude przyznał się do błędu. Korekta z §11.7 v0.2.3 pozostaje w mocy — plateau koreluje z ‖T‖, nie ω.

11.8. Prawo skalowania plateau ~ ‖T‖^4.5

Wynik z równoległej ścieżki E-TETRA-06c (interpolacje niezmienników).

Na 11 unikalnych punktach, pochodzących z dwóch niezależnych ścieżek interpolacji:

Ścieżka corr(próg, plateau) corr(‖T‖, plateau)
(1,5) −0.82 +0.91
(1,3) −0.97 +0.96
połączone (n=11) −0.89 +0.92

Fit potęgowy: plateau ~ A·‖T‖^n daje

n \approx 4.5, \quad R^2 = 0.82.

Uwaga metodologiczna: Claude cofa wcześniejszą wątpliwość z v0.1 TETRA-20 (korelacja próg↔plateau jako artefakt k=5). Dwie niezależne ścieżki interpolacji dają ten sam kierunek zależności — efekt jest realny.

Ale nie jest to czysta funkcja ‖T‖. Reszty fitu są rzędu ±1 na plateau ~4–9. Ścieżka (1,3) leży ciaśniej wokół trendu niż (1,5) — kierunek w przestrzeni niezmienników ma znaczenie.

Niezależne potwierdzenie (v0.2.4). Dwie niezależne implementacje — ścieżka główna TETRA-20 i ścieżka równoległa E-TETRA-06c — dają ten sam kierunek korelacji plateau ↔ ‖T‖ (+0.91/+0.96) i tę samą liczbę 22/7/15 (co do jedności). To podnosi wiarygodność obu wyników.

Status: 🔍 (dwie ścieżki, n=11); 💡 (postać funkcyjna).

---

12. Otwarte problemy

12.1. Tabela

# Problem Status Priorytet
T1 Prawdziwy klaster Mackaya (nie ASE FCC) 🔍 Wysoki
T2 Test niezmienniczości atraktorów — 10 seed per k ✅ —
T3 Okresy atraktorów per niezmiennik (FFT) — I_h ✅ —
T4 Analiza spektralna atraktorów quasi-periodycznych 💡 Średni
T5 Klasyfikacja 7 niezmienników pod A₅ vs I_h ✅ (22 vs 7) —
T6 Związek z P₀-Flow T_a/T_b na ikosaedrze 💡 Wysoki
T7 Rozszerzenie R4 na R12 (12 sąsiadów) 💡 Średni
T8 Test niezmienniczości trybów pod innymi x0 ✅ —
T9 Powiązanie z 7-wymiarową przestrzenią niezmienników 💡 Niski
T10 Test na większym klastrze (N=7 powłok) 💡 Średni
T11 Interpretacja fizyczna 22 trybów 💡 Wysoki
T12 Stabilność 15 chiralnych na większym klastrze 💡 Średni
T13 Czy istnieje G z Hom_G(Sym²V_cyc, V_cyc) = 0 na ikosaedrze? 💡 Wysoki
T14 Postać funkcyjna ω(‖x‖_attr) 🔍 Wysoki
T15 Test skanu γ — czy ω/‖x‖ ≈ const również przy zmianie γ? 💡 Wysoki
T16(a) Algebra stopnia 4: 82 = 15 + 67 ✅ §5.5.7 —
T16(b) Czy wykładnik plateau ~ ‖T‖^n zależy od stopnia? 💡 Wysoki

12.2. Opis T11–T16

T11. 22 tryby dynamiczne odpowiadają potencjalnie 22 modom kolektywnym klastra Mackaya. Czy dominujący irrep jest skorelowany z typem modu? Test na N=13.

T12. Czy 15 chiralnych pozostaje niezależnych na większej powłoce (N=55, N=147)?

T13. Czy istnieje G ⊃ I_h, na której Hom_G(Sym²V_cyc, V_cyc) = 0? To naturalne uogólnienie Tw. A.

T14. Trzy fity (ω² ∝ ‖x‖, ω² ∝ ‖x‖², ω² ∝ ‖x‖+‖x‖²) dają R² ≈ 0.87 bez poprawy przy dodaniu parametru. Kandydat: ω = c·‖x‖, c różne dla różnych niezmienników.

T15. Czy ω = f(‖x‖) niezależnie od mechanizmu? Zmieniając γ (zamiast ε): jeśli ω/‖x‖ ≈ const wzdłuż γ — potwierdzenie. Test: k=5, ε = 20 stałe, γ ∈ {5, 10, 20, 40, 80}.

T16(a). ✅ Zamknięte w v0.2.4. dim Sym⁴(V_cyc)^{I_h} = 82 = 15 + 67. 15 to iloczyny znanych niezmienników kwadratowych, 67 to genuinie nowe (Claude, niezależna weryfikacja numeryczna).

T16(b). 💡 Nadal otwarte. Jeśli zbudujemy bazę niezmienników stopnia 4 i uruchomimy Φ_quartic (gradient sześcienny), czy plateau skaluje się jak ‖T‖^n z tym samym wykładnikiem n ≈ 4.5, czy z innym?

Kandydaci z „prawa stopnia":

· 2·(stopień−1) = 6
· stopień+1 = 5
· stopień·1.5 = 6

Jeśli wykładnik się zmienia — prawo zależy od stopnia. Jeśli nie — 4.5 jest uniwersalne.

Stan na 2026-09-18: Claude nie domknął T16(b) w swoim limicie czasowym (300s na wywołanie). Przy skróconych krokach (3000) układ nie zbiegł do plateau. Dostarczył gotowy skrypt e_tetra_08_quartic_scaling.py (logika poprawna), ale skrypt nie jest samodzielny — wymaga pliku core_reconstruction.py z setupem (ikosaedr, I_h, P_cyc, L_cyc, Ms_all, P_irrep). Trzeba dobudować setup w Colabie.

Uwaga o ograniczeniu: skrypt buduje tylko 3 nowe niezmienniki stopnia 4 przez find_new_quartic(3, seed=777). Dla fitu potęgowego potrzeba więcej punktów. Z bazy 67 niezmienników warto wybrać ≥ 10 reprezentatywnych.

Uwaga implementacyjna: Φ_quartic jest gradientem sześciennym (dla porównania Φ_cubic — kwadratowy). Dynamika może być sztywniejsza numerycznie. Rozważyć damping_order = 3 lub 5.

---

13. Status twierdzeń

Twierdzenie / wynik Status
Link ikosaedryczny = V_ρ (11) ⊕ V_cyc (19) ✅
V_cyc ≇ Λ²(V_ρ) na ikosaedrze (19 ≠ 55) ✅
V_cyc = T1g ⊕ T2g ⊕ G_g ⊕ G_u ⊕ H_u ✅
Sym²V_cyc → 24 kanałów I_h ✅
Λ²V_cyc → 30 kanałów I_h ✅
Sym³V_cyc ⊃ A_g^{I_h} z krotnością 7 ✅
Sym³V_cyc ⊃ A_g^{A₅} z krotnością 22 ✅
Chiralne = 22 − 7 = 15 ✅
Sym⁴V_cyc ⊃ A_g^{I_h} z krotnością 82 ✅ §5.5.7
82 = 15 + 67 (iloczyny + genuinie nowe) ✅ §5.5.7
Φ_30 (elementwise) = 0 ✅
Φ_cross = 0 ✅
Φ_D niezerowa, ale nie-eq ✅
Φ_cubic G-ekwivariantna ✅
Φ_quartic G-ekwivariantna (eq-err = 6.5e-16) ✅ §7.5
7 różnych atraktorów I_h 🔍
15 różnych atraktorów chiralnych 🔍
22 tryby niezależne (chamfer > 0.4) 🔍
Nowy kanał T1g (c3, c10) 🔍
Blowup realny (T_c zbiega z dt→0) ✅
FCC ≠ Mackay (topologicznie) ✅
Brak SSB I_h → A₅ (kowariancja po 120) 🔍
Korelacja ‖T‖ ↔ ω jest artefaktem k=5 (dla ω) ✅ §11.3
Korelacja ‖T‖ ↔ plateau jest realna (dla plateau) 🔍 §11.7, §11.8
Widmo L_cyc ma 5–6 unikatowych wartości ✅ §9.4.7
Hipoteza harmonicznej k=5 — sfalsyfikowana ❌ §11.6
ω/‖x‖ ≈ 0.55 stałe wzdłuż ε (k=5) 🔍 §11.6
k=5 i k=6 różne mechanizmy (dω/dε: 0.30 vs 0.10) 🔍 §9.3
Rodziny miękkie grupują po kanale, nie mechanizmie 🔍 §9.3
Plateau ~ ‖T‖^4.5 (n=11, dwie ścieżki) 🔍 §11.8
Odchylenie od plateau ~ ‖T‖^n zależy od kierunku 🔍 §11.8
LIGHT: 3D NIE emerguje z propagacji ❌
Mechanizm VII na K₄ ❌
Mechanizm VII na ikosaedrze 🔍 aktywny

---

14. Rekomendacje

14.1. Do włączenia do PILLARS-TABLE

P₀-TETRA-20 jako kandydat na filar/podprojekt łączący P₀-Defect, P₀-Flow, P₀-Relacje.

14.2. Do P₀-Experiments

· E-TETRA-01…09 (jak w v0.2.3)
· E-TETRA-10: Interpolacje niezmienników — plateau ~ ‖T‖^4.5
· E-TETRA-11: Algebra stopnia 4 — 82 = 15 + 67
· E-TETRA-12: (planowany) Dynamika stopnia 4 — wykładnik plateau ~ ‖T‖^n

14.3. Do P₀-Defect v0.9

Dodać §12I — Przypadek niezupełny: ikosaedr.

14.4. Do P₀-Flow v0.6

Dodać §12.2a — Ikosaedr jako czwarty obiekt.

14.5. Do P₀-Algebra v0.4.1

Trzy dopiski (klasyfikacja dynamiczna widma, struktura sprzężeń, algebra obserwowalności) + nowy:

4. Algebra stopnia 4. Dodać do §7 jako kontrast dla stopnia 3: dim Sym⁴(V_cyc)^{I_h} = 82 (15 trywialnych + 67 nowych). Pokazuje nieliniowy wzrost wymiaru przestrzeni niezmienników z stopniem.

14.6. Kolejne kroki badawcze

Priorytet 1: T16(b) — dynamika stopnia 4 z Φ_quartic. Wymaga samodzielnego setupu + bazy ≥ 10 niezmienników stopnia 4.

Priorytet 2: T15 — test γ.

Priorytet 3: T14 — gęsty skan ‖x‖.

Priorytet 4: T11 — prawdziwy klaster Mackaya.

---

15. Historia

Data Zmiana
2026-09-15 Analiza notatnika światło
2026-09-16 TETRA-20 v0.1: budowa sieci, Hodge, I_h, Sym²V_cyc
2026-09-16 Konstrukcje Φ; Φ_cubic
2026-09-17 Baza 7 niezmienników → 7 atraktorów
2026-09-18 v0.2 — rozszerzenie A₅: 15 chiralnych
2026-09-18 v0.2.1 — FFT chiralnych, r=0.932
2026-09-18 v0.2.2 — skan ε; hipoteza harmonicznej sfalsyfikowana
2026-09-18 v0.2.3 — klaryfikacja ω vs plateau; plateau ~ ‖T‖^4.5
2026-09-18 v0.2.4 — algebra stopnia 4 (82=15+67); niezależne potwierdzenie 22/7/15; skrypt quartic zweryfikowany

---

16. Zasada końcowa

\boxed{\text{Relacja na ikosaedrze ma 22-wymiarową przestrzeń trybów nieliniowych.}}

W przeciwieństwie do K₄ (gdzie Tw. A blokuje mechanizm VII), ikosaedr ma:

· 5 nieprzywiedlnych reprezentacji w V_cyc
· 24 kanały symetryczne + 30 antysymetrycznych (dla I_h)
· 22 niezależne niezmienniki kubiczne (7 I_h + 15 chiralnych)
· 67 genuinie nowych niezmienników stopnia 4
· 22 różne atraktory o wysokiej stabilności
· Widmo L_cyc o 5–6 unikatowych wartościach

Zasada metodologiczna v0.2. Wszelkie korelacje między miarami niezmienników wymagają testu bez outlierów.

Zasada pełnej grupy (v0.2.1). Trzy razy w tej sesji pojedynczy punkt sugerował zjawisko, które znikało przy pełnym teście. Zasada: żadna kowariancja ani korelacja na skończonej próbce nie jest ustalona, dopóki nie zostanie sprawdzona bez outlierów i po pełnej grupie symetrii.

Zasada skalowania amplitudowego (v0.2.2). Częstotliwość oscylacji atraktora zależy tylko od amplitudy ‖x‖. ω/‖x‖ ≈ 0.55 dla k=5.

Zasada rozróżnienia zmiennych zależnych (v0.2.3). W analizie korelacji z ‖T‖ trzeba jawnie odróżnić ω (częstość), plateau (amplituda atraktora), próg (energia startowa). Trzy różne zmienne, trzy różne historie.

Zasada niezależnej implementacji (v0.2.4). Trzy wyniki liczbowe w tej sesji zostały niezależnie potwierdzone przez dwie różne implementacje: (1) 22/7/15 (rachunek charakterów vs sumowanie po A₅); (2) plateau ~ ‖T‖^n (dwie ścieżki interpolacji); (3) kowariancja po I_h (inwersja pojedyncza vs pełna grupa). Zasada: żaden wynik liczbowy nie jest ustalony, dopóki nie zostanie odtworzony inną metodą.

Pytanie końcowe: czy te 22 tryby odpowiadają 22 różnym „sposobom" organizacji relacji? To otwiera nowy kierunek badawczy dla P₀ — ikosaedryczną teorię relacji, obok (nie zamiast) teorii K₄.

---

P₀-TETRA-20 v0.2.4. Podsumowanie wątku badawczego 2026-09-15/18. Wyniki wymagają niezależnej replikacji. 