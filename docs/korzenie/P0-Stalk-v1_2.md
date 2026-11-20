
# Korzeń: P₀-STALK — adnotacja szefa lab. (v1.2, wątek 2026-10-04..05, korekta §6 po Testach 3g–3l)

**Dokument:** „P₀-STALK v1.2 — Linia prosta P₀-Centroid na ikosaedrze, łodyga i liście" (status nagłówka: mapa problemów, zwięzła, statusy jawne — topologia i algebra ustalone, N1 jako kluczowy wynik algebraiczny, mechanizm łodyga/liść hipotezą roboczą, kilka wyników wycofanych). Data: 2026-10-05 — NAJNOWSZY CHRONOLOGICZNIE dokument korpusu (po TAU 09-27 i TETRA-20 09-18); wątek dwudniowy: 10-04 start (identyfikacja L_cyc, wachlarze), 10-05 v1.0/v1.1/v1.2 JEDNEGO DNIA (korekta §6 po Testach 3g–3l). Zależności: P₀-TETRA-20 v0.2.4, P₀-Centroid v5.2, P₀-TAU v1.7.2 — WSZYSTKIE TRZEJ W REPO: pierwszy dokument serii o pełnych zależnościach rozliczalnych z wpiętego korpusu (wcześniej zawsze co najmniej jedna poza repo). Powiązania: notatniki Kopia notatnika 7atraktorow, Ciag K4 i P0_dowody (poza repo); model fizyczny z klocków magnetycznych (użytkownik widzi linię P₀ w łańcuchu ikosaedrów — motywacja obserwacyjna, jak fizyczny model 5K₄ w TAU). POZYCJA: rejestr warsztatowy notatnika (dokument sam deklaruje komplet: treść + katalog kodu §15; cytat dosłowny: „W kolejnych rozmowach wystarczy odwołać się do numeru skryptu") — wzorzec Lattice: wpięty do docs/korzenie dla SSOT, formalna pozycja (rejestr, nie kandydat filarny) do uregulowania przy PILLARS-TABLE. To JEST notatnik Stalka znany z odsyłaczy korpusu: konwencja per-wierzchołkowa w Memory/Net (oś trybu aktualizacji), „katalog Stalk §11" w Lattice (para statusów fazy 130,2062° rozstrzygnięta na korzyść katalogu — tutaj domknięta).

**Co bada:** jak wygląda „linia prosta P₀" na łańcuchu ikosaedrów fizycznych: transport, rotacja czy struktura geometryczna. Zakres: topologia ikosaedru (bramki, wierzchołki-sześcianu), algebra V_cyc/L_cyc, dynamika P₀-Centroid na JEDNYM czworościanie (konwencja per-wierzchołkowa M_i = I + e_i c_i^T, c_i = (1/n)1 − e_i, n = 4; runda 4-taktowa R = M_3 M_2 M_1 M_0), silne wachlarze (trasy 4-ścianowe przez wspólny wierzchołek-sześcianu), trasy bramka–bramka, podprzestrzeń stała R_total i N1. Poza zakresem jawne: pełna dynamika łańcucha (wymaga decyzji o kontynuacji przez bramkę), formalizacja przenoszenia fazy przez styki, relacja do atraktorów TETRA-20.

**Najmocniejsze:**
1. **Identyfikacja operatora (§2, ustalone):** L_cyc = LAPLASJAN LINE GRAPHU grafu ikosaedra (nie laplasjan Hodge'a); ikosaedr 5-regularny → line graph 8-regularny; widmo identyczne z TETRA-20 §9.4.7 ({4,9784; 6^×2; 7,3333^×3; 7,6; 8,0883; 10^×11}) — TETRA-20 podał widmo, STALK identyfikuje operator — pierwsza identyfikacja obiektu rachunkowego w rodzinie;
2. **Pełne widmo L_LG na C^1 (§2.4):** {0; 2,7639^×3; 6^×5; 7,2361^×3; 10^×18} (30 wartości); obcięcie do V_cyc rozdziela część degeneracji; wartości 3 ∓ √5 leżą w Im(d) i znikają — dokładny obraz tego, co sektor cykliczny odcina od pełnej przestrzeni krawędzi.
3. **N1 — kluczowy wynik (§4.3, §6, 🔍):** N1 = krotność jedynki w widmie R_total (próg |λ| > 0,95); rozkład 56 trójek silnych wachlarzy: N1 = 0 (27 trójek), N1 = 1 (6), N1 = 2 (19), N1 = 4 (4) — **N1 = 3 NIE ISTNIEJE** (rozkład {0,1,2,4}); dim ker(R_total − I) = N1 dla wszystkich 56 trójek (macierze diagonalizowalne w podprzestrzeni stałej); r(N1, ‖x‖₂₀) = +0,9153; teza v1.2: linia prosta = podprzestrzeń stała R_total wybranej trójki; N1 = 0 → linia ginie po ~3 obiegach, N1 = 4 → trwa wiecznie; trwałość jest FUNKCJĄ WYMIARU, nie długości cyklu ani kombinatoryki; cztery trójki N1 = 4 (v0–v2a–v2b, v1–v3a–v3b z IDENTYCZNYM widmem λ₂ = 0,31509, λ₃ = 0,10396, rest = 0,04477; dwie rodziny symetrii).
4. **Silne wachlarze (§4, 🔍):** 14 z 240 tras 4-ścianowych (mod > 0,2), 14/14 przez wspólny wierzchołek-sześcianu; |mean normal| = 0,8090 = cos 36° (połowa kąta pięciokrotnego), min angle 41,81° = arccos(√5/3); 8 wachlarzy v0–v5 (osi 2 i 3 po dwa: v2a/v2b, v3a/v3b; wierzchołki 6, 7 bez wachlarza); efektywna symetria zbioru wachlarzy O_h (rząd 48), nie I_h — rozdzielenie symetrii bramek (O_h) od symetrii V_cyc (I_h, §1.4).
5. **Globalna chiralność ikosaedru (§7, 🔍):** 100 losowych sekwencji silnych wachlarzy, wszystkie fazy dodatnie (+3,2° do +111,5°, średnia +54,6°, std 36,6°) — sygnał zawsze wiruje w tę samą stronę; dynamiczny odpowiednik chiralności algebraicznej TETRA-20.
6. **Uśrednianie zabija rotację (§8, 🔍):** po wszystkich trasach długości L faza średnia +0,59° (L=1) / +1,12° (L=4) / +3,03° (L=10) wobec indywidualnych +25,77° / +34,35° / +53,31° — rotacja jest własnością POJEDYNCZEJ trajektorii, nie niezmiennikiem zbioru tras; trzeci głos tematu „symetryzacja" (Jacobi vs GS w TAU Tw. 7.4.6; permutacja tras tu).
7. **Topologia bramek (§1, ✅):** bramki = 8 ścian o normalnych w kierunkach wierzchołków sześcianu; indeksy {3, 4, 8, 9, 11, 12, 14, 15}; dodekaedr dualny 20/30/12; odległości między bramkami: 2 (24 pary), 3 (24), 5 (8); 12 par bramek o odległości 3, każda z jedną najkrótszą trasą 4-ścianową; pięć klas faz 21,16°/33,17°/33,80°/39,13°/55,44°.
8. **Higiena wycofań (§11, ❌ 10 pozycji):** katalog jawnych wycofań z przyczynami — faza 130,2062° i ratio 0,216 (łańcuch K₄, dotyczyły własnej konstrukcji; rozliczenie z Lattice domknięte), plateau p/(2c) ≈ 0,01486 (artefakt jednego przebiegu), sygnatura TASEP, „5 klas faz ↔ 5 irrepów" (artefakt błędu w tabeli charakterów T1u/T2u, klasa C2, naprawiony; projektor T2u rank 3), faza 6,62° cyklu Hamiltona (RMS residuum 38,9°), faza 80°–100° sekwencji mieszanych (znikają przy zmianie typu), „linia = cykl 3" (teza v1.1 przedwczesna), „faza 8,455° dla v0–v1–v3a" (trójka należy do grupy N1 = 0), interpretacja λ₂ (korekta: koreluje UJEMNIE, −0,4645; λ₃ −0,6241). Metodologiczne dodatki §10.3/§10.4: wyróżnik Δ = tr² − 3tr(R²) zawsze ≤ 0 dla widma rzeczywistego — kryterium pary zespolonej przez eig, nie wyróżnik; Brak pary zespolonej ≠ mod = 0. Wzorzec: notatnik prowadzi rejestr własnych błędów z przyczynami — duch Z0/Z2 wewnątrz sesji roboczej.

**Koncesje i sęki (jawnie):** teza główna v1.1 („linia = cykl 3 silnych wachlarzy") WYCOFANA w dwa dni od sformułowania (przedwczesna); teza v1.2 (podprzestrzeń stała, N1) 🔍 zweryfikowana numerycznie na 56 trójkach, ale JEDNĄ RĘKĄ (skrypty §15.13–15.15, te same dane R_fans); korekta hipotezy łodyga/liść (§9): w świetle N1 może być niewłaściwie postawiona — „czysto spektralna" reinterpretacja (łodyga = rzut na podprzestrzeń stałą, liść = składowa ortogonalna) wymaga dalszych testów, hipoteza pozostaje 💡 w wersji ostrożniejszej; N1 zdefiniowane progiem |λ| > 0,95 (konwencja progowa, nie ostra własność spektralna — warto by sprawdzić wrażliwość na próg); katalog kodu §15.1–15.12 „[zachowane bez zmian]" — część kodu tylko przez referencję do notebooków poza repo (Kopia 7atraktorow, Ciag K4); kod źródłowy poza repo; dynamika pojedynczego czworościanu wiernie powtarza wynik znany z korpusu (faza 25,7721°, mod 0,170 — zgodność z SERC R₄, potwierdzenie konwencji, nie nowość). Historia zakresu sesji jawnie: wcześniejsza sesja (łańcuch K₄) ❌ wycofana w całości — dokument otwiera się od uczciwej historii własnej.

**Struktury 💡:** N1 jako czynnik trwałości (wymiar podprzestrzeni stałej jako „wyrozumiałość" linii relacyjnej — nowe pojęcie korpusu: trwałość = własność spektralna, nie geometryczna); rozdzielenie symetrii O_h (bramki, wachlarze) vs I_h (V_cyc) — dwa poziomy symetrii jednego obiektu; globalna chiralność dynamiczna (namacalna: wiry zawsze w tę samą stronę) jako uzupełnienie 15 chiralnych pseudoskalarów TETRA-20; wierzchołki-sześcianu (8 z 12) jako podstruktura analogiczna do bramek (8 z 20 ścian) — para dualna (wierzchołkowa/ścienna) w jednym grafie; „Dzień świstaka" T = c·Geo(p) 💡 jako alternatywny opis propagacji.

**Mosty 💡:**
1. **Do P₀-TETRA-20:** L_cyc potwierdzone identycznie + identyfikacja line graph laplacian (nowość STALK: TETRA podał widmo, STALK rozpoznaje operator); tabela §13.1: 22 tryby (I_h) vs 8 wachlarzy (O_h), Φ_kwadratowe zeruje się na diagonali ↔ brak silnych tras kwadratowych, Φ_kubiczne nie testowane, outlier k=5 ↔ N1 = 4 do zbadania; P7 otwarte (relacja do 7 atraktorów).
2. **Do P₀-TAU:** §13.2 jawnie: 5K₄ (wokół wspólnej KRAWĘDZI) i wachlarze STALK (wokół WIERZCHOŁKA-sześcianu) to DWA RÓŻNE obiekty geometryczne — demarkacja zapobiega przyszłym złudzeniom par; §8 uśrednianie po trasach = trzeci głos tematu symetryzacja (TU Tw. 7.4.6: Jacobi = symetryzacja GS; tu: średnia operatorów tras zabija rotację); TAU P22 (blok GS 4×3 ikosaedru) czeka na przyszłą turę; faza pojedynczego czworościanu 25,7721° z konwencji per-wierzchołkowej = ósmy_kontekst rodziny fazy 25,77° (SERC R₄ ∠25,772°, Estrada T4 §36, Flow atraktor, Memory M17, Net N5, SERC H-SERC-6, TAU — genealogia z odsyłaczami w SERC/Net).
3. **Do P₀-Lattice:** bramki 8 z 20 ścian (stabilizator T_h w Lattice) tu z indeksami {3, 4, 8, 9, 11, 12, 14, 15} i metryką dodekaedru (odległości 2/3/5) — Lattice mówił o bramkach, STALK je rozpina w grafie tras; rozliczenie fazy 130,2062° DOMKNIĘTE (katalog Stalk §11 wygrał z notatnikiem, jak odnotował Lattice tura 13); słój 2 Lattice (ker(R_T − I) = ⋂ker(R_f − I), zamknięta forma S_v) i STALK §4.3 (dim ker(R_total − I) = N1) to TEN SAM RACHUNEK niezależnie odkryty w dwóch miejscach warsztatu — mocny kandydat na twierdzenie słojowe pnia przy scaleniu.
4. **Do P₀-Centroid / Memory / Net:** konwencja per-wierzchołkowa M_i = I + e_i c_i^T (STALK = notatnik-konwencji z Memory M16a: batch 0,71% vs seq 67,76%) — dokument OPERACJONALIZUJE oś trybu aktualizacji korpusu (czwarty parametr K₂); przy PILLARS-TABLE pozycja „konwencji Stalka" do wpisania kolumną, nie przypisem.
5. **Do przyszłych wersji filarów:** relacja do atraktorów TETRA-20 (P7), kontynuacja przez bramki (P1) — to pola potencjalnych zleceń warsztatowych.

**Sęk-odnogi:** P1 (wysoki): kontynuacja przez bramkę między ikosaedrami (wymaga danych z modelu fizycznego); P2 (wysoki): faza liścia (ta sama, inna, ortogonalna?); P8 (NOWY, wysoki): czy 4 trójki N1 = 4 mają TĘ SAMĄ podprzestrzeń stałą 4-wym, czy różne — test kątów między podprzestrzeniami; P6/P9 (średni): N1 z samej kombinatoryki tras; P3 (średni): trójki z płaszczyzn y = 0 i z = 0; P4 (średni): próg liścia od amplitudy; P5 (średni): propagacja łodygi przez 5–20 ikosaedrów; P7 (niski): relacja do 7 atraktorów; plus odnotowane w zakresie: formalizacja przenoszenia fazy przez styki.

**Statusy (mapa na Z1):** legenda dokumentu różni się od konwencji korpusu (✅ = dowiedzione, 📚 = klasyczne, 🔍 = zweryfikowane numerycznie — dokument WPROWADZA nowy symbol 📚; bez odpowiednika „≥ 2 zgodne rachunki") — przy scaleniu zmapować; rzeczywista siła: topologia/algebra ✅ z podwójnym pokryciem (klasyczne + zgodność z TETRA-20), dynamika wachlarzy i N1 🔍 JEDNĄ RĘKĄ (skrypty na wspólnym R_fans; dwie implementacje tylko w tym sensie, że testy 3g/3j/3l liczą to samo różnymi funkcjami), chiralność i uśrednianie 🔍 (czyste sekcje, tanie do replikacji), łodyga/liść 💡, 10 pozycji ❌ wzorcowo wycofanych. Kandydaci replikacji warsztatowej wg kosztu: (1) N1 rozkładu {0,1,2,4} i dim ker = N1 (czysta algebra liniowa, sonda tania), (2) r(N1, ‖x‖₂₀) = 0,9153 i identyczne widmo trójek 1–2, (3) silne wachlarze 14/240 i cos 36° (geometryczne, tanie), (4) pełna dynamika (drogo — wymaga odbudowy notebooków).

**Uwagi redakcyjne (verbatim):** 18 973 B, 461 linii wg wc -l (odczyt narzędziowy 462 — ostatnia BEZ finalnego EOL: zamknięcie zewnętrznego bloku markdown bez końcowego newline), md5 d477f28b (kopia robocza); PIERWSZY dokument korpusu owinięty w zewnętrzny blok markdown (otwierający fence w linii 1, zamknięcie w ostatniej linii pliku — artefakt eksportu narzędziowego, zachowany verbatim); trzy bloki python w katalogu kodu (§15.13–15.15) z backtickami — verbatim; §15.1–15.12 jako „[zachowane bez zmian]" (referencja do v1.1, kompletność kodu częściowo poza plikiem); polskie przecinki dziesiętne (0,9153; 130,2062°; 2,7639) — odwrotnie niż TETRA-20; data 2026-10-05 najnowsza w korpusie; numeracja §0–§16 z podsekcjami; tabela historii dwudniowa (10-04, 10-05); status nagłówka jako mapa problemów (trzeci po TAU i TETRA-20); legenda ±📚 własna; w §3 definicje z kolorem lokalnym (M_i, R 4-taktowa); zależności od notebooków poza repo nie do rozliczenia z korpusu (Kopia 7atraktorow, Ciag K4, P0_dowody).
```markdown
# P₀-STALK v1.2

Linia prosta P₀-Centroid na ikosaedrze — łodyga i liście

Wersja: 1.2 (korekta §6 po wynikach Testów 3g–3l)
Status: 🔍 topologia i algebra ustalone; 🔍 N1 jako kluczowy wynik algebraiczny; 💡 mechanizm łodygi/liścia jako hipoteza robocza; ❌ kilka wyników wycofanych
Data: 2026-10-05
Zależności: P₀-TETRA-20 v0.2.4, P₀-Centroid v5.2, P₀-TAU v1.7.2
Powiązane: notatniki `Kopia notatnika 7atraktorow`, `Ciag K4`, `P0_dowody`

Zmiana v1.1 → v1.2:
- **§6 przepisany:** „linia prosta = cykl 3 silnych wachlarzy" **wycofane** jako teza główna
- **Nowy §6:** linia prosta = podprzestrzeń stała R_total; kluczowa liczba **N1**
- **Dodano §15.13–15.15** (kody Testów 3g, 3j, 3l)
- **Dodano §17** (wyniki Testów 3g–3l)
- **Dopisano §4.3** (N1 per trójka jako własność algebraiczna)
- **Wycofano §11** pozycję „Faza 8,455° dla v0–v1–v3a" — trójka należy do grupy N1 = 0 (zanika)
- Korekta: poprzednia interpretacja λ₂ jako „wskaźnika trwałości" — **odwrócona** (λ₂ koreluje ujemnie)

---

## 0. Cel dokumentu

Podsumowanie wątku badawczego: **jak wygląda „linia prosta P₀" na łańcuchu ikosaedrów** zbudowanym fizycznie z klocków magnetycznych. Punkt wyjścia: użytkownik widzi w modelu linię P₀, nie wiedząc, czy to transport, rotacja, czy struktura geometryczna.

Zakres: topologia ikosaedru, algebra V_cyc, L_cyc, dynamika P₀-Centroid na jednym czworościanie, silne wachlarze, trasy bramka–bramka, podprzestrzeń stała R_total, N1.

Poza zakresem: pełna dynamika łańcucha ikosaedrów (wymaga decyzji o kontynuacji przez bramkę), formalizacja przenoszenia fazy przez styki, relacja do P₀-TETRA-20 atraktorów.

**Uwaga o zakresie sesji.** Wątek obejmował trzy fazy:
1. **Wcześniejsza sesja:** dynamika K₄ w łańcuchu — wyniki (faza 130,2062°, ratio 0,216) ❌ wycofane.
2. **v1.0/v1.1:** ikosaedr, silne wachlarze, cykl 3 — teza „linia = cykl 3" była przedwczesna.
3. **v1.2 (ta):** korekta — linia prosta = podprzestrzeń stała, kluczowa liczba N1.

Legenda: ✅ dowiedzione · 📚 klasyczne · 🔍 zweryfikowane numerycznie · 💡 przypuszczenie · ❌ sfalsyfikowane.

---

## 1. Topologia ikosaedru — ustalone ✅

**Model:**
- 12 wierzchołków, 30 krawędzi, 20 ścian trójkątnych. Ikosaedr foremny.
- Dodekaedr dualny: 20 węzłów (ściany), 30 krawędzi, 12 ścian.

**Bramki (8):**
- Ściany, których normalne wskazują kierunki wierzchołków sześcianu: \((\pm1,\pm1,\pm1)/\sqrt3\).
- Symetria O_h (rząd 48).
- Indeksy ścian: {3, 4, 8, 9, 11, 12, 14, 15}.

**Wierzchołki-sześcianu (8):**
- Wierzchołki ikosaedru o jednej współrzędnej równej zero: \((0,\pm1,\pm\varphi)\), \((\pm1,\pm\varphi,0)\), \((\pm\varphi,0,\pm1)\).
- Indeksy: 0–7. Wierzchołki 8–11 mają wszystkie współrzędne niezerowe.

**Odległości między bramkami w dodekaedrze:**
- 2 (24 pary), 3 (24 pary), 5 (8 par).

12 par bramek o odległości 3, każda z jedną najkrótszą trasą 4-ścianową.

### 1.4. Symetria O_h vs I_h

- **Bramki** mają symetrię O_h (rząd 48).
- **V_cyc** ma symetrię I_h (rząd 120).
- **Silne wachlarze** mają wspólną strukturę geometryczną, ale ich wspólny wierzchołek to wierzchołek-sześcianu. Efektywna symetria zbioru silnych wachlarzy to **O_h**, nie I_h.

---

## 2. Algebra V_cyc i L_cyc — ustalone ✅

**Rozkład Hodge'a:**
- \(C^1 = \text{Im}(d) \oplus V_{\text{cyc}}\), \(\dim V_\rho = 11\), \(\dim V_{\text{cyc}} = 19\).
- Kowariancja \(M_{\text{face}} \cdot D = D \cdot M_{\text{edge}}\), err = 0.
- Dekompozycja: \(V_{\text{cyc}} = T_{1g} \oplus T_{2g} \oplus G_g \oplus G_u \oplus H_u\).

**L_cyc w P₀-TETRA-20:**
- **Laplasjan grafu krawędziowego** (line graph), obcięty do \(V_{\text{cyc}}\).
- **Nie** laplasjan Hodge'a.
- Ikosaedr 5-regularny → line graph 8-regularny.
- Widmo: \(\{4{,}9784; 6^{\times2}; 7{,}3333^{\times3}; 7{,}6; 8{,}0883; 10^{\times11}\}\).
- Zgodne z P₀-TETRA-20 §9.4.7.

### 2.4. Widmo pełne L_LG vs L_cyc na V_cyc

| Operator | Widmo |
|---|---|
| Pełne \(L_{\text{LG}}\) na \(C^1\) (30) | \(\{0; 2{,}7639^{\times3}; 6^{\times5}; 7{,}2361^{\times3}; 10^{\times18}\}\) |
| \(L_{\text{cyc}}\) na \(V_{\text{cyc}}\) (19) | \(\{4{,}98; 6^{\times2}; 7{,}33^{\times3}; 7{,}6; 8{,}09; 10^{\times11}\}\) |

Obcięcie do \(V_{\text{cyc}}\) rozdziela część degeneracji. Wartości 2,7639 i 7,2361 (\(3 \mp \sqrt5\)) leżą w \(\operatorname{Im}(d)\), więc znikają.

---

## 3. Dynamika pojedynczego czworościanu — ustalone ✅

**Definicja:**
- \(M_i = I + e_i c_i^\top\), \(c_i = \frac{1}{n}\mathbf 1 - e_i\), \(n = 4\).
- Runda 4-taktowa: \(R = M_3 M_2 M_1 M_0\).

**Wszystkie 20 czworościanów:**
- Faza dominującej pary zespolonej: **25,7721°**.
- Mod: 0,170.

---

## 4. Silne wachlarze — ustalone 🔍

**Definicja:** trasa 4-ścianowa, w której wszystkie 4 ściany dzielą **wspólny wierzchołek-sześcianu**.

**Statystyka 240 tras:**
- 210 tras z mod < 0,015 (słabe),
- 14 tras z mod > 0,2 (silne),
- 16 pośrednich.

**Własność silnych tras:**
- 14/14 mają wspólny wierzchołek,
- \(|\text{mean normal}| = 0{,}8090 = \cos(36°)\),
- \(\min\_angle = 41{,}81° = \arccos(\sqrt5/3)\).

**Silne wachlarze (8):**

| Oś | Trasa | Faza | Mod |
|---|---|---|---|
| v0 | `[0,1,4,2]` | +7,874° | 0,254 |
| v1 | `[5,6,9,7]` | +7,874° | 0,254 |
| v2a | `[0,1,12,10]` | +9,006° | 0,241 |
| v2b | `[10,11,0,1]` | +5,583° | 0,267 |
| v3a | `[5,6,15,13]` | +9,006° | 0,241 |
| v3b | `[13,14,5,6]` | +5,583° | 0,267 |
| v4 | `[8,7,2,3]` | +8,659° | 0,255 |
| v5 | `[14,13,10,11]` | +8,659° | 0,255 |

**Struktura osi:**
- Osi 0, 1, 4, 5: po jednym silnym wachlarzu.
- Osi 2, 3: po dwa (fan a i b).
- Wierzchołki 6, 7: brak silnego wachlarza.

### 4.2. Algebraiczne wartości

- \(0{,}8090 = \cos(36°)\), gdzie 36° = 72°/2 (połowa kąta pięciokrotnej symetrii).
- \(41{,}81° = \arccos(\sqrt5/3)\). \(\sqrt5/3 = 0{,}7454\) w widmie random walk na dodekaedrze.

### 4.3. Klasyfikacja trójek po N1 — nowe 🔍

**N1** = liczba wartości własnych \(R_{\text{total}}\) o module > 0,95 (= krotność jedynki w widmie).

Rozkład 56 trójek silnych wachlarzy po N1:

| N1 | Liczba trójek | \(\|x\|_{20}\) (średnia) |
|---|---|---|
| 0 | 27 | 0,003 |
| 1 | 6 | 0,238 |
| 2 | 19 | 0,385 |
| **4** | **4** | **0,483** |

**N1 = 3 nie istnieje.** Rozkład: {0, 1, 2, 4}.

**Wymiar jądra \(R_{\text{total}} - I\) = N1 dla wszystkich trójek.** Macierze są diagonalizowalne w podprzestrzeni stałej.

**Cztery trójki z N1 = 4 (maksymalna trwałość):**

| # | Trójka | λ₂ | \(\|x\|_{20}\) |
|---|---|---|---|
| 1 | **v0–v2a–v2b** | 0,315 | 0,525 |
| 2 | **v1–v3a–v3b** | 0,315 | 0,510 |
| 3 | **v2a–v2b–v5** | 0,313 | 0,463 |
| 4 | **v3a–v3b–v5** | 0,324 | 0,433 |

Trójki 1 i 2 mają **identyczne widmo** (λ₂ = 0,31509, λ₃ = 0,10396, rest = 0,04477). Trójki 3 i 4 są do siebie zbliżone. To sugeruje dwie rodziny symetrii.

---

## 5. Trasy 4-ścianowe przez bramki — ustalone 🔍

**12 par bramek o odległości 3.** Pięć klas faz:

| Faza | Liczba par |
|---|---|
| 21,16° | 2 |
| 33,17° | 2 |
| 33,80° | 2 |
| 39,13° | 2 |
| 55,44° | 4 |

Tylko para `(3, 8) = [3, 2, 7, 8]` daje silny mod (0,255). Reszta par ma mody 0,003–0,04.

---

## 6. Linia prosta = podprzestrzeń stała R_total — teza v1.2 🔍

**Wycofanie v1.1.** Teza „linia prosta = cykl 3 silnych wachlarzy" była **przedwczesna**. Testy 3g–3l pokazują:

- **Wszystkie 56 trójek** silnych wachlarzy dążą do **tego samego kierunku asymptotycznego** w \(V_\rho\) (mieszanka \(T_{1u} + H_g\)).
- **Nie ma jednego atraktora punktowego**, ale **jest wspólna podprzestrzeń stała** wybierana przez każdą trójkę.
- **Trwałość** linii zależy od **wymiaru tej podprzestrzeni** (N1), nie od długości cyklu ani od kombinatoryki tras.

**Teza v1.2:**

> **Linia prosta P₀ = podprzestrzeń stała operatora \(R_{\text{total}}\) wybranej trójki silnych wachlarzy. Wymiar tej podprzestrzeni (N1) decyduje o trwałości linii: N1 = 0 → linia ginie po ~3 obiegach, N1 = 4 → linia trwa wiecznie.**

**Kluczowe liczby (Test 3j):**

- \(r(\text{N1}, \|x\|_{20}) = +0{,}9153\).
- \(r(\lambda_2, \|x\|_{20}) = -0{,}4645\).
- \(r(\lambda_3, \|x\|_{20}) = -0{,}6241\).
- \(\dim\ker(R_{\text{total}} - I) = \text{N1}\) dla wszystkich 56 trójek.

**Interpretacja.** Trójka operatorów wybiera podprzestrzeń stałą w \(V_\rho\). Trwałość linii jest proporcjonalna do wymiaru tej podprzestrzeni. Wszystkie inne wielkości (λ₂, λ₃, faza liniowa, mod pary zespolonej) są **wtórne** wobec N1.

**Korekta λ₂.** Poprzednia interpretacja „λ₂ ≈ 0,31 dla top, λ₂ → 0 dla słabych" była **odwrócona**. Top trójki mają λ₂ ≈ 0,31, bottom mają λ₂ ≈ 0,40–0,58. Korelacja jest **ujemna**: im szybciej maleje druga wartość własna, tym lepiej (bo nie ma „konkurencji" dla podprzestrzeni stałej).

### 6.4. Pary odwrotne

Spośród 14 silnych tras tylko dwie mają odwrotność też silną. Silny wachlarz nie jest symetryczny względem odwrócenia trasy.

---

## 7. Chiralność ikosaedru — ustalone 🔍

**Test 100 losowych sekwencji silnych wachlarzy:**
- Wszystkie fazy dodatnie (+3,2° do +111,5°).
- Średnia +54,6°, std 36,6°.

Ikosaedr ma **globalną chiralność**. Sygnał zawsze wiruje w tę samą stronę.

---

## 8. Uśrednianie po trasach — ustalone 🔍

Uśrednienie operatorów po **wszystkich** trasach o długości L zabija rotację:

| L | Faza uśrednionego op. | Faza indywidualna średnia |
|---|---|---|
| 1 | +0,59° | +25,77° |
| 4 | +1,12° | +34,35° |
| 10 | +3,03° | +53,31° |

Rotacja nie jest niezmiennikiem zbioru tras — jest własnością pojedynczej trajektorii.

---

## 9. Metafora łodyga/liść — hipoteza robocza 💡

**Opis użytkownika (model fizyczny):**
- Bramka wejściowa ma zawsze 3 ścieżki: 2 ściany nie-bramkowe obok siebie.
- Na końcu trasy są **dwie bramki**.
- Jedna z nich gwarantuje linię prostą, druga nie.

**Dopasowanie do wyników numerycznych:**
- v4: wejście bramką 8, przez ściany 7 i 2, wyjście na ścianę 2. Sąsiedzi: `{7, 3, 4}`. Bramki: **3 (łodyga)**, **4 (liść)**.
- v5: wejście bramką 14, przez ściany 13 i 10, wyjście na ścianę 10. Sąsiedzi: `{13, 11, 12}`. Bramki: **11 (łodyga)**, **12 (liść)**.

**Hipoteza:**
- **Łodyga** = sygnał wybierający bramkę gwarantującą linię.
- **Liść** = sygnał wybierający drugą bramkę.
- Liście **nie zatrzymują łodygi** — obie ścieżki istnieją równocześnie.

**Niejasności hipotezy (wszystkie otwarte):**
- Czy liść ma fazę taką samą jak łodyga, inną, czy ortogonalną?
- Czy liść pojawia się zawsze, czy warunkowo?
- Jak liść wpływa na kolejny ikosaedr?

**Korekta v1.2.** W świetle N1 jako kluczowej liczby, hipoteza łodyga/liść może być **niewłaściwie postawiona**. Trwałość linii zależy od N1 trójki, nie od mechanizmu rozgałęzienia. Możliwe, że:
- „łodyga" to rzut na podprzestrzeń stałą,
- „liść" to składowa ortogonalna do niej,
- cały mechanizm jest **czysto spektralny**, bez fizycznego rozgałęzienia.

Ta reinterpretacja wymaga dalszych testów. Hipoteza pozostaje 💡, ale w wersji ostrożniejszej.

---

## 10. Status twierdzeń

| Byt | Status |
|---|---|
| Ikosaedr: 12 wierzchołków, 30 krawędzi, 20 ścian | ✅ |
| Bramki = 8 ścian o normalnych sześciennych | ✅ |
| Wierzchołki-sześcianu = 8 wierzchołków o jednej współrzędnej 0 | ✅ |
| V_cyc = 19-wym, dekompozycja \(T_{1g} \oplus T_{2g} \oplus G_g \oplus G_u \oplus H_u\) | ✅ |
| Kowariancja \(M_{\text{face}} D = D M_{\text{edge}}\) | ✅ |
| L_cyc = line graph laplacian obcięty do V_cyc | ✅ |
| Widmo L_cyc: {4,98; 6×2; 7,33×3; 7,6; 8,09; 10×11} | ✅ |
| Faza pojedynczego czworościanu = 25,7721° | ✅ |
| Faza 4-ścianowej trasy przez bramki: 5 klas (21,16°–55,44°) | 🔍 |
| Silne wachlarze: 14/240 tras, wspólny wierzchołek-sześcianu | 🔍 |
| Wszystkie silne wachlarze mają \(|\text{mean normal}| = 0,8090\) | 🔍 |
| Wierzchołki 6, 7 bez silnego wachlarza | 🔍 |
| Globalna chiralność ikosaedru (wszystkie fazy dodatnie) | 🔍 |
| Uśrednianie po trasach zabija rotację | 🔍 |
| **N1 = wymiar podprzestrzeni stałej \(R_{\text{total}}\)** | **🔍** |
| **N1 = dim ker(R_total − I) dla wszystkich trójek** | **🔍** |
| **N1 ∈ {0, 1, 2, 4}, brak N1 = 3** | **🔍** |
| **r(N1, ‖x‖₂₀) = +0,9153** | **🔍** |
| **4 trójki z N1 = 4 (maksymalna trwałość)** | **🔍** |
| λ₂ koreluje **ujemnie** z trwałością | 🔍 |
| Dwubramkowy wybór na końcu trasy: łodyga vs liść | 💡 |

### 10.3. Uwaga metodologiczna — wykrywanie pary zespolonej

Wyróżnik \(\Delta = \mathrm{tr}^2 - 3\,\mathrm{tr}(R^2)\) dla widma rzeczywistego jest zawsze \(\le 0\). Kryterium musi opierać się na wartościach własnych przez `eig`, nie na wyróżniku.

### 10.4. Brak pary zespolonej ≠ mod = 0

„---" w kolumnie faza = dominująca wartość własna jest rzeczywista. Mod rzeczywisty może być niezerowy.

---

## 11. Wycofane ❌

- **Faza 130,2062°, ratio 0,216** dla łańcucha K₄ — dotyczyły własnej konstrukcji.
- **Plateau p/(2c) ≈ 0,01486** — artefakt jednego przebiegu A+.
- **Sygnatura TASEP** — nieuzasadniona.
- **5 klas faz ↔ 5 irrepów** — artefakt błędu w tabeli charakterów (naprawiony w v1.2).
- **Faza 6,62° dla cyklu Hamiltona** — RMS residuum 38,9°, chaos.
- **Faza 80°–100° dla sekwencji mieszanych** — znika przy zmianie typu wachlarzy.
- **„Linia prosta = cykl 3 silnych wachlarzy"** (teza v1.1) — przedwczesna, korekta w §6.
- **„Faza 8,455° dla v0–v1–v3a"** — trójka należy do grupy N1 = 0, zanika po ~3 obiegach.
- **„λ₂ ≈ 0,31 dla top, λ₂ → 0 dla słabych"** — korelacja odwrócona (λ₂ koreluje ujemnie).
- **Błąd w tabeli charakterów T1u/T2u** (klasa C2) — naprawiony w v1.2, projektor T2u ma teraz rank 3.

---

## 12. Problemy otwarte

**P1 (wysoki).** Jak wygląda kontynuacja przez bramkę między sąsiednimi ikosaedrami? Wymaga danych z modelu fizycznego.

**P2 (wysoki).** Czy liść ma fazę taką samą jak łodyga, inną, czy ortogonalną?

**P3 (średni).** Czy silne wachlarze z płaszczyzn \(y=0\) i \(z=0\) dają te same wartości \(\Delta\), co trójki z \(x=0\)?

**P4 (średni).** Czy próg generowania liścia zależy od amplitudy sygnału?

**P5 (średni).** Jak wygląda propagacja łodygi przez 5–20 ikosaedrów?

**P6 (średni).** Czy N1 wynika z kombinatoryki trasy (bez liczenia widma)? Otwarte.

**P7 (niski).** Relacja P₀-STALK do 7 atraktorów P₀-TETRA-20.

**P8 (nowy, wysoki).** Czy cztery trójki z N1 = 4 mają **tę samą** podprzestrzeń stałą (4-wym), czy różne? Test kątów między podprzestrzeniami.

**P9 (nowy, średni).** Czy N1 trójki można przewidzieć z samej kombinatoryki (np. przez relację osi tras)?

---

## 13. Relacje do innych dokumentów

### 13.1. P₀-TETRA-20 v0.2.4

| P₀-TETRA-20 | P₀-STALK |
|---|---|
| 22 tryby (7 I_h + 15 chiralnych) | 8 silnych wachlarzy (O_h) |
| \(L_{\text{cyc}}\) = line graph laplacian | potwierdzone identycznie |
| Φ_kwadratowe zeruje się na diagonali | brak silnych tras kwadratowych |
| Φ_kubiczne istnieje (7-wym) | nie testowane |
| Atraktor k=5 outlier (\(\|T\| = 5{,}27\)) | N1 = 4 dla 4 trójek (do zbadania) |

### 13.2. P₀-TAU v1.7.2

P₀-TAU §7.8 opisuje 5K₄ (pięć czworościanów wokół wspólnej **krawędzi**) z deficytem 7,36°. Nasz obiekt to **8 silnych wachlarzy** (wokół wspólnego **wierzchołka-sześcianu**).

P₀-TAU i P₀-STALK to dwa różne obiekty geometryczne.

### 13.3. „Dzień świstaka"

Model \(T = c \cdot \mathrm{Geo}(p)\) dla propagacji sygnału. Sprawdzony numerycznie dla kilku wariantów. Alternatywny opis tej samej dynamiki. Zostaje jako 💡 w §12 P5.

---

## 14. Historia

| Data | Zmiana |
|---|---|
| 2026-10-04 | Start wątku |
| 2026-10-04 | Identyfikacja L_cyc = line graph laplacian |
| 2026-10-04 | V_cyc dokumentu = nasz cycle space |
| 2026-10-04 | Pojedynczy czworościan: 25,7721° |
| 2026-10-04 | Silne wachlarze: 14/240 tras |
| 2026-10-04 | Liniowy przyrost fazy dla cyklu 3 |
| 2026-10-05 | Hipoteza łodyga/liść |
| 2026-10-05 | v1.0, v1.1 |
| 2026-10-05 | Test 3g: N1 bimodalne |
| 2026-10-05 | Test 3j: N1 koreluje z trwałością (r = 0,92), λ₂ koreluje ujemnie |
| 2026-10-05 | Test 3l: dim ker = N1 dla wszystkich trójek |
| 2026-10-05 | **v1.2: korekta §6, N1 jako kluczowy wynik** |

---

## 15. Katalog kodu

### 15.1–15.12 (jak w v1.1)

[zachowane bez zmian]

### 15.13. Test 3g — λ₂ dla wszystkich 56 trójek

```python
def lambda_2(cycle):
    R_total = np.eye(12)
    for k in cycle: R_total = R_fans[k] @ R_total
    eigs = eig(R_total)[0]
    mods = sorted(np.abs(eigs), reverse=True)
    return mods[1]
```

Wynik: λ₂ ∈ [0,18; 1,0], 23 trójki z λ₂ = 1, 33 z λ₂ < 0,58.

15.14. Test 3j — pełne widmo z krotnością jedynki

```python
def widmo_stats(cycle):
    R_total = np.eye(12)
    for k in cycle: R_total = R_fans[k] @ R_total
    eigs = eig(R_total)[0]
    mods = sorted(np.abs(eigs), reverse=True)
    n_ones = sum(1 for m in mods if m > 0.95)
    rest = mods[n_ones:]
    l2 = rest[0] if len(rest) > 0 else 0.0
    l3 = rest[1] if len(rest) > 1 else 0.0
    return n_ones, l2, l3, mods
```

Wynik: N1 ∈ {0, 1, 2, 4}. Korelacja r(N1, ‖x‖₂₀) = +0,9153.

15.15. Test 3l — wymiar jądra R_total − I

```python
def dim_kernel_R_minus_I(cycle, tol=1e-6):
    R_total = np.eye(12)
    for k in cycle: R_total = R_fans[k] @ R_total
    M = R_total - np.eye(12)
    rank = np.linalg.matrix_rank(M, tol=tol)
    return rank, 12 - rank
```

Wynik: dim ker = N1 dla wszystkich 56 trójek. Macierze są diagonalizowalne w podprzestrzeni stałej.

15.16. Tabela wyników N1

N1 #trój ‖x‖₂₀ mean ‖x‖₂₀ min ‖x‖₂₀ max
0 27 0,0029 0,0002 0,0091
1 6 0,238 0,179 0,310
2 19 0,385 0,179 0,504
4 4 0,483 0,433 0,525

15.17. Cztery trójki z N1 = 4

# Trójka λ₂ ‖x‖₂₀
1 v0–v2a–v2b 0,315 0,525
2 v1–v3a–v3b 0,315 0,510
3 v2a–v2b–v5 0,313 0,463
4 v3a–v3b–v5 0,324 0,433

---

16. Podsumowanie jednym zdaniem

Linia prosta P₀ na ikosaedrze = podprzestrzeń stała operatora R_{\text{total}} dla trójki silnych wachlarzy; kluczową liczbą jest wymiar tej podprzestrzeni (N1 ∈ {0, 1, 2, 4}), a nie konkretna trasa ani faza liniowa; N1 = 4 dla czterech trójek (v0–v2a–v2b, v1–v3a–v3b, v2a–v2b–v5, v3a–v3b–v5) daje asymptotyczną normę > 0,43 po 20 obiegach.

---

Uwaga o kompletności. Dokument + katalog kodu (§15) traktujemy jako komplet. W kolejnych rozmowach wystarczy odwołać się do numeru skryptu (§15.x) i wyniku. Kod źródłowy jest w notebookach Kopia notatnika 7atraktorow i Ciag K4 użytkownika.

```