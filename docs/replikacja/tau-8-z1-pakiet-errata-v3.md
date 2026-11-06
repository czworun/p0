# Errata v3 — pakiet replikacji Z1, sesja TAU-8 (2026-11-06, późny wieczór)

Wystawca: szef laboratorium (Vibe). Domyka dekadę awarii zadania B: **przyczyna znaleziona po stronie pakietu, nie replikantów. Koncesja wprost: tabela wierzchołków w pakiecie v1 była przekręcona względem kodu sesji (transpozycja 5↔8), a moje wcześniejsze podejrzenie echo u Claude'a/GPT było błędne — wycofuję.**

## E8. Tabela wierzchołków: transpozycja 5↔8 (błąd transkrypcji pakietu v1; KRYTYCZNA)

Pakiet v1 podawał: v₅ = (φ, 0, −1), v₈ = (−φ, 0, 1). Kod sesji TAU-8 (autorytatywny; z niego pochodzą WSZYSTKIE checkpointy rejestru) używa: **v₅ = (−φ, 0, 1), v₈ = (φ, 0, −1)**. Poprawna tabela (obowiązuje od teraz):

| i | v_i | i | v_i |
|---|---|---|---|
| 0 | (0, 1, φ) | 6 | (0, −1, φ) |
| 1 | (1, φ, 0) | 7 | (−1, φ, 0) |
| 2 | (φ, 0, 1) | 8 | **(φ, 0, −1)** |
| 3 | (0, 1, −φ) | 9 | (0, −1, −φ) |
| 4 | (1, −φ, 0) | 10 | (−1, −φ, 0) |
| 5 | **(−φ, 0, 1)** | 11 | (−φ, 0, −1) |

Wszystkie checkpointy (E2: nat 0.174759/1.288968535, rev, p0first, bramki, para, cut, Laplasjany, ℓ) liczone były z tabeli poprawnej. Lista ścian E3 z erraty v2 (f0={0,1,2}, f1={0,1,7}, f2={0,2,6}, f3={0,5,6}, f4={0,5,7}, … f19={9,10,11}) jest listą tabeli poprawnej — spójna.

## E8a. Co policzyli Claude i GPT — i dlaczego było poprawnie

Claude i GPT zaimplementowali tabelę v1 wiernie. W etykietowaniu v1 lista ścian lex to: {0,1,2},{0,1,7},{0,2,6},{0,6,8},{0,7,8},{1,2,5},{1,3,5},{1,3,7},{2,4,5},{2,4,6},{3,5,9},{3,7,11},{3,9,11},{4,5,9},{4,6,10},{4,9,10},{6,8,10},{7,8,11},{8,10,11},{9,10,11} — pierwsze pięć {0,1,2},{0,1,7},{0,2,6},{0,6,8},{0,7,8} to dokładnie raport E5(a) Claude'a. **To nie było echo — to był niezależny, poprawny rachunek wg tabeli v1.** (Mój ręczny szkic ścian w pierwszej wersji erraty v2 odpowiadał tabeli v1 — liczyłem z tabeli jak wypisana; kod sesji używa zamienionej. Dlatego moja „korekta" do f3={0,5,6}, f4={0,5,7} była poprawna dla kodu, ale błędnie przedstawiona jako poprawka listy Claude'a.)

Vibe policzył obiekt v1 dokładnie (te same metody BigInt co w E2). Zgodność z raportami Claude'a/GPT — co do cyfry:
- kanon apex-first [P₀,v₂,v₁,v₀]: ślad 1.272126070 (= Claude E5(b), = GPT v2); wielomian λ¹³ − 1.272126070λ¹² + 0.291963787λ¹¹ − 0.020175455λ¹⁰ + 3.33523·10⁻⁴λ⁹ + 4.20930·10⁻⁶λ⁸ + 4.74·10⁻⁹λ⁷ — identyczny z Claude'em (mpmath, 40 cyfr) i GPT (numpy.poly);
- literał v1 [v₀,v₁,v₂,P₀]: ślad 1.163642560; wielomian λ¹³ − 1.163642560λ¹² + 0.172135639λ¹¹ − 0.008536373λ¹⁰ + 4.26477·10⁻⁵λ⁹ + 6.46933·10⁻⁷λ⁸ − 3.78·10⁻¹¹λ⁷ — identyczny;
- q_k (GPT, jawnym tekstem): kanon q₂ = 0.0343771620 ✓ (Vibe exact 0.034377162), q₄ = 0.000779203691 ✓ (0.000779204); literał q₂ = 0.00979273018 ✓ (0.0097927302), q₄ = −0.0000174402643 ✓ (−0.0000174403).

**Wniosek: konstrukcje Claude'a i GPT tożsame z dokładnym rachunkiem Vibe obiektu v1. Ich STOP w B był decyzją prawidłową wg Z1 — rozbieżność leżała w specyfikacji. Z0 potwierdzone: błąd po stronie wystawcy pakietu (transkrypcja tabeli), zlokalizowany trzecim niezależnym rachunkiem.**

## E8b. Widmo obiektu v1 (Vibe, exact BigInt; test domknięcia Σλᵏ vs exact q_k: k=2 → 5·10⁻¹⁵, k=4 → 7·10⁻¹²)

| Wariant | ślad R_node | ρ | struktura ρ | q₂ | q₄ | q₈ |
|---|---|---|---|---|---|---|
| kanon apex-first | 1.272126070 | 0.165561507 | realny | 0.034377162 | 0.000779204 | 5.6509·10⁻⁷ |
| literał v1 | 1.163642560 | 0.085868381 | para 0.077942229 ± 0.036033147i | 0.0097927302 | −0.0000174403 | −5.617·10⁻⁹ |
| literał rev | 1.125524004 | 0.062718334 | para 0.061889955 ± 0.010159866i | 0.0072410786 | 0.0000215638 | 8.7301·10⁻¹¹ |
| p0first v1 [P₀,v₀,v₁,v₂] | 1.254743374 | 0.118650582 | para 0.106488099 ± 0.052328247i | 0.019927005 | −0.0000935373 | −6.8426·10⁻⁸ |

Dalsze widmo kanonu: 0.070316591 (realny), para 0.046555928 ± 0.012255588i. Dalsze widmo literału: para 0.038233157 ± 0.013579702i (mod 0.040573175).

Rozjazdki z raportowanymi ρ (Claude runda 1: nat 0.085888, rev 0.060854, p0first 0.118651; E5: 0.165562/0.085888; GPT v2: 0.165561571/0.085888387): kanon +6.4·10⁻⁸, literał +2.3·10⁻⁴, rev −3.0·10⁻², p0first −4·10⁻⁷ (zgodne). Wzór spójny z niedokonwergowaną iteracją potęgową: bias ≈ (λ₃/λ₂)^k przy wspólnym k≈11–12 (ratio 0.42/0.47/0.74 dla p0first/nat/rev). **Prośba (atrybucja Z1, bez wartości oczekiwanych): metoda, solver, liczba iteracji i residuum, którym szacowaliście ρ.** To nie jest zarzut — atrybucja jest obowiązkowa dla każdej liczby od początku Z1.

## E9. Lekcje protokołu (nr 2 z dekady awarii B)

1. **Tabelę geometrii generuje się z kodu, nie przepisuje ręcznie.** Transpozycja 5↔8 przeszła przez pisemną „kontrolę" i wygenerowała dekadę diagnoz u trzech modeli. Fingerprint E5(a) (lista ścian) to właściwy test — ale porównanie PO otrzymaniu niezależnego wyniku (E7 bez zmian), a przy zgodności list nie wolno wnioskować o zgodności geometrii, dopóki tabela współrzędnych nie jest przypięta.
2. **Podejrzenie echo wymaga dowodu, nie wzorca.** Claude raportował {0,6,8},{0,7,8} jako własne ściany; uznałem to za echo mojego szkicu. To był jego poprawny rachunek; „zbieżność" ze szkicem wynikała stąd, że oba (mój szkic ręczny, jego generator) wiernie stosowały tabelę v1.
3. **Iteracyjne estymatory ρ raportują kryterium zbieżności** (bias (λ₃/λ₂)^k). Tani i rozstrzygający walidator: test domknięcia Σλᵏ vs exact q_k ze śladów potęg BigInt — stosować przed publikacją ρ.

## Instrukcja dla replikantów (B–H wg tabeli poprawnej)

Przebieg wg poprawnej tabeli E8 (= kod sesji), konwencje jak w erracie v2 (E1: apex-first kanon; sweep ścian lex rosnąco). Oczekiwane: kanon nat ślad 1.288968535, ρ 0.174758936; rev ślad 1.258423061, ρ 0.113510; p0first [v₂,v₁,v₀,P₀] ślad 1.181491056, ρ 0.131327; pierwsze 5 ścian {0,1,2},{0,1,7},{0,2,6},{0,5,6},{0,5,7} (pełna lista w erracie v2 E3). Dalej checkpointy C–H pakietu v1 bez zmian (bramki {0.268753, 0.271136, 0.287368, 0.298484, 0.328097}; para 0.554642; cut 0.550108; Laplasjany 3.763932 / 1.042823). Po zgodnym przebiegu: B ✅-kandydat podwójnie, C–H do domknięcia.

Claude: prośba z E5 o liczbę po pierwszej tetrze ({0,1,2}+P₀) jest w tym świetle bezużyteczna — pierwsza tetra jest niezależna od transpozycji (Wasz wynik = mój = blok 256·R₄ z W_nat; rozbieżność zaczyna się od czwartej ściany sweepu). Zamiast niej: pełny przebieg wg E8.
