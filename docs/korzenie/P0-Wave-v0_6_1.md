# Korzeń: P₀-Wave — adnotacja (v0.6.1, 2026-08-12)

**Dokument filarowy:** „P₀-Wave: Dynamika Słów Relacyjnych" v0.6.1 (2026-08-12) — filar 2 trylogii (Centroid · Wave · Net); baza: P₀-Centroid v4.9.5 (rodowód baz: v4.9.5 tu → v4.9.6 u Alchemy → v5.1 → audyt v5.2 z 2026-09-29). **Okres:** prace VII–VIII 2026, sprzed warsztatu. **Zasada repo:** adnotacja szefa lab. + pełny dokument verbatim (wzorzec Alchemy/Relacje). **Uwaga architektoniczna:** trylogia deklaruje świadomą jednokierunkowość (fundament dla Philosophy/Applications/Experiments/Origins, nie odwrotnie); liczba filarów faluje między dokumentami (tytuł §0 „fundament siedmiu filarów" vs treść „ośmiu komplementarnych filarów") — do skonfrontowania przy wpięciu PILLARS-TABLE.

## Co bada ten korzeń

Zmianę paradygmatu: fundamentalnym obiektem nie jest operator, lecz **słowo** — skończona sekwencja nad alfabetem Σ = {M₀, M₁, M₂, M₃, T}, z konwencją ρ(w) = a_L···a₂a₁ (doklejanie litery z prawej = mnożenie z lewej, jawna konwencja). T = cykliczna permutacja wierzchołków (0123): T𝟏 = 𝟏, izometria, nie komutuje z M_i (‖[M_i, T]‖ ≈ 1,22), **zewnętrzny względem 𝔤₄**. Pytanie przewodnie: które mody |λ| = 1 na części relacyjnej V_ρ **przetrwają relacyjnie** po doklejaniu kolejnej litery (definicja przetrwania §3.2, z pułapką λ = 1: wymaga krotności ≥ 2).

## Twierdzenia domknięte (✅)

- **Kryterium projektorowe (mod prosty, λ ≠ 1):** λ przetrwa po M_m ⟺ 1 ∈ spec(P M_m P) ⟺ v_m l_m = 0; 14 220 testów, 0 kontrprzykładów (towarzyszący lemat V-Z: 🔍, 24/24).
- **Kryterium wektorowe (mod prosty, λ = 1):** λ = 1 przetrwa ⟺ (v_ρ)_m = 0 — w pełni dowiedzione (Krok 2 + Lemat W-L); 16 468 testów, 0 kontrprzykładów.
- **Lemat W-L (W9, ✅ 2026-08-10):** domknięty dowodem przez indukcję po długości słowa **na poziomie łańcucha Markowa** (Lemmaty A/B/C, każdy zweryfikowany dokładnie: 0/20 000, 0/3990, 0/80 000; przy Lemmacie C jawna korekta kierunku relabelingu: i ↦ (i−1) mod 4, nie i+1); dowód silniejszy niż wymagany (dowolna liczba klas rekurencyjnych > 1, nie tylko dwie).
- **Stabilizator alfabetu:** S₄ to dokładnie stabilizator Σ w O(3) — izolowany zbiór dokładnych rozwiązań RΣR⁻¹ = Σ (infimum = 0 nieosiągnięte poza S₄: sprzężenia dowolnie bliskie, nigdy dokładne); własność czysta algebry Wave, choć odkryta przy pytaniu sieciowym N9/N10 (dowód w P₀-Net).

## Koncesje i sęki (obalenia — trwałe)

- **Symetria prawy/lewy (W2) ❌:** v_m = 0 ⟺ l_m = 0 sfalsyfikowana — 8 056 asymetrii na 30 192 testach; prawy i lewy wektor własny to nie to samo.
- **„Dowód" v0.5 ❌ wycofany:** rachunek oparty na 𝟏ᵀM_m = (5/4)𝟏ᵀ − e_mᵀ redukował się do tautologii (0 = 0) i nie wymuszał u_m = 0; erratum wzorcowe z jawną konstrukcją (z = u + 4u_m e_m spełnia M_m z = u niezależnie od u_m).
- **Hipoteza j = (m + t) mod 4 ❌:** pozycja zerowej współrzędnej V_1 zależy także od liter po pierwszym M — kontrprzykład „T0TTT" od L = 5 (720/1076 zgodności: kuszące, ale fałszywe).
- **Typ A (< 1% słów propagacyjnych):** artefakt brzegowy (zamrożona współrzędna), nie zachowanie reprezentatywne.

## Struktury odkryte (🔍)

- **Moduły zdegenerowane mają zawsze strukturę „1+3":** V_1 = {u ∈ V_ρ : u_j = 0} dla dokładnie jednego j — nigdy „2+2" (0/1076 na wszystkich słowach L ≤ 9); **moduły zdegenerowane są stabilniejsze**: nie mają „martwych liter", które zabijają λ = 1 (wymiarowe uzasadnienie: codim hiperpłaszczyzny u_m = 0 w V_ρ wynosi 1 < dim V_1).
- Katalog: 195 768 słów L ≤ 8 (zawierających wszystkie M_i) → 1 328 propagacyjnych; zanik koherencji ∝ e^{−0,085L} (przeniesione z v0.1).

## Mosty do pnia i warsztatu (odczytanie interpretacyjne, 💡)

- **S₄ po raz trzeci w rodzinie filarów:** Aut(𝔤₄; {Mᵢ}) ≅ S₄ (audyt Centroid v5.2 §8.1), stabilizator Σ w O(3) (tu), stabilizator {δ(M_m)} = S₄ (Alchemy §7 przez Centroid §8.1/Net N9) — jedna rodzina symetrii K₄ do zestawienia w atlasie pnia; izolację z infimum = 0 czytam: symetria algebraiczna jest dyskretna, ciągłe przybliżenia nie docierają nigdy dokładnie.
- **Słowo zamiast operatora:** kolejność liter = historia, dokładnie ten zwrot co „kolejność daje fazę" w Centroid i asymetria rund w pniu (C2); tuż obok — hierarchia czasowa §13 Centroid jako kontekst, słowo jako historia na jednym poziomie.
- **Lemat W-L jako wzorzec metodologiczny:** gdy algebra liniowa trywializuje się do tautologii (v0.5), zmienić POZIOM OPISU (słowo jako macierz stochastyczna; klasy rekurencyjne łańcucha Markowa) zamiast dopowiadać brakujący argument — ta sama rodzina ruchów co mechanizmy blokowe warsztatu: dowód musi mieszkać w strukturze, nie w rachunku.
- **Asymetria prawy/lewy (W2 ❌):** echo „równe normy ≠ ten sam stan" i chiralności z konwencji (C2) — kierunki w V_ρ nie są zamienne.
- **Automat projektorowy (§5, 💡):** stan = projektor, nie widmo (widmo niedeterministyczne; widmo + rangi tylko 60% determinizmu); jeśli projektor jest fundamentalniejszy, naturalnym globalnym stanem sieci jest **sekcja projektowa** — most do Net i kandydat struktury stanu dla P₀-AI.
- **Analogia QED/propagacji (💡, oznaczona w dokumencie jako kontekst, nie twierdzenie):** intuicyjny korzeń gałęzi optycznej (H-OPTYKA, Φ_D).

## Sęk-odnogi (bank nasion z korzenia)

1. **W1:** kierunek ⇒ kryterium geometrycznego dla modułów zdegenerowanych — ogólny dowód wykluczenia u_m ≠ 0 (domknięty dla klas M i I; Lemat Z-D 🔍).
2. **W10 (Z-D):** ogólny wzór na j w strukturze „1+3" (kontrprzykłady pokazują zależność od pełnego słowa, nie tylko prefiksu).
3. **W4:** orbita projektorów względem S₄; **W5:** determinizm automatu projektorowego (zalecenie dokumentu: najpierw kryteria, potem ewentualna teoria języka formalnego — nie odwrotnie); **W6:** działanie T na projektorach; **W7:** prezentacja półgrupy Σ; **W8:** słowa defektywne (Jordana) poza L ≤ 12 (brak w L ≤ 12).
4. **Zależności odblokowane:** Lemat W-L (W9) blokował Applications A1/A2 i Experiments E-03/E-04 — po domknięciu ścieżka otwarta (kolejka uploadów: Applications, Experiments).
5. **Trylogia:** punkty wspólne z Net (N9/N10) do rozliczenia przy wpięciu Net i PILLARS-TABLE.

## Statusy: mapa legendy na konwencje warsztatu

Legenda identyczna z Alchemy (✅ Dowiedzone · 📚 Klasyczne · 🔍 Zweryfikowane · 💡 Przypuszczenie · ❌ Sfalsyfikowane) oraz te same zasady redakcyjne i niezależności; historia wersji §9 z wycofanym dowodem v0.5 i wyraźnym erratum to wzorzec uczciwej erraty sprzed warsztatu (tautologia nazwana tautologią, konstrukcja podana, statusy cofnięte do 🔍). Mapowanie na Z1: dowody = twierdzenia (do niezależnej replikacji); „zweryfikowane dokładnie" z pojedynczego kodu = 🔍 warsztatowe.

## Dokument verbatim (v0.6.1, bez zmian)

# P₀-Wave: Dynamika Słów Relacyjnych

### Filar 2 serii P₀ — Lokalna ewolucja i propagacja

**Wersja:** 0.6.1  
**Baza:** P₀-Centroid v4.9.5 (zakładana znajomość — algebra 𝔤₄, rozkład Schura, operatory M_m, runda R₄, podalgebra rotacyjna §2.5, hierarchia czasowa §13).  
**Data:** 2026-08-12  
**Status:** Korekta redakcyjna v0.6.0→v0.6.1 — dodano w §6 odnośnik do P₀-Net N9/N10 (stabilizator alfabetu Σ w O(3) jest własnością Wave, odkrytą przy pytaniu sieciowym). Treść matematyczna §4.3bis (Lemat W-L) bez zmian.

---

## 0. P₀ jako trylogia i fundament siedmiu filarów

Seria P₀ składa się z ośmiu komplementarnych filarów — zobacz [`PILLARS-TABLE.md`](PILLARS-TABLE.md) dla aktualnej listy, wersji i statusów.

**Świadomość architektoniczna.** Dokumenty trylogii (Centroid, Wave, Net) deklarują się jako „trylogia" w §0 każdego z nich. Jest to **świadoma jednokierunkowość**, nie przeoczenie: trylogia stanowi zamknięty fundament matematyczny, na którym budowane są późniejsze warstwy (Philosophy, Applications, Experiments, Origins), ale sama nie zależy od nich. Przy kolejnych rewizjach warto to nazwać wprost, aby nie wyglądało na niedopatrzenie.

**Zasada niezależności.** Każdy filar może być czytany i weryfikowany autonomicznie. P₀-Wave opisuje lokalną dynamikę — sekwencję operacji na jednym lokalnym modelu P₀. Nie zakłada z góry istnienia sieci ani transportu między modelami. Wszystkie wyniki dotyczą pojedynczej kopii $\mathbb{R}^4$ z operatorem $\rho(w) \in \mathrm{End}(\mathbb{R}^4)$.

**Zasada redakcyjna.**

> Żadne zdanie w prozie nie może twierdzić więcej, niż mówi status twierdzenia, którego dotyczy.

Statusy: ✅ Dowiedzione · 📚 Klasyczne · 🔍 Zweryfikowane numerycznie lub symbolicznie (bez dowodu ogólnego) · 💡 Przypuszczenie · ❌ Sfalsyfikowane (odrzucone po weryfikacji).

---

## 1. Zmiana paradygmatu: od operatora do słowa

Dotychczas (§1–13 Centroid) analizowano pojedyncze operatory ($M_m$, $R_4$, $\exp(tK)$).

**Hipoteza wyjściowa (💡).** Fundamentalnym obiektem nie jest operator, lecz **słowo** — skończona sekwencja lokalnych operacji nad alfabetem
$$\Sigma=\{M_0,M_1,M_2,M_3,T\}.$$
Operator jest interpretacją słowa. Przyjęta konwencja: dla słowa w=(a₁,…,a_L) odpowiadająca mu macierz to
$$\rho(w)=a_L\cdots a_2 a_1\in\mathrm{End}\mathbb R^4.$$
Doklejenie litery b z prawej odpowiada mnożeniu z lewej: w'=(w,b) ⟹ ρ(w')=b·ρ(w).

**Uwaga względem P₀-Net.** Słowo w P₀-Wave jest ciągiem operacji **wewnątrz jednego lokalnego modelu**. P₀-Net bada, jak ten sam słowo (lub jego fragmenty) mogą być transportowane między kopiami modelu. Wave nie zakłada istnienia takiego transportu — jest teorią czysto lokalną.

---

## 2. Operator transportu T

**Definicja.** T = cykliczna permutacja wierzchołków (0 1 2 3), tj. Te_i=e_{i+1 mod 4}.

**Fakty (🔍, zweryfikowane bezpośrednim rachunkiem):**
- T𝟏 = 𝟏 (zachowuje p₀, tak jak każdy M_m).
- TᵀT = I (T jest izometrią).
- [M_i,T]≠0 dla każdego i (sprawdzone: norma komutatora ≈1,22).

T nie należy do algebry 𝔤₄ — jest zewnętrznym generatorem.

**Powiązanie z P₀-Net.** W kontekście sieci lokalnych modeli, T może być interpretowany na dwa sposoby: (a) jako operator wewnętrzny w jednym modelu (obecny dokument), lub (b) jako operator transportu między braćmi w drzewie (P₀-Net, status 💡). Wave traktuje T wyłącznie w sensie (a).

---

## 3. Słowo propagacyjne i jego klasy

**Definicja.** Słowo w jest *propagacyjne*, jeśli ρ(w) ma co najmniej jedną wartość własną λ spełniającą |λ|=1 na części relacyjnej V_ρ (tzn. odpowiadającą wektorowi własnemu nierównoległemu do 𝟏).

### 3.1. Klasyfikacja Typ A vs Typ B

| | **Typ A — degenerowany** | **Typ B — relacyjny** |
|---|---|---|
| Przykład | TM₃TM₂TM₁TM₀ | 02T13T |
| spec | {1,1,1,1/256} | {−0,02, 0,196, 1, −1} |
| rank(W−I) | 1 | 3 |
| Mechanizm | Jedna współrzędna „zamrożona" — wiersz macierzy jednostkowy | Pełne mieszanie, brak wyróżnionej współrzędnej |
| Status | Wyjątek brzegowy (mechaniczny artefakt) | Reprezentatywne zachowanie |

**Fakt (🔍).** W katalogu L≤8 (195 768 słów zawierających wszystkie M_i) znaleziono 1 328 słów propagacyjnych. Frakcja Typ A wśród nich: <1%.

### 3.2. Precyzja: przetrwanie relacyjne

**Konwencja (definicja).** Niech λ będzie wartością własną słowa W. Mówimy, że λ *przetrwa relacyjnie* po doklejeniu M_m, jeśli w macierzy M_m W istnieje wartość własna λ z wektorem własnym nierównoległym do 𝟏.

**Uwaga krytyczna (v0.3).** Dla λ=1 definicja wymaga ostrożności: p₀=⟨𝟏⟩ zawsze daje λ=1. Zatem λ=1 przetrwa relacyjnie iff krotność geometryczna λ=1 w M_m W wynosi co najmniej 2. Ponadto, jeśli prawy wektor własny v zwrócony przez procedurę numeryczną nie jest ortogonalny do 𝟏, należy go zrzutować na V_ρ przed testem kryterialnym.

---

## 4. Kryterium projektorowe i wektorowe

### 4.1. Formuła ogólna (modu proste λ≠1)

Niech W będzie słowem, λ prostą wartością własną W na V_ρ z |λ|=1, λ≠1. Niech v — prawy wektor własny, l — lewy wektor własny (lᵀv=1, lᵀ𝟏=0), P=vlᵀ — projektor spektralny.

**Twierdzenie (✅, v0.2).** Dla każdego m∈{0,1,2,3}:
$$\lambda\text{ przetrwa relacyjnie po }M_m\quad\iff\quad 1\in\operatorname{spec}(P M_m P)\quad\iff\quad v_m l_m = 0.$$

**Weryfikacja numeryczna (🔍):** 14 220 testów (L≤12), 0 kontrprzykładów.

**Uwaga o rzucie na V_ρ (v0.5).** W praktyce numerycznej prawy wektor własny v może mieć drobną składową wzdłuż 𝟏. Zamiast testować $v_m l_m = 0$ bezpośrednio, należy zastąpić $v$ przez $v_\rho = v - \frac14(\mathbf 1^\top v)\mathbf 1$ i testować $(v_\rho)_m l_m = 0$. Ponieważ $l \in V_\rho$ (lewy wektor własny dla λ≠1 zawsze ma $l^\top \mathbf 1 = 0$), mnożenie przez $l_m$ eliminuje składową wzdłuż 𝟏. W przypadku idealnym $v_\rho = v$, ale formuła z $v_\rho$ jest numerycznie stabilniejsza i nie wymaga Lematu V-Z.

**Uwaga o ukrytym lemacie (v0.3.1).** Dowód v0.2 §4.2 (Krok 2 ⇒) polega niejawnie na fakcie, że prawy wektor własny v dla |λ|=1, λ≠1 (praktycznie: λ=−1) leży w V_ρ (tzn. 𝟏ᵀv=0). Weryfikacja numeryczna (24/24 przypadków w katalogu L≤12) potwierdza ten fakt; ogólne uzasadnienie pozostaje otwarte (lemat V-Z, status 🔍). Nie wpływa to na poprawność kryterium, które działa z $v_\rho$.

### 4.2. Formuła dla λ=1 relacyjnego

Niech W będzie słowem, λ=1 prostą wartością własną W na V_ρ. Niech v będzie prawym wektorem własnym (zwróconym przez procedurę numeryczną). Zdefiniujmy **rzut na V_ρ**:
$$v_\rho = v - \frac{1}{4}(\mathbf 1^\top v)\,\mathbf 1.$$
Zachodzi v_ρ∈V_ρ (bo 𝟏ᵀv_ρ=0) oraz W v_ρ = v_ρ (bo W𝟏=𝟏 i Wv=v).

**Twierdzenie (✅ Krok 2; 🔍 Krok 3, v0.5.2).** Dla każdego m∈{0,1,2,3}:
$$\lambda=1\text{ przetrwa relacyjnie po }M_m\quad\iff\quad (v_\rho)_m = 0.$$

**Równoważność:** Ponieważ v_ρ∈V_ρ, zachodzi M_m v_ρ = v_ρ iff (v_ρ)_m = 0 (z definicji M_m, §6 Centroid).

**Weryfikacja numeryczna (🔍):** 16 468 testów (L≤12), 0 kontrprzykładów.

**Status dowodu.** Krok 2 (⇐) jest udowodniony formalnie. Krok 3 (⇒) wymagał lematu W-L — **domkniętego w §4.3bis (2026-08-10)**. Pełne twierdzenie ma status ✅: implikacja w lewo i w prawo są teraz oba dowiedzione.

### 4.3. Dowód (λ=1) i postęp częściowy

**Krok 1 (rzut).** W v=v i W𝟏=𝟏 implikują W(v−a·𝟏)=v−a·𝟏 dla dowolnego a∈ℝ. Wybierając a=(𝟏ᵀv)/4, otrzymujemy v_ρ∈V_ρ z W v_ρ=v_ρ.

**Krok 2 (⇐, ✅).** Jeśli (v_ρ)_m=0, to M_m v_ρ=v_ρ (bo v_ρ∈V_ρ, więc (M_m v_ρ)_i=(v_ρ)_i dla i≠m oraz (M_m v_ρ)_m=0=(v_ρ)_m). Wtedy M_m W v_ρ=M_m v_ρ=v_ρ. Ponieważ v_ρ∈V_ρ i 𝟏 są liniowo niezależne, krotność λ=1 w M_m W wynosi co najmniej 2. Zatem mod przetrwał relacyjnie.

**Krok 3 (⇒, 🔍).** Załóżmy, że λ=1 przetrwa relacyjnie po M_m. Istnieje więc u∈V_ρ, u≠0, takie że M_m W u=u. Z definicji M_m:
- dla i≠m: (Wu)_i = u_i,
- dla i=m: ¼(𝟏ᵀWu) = u_m.

Sumując pierwsze równanie po i≠m i używając u∈V_ρ: 𝟏ᵀWu − (Wu)_m = −u_m. Z drugiego równania: 𝟏ᵀWu = 4u_m. Stąd (Wu)_m = 5u_m, więc
$$Wu = u + 4u_m e_m. \tag{3}$$

Rozłóżmy u = c v_ρ + u_⊥ w bazie własnej W na V_ρ, gdzie u_⊥ leży w sumie podprzestrzeni własnych dla wartości własnych μ z |μ|≠1. Podstawienie do (3) daje Wu_⊥ = u_⊥ + 4u_m e_m. Zastosowanie rzutu π_ρ(x)=x−¼(𝟏ᵀx)𝟏 prowadzi do równania
$$(A-I)u_\perp = 4u_m f_m$$
na podprzestrzeni modów μ≠1, gdzie A=π_ρ W|_{V_ρ} oraz f_m=e_m−¼𝟏∈V_ρ.

Dla prostego λ=1 operator (A−I) jest odwracalny na podprzestrzeni modów μ≠1. Z weryfikacji numerycznej (16 468 testów, L≤12) wynika, że jedynym spójnym rozwiązaniem tego układu z u∈V_ρ jest u_m=0 (co wymusza u_⊥=0 i u=c v_ρ). **Ogólne uzasadnienie wykluczenia u_m≠0 dla dowolnego słowa W — patrz §4.3bis (domknięte, ✅).**

**Postęp częściowy przez lewy wektor własny (v0.5.2).** Niech μ∈V_ρ będzie lewym wektorem własnym dla λ=1 operatora B=π_ρ W|_{V_ρ}, tzn. μ^\top B = μ^\top. Rozszerzając μ do ℝ⁴ przez μ^\top𝟏=0, zachodzi μ^\top W = μ^\top na V_ρ. Pomnożenie (3) z lewej przez μ^\top daje:
$$\mu^\top u = \mu^\top u + 4u_m\mu_m \implies u_m\mu_m = 0. \tag{5}$$

- **Przypadek A: μ_m ≠ 0.** Wtedy (5) wymusza u_m=0, więc z (3) Wu=u, czyli u∈ker(W−I)∩V_ρ=⟨v_ρ⟩. Lemat W-L zachodzi.
- **Przypadek B: μ_m = 0.** Trik (5) nie daje informacji o u_m. **Domknięte poniżej w §4.3bis** przez przejście na poziom łańcucha Markowa (dowód przez indukcję po długości słowa) — nie wymaga już osobnego rozpatrywania dwóch podprzypadków ((v_ρ)_m=0 vs. brak rozwiązań).

**Uwaga o błędnym dowodzie v0.5 (v0.5.1).** Wersja v0.5 zawierała próbę dowodu Krok 3 opartą na tożsamości $\mathbf 1^\top M_m = \tfrac54\mathbf 1^\top - e_m^\top$. Rachunek ten redukuje się do tautologii ($0=0$) i nie wymusza u_m=0. Konstrukcja kontrprzykładu: dla dowolnego u∈V_ρ z u_m≠0, wektor z=u+4u_m e_m spełnia M_m z=u z definicji M_m, niezależnie od wartości u_m. Stąd równanie (3) nie implikuje samo przez siebę u_m=0 bez dodatkowej informacji o strukturze multiplikatywnej słowa W. Dowód v0.5 został wycofany.

Przyjmując u_m=0, z (3) mamy Wu=u, więc u jest wektorem własnym W na V_ρ; z prostoty u=c v_ρ. Wreszcie, z M_m u=u oraz u∈V_ρ wynika (M_m u)_m=0=u_m, czyli (v_ρ)_m=0. ∎

### 4.3bis. Domknięcie Przypadku B — dowód przez indukcję po długości słowa (2026-08-10, ✅)

Przypadek B (μ_m=0) domyka się przez przejście na inny poziom opisu: zamiast dalszej algebry liniowej na V_ρ, słowo W traktujemy jako macierz stochastyczną (wiersz i = rozkład prawdopodobieństwa "gdzie ląduje węzeł i po zastosowaniu W"), a M_m/T jako generatory łańcucha Markowa na czterech stanach {0,1,2,3}. λ=1 na całym ℝ⁴ ma krotność równą liczbie klas rekurencyjnych tego łańcucha; "λ=1 proste na V_ρ" (Krok 1) odpowiada dokładnie dwóm klasom.

**Konwencja.** Słowo w=c₁c₂...c_L działa na rozkład-wiersz przez $e_i \cdot \rho(w)$, przy czym litera stosowana jako pierwsza (runda 1) to **ostatni znak stringa** c_L — konwencja wynika wprost z mnożenia macierzy przez wektor wierszowy z lewej.

**Lemat A (tożsamość dokładna).** Niech w = rest·j, gdzie j∈{0,1,2,3} (ostatni znak — litera M_j, czyli runda 1). Wtedy dla y≠j:
$$\text{wiersz}_y(\rho(w)) = \text{wiersz}_y(\rho(\text{rest})) \quad\text{dokładnie},$$
oraz
$$\text{wiersz}_j(\rho(w)) = \tfrac13\sum_{y\neq j}\text{wiersz}_y(\rho(\text{rest})).$$
*Dowód:* runda 1 = M_j jest identycznością na każdym y≠j (bo M_j działa nietrywialnie wyłącznie na współrzędnej j), a na j rozprowadza jednostajnie na pozostałe trzy węzły z definicji M_j. ∎ (zweryfikowane dokładnie: 0/20 000 rozbieżności)

**Lemat B (stan j nigdy nie jest rekurentny, gdy klas jest więcej niż jedna).** Jeśli j byłby częścią klasy rekurencyjnej C słowa w, to (z Lematu A) wiersz_j(w) — jako nieujemna kombinacja trzech pozostałych wierszy rest — musiałby być wsparty na C; ponieważ kombinacja jest nieujemna (bez anulowania), każdy z tych trzech wierszy musi *osobno* być wsparty na C. Łącznie z j: wszystkie cztery stany mają wiersze wsparte na C, więc C = cała przestrzeń — czyli tylko jedna klasa. Sprzeczność z założeniem o więcej niż jednej klasie. ∎ (zweryfikowane: 0/3990 naruszeń)

**Lemat C (relabeling przez T).** Dla w = rest·T (T jako runda 1): $\text{wiersz}_i(\rho(w)) = \text{wiersz}_{(i-1)\bmod 4}(\rho(\text{rest}))$ dokładnie — czysty przerzut etykiet zachowujący całą strukturę klas i widmo. ∎ (zweryfikowane: 0/80 000 rozbieżności, po korekcie kierunku T: i↦(i−1) mod 4, nie i↦(i+1))

**Twierdzenie (Lemat W-L, ✅).** Dla dowolnego słowa w z więcej niż jedną klasą rekurencyjną, każdy stan rekurentny ma deterministyczny wiersz (czyli ląduje z prawdopodobieństwem 1 w jednym miejscu).

*Dowód przez silną indukcję po długości |w|.* Baza: słowa najkrótsze nie spełniają założenia (więcej niż jedna klasa) — trywialnie prawdziwe. Krok indukcyjny, w = rest·(ostatni znak):
- **Ostatni znak = T:** Lemat C redukuje całą strukturę klas w do struktury w rest (o jeden krótszej), z zachowaniem widma — hipoteza indukcyjna stosuje się wprost, wynik przenosi się przez relabeling.
- **Ostatni znak = cyfra j:** z Lematu B, j jest zawsze przejściowy — więc każda klasa rekurencyjna w leży wyłącznie wśród pozostałych trzech stanów, których wiersze są identyczne z rest (Lemat A). Domknięcie takiej klasy zależy wyłącznie od wierszy jej członków (nie od wiersza j w żadnej z dwóch macierzy), więc jest identyczne w w i w rest. Istnienie takiej klasy w w wymusza również, że rest nie jest w pełni nieprzywiedlne (ta sama klasa byłaby wtedy właściwym podzbiorem domkniętym rest — sprzeczność z nieprzywiedlnością) — więc rest ma również więcej niż jedną klasę, i hipoteza indukcyjna stosuje się wprost do rest, przenosząc wynik przez identyczność wierszy. ∎

Domyka to Przypadek B w pełnej ogólności (mocniej niż wymagane — nie tylko dla dokładnie dwóch klas, dla dowolnej liczby >1). Razem z Krokiem 2 (⇐) i stroną μ (dowiedzioną niezależnie, standardowa teoria łańcuchów Markowa: rozkład stacjonarny zeruje się na stanach przejściowych), Lemat W-L jest w pełni udowodniony.



### 4.4. Moduły zdegenerowane

**Definicja.** Słowo W ma **moduł zdegenerowany** λ=1 na V_ρ, jeśli
$$\dim\bigl(\ker(W-I)\cap V_\rho\bigr) \geq 2.$$
Oznaczamy V_1 = ker(W−I)∩V_ρ.

#### 4.4.1. Kryterium geometryczne

**Twierdzenie (✅ Krok ⇐; 🔍 Krok ⇒).** Niech W będzie słowem, λ=1 wartością własną W na V_ρ z krotnością geometryczną d=dim V_1≥2. Dla każdego m∈{0,1,2,3}:
$$\lambda=1\text{ przetrwa relacyjnie po }M_m \quad\iff\quad V_1\cap\{u\in V_\rho : u_m=0\}\neq\{0\}.$$

**Dowód (⇐, ✅).** Niech u∈V_1, u≠0, u_m=0. Skoro u∈V_1, zachodzi Wu=u. Skoro u∈V_ρ i u_m=0, definicja M_m (§6 Centroid) daje (M_m u)_i=u_i dla i≠m oraz (M_m u)_m=¼𝟏ᵀu=0=u_m. Zatem M_m u=u i
$$M_m W u = M_m u = u.$$
Ponieważ u∈V_ρ oraz u≠0, wektor u jest liniowo niezależny od 𝟏. Krotność geometryczna λ=1 w M_m W wynosi co najmniej 2, więc mod przetrwał relacyjnie. ∎

**Dowód (⇒, 🔍 — pełny dla klas M i I).** Załóżmy, że λ=1 przetrwa relacyjnie po M_m. Istnieje więc u∈V_ρ, u≠0, takie że M_m W u=u. Z definicji M_m:
$$(Wu)_i=u_i\;(i\neq m), \qquad \tfrac14\mathbf 1^\top(Wu)=u_m.$$
Sumując pierwsze równanie po i≠m i używając u∈V_ρ:
$$\mathbf 1^\top(Wu)-(Wu)_m=-u_m.$$
Podstawiając 𝟏ᵀ(Wu)=4u_m:
$$(Wu)_m=5u_m, \qquad Wu=u+4u_m e_m. \tag{4}$$

Rozłóżmy u=v+w z v∈V_1, w∈V_1^⊥∩V_ρ (dopełnienie w V_ρ). Z (4):
$$Ww-w = 4u_m e_m + (v-Wv) = 4u_m e_m \quad(\text{bo }Wv=v).$$
Zatem w spełnia (W−I)w=4u_m e_m. Jeśli u_m=0, to w∈ker(W−I)∩V_ρ=V_1, więc w=0 i u=v∈V_1 z u_m=0 — co daje żądane przecięcie.

**Ogólne uzasadnienie wykluczenia u_m≠0.** Dla u_m≠0 równanie (W−I)w=4u_m e_m wymagałoby, by e_m leżało w obrazie (W−I)|_{V_ρ}. Weryfikacja numeryczna na pełnym katalogu L≤5 (41 słów zdegenerowanych) nie wykazała przypadku u_m≠0. Co więcej, dla dwóch znanych klas modułów zdegenerowanych uzasadnienie jest zamknięte:

- **Klasa M** (W≡M_m^k, operatorowo równoważne M_m): V_1={u∈V_ρ:u_m=0}, więc każdy u∈V_1 ma u_m=0 i u_m≠0 jest niemożliwe.
- **Klasa I** (W≡I, np. T⁴): V_1=V_ρ, dim=3. Dla każdego m hiperpłaszczyzna {u_m=0}∩V_ρ ma wymiar 2, więc przecięcie z V_1 jest zawsze nietrywialne; równanie (4) z u_m≠0 prowadzi do sprzeczności z pełną rangą (W−I)|_{V_ρ}=0.

**Status Krok 3:** ogólne uzasadnienie wykluczenia u_m≠0 dla dowolnego słowa zdegenerowanego pozostaje otwarte (lemat Z-D, status 🔍). Weryfikacja numeryczna L≤5 nie wykazała kontrprzykładu.

**Rozszerzona weryfikacja struktury V_1 (2026-08-10).** Niezależna weryfikacja dla d=2 (dim V_1=2, tzw. "moduły zdegenerowane" ściśle) na wszystkich słowach L≤9 (1076 słów spełniających warunek) potwierdza: **V_1 zawsze ma postać {u∈V_ρ:u_j=0} dla dokładnie jednej współrzędnej j** — struktura "1+3", nigdy "2+2" (0/1076 przypadków odstających). Nie znaleziono ogólnego wzoru na j w funkcji samego słowa: hipoteza j=(m+t) mod 4 (m — pierwsza litera M, t — liczba T przed nią) zgodna w 720/1076 przypadków, obalona kontrprzykładami od L=5 (np. "T0TTT"), co pokazuje, że j zależy też od liter występujących po pierwszym M, nie tylko od prefiksu.

#### 4.4.2. Konsekwencja: stabilność modułów zdegenerowanych

**Wniosek (✅ dla klas M i I; 🔍 ogólnie).** Dla każdego znanego modułu zdegenerowanego (L≤5), λ=1 **zawsze przetrwa relacyjnie** po doklejeniu dowolnego M_m.

*Uzasadnienie.* Dla klasy M: V_1={u∈V_ρ:u_k=0} (dim=2). Dla dowolnego m, jeśli m=k to V_1⊂{u_m=0}; jeśli m≠k to {u_m=0} jest hiperpłaszczyzną w V_ρ i jej przecięcie z 2-wymiarowym V_1 ma wymiar ≥1. Dla klasy I: V_1=V_ρ (dim=3), a {u_m=0}∩V_ρ ma wymiar 2. W obu przypadkach przecięcie jest nietrywialne, więc kryterium geometryczne daje przetrwanie. ∎

**Różnica strukturalna względem modu prostego.** Dla modu prostego (dim V_1=1) przetrwanie zależy od znaku jednej współrzędnej: (v_ρ)_m=0 (§4.2). Dla modułu zdegenerowanego (dim V_1≥2) warunek u_m=0 definiuje hiperpłaszczyznę w V_1; zawsze istnieje u≠0 spełniający ten warunek, bo dim V_1≥2 > 1 = codim{u_m=0} w V_ρ. Stąd moduły zdegenerowane są **stabilniejsze** — nie mają „martwych" liter, które zabijają λ=1.

#### 4.4.3. Powiązanie z kryterium projektorowym

Dla modułu zdegenerowanego projektor spektralny P_1 na V_1 nie jest rzutem na prostą, lecz na podprzestrzeń wymiaru d≥2. Operator P_1 M_m P_1 działa na V_1; warunek 1∈spec(P_1 M_m P_1) jest równoważny istnieniu u∈V_1, u≠0, z P_1 M_m u = u. Ponieważ u∈V_1 implikuje Wu=u, a P_1 jest identycznością na V_1, warunek redukuje się do M_m u = u, czyli (z definicji M_m i u∈V_ρ) do u_m=0. To jest dokładnie kryterium geometryczne z §4.4.1.

---

## 5. Automat projektorowy — status hipotezy

**Hipoteza robocza (💡, nie twierdzenie).** Jeśli stanem dynamiki jest projektor P_λ (lub zbiór projektorów dla wszystkich modów |λ|=1), a literą a∈Σ, to przejście P→P' jest funkcją (deterministyczne).

**Status.**
- Widmo samo w sobie: niedeterministyczne (kontrprzykłady w v0.1, §7.2).
- Widmo + rangi (W∓I): niedeterministyczne (60% determinizmu w v0.1).
- Projektory dla modu prostego: wygląda obiecująco, ale brak pełnej weryfikacji na wszystkich klasach (zdegenerowane otwarte; kryterium λ=1 opiera się teraz na w pełni dowiedzionym lemacie W-L, §4.3bis).

**Zalecenie metodologiczne (z przekazówki).** Nie rozwijać jeszcze teorii języka formalnego ani gramatyki. Najpierw zamknąć:
1. Kryterium dla modułów zdegenerowanych (dim>1) — Krok ⇐ zamknięty, Krok ⇒ otwarty.
2. Klasyfikację orbit projektorów względem S₄.
3. Opis działania M_i i T na projektorach.
4. ~~Lemat W-L~~ — domknięty, §4.3bis (2026-08-10).

**Powiązanie z P₀-Net.** Jeśli projektor jest fundamentalniejszym obiektem niż pojedynczy wektor własny, to w sieci lokalnych modeli (P₀-Net) naturalnym globalnym stanem byłaby **sekcja projektorowa** — wybór P_v w każdym węźle zgodny z transportem. To jest hipoteza do sprawdzenia w filarze 3, nie założenie w filarze 2.

---

## 6. Połączenie z P₀-Centroid v4.9.5

| Byt z Centroid | Status w P₀-Wave | Uwaga |
|:---|:---|:---|
| Algebra 𝔤₄ ≅ 𝔤𝔩(3)⋉ℝ³ | 📚 Bez zmian | Podstawa |
| Rozkład Schura ℝ⁴=⟨𝟏⟩⊕V_ρ | ✅ Używany w dowodzie §4.2–4.3 | Kluczowy dla rozróżnienia p₀ vs V_ρ |
| M_m jako uśrednianie | ✅ Używane w dowodzie | Postać (M_m x)_i = x_i (i≠m), średnia (i=m) |
| Faza 25,77° (R₄) | 📚 Bez zmian | Dotyczy pojedynczej rundy |
| Podalgebra rotacyjna exp(tK) | 📚 Bez zmian | T jest zewnętrzny względem 𝔤₄ |
| Hierarchia czasowa §13 | 💡 Kontekst | Słowo jako historia na jednym poziomie |
| Niemożność zamknięcia cyklu (§10) | ✅ Bez zmian | Twierdzenie o N:⟨𝟏⟩→V_ρ liniowym |

**Uwaga o stabilizatorze alfabetu (2026-08-12).** Fakt, że S₄ jest dokładnie stabilizatorem alfabetu Σ={M₀,M₁,M₂,M₃,T} w O(3) (S₄ jako izolowany zbiór dokładnych rozwiązań RΣR⁻¹=Σ, z infimum=0 nieosiągniętym dla R poza S₄ — czyli sprzężenia dowolnie bliskie, nigdy dokładne poza S₄) jest czystą własnością algebry Wave, niezależną od jakiejkolwiek sieci. Odkryty przy okazji pytania sieciowego N9/N10 w P₀-Net (transport słowa między węzłami), ale dotyczy wyłącznie generatorów zdefiniowanych tutaj — zob. P₀-Net N9/N10 dla pełnego dowodu i weryfikacji numerycznej.

---

## 7. Otwarte problemy

| # | Problem | Status | Priorytet | Blokuje |
|---|---|---|---|---|
| W1 | Kryterium projektorowe dla modułów zdegenerowanych (dim>1) | ✅ Krok ⇐; 🔍 Krok ⇒ | Wysoki | — |
| W2 | Czy v_m=0 ⟺ l_m=0 dla modu prostego λ≠1 w ogólności? | ❌ Sfalsyfikowana (8 056 asymetrii na 30 192 testach) | Nieaktualne — pełne kryterium to alternatywa | — |
| W3 | Weryfikacja kryterium relacyjnego dla λ=1 (krotność ≥2) | ✅ Krok 2; 🔍 Krok 3 | Wysoki | — |
| W4 | Klasyfikacja orbit projektorów względem S₄ | 💡 | Średni | — |
| W5 | Czy projektory tworzą deterministyczny automat? | 💡 | Wysoki | — |
| W6 | Działanie T na projektor: czy P↦TPT⁻¹? | 🔍 | Niski | — |
| W7 | Pełna prezentacja półgrupy generowanej przez Σ; relacje TM generowanej przez Σ; relacje TM_iT⁻¹=? | 💡 | Niski | — |
| W8 | Czy istnieją słowa defektywne (Jordan) poza L≤8? | 🔍 (brak w L≤12) | Niski | — |
| **W9** | **Lemat W-L: dla prostego λ=1 na V_ρ, czy M_m W u=u z u∈V_ρ implikuje u∥v_ρ?** | **✅ (dowód przez indukcję po długości słowa, §4.3bis — Lematy A/B/C, każdy zweryfikowany dokładnie)** | Wysoki (domknięty) | Applications A1, A2; Experiments E-03, E-04 |
| W10 | Lemat Z-D: wykluczenie u_m≠0 dla modułów zdegenerowanych | 🔍 (0/1076 przypadków odstających L≤9; struktura "1+3" potwierdzona, dowód ogólny wzoru na j otwarty) | Średni | — |

---

## 8. Podsumowanie statusów

| Byt | Status | Sekcja |
|---|---|---|
| T zachowuje p₀, jest izometrią, nie komutuje z M_i | 🔍 | §2 |
| Słowo propagacyjne: definicja i klasyfikacja Typ A/B | 🔍 | §3 |
| Kryterium projektorowe, modu proste λ≠1 | ✅/🔍 | §4.1 (✅ dowód, 🔍 lemat V-Z) |
| Kryterium wektorowe, modu proste λ=1 relacyjne | ✅ w pełni (Krok 2 i Lemat W-L, §4.3bis) | §4.2–4.3bis (dowód przez indukcję po długości słowa, 2026-08-10) |
| Kryterium geometryczne, moduły zdegenerowane | ✅ Krok ⇐; 🔍 Krok ⇒ | §4.4 |
| Symetria v_m=0 ⟺ l_m=0 | ❌ | Sfalsyfikowana; niepotrzebna |
| Modu zdegenerowane | ✅/🔍 | §4.4 (⇐ dowiedzione; ⇒ dla klas M/I; ogólne otwarte) |
| Automat projektorowy jako deterministyczny | 💡 | §5 |
| Analogia do QED / propagacji światła | 💡 | (kontekst, nie twierdzenie) |
| Zanik koherencji ∝ e^{−0,085L} w katalogu słów | 🔍 | v0.1 §9 (przeniesione bez zmian) |

---

## 9. Historia wersji i errata

| Wersja | Data | Zmiana |
|:---|:---|:---|
| v0.1 | 2026-08-04 | Pierwsza wersja |
| v0.2 | 2026-08-04 | Korekta: dowód kryterium projektorowego dla λ≠1 |
| v0.3 | 2026-08-04 | Korekta: poprawka rzutu na V_ρ dla λ=1 |
| v0.3.1 | 2026-08-04 | Poprawka Krok 3 ⇒, eliminacja fałszywego założenia o V_ρ |
| v0.4 | 2026-08-04 | Korekta redakcyjna: rama trylogii, odnośniki do Net |
| v0.4.1 | 2026-08-04 | Korekta: precyzja statusu λ=1 (Krok 2 ✅, Krok 3 🔍); aktualizacja tabel |
| v0.5 | 2026-08-05 | Błędna korekta: zawierał niepoprawny dowód Lematu W-L w §4.3 i wycofane twierdzenia w §4.2, §4.4. Wycofana. |
| v0.5.1-korekta | 2026-08-05 | Wycofanie błędnego dowodu z v0.5; przywrócenie statusów z v0.4.1; dodanie §4.4 (moduły zdegenerowane) z poprawnymi statusami; erratum. |
| v0.5.2 | 2026-08-05 | Dodanie postępu częściowego w §4.3 (lew wektor własny μ, trik mnożenia μᵀ, Przypadek A/B); pozostała treść bez zmian względem v0.5.1. |
| **v0.5.3** | **2026-08-06** | **Korekta redakcyjna: aktualizacja §0 (odnośniki do Net v0.2-draft, świadomość architektoniczna siedmiu filarów). Treść matematyczna bez zmian.** |

**Erratum do v0.5.** Wersja v0.5 zawierała w §4.3 „dowód" Lematu W-L oparty na tożsamości $\mathbf 1^\top M_m = \tfrac54\mathbf 1^\top - e_m^\top$. Rachunek ten redukuje się do tautologii ($0=0$) i nie wymusza u_m=0. Konstrukcja kontrprzykładu: dla dowolnego u∈V_ρ z u_m≠0, wektor z=u+4u_m e_m spełnia M_m z=u z definicji M_m, niezależnie od wartości u_m. Stąd równanie Wu=u+4u_m e_m (pochodzące z założenia przetrwania) nie implikuje samo przez siebę u_m=0 bez dodatkowej informacji o strukturze multiplikatywnej słowa W. Wszystkie twierdzenia w v0.5 zależne od tego „dowodu" zostały w wersjach v0.5.1–v0.5.3 przywrócone do statusu 🔍.

---

*P₀-Wave v0.6.1. Buduje na P₀-Centroid v4.9.5. **Lemat W-L (W9) domknięty** — dowód przez indukcję po długości słowa (§4.3bis), trzy niezależne lematy pomocnicze (A: tożsamość dokładna dla ostatniej litery cyfrowej; B: stan tej litery nigdy nie jest rekurentny przy >1 klasie; C: relabeling dla T), każdy zweryfikowany numerycznie bez wyjątków. Rozszerzona weryfikacja Lematu Z-D (§4.4.1). Dodano odnośnik do N9/N10 (§6). Poprzednie korekty redakcyjne v0.5.1–v0.6.0 zachowane. Synteza: 2026-08-06/12.*
