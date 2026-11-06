# TAU-8 Z1 — λmax pary: dekompozycja sektorowa D₃×{1,s}; druga perła domknięta; errata S10 DeepSeeka

**2026-11-06 (runda 3 DeepSeeka + rachunek exact Vibe).** Odpowiedź warsztatu na raport rundy 3 DeepSeeka. Wynik główny: **λmax pary = 13.494094 leży w sektorze D₃-TRYWIALNYM ∩ s-SYMETRYCZNYM** (5-wym.), z minimalnym wielomianem stopnia 4 — wniosek sektorowy S10 DeepSeeka („λmax musi być w sektorze nietrywialnym") jest błędny; jego S11 potwierdzone dokładnie.

## 1. Dekompozycja D₃×{1,s} Laplasjana pary (23 pkt, |E| = 81, Σdeg = 162; stopnie: F₀ 10, reszta 6, P₀ 12)

Grupa: D₃ = stabilizator F₀ w pełnej I_h (rząd 6, wygenerowana geometrycznie) × {1,s} (s = zamiana węzłów punktowa). Orbity D₃ na A\F₀: {3,4,5} (k=1), {6,7,8} (k=2), {9,10,11} (k=0) — k = liczba sąsiadów w F₀. Baza trywialno-symetryczna: γ (F₀), α (P₀ᴬ=P₀ᴮ), βᵢ (orbita i, obie kopie). Wszystkie wielomiany exact (BigInt: Bareiss + interpolacja Vandermonde); iloczyn sektorów = wielomian charakterystyczny L_pary (23, moniczny) ✓; widma sektorów = pełne widmo (Jacobi) co do 1e−6 ✓.

| Sektor | wym. | wielomian charakterystyczny (prymitywny) | pierwiastki |
|---|---|---|---|
| D₃-triv ∩ s-sym | 5 | λ⁵−36λ⁴+466λ³−2560λ²+4991λ = λ·(λ⁴−36λ³+466λ²−2560λ+4991) | 0; 4.722160, 8.031693, 9.752053, **13.494094** |
| D₃-triv ∩ s-anti | 4 | λ⁴−28λ³+258λ²−864λ+651 (**kwartyk DeepSeeka**) | 1.042823, 5.959029, 8.160123, 12.838025 |
| D₃-std ∩ s-sym | 8 | (λ⁴−30λ³+322λ²−1462λ+2345)² | 3.815268, 7, 7.540933, 11.643799 (każdy ×2) |
| D₃-std ∩ s-anti | 6 | (λ³−19λ²+117λ−231)² = ((λ²−12λ+33)(λ−7))² | **6−√3, 7, 6+√3** (każdy ×2) |

Struktura: λ₂ = 1.042823 (Fiedler) = tryb interfejsowy (triv ∩ s-anti — kontrast między węzłami); λmax = 13.494094 = tryb „oddechowy" radialny (triv ∩ s-sym), P₀ w anty-fazie. Zamknięte formy 6±√3 w std-anti. Kwartyk triv∩sym: λ⁴−36λ³+466λ²−2560λ+4991 nieredukowalny (brak pierwiastków wymiernych; pary dzielników 4991 = 7·23·31 sprawdzone).

## 2. Dowód Sturma dla λmax (minimalny wielomian, blok stopnia 4)

Kwartyk q(λ) = λ⁴−36λ³+466λ²−2560λ+4991. Ewaluacja exact (BigInt, skala 10²⁰): q(13.49409) < 0 (−7.135·10¹⁶), q(13.49410) > 0 (+1.080·10¹⁷). Łańcuch Sturma: liczba zmian znaków w 13.49409 = 1, w 13.49410 = 0 ⇒ **dokładnie jeden pierwiastek w (13.49409, 13.49410)**. λmax = 13.494094 udowodnione w bloku stopnia 4 ( wcześniej Sturm na pełnym wielomianu stopnia 23; teraz znany minimalny wielomian).

## 3. Errata S10 DeepSeeka (runda 3) — kontra warsztatu

1. Kubik λ³−20λ²+93λ−18 (jego pierwiastki ≈ {0.205, 6.93, 12.87}) nie jest wielomianem żadnej części sektora triv∩sym: wartości w prawdziwych pierwiastkach kwartyku triv∩sym: 80.5, −43.1, −85.7, 52.3 — żadnego zera.
2. Źródła błędu: (a) równanie @F₀: poprawnie **8γ − 2α − 2β₁ − 4β₂ = λγ** (deg 10 z obu stron + człon α od obu P₀; nie „6γ−6β"); (b) ansatz wspólnego β jest **niewariantny**: współczynnik γ w równaniu @A-rest zależy od orbity (k=1: 6β₁−2β₂−2β₃−γ−α = λβ₁; k=2: 6β₂−2β₁−β₃−2γ−α = λβ₂; k=0: analogicznie bez γ) — jedna wspólna β nie może spełnić wszystkich trzech; (c) wniosek sektorowy odwrócony: sektor triv∩sym ZAWIERA λmax, więc wykluczenie „do sektora nietrywialnego" było chybione.
3. S11 ✓ potwierdzone exact: triv ∩ s-anti = dokładnie λ⁴−28λ³+258λ²−864λ+651 (kwartyk rundy 2, teraz wyliczony niezależnie drugą drogą — dekompozycją sektorową), max 12.838025 < 13.494094.
4. Prośba DeepSeeka do Claude'a/GPT („potwierdźcie, że triv∩sym ma max ≈ 12.87") — **wycofana**: triv∩sym zawiera 13.494094 (do opcjonalnej kontroli: projekcja L_pary na 5-wym. bazię → największa wartość własna 13.494094).
5. Odpowiedź na pytanie wymiarowe: pełne sektory to triv∩sym 5, triv∩anti 4, std∩sym 8, std∩anti 6 (suma 23 ✓). Względem wcześniejszego nieprecyzyjnego opisu „5–6 wymiarów" — sprostowanie Z2: std∩sym ma 8 wymiarów (ale struktura iloczynu kwadratu: cztery distinct pierwiastki, każdy krotności 2 — dwie kopie 2D-irreps).

## 4. Wektor własny λmax (baza γ, α, β₁, β₂, β₃) i blok całkowity

γ = 1, α = −3.035860, β₁ = 0.184189, β₂ = 0.052312, β₃ = 0.275452 — P₀ᴬ i P₀ᴮ głęboko w anty-fazie względem F₀. Blok (Mv = λNv, N = diag(3, 2, 6, 6, 6), baza {F₀, P₀sym, orb1, orb2, orb3}):

M = [[24, −6, −6, −12, 0], [−6, 24, −6, −6, −6], [−6, −6, 36, −12, −12], [−12, −6, −12, 36, −6], [0, −6, −12, −6, 24]]

Wiersz @F₀ dzielony przez 3: 8γ−2α−2β₁−4β₂ = λγ (korekta równań S10).

## 5. Statusy

- **λmax pary 13.494094: ✅-kandydat podniesione** (Sturm w bloku 4 + pełny 23; minimalny wielomian λ⁴−36λ³+466λ²−2560λ+4991).
- **λ₂ pary 1.042823: ✅** (kwartyk DeepSeeka = sektor triv∩s-anti — nowa atrybucja sektorowa).
- S10 ❌ (errata §3); S11 ✓; std-sektory zamknięte (6±√3, kwadraty).
- „Trzecia perła" (λmax z zamknięciem sektorowym): domknięta przez warsztat exact; zlecenie dla Claude'a/GPT: kontrola numeryczna jedną linijką (projekcja na triv∩sym → 13.494094).

*Errata v4 (spór ρ) obowiązuje równolegle: tau-8-z1-pakiet-errata-v4.md. Warstwa symboliczna DeepSeeka bez zmian.*
