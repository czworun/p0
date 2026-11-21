# Asterion — audyt Axis: komutatory i dysklinacja kontaktowa (2026-11-21)

## Zakres i punkt odniesienia

Audyt dotyczy `docs/korzenie/P0-Axis_v0_3.md`, wersja v0.3, odczytana z commita `b6bd5a1735a1206f3f921884212cf3b28f72ea99`.

Wyniki zapisano na gałęzi audytowej `audit/asterion-continuation-2026-11-20`. Nie zmieniano `main`.

Istotne ograniczenie: w repozytorium nie ma kodu źródłowego `P0-AXIS-01`. Poniższy audyt odtwarza algebrę z macierzy w §13–16 oraz geometrię z warunków opisanych w §16ter.4. Wnioski dotyczące geometrii kontaktowej są warunkowe względem tej jawnej interpretacji warunków; nie przypisuję ich nieodczytanemu solverowi.

## A. Sześć komutatorów — rachunek dokładny

Z macierzy `rho_B(M_i)` z §13 obliczono dokładnie
`K_ij = rho_B(M_i) rho_B(M_j) - rho_B(M_j) rho_B(M_i)`.

Wyniki:

- Każde `K_ij` jest rzeczywistą macierzą antysymetryczną 3×3.
- Dla każdego `K_ij`: `-tr(K_ij^2)/2 = 1/32`, zatem długość wektora osiowego wynosi dokładnie `1/(4 sqrt(2))`.
- Nieorientowane osie sześciu komutatorów to dokładnie:
  `(0,±1,±1)`, `(±1,0,±1)`, `(±1,±1,0)`, z utożsamieniem `v ~ -v`.
- Są to sześć osi dwukrotnego obrotu grupy o symetrii ośmiościanu.

Wektor osiowy wyznaczony z macierzy może mieć znak przeciwny do zapisu w §16. Nie jest to rozbieżność, jeżeli §16 opisuje nieorientowane osie. Jeżeli zapis ma oznaczać wektory skierowane, trzeba ujednolicić konwencję orientacji.

## B. Grupa 24-elementowa — tak, ale po dodatkowym wyborze kąta

Niech `K_hat_ij = 4 sqrt(2) K_ij`. Jest to generator obrotu o jednostkowej prędkości kątowej wokół odpowiedniej osi. Wtedy
`R_ij = exp(pi K_hat_ij)`
jest obrotem o pi.

Sześć macierzy `R_ij` jest dokładnymi macierzami signed-permutation z wyznacznikiem +1. Domknięcie generowane przez te sześć macierzy ma dokładnie 24 elementy i jest całym podzbiorem
`{Q: Q jest macierzą signed-permutation 3×3 oraz det(Q)=+1}`.
To obrotowa grupa ośmiościanu, izomorficzna z `S4`.

**Warunek jest istotny:** surowe `exp(K_ij)` nie daje powyższej grupy. Surowy komutator ma kąt `1/(4 sqrt(2))` radiana. Ponieważ ten kąt jest niezerowy algebraiczny, a `pi` jest przestępne, iloraz kąta przez `pi` jest niewymierny; pojedynczy obrót `exp(K_ij)` ma więc nieskończony rząd. Sama przynależność `K_ij ∈ so(3)` ani sam zestaw osi nie wybierają kąta `pi`.

**Status:**
- sześć osi i ich długości — ✅ dokładny rachunek;
- grupa 24 po normalizacji i kącie `pi` — ✅ dokładne domknięcie;
- twierdzenie, że surowe `K_ij` przez eksponencjację dają grupę 24 — ❌;
- kanoniczność wyboru `pi` w teorii P₀ — 💡 / niewykazana.

## C. Nowy most reprezentacyjny: realizacja skręconej reprezentacji

Obrotowa grupa ośmiościanu działa wiernie na czterech nieorientowanych przekątnych bryły (czterech prostych wyznaczonych przez przeciwległe wierzchołki). To daje identyfikację grupy z `S4`.

Jej naturalna trójwymiarowa reprezentacja obrotowa ma charakter klasowy:
- identyczność: 3;
- transpozycja: −1;
- 3-cykl: 0;
- podwójna transpozycja: −1;
- 4-cykl: +1.

Jest to charakter `standard ⊗ sign`, czyli `V_cyc` z §16bis, a nie zwykłej reprezentacji standardowej `V_rho`. To jest dokładnie ten skręt, który Axis v0.3 omawia w §16bis.

Wniosek: po dodaniu jawnego wyboru obrotów o pi, sześć osi komutatorów daje geometryczną realizację grupy `S4` w trójwymiarowej reprezentacji skręconej znakiem. Jest to mocny kandydat na geometryczny słownik dla `V_cyc`.

Granica wniosku: samo to nie konstruuje jeszcze konkretnego splotnika `T: V_rho -> V_cyc` spełniającego warunek skręcony ani nie dowodzi, że operator `C` z Defect jest tym splotnikiem. To osobny test.

## D. Kontakt pięciu czworościanów — rekonstrukcja warunkowa

Przyjmuję dokładnie następujący model geometryczny zgodny z opisem §16ter.4:

1. wspólna krawędź osiowa ma długość 2;
2. zewnętrzna krawędź każdego czworościanu ma długość 2;
3. cztery krawędzie „szprychowe” łączące końce osi z dwoma zewnętrznymi wierzchołkami mają jedną wspólną długość `l`;
4. sąsiednie komórki są sklejone przez dokładną identyfikację kolejnych zewnętrznych wierzchołków;
5. pierścień jest prosty (bez samoprzecięcia), a wszystkie pięć komórek ma tę samą orientację obiegu.

Ustawiam końce osi w `A=(0,0,-1)` i `B=(0,0,1)`. Równość czterech szprych w danym czworościanie wymusza, że oba zewnętrzne wierzchołki leżą w płaszczyźnie `z=0`, na okręgu o tym samym promieniu `r` od osi. Z długości szprych:
`l^2 = 1 + r^2`.

Zewnętrzna krawędź długości 2 jest cięciwą tego okręgu. Dla pięciu równych, zgodnie zorientowanych kroków w prostym pierścieniu kąt środkowy wynosi:
`theta = 2 pi / 5 = 72°`.
Stąd:
`2 = 2 r sin(36°)`,
`r = csc(36°)`,
`l = sqrt(1 + csc^2(36°)) = 1.973430310651966...`.

Współczynnik liniowy długości szprych wynosi:
`l/2 = 0.986715155325983...`.
Skurcz liniowy wynosi:
`(2-l)/2 × 100% = 1.328484467401692...%`.

To jest bezpośrednie rozwiązanie równań kontaktu dla podanego modelu symetrycznego; nie wymaga BFGS ani SLSQP.

## E. Niespójność liczb §16ter.4

W Axis v0.3 podano jednocześnie:
- `radius_scale = 0.973254`;
- szprychy zmieniają długość z 2.000 do około 1.9734;
- skurcz szprych wynosi 2.675%.

Te trzy wartości nie są zgodne, jeżeli odnoszą się do tej samej wielkości liniowej:
- długość 1.9734 z 2.000 oznacza skurcz około 1.33%, nie 2.675%;
- liniowy współczynnik 0.973254 zastosowany do długości 2 daje 1.946508;
- współczynnik liniowy wynikający z podanej długości 1.97343031 to 0.98671516.

Możliwe, że `radius_scale` opisuje inną wielkość (np. parametr kwadratowy albo wysokość/radius, a nie długość szprych). Dokument nie podaje jednak mapowania parametru na współrzędne i długości, więc takiej interpretacji nie można przyjąć bez kodu lub jawnego wzoru.

Dodatkowo kwadrat współczynnika liniowego wynikającego z geometrii wynosi około 0.97360680, a więc również nie jest równy 0.973254. Różnica nie jest wyjaśniona samą zamianą długości na kwadrat długości.

**Status:** liczby §16ter.4 jako jeden wspólny zestaw — ❌ / niespójne w opisanej interpretacji. Sama wartość długości około 1.9734 jest zgodna z analityczną rekonstrukcją; wartość `radius_scale` i procent skurczu wymagają definicji parametru lub korekty.

## F. Czy rozwiązanie symetryczne jest globalne?

W ramach powyższego modelu jednoparametrowego na każdą komórkę, dokładne sklejenie sąsiednich zewnętrznych wierzchołków wymusza równość promieni sąsiednich komórek. Przez cykliczność:
`r_0 = r_1 = ... = r_4`.
Nie ma więc niezależnych promieni pięciu czworościanów, które można by niesymetrycznie optymalizować. Symetria nie jest tu tylko ansatzem solvera — wynika z warunków sklejenia i jednego parametru kształtu na komórkę.

Dla prostego pierścienia i ustalonych długości obu krawędzi równania kontaktu ustalają `theta=72°`, a następnie jednoznacznie ustalają `r` i `l`. W tej klasie dopuszczalnych geometrii rozwiązanie jest jedyne, a zatem globalne — ale to globalność rozwiązania więzów, nie minimum nieokreślonej funkcji energii.

Jeżeli oryginalny `P0-AXIS-01` dopuszcza dodatkowe stopnie swobody (np. nierówne cztery szprychy, przesunięcia osiowe, niepłaskie punkty kontaktu, zmienne długości zewnętrznej krawędzi albo samoprzecięcia), powyższy argument nie rozstrzyga jego pełnego problemu optymalizacyjnego. Bez definicji funkcji celu i pełnych więzów nie wolno nazywać rozwiązania globalnym minimum energii.

## G. Wnioski i zadania do dalszego audytu

1. Dopisać do Axis definicję `K_hat_ij = K_ij / ||K_ij||` oraz jawny wybór kąta `pi`, jeśli intencją jest uzyskanie grupy 24.
2. Zestawić tę realizację z `V_cyc = standard ⊗ sign` i sprawdzić, czy da się zbudować jawny splotnik skręcony zgodny z działaniem na obrazie `C`.
3. Dostarczyć definicję `radius_scale` i kod `P0-AXIS-01` albo jawne równania współrzędnych, by ustalić, czy parametr jest liniowy, kwadratowy, czy opisuje inną wielkość.
4. Zdefiniować funkcję celu i pełny zbiór więzów, jeśli teza ma dotyczyć minimum energii, a nie wyłącznie rozwiązania równań kontaktu.

Najważniejszy rezultat: Axis zawiera bardzo dobry zalążek geometrycznej realizacji skręconej reprezentacji `S4`, ale §16ter.4 ma niezamknięte mapowanie parametru skali i niespójne liczby liniowe. Nie należy scalać tych kwestii w jeden status „zweryfikowane”.
