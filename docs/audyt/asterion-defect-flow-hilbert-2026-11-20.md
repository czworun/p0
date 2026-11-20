# Audyt Asteriona: Defect ↔ Flow ↔ Hilbert

**Data:** 2026-11-20  
**Baza korpusowa:** `main` @ `ff5345f50f509ff95fafcd1e4b28ce64b388eb1c`  
**Gałąź:** `audit/asterion-defect-flow-hilbert-2026-11-20`  
**Zakres:** P₀-Flow v0.5.3, P₀-Defect v0.8 (§12A–§12H), dostępność źródła P₀-Hilbert oraz rachunek niezależny dla §12H.  
**Charakter:** audyt matematyczny i źródłowy, materiał wejściowy dla laboratorium. Bez decyzji statusowych i bez zmian w korzeniach.

## 1. Wniosek ogólny

Przeniesienie Flow do Defect jest **konsolidacją selektywną, nie pełnym zastąpieniem źródła**. Flow sam to deklaruje: Defect rozwija konteksty §12A–G, ale Flow pozostaje korzeniem źródłowym dla treści, których nie przeniesiono. Repozytorium nie zawiera oddzielnego pliku P₀-Hilbert; dostępna jest tylko sekcja §12H w Defect. To ogranicza możliwość potwierdzenia kompletności transferu Hilberta.

Najważniejsze kandydaty do dalszego sprawdzenia:

1. **Euler–Arnold, §12G.4:** zapis równania zawiera składnik z bracketem `[R_B,R_B]`, który przy standardowym rozumieniu jest identycznie zerowy. To może być błąd zapisu w kluczowym miejscu wnioskowania.
2. **Hilbert, R3-1/R3-3:** niezależny rachunek macierzowy potwierdza `CᵀC = 4P_cyc`; ponadto brak przecięcia torusa równych amplitud z przestrzenią exact ma krótki dowód geometryczny, którego nie zapisano w §12H.5.
3. **Hilbert, R3-2:** podana konfiguracja osiąga wartość `(3−2√2)δ²` dokładnie, ale globalna dolna granica nadal nie ma dowodu. 400 niezależnych startów optymalizacji Asteriona nie znalazło niższej wartości; to kontrola numeryczna, nie dowód globalności.
4. **Reprezentacje:** historia „Tylko Vρ ⊙ Vcyc” nie przeczy automatycznie twierdzeniu o bracketcie Vcyc×Vcyc, ale dokument powinien określić pełną przestrzeń map, którą ta tabela klasyfikuje.
5. **Granica continuum:** lista grup z niezmiennikiem kubicznym wymaga jawnego wskazania reprezentacji i rozdzielenia Sym³ od Λ³.

---

## 2. Zakres transferu Flow → Defect

Źródła:
- `docs/korzenie/P0-Flow-v0_5_3.md`
- `docs/korzenie/P0-Defect-v0_8.md`

### 2.1. Co zostało przeniesione

W przybliżeniu odpowiadają sobie:
- Flow §3.1–§3.4 ↔ Defect §12A–§12B: twierdzenie A, rachunek charakterów i historia korekt;
- Flow §4.1–§4.9 ↔ Defect §12C–§12F: rozszczepienie A⊕B, kanały T_a/T_b, kryterium reprezentacyjne i stabilność architektury;
- Flow §7.1–§7.5 ↔ Defect §12G: kandydacka granica continuum, bracket T_a, nieprzenoszenie T_b i porównanie z Eulerem–Arnoldem.

To jest spójne z deklaracją Defect §0.5 i notą Flow na początku pliku.

### 2.2. Co pozostało wyłącznie w źródle Flow

Flow jawnie zachowuje jako treści, dla których sam pozostaje źródłem, między innymi:
- §5.5.1 — pełną historię testu kowariancji S₄;
- §5.7 — genezę i taksonomię asymetrii strukturalnej;
- §7.5 — pełne zestawienie kanałów z Eulerem–Arnoldem i jego wyprowadzenie.

Defect §12G.4 zawiera skróconą postać równań i wniosek, ale nie cały aparat porównawczy Flow §7.5. To nie jest błąd, jeśli oba korzenie pozostają w obiegu zgodnie z klauzulą SSOT. Jest natomiast błędem traktowanie samego Defect jako samowystarczalnego zamiennika pełnej treści Flow.

**Rekomendacja:** w materiałach replikacyjnych wskazywać parę źródeł: Defect §12A–G jako aktualną konsolidację oraz Flow v0.5.3 jako źródło części nieprzeniesionych. Nie kopiować brakujących fragmentów bez decyzji autora.

---

## 3. Hipoteza F1 — równanie Euler–Arnolda w §12G.4 wymaga pilnej kontroli

**Miejsce:** Defect §12G.4 i Flow §7.4–§7.5.

W obu tekstach występuje równanie:
`\dot R_A = -I_B[R_B,R_B], \qquad \dot R_B = -(I_B-I_A)[R_A,R_B].`

### Problem

Jeżeli nawias kwadratowy oznacza — jak w pozostałym korpusie — bracket Liego, to:
`[R_B,R_B] = 0`
z antysymetrii bracketu. Pierwsza składowa równania jest zatem identycznie zerowa, niezależnie od anizotropii `I_B`, jeśli `I_B` działa dopiero na wynik bracketu.

Tymczasem tekst opisuje kanał `B × B → A` jako kanał obecny w pełnym Eulerze–Arnoldzie. Taki kanał biliniowy może być niezerowy dla dwóch różnych argumentów `B_1,B_2`, ale nie przy podstawieniu tego samego argumentu dwa razy. W równaniu ewolucji z anizotropią zwykle trzeba sprawdzić wyrażenie w rodzaju bracketu między `R_B` a przekształconym `I_B R_B`; nie wolno jednak samowolnie wstawiać tej postaci bez odtworzenia konwencji autora.

### Test rozstrzygający

1. Ustalić, czy `R_A,R_B` oznaczają prędkość, pęd czy składowe innej zmiennej.
2. Podać dokładną definicję operatora bezwładności `I), w tym działanie `I_A,I_B`.
3. Wyprowadzić równanie Euler–Arnolda z `\dot m = \operatorname{ad}^*_u m` (albo jawnie przyjętej konwencji znaku), a następnie rozłożyć je na A i B.
4. Sprawdzić jawnie, że projekcja `B×B→A` nie znika po podstawieniu właściwych argumentów dynamicznych.
5. Dopiero wtedy używać tabeli kanałów w Flow §7.5/Defect §12G.4 jako podstawy wniosku o „obiekcie trzecim”.

**Priorytet: P0 — pierwsze zadanie do laboratorium.** Jeśli to tylko błąd zapisu, naprawa może być lokalna. Jeśli równanie jest literalne, uzasadnienie porównania z pełnym Eulerem–Arnoldem wymaga ponownego wyprowadzenia.

---

## 4. Hipoteza F2 — doprecyzować reprezentacyjne znaczenie historii „Tylko Vρ ⊙ Vcyc”

**Miejsca:** Flow §3.1–§3.4; Defect §12A–§12B.5.

W pierwszym odczycie tabela historii korekt może wyglądać na sprzeczną:
- Twierdzenie A: `Hom_Sn(Vcyc⊗Vcyc,Vcyc)` ma wymiar 1, a jedyny kanał to antysymetryczny bracket;
- konsekwencja: `Hom_Sn(Sym²(Vcyc),Vcyc)=0`;
- wiersz v2 tabeli historii: „Tylko `Vρ ⊙ Vcyc`, krotność 1”.

Te zdania mogą być jednocześnie prawdziwe, jeśli tabela v2 klasyfikuje **symetryczne kwadratowe samoodziaływanie całej przestrzeni** `C¹ = Vρ ⊕ Vcyc`, a nie samą przestrzeń `Vcyc⊗Vcyc`.

Wtedy:
`Sym²(C¹) = Sym²(Vρ) ⊕ (Vρ ⊙ Vcyc) ⊕ Sym²(Vcyc)`.

Dla tej interpretacji oczekiwany rozkład krotności do sprawdzenia to:
- `Hom(Sym²(Vρ),Vcyc) = 0`;
- `Hom(Vρ ⊙ Vcyc,Vcyc) = 1`;
- `Hom(Sym²(Vcyc),Vcyc) = 0`.

### Niezależna kontrola Asteriona

Rachunek charakterów dla `n=4,…,10` daje krotności `(0,1,0)` dla trzech powyższych składowych. Dodatkowo `Hom(Vcyc⊗Vcyc,Vcyc)` ma wymiar 1, ale cała ta krotność leży w części antysymetrycznej — w bracketcie. Wynik jest zgodny z interpretacją „jeden symetryczny kanał mieszany” plus osobny bracket antysymetryczny.

### Co trzeba dopisać / sprawdzić

- W tabeli historii wskazać pełną przestrzeń źródłową, np. `Hom_Sn(Sym²(C¹(K_n)),Vcyc)`.
- Wyjaśnić, że dwie uporządkowane kopie `Vcyc⊗Vρ` i `Vρ⊗Vcyc` składają się w jeden blok mieszany po symetryzacji.
- Osobno podać Twierdzenie A dla `Vcyc⊗Vcyc`.

**Priorytet: P1 — tania kontrola rachunkiem charakterów.** Nie widzę tu obecnie dowodu na sprzeczność matematyczną; widzę niedookreślony zakres tabeli, który utrudnia replikację.

### Drobna korekta dowodu

W Defect §12A.4 zapisano, że `𝔰𝔬(m)` jest prosta dla każdego `m≥3`. To fałsz dla `m=4`: `𝔰𝔬(4)` jest półprosta, ale nie prosta. Ponieważ do niezerowości bracketu wystarcza nieabelowość, w tym miejscu należy użyć słabszego i prawdziwego stwierdzenia. Przypadek dotyczy `n=5`, bo `m=n−1`.

---

## 5. Hipoteza H1 — niezależne odtworzenie operatora Hilberta

**Miejsce:** Defect §12H.2–§12H.3, §12H.8.

Repozytorium nie zawiera osobnego pliku `P₀-Hilbert`; w drzewie jest tylko Defect v0.8 z osadzoną sekcją §12H. Dlatego mogę sprawdzić poprawność rachunku widocznego w §12H, ale nie mogę potwierdzić, czy transfer zachował całą treść oryginalnego korzenia Hilbert.

### Jawna rekonstrukcja

Przyjmuję kolejność krawędzi:
`01, 02, 03, 12, 13, 23`,
a orientację każdej krawędzi `i<j` jako `i→j`.

Macierz incydencji:
```text
d = [
 [-1,  1,  0,  0],
 [-1,  0,  1,  0],
 [-1,  0,  0,  1],
 [ 0, -1,  1,  0],
 [ 0, -1,  0,  1],
 [ 0,  0, -1,  1]
]
```

Cztery cykle trójkątne, z konsekwentną orientacją:
```text
C = [
 [1, -1,  0,  1,  0,  0],   # 0-1-2-0
 [1,  0, -1,  0,  1,  0],   # 0-1-3-0
 [0,  1, -1,  0,  0,  1],   # 0-2-3-0
 [0,  0,  0,  1, -1,  1]    # 1-2-3-1
]
```

Dla `P_cyc = I - d(dᵀd)^+dᵀ` rachunek dokładny daje:
`CᵀC = 4P_cyc`,
`rank(C)=3`,
a widmo `CCᵀ` wynosi `{0,4,4,4}`.

To potwierdza R3-1 przy podanej konwencji orientacji. Wniosek jest niezależny od wyboru znaków poszczególnych wierszy C, o ile każdy wiersz nadal opisuje właściwy cykl; jednak jawna macierz powinna znaleźć się w specyfikacji, żeby replikator nie musiał odgadywać orientacji.

**Priorytet: P1 — bardzo tani test algebraiczny.**

---

## 6. Hipoteza H2 — brak przecięcia torusa równych amplitud z exact ma krótki dowód

**Miejsce:** Defect §12H.5.

Twierdzenie:
`T_δ ∩ Im(d_ℂ) = ∅`, dla `δ>0`.

### Dowód geometryczny

Gdyby `z∈Im(d_ℂ`, istniałyby potencjały `x_1,…,x_4∈ℂ` takie, że `z_{ij}=x_j−x_i`. Warunek `|z_{ij}|=δ` dla wszystkich sześciu krawędzi oznaczałby, że cztery punkty `x_i` na płaszczyźnie zespolonej są parami odległe o tę samą dodatnią odległość.

Takie cztery punkty nie istnieją. Po przesunięciu i obrocie można przyjąć `x_1=0`, `x_2=δ`. Punkt `x_3` musi być jednym z dwóch przecięć okręgów o promieniu δ: `δe^{iπ/3}` lub `δe^{-iπ/3}`. Punkt `x_4` musi być tym samym punktem albo drugim przecięciem. W pierwszym przypadku `|x_3−x_4|=0`, w drugim `|x_3−x_4|=√3δ`; żaden nie daje δ. Sprzeczność.

Wynika stąd dokładnie dodatniość minimum `‖P_cyc z‖` na torusie równych amplitud, choć ten argument sam nie wyznacza jego optymalnej wartości.

**Rekomendacja:** dodać ten dowód do §12H.5. Pozwala oddzielić łatwe twierdzenie o nieosiągalności exact od trudniejszego problemu optymalizacji R3-2.

**Priorytet: P1 — prosty dowód analityczny.**

---

## 7. Hipoteza H3 — globalne minimum R3-2 i jego postać geometryczna

**Miejsce:** Defect §12H.4 i §12H.8.

W §12H podano:
`min Q_H = (3−2√2)δ²`,
czyli
`min ‖P_cyc z‖ = (√2−1)δ`.

### Co zostało potwierdzone dokładnie

Dla faz podanych w tabeli §12H.4:
`z = (1, (1−i)/√2, (1+i)/√2, (−1−i)/√2, (−1+i)/√2, i)`
w kolejności krawędzi `01,02,03,12,13,23`.

Rekonstrukcja daje:
`Cz = (1−√2, 1−√2, i(1−√2), i(1−√2))`,
więc:
`Q_H = ¼‖Cz‖² = 3−2√2`.

Zatem podana konfiguracja osiąga tę wartość **dokładnie**, nie tylko w przybliżeniu numerycznym. To dowodzi górnego ograniczenia na globalne minimum.

### Co pozostaje do dowiedzenia

Nie wykazano, że żadna inna konfiguracja faz nie daje mniejszego Q_H. 5000 startów L-BFGS-B i Differential Evolution są wsparciem numerycznym, nie dowodem globalności. W niezależnym teście Asteriona 400 losowych startów również wróciło do tej samej wartości; nie znalazłem niższego wyniku. To nadal nie zamyka globalnego problemu.

### Redukcja do czystej nierówności geometrycznej

Dla `|z_e|=δ` i `‖z‖²=6δ²`:
`Q_H(z)=6δ²−¼‖dᵀz‖²`.

Z dualności norm:
`max_{|z_e|=δ} ‖dᵀz‖ = δ · max_{x⊥1, ‖x‖=1} Σ_{i<j}|x_j−x_i|`.

Wobec tego podana wartość R3-2 jest równoważna nierówności:
`Σ_{i<j}|x_j−x_i| ≤ 2(1+√2)‖x‖`,
dla czterech punktów `x_i∈ℂ` po wycentrowaniu (`Σx_i=0`). Równość jest osiągana przez konfigurację kwadratową. To bardzo konkretny cel dowodowy: maksymalna suma sześciu odległości czterech punktów płaszczyzny przy ustalonym momencie bezwładności.

**Rekomendacja:** laboratorium powinno próbować udowodnić tę nierówność bezpośrednio. To lepszy cel niż dalsze zwiększanie liczby startów optymalizatora.

**Priorytet: P2 — istotny, ale trudniejszy dowodowo.**

---

## 8. Hipoteza F3 — twierdzenie o granicy continuum jest niedookreślone

**Miejsce:** Defect §12G.3 i Flow §7.3.

Tekst deklaruje, że istnieje skończona lista par `(𝔤,V)` z `Sym³(V) ⊇ triv`, po czym podaje same nazwy algebr: `𝔰𝔲(n), 𝔤₂, 𝔣₄, 𝔢₆`.

To nie jest jeszcze specyfikacja twierdzenia klasyfikacyjnego. Trzeba podać:
- czy `𝔤` jest prostą algebrą Liego, grupą zwartą czy jej reprezentacją;
- czy `V` jest nieprzywiedlna, wierna, rzeczywista czy zespolona;
- dokładnie które moduły `V` są rozważane;
- czy chodzi o symetryczny niezmiennik w `Sym³(V*)`, czy o alternujący 3-form w `Λ³(V*)`;
- jakie ograniczenie wymiaru i rodziny reprezentacji uzasadnia wniosek „brak nieskończonej rodziny”.

To rozróżnienie jest ważne: na przykład definiująca reprezentacja 7-wymiarowa G₂ ma kanoniczną formę alternującą 3. stopnia; nie wolno automatycznie utożsamiać jej z symetrycznym kubikiem w `Sym³(V*)`.

**Test:** napisać precyzyjne twierdzenie z listą modułów i sprawdzić je przez rozkłady `Sym³(V)` dla każdej pozycji. Dopiero z taką specyfikacją można potwierdzać negatywną granicę continuum.

**Priorytet: P2 — potencjalnie fundamentalne dla wniosku Flow, ale wymaga najpierw poprawnej definicji twierdzenia.**

---

## 9. Hipoteza F4 — skala `λ_max(Φ(x*))` wymaga normalizacji między n

**Miejsce:** Defect §12F.1; Flow §3.5–§3.6.

Defect podaje:
- K₄: `λ_max ≈ 1.155`;
- K₅: `λ_max ≈ 0.224`;
- wyjaśnienie: `Φ(x*)` skaluje się jak `1/√(n−1)`.

Jeśli porównywane są te same normy i ten sam sposób normalizacji `x*`, przejście n=4→5 według `1/√(n−1)` przewidywałoby czynnik `√(3/4)≈0.866`, a nie obserwowany iloraz około `0.194`. Możliwe, że różne `x*`, normy lub normalizacje sektorów zostały użyte dla K₄ i K₅; dokument nie podaje ich w tym miejscu wystarczająco jawnie.

**Test:**
1. wypisać `x*` dla obu n;
2. podać normę i bazę operatora Φ;
3. wyprowadzić `λ_max(n)` w tej samej normalizacji;
4. sprawdzić, czy deklarowane `1/√(n−1)` opisuje dokładny czynnik, asymptotykę czy jedynie trend.

**Priorytet: P3 — kontrola ilościowa, możliwa do wykonania po doprecyzowaniu normalizacji.**

---

## 10. Zalecana kolejność dla laboratorium

| Kolejność | Zadanie | Powód |
|---|---|---|
| 1 | Wyprowadzić od zera równania Euler–Arnolda i naprawić/wyjaśnić `[R_B,R_B]` | Możliwy błąd w kluczowym równaniu całego porównania Flow |
| 2 | Odtworzyć `d`, `P_cyc`, `C` dla K₄; dopisać jawny dowód R3-1 i geometryczny dowód R3-3 | Mały koszt, wynik ścisły i w pełni niezależny od dynamiki |
| 3 | Udowodnić globalną nierówność czterech punktów dla R3-2 | Domyka centralny wynik Hilberta, zamiast mnożyć próby numeryczne |
| 4 | Rozdzielić Tw. A od klasyfikacji `Sym²(C¹)→V_cyc`; sprawdzić krotności ogólnie w n | Usuwa niejasność w rejestrze reprezentacji |
| 5 | Sprecyzować klasyfikację kubików continuum i dopiero potem sprawdzać ją dla rodzin algebr | Weryfikacja wymaga jednoznacznego twierdzenia |
| 6 | Ujednolicić normalizację Φ i przetestować `1/√(n−1)` | Kontrola skalowania po rozstrzygnięciu definicji |

## 11. Ograniczenia i rozdzielenie wniosków

- Nie znaleziono w bieżącym drzewie repozytorium osobnego źródła P₀-Hilbert. Nie twierdzę więc, że §12H zawiera cały pierwotny korzeń.
- Rachunek macierzowy R3-1 i geometria R3-3 są niezależnymi wynikami Asteriona dla jawnie zadanej orientacji.
- R3-2 ma dokładnie odtworzoną konfigurację osiągającą kandydującą wartość, ale globalność minimum pozostaje do dowodu.
- Wniosek o problemie `[R_B,R_B]` dotyczy standardowego bracketu Liego. Jeżeli źródło używa innego operatora, musi go zdefiniować.
- Nie zmieniono statusów Vibe'a, treści korzeni ani `main`.

**Następny kierunek audytu:** po rozliczeniu punktu F1 przejść do Net ↔ Memory, ale pozostawić H3 (globalne minimum R3-2) jako osobne zadanie matematyczne, niezależne od dalszego przeglądu architektury.
