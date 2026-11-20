
# Korzeń: P0-Experiments v0.3.2 — adnotacja szefa lab. (2026-11-20)

**Dokument:** upload Leszka „P0_Experiments_v0_3_2.md" (21 026 B, 284 linie wg wc -l, odczyt narzędziowy 284 — zgodność pełna, trzecia z rzędu po Scalar i PILLARS; ostatnia z finalnym EOL, piąty dokument korpusu z EOL po Memory, TETRA-20, Scalar, PILLARS; md5 16c78174). „P₀-Experiments / Protokoły falsyfikacji hipotez projektu P₀", Wersja 0.3.2 (Draft), Data: 2026-08-12, synteza 2026-08-06/12 (wspólna stopka z Scalar); status nagłówka 🔍 Program eksperymentalny, status korekty jawnie: v0.3.2 aktualizuje E-04 po domknięciu Lematu W-L (2026-08-10) i bazę matematyczną. Filar 6 tabeli PILLARS w wersji dokładnie bumpowanej w dzienniku 08-15 — POTWIERDZENIE SĘKA TABELI: bump realny, bo dokument istnieje w tej wersji. Baza deklarowana: Centroid v4.9.5, Wave v0.6.1, Net v0.3-draft, Philosophy v0.6.1, Applications v0.5.2, Scalar v0.3.4 — obraz chronologii WEWNĄTRZ dnia 08-15: Experiments powstał po bumpie Applications (0.5.2 w bazie) i przed bumpami Centroid (4.9.6), Philosophy (0.6.2), Net (0.3.2), Scalar (0.3.5) — wzorzec dat wyjaśniający rozjazd nagłówka Scalara (08-12) z bumpem (08-15): nagłówek = data syntezy, korekty 08-15 nie podbijają daty; pięć wierszy tabeli PILLARS przesądza się ku „bumpy realne, wiersze do aktualizacji" (4 z 5 potwierdzone dokumentami: Experiments ten, Scalar, Alchemy, Applications w bazie tu). Pozycja: dokument metodologiczny, „nie stanowi części aksjomatyki matematycznej", nie zawiera wyników eksperymentalnych — wyłącznie definicje. Po tym wpięciu 5 z 8 filarów tabeli jest w repo (Centroid, Wave, Net, Alchemy, Experiments); brak: Philosophy, Applications, Origins (obecny pośrednio przez gałąź Scalar).

**Co bada:** warunki falsyfikacji hipotez aplikacyjnej warstwy P0: trzy poziomy testowania (E1 symulacja / E2 dane wtórne / E3 eksperyment pierwotny), sześcioelementowa struktura protokołu (hipoteza, predykcja, warunek falsyfikacji, schemat pomiaru, poziom, status), zasady reprodukowalności (otwarty kod, parametry, niezależna replikacja, raport z falsyfikacji), priorytety i harmonogram.

**Najmocniejsze:** (1) §0 zasada redakcyjna: „Żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia, którego dotyczy" — najkrótsza formuła zasady nadrzędnej warsztatu w korpusie; legenda statusów z pięcioma symbolami (✅ Dowiedzione, 📚 Klasyczne, 🔍 Zweryfikowane numerycznie lub symbolicznie bez dowodu ogólnego, 💡 Przypuszczenie, ❌ Sfalsyfikowane) — rozszerzenie legendy repo o jawne rozróżnienie dowodu od weryfikacji numerycznej; symbol 📚 współczesny Scalar (oba 08-12/15): geneza w dwóch dokumentach jednego dnia, przy scaleniu jedna legenda Z1. (2) zasada asymetrii: „Jeśli eksperyment nie spełnia warunku falsyfikacji, hipoteza pozostaje nieobalona — nie potwierdzona" oraz zasada niezależności: „Jeśli hipoteza aplikacyjna upada, upada model zastosowaniowy, nie algebra 𝔤₄ ani dynamika słów" — twardy rozdział epistemiczny między matematyką a aplikacjami, echo etyczne SERC (P₀ nie diagnozuje) sformułowane jako reguła programu eksperymentalnego. (3) E-04 jako wzorzec reakcji na domknięcie: Lemat W-L dowiedziony 08-10 — protokół NIE skasowany, lecz przebudowany z testu lematu na test uogólnienia wzorca na systemy rozproszone z innymi regułami niż M_m/T, z jawnym zastrzeżeniem „dowód w jednym systemie nie implikuje niczego o innym" i świadomie obniżonym priorytetem (Wysoki → Średni, bo „nie odblokowuje już niczego wewnątrz Wave") — dokument praktykuje własną zasadę redakcyjną na żywo. (4) E-14 z jawną barierą epistemiczną: redukcja cech do ℝ⁴ to „modelowanie zewnętrzne względem P₀", eksperyment testuje „czy obraz da się opisać w języku P₀ przy rozsądnym wyborze cech" — „to jest heurystyka (poziom C), nie bezpośredni transfer": najuczciwiejsza konstrukcja pomostu aplikacyjnego w korpusie, dwa cudzysłowy typograficzne w tekście tej uwagi verbatim. (5) E-01 operacjonalizacja fazy 25,77° z najostrzejszym marginesem w korpusie: para zespolona arg(0,153 + 0,074i) ≈ 25,77°, falsyfikacja przy odchyleniu > 5° i precyzji < 10⁻⁶; liczba 0,153 + 0,074i pochodzi z Centroid §5/§6.4 (wg tabeli zależności §4) — niezależna linia tej samej liczby, którą Memory (09-07) potwierdzi jako 0,1533 ± 0,0740i trzy tygodnie później: jedna wartość, dwa dokumenty, kandydat na twierdzenie słojowe klasyczne (📚).

**Koncesje i sęki:** (1) rozjazd liczebnika w §1: tytuł sekcji „P₀ jako siedmiofilarowa architektura", pierwsze zdanie „składa się z ośmiu komplementarnych filarów" — ślad okresu siedmiu filarów, nie tykamy verbatim, pył do autora. (2) luka numeracyjna E-08..E-13: dokument zawiera E-01..E-07 i E-14, protokoły E-08..E-13 nie istnieją w treści; bank kolejki rozliczony: te numery to przyszłe protokoły Scalar (adnotacja Scalar: „E-08..E-13 do Experiments") — tylko że Experiments stanu 08-15 bazuje na Scalar v0.3.4 i zna wyłącznie S1/S12 w zależnościach E-14; E-TETRA-01..12 też nieobecne (TETRA-20 z 09-18 jest po horyzontem dokumentu); przypuszczenie (nie pewność): luka to rezerwacja numeracji pod protokoły Scalar. (3) dwa opisy N9 w jednym dokumencie: zależności E-14 mówią „problem N9 (transport geometryczny vs algebraiczny, §6)" wg starego Net v0.3-draft, rekomendacja §4 mówi językiem PILLARS „N9 potwierdzone dla {M₀,...,M₃}, wciąż otwarte dla pełnego alfabetu z T — zob. N10" — zgodność z tabelą co do znaku, ale wewnętrzna niespójność definicji vs statusu. (4) dwa opisy S12: zależności E-14 „częściowo sfalsyfikowana, wymaga twierdzenia warunkowego" (zgodne z koncesją §9.5 Scalar), rekomendacja „S1, S12 wciąż otwarte" — luźniejsze sformułowanie tego samego, pył. (5) językowe pyły verbatim: „w momentach coincydencji" (E-02 krok 4, anglicyzm zamiast „zbiegu"), „jest zewnętrznym względem P₀ modelemowaniem" (E-14 uwaga, forma „modelemowaniem" zamiast „modelowaniem") — oba do nota u autora. (6) cytaty sekcji Scalar (C_ε §2.1, R_ε §2.2, J_ε §2.3, S1 §5, S12 §4.2) są wg bazy v0.3.4 — numeracja może być przesunięta względem wpiętego v0.3.5 (rodzina rozjazdów §11.6 SERC ↔ §6.3 Scalar), przy scaleniu kontrolować. (7) Data 08-12 + rekomendacja „zaktualizowana 2026-08-12", a jednak zna Applications v0.5.2 bumpowane 08-15 i język N9/N10 z tabeli 08-15 — spójne z wzorcem dat (korekta 08-15 nie podbija nagłówka), ale chronologia nagłówka jest myląca.

**Struktury 💡:** (1) hierarchia czasowa L/T/Z (liść, gałąź, pień) z Centroid §13 operacjonalizowana w protokołach: E-02 (rozdzielenie skal: pierwsze 29/31/899 vs gładka 32/256, τ_intra/τ_inter) i E-14 (poziomy obrazu) — to jest progenitor terminologii, którą STALK (10-05) użyje jako łodyga/liść; linia: Centroid §13 → E-02/E-14 → STALK. (2) trójstopniowa skala poziomów E1/E2/E3 jako mapa ryzyka replikacji: symulacyjne protokoły (E-01, E-02, E-05) są tanie i w zasięgu warsztatu Z1, empiryczne (E-03, E-14) wymagają danych zewnętrznych, pierwotne (E-07) budowy systemu — priorytety dokumentu izomorficzne z naszą kolejnością replikacji wg kosztu. (3) struktura sześcioelementowa protokołu jako wzorzec specyfikacji testu: warunek falsyfikacji powinien być zapisywalny jednym zdaniem obserwacyjnym — sprawdzić przy przeglądzie zleceń warsztatowych. (4) E-03 (attention jako projektory P_λ Wave, idempotentność, dominująca λ ≈ 1, kryterium wektorowe) jako pre-echo P₀-AI (09-10): pierwszy pomost AI w korpusie, miesiąc przed dokumentem AI.

**Mosty 💡:** (1) do PILLARS-TABLE: drugi aktywny odnośnik w korpusie (po Scalar §11), potwierdzenie zasady odnośnika; zgodność opisu N9/N10 co do znaku z wierszem Net tabeli; rozliczenie sęka synchronizacji tabeli (bumpy realne). (2) do Applications v0.5.2 (jeszcze poza repo): zasada falsyfikacji zdefiniowana WZGLĘDEM Applications („hipoteza z P₀-Applications zostaje uznana za sfalsyfikowaną"), więc E-14 to konkret: aplikacja obrazowa — przy wpięciu Applications rozliczyć nakładki domen (obraz/film/kolor z SERC) z E-14. (3) do Wave: E-04/E-05/E-06 testują katalog słów, zanik koherencji (0,085 na literę) i moduły zdegenerowane; katalog L ≤ 12 to kontynuacja warsztatowa tego, czego Wave nie domknął. (4) do Net: E-07 (transport jako protokół konsensusu, warunki 1–3 §4) i E-14 krok 6 — N9 rozstrzyga klasę transportu w teście. (5) do Centroid: E-01 (faza, §5, §6.4), E-02 (§13.5), E-14 (hierarchia §13, warunek §13.1). (6) do STALK: konwencja per-wierzchołkowa N1/25,7721° vs E-01 25,77° na K₄ z pełną rundą — dwa konteksty tej samej pary zespolonej (runda totalna vs wachlarzowa). (7) do SERC: zasada niezależności jako etyka warstwowa; oraz SERC pyta o rytm interwencji — E-02 mierzy rytm hierarchii: przy scaleniu połączyć.

**Sęk-odnogi:** (1) E-02: czy 899 = 29·31 zamierzona (iloczyn kolejnych liczb pierwszych), a hierarchia gładka 32 = 2⁵ i 256 = 2⁸ — porównanie pierwszych vs potęg dwójki; sęk: czy wynik zależy od wartości iloczynu, czy od samego rozdzielenia skal; do autorskiego sondażu. (2) E-01 na E2: wymaga identyfikacji empirycznego systemu z czterema zmiennymi sekwencyjnymi — czy istnieje naturalny kandydat (mała sieć sensorów)? (3) E-03: losowe macierze gaussowskie jako baseline — doprecyzować metrykę struktury projektorowej. (4) E-14: próg IoU 0,3 i korelacja 0,2 uzasadnione? (5) luka E-08..E-13: czy numeracja zarezerwowana dla protokołów Scalar — potwierdzić u autora przy dostawie v0.3.3+. (6) E-05 z E2: szeregi finansowe jako „słowa operacji rynkowych" — luźna analogia, sęk typologiczny. (7) powtórzyć przy scaleniu: cytaty sekcji Scalar wg v0.3.4 mogą nie zgadzać się z v0.3.5.

**Statusy (mapa na Z1):** osiem protokołów w dokumencie, wszystkie 💡 (zaprojektowane, nieprzeprowadzone) — zgodnie z własnym szablonem §2.2 i deklaracją „nie zawiera wyników eksperymentalnych"; dokument czysto metodologiczny. Kolejność uruchomienia wg kosztu (rekomendacja dokumentu spójna z naszą praktyką): E-01 najtańszy (widmo 4×4 pełnej rundy GS na K₄, czysta algebra), E-02 (symulacja 3-poziomowa, N = 100), E-05 (N = 10⁴ słów), E-04 (kontynuacja katalogu L ≤ 12, drożej), E-03 (transformery, dane wtórne), E-14 (zbiory obrazów, najdroższy aplikacyjnie). W warsztacie: E-01 pokrywa się z kandydatami replikacji fazy (STALK/Scalar) i jest prawie darmowy — do pierwszego uruchomienia razem z testem 1/8 vs 0,12383. Zalecenia dokumentu co do E-04 (obniżony priorytet, ale wzorzec otwarty do testu uogólnienia) — kandydat na zlecenie po P26.

**Uwagi redakcyjne (verbatim):** 21 026 B, 284 linie wg wc -l, odczyt narzędziowy 284 — zgodność pełna trzecia z rzędu; md5 16c78174; ostatnia z finalnym EOL (piąty dokument z EOL); CJK 0; CYR 0; backticki 2 (jedna para w §1 wokół linku PILLARS-TABLE.md — drugi aktywny odnośnik w korpusie); cudzysłowy typograficzne: 5 (wszystkie w E-14: trzy w uwadze metodologicznej i dwa w testowanym sformułowaniu) oraz cudzysłowy ASCII wokół słów Wysoki i Średni w rekomendacji (verbatim); potknięcia językowe verbatim: „coincydencji" (linia 90), „modelemowaniem" (linia 252), „siedmiofilarowa" (linia 25) — trzy pyły do autora; liczebności: 8 protokołów w dokumencie (E-01..E-07 + E-14), 6-elementowa struktura, 3 poziomy testowania, trzy wersje bazy starsze niż bumpy z tego samego dnia (Centroid 4.9.5, Philosophy 0.6.1, Scalar 0.3.4), Applications 0.5.2 zgodna z bumpem 08-15; tabele: §2.1 trzy poziomy, §4 priorytety (8 wierszy); stopka kursywą zamyka dokument gwiazdką kursywy przed końcowym EOL; dokument współczesny Relacje/Wave/Scalar (08-12) wg daty syntezy 08-06/12 — ta sama stopka syntezy co Scalar.
# P₀-Experiments
## Protokoły falsyfikacji hipotez projektu P₀
### Wersja 0.3.2 (Draft)

**Status dokumentu:** 🔍 Program eksperymentalny projektu P₀  
**Status korekty:** Korekta v0.3.2 — zaktualizowano E-04 (kontekst: Lemat W-L domknięty 2026-08-10, protokół testuje teraz uogólnienie wzorca, nie sam lemat; priorytet obniżony z Wysoki na Średni), zaktualizowano bazę matematyczną do Centroid v4.9.5, Wave v0.6.1, Net v0.3-draft, Applications v0.5.2.  
**Powiązanie:** Dokument metodologiczny. Nie stanowi części aksjomatyki matematycznej. Każdy protokół wymaga niezależnej weryfikacji przez zespoły eksperymentalne.  
**Baza matematyczna:** P₀-Centroid v4.9.5, P₀-Wave v0.6.1, P₀-Net v0.3-draft, P₀-Philosophy v0.6.1, P₀-Applications v0.5.2, P₀-Scalar v0.3.4.  
**Data:** 2026-08-12

---

## 0. Zasada redakcyjna

> Żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia, którego dotyczy.

Statusy: ✅ Dowiedzione · 📚 Klasyczne · 🔍 Zweryfikowane numerycznie lub symbolicznie (bez dowodu ogólnego) · 💡 Przypuszczenie · ❌ Sfalsyfikowane (odrzucone po weryfikacji).

**Zasada falsyfikacji.** P₀-Experiments nie dowodzi hipotez. Definiuje warunki, przy których hipoteza z P₀-Applications zostaje uznana za sfalsyfikowaną. Jeśli eksperyment nie spełnia warunku falsyfikacji, hipoteza pozostaje nieobalona — nie potwierdzona.

**Zasada niezależności.** Wynik eksperymentu nie wpływa na matematykę P₀. Jeśli hipoteza aplikacyjna upada, upada model zastosowaniowy, nie algebra 𝔤₄ ani dynamika słów.

---

## 1. P₀ jako siedmiofilarowa architektura

Seria P₀ składa się z ośmiu komplementarnych filarów — zobacz [`PILLARS-TABLE.md`](PILLARS-TABLE.md) dla aktualnej listy, wersji i statusów.

---

## 2. Metodologia eksperymentalna

### 2.1. Trzy poziomy testowania

| Poziom | Nazwa | Opis | Przykład |
|:---|:---|:---|:---|
| **E1** | Symulacja numeryczna | Test na danych syntetycznych wygenerowanych przez model P₀ | Weryfikacja, czy faza 25,77° pojawia się w symulacji Gaussa-Seidela dla K₄ |
| **E2** | Analiza danych wtórnych | Test na istniejących zbiorach danych empirycznych | Analiza szeregów czasowych rynkowych pod kątem fazy zespolonej |
| **E3** | Eksperyment pierwotny | Celowo zaprojektowany eksperyment generujący nowe dane | Pomiar dynamiki konsensusu w kontrolowanej sieci rozproszonej |

### 2.2. Struktura protokołu

Każdy protokół w tym dokumencie zawiera:
1. **Hipotezę** (założenie do przetestowania)
2. **Predykcję** (co powinniśmy zaobserwować, jeśli hipoteza jest prawdziwa)
3. **Warunek falsyfikacji** (co musi się wydarzyć, by hipotezę uznać za obaloną)
4. **Schemat pomiaru** (jak zmierzyć; przybliżenie, nie pełny opis techniczny)
5. **Poziom testowania** (E1/E2/E3)
6. **Status** (💡 — protokół zaprojektowany, nie przeprowadzony)

---

## 3. Protokoły eksperymentalne

---

### Protokół E-01: Faza 25,77° w systemach sekwencyjnych

**Hipoteza.** Systemy z cykliczną aktualizacją lokalnych zmiennych na grafie zawierającym cykl wykazują charakterystyczną fazę zespoloną w widmie operatora ewolucji. Dla grafu K₄ i kolejności cyklicznej 0,1,2,3 faza ta wynosi dokładnie arg(0,153 + 0,074i) ≈ 25,77°.

**Predykcja.** W dowolnym systemie, w którym cztery podsystemy aktualizują sekwencyjnie swoje stany przez lokalne uśrednianie (Gauss-Seidel), widmo operatora pełnej rundy zawiera parę zespoloną z argumentem ≈ 25,77° ± margines numeryczny.

**Warunek falsyfikacji.** Jeśli dla potwierdzonego cyklu w grafie aktualizacji i sekwencyjnej kolejności wszystkie wartości własne operatora rundy są rzeczywiste, lub para zespolona ma argument odbiegający o > 5° od 25,77° przy precyzji numerycznej < 10⁻⁶, hipoteza zostaje sfalsyfikowana.

**Schemat pomiaru (E1/E2).**
1. Zidentyfikować system czterech zmiennych z sekwencyjną aktualizacją (syntetyczny: iteracja M_m; empiryczny: dane czasowe z systemu rozproszonego).
2. Zbudować operator przejścia jednej pełnej rundy.
3. Obliczyć widmo operatora (np. metodą QR dla macierzy 4×4).
4. Zmierzyć argument pary zespolonej.
5. Porównać z 25,77°.

**Poziom testowania.** E1 (gotowy — symulacja M_m). E2 (wymaga identyfikacji empirycznego systemu z czterema zmiennymi i sekwencyjną aktualizacją, np. mała sieć sensorów).

**Status.** 💡

---

### Protokół E-02: Hierarchia czasowa z pierwszymi liczbami

**Hipoteza.** Systemy wielopoziomowe z rozdzieleniem skal czasowych proporcjonalnym do kolejnych liczb pierwszych wykazują mniejszą zmienność konsensusu niż systemy z rozdzieleniem gładkim (potęgi 2), przy tym samym szumie zewnętrznym.

**Predykcja.** Dla hierarchii trzypoziomowej z τ_T = 29·τ_L i τ_Z = 31·τ_T, odchylenie standardowe trajektorii konsensusu jest mniejsze niż dla hierarchii τ_T = 32·τ_L i τ_Z = 256·τ_T, przy identycznym szumie gaussowskim σ = 0,05 na magistrali.

**Warunek falsyfikacji.** Jeśli w co najmniej trzech niezależnych konstrukcjach symulacyjnych hierarchia „pierwsze" nie wykazuje istotnie mniejszej zmienności (test t-Studenta, p > 0,05) niż hierarchia „gładka", hipoteza zostaje sfalsyfikowana.

**Schemat pomiaru (E1).**
1. Zasymulować hierarchię 3-poziomową (L, T, Z) z operatorami M_m na każdym poziomie.
2. Dla konfiguracji (A) gładkiej: τ_T = 32, τ_Z = 256.
3. Dla konfiguracji (B) pierwszych: τ_T = 29, τ_Z = 899.
4. Dodać szum gaussowski σ = 0,05 w momentach coincydencji.
5. Zmierzyć odchylenie standardowe trajektorii poziomu T w oknie 20 000 taktów.
6. Powtórzyć N = 100 razy; porównać średnie.

**Poziom testowania.** E1 (symulacja). E3 (wymagałoby zbudowania fizycznego systemu wielopoziomowego, np. hierarchii mikroprocesorów).

**Status.** 💡

---

### Protokół E-03: Projektory jako stany attention w transformerach

**Hipoteza.** Macierze attention w transformerach spełniają algebraiczne własności projektorów spektralnych P₀-Wave: idempotentność (P² ≈ P) w przestrzeni wartości własnych dominujących, oraz zachowanie podprzestrzeni przy doklejeniu nowego tokena (analogia do przetrwania relacyjnego).

**Predykcja.** Dla wytrenowanego modelu transformer (np. BERT-base, GPT-2), macierze attention z ostatnich warstw wykazują:
(a) dominującą wartość własną bliską 1 z krotnością geometryczną ≥ 1 na podprzestrzeni V_ρ (analogia do modułu propagacyjnego),
(b) wektory własne spełniające kryterium (v_ρ)_m ≈ 0 dla pewnych pozycji m (analogia do kryterium wektorowego Wave §4.2).

**Warunek falsyfikacji.** Jeśli w co najmniej trzech różnych architekturach transformerów macierze attention nie wykazują struktury projektorowej (brak dominującej wartości własnej ≈ 1, lub widmo rozproszone jednorodnie), hipoteza zostaje sfalsyfikowana.

**Schemat pomiaru (E2).**
1. Wczytać wytrenowany model transformer.
2. Ekstrahować macierze attention A_l z warstw l = 1, ..., L.
3. Dla każdej A_l obliczyć rozkład SVD lub widmo własne.
4. Sprawdzić, czy istnieje dominująca wartość własna λ₁ z |λ₁| ≈ 1.
5. Sprawdzić, czy odpowiadający jej wektor własny v spełnia kryterium zrzutowane (v_ρ)_m ≈ 0 dla pewnych m.
6. Porównać z losowymi macierzami gaussowskimi jako baseline.

**Poziom testowania.** E2 (dane wtórne — publiczne modele). E1 (można zasymulować attention na małym słowniku).

**Status.** 💡

---

### Protokół E-04: Lemat W-L w systemach rozproszonych

**Kontekst (zaktualizowany 2026-08-12).** Źródłowy Lemat W-L (P₀-Wave §4.3bis) jest teraz **dowiedziony** (✅, nie hipoteza) dla generatorów M_m/T. Ten protokół testuje coś innego i wciąż otwartego: czy ten sam **wzorzec** (brak ukrytych rozwiązań poza modułem prostym/zdegenerowanym) uogólnia się na systemy konsensusu rozproszonego z innymi regułami uśredniania niż M_m/T. To pozostaje osobną, w pełni otwartą hipotezą empiryczną — dowód w jednym systemie nie implikuje niczego o innym.

**Hipoteza.** W systemach konsensusu rozproszonego, jeśli stan przetrwa relacyjnie po lokalnej aktualizacji, to istnieje jednoznaczny wektor własny (z dokładnością do skalowania) opisujący ten stan. Brak ukrytych rozwiązań z u_m ≠ 0 (analogia do lematu W-L).

**Predykcja.** W symulacji systemu rozproszonego z lokalnymi regułami uśredniania, stany przetrwania (stabilne podprzestrzenie) są jednowymiarowe dla modułów prostych i wielowymiarowe dla modułów zdegenerowanych — bez pośrednich przypadków.

**Warunek falsyfikacji.** Jeśli w katalogu słów o długości L ≤ 12 (lub odpowiedniku empirycznym) znaleziono choć jeden przypadek, w którym stan przetrwa relacyjnie, ale nie jest równoległy do v_ρ i nie leży w module zdegenerowanym, hipoteza zostaje sfalsyfikowana.

**Schemat pomiaru (E1/E3).**
1. Zbudować system rozproszony z czterema węzłami i lokalnymi regułami uśredniania.
2. Generować losowe sekwencje aktualizacji (słowa) o długości L ≤ 12.
3. Dla każdego słowa obliczyć operator ρ(w) i sprawdzić moduły |λ| = 1.
4. Dla każdego modułu prostego λ = 1 sprawdzić, czy M_m W u = u implikuje u ∥ v_ρ.
5. Zliczyć kontrprzykłady.

**Poziom testowania.** E1 (symulacja numeryczna, kontynuacja katalogu Wave). E3 (fizyczna sieć rozproszona z kontrolowanym szumem).

**Status.** 💡

---

### Protokół E-05: Zanik koherencji w długich sekwencjach

**Hipoteza.** W dynamice słów P₀-Wave, korelacja między stanem początkowym a stanem końcowym po słowie długości L zanika eksponencjalnie: corr(x₀, x_L) ∝ e^(−0,085L).

**Predykcja.** Dla losowych stanów startowych i losowych słów propagacyjnych z katalogu L ≤ 12, korelacja między składową w V_ρ stanu startowego a końcowego maleje ze stałą dekrementu ≈ 0,085 na literę.

**Warunek falsyfikacji.** Jeśli zanik nie jest eksponencjalny (np. potęgowy, oscylacyjny, lub brak zaniku), lub stała dekrementu odbiega o > 20% od 0,085 przy N > 10 000 prób, hipoteza zostaje sfalsyfikowana.

**Schemat pomiaru (E1).**
1. Wygenerować N = 10 000 losowych stanów startowych x₀ ∈ ℝ⁴ z jednostkową składową w V_ρ.
2. Dla każdego stanu wylosować słowo propagacyjne w z katalogu L ≤ 12.
3. Obliczyć x_L = ρ(w)x₀.
4. Zmierzyć korelację corr(x₀, x_L) na podprzestrzeni V_ρ.
5. Dopasować krzywą eksponencjalną e^(−αL); sprawdzić, czy α ≈ 0,085.

**Poziom testowania.** E1 (symulacja). E2 (analiza długich sekwencji w danych empirycznych, np. szeregi czasowe finansowe, jeśli traktować je jako „słowa" operacji rynkowych).

**Status.** 💡

---

### Protokół E-06: Moduły zdegenerowane jako nadmiarowość systemowa

**Hipoteza.** Systemy biologiczne i techniczne zachowują trwałość poprzez nadmiarowość (redundancję), która matematycznie odpowiada modułom zdegenerowanym w P₀-Wave (dim V₁ ≥ 2). W takich systemach uszkodzenie pojedynczego elementu nie powoduje utraty stabilności.

**Predykcja.** System z redundancją (np. sieć neuronowa z dropout, system biologiczny z duplikacją genów) wykazuje własności algebraiczne analogiczne do modułów zdegenerowanych: przestrzeń stanów stabilnych ma wymiar ≥ 2, więc utrata jednego wymiaru nie niszczy stabilności.

**Warunek falsyfikacji.** Jeśli system z potwierdzoną redundancją biologiczną/techniczną nie wykazuje wielowymiarowej przestrzeni stanów stabilnych po perturbacji, lub jeśli usunięcie jednego elementu zawsze prowadzi do utraty stabilności mimo pozornej redundancji, hipoteza zostaje sfalsyfikowana.

**Schemat pomiaru (E2/E3).**
1. Zidentyfikować system z redundancją (np. sieć z podwójnymi połączeniami, organizm z duplikowanym metabolizmem).
2. Zbudować model operatorowy systemu (uproszczony do postaci M_m-like).
3. Obliczyć przestrzeń własną dla λ = 1.
4. Sprawdzić, czy dim V₁ ≥ 2.
5. Usunąć jeden element (symulacja lub eksperyment) i ponownie zmierzyć dim V₁.

**Poziom testowania.** E2 (analiza danych biologicznych). E3 (eksperyment inżynieryjny z siecią rozproszoną).

**Status.** 💡

---

### Protokół E-07: Transport w P₀-Net jako protokół konsensusu

**Hipoteza.** Operator transportu R zdefiniowany w P₀-Net (zachowujący p₀, V_ρ, G_4) może być zaimplementowany jako protokół konsensusu w sieciach rozproszonych (np. blockchain, federated learning).

**Predykcja.** Jeśli węzły sieci rozproszonej komunikują się zgodnie z warunkami transportu P₀-Net (zachowanie punktu stałego, izometria na części relacyjnej), system osiąga konsensus zbieżny do p₀ i zachowuje metrykę relacyjną między węzłami.

**Warunek falsyfikacji.** Jeśli implementacja operatora transportu spełniająca warunki (1)–(3) Net §4 nie prowadzi do zbieżnego konsensusu, lub jeśli konsensus zachodzi, ale narusza metrykę G_4, hipoteza zostaje sfalsyfikowana.

**Schemat pomiaru (E3).**
1. Zbudować sieć czterech węzłów z lokalnymi modelami P₀.
2. Zaimplementować operator transportu R_e między węzłami spełniający warunki (1)–(3).
3. Uruchomić lokalną dynamikę (słowa) w każdym węźle równolegle.
4. Mierzyć odległość między stanami węzłów w metryce G_4.
5. Sprawdzić, czy odległość pozostaje stała (izometria) i czy wszystkie węzły zbiegają do wspólnego p₀.

**Poziom testowania.** E3 (eksperyment inżynieryjny).

**Status.** 💡

---

### Protokół E-14: Segmentacja relacyjna i hierarchia skal obrazu

**Hipoteza.** Obraz naturalny (fotografia, scena) może być reprezentowany jako hierarchia lokalnych modeli P₀ połączonych transportem, gdzie:
- poziom L (liść/fragment) = lokalny model P₀ (ℝ⁴, M_m) opisujący relacje wewnątrz małego regionu;
- poziom T (gałąź/region) = zredukowane stany p₀^{(L)} połączone w sieć z transportem R;
- poziom Z (pień/scena) = zredukowane regiony p₀^{(T)} tworzące globalną konfigurację;
- segmentacja = emergencja domen P₀-Scalar (operator C_ε, sąsiedztwo N_ε(i));
- granice obiektów = miejsca zaniku transportu lub rozłączenia domen Scalar.

**Predykcja.**
1. Dla obrazu o rozdzielczości N×M, zastosowanie operatora C_ε w przestrzeni cech (np. kolor, gradient, tekstura) generuje domeny emergentne odpowiadające semantycznym regionom (tło, obiekt, tekstura).
2. Domeny te tworzą hierarchię skal zgodną z §13 Centroid: czas relaksacji wewnętrznego konsensusu w domenie jest znacznie krótszy niż czas relaksacji między domenami.
3. Transport między sąsiednimi domenami wewnątrz tego samego poziomu zachowuje metrykę G₄ (izometria na V_ρ).
4. Granice między semantycznie różnymi obiektami odpowiadają miejscom, gdzie transport zanika (R nie spełnia warunków 1–3 Net) lub gdzie domeny Scalar się rozłączają (N_ε(i) = ∅).

**Warunek falsyfikacji.** Hipoteza zostaje sfalsyfikowana, jeśli spełni się **co najmniej jeden** z poniższych warunków:
- (a) Dla co najmniej trzech różnych klas obrazów (np. krajobrazy, portrety, tekstury) segmentacja przez C_ε nie generuje domen korespondujących z segmentacją referencyjną (IoU < 0,3 dla głównych regionów).
- (b) Hierarchia skal czasowych nie wykazuje rozdzielenia τ_L ≪ τ_T ≪ τ_Z (np. wszystkie skale są tego samego rzędu).
- (c) Transport między sąsiednimi regionami narusza metrykę G₄ (odległość w V_ρ rośnie zamiast być zachowana).
- (d) Granice semantyczne nie korespondują z miejscami zaniku transportu lub rozłączenia domen (korelacja < 0,2).

**Schemat pomiaru (E1/E2).**
1. **Przygotowanie danych.** Wybrać zbiór obrazów referencyjnych z adnotacjami segmentacyjnymi (np. COCO, Pascal VOC, BSDS500).
2. **Ekstrakcja cech.** Dla każdego piksela/patcha zdefiniować wektor cech f ∈ ℝ^d (d ≥ 4). Zredukować do przestrzeni 4-wymiarowej metodą wybraną (PCA, ręczna selekcja, autoencoder) — **to jest krok modelowania, nie wynik P₀**.
3. **Segmentacja Scalar.** Zastosować operator C_ε (Scalar §2.1) w przestrzeni cech:
   - Dla każdego węzła i zdefiniować sąsiedztwo N_ε(i) na podstawie odległości w przestrzeni cech.
   - Wykonać rundę asynchroniczną R_ε (Scalar §2.2) lub synchroniczną J_ε (§2.3).
   - Powtarzać do stabilizacji domen (brak zmian w grafie G_t(ε)).
4. **Pomiar domen.** Porównać emergentne domeny z segmentacją referencyjną (miary: IoU, Rand Index, Boundary F-score).
5. **Hierarchia czasowa.** Zmierzyć tempo relaksacji wewnątrz domeny (liczba rund do osiągnięcia konsensusu p₀^{(L)}) oraz tempo relaksacji między domenami. Sprawdzić, czy τ_{intra} / τ_{inter} ≥ 10 (warunek hierarchii §13.1).
6. **Transport Net.** Dla par sąsiednich domen wewnątrz poziomu L obliczyć operator transportu R. Sprawdzić, czy zachowuje p₀, V_ρ, G₄ (warunki 1–3 Net §4). Na granicach obiektów sprawdzić, czy transport nie istnieje (warunek 1 lub 2 naruszony).
7. **Porównanie z baseline.** Porównać wyniki z klasycznymi metodami segmentacji (k-means, mean-shift, graph cut).

**Poziom testowania.** E1 (symulacja numeryczna na danych referencyjnych). E2 (analiza istniejących zbiorów obrazów). E3 (wymagałoby zbudowania dedykowanego systemu przetwarzania obrazu w architekturze P₀).

**Status.** 💡

**Zależności.** Protokół E-14 wymaga zamknięcia następujących problemów otwartych w innych filarach:
- P₀-Scalar: hipoteza P₀-S1 (emergencja domen, §5) oraz S12 (niezmienniczość regionów, §4.2) — częściowo sfalsyfikowana, wymaga twierdzenia warunkowego.
- P₀-Net: problem N9 (transport geometryczny vs algebraiczny, §6) — decyduje o klasie transportu R zastosowanego w kroku 6.
- P₀-Centroid: hierarchia czasowa §13 — zweryfikowana numerycznie dla 3 poziomów, ale dowód ogólny otwarty.

**Uwaga metodologiczna.** Krok 2 (redukcja cech do ℝ⁴) jest **zewnętrznym względem P₀** modelemowaniem. P₀ dostarcza struktury (ℝ⁴, M_m, R, C_ε), ale nie dyktuje, które cechy wizualne odpowiadają którym wymiarom. Eksperyment testuje więc nie „P₀ opisuje obraz", lecz „czy obraz da się opisać w języku P₀ przy rozsądnym wyborze cech". To jest heurystyka (poziom C), nie bezpośredni transfer.

---

## 4. Priorytety i harmonogram

| Protokół | Zależność matematyczna | Poziom | Trudność | Priorytet |
|:---|:---|:---|:---|:---|
| E-01 | Centroid §5, §6.4 | E1/E2 | Niska | **Wysoki** |
| E-02 | Centroid §13.5 | E1 | Niska | Średni |
| E-03 | Wave §4, Philosophy §14.1 | E2 | Średnia | Średni |
| E-04 | Wave §4.3bis (wzorzec z dowiedzionego lematu W-L, testowany na innych systemach) | E1/E3 | Średnia | Średni |
| E-05 | Wave v0.1 §9 (zanik koherencji) | E1 | Niska | Średni |
| E-06 | Wave §4.4 (moduły zdegenerowane) | E2/E3 | Wysoka | Niski |
| E-07 | Net §4 (transport) | E3 | Wysoka | Średni |
| **E-14** | **Scalar §5 + Net §4 + Centroid §13** | **E1/E2** | **Średnia** | **Średni** |

**Rekomendacja (zaktualizowana 2026-08-12).** Rozpocząć od E-01 (najniższy koszt, najwyższy zwrot informacyjny — weryfikuje jeden z najbardziej charakterystycznych wyników P₀, fazę 25,77°). E-04 zmieniło charakter: Lemat W-L jest już dowiedziony (2026-08-10, Wave §4.3bis) — E-04 nie testuje już otwartego problemu Wave, tylko sprawdza, czy ten sam, teraz ustalony wzorzec matematyczny uogólnia się na systemy rozproszone spoza P₀. To wciąż wartościowy, ale inny w charakterze test — obniżony z priorytetu "Wysoki" na "Średni", bo nie odblokowuje już niczego wewnątrz Wave. E-14 pozostaje drugorzędny — zależy od Scalar (S1, S12 wciąż otwarte) i Net N9 (potwierdzone dla {M₀,...,M₃}, wciąż otwarte dla pełnego alfabetu z T — zob. N10).

---

## 5. Zasady reprodukowalności

Każdy eksperyment przeprowadzony w ramach P₀-Experiments musi spełniać:

1. **Otwarty kod.** Implementacja symulacji i analizy dostępna w repozytorium publicznym.
2. **Dokumentacja parametrów.** Wszystkie parametry (rozmiar grafu, długość słów, liczba iteracji, seed RNG, próg ε, wymiar cech d) zapisane w metadanych.
3. **Niezależna replikacja.** Co najmniej jedna replikacja przez zespół niezwiązany z autorami protokołu.
4. **Raport z falsyfikacji.** Jeśli hipoteza upada, raport musi zawierać dokładny warunek, przy którym upadła, oraz sugestię, czy model aplikacyjny wymaga korekty, czy cała hipoteza P₀ w tej dziedzinie jest nieadekwatna.

---

*P₀-Experiments v0.3.2. Aktualizacja odnośników do Applications v0.5.2, Philosophy v0.6.1, Net v0.3-draft i Scalar v0.3.4. Dodano protokół E-14 (segmentacja relacyjna i hierarchia skal obrazu). Zaktualizowano E-04 po domknięciu Lematu W-L (2026-08-10) — protokół testuje teraz uogólnienie wzorca na systemy rozproszone, nie sam lemat; priorytet obniżony. Architektura filarów — odesłanie do PILLARS-TABLE.md. Nie zawiera wyników eksperymentalnych — wyłącznie definicje predykcji, warunków obalenia i schematów pomiaru. Synteza: 2026-08-06/12.*
