# MVP-02 v1.3 — kontrola brzmienia (aj)–(ao), semantyka strefy i ocena E-1

Data: 2026-11-23
Autor: Asterion
Zakres: kontrola tekstu bindu v1.3 + Aneks A; analiza semantyczna A.4; opinia o E-1; kontrola H_t. Bez replikacji transportowej i bez podnoszenia statusów Z1.

## 1. Bind i kotwice poboru

Pobrano:
- `docs/mvp-02-spec-v1_3.md` z commitu `e4ac4a6d64c4a69983d7378bc5e82d961bb49f5c`; Git blob `b0399def39397f39d9d058bdaebd2884b8a47391`.
- `docs/mvp-02-spec-v0_4-aneks-a-uzupelnienie.md` z commitu `1ffdd3d4428b74c9306464cfefd02579f8c6f3d4`; Git blob `e68906bed162eb6f0aecec416c6bba9e1b655482`.

Kontrola długości UTF-8:
- K1: tytuł specyfikacji 318 B — PASS.
- K2: ostatnia linia specyfikacji 2245 B — PASS.
- K3: A.3 4372 B, A.4 6377 B — PASS.
- K4: linia erraty zbiorczej v1.3 5044 B; z LF 5045 B — PASS.
- K5: tytuł aneksu 160 B, ostatnia linia aneksu 702 B — PASS.

Specyfikacja ma 86095 B, Aneks 16196 B. Git blob IDs zgodne z podanymi kotwicami. Niezależne przeliczenie SHA-256 plików nie zostało wykonane; blob SHA nie jest SHA-256 i nie jest tu przedstawiany jako jego zamiennik. Zatem kontrola bajtowych kotwic i identyfikatorów Git: PASS; niezależna kontrola SHA-256: NIE WYKONANO.

## 2. Z-A — kontrola (aj)–(ao)

### 2.1 Wierność przeniesienia intencji

- (aj): PASS. Lemat `sup F = (suma |g_a|)^2` poprawnie uwzględnia relację `theta_5 = theta_1 + theta_2`. Wskazany świadek na kątach 0/pi jest zgodny z ograniczeniem trójkąta. Dla wag z Aneksu A iloczyn `g1*g2*g5` jest niezerowy w rozpatrywanych konfiguracjach, więc definicja znaku sigma nie napotyka przypadku `sgn(0)`.
- (ak): PASS co do zasady. Zachowuje lewostronny niezmiennik i odrzuca zwykłą bisekcję znakową jako dowód pierwszego przekroczenia. Nie definiuje jednak jawnie semantyki nierozstrzygniętej strefy przyległej do znanego przekroczenia.
- (al): PASS. Arytmetyka przedziałowa lub zaokrąglenia na zewnątrz są konieczne dla certyfikacji.
- (am): PASS. Etykieta neutralna nie sugeruje dowiedzionej styczności.
- (an): PASS. Definicja infimum dla `t >= 0` jest zgodna z regułą przecieku początkowego.
- (ao): PASS przy dodatnim mianowniku. Przedział ilorazu `[tau_s_lo/tau_i_hi, tau_s_hi/tau_i_lo]` jest poprawny, gdy przedział mianownika jest ściśle dodatni. Osobne traktowanie zera, przecieku i cenzury jest konieczne.

### 2.2 Semantyka strefy przyległej

Werdykt: v1.3 nie rozstrzyga jednoznacznie, czy najwcześniejsza nierozstrzygnięta strefa może być wchłonięta do przedziału lokalizacji pierwszego przekroczenia. Dosłowne czytanie (aa) prowadzi do `NIEROZSTRZYGALNY-PARCJALNY`, gdy lewa połówka pozostaje nierozstrzygnięta. (ak) nie zawiera jawnego wyjątku ustanawiającego absorpcję.

Sama absorpcja może być matematycznie poprawna, ale wyłącznie jako konserwatywny przedział lokalizacji, nie jako certyfikacja strefy wolnej od przekroczenia. Jeżeli wszystkie chwile przed `lo` są certyfikowane jako wolne od przekroczenia, a `hi` jest ocenionym węzłem z `udział(hi) >= theta`, to pierwsze przekroczenie należy do `[lo, hi]`. Strefa `[lo, hi]` nie jest przez to certyfikowana jako wolna od przekroczenia.

Proponowana errata v1.4:

**(ap) ABSORPCJA LEWOSTRONNEJ STREFY NIEPEWNOŚCI DO PRZEDZIAŁU LOKALIZACJI PIERWSZEGO PRZEKROCZENIA:** Jeżeli chronologicznie pierwsza nierozstrzygnięta strefa A.4 pkt 2 bezpośrednio poprzedza oceniony węzeł z `udział >= theta`, wszystkie przedziały poprzedzające początek tej strefy są certyfikowane jako wolne od przekroczenia, a prawy koniec strefy jest ocenionym węzłem przekraczającym próg, strefa może zostać zachowana w całości jako dolna część przedziału lokalizacji pierwszego przekroczenia. Dolny koniec `lo` jest początkiem najwcześniejszej nierozstrzygniętej strefy, a górny koniec `hi` jest pierwszym chronologicznym ocenionym węzłem z `udział >= theta`. Nie wolno opisywać strefy jako certyfikowanej wolnej od przekroczenia. Status RESOLVED jest dopuszczalny wyłącznie wtedy, gdy przedział `[lo, hi]` spełnia kryterium szerokości z A.4 pkt 3, arytmetyka spełnia (al), a wszystkie chwile przed `lo` mają certyfikat braku przekroczenia. Jeżeli którykolwiek z tych warunków nie zachodzi, obowiązuje status NIEROZSTRZYGALNY-PARCJALNY.

Koncesja warsztatu jest dopuszczalna jako konstrukcja przedziału lokalizacji, lecz nie jako niejawna interpretacja obowiązującego v1.3. Ponieważ zmienia status formalny transferu, wymaga jawnej erraty.

## 3. Z-B — ocena E-1

Werdykt: matematyka E-1 jest poprawna.

Dla `S(t) = suma_a g_a cos(omega_a*t)` i `F(t)=S(t)^2`, niech:
- `A = suma_a |g_a|*omega_a`,
- `B = suma_a |g_a|`,
- `C = suma_a |g_a|*omega_a^2`.

Wtedy `|S'| <= A`, `|S| <= B`, `|S''| <= C`, a więc:
`|F''| = |2(S')^2 + 2*S*S''| <= 2*A^2 + 2*B*C = H_t`.

Jest to globalne ograniczenie dla wszystkich `t`. Z klasycznego oszacowania błędu interpolacji liniowej wynika:
`max F na [a,b] <= max(F(a),F(b)) + H_t*(b-a)^2/8`.
Wobec tego E-1 daje poprawny górny certyfikat. Błąd spada kwadratowo z szerokością przedziału, w odróżnieniu od liniowego członu Lipschitza.

### 3.1 Niezależna kontrola H_t (Z-D)

Wagi wyliczono z formy zamkniętej Aneksu A, sekcja 6; częstości z par. 0.4(ii) specyfikacji. Wartości poniżej są wynikiem Asteriona:

| Konfiguracja | Kanał | H_t |
|---|---|---:|
| d1 / d4 | powierzchnia | 2.77992560864190155994 |
| d1 / d4 | wnętrze | 4.46389318477414865320 |
| d2 / d3 | powierzchnia | 1.26276611337246485893 |
| d2 / d3 | wnętrze | 1.40772075287285313478 |
| d5 | powierzchnia | 12.14254450489029524878 |
| d5 | wnętrze | 15.68260375168060008856 |

Wartości są zgodne z liczbami Claude'a w granicach ich publikowanej precyzji, ale nie wszystkie podane przez Claude'a wartości dziesiętne są bezpiecznymi górnymi ograniczeniami. Część została zaokrąglona w dół. Do sześciu cyfr znaczących, z zaokrągleniem na zewnątrz, należy użyć:

| Konfiguracja | Kanał | Bezpieczne H_t |
|---|---|---:|
| d1 / d4 | powierzchnia | 2.77993 |
| d1 / d4 | wnętrze | 4.46390 |
| d2 / d3 | powierzchnia | 1.26277 |
| d2 / d3 | wnętrze | 1.40773 |
| d5 | powierzchnia | 12.1426 |
| d5 | wnętrze | 15.6827 |

Najbezpieczniej przechowywać dokładne wyrażenia lub przedziały, nie pojedyncze zaokrąglone liczby.

### 3.2 Relacja do (al) i bramki (aj)

(al) pozostaje obowiązkowa. Certyfikat E-1 wymaga arytmetyki przedziałowej lub zaokrągleń na zewnątrz dla wag, częstości, `H_t`, wartości węzłowych i końcowego `g_k`.

Bramka świadka z (aj) nie jest potrzebna do samego dowodu ograniczenia `|F''|`: E-1 nie wyznacza supremum i nie korzysta ze świadka maksimum. Wymagana jest jednak osobna bramka sanity `H_t`, która sprawdza: dokładne wagi z Aneksu A, przypisanie częstości z par. 0.4(ii), globalne ograniczenie drugiej pochodnej i bezpieczny kierunek zaokrąglenia.

### 3.3 Ryzyka i warunki wdrożenia

1. Nie wolno używać wartości `H_t` zaokrąglonej w dół.
2. Wartości węzłowe `udział(t_k)` i `udział(t_(k+1))` muszą mieć kontrolowany błąd; samo `H_t` nie naprawia błędów próbkowania.
3. Wagi i częstości muszą pochodzić wyłącznie z zamrożonego bindu; zmiana projektora, wag, miary lub relacji fazowej wymaga ponownej kontroli.
4. Reguła chronologiczna (ak)/(aa) nadal obowiązuje: E-1 poprawia możliwość certyfikowania braku przekroczenia, ale nie uprawnia do przeskakiwania nierozstrzygniętej lewej części.
5. Jeżeli po zadanym limicie procedura nadal nie certyfikuje lewej części, status pozostaje nierozstrzygnięty; nie wolno wymuszać RESOLVED.
6. Limit poziomów, kryterium szerokości, kolejność przetwarzania i zachowanie przy restarcie muszą być jawnie zapisane w v1.4. Nie należy pozostawiać ich jako koncesji implementacyjnej.

## 4. Z-C — rekomendacja dla właściciela

Rekomenduję drogę (2): wprowadzić E-1 jako certyfikat A.4 w v1.4, dołączyć erratę (ap) wyjaśniającą semantykę absorpcji, zamrozić oba pliki nowym bindem, a następnie wykonać formalny rerun rachunku zerowego przez warsztat i niezależnego wykonawcę. To najczystsza droga do KILL K3 = PASS: dwie implementacje muszą uzyskać ten sam formalny status przy tym samym bindzie i tych samych regułach. Droga (1) jest możliwa tylko po niezależnym audycie logów obu istniejących przebiegów i wykazaniu, że spełniają dopiero co doprecyzowane warunki absorpcji oraz szerokości; sama zgodność liczb nie wystarcza. Droga (3), czyli literalne czytanie A, pozostawia kill NIEROZSTRZYGALNY i nie pozwala podnieść K3 do PASS.

## 5. Werdykt końcowy

- Z-A: częściowo PASS; transpozycja (aj)–(ao) wierna, lecz semantyka strefy wymaga erraty (ap).
- Z-B: E-1 matematycznie PASS, warunkowo do wdrożenia po dopięciu arytmetyki przedziałowej i limitów proceduralnych.
- Z-C: rekomendowana droga (2).
- Z-D: wykonano; wartości H_t zgodne z formą zamkniętą, z korektą bezpiecznego zaokrąglenia w górę.

Nie wykonywano rachunków `theta`, `tau`, `U_b`, `F_r` ani `kill`. Nie podnoszono statusów Z1. Raport jest recenzją brzmienia i matematyki certyfikatu, nie replikacją transportową.
