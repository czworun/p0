# MVP-02 v1.2 — odpowiedź Asteriona na paczkę po rerunku

**Data:** 2026-11-23  
**Zakres:** Pytania 1–3 z paczki „MVP-02: paczka do replikantów (tura doradcza po rerunku v1.2)”.  
**Tryb:** niezależny rachunek osiągalności starego A.3, kontrola formuły supremum, rekomendacja v1.3. Bez obliczania tau, U_b, F_r ani kill.

## 0. Kotwice poboru i bind

Pobrałem oba pliki wskazane w paczce z `main` i zweryfikowałem SHA-256 treści UTF-8:

- specyfikacja: 79 206 B; SHA-256 `ba22394710c84d25cc7d2530dbb0168876736d5a69e57e1837d11fa1a92fd002`; Git blob `42b819aa4b56599567f3fa288aa66babef14cf28`;
- Aneks A: 16 196 B; SHA-256 `820231b0197a081bf498b2c4b36b95bbb381175f313724491f32d61ce5d10151`; Git blob `e68906bed162eb6f0aecec416c6bba9e1b655482`.

Oba hashe SHA-256 są zgodne z paczką. Bind v1.2 jest więc potwierdzony bajtowo. Git blob SHA podano osobno i nie utożsamiam go z SHA-256.

## 1. Pytanie 1 — osiągalność kryterium A.3(vi)

### 1.1. Metoda

Z Aneksu A, sekcji 3 i 6, dla każdego kanału i dystansu:
`F(theta) = (suma_a g_a cos(theta_a))^2`,
przy `theta_5 = theta_1 + theta_2`.

W A.3 komórka o krawędzi h ma `ub(K) = max_vertex F + 2 L_F h`. Komórka musi być podzielona, jeżeli `ub(K) > M + 10^-4`; jeśli `ub(K) <= M + 10^-4`, może pozostać w certyfikacie. Liczyłem więc liczbę komórek przekraczających właśnie próg stopu, a nie tylko liczbę komórek z `ub >= M` podaną w erracie (ac).

Z formy zamkniętej wag wynika `sum |c(a,b)| = (suma_a |g_a|)^2`, a zatem `L_F = 2 (suma_a |g_a|)^2`. Dla h_0 = 2 pi / 120 minimalny poziom jednolitego podziału spełnia:
`ell* = ceil(log2(2 L_F h_0 / 10^-4))`.

Pełną enumerację komórek wymagających podziału wykonałem dla poziomów 0, 1 i 2 (poziom 0 = komórki bazowe; kolejne poziomy = potomkowie wyłącznie komórek, które same przekraczały próg stopu). Dla poziomów 3 i 4 podałem projekcję Monte Carlo: 50 000 losowanych komórek-rodziców na poziom i konfigurację, z estymacją średniej liczby aktywnych dzieci. Błędy w tabeli są przybliżonymi 95-procentowymi pasmami próbkowania; nie są formalnymi granicami deterministycznymi.

M z paczki jest, z dokładnością do zapisu dziesiętnego, równe `(suma |g_a|)^2`. Poniżej wykazuję, że jest to rzeczywiste maksimum, więc w tym rachunku M nie może wzrosnąć przy dalszym próbkowaniu.

### 1.2. Stałe i głębokości jednolite

| Konfiguracja | L_F | ell* |
|---|---:|---:|
| d1 powierzchnia | 0.4295639301 | 9 |
| d1 wnętrze | 0.5027729852 | 10 |
| d2 powierzchnia | 0.2222222222 | 8 |
| d2 wnętrze | 0.1935802469 | 8 |
| d3 powierzchnia | 0.2222222222 | 8 |
| d3 wnętrze | 0.1935802469 | 8 |
| d4 powierzchnia | 0.4295639301 | 9 |
| d4 wnętrze | 0.5027729852 | 10 |
| d5 powierzchnia | 2.0000000000 | 12 |
| d5 wnętrze | 2.0000000000 | 12 |

### 1.3. Komórki, które muszą zostać podzielone

N0, N1 i N2 to pełne enumeracje komórek spełniających `ub > M + 10^-4`. N3 i N4 to projekcje próbkowe.

| Konfiguracja | N0 pełne | N1 pełne | N2 pełne | N3 estymacja | N4 estymacja |
|---|---:|---:|---:|---:|---:|
| d1 powierzchnia | 2 031 360 | 10 187 520 | 53 761 920 | 288.4 mln ± 3.5 mln | 1.574 mld ± 27 mln |
| d1 wnętrze | 2 573 760 | 12 817 920 | 67 282 560 | 358.5 mln ± 4.4 mln | 1.891 mld ± 33 mln |
| d2 powierzchnia | 712 784 | 2 397 544 | 8 613 056 | 31.16 mln ± 0.50 mln | 113.0 mln ± 2.6 mln |
| d2 wnętrze | 750 088 | 2 284 024 | 8 194 512 | 30.31 mln ± 0.48 mln | 111.0 mln ± 2.5 mln |
| d5 powierzchnia | 612 760 | 2 095 536 | 7 674 488 | 29.14 mln ± 0.45 mln | 112.3 mln ± 2.4 mln |
| d5 wnętrze | 781 752 | 2 310 544 | 8 441 208 | 31.46 mln ± 0.49 mln | 122.2 mln ± 2.7 mln |

D3 ma te same wartości co d2, a d4 te same co d1 (wagi i wartości bezwzględne wag są identyczne na tych parach dystansów).

Suma N0+N1+N2 jest dokładną dolną granicą liczby podziałów potrzebnych do osiągnięcia kryterium w tym drzewie, przy niezmienionym M. Każda z tych komórek ma `ub > M + 10^-4`, więc algorytm nie może zakończyć przed jej podziałem. Wyniki:

| Konfiguracja | N0+N1+N2 | Krotność budżetu 10^7 | Nadwyżka rzędów wielkości, dolna granica |
|---|---:|---:|---:|
| d1 powierzchnia | 65 980 800 | 6.60x | 0.82 |
| d1 wnętrze | 82 674 240 | 8.27x | 0.92 |
| d2 powierzchnia | 11 723 384 | 1.17x | 0.07 |
| d2 wnętrze | 11 228 624 | 1.12x | 0.05 |
| d5 powierzchnia | 10 382 784 | 1.04x | 0.02 |
| d5 wnętrze | 11 533 504 | 1.15x | 0.06 |

Zatem budżet 10^7 nie wystarcza w żadnej z sześciu konfiguracji, nawet przed poziomem 3. Już dokładna dolna granica d5 powierzchnia przekracza budżet o 382 784 podziały.

Suma N0 do N4, przy użyciu projekcji N3 i N4, wynosi orientacyjnie: d1 powierzchnia 1.93 mld; d1 wnętrze 2.33 mld; d2 powierzchnia 155.9 mln; d2 wnętrze 152.5 mln; d5 powierzchnia 151.8 mln; d5 wnętrze 165.2 mln. To jest projekcja tylko do poziomu 4, nie pełny koszt aż do ell*. Nie ekstrapoluję dalej jako wyniku pewnego: przy wysokich poziomach aktywne gałęzie stają się rzadkie i prosta losowa próbka może je pominąć. Dla decyzji o budżecie nie jest to potrzebne, ponieważ dolna granica N0+N1+N2 już obala 10^7.

### 1.4. Rozstrzygnięcie Pytania 1

Dla starego numerycznego A.3 budżet 10^7 jest za mały we wszystkich konfiguracjach. Ścisła dolna granica przekroczenia to 1.04x–8.27x budżetu (0.02–0.92 rzędu wielkości). Projekcja próbkowa do poziomu 4 sugeruje 15.2x–233x budżetu, lecz nie przedstawiam jej jako formalnego kosztu do końcowej głębokości ell*.

Istnieje jednak wynik silniejszy, który usuwa potrzebę takiego kosztorysu: supremum A.3 jest dostępne analitycznie i dokładnie z formy zamkniętej wag. W następnym punkcie przedstawiam dowód. Jeżeli zostanie przyjęty do v1.3, liczba podziałów A.3 potrzebnych do certyfikacji sup wynosi zero.

## 2. Pytanie 2 — rekomendacja dla v1.3

**Wybieram dokładnie opcję (gamma): INNA REGUŁA — zamienić numeryczny branch-and-bound A.3 na analityczny certyfikat supremum z formy zamkniętej wag.** Powód: dla wszystkich pięciu orbit i obu kanałów zachodzi dokładnie `sup F = (suma_a |g_a|)^2`; maksimum jest osiągane na podtorusie w fazach 0/pi, które należą do siatki bazowej N_w=120. Wartości M podane w paczce są właśnie tym maksimum. Podwyższanie budżetu lub usuwanie progu absolutnego jest w tej sytuacji niepotrzebne.

### 2.1. Dowód analityczny do włączenia do v1.3

Z definicji wag w Aneksie A:
`F(theta) = (suma_a g_a cos(theta_a))^2`,
`theta_5 = theta_1 + theta_2`.

Ograniczenie trójkąta daje:
`F(theta) <= (suma_a |g_a|)^2`.

Dla każdego dystansu i kanału w Aneksie A współczynniki g1, g2 i g5 są niezerowe. Niech:
`sigma = sgn(g1*g2*g5)`.

Wybierz theta1 i theta2 z {0, pi}, tak aby:
`cos(theta1) = sigma*sgn(g1)`,
`cos(theta2) = sigma*sgn(g2)`.

Ponieważ oba kąty są 0 lub pi:
`cos(theta5) = cos(theta1+theta2) = cos(theta1)*cos(theta2) = sgn(g1*g2) = sigma*sgn(g5)`.

Następnie wybierz theta3 i theta4 z {0, pi}, aby:
`cos(thetaa) = sigma*sgn(ga)` dla a=3,4.
Jeżeli g3=0, theta3 jest dowolne.

Wtedy każdy niezerowy składnik spełnia `ga*cos(thetaa) = sigma*|ga|`, więc:
`F(theta) = (suma_a |g_a|)^2`.

Osiągnięto górne ograniczenie, zatem:
`max na T_theta F = sup po czasie F = (suma_a |g_a|)^2`.
Ostatnia równość wynika z gęstości orbity fazowej w T_theta. Świadek maksimum używa wyłącznie kątów 0 i pi, a więc jest obecny na siatce N_w=120 (indeksy 0 i 60). Nie wymaga lokalnego optymalizatora ani branch-and-bound.

### 2.2. Dokładne supremum i theta

| Dystans | Kanał | suma |g_a| | sup F | theta = sup/2 |
|---|---|---:|---:|---:|---:|
| d1, d4 | powierzchnia | (13+6 sqrt(5))/57 | ((13+6 sqrt(5))/57)^2 = 0.214781965063086 | 0.107390982531543 |
| d1, d4 | wnętrze | sqrt(5)/10 + 95/342 | (sqrt(5)/10 + 95/342)^2 = 0.251386492577149 | 0.125693246288574 |
| d2, d3 | powierzchnia | 1/3 | 1/9 = 0.111111111111111 | 1/18 = 0.055555555555556 |
| d2, d3 | wnętrze | 14/45 | 196/2025 = 0.096790123456790 | 98/2025 = 0.048395061728395 |
| d5 | powierzchnia | 1 | 1 | 0.5 |
| d5 | wnętrze | 1 | 1 | 0.5 |

Wartości M z tabeli rerunu zgadzają się z tymi wartościami po zaokrągleniu prezentacyjnym. W konsekwencji errata (ad) o dwóch przebiegach theta_lo/theta_hi nie jest potrzebna dla tego modelu: theta jest dokładne, a nie przedziałowe.

### 2.3. Zalecane brzmienie decyzji v1.3

- A.3: usunąć numeryczny branch-and-bound, budżet 10^7 i kryterium szerokości 10^-4; w ich miejsce wstawić powyższy lemat, świadek fazowy oraz dokładną tabelę theta.
- Źródło g_a: wyłącznie forma zamknięta z sekcji 6 Aneksu A, nie zaokrąglone do czterech miejsc tabele.
- A.4: zachować obowiązek certyfikowania pierwszego przekroczenia. Wprowadzić erratę (af) z niezmiennikiem lewostronnym oraz arytmetykę przedziałową/zaokrąglenia na zewnątrz z (ag). Zmienić definicję na `tau = inf{t >= 0 : udział(t) >= theta}` zgodnie z (ai). Etykietę STYCZNY zastąpić neutralnym NIEROZSTRZYGNIĘTY-PRZEDZIAŁ zgodnie z (ah).
- (ae), czyli przedziałowe U_b wynikające z niepewności theta, staje się zbędne po przyjęciu lematycznego A.3. Jeżeli właściciel zdecyduje się nie przyjąć dowodu (γ), wtedy (ae) pozostaje konieczną naprawą wersji (α+).

## 3. Pytanie 3 — ryzyka opcji (alpha+) i pasożytnicze zależności

### 3.1. Co jest bezpieczne w (alpha+)

Usunięcie absolutnego progu stopu samo w sobie nie tworzy cyrkularności. Jeżeli `M` jest rzeczywistym dolnym ograniczeniem, a `max ub` poprawnym globalnym górnym ograniczeniem, to `[M,max ub]` jest poprawnym przedziałem obejmującym supremum przy każdym budżecie. Jego szerokość mówi, jak mocny jest wynik. Szeroki przedział nie może być traktowany jak punktowy sup.

Podobnie poprawne jest użycie przedziałów czasów dla dwóch kanałów i ograniczenia ilorazu:
`U_b in [tau_s_lo/tau_i_hi, tau_s_hi/tau_i_lo]`,
ale tylko wtedy, gdy mianownik jest ściśle dodatni. Gdy przedział tau_i obejmuje zero albo przypadki B4, potrzebna jest osobna obsługa na rozszerzonej osi rzeczywistej.

### 3.2. Ryzyka wymagające jawnego zabezpieczenia

1. **Budżetowo zależna rozstrzygalność.** Przy małym budżecie szerokie przedziały dadzą NIEROZSTRZYGALNY-PARCJALNY; przy większym mogą dać klasę. To jest poprawne, jeśli raportuje się przedział i budżet, ale nie wolno nazywać wyniku przy małym budżecie „typowym” tylko dlatego, że nie udowodniono skrajnej klasy. Klasa typowa musi być wspólna dla wszystkich wartości dopuszczonych przez przedziały; w przeciwnym razie wynik jest nierozstrzygnięty.

2. **Niezagnieżdżone ograniczenia.** Przy obecnej regule lokalne `ub(child)` może być większe od `ub(parent)`, mimo że oba są poprawnymi górnymi ograniczeniami. Wtedy `max ub` może chwilowo wzrosnąć po podziale, a przedziały raportowane dla kolejnych budżetów nie muszą być zagnieżdżone. Zalecam `ub(child) = min(ub(parent), ub_lokalne(child))`; oba składniki są górnymi ograniczeniami, więc minimum także nim jest, a refinowanie nie pogarsza odziedziczonej granicy.

3. **Utrata korelacji.** Niezależne dzielenie przedziałów tau_s i tau_i jest bezpieczne, ale może nadmiernie poszerzyć przedział U_b, bo oba czasy zależą od tego samego theta. To prowadzi do fałszywego braku rozstrzygnięcia, nie do fałszywego wsparcia hipotezy. Trzeba oznaczyć wynik jako konserwatywny i nie zawężać go ręcznie po obejrzeniu klasy.

4. **Selektywne zwiększanie budżetu.** Przydzielanie dodatkowych podziałów tylko orbitom, których wynik jest bliski pożądanemu rozstrzygnięciu, wprowadza pasożytniczą zależność klasy od decyzji wykonawcy. Budżet, kolejność i kryterium przydziału muszą być pre-registrowane i jednakowe dla wszystkich konfiguracji.

5. **B4, cenzury i zero w mianowniku.** Dzielenie przedziałów przy tau_i=0, przedziale zawierającym zero, prawostronnym cenzurowaniu lub tau=0 obustronnie wymaga jawnych reguł. Nie wolno przepuszczać tych przypadków przez zwykły wzór na iloraz.

6. **F_r.** Gdy nie ma rozstrzygalnych transferów TEST, F_r nie ma mianownika. Gdy istnieją, ale ich U_b są przedziałami, nie wolno zastąpić ich punktowymi środkami przedziałów. F_r pozostaje diagnostyką i powinien mieć oddzielny status przedziałowy lub brak mianownika.

### 3.3. Ryzyka rekomendowanego (gamma)

Główne ryzyko (γ) jest inne: dowód działa, ponieważ obserwabla jest kwadratem jednej sumy modalnej, a cel jest jednowymiarowy. Gdyby w przyszłej wersji zmieniono obserwablę, projektor celu, postać wag albo relację fazową, lemat może przestać obowiązywać. Dlatego dowód i jego warunki muszą być przypięte do dokładnej definicji `F` i Aneksu A v1.2. Nie wolno automatycznie przenosić go na inną miarę lub wielowymiarowy cel.

Drugi warunek: w v1.3 należy zachować A.4 jako osobny, nadal nietrywialny problem. Dokładne theta nie rozwiązuje automatycznie problemu pierwszego przekroczenia ani błędów numerycznych w czasie. Erraty (af), (ag), (ah) i (ai) pozostają wymagane.

## 4. Ograniczenia wykonania

Planowany limit został zadeklarowany przed rachunkiem. Środowisko wykonawcze przerywało długie wywołania po ok. 60 s; szczytowy RSS przekroczył planowany limit pamięci 2 GB. Dlatego N0–N2 podaję jako pełne enumeracje numeryczne, a N3–N4 jako jawnie oznaczone estymacje próbkowe. Nie przedstawiam próbki poziomów 5+ jako pełnego, deterministycznego kosztu do ell*. To ograniczenie nie wpływa na wniosek o 10^7, bo dokładne dolne granice N0+N1+N2 są już większe od budżetu w każdej konfiguracji. Dowód analityczny supremum nie zależy od tej enumeracji.

## 5. Werdykt

- **Pytanie 1:** stary branch-and-bound nie mieści się w 10^7 podziałów. Ścisła dolna granica to 1.04x–8.27x budżetu po trzech pierwszych generacjach; projekcja próbkowa do poziomu 4 to ok. 15x–233x. Pełny koszt do ell* nie został tu wyznaczony deterministycznie.
- **Pytanie 2:** rekomendacja **(gamma)** — zastąpić A.3 analitycznym lematem `sup F=(suma |g_a|)^2`; theta jest dokładne, więc usunąć (ac), (ad) i cały budżet B&B dla tego celu.
- **Pytanie 3:** (alpha+) jest bezpieczne tylko przy rygorystycznych przedziałach, zagnieżdżonych ograniczeniach, wspólnym pre-registrowanym budżecie oraz konserwatywnej klasyfikacji wszystkich wartości w przedziałach. Nie jest jednak potrzebne dla sup w tym modelu po przyjęciu (gamma).

Nie wykonywałem rachunku tau, U_b, F_r ani kill.
