# TAU-8 Z1 pakiet — errata v4: rozstrzygnięcie sporu ρ (koncesja pełna)

**2026-11-06, warsztat Vibe (szef laboratorium).** Erraty v2/v3 opublikowały wartości ρ jako „exact" z pipeline'u: ślady potęg (BigInt, dokładne) → wielomian charakterystyczny (Newton, dokładny) → pierwiastki (Durand–Kerner/Newton na współczynnikach zaokrąglonych do 53 bitów). Ścieżka śladów, q_k, współczynniki wielomianów i det STOJĄ (potwierdzone niezależnie). **Ścieżka pierwiastkowa jest dla tego widma katastrofalnie źle uwarunkowana i dała wartości obarczone błędem do 2·10⁻⁵.** Prawdziwe ρ to wartości macierzowe: LAPACK/mpmath Claude'a, numpy GPT oraz dwa niezależne rachunki Vibe. **Koncesja pełna: liczby Claude'a i GPT były poprawne; „poprawki exact" errat v2/v3 chybione. Zadanie B domknięte.**

## 1. Pomiary rozstrzygające (Vibe, sesja TAU-8, 2026-11-06)

1. **Identyczność obiektów.** Macierz iloczynu float64 (20 bloków, pełny akumulacja) i macierz exact (BigInt) po zaokrągleniu wpisów do 53 bitów: max |różnica wpisu| = 5.6·10⁻¹⁷ (4 obiekty). Ślady: exact vs float zgodne co do 16 cyfr (1.2889685345212; 1.163642560270783; 1.258423060938833; 1.272126069591923). Potęgi śladów (fingerprinty): tr(R²) = 1.037959679, tr(R⁵) = 1.000165444, tr(R²⁰) = 1.000000000 — exact = float co do 9 cyfr. To ten sam obiekt na wszystkich poziomach.
2. **λ macierzy exact** (inwersja zespolona z pełnym pivotowaniem + dwustronny Rayleigh; deflacja pierwiastka 1): tabela w §3. Wszystkie wartości = LAPACK Claude'a / numpy GPT co do drukowanych cyfr.
3. **Empiryczne κ(λ)** (perturbacja 1·10⁻¹⁰ → pomiar przesunięcia λ): v3 kanon 0.3; v3 rev 6.8; v1 literał 2.0; v1 kanon 0.03. Ścieżka macierzowa dobrze uwarunkowana ⇒ λ z LAPACK/eigvals dokładne do ~10⁻¹⁵.
4. **Podłoga szumu ewaluacji wielomianu.** Szum absolutny na dużych współczynnikach dominuje: Σ|c_m·λ^m|·2⁻⁵³ ≈ 1.3·10⁻¹⁶, nie |P(λ)|·2⁻⁵³ ≈ 10⁻²⁷. Argument E8b „P(λ_Claude) = 2.9·10⁻¹⁷ vs szum 10⁻²⁷ (10¹⁰ nad podłogą)" był chybiony o 11 rzędów: 2.9·10⁻¹⁷ leży PONIŻEJ podłogi ⇒ nie było dowodu przeciw λ Claude'a. Wycofane.

## 2. Mechanizm (dlaczego „exact" był gorszy niż LAPACK)

- **Kondycjonowanie pierwiastków wielomianu vs wartości własnych macierzy** (klasyczne zjawisko Wilkinsona): κ_poly(pary literału v1) = Σ|c_m·λ^m|/|P′(λ)| ~ 3·10¹⁰. Zaokrąglenie współczynników do 53 bitów (decNum przed DK/Newtonem) przesuwa pierwiastki o ~2·10⁻⁵; iteracje dodatkowo zatrzymują się na poziomie 10⁻⁹ (kanon v3). Dla kanonu v3 κ_poly ≈ 6 — tam błąd 10⁻⁹ pochodzi z niedomknięcia iteracji, nie z zaokrąglenia.
- **Domknięcia Σλᵏ vs q_k (E8b) są nieważne wobec tej klasy błędu**: pierwiastki zaokrąglonego wielomianu automatycznie spełniają zaokrąglone momenty (~10⁻¹⁵) — kontrola dzieli ścieżkę zaokrąglenia z produkcją (samoreferencja). Test domknięcia chroni przed błędem SOLVERA pierwiastków, nie przed błędem REPRESENTACJI wielomianu.
- **Hipoteza „niedokonwergowana iteracja potęgowa" z E8b wycofana**: Claude nie używa iteracji potęgowej (LAPACK eigvals: Hessenberg + QR; kontrola mpmath Faddeev–Leverrier + polyroots).
- **Drobna rozbieżność Claude'a 0.085888 (LAPACK) vs 0.085890 (mpmath polyroots) wyjaśniona**: polyroots działa na wielomianie = ta sama słabo uwarunkowana ścieżka (błąd 2·10⁻⁶); LAPACK = ścieżka macierzowa (dokładna). Prawdziwa wartość: 0.0858884.

## 3. Tabela prawdziwych wartości (checkpointy v4; dokładność macierzowa ~10⁻¹²)

Ślady, q_k, wielomiany i det: exact BigInt — bez zmian. ρ: wartości macierzowe.

| Obiekt | Ślad R (exact) | ρ opublikowane v2/v3 (BŁĘDNE) | ρ PRAWDZIWE | Potwierdzenie |
|---|---|---|---|---|
| v3 kanon apex-first [P₀,v₂,v₁,v₀] | 1.288968535 | 0.174758936 | **0.174758932** | Claude LAPACK 0.174758932 ✓, mpmath 0.174758933 ✓, Vibe macierz ×2 ✓ |
| v3 rev | 1.258423061 | 0.113509600 | **0.113514662** = \|0.106293762 ± 0.039839861i\| | Claude 0.113514/0.113515 ✓; sesja 0.113515 ✓; Vibe ✓ |
| v3 p0first [v₂,v₁,v₀,P₀] | 1.165182204 | 0.131327191 | **0.131327883** | Claude 0.131328 ✓; Vibe ✓ |
| v1 kanon apex-first | 1.272126070 | 0.165561507 | **0.165561571** | GPT 0.165561571 ✓ (co do cyfry); Vibe ✓ |
| v1 literał [v₀,v₁,v₂,P₀] | 1.163642560 | 0.085868381 | **0.085888387** = \|0.077960923 ± 0.036040387i\| | GPT 0.085888387 ✓ (co do cyfry); Claude 0.085888 ✓; Vibe ✓ |
| v1 literał rev | 1.125524004 | 0.062718334 | **0.060853926** = \|0.060006612 ± 0.010119629i\| | Claude/GPT 0.060854 ✓; Vibe ✓ |
| v1 p0first [P₀,v₀,v₁,v₂] | 1.254743374 | 0.118650582 | **0.118651078** | Claude/GPT 0.118651 ✓; Vibe ✓ |

Komponenty par zespolonych z E8b (0.077942±0.036033i; 0.106290±0.039835i; 0.061890±0.010160i; 0.106488±0.052328i) — wycofane; poprawne w tabeli. q₂/q₄/q₈/q₁₆ z E8b — exact, stoją (ścieżka śladów).

**Sesja-oryginalne wartości 6-cyfrowe potwierdzone**: 0.174759 ✓; 0.113515 ✓ (errata v2 błędnie „poprawiła" ją na 0.113510 — rekonstrukcja); 0.118651 ✓; p0first węzła: prawda 0.131327883, sześciocyfrowo 0.131328 (sesyjne 0.131327 — różnica 1 ulp szóstego miejsca, replikacja Claude'a 0.131328 ✓).

## 4. Skan 24 permutacji — powtórzony metodą macierzową (moje etykietowanie v3)

Maksimum: **apex-first [P₀,v₂,v₁,v₀], ρ = 0.174758932** (rank 1/24); dalej: 0.168472, 0.166173, 0.163160, 0.160886, 0.159748. Wniosek E3 (zakres ρ ~×4, maksimum apex-first) POTWIERDZONY; wartości liczbowe skanu E3 obarczone błędem ścieżki pierwiastkowej do ~2·10⁻⁵ (np. E3: 0.166167 → prawda 0.166173).

## 5. Statusy po erracie v4

- **B: ✅-kandydat** (Claude LAPACK + mpmath; Vibe macierzowo ×2 [iloczyn float + entry-rounded exact]; sesja 6-cyfrowo; GPT: przebieg wg v3/v4 oczekiwany).
- **A, C–G, H4: ✅-kandydat** (Claude: wszystkie checkpointy zgodne; H4 det = 256⁻²⁰ = 6.842278·10⁻⁴⁹ potrójnie).
- **H2, H3: ✅-kandydat** (Claude: lustro ℓ per punkt max 1.4·10⁻¹⁷; przełącznik centrum z liczbami: rev ℓ(P₀) = 0.018315, p0first-rev 0.091528 na 4/13).
- **H1: 🔍** (jakościowo: znaki stron przeciwne, moduły nierówne — wektor Claude'a: A-only −7.886, B-only +5.873, F₀ +1.322, P₀ᴬ −0.852, P₀ᴮ +0.634 — nie czysta antysymetria).
- **Warstwa symboliczna DeepSeeka nietknięta** (kwartyk λ⁴−28λ³+258λ²−864λ+651, λ₂ węzła 6−√5, λ₂ pary 1.042823, lemat jąder — niezależne od ścieżki pierwiastków ρ).

## 6. Lekcje protokołu (E12 → rejestr)

1. **„Exact" dotyczy śladów, q_k, współczynników i det. ρ liczyć z macierzy** (eigvals / inversja + Rayleigh na obiekcie entry-rounded-exact), z empirycznym κ(λ) przy raporcie; pierwiastki wielomianu charakterystycznego traktować jako walidację strukturalną, nie źródło cyfr znaczących.
2. **Domknięcie współdzielące ścieżkę obliczeń z produkcją nie jest kontrolą** (Σλᵋ vs q_k chroni tylko przed błędem solvera, nie reprezentacji).
3. **Podłoga szumu ewaluacji wielomianu = Σ|c_m·λ^m|·ε** (szum absolutny na dużych współczynnikach), nie ε·|P(λ)|.
4. **κ mierzyć empirycznie zanim oskarży się solver drugiej strony**; własny „dokładny" pipeline wymaga niezależnego walidatora na tym samym obiekcie.
5. **Przed publikacją „poprawki" liczby drugiej strony: odtworzyć jej wartość DWIEMA niezależnymi u siebie ścieżkami** (tu: macierzowo — spór by się nie zdarzył; koszt rozstrzygnięcia: jedna noc i trzy tury relayu).

## 7. Prośby

- **GPT**: przebieg wg tabeli poprawnej (errata v3) nadal oczekiwany; jego q₂ = 0.0343771620 / q₄ = 0.000779204 (kanon) i q₂ = 0.0097927302 / q₄ = −0.0000174403 (literał) potwierdzone exact; jego ρ 0.165561571 / 0.085888387 potwierdzone jako PRAWDZIWE.
- **Claude**: potwierdzenie erraty v4 (jedno zdanie + statusy); kwartyk λ₂ pary do numerycznej kontroli (eigvalsh 23×23 vs λ⁴−28λ³+258λ²−864λ+651) pozostaje w kolejce.
- **DeepSeek**: errata v4 (odczyt); jego warstwa symboliczna bez zmian.

---
*Errata v4 zastępuje linie „exact ρ" errat v2/v3 (E2, E8b, skan E3). Wszystko poza ρ (konwencje, tabele geometryczne, ślady, q_k, wielomiany, det, Laplasjany, lemat) bez zmian.*
