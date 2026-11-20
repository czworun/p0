# Audyt Asteriona: Scalar ↔ Centroid ↔ TAU

**Data:** 2026-11-20  
**Baza:** `main` @ `ff5345f50f509ff95fafcd1e4b28ce64b388eb1c`  
**Gałąź audytowa:** `audit/asterion-scalar-centroid-tau-2026-11-20`  
**Zakres:** P₀-Scalar v0.3.5, adnotacja P₀-Centroid v5.2, P₀-TAU v1.7.2 oraz deklaracja absorpcji w P₀-Defect v0.8.  
**Charakter:** audyt źródeł i rachunku; nie jest decyzją statusową laboratorium. Nie zmieniono korzeni ani rejestru.

## 1. Wynik w skrócie

Węzeł Scalar–Centroid–TAU zawiera dwa ścisłe mosty operatorowe i jeden ważny problem asymptotyczny.

1. **P₀-CS1 — pełna trajektoria:** warunek `ε > diam(R₀)` wystarcza, aby trajektoria A2 pozostała w reżimie pełnego grafu. Wynika to bezpośrednio z niezmienniczości otoczki wypukłej podczas aktualizacji średnią. W konsekwencji korespondencja Scalar–Centroid zachodzi na całej trajektorii, nie tylko w pierwszym kroku.
2. **S10 ↔ TAU 7.3.6 przy α=1:** wagi granicznego konsensusu są identyczne dokładnie, po normalizacji: `2k/[n(n+1)]`. To nie jest analogia, lecz ten sam niezmiennik zapisany w dwóch parametryzacjach.
3. **S11-A:** równanie graniczne Scalar jest zgodne z równaniem Centroid i układem TAU, ale wartość `|λ|=1/8` oraz wynikający z niej kąt są błędne. Poprawny niebanalny pierwiastek ma moduł około `0.123830322719` i argument około `67.5118449501°`. W TAU wartość `67.40°` jest z kolei niezgodna z własnym układem równań zapisanym w §7.4.9.
4. **Dowód S11 w Scalar ma lukę dla parzystego n:** Centroid v5.2 zawiera poprawioną analizę, której brakuje w Scalar. Dla parzystego n istnieje jeden ujemny pierwiastek pomocniczej zmiennej `w`; nie wolno go wykluczać.

Wniosek audytowy: priorytetem nie jest eksperyment symulacyjny. Najpierw należy wykorzystać dokładne dowody operatorowe, następnie ujednolicić asymptotykę i poprawić rachunek S11. Dopiero potem warto uruchamiać kosztowniejsze testy numeryczne.

---

## 2. H1 — pełna trajektoria P₀-CS1 wynika z niezmienniczości otoczki wypukłej

**Źródła:** Scalar §2.2, §3.1–§3.3; Centroid v5.2, definicja operatorów `M_i` i pełnej rundy `R_n`.

### Obserwacja

Scalar §3.1–§3.2 dowodzi, że dla pojedynczego stanu o `ε > diam(R)` każda aktualizacja A2 jest dokładnie operatorem Centroid, a pełna runda jest `R_n`. Scalar §3.3 pozostawia jednak pełną trajektorię jako 🔍 i wskazuje potrzebę dowodu, że średnica nie przekracza ε.

### Hipoteza do sprawdzenia

Jeżeli `diam(R₀) < ε`, to dla każdej kolejnej aktualizacji A2 zachodzi `diam(R_t) ≤ diam(R₀) < ε`. Wobec tego każda aktualizacja w każdej rundzie pozostaje aktualizacją pełnografową.

### Dowód

Niech `m₀ = min_i r_i(0)` i `M₀ = max_i r_i(0)`. Przy założeniu `diam(R₀)<ε` wszystkie węzły są wzajemnie sąsiadami. Pierwsza aktualizacja zastępuje jedną współrzędną średnią wszystkich bieżących współrzędnych. Średnia należy do przedziału `[m₀,M₀]`; pozostałe współrzędne już w nim leżą.

Po aktualizacji cały wektor nadal należy więc do `[m₀,M₀]^n`. Ten sam argument stosuje się indukcyjnie do każdej kolejnej aktualizacji. Zatem dla każdego czasu dyskretnego `t`:

`m₀ ≤ r_i(t) ≤ M₀` dla wszystkich i, a więc `diam(R_t) ≤ M₀-m₀ < ε`.

Wszystkie kroki pozostają pełnograficzne. Z lematu Scalar §3.1 każda aktualizacja jest dokładnie odpowiednim `M_i`; po rundzie otrzymujemy dokładnie `R_n`. Pełna trajektoria Scalar A2 i Centroid jest identyczna.

### Minimalny test kontrolny

- Dowolne `n ≥ 2`, dowolny wektor rzeczywisty i dowolne `ε > diam(R₀)`.
- Po każdej pojedynczej aktualizacji sprawdzić `diam(R_t) ≤ diam(R₀)`.
- Porównać stan po każdej rundzie z iteracją macierzy `R_n`, nie tylko stan końcowy.

Test numeryczny jest kontrolą implementacji; zasadniczy argument jest analityczny.

**Rekomendacja:** przygotować krótką erratę/propozycję dowodu do Scalar §3.3. Nie zmieniać statusu w repo — decyzja należy do Vibe'a.

---

## 3. H2 — S10 Scalar i granica TAU przy α=1 są tym samym niezmiennikiem

**Źródła:** Scalar §2.4; Centroid v5.2, Tw. 7.1 i część o S10; TAU §7.3.1–§7.3.6.

### Rachunek zgodności

Scalar podaje lewy wektor własny rundy pełnograficznej:
`c_k = k/n`, dla `k=1,…,n`.

Suma wag wynosi:
`Σ(k/n) = (n+1)/2`.

Po normalizacji otrzymujemy:
`c_k / Σc = 2k/[n(n+1)]`.

TAU §7.3.6 podaje:
`w_k(α,n) = [1 + (α/n)(k−n)] / [n − α(n−1)/2]`.

Dla `α=1` licznik upraszcza się do `k/n`, a mianownik do `(n+1)/2`. Zatem:
`w_k(1,n) = 2k/[n(n+1)]`.

To dokładnie znormalizowany niezmiennik S10. Centroid v5.2 podaje tę samą graniczną średnią ważoną:
`2Σ k r_k/[n(n+1)]`.

### Zakres zgodności

- Zgodność jest dokładna dla pełnego grafu i tej samej kolejności aktualizacji.
- TAU uogólnia rodzinę na `α ≠ 1`; Scalar S10 jest szczególnym punktem `α=1`.
- Nie należy przenosić tej równości na grafy niepełne, inne harmonogramy lub konwencję exclude-self bez osobnego dowodu.
- Indeksowanie Scalar `1,…,n` odpowiada indeksowaniu Centroid `0,…,n−1` po przesunięciu o jeden.

### Test kontrolny

Dla małych `n` (np. 2–8) wyprowadzić dokładne macierze rundy i sprawdzić:
1. `cᵀR_n = cᵀ`;
2. `R_n^k x₀ → (w(1,n)ᵀx₀)·1`;
3. zgodność symboliczna współczynników, a nie tylko wartości zmiennoprzecinkowych.

**Rekomendacja:** traktować jako jeden wspólny most twierdzeniowy do niezależnej replikacji, nie jako trzy niezależne hipotezy.

---

## 4. H3 — asymptotyka S11-A: poprawne równanie, błędna wartość Scalar i błędna liczba kątowa TAU

**Źródła:** Scalar §6.3 i §9; Centroid v5.2 §11.7; TAU §7.4.9.

### Równanie graniczne

Centroid wyprowadza z równania `μⁿ=λ` i `μ=1+(λ−1)/(nλ)`, w granicy `n→∞`:

`λ = exp(1 − 1/λ)`.

Jest to równoważne równaniu Scalar:
`λ exp(1/λ) = e`.

Zatem samo równanie graniczne Scalar jest zgodne z Centroid. Błąd pojawia się w wyborze/ocenie niebanalnego rozwiązania: Scalar przyjmuje `|λ|=1/8`, a następnie wyprowadza z tego kąt około `67.38°`. To przybliżenie nie spełnia równania granicznego.

Niebanalny pierwiastek z gałęzi `W₁`:
`λ∞ = −1/W₁(−1/e)`
ma wartość numeryczną:
- Re(λ∞) = 0.0473641607289
- Im(λ∞) = 0.1144140948622
- |λ∞| = 0.123830322719
- arg(λ∞) = 67.5118449501°

Wynik jest zgodny z wartością Centroid v5.2: `0.1238` i `67.512°`.

### Kontrola równania TAU

TAU §7.4.9 zapisuje układ:
`cos θ = r(1−ln r)`
`θ − sin θ/r = −2π`.

Numeryczne rozwiązanie układu (wysoka precyzja) daje:
- r = 0.123830322718995…
- θ = 67.511844950072…°

To potwierdza moduł TAU, ale nie kąt wydrukowany w TAU (`67.40°`). Po podstawieniu `r=0.123830322719` i `θ=67.40°` reszty równań wynoszą odpowiednio około `1.8029·10⁻³` i `4.0918·10⁻³`, zdecydowanie więcej niż błąd zaokrąglenia. Dla `67.511845°` reszty są rzędu `10⁻⁹` lub mniejsze.

### Co z tego wynika

- Scalar: błędne są deklaracja `|λ|∞=1/8` i kąt z niej wyliczony; równanie graniczne pozostaje zgodne.
- Centroid: podaje właściwy pierwiastek i kąt.
- TAU: układ równań prowadzi do tego samego pierwiastka, ale zapis `67.40°` wymaga korekty liczbowej.
- Zbieżność skończonych pierwiastków do rozwiązania granicznego nadal wymaga rygorystycznego domknięcia (np. twierdzenia Hurwitza/Rouché), co Centroid sam wskazuje jako brakujący krok.

### Test rozstrzygający

1. Wyznaczyć dla kolejnych n właściwy pierwiastek zespolony wielomianu Centroid, z jawną regułą śledzenia gałęzi.
2. Liczyć z precyzją rosnącą z n, aby oddzielić błąd numeryczny od zbieżności.
3. Porównać osobno moduł i argument z `λ∞`.
4. Następnie uzupełnić dowód analityczny zbieżności pierwiastków, zamiast uznawać samą zgodność numeryczną za dowód.

**Rekomendacja:** wysoki priorytet. To wspólna hipoteza asymptotyczna, ale wymaga dwóch rozdzielonych rozliczeń: poprawności równania granicznego oraz zbieżności konkretnej gałęzi pierwiastków.

---

## 5. H4 — luka w dowodzie S11 dla parzystego n

**Źródła:** Scalar §6.2; Centroid v5.2 §11.7.

W Scalar krok 2 wyklucza ujemne rzeczywiste `w` także dla parzystego `n`, twierdząc, że dla `w=-t` i `0<t<1` zachodzi `f(-t)<C`. To nie jest prawdą na całym przedziale: dla parzystego n funkcja
`f(-t)=(1−t)^(n+1)/t^n`
dąży do +∞, gdy `t→0⁺`, i do 0, gdy `t→1⁻`. Jest więc dokładnie jedno przecięcie poziomu C. Odpowiada mu jeden rzeczywisty pierwiastek pomocniczej zmiennej w.

Centroid v5.2 poprawia ten fragment: dla parzystego n funkcja jest ściśle malejąca na `(0,1)`, a więc ma dokładnie jeden pierwiastek ujemny w. Liczba pierwiastków nierzeczywistych wynosi wtedy `n−2`, nadal co najmniej dwa dla parzystego `n≥4`. Dla nieparzystego n jest ich `n−1`.

### Rekomendowany test

- Odtworzyć dowód dla n nieparzystego i parzystego osobno.
- Sprawdzić dokładnie przypadek n=4, w tym rzeczywisty pierwiastek λ≈0.1347 podany w Centroid.
- Sprawdzić, że twierdzenie „co najmniej jedna para zespolona dla każdego n≥3” wynika z poprawionego rachunku.

**Rekomendacja:** naprawić dowód Scalar przez przeniesienie poprawnej argumentacji Centroid, zachowując ślad pierwotnego błędu. Nie ma podstaw do odrzucenia samego twierdzenia S11 na podstawie tej luki.

---

## 6. Kolejność badań dla laboratorium

| Kolejność | Hipoteza / zadanie | Metoda | Dlaczego teraz |
|---|---|---|---|
| 1 | P-CS1: pełna trajektoria pozostaje pełnograficzna | Krótki dowód otoczki wypukłej; kontrola macierzowa n=2–8 | Najtańsze, usuwa zbędną niepewność w Scalar↔Centroid |
| 2 | S10 = TAU α=1 = Centroid | Rachunek symboliczny i dokładne macierze | Domyka wspólny most operatorowy |
| 3 | S11 dla parzystego i nieparzystego n | Poprawa dowodu; kontrola n=3,4,5,6 | Wykryta konkretna luka w Scalar |
| 4 | S11-A: właściwy pierwiastek i zbieżność n→∞ | Wysoka precyzja + śledzenie gałęzi + Hurwitz/Rouché | Najważniejsza nierozstrzygnięta kwestia ilościowa |
| 5 | Wpływ permutacji i przejście poza pełny graf | Dopiero po 1–4; oddzielne harmonogramy i grafy | Nie mieszać własności pełnego Kₙ z dynamiką grafów progowych |

## 7. Granice wnioskowania

- Ten audyt nie potwierdza całej architektury Scalar ani programu emergencji domen.
- Dowód P-CS1 dotyczy wyłącznie A2, średniej ze wszystkich bieżących współrzędnych, ustalonego ε i warunku `ε > diam(R₀)`.
- Zgodność S10–TAU dotyczy α=1, pełnego grafu i zgodnej kolejności aktualizacji.
- Zbieżność pierwiastków do granicy wymaga odrębnego dowodu; zgodność dwóch zapisów równania granicznego nie zamyka tego kroku.
- Nie rozstrzygam pozycji architektonicznej Scalar ani deklaracji „wchłonięty do Centroid”. To osobna decyzja laboratorium; niniejszy raport dostarcza materiału matematycznego do jej podjęcia.

**Następny etap audytu:** Defect ↔ Flow ↔ Hilbert, zaczynając od sprawdzenia, czy transfer §12A–§12H zachowuje definicje operatorów, zakresy twierdzeń i warunki brzegowe, a nie tylko końcowe wnioski.
