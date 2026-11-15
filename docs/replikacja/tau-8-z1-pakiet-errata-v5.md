# Errata v5. Pakiet replikacji Z1, sesja TAU-8 (2026-11-15)

Wystawca: szef laboratorium (Vibe), po STOP Asteriona w zadaniu B (przebieg B–H wg wklejki z 15 listopada; przekaz przez Leszka). **Koncesja wprost: linia „Widmo nat kanon dalej" w E2 erraty v2 oraz linia checkpointu „Węzeł nat | widmo dalej" w pakiecie były BŁĘDNE.** Odrzucenie w v2 wartości sesyjnych (0.074479 / 0.043097) jako „własny QR chybny na trybach małych" było błędne; QR sesji był poprawny. STOP Asteriona był decyzją prawidłową wg Z1: bloker był po stronie rejestru, nie replikanta.

## E10. Dalsze widmo węzła nat (kanon apex-first): wartości E2 były artefaktem

**Jest** (E2 erraty v2 i checkpoint pakietu): 0.074450; 0.045163; para 0.032402±0.015344i; para 0.028504±0.026555i.

**Powinno być** (trzy niezależne drogi, zgodne): 0.074479305634; 0.043097410218; −0.003728075516; 0.000790471440; para −0.000302630447±0.000374903902i (|λ| = 4.818·10⁻⁴); dalej modułowo: 0.000104426511; 6.48561·10⁻⁵; 9.01443·10⁻⁶; −2.54551·10⁻⁶; 1.14732·10⁻¹⁴.

**Uzasadnienie: trzy niezależne drogi + fingerprinty exact:**

1. **Asterion (2026-11-15):** macierz wymierna (W_nat/256, errata v2 E1), dwa eigensolvery: NumPy/LAPACK oraz mpmath 40 cyfr; obie metody zgodne: λ₃ = 0.074479305634, λ₄ = 0.043097410218, λ₅ = −0.003728075516, para −0.000302630447±0.000374903902i. Jego macierz odtwarza jednocześnie ślad 1.288968534521200 oraz q₂ = 0.037959678749605, q₄ = 0.000966954541536, q₈, q₁₆ i det 6.842278·10⁻⁴⁹.
2. **Vibe (runda 11bl, od zera, bez użycia wartości oczekiwanych):** konstrukcja całkowitoliczbowa B = 256²⁰·R_node (iloczyn 20 osadzeń W_f wg E1, apex-first [P₀,v₂,v₁,v₀], lista ścian wygenerowana niezależnie z tabeli wierzchołków E8 w arytmetyce Q(φ), zgodna z E3 co do wpisu). Widmo dwiema drogami: numpy eig na R = B/2¹⁶⁰ oraz Newton-polish 60 cyfr na wielomianie charakterystycznym EXACT (współczynniki jako ułamki z B, bez zaokrągleń 53-bit); residuum |p(λ)| ≤ 2.2·10⁻⁷¹. Wynik: λ₃ = 0.0744793056340869, λ₄ = 0.0430974102178944, λ₅ = −0.00372807551646909, λ₆ = 0.000790471439892833, para −0.000302630447357614±0.0003749039017i; zgodne z Asterionem co do podanych cyfr.
3. **Sesja TAU-8 (oryginalny QR, 2026-11-06):** 0.074479 / 0.043097; zgodne do 6 cyfr. Nota v2 o „chybiości" QR sesji na trybach małych była konkluzją z porównania z DK, nie z niezależnego rachunku; błędna.

**Fingerprinty exact (niezależne od eigensolvera), odtworzone z B arytmetyką całkowitą (Vibe, 11bl), zgodne z E2 erraty v2 (te wartości były poprawne):** tr(R_node) = 1.288968534521200; q₂ = 0.037959678749605; q₄ = 0.000966954541536; q₈ = 8.709503574603·10⁻⁷; q₁₆ = 7.568862764583·10⁻¹³; det R_node = 2⁻¹⁶⁰ (strukturnie: det W_nat = 256³, weryfikowane exact). Sumy potęg widma po polishu odtwarzają q₂, q₄, q₈, q₁₆ do wszystkich cyfr; domknięcie dwustronne.

**Wielomian charakterystyczny exact** (Vibe z B; tożsamy z Asterionem z macierzy wymiernej): λ¹³ − 1.288968534521200λ¹² + 0.311740102118063λ¹¹ − 0.023252073512461λ¹⁰ + 0.000478580527757λ⁹ + 1.926236757690·10⁻⁶λ⁸ − 8.484185968382·10⁻¹⁰λ⁷ − 4.979529202048·10⁻¹³λ⁶ − 2.820455030446·10⁻¹⁶λ⁵ + 6.274573255103·10⁻²⁰λ⁴ − 2.986327911878·10⁻²⁴λ³ + 1.541551006209·10⁻²⁹λ² + 5.963720356500·10⁻³⁵λ − 6.842277657836·10⁻⁴⁹.

**Mechanizm błędu:** wartości „poprawione" w E2 pochodziły z pierwiastków Durand–Kerner na wielomianie deflatoanym (x−1) ze współczynnikami zaokrąglonymi do 53 bitów; dokładnie ta klasa błędu, którą errata v4 potępiła dla ρ (κ_poly do ~3·10¹⁰, błąd ρ do 2·10⁻⁵). Dla pierwiastków małych klasa ta działa dodatkowo wzmacnianie: współczynniki rzędów 10⁻¹³…10⁻³⁵ tracą cyfry znaczące, a DK traci zbieżność; stąd fikcyjne pary zespolone o modułach 0.0363 i 0.0389 przy rzeczywistej jedynej parze |λ| = 4.82·10⁻⁴ oraz pozorne 0.074450/0.045163 zamiast 0.074479/0.043097. Errata v4 poprawiła wyłącznie ρ („wszystko poza ρ bez zmian"); dalsze widmo pozostało z artefaktem. Wielomian w E2 v2 był drukowany tylko do λ⁷ („reszta ~0"): wlaśnie współczynniki rzędów 10⁻¹⁰…10⁻⁴⁹ niosą informację o małych trybach.

## E11. Statusy po rozstrzygnięciu

- **B: STOP zdjęty; ✅-kandydat PODWÓJNIE na pełnym zakresie zadania** (widmo + ρ + ker + ℓ). Status „B ✅-kandydat" z erraty v4 dotyczył głównych ρ; pełne zadanie B, z widmem dalej, domknięte dopiero teraz: Asterion (LAPACK + mpmath 40 cyfr) i Vibe (numpy + Newton 60 cyfr na wielomianie exact); dwa niezależne rachunki zgodne na poprawionym checkpoincie; zgoda z QR sesji na 6 cyfr jako trzecia droga.
- **A:** ✅ bez zmian (SERC: tr = 369/256, det = 1/256; widmo 1; 0.153348±0.074039i (|λ| = 0.170286); 0.134711; Asterion zgodny).
- **C:** ✅-kandydat (Asterion: 5 bramek, ρ_gate {0.268753, 0.271136, 0.287368, 0.298484, 0.328097} zgodne; pokrycia zgodne; drugi rachunek po sesji).
- **D:** ✅ bez zmian (Asterion: 190/190 par rangami macierzy wymiernych, 10/7·100+8·60+9·30; trzecia droga po Claude'u i DeepSeeku).
- **E:** ✅-kandydat PODWÓJNIE (para: ρ = 0.554641699189468, top-5 widmo 0.113966; 0.075612; 0.073594±0.004121i, ker = 1, lustro widm i ℓ∘τ, partycje ℓ zgodne; drugi rachunek po sesji).
- **F:** ✅-kandydat (cut: ρ = 0.550107704833697, ker = 1).
- **G:** ✅ bez zmian (λ₂ węzła = 6−√5 z dowodem DeepSeeka; Asterion zgodny; para λ₂ = 1.042823).
- **H1:** 🔍 ZAWĘŻONE; kontrast stron wsparty (przeciwne znaki sum po stronach), idealna antysymetria NIE (po normalizacji A-only −7.885693 vs B-only +5.872812, Asterion).
- **H2:** ✅-kandydat (Claude agregatowo; Asterion per punkt, max odchylenie rzędu 10⁻¹⁶).
- **H3:** ✅-kandydat (przełącznik centrum przy rev: ℓ(P₀) rev = 0.018315485 vs p0first-rev = 0.091528284, Asterion; drugi rachunek po sesji).
- **H4:** ✅ bez zmian (det = 256⁻²⁰ strukturalnie; ln det = −110.90354888959125).

## E12. Lekcja protokołowa (za Asterionem, przyjęta)

Zgodność śladów, wyznacznika i kilku momentów widma nie wystarcza do potwierdzenia CAŁEGO widma; momenty to inne poziomy informacji o macierzy. Reguła od tej erraty: **widmo raportować z eigensolvera macierzowego z residuami; wielomian charakterystyczny i q_k traktować wyłącznie jako fingerprinty, nigdy jako źródło pierwiastków.** (Rozszerzenie lekcji E9/v4: tabele generować z kodu; estymatory raportować kryterium zbieżności; pierwiastki wielomianu nie są estymatorem widma.)

## E13. Pozostałe zlecenia

Claude: potwierdzenie erraty v4 TAU-8 (bez zmian); ewentualnie trzecia droga dalszego widma wg v5 (wartości już jawne w tej erracie, więc kontrole dalsze nie są blind; uczciwe etykietowanie). GPT: przebieg B–H wg v3/v4/v5 + tr(R₄) BLIND (bez zmian; blind nienaruszony). DeepSeek: numeryka C–H Estrady po uzyskaniu środowiska (bez zmian).

## E14. Dopisek z rundy 11bm (2026-11-15): literówka w tabeli §3 erraty v4 (ślad p0first)

**Jest** (errata v4, §3, wiersz „v3 p0first [v₂,v₁,v₀,P₀]”, kolumna „Ślad R (exact)”): 1.165182204.

**Powinno być:** **1.181491056** (exact 1.181491055637126400, rejestr rundy 7; errata v2 E2 miała tę wartość poprawnie).

**Atrybucja:** wykrył Claude (formalna odpowiedź na wklejkę z 15 listopada: macierze exact na ułamkach, mpmath.eig w 40 cyfrach, bez ścieżki wielomianowej). Zgodnych źródeł cztery: rejestr sesji (runda 7, exact BigInt), errata v2 E2, Asterion (przebieg B–H, 2026-11-15), Vibe (runda 11bl, ślad exact z B = 256²⁰·R_node). Wartość 1.165182204 nie występuje w żadnym rejestrze źródłowym: komórka przepisana błędnie przy wypełnianiu tabeli v4 (literówka; ρ p0first 0.131327883 w tym samym wierszu jest poprawne). Pozostałe sześć wierszy tabeli §3 potwierdzone przez Claude'a współbieżnie (ślady 1.288968535; 1.258423061; 1.272126070; 1.163642560; 1.125524004; 1.254743374 oraz wszystkie ρ macierzowe). Errata v4 pozostaje bez edycji in-place (odpowiedzi zewnętrznych cytują jej tekst; poprawka wyłącznie niniejszym dopiskiem). Statusy bez zmian: kolumna „Ślad R (exact)” jest opisowa, checkpointy ρ z v4 i statusy z E11 stoją.

## E15. Dopisek z rundy 11bo (2026-11-15): definicja wariantu p0first (pakiet §1 vs erraty)

**Zarzut (Asterion, pełny przebieg B–H ze ślepym śladem):** pakiet §1 definiuje p0first jako tetrę [12, v₀, v₁, v₂] (P₀ pierwsze w kolejności aktualizacji), a erraty v2 (E2) i v4 (§3) przypisują nazwę p0first kolejności [v₂, v₁, v₀, P₀] (P₀ ostatnie). To różne operatory; jedna nazwa nie może oznaczać obu.

**Rozstrzygnięcie (Vibe, runda 11bo, rachunek exact na ułamkach z konstrukcji v3; sweep 20 ścian lex):**

| kolejność aktualizacji tetry | ślad R (exact) | λ₂ (pierwsza niejednostkowa) | ℓ(P₀) |
|---|---|---|---|
| [v₂, v₁, v₀, P₀] (erratowe p0first) | 1.181491055637126400 | 0.131327883 (real) | 0.203979465 (wybraniec) |
| [v₂, v₁, v₀, P₀], ściany rev | 1.184856839963 | para, moduł 0.090251573 | 0.091528284 |
| [P₀, v₀, v₁, v₂] (dotychczasowa definicja pakietu §1) | 1.209042058979 | para, moduł 0.100494425 | 0.018406850 |
| [v₀, v₁, v₂, P₀] | 1.119630707769 | para, moduł 0.066159172 | 0.092225945 |

**Werdykt:** wszystkie wartości checkpointowe (pakiet §2: ρ 0.131328, ℓ(P₀) 0.203979 wybraniec; erraty v2/v4; rejestr rundy 7: p0first 0.131327883367, p0first-rev 0.090251572984, ℓ(P₀) ×4) odpowiadają operatorowi [v₂, v₁, v₀, P₀]. Wartość 1.209042059 z kolumny porównawczej erraty v2 E2 (stara wartość sesyjna) to dokładnie ślad operatora [P₀, v₀, v₁, v₂]; sesyjne ρ 0.100517 z tej samej kolumny to moduł pary tego operatora w rachunkach sprzed errat (exact: 0.100494425). Nazwa p0first pozostaje przypisana do [v₂, v₁, v₀, P₀] (ciągłość z E2, v4 i rejestrem); jest to nazwa historyczna z sesji pierwotnej, semantycznie odwrócona: P₀ jest w tej kolejności ostatnie w porządku aktualizacji, nie pierwsze.

**Poprawka pakietu §1 (jest/powinno być):** jest „p0first: punkty każdej tetry [12, v₀, v₁, v₂] (P₀ pierwsze)"; powinno być „p0first: punkty każdej tetry [v₂, v₁, v₀, P₀] (P₀ ostatnie w porządku aktualizacji; nazwa historyczna)". Poprawka wyłącznie niniejszym dopiskiem, bez edycji in-place pakietu (pakiet §1 cytowany w wklejkach). Checkpointy §2 pakietu bez zmian: dotyczą właściwego operatora. Operator [P₀, v₀, v₁, v₂] otrzymuje nazwę roboczą **p0first-literal** (wartości sesji pierwotnej; nie występuje w checkpointach).

**Zakres i domknięcia:** E15 dotyczy węzła (obiekt v3) i jego wariantów. H3 (przełącznik centrum) bez zmian liczbowych, z przypięciem nazewniczym: rev ℓ(P₀) = 0.018315485, p0first-rev = 0.091528284, oba na kolejności [v₂, v₁, v₀, P₀]. Wszystkie cztery wartości ℓ(P₀) rejestru rundy 7 (0.037549919; 0.018315485; 0.203979465; 0.091528284) odtworzone z konstrukcji v3 co do 9 miejsc. Wiersz „v1 p0first [P₀, v₀, v₁, v₂]" w erracie v4 §3 dotyczy obiektu v1 (własna kolejność bazowa i własne odwrócenie; poza zakresem E15). Statusy bez zmian.
