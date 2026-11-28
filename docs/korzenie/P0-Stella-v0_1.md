# P0-Stella v0.1 - rejestr laboratorium stella octangula

**Status:** rejestr laboratorium (wzorzec Lattice i STALK: rejestr, nie filar). Laboratorium otwarte rozkazem Leszka Papiernika (właściciel projektu P0) 2026-11-28; szef laboratorium: Vibe; wykonawcy zewnętrzni przez relay Leszka: Asterion (GPT-6), Claude, DeepSeek. Wersja rejestru: v0.1 (otwarcie, 2026-11-28); v0.1.1 (runda replikacyjna częściowo rozliczona); v0.1.2 (werdykt Asteriona: Z1 otwarty; tablice referencyjne konstrukcji S i C jako pokwitowanie Z3; obserwacje post-hoc, 2026-11-28); v0.1.3 (pokwitowanie konstrukcji Claude: tablice S i C zgodne z załącznikiem A, potwierdzone niezależnym odtworzeniem Vibe; korekta Asteriona: uwaga o polu współdzielenia wycofana; 2026-11-28); v0.1.4 (replikacja Copilota rozliczona: pełna zgodność tablic, wielomianów i widma; kwalifikacja do puli Z1; DeepSeek zastąpiony Copilotem decyzją właściciela, 2026-11-28); v0.1.5 (finalny werdykt kontrolny Asteriona: Z1 zaliczone; P2-1 podniesione do ✅; 2026-11-28); v0.1.6 (prerejestracja P3: rdzeń bezklikowy jako warstwa modelowa; bramki G3.1-G3.4 przed rachunkiem; 2026-11-28); v0.1.7 (wynik P3-1 kandydat 🔍: widmo rundy rdzenia, nowa faza 36.391244284100 stopnia, rho_2 = 1/5, test 720 kolejnosci: 5 klas widm; 2026-11-28); v0.1.8 (runda replikacyjna P3 rozliczona: Claude i Copilot zgodni, kontrola Vibe wielomianów klas i tablic; status P3-1 🔍 wzmocniony, czeka na finalny werdykt Asteriona; 2026-11-28); v0.1.9 (finalny werdykt kontrolny Asteriona: Z1 zaliczone; P3-1 podniesione do ✅; załącznik C: wielomiany klas testu 720; 2026-11-28); v0.1.10 (prerejestracja P5: domknięcie pod Oh; lematy L5a-L5c, bramki G5.1-G5.5 przed rachunkiem; 2026-11-28); v0.1.11 (wynik P5: Oh=48, L5b 288/288, orbita S=24, Stab={id,-I}, H5c potwierdzona: klasa 48 z P2 = orbita Oh; P5-1 🔍 kandydat; 2026-11-28); v0.1.12 (rozliczenie rundy replikacyjnej P5: Claude i Copilot zgodni, kontrola Vibe potwierdzona, luka jawna: pokwitania Copilota; 2026-11-28); v0.1.13 (uzupelnienie Copilota: luka zamknieta; spis klas 720 z reprezentantami; pula Z1 gotowa do werdyktu; 2026-11-28); v0.1.14 (finalny werdykt kontrolny Asteriona: P5-1 = ✅, Z1 zaliczone; 2026-11-28); v0.1.15 (prerejestracja P6: rodzina mK4 ustalona na delegacji właściciela, bipiramida 5K4, ośmiościan jako 6K4, bramki G6.0-G6.6 przed rachunkiem, Z9; 2026-11-28); v0.1.16 (wynik P6: rachunek główny Vibe, bramki G6.0-G6.6 rozstrzygnięte, kwartetyk nierozkładalny nad Q, faza pary 33,311881184741 stopnia, dekompozycja izotypowa R_O, tablica R_5 w załączniku D, status P6-1 kandydat; 2026-11-28); v0.1.17 (errata do wyniku P6: odwrócony porządek rundy w rachunku głównym, wartości G6.2-G6.4 poprawione za zgodnymi replikacjami Claude i Copilot, faza pary 30,817605013288 stopnia, rho_2 0,209788902575374, tablica R_5 poprawiona w załączniku D, rozliczenie rundy, P6-1 wzmocniony; 2026-11-28); v0.1.18 (finalny werdykt kontrolny Asteriona: P6-1 = ✅, Z1 zaliczone z erratą konwencji; 2026-11-28) v0.1.19 (prerejestracja GO P4: transformacja nośnika pod −I, linia Lattice, bramki G4.1-G4.6 przed wydaniem wrzutki dla Claude i DeepSeek; 2026-11-28); v0.1.20 (rozliczenie etapu 1 GO P4: Claude i Copilot zgodni, H4b i H4d potwierdzone, kontrola Vibe od definicji zgodna w całości, zmiana składu odnotowana, audyt krzyżowy G4.6 następny; 2026-11-28). Poziom wyniku P2: ✅ (od 2026-11-28: dwie pełne replikacje zewnętrzne zgodne, finalny werdykt kontrolny Asteriona, Z1 zaliczone; wzorzec E-01 spełniony; runda: Claude + Copilot, zlecenie DeepSeeka zawieszone, nie odwołane). Poziom wyniku P3: ✅ (od 2026-11-28: pełna runda replikacyjna, finalny werdykt kontrolny Asteriona, Z1 zaliczone).

## 1. Mandat i zweryfikowana geometria (rachunek niezależny Vibe 2026-11-28)

Badanie unikatowej geometrii stella octangula: dwóch czworościanów przenikających się ze wspólnym środkiem P0, oraz konsekwencji dynamicznych, algebraicznych i strukturalnych. Konwencja współrzędnych: T1 = {(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)}, T2 = -T1.

Fakty (rachunkowo, nie z pamięci):
1. T2 = -I(T1); P0 = (0,0,0) jedyny punkt stały odwzorowania wymieniającego połówki.
2. 8 wierzchołków obu K4 = wierzchołki sześcianu; połówki to klasy parzystości (szachownica).
3. Opol bryl: T1 = {s_i >= -1}, T2 = {s_i <= 1} dla s1 = x+y+z, s2 = x-y-z, s3 = -x+y-z, s4 = -x-y+z.
4. Część wspólna = foremny ośmiościan o wierzchołkach (±1,0,0), (0,±1,0), (0,0,±1) = środki ścian sześcianu (dualność).
5. Parowanie krawędzi bijektywne: każda krawędź T1 przecina dokładnie jedną krawędź T2 w środkach krawędzi; 6 punktów styku = wierzchołki rdzenia.
6. Graf ośmiościanu nie zawiera żadnego K4 (15/15 czwórek odrzuconych, pigeonhole): rdzeń bezklikowy; konsensus między połówkami może przechodzić wyłącznie przez 6 przecięć.
7. Pełna symetria stelli: Oh (48), obroty izomorficzne z S4; ten sam abstrakcyjny S4 w realizacji permutacji wierzchołków K4 i obrotów pary sześcian/ośmiościan.
8. Lekcja techniczna: test punkt-na-odcinku przez parametr dzielenia psuje się przy zerowym składniku kierunku; iloczyn wektorowy zamiast dzielenia.

## 2. Konwencje P1 (zatwierdzone przez właściciela 2026-11-28, blokują P2-P6)

- P1-a Numeracja: połówka A: A0=(1,1,1), A1=(1,-1,-1), A2=(-1,1,-1), A3=(-1,-1,1); połówka B: B_i = -A_i (definicja przez -I); rdzeń: O1=(1,0,0), O2=(-1,0,0), O3=(0,1,0), O4=(0,-1,0), O5=(0,0,1), O6=(0,0,-1); pary antypodyczne: (O1,O2), (O3,O4), (O5,O6).
- P1-b Nośnik: stan pary (x^A, x^B) w R^4 x R^4 na wierzchołkach połówek; rdzeń POCHODNY, bez własnych stopni swobody (wartość w punkcie styku wyliczana z połówek). Uzasadnienie: rdzeń bezklikowy jako sala spotkań, nie trzeci gracz.
- P1-c Operatory lokalne: M_m identyczne jak na pojedynczym K4 (identyczność z wierszem m = (1/4,1/4,1/4,1/4)); sprzężenie między połówkami wyłącznie przez 6 punktów styku, każdy punkt = dokładnie jedna para krawędzi.
- P1-d Kolejność rundy: wariant bazowy: połówki kolejno (pełna runda A, potem pełna runda B); przeplatane tylko jako kontrola drugorzędna.
- P1-e Koordynacja z kolejką Lattice: P4 (transformacja nośnika pod -I) pozostaje GO dla Claude'a i DeepSeeka w Lattice; laboratorium nie dubluje, konsumuje wynik.

## 3. Prerejestracja P2 (szef lab., 2026-11-28, przed rachunkiem; Z9)

Poziom E1a (rachunek operatora). Nośnik R^8 = (x^A, x^B), indeksy 0-3 = A0-A3, 4-7 = B0-B3.

Definicje jawne (Z2):
- R = M3*M2*M1*M0 jak w E-01; D = diag(R, R) na R^8 (runda A, potem runda B).
- Punkt styku O_p = środek krawędzi {i,j} połówki A oraz krawędzi {k,l} połówki B; biiekcja (fakt 5), przyporządkowanie: O1: A{0,1} x B{2,3}; O2: A{2,3} x B{0,1}; O3: A{0,2} x B{1,3}; O4: A{1,3} x B{0,2}; O5: A{0,3} x B{1,2}; O6: A{1,2} x B{0,3}. Wartość połówki na styku: średnia krawędziowa e_A = (x^A_i + x^A_j)/2, e_B = (x^B_k + x^B_l)/2.
- Operator styku W_p = I_8 - v_p v_p^T, v_p = (e_i + e_j - e_k - e_l)/2 w R^8 (niezerowe współrzędne +1/2 na i, j; -1/2 na 4+k, 4+l); norma 1. W_p = rzut ortogonalny na hiperplan zgody e_A = e_B w punkcie styku (konsensus pełny, bez relaksacji; różnice wewnątrz krawędzi niezmienne).
- C = W6 W5 W4 W3 W2 W1 (kolejność wg indeksów rosnąco, O1 pierwszy).
- Wariant bazowy V1: S = C*D. Kontrole: V1b: S' = D*C; V1c: kolejność styków malejąco C' = W1 W2 ... W6, S'' = C'*D; V0: S0 = D.

Bramki (przed rachunkiem):
- G2.1 (sanity): widmo S0 = widmo R zdublowane; referencje E-01: 1; 0.134710644695282; 0.153347802652359 +/- 0.074039102546458i.
- G2.2: dim ker(S - I) wyliczana dokładnie; hipoteza H2a: dim = 1.
- G2.3: pełne widmo V1; punkty referencyjne: 25.772093727472 stopnia (para E-01); hipotezy H2b (faza inna) vs H2c (faza 25.772093727472 w granicy 0.005 stopnia).
- G2.4: rho(S) raportowane.

## 4. Wynik P2 (sprawozdawcze po prerejestracji; sesja 2026-11-28, wątek otwarcia)

**P2-1 (kandydat 🔍): TOŻSAMOŚĆ WIELOMIANOWA cp(V1) = z^4 * cp(R), dokładna, na ułamkach.** Pełne widmo niezerowe operatora pary równa się dokładnie widmu pojedynczego K4; dodatkowo 4 wartości własne 0 (ranga S = 4, dim ker(S) = 4 algebraiczna i geometryczna). Metody zgodne: Faddeev-LeVerrier i Newton ze śladów potęg (zgodna bitowa na ułamkach), Durand-Kerner + testy sum potęg vs tr(S^k) dokładne (max odchylenie 2.2e-16), Sturm z bisekcją dla pierwiastków rzeczywistych.

Rozstrzygnięcia bramek:
- G2.1 SPEŁNIONA dokładnie: cp(V0) = cp(R)^2 (tożsamość wielomianowa; kontrola float DK ograniczona zbieżnością liniową na pierwiastkach podwójnych, 9.6e-07, udokumentowana jako granica metody).
- G2.2: H2a POTWIERDZONA dokładnie: dim ker(V1 - I) = 1 (kontrola V0: 2). Echo faktu 1.
- G2.3: H2c SPEŁNIONA DOKŁADNIE: para zespolona V1 jest parą E-01 co do wielomianu; theta = 25.772093727472 stopnia (odchylenie 0).
- G2.4: rho(V1) = 1.

Struktura (tożsamości dokładne):
- U = {(x,x)} (przestrzeń zgodności połówek, wymiar 4) niezmiennicza pod S; S|_U ma RZĄD 1: mapa uśredniająca z wagami (125, 225, 305, 369)/1024 (suma 1, wagi nierówne; odcisk kolejności styków). Widmo S|_U = {1, 0, 0, 0}: konsensus na nośniku zgodności w JEDNEJ rundzie.
- Iloraz R^8/U: widmo = pierwiastki wielomianu przejściowego E-01 (256L^3 - 113L^2 + 18L - 1) plus 0. Pełny rytm pary (0.134710644695282 oraz para zespolona 0.153347802652359 +/- 0.074039102546458i) żyje NA ILORAZIE, czyli w strukturze relacyjnej między połówkami.
- Kontrola domknięcia: cp(S|_U) * cp(S na ilorazie) = cp(S) dokładnie.
- Kontrole: cp(V1b) = cp(V1) (klasyczna tożsamość AB/BA); cp(V1c) = cp(V1) (odwrotna kolejność styków; 2 z 720 sprawdzonych) mimo że operatory W_p NIE komutują parami; rozpiętość {v_p} ma rangę dokładnie 4.

Odczyt sprawozdawczy (interpretacyjny, nie podnoszony do statusu twierdzenia): konsensus przez ściany jest natychmiastowy (rundowy), a rytm zbliżania E-01 nosi relacja między połówkami (iloraz); wspólny środek jest jeden. Most do P0-Defect: 6 kierunków v_p = struktura oktaedryczna V_cyc pary.

Erraty wewnętrzne sesji (Z0, trwałe, wszystkie znalezione przed raportem): (1) skalowanie int() obcinało ułamki (mianowniki R do 256); (2) pdiv wyrównywał dzielnik z przesunięciem zamiast w indeksie 0 (pętla nie terminowała); (3) łańcuch Sturma normalizowany monicznie zmieniał znak (fikcyjne pierwiastki); (4) test tożsamości z^4 podawał z^4 jako stałą 1. Lekcja: podwójne metody dokładne w jednej sesji łapią błędy, które przechodzą przez pojedynczy rachunek.

Provenance (Z1): wykonawca Vibe (szef lab.), sesja nowa 2026-11-28, kod własny, współdzielenie kodu: brak, dostęp do wcześniejszych wyników: przekazówka (fakty 1-8, referencje E-01 ze STAN v1.11), rodzaj wykonania: E1a, wynik wobec bramek jak wyżej. Status 🔍 kandydat: do ✅ wymaga niezależnej replikacji zewnętrznej (zlecenie przygotowane).

## 5. Odnogi i kolejka badawcza

Odnogi kandydackie: (a) pełny test 720 kolejności styków (czy widmo niezależny od kolejności mimo niekomutatywności); (b) wagi wyborca w S|_U vs kolejność styków (most do C2 i ruchomego P0); (c) dowód algebraiczny tożsamości z^4 (dlaczego iloraz niesie cubic E-01); (d) interpretacja kliniczna: rytm w relacji, konsensus natychmiastowy przez ścianę; (e) P3 wzmocnione: konsensus przez styki wystarcza w jedną rundę na U.

Kolejka: P3 rdzeń bezklikowy (dynamika konsensusu na grafie ośmiościanu); P4 transformacja nośnika pod -I (koordynacja z Lattice, GO Claude i DeepSeek); P5 domknięcie rodziny operatorów pod sprzężeniami Oh; P6 ośmiościan jako bipiramida i rodzina mK4. Zasada kolejności: prerejestracja bramek przed każdym rachunkiem (Z9).


## 6. Runda replikacyjna (częściowo rozliczona, 2026-11-28)

**Claude (Sonnet 5.5, pełna replikacja): ZGODNA.** Arytmetyka wymierna (SymPy). Wielomiany: cp(S0) = (z-1)^2 * (256z^3 - 113z^2 + 18z - 1)^2 / 65536; cp(S) = z^4 * (z-1) * (256z^3 - 113z^2 + 18z - 1) / 256, oba dokładnie, tożsamości potwierdzone niezależnie od rachunku głównego. Ślad S = 369/256 = ślad R; det S = 0; det S0 = 1/65536. dim ker(S - I) = 1, wektor własny (1,1,1,1,1,1,1,1); dim ker(S) = 4 (zero półproste; kontrola dim ker(S0) = 0). Widmo: 1; 0.134710644695282; 0.153347802652359 +/- 0.0740391025464575i, moduł 0.170286045476991, argument 25.7720937274724 stopnia; zero poczwórne. rho(S) = 1. Bramki: G2.1 spełniona; H2a potwierdzona; H2c potwierdzona (odchylenie rzędu 1e-13 stopnia); H2b niepotwierdzona; G2.4 rho = 1. Widmo niezerowe S = widmo R jednokrotnie, dublowanie tylko w S0. Pola niezależności: wynik P2 nieznany przed rachunkiem; plik rejestru nieczytany; znał własne widmo R z E-01 z tego samego czatu (referencje R i tak jawne w bramce G2.1). Replikacja uznana przez szefa lab. za niezależną od wyniku głównego.

Errata Claude (sprawozdawcza, dotyczy jego raportu replikacyjnego E-01 z wcześniejszej sesji): wartość 0.153347802659 przepisana błędnie, poprawnie z własnego wydruku 0.153347802652359; błąd przepisania, nie rachunku; argument 25.772094 stopnia był poprawny. Utrwalone zgodnie z Z0.

**Asterion (GPT-6, kontroler): walidacja specyfikacji V1-V5 zaliczona; uwaga formalna PRZYJĘTA** przez szefa lab.: w przyszłych specyfikacjach konwencja wielomianu charakterystycznego deklarowana jawnie jako det(zI - S) (Z2; dla S o wymiarze 8 obie konwencje dają ten sam wielomian, więc wynik P2 bez zmian). Własny rachunek kontrolny (SymPy, arytmetyka dokładna): tożsamości wielomianowe, wymiary jąder i widmo zgodne z rachunkiem głównym. Deklaracja niezależności: czytał docs/korzenie/P0-Stella-v0_1.md przed rachunkiem (wyniki główne były tam już opublikowane), dlatego sam nie zalicza swojego rachunku jako drugiej niezależnej replikacji Z1; werdykt Z1 odroczony do kontroli raportów Claude i DeepSeek. Ustalenie wzorcowe z tej rundy: kontroler znający wynik główny przed rachunkiem deklaruje to jawnie w polach niezależności i nie wchodzi do puli replikacji Z1; jego rachunek pozostaje kontrolą.

**DeepSeek: przerwa; zlecenie aktualne** (samodzielne, jak przy E-01; instrukcja dodana: nie czytać pliku rejestru przed rachunkiem, pole niezależności wypełnić jawnie).

**Status P2-1: 🔍 wzmocniony (decyzja szefa lab.).** Warunek liczbowy Z1 (dwa zgodne niezależne rachunki wspólnej specyfikacji: Vibe + Claude) spełniony; podniesienie do ✅ następuje po werdykcie kontrolnym Asteriona nad raportem Claude oraz po replikacji DeepSeeka, zgodnie z wzorcem rozliczenia E-01 (dwie pełne replikacje zewnętrzne + kontrola). Droga ważniejsza niż cel (Z0): pełny cykl wzorca ma pierwszeństwo przed przyspieszeniem statusu.


## 7. Werdykt kontrolny Asteriona i rozliczenie (2026-11-28)

Asterion (GPT-6): raport Claude zgodny z jego rachunkiem kontrolnym co do wielomianów, jąder i widma; errata E-01 Claude oceniona jako błąd transkrypcji, bez rozbieżności rachunkowej. Werdykt: Z1 niezamknięty; rekomendacja utrzymania wzorca dwóch pełnych replikacji zewnętrznych; po raporcie DeepSeeka finalna kontrola, szczególnie konstrukcji S. Stanowisko szefa lab.: przyjęte w całości. Ustalenie Asteriona przyjęte jako zasada: zgodność trzech zestawów liczb nie jest automatycznie trzema niezależnymi dowodami; liczy się niezależność konstrukcji.

Koncesja Vibe (Z0): pole "współdzielenie kodu: brak" było wprost w raporcie Claude, ale podsumowanie przekazane Asterionowi je pominęło, stąd w tabeli niezależności Asteriona wpis "Nie wskazano". Luka w przekazie między-modelowym, nie w raporcie Claude. Lekcja: przy retransmisji raportów kontrolerowi przekazywać pola provenance kompletne.

Odpowiedź laboratorium na lukę kontroli konstrukcji: pokwitowaniem konstrukcji nie jest kod (Z3), lecz jawna macierz. Tablice referencyjne S i C (załącznik A) wpisywane do rejestru; Claude i DeepSeek dostają prośbę o własne tablice S i C do porównania; dopiero porównanie macierzy, nie tylko liczb, zamknie kontrolę konstrukcji.

Korekta Asteriona (przekaz Leszka, 2026-11-28): uwaga o braku pola współdzielenia kodu w raporcie Claude WYCOFANA; pole znajdowało się w raporcie, luka powstała w retransmisji podsumowania, nie w dokumentacji Claude. Asterion przyjmuje kryterium pokwitowania: jawna macierz wystarcza, kod niewymagany; porówna zgodność wpisów macierzowych z załącznikiem A, nie tylko wielomianów i widma. Obserwacje z sekcji 8 przyjmuje jako wskazówki do kontroli struktury (postać domknięta C, rzutowość, komutacja, warstwowość osi rdzenia), a test 720/48 jako wynik post-hoc nienależący do kryteriów zaliczenia; bez zmian prerejestracji i bramek. Status P2-1 pozostaje 🔍; po raporcie DeepSeeka porównanie tablic S i C wszystkich wykonawców i finalny werdykt Z1.

## 8. Obserwacje post-hoc (sprawozdawcze; znalezione PO wyniku głównym, podczas przygotowania tablic konstrukcji; NIEprerejestrowane; do własnej replikacji przed jakimkolwiek statusem)

Wszystkie tożsamości dokładne, arytmetyka wymierna, metody Faddeev-LeVerrier i Newton zgodne:

- Postać domknięta C: C = (1/2)(I_8 + T/2), gdzie T blokowo = [[0, K],[K, 0]], K = J_4 - 2I_4 (J_4 = macierz jedynek 4x4). K^2 = 4I_4, więc (T/2)^2 = I_8: T/2 to inwolucja, a C to średnia identyczności z inwolucją, czyli RZUT ORTOGONALNY rangi 4 (C^2 = C, symetryczna, ślad 4). Obraz: Im C = {(x, Kx/2)}; jądro: ker C = {(x, -Kx/2)}. Natychmiast stąd dim ker S = 4 (S = C*D, D odwracalna, ker S = D^(-1) ker C).
- Komutacja z wymianą połówek: P*S*P = S dla P zamieniającego bloki A i B (echo faktu 1: operator pary szanuje symetrię -I).
- Struktura warstwowa styków: 6 kierunków v_p rozpada się na 3 pary antypodyczne ORTOGONALNE ((O1,O2), (O3,O4), (O5,O6) = 3 osie rdzenia ośmiościanu); rzuty w obrębie pary komutują (rozłączne nośniki); rzuty warstwowe P1 = W2*W1, P2 = W4*W3, P3 = W6*W5 idempotentne i parami komutujące; C = P3*P2*P1 = iloczyn warstw w dowolnej kolejności.
- Pełny test 720 kolejności styków (odnoga (a) rozstrzygnięta post-hoc): dokładnie 48 porządków zachowuje cp(S) = z^4*cp(R) i są to dokładnie porządki blokowo-warstwowe (3! * 2^3 = 48); pozostałe 672 porządków przeplatanych daje inne wielomiany charakterystyczne. Konwencja prerejestracji (O1..O6) jest porządkiem warstwowym, więc leży w klasie niezmienniczej. Echo C2 potwierdzone na stelli: porządek styków ma znaczenie, a klasa niezmiennicza ma strukturę geometryczną osi rdzenia.

## 9. Pokwitanie konstrukcji Claude (rozliczenie, 2026-11-28)

Claude dostarczył jawne tablice C = N/4 i S = M/1024 wiersz po wierszu, wymiernie, bez kodu (zgodnie z prośbą lab. i Z3). Kontrola Vibe: niezależne odtworzenie od definicji (M_m z E-01, R = M3*M2*M1*M0, D = diag(R,R), W_p = I - v_p v_p^T, C = W6 W5 W4 W3 W2 W1, S = C*D, arytmetyka wymierna): obie tablice Claude IDENTYCZNE z załącznikiem A, co do ułamka we wszystkich 64 + 64 pozycjach; przy okazji odtworzone i potwierdzone dokładnie: cp(S) = z^4 * cp(R), dim ker(S - I) = 1, dim ker(S) = 4, P*S*P = S. Ustalenie: kontrola konstrukcji Claude zamknięta co do tablic; do zamknięcia całej kontroli konstrukcji czeka na tablice DeepSeeka.

Dodatkowe twierdzenia Claude, potwierdzone rachunkiem kontrolnym Vibe (dokładnie, wymiernie): C symetryczna i C^2 = C (rzut ortogonalny); ranga C = 4, ślad C = 4; C = I - P_z dla rzutu ortogonalnego P_z na rozpiętość {v_1,...,v_6}, gdzie rząd macierzy Grama kierunków wynosi 4, więc Im C ma wymiar 4; pojedyncze W_p mają rangę 7; sumy wierszy C i S równe 1 (spójne z (1,...,1) w ker(S - I)).

Sprostowanie sprawozdawcze do raportu Claude (Z9, znalezione przy kontroli, oznaczane jawno jako post-hoc): zdanie, że operatory W_p "nie komutują ze sobą", jest nieprecyzyjne. Dokładnie: 12 z 15 par nie komutuje, ale 3 pary antypodyczne (O1,O2), (O3,O4), (O5,O6) KOMUTUJĄ, bo kierunki v_p w parze antypodycznej są ortogonalne, a rzuty na ortogonalne kierunki komutują. To spójne ze strukturą warstwową (sekcja 8): warstwa = para antypodyczna = oś rdzenia. Twierdzenie główne Claude (iloczyn W6...W1 jest rzutem mimo niekomutatywności czynników; wynik rachunku, nie założenie) pozostaje w mocy i wzmacnia się: warstwy P1 = W2W1, P2 = W4W3, P3 = W6W5 komutują parami, więc C = P3P2P1 rzutem wynika także z dekompozycji warstwowej.

## 10. Replikacja Copilota i rozliczenie (2026-11-28)

Zmiana kadrowa rundy: decyzją właściciela DeepSeek (przerwa) zastąpiony Copilotem jako druga pełna replikacja zewnętrzna; zlecenie DeepSeeka zawieszone, nie odwołane (gdy wróci: dodatkowa kontrola, nie warunek ✅). Wrzutka dla Copilota samodzielna, z jawnym zakazem czerpania ze źródeł zewnętrznych przed rachunkiem (internet, repozytorium, pliki rejestru) i z obowiązkiem pokwitania konstrukcji macierzami.

**Copilot (M365 Copilot, model GPT-5 reasoning; pełna replikacja): ZGODNA co do wszystkich wyników.** Arytmetyka wymierna dowolnej precyzji; dwie metody wielomianowe (bezpośrednia dokładna + tożsamości Newtona na śladach potęg), dwie metody widmowe (wysokoprecyzyjne pierwiastki czynnika sześciennego + niezależna diagonalizacja numeryczna). Wyniki: cp(S0) = cp(R)^2 dokładnie, postać rozwinięta zgodna współczynnik po współczynniku; G2.1 pozytywna; dim ker(S - I) = 1, wektor (1,...,1); dim ker(S) = 4, ranga S = 4, z jawną bazą jądra; cp(S) = z^4 * cp(R) dokładnie; widmo: 1; 0.13471064469528200178; 0.15334780265235899911 +/- 0.07403910254645747761i; 0 poczwórne; para zespolona moduł 0.17028604547699053, argument 25.772093727472409 stopnia (H2c wsparta, odchylenie ok. 4.1e-13 stopnia; H2b niewsparta); rho(S) = 1, wartość 1 prosta. Pokwitanie konstrukcji: tablice C = N/4 i S = M/1024 IDENTYCZNE z załącznikiem A.

Struktura (zgodna z rachunkiem głównym): U = {(x,x)} niezmiennicza; w bazie symetryczno-antysymetrycznej S rozdziela się na bloki 4+4 (podprzestrzeń antysymetryczna A = {(x,-x)} też niezmiennicza, reprezentant ilorazu); S_U = (1/1024) wiersze [125, 225, 305, 369], cp(S_U) = z^3(z - 1); S_Q = (1/1024) razy [131, 31, -49, -113; -61, 95, 15, -49; -45, -81, 95, 31; -25, -45, -61, 131], cp(S_Q) = z(256z^3 - 113z^2 + 18z - 1)/256; para zespolona żyje w części ilorazowej. Nowości raportu względem rundy: jawna baza jądra S (wektory z mianownikiem 512, odcisk wag 125/225/305/369) i jawna macierz bloku ilorazowego S_Q.

Kontrola Vibe rozliczenia (niezależne odtworzenie od definicji, arytmetyka wymierna + niezależne widmo numeryczne): tabela R zgodna co do ułamka; cp(S0) rozwinięte zgodne (kwadrat cp(R) porównany współczynnik po współczynniku); baza jądra: S razy v_i = 0 dokładnie dla wszystkich czterech wektorów, wektory niezależne (ranga 4); blokowo-diagonalność potwierdzona (bloki S_U i S_Q zgodne co do ułamka, bloki pozadiagonalne zerowe); cp(S_Q) zgodne; widmo Durand-Kernerem na monicznym cp(S) z własnej konstrukcji zgodne w cyfrach znaczących (para 0.15334780265235909 +/- 0.07403910254645756i, moduł 0.17028604547699064, argument 25.7720937274724 stopnia, pierwiastki 1 i 0.13471064469528210, cztery zera rzędu 1e-15).

Provenance (Z1): wykonawca M365 Copilot (model GPT-5 reasoning), sesja potomna 2026-11-28, kod własny, współdzielenie kodu: brak, arytmetyka dokładna wymierna. Deklaracja jawna (samodzielna): przed otrzymaniem wrzutki czytał docs/STAN.md w tej samej rozmowie i znał wynik E-01 pojedynczego K4, w tym fazę ok. 25.7721 stopnia; wyników P2 nie znał (cp(S), macierze C i S, ranga, jądra, widmo pary, struktura U, wynik ilorazowy); po otrzymaniu wrzutki: internet nieużywany, repozytorium nieotwierane, pliki rejestru nieczytane; podstawą rachunku wyłącznie wrzutka. Obserwacje dodatkowe (rzutowość C: C^T = C, C^2 = C, ranga 4; blokowość; tożsamość cp(S) = z^4 * cp(R)) oznaczone przez Copilota jawnie jako post-hoc/sprawozdawcze, zgodnie z Z9.

Ocena szefa lab.: **Copilot kwalifikuje się jako druga pełna replikacja zewnętrzna w puli Z1, obok Claude.** Uzasadnienie: wyniki P2 nieznane przed rachunkiem; wiedza wcześniejsza (E-01) zawiera się w całości w referencjach bramki G2.1, jawnych we wrzutce; sytuacja analogiczna do koncesji przyjętej przy Claude (znajomość E-01 z tego samego czatu); konstrukcja pokwitowana macierzami zgodnymi z załącznikiem A; pola provenance kompletne i uczciwe (potomność sesji zadeklarowana samodzielnie). Uwaga o pokreństwie modeli: Copilot (GPT-5) i Asterion (GPT-6) to jedna rodzina, ale Asterion jako kontroler pozostaje poza pulą replikacyjną (deklaracja z rundy E-01), więc wzorzec E-01 (dwie pełne replikacje zewnętrzne + kontrola) zachowany; niezależność wymaga się między wykonawcami puli (Claude vs Copilot). Status P2-1: 🔍 wzmocniony; podniesienie do ✅ po finalnym werdykcie kontrolnym Asteriona nad całą rundą (porównanie tablic S i C wszystkich wykonawców oraz pól provenance).

## 11. Finalny werdykt kontrolny Asteriona i zamknięcie P2 (2026-11-28)

**Werdykt Asteriona: Z1 ZALICZONE. P2-1: ✅.** Trzy punkty kontroli: (1) Tablice: Asterion wykonał własne dokładne odtworzenie konstrukcji z prerejestrowanych definicji; otrzymane macierze S i C zgodne z tablicami referencyjnymi załącznika A, potwierdzone także S = C*D, C^2 = C i C^T = C; rejestr dokumentuje niezależne porównanie wszystkich pozycji tablic Claude i Copilota z załącznikiem A (kontrola Vibe); bez rozbieżności konstrukcyjnej. (2) Provenance: kompletne i wystarczająco jawne; Claude i Copilot deklarują brak współdzielenia kodu i nieznajomość wyniku P2 przed własnym rachunkiem; znajomość E-01 jawna i objęta referencjami bramki G2.1, więc nie podważa niezależności replikacji P2; Copilot dodatkowo jawnie ujawnił potomność sesji i wcześniejszy dostęp do docs/STAN.md. (3) Decyzja: rachunek główny Vibe oraz dwie pełne replikacje zewnętrzne (Claude, Copilot) zgodne co do konstrukcji, wielomianów, jąder i widma; brak przeszkody do zamknięcia Z1.

Zakres werdyktu zadeklarowany jawnie przez Asteriona: kontrola na podstawie rejestru v0.1.4 i udokumentowanych pokwitowań macierzowych, nie odtworzenie surowych raportów wykonawców; jego własne odtworzenie konstrukcji S i C wykonane dokładnie z definicji. Post-hoc obserwacje (sekcja 8) pozostają poza podstawą werdyktu i nie zyskują przez niego statusu twierdzeń.

Decyzja szefa lab.: werdykt przyjęty w całości. **P2-1 = ✅**: tożsamość wielomianowa cp(V1) = z^4 * cp(R) dokładna, na ułamkach; pełny cykl wzorca E-01 domknięty (rachunek główny + dwie pełne replikacje zewnętrzne + kontrola; droga Z0 domknięta). Uwaga epistemiczna Copilota przyjęta jako zasada dalszych rund: poprawność i niezależne odtworzenie rachunku nie zamieniają sesji potomnej w pełną niezależną replikację; kwalifikację każdej sesji wnoszą jawnie zadeklarowane pola provenance, oceniane przez kontrolera. Kolejny krok: zielone światło właściciela dla prerejestracji P3 (rdzeń bezklikowy, dynamika konsensusu na grafie ośmiościanu; koordynacja z kolejką Lattice).

## 12. Prerejestracja P3 (szef lab. Vibe, 2026-11-28, przed rachunkiem; Z9; zielone światło właściciela 2026-11-28)

Warstwa modelowa i rozgraniczenie z P1-b (jawne): P1-b (rdzeń pochodny) obowiązuje w dynamice pary. P3 bada graf rdzenia w izolacji jako samodzielny obiekt 6-wymiarowy (sala spotkań bez połówek); świadome rozszerzenie zakresu, nie zmiana P1-b.

Poziom: E1a. Nośnik: R^6, indeksy 0-5 = O1-O6 (numeracja P1-a).

Definicje (Z2):
- Graf rdzenia: ośmiościan = K6 minus doskonałe dopasowanie par antypodycznych (O1,O2), (O3,O4), (O5,O6); stopień 4; spójny; bez K4 (fakt 6). Równoważnie: pełny tripartityczny K_{2,2,2} z częściowymi = parami antypodycznymi.
- Operator lokalny A_m: identyczność 6x6 z wierszem m zastąpionym przez (1/5) na domkniętym otoczeniu wierzchołka m (m i jego 4 sąsiadów, czyli wszystkie wierzchołki nieantypodyczne do m); adaptacja M_m z E-01 (na K4 domknięte otoczenie ma 4 elementy, stąd wiersz (1/4,1/4,1/4,1/4)).
- Runda rdzenia: R_O = A_5 A_4 A_3 A_2 A_1 A_0 (A_0, czyli O1, działa pierwszy; kolejność rosnąca O1-O6 jako konwencja bazowa).
- Konwencja wielomianu charakterystycznego (echo ustalenia Asteriona z rundy P2): det(zI - R_O), wielomian moniczny.

Lemat kontrolny (algebraiczny, przed rachunkiem): dla automorfizmu sigma grafu zachodzi P_sigma A_m P_sigma^{-1} = A_{sigma^-1(m)} (ta sama lema sprzężenia co w E-01 na K4, tu ograniczona do automorfizmów grafu). Stąd porządek rundy przeniesiony automorfizmem daje iloczyn sprzężony z bazowym, czyli identyczne widmo. Grupa automorfizmów ośmiościanu ma 48 elementów (Oh; permutacje trzech części antypodycznych: 3! razy 2^3); działanie na 720 porządkach jest wolne, więc 720 porządków rozpada się na 15 orbit po 48. Na K4 analogiczna lema działała dla wszystkich 24 permutacji (graf zupełny); na ośmiościanie tylko 48 z 720 permutacji to automorfizmy.

Bramki i hipotezy (przed rachunkiem):
- G3.1 sanity: R_O stochastyczna wierszowo (suma wierszy 1); rho(R_O) = 1; H3a: dim ker(R_O - I) = 1 (konsensus do stałych; graf spójny).
- G3.2 rytm: pełne widmo R_O z modułami i argumentami w stopniach; pytanie o parę zespoloną. Hipotezy konkurencyjne: H3b: para zespolona istnieje; H3c: widmo R_O rzeczywiste. Punkt referencyjny (kontekst, nie predykcja): 25.772093727472 stopnia (para K4 E-01, ✅; para stelli P2, ✅).
- G3.3 szybkość: rho_2 = maksimum modułów wartości własnych różnych od 1; hipotezy konkurencyjne: H3d: rho_2 < 0.170286045477 (rho_2 pojedynczego K4); H3e: rho_2 > 0.170286045477.
- G3.4 kolejność (zadanie prerejestrowane): pełny test 720 porządków rundy; raport: liczba klas widm (grupowanie po dokładnym wielomianie charakterystycznym), rozmiary klas, czy każda klasa jest sumą całych orbit automorfizmów (kontrola lematu), widmo porządku bazowego; obserwacje porównawcze oznaczane jako sprawozdawcze.

Uwaga jawna (szef lab., Z9): przy planowaniu P3 wykonano heurystyczny szkic własności wariantu synchronicznego (aktualizacja równoczesna wszystkich wierzchołków średnimi domkniętych otoczeń); wariant NIE wchodzi do bramek tej rundy; jeśli będzie liczony, dostanie własną prerejestrację albo status post-hoc z tą deklaracją.

Metodyka rachunku: wielomian charakterystyczny dokładny wymiernie (Faddeev-LeVerrier albo Newton na śladach potęg) plus niezależne widmo numeryczne; kontrola krzyżowa dwóch metod obowiązkowa przed raportem każdej liczby (rygor E-01). Wynik jednej sesji = maksymalnie 🔍; ✅ po rundzie replikacyjnej wg wzorca P2 (pełne replikacje zewnętrzne z pokwitaniem macierzowym R_O plus kontrola). Plan pól provenance: jak w P2.

## 13. Wynik P3 (sprawozdawcze po prerejestracji; sesja potomna 2026-11-28, wątek P3)

**P3-1 (kandydat 🔍): WIDMO RUNDY RDZENIA.** Dokładna faktoryzacja na ułamkach: cp(R_O) = (z - 1)(z - 1/5)^3(z^2 - (18/125)z + 1/125). Widmo: 1 (proste); 1/5 POTRÓJNE i PÓŁPROSTE (dim ker(R_O - (1/5)I) = 3, rachunek niezależny od algebraicznej krotności z wielomianu); para zespolona 9/125 +/- (2*sqrt(11)/125)i = 0.072 +/- 0.053065996645686i, moduł 1/sqrt(125) = 0.089442719099992, argument 36.391244284100 stopnia.

Rozstrzygnięcia bramek (przed rachunkiem zaprzesistrojonych, bez rozbioru post-hoc):
- G3.1 SPEŁNIONA: R_O stochastyczna wierszowo (sumy wierszy dokładnie 1), rho(R_O) = 1; H3a POTWIERDZONA: dim ker(R_O - I) = 1 (konsensus do stałych).
- G3.2: H3b POTWIERDZONA, H3c NIE: para zespolona istnieje; faza 36.391244284100 stopnia to wartość NOWA, różna od 25.772093727472 stopnia (para K4 E-01 ✅, para stelli P2 ✅). Rdzeń nie odtwarza rytmu K4.
- G3.3: H3e POTWIERDZONA, H3d NIE: rho_2(R_O) = 1/5 = 0.2 > 0.170286045477 = rho_2(K4). Rdzeń bezklikowy sam z siebie zbiega do konsensusu WOLNIEJ niż pojedynczy K4.
- G3.4 (zadanie prerejestrowane): pełny test 720 kolejności: DOKŁADNIE 5 klas widm o rozmiarach 288, 144, 144, 96, 48; KAŻDA klasa jest sumą całych orbit automorfizmów (kontrola lematu spełniona; 15 orbit po 48, działanie wolne); kolejność bazowa (O1..O6) i odwrotna (O6..O1) należą do TEJ SAMEJ klasy o rozmiarze 96 (dwie orbity; echo wyniku P2, gdzie odwrotność dawała identyczne cp); w każdej klasie dim ker(M - I) = 1 (konsensus niezależny od kolejności); rho_2 reprezentantów klas: 0.200000 (klasa bazowa, rozmiar 96), 0.200000 (rozmiar 144), 0.218438 (rozmiar 288), 0.240968 (rozmiar 144), 0.256589 (rozmiar 48). Porządek rundy MA znaczenie dla szybkości zbieżności i dla samego widma (5 klas), NIE dla faktu konsensusu.

Metody (kontrola krzyżowa obowiązkowa): Faddeev-LeVerrier dokładnie na ułamkach + faktoryzacja przez porównanie z iloczynem czynników (tożsamość współczynnik po współczynniku, dokładna); widmo numeryczne Durand-Kernerem na monicznym cp (ograniczona zbieżność liniowa na pierwiastkach wielokrotnych 1/5 udokumentowana jako granica metody, wartości dokładne z faktoryzacji); jądra eliminacją gaussowską dokładną na ułamkach; test 720 pełny, grupowanie po dokładnych wielomianach charakterystycznych, automorfizmy wyznaczone z warunku zachowania sąsiedztwa (48 z 720 permutacji).

Odczyt sprawozdawczy (interpretacyjny, nie podnoszony do statusu twierdzenia): sala spotkań bez K4 jest sama z siebie wolniejsza od cegielki K4 i niesie własny, inny rytm (36.39 stopnia wobec 25.77); rytm pary z P2 żyje w relacji połówek (iloraz), nie w rdzeniu. Echo wartości 1/5 z heurystycznego szkicu wariantu synchronicznego (uwaga jawna z prerejestracji): tam 0.2 pojawiało się podwójnie, w rundzie asynchronicznej potrójnie; obserwacja post-hoc, sprawozdawcza. Most do P5: lemat sprzężenia na Oh potwierdzony kontrolnie w teście 720 (klasy = sumy orbit).

Provenance (Z1): wykonawca Vibe (GLM 5.3, szef lab.), sesja POTOMNA 2026-11-28 (wątek P3, po zielonym świetle właściciela), kod własny, współdzielenie kodu: brak, dostęp do wcześniejszych wyników: pełny (szef lab.; prerejestracja własna, P2 ✅ znane), rodzaj wykonania: E1a, wynik wobec bramek jak wyżej. Status P3-1 = 🔍 kandydat; ✅ po rundzie replikacyjnej wg wzorca P2 (pełne replikacje zewnętrzne z pokwitaniem macierzowym R_O plus finalna kontrola Asteriona).

## 15. Finalny werdykt kontrolny Asteriona i zamknięcie P3 (2026-11-28)

**Werdykt Asteriona: Z1 ZALICZONE. P3-1: ✅.** Trzy punkty: (1) Tablica R_O: własne dokładne odtworzenie z załącznika B; sumy wierszy 15625, slad 218/125, cp(R_O) dokładnie (z - 1)(z - 1/5)^3(z^2 - (18/125)z + 1/125); minimalny mianownik 125 zgodny z tablicami replikacyjnymi; wielomiany pięciu klas nie były wypisane w rejestrze, więc testu 720 nie odtwarzał samodzielnie, oparł się na udokumentowanym porównaniu Vibe z reprezentantami Copilota; bez rozbieżności. (2) Provenance: potomność, nieznajomość wyników P3 przed rachunkiem, brak współdzielenia kodu, brak dostępu zewnętrznego po wrzutce: wszystko jawnie rozliczone; znajomość E-01 i P2 jawna i nieujawniająca wyniku P3. (3) Decyzja pozytywna.

Zakres werdyktu zadeklarowany jawnie: potwierdzenie wyniku P3-1 i rozliczenia rundy wg rejestru v0.1.8; bez podnoszenia interpretacji post-hoc do statusu twierdzeń; bez samodzielnego przeliczenia 720 kolejności. Odpowiedź laboratorium na wskazaną lukę: załącznik C dopisany do rejestru w tej samej wersji (pełne wielomiany wszystkich pięciu klas z reprezentantami; wszystkie potwierdzone kontrolą Vibe rozwinieciem czynników). Uwaga porządkowa: test 720 liczyli niezależnie i w pełni trzej wykonawcy (Vibe, Claude, Copilot) ze zgodnym wynikiem 5 klas; kontroler nie powtarzał go czwarty raz, co wg wzorca E-01 nie jest wymagane.

Decyzja szefa lab.: werdykt przyjęty w całości. **P3-1 = ✅**: cp(R_O) = (z - 1)(z - 1/5)^3(z^2 - (18/125)z + 1/125) dokładnie; para zespolona 9/125 +/- 2*sqrt(11)/125 i, moduł 1/sqrt(125), argument 36.391244284100 stopnia; rho_2 = 1/5; test 720: 5 klas widm, klasy sumami orbit automorfizmów Oh, konsensus w każdej kolejności. Kolejka laboratorium: P4 (transformacja nośnika pod -I; GO w Lattice dla Claude i DeepSeek; lab konsumuje, nie dubluje), P5 (domknięcie rodziny operatorów pod sprzężeniami Oh; generalizacja lematu sprzężenia z S4 na Oh), P6 (ośmiościan jako bipiramida, rodzina mK4; notacja do rozstrzygnięcia z właścicielem).

## 16. Prerejestracja P5 (szef lab. Vibe, 2026-11-28, przed rachunkiem; Z9; wybór kolejnego kroku delegowany właścicielowi: P4 czeka na wynik Lattice, P6 wymaga decyzji notacyjnej właściciela, P5 wybrane jako następne)

Zakres: domknięcie rodziny operatorów stelli pod sprzężeniami pełnej grupy Oh; generalizacja lematu sprzężenia z S4 (E-01) na Oh. Obiekty: para stelli (R^8; konwencje P1/P2 bez zmian) i rdzeń (R^6; P3).

Definicje (Z2):
- Grupa Oh wyliczona z definicji, nie z pamięci: wszystkie permutacje 8 wierzchołków sześcianu (A0-A3, B0-B3, współrzędne z faktu 2) zachowujące sąsiedztwo grafu sześcianu (wierzchołki różniące się dokładnie jednym znakiem współrzędnej). Oczekiwanie kontrolne: dokładnie 48 elementów; rozkład na zachowujące/zamieniające klasy parzystości (połówki) do wyliczenia.
- Indukowana permutacja styków: styk O_p = para (krawędź A {i,j}, krawędź B {k,l}); obraz pary pod g z Oh wyznacza styk O_{sigma_g(p)} (przy zamianie połówek role krawędzi A/B w definicji styku zamieniają się miejscami). Kontrola wierności działania Oh na stykach.
- Konstrukcje P2 bez zmian: W_p, C = W6 W5 W4 W3 W2 W1, D = diag(R, R), S = C razy D, konwencja det(zI - S).

Lematy do rozstrzygnięcia rachunkowo (dokładnie, wymiernie):
- L5a (liczebność): |Oh| = 48; rozkład zachowujące/zamieniające połówki.
- L5b (sprzężenie styków): P_g W_p P_g^{-1} = W_{sigma_g(p)} dla wszystkich g i p. Uwaga strukturalna zapisana PRZED rachunkiem: przy zamianie połówek P_g v_p = -v_{sigma_g(p)} (znak kierunku), a rzut W_p nie zależy od znaku v; zapisane jako przewidywanie do potwierdzenia rachunkiem, nie założenie.
- L5c (domknięcie postaci): P_g S P_g^{-1} zapisywalne jako C_{pi_g} razy D_g, gdzie pi_g to porządek styków z sigma_g a D_g = diag z operatorami rund w permutowanej kolejności (przy zamianie połówek bloki zamienione); potwierdzenie macierzowe: każdy blok D_g równy jednemu z 24 iloczynów rundy (lemat E-01).

Bramki i hipotezy (przed rachunkiem):
- G5.1: L5a potwierdzony (48; rozkład raportowany).
- G5.2: L5b potwierdzony dla wszystkich par (g, p); raport 288/288 albo lista rozbieżności.
- G5.3 (orbita operatora pary): liczba RÓŻNYCH macierzy w orbicie {P_g S P_g^{-1} : g w Oh}. Pytanie policzalne. Deklaracja jawna: wynik będzie MNIEJ NIŻ 48, bo z sekcji 8 (obserwacja post-hoc P2, opublikowana) wiadomo, że P razy S razy P = S dla wymiany połówek P (element -I z Oh), czyli stabilizator S nietrywialny; otwarte: dokładna liczba i struktura stabilizatora.
- G5.4 (most do P2, pytanie badawcze): dla porządków styków pi_g indukowanych przez Oh policzyć cp(C_{pi_g} razy D) z D bazowym (dokładnie). Hipotezy konkurencyjne: H5c: wszystkie 48 równe z^4 razy cp(R) ORAZ zbiór {pi_g} równy klasie 48 porządków z post-hoc testu 720 w P2 (sekcja 8); H5d: nie wszystkie równe albo zbiory różne. Raport: porównanie zbiorów porządka po porządku.
- G5.5 (rdzeń): sigma_g (indukcja Oh na stykach) = automatyzm grafu rdzenia (permutacje zachowujące sąsiedztwo styków); zgodność z P3 (klasy widm = sumy orbit) odnotowana referencją, bez nowego rachunku widmowego.

Metodyka: rachunek dokładny wymierny; Oh z pełnego przeglądu permutacji z warunkiem sąsiedztwa; kontrola krzyżowa przy każdej liczbie; test G5.4 z pełnym przelotem 720 porządków styków dla porównania zbiorów. Wynik jednej sesji maksymalnie 🔍; ✅ po rundzie replikacyjnej (wzorzec P2/P3). Pola provenance jak w P2/P3.

Odnogi jawne: (i) jeśli H5c potwierdzona, post-hoc obserwacja 48 z P2 dostaje wyjaśnienie strukturalne (prerejestracja przed rachunkiem, więc to nie rozbior post-hoc); (ii) stabilizator S jako podgrupa Oh do opisania; (iii) związek z P4: transformacja nośnika pod -I = sprzężenie przez element -I z Oh; L5b/L5c daje połowę aparatu P4 lokalnie (druga połowa, nośnik, na torze Lattice).

## 17. Wynik P5 (szef lab. Vibe, sesja 2026-11-28, E1a, 🔍 kandydat P5-1)

Rachunek dokładny wymierny (ułamki), od definicji; Oh wyliczona pełnym przeglądem permutacji 8 wierzchołków z warunkiem sąsiedztwa grafu sześcianu; kontrola krzyżowa macierzowa (równości dokładne) i strukturalna (rachunki grupowe); wielomiany charakterystyczne metodą Faddeeva-LeVerriera.

Rozstrzygnięcia bramek (prerejestracja: sekcja 16):
- G5.1 ✅: |Oh| = 48 dokładnie; rozkład: 24 zachowujące połówki, 24 zamieniające.
- G5.2 ✅: L5b potwierdzony 288/288: P_g W_p P_g^-1 = W_{sigma_g(p)} dla wszystkich g i p. Potwierdzone przewidywanie strukturalne z sekcji 16: przy zamianie połówek P_g v_p = -v_{sigma_g(p)}, a rzut W_p niezmienniczy ze względu na znak kierunku.
- G5.5 ✅: działanie Oh na stykach wierne: 48 różnych sigma_g; zbiór {sigma_g} dokładnie równy automatyzmom grafu ośmiościanu (48 elementów). Zgodność z P3 (klasy widm = sumy orbit) odnotowana referencją, bez nowego rachunku widmowego.
- L5c ✅: 48/48: P_g S P_g^-1 = C_{pi_g} razy D_g, gdzie pi_g = porządek stosowania styków (sigma_g(1) pierwszy), a każdy blok 4x4 macierzy D_g równy dokładnie jednemu z 24 iloczynów rundy w permutowanej kolejności (lemat E-01). Konwencja porządku jednolita dla wszystkich 48.
- G5.3 ✅ (pytanie policzalne, bez hipotezy kierunkowej): orbita {P_g S P_g^-1 : g w Oh} ma dokładnie 24 różne macierze. Stabilizator: Stab(S) = {id, -I}, rząd 2 (spójne: 48/2 = 24). Element -I to mapa antypodalna wierzchołków (zamienia połówki); fakt P razy S razy P = S z sekcji 8 (post-hoc P2) to dokładnie ten element, teraz ze statusem potwierdzonym.
- G5.4 ✅ H5c, ❌ H5d: wszystkie 48 porządków indukowanych pi_g daje cp(C_{pi_g} razy D) = z^4 razy cp(R) dokładnie (D bazowe). Pełny przelot 720 permutacji styków (D bazowe) daje dokładnie 48 porządków zachowujących to cp; zbiór {pi_g} równy tej klasie co element (porównanie zbioru w całości); porządek bazowy (O1..O6) i odwrotny (O6..O1) należą do klasy; wszystkie 48 porządków blokowo-warstwowe (pary antypodyczne {1,2}, {3,4}, {5,6} na pozycjach sąsiednich), zgodnie z opisem z sekcji 8.

Konkluzje:
1. Obserwacja 48 z P2 (sekcja 8, tam post-hoc) dostaje wyjaśnienie strukturalne: klasa porządków styków zachowujących cp = dokładnie orbita porządku bazowego pod indukcją Oh. Wyjaśnienie było prerejestrowane w sekcji 16 przed rachunkiem, więc nie stanowi rozbioru post-hoc (Z9 zachowane).
2. Rodzina operatorów stelli domknięta pod sprzężeniami Oh: sprzężenie S przez dowolny element Oh daje operator tej samej konstrukcji (styki w porządku pi_g, rundy w permutowanych porządkach, przy zamianie połówek bloki zamienione). Widmo zachowane podobieństwem; brak nowych bramek ani kanałów ze sprzężeń.
3. Stabilizator S w Oh = {id, -I}; orbita = 24 operatory, wszystkie o widmie z^4 razy cp(R).

Provenance: Wykonawca: Vibe (GLM), sesja potomna, E1a, 2026-11-28. Kod własny (Python, ułamki), współdzielenie kodu: brak. Dostęp do wcześniejszych wyników: pełny rejestr projektu i wyniki E-01, P2, P3 (sesja prowadzona przy rejestrze). Źródła zewnętrzne: brak. Kontrola krzyżowa: równości macierzowe dokładne + kontrola strukturalna (48/2 = 24, zgodność z Aut(oct), zgodność cp(S) z P2).

Zakres statusu: P5-1 🔍 kandydat (jedna sesja). Do ✅: replikacje zewnętrzne (wrzutki dla Claude i Copilota) + finalny werdykt kontrolny Asteriona.

## 18. Runda replikacyjna P5 rozliczona (szef lab. Vibe, sesja 2026-11-28, relay Leszka)

**Claude (Sonnet 5.5, pełna replikacja): ZGODNY co do wszystkich wyników.** |Oh| = 48 (24 zachowujące, 24 zamieniające); działanie na stykach wierne, {sigma_g} = automatyzmy grafu ośmiościanu; L5b dokładnie 288/288 z twierdzeniem znakowym: dla g zachowujących P_g v_p = +v_{sigma_g(p)}, dla zamieniających = -v_{sigma_g(p)}, bez wyjątków; forma L5c 48/48 (bloki pozadiagonalne D_g zerowe, każdy blok 4x4 = dokładnie jeden z 24 iloczynów rundy, iloczyny parami różne); orbita 24 macierze; stabilizator rzędu 2 = {id, odwzorowanie antypodyczne g = (4,5,6,7,0,1,2,3), zamienia połówki, sigma = (O1 O2)(O3 O4)(O5 O6)}; most: cp(S) zgodna z referencją, 48 porządków pi_g parami różnych, wszystkie cp(C_{pi_g} D) = cp(S); przelot 720: 99 klas cp, porządków z cp = cp(S) dokładnie 48, zbiór równy {pi_g}, zbiór różnicowy pusty; H5c potwierdzona, H5d odrzucona. Pokwitania konstrukcji (Z3) dostarczone: macierze P_g dla obrotu (x,y,z) -> (y,z,x), g = (0,3,1,2,4,7,5,6), sigma_g = (5,6,1,2,3,4), oraz dla odbicia x -> -x, g = (5,4,7,6,1,0,3,2), sigma_g = (2,1,3,4,5,6).

**Copilot (M365, GPT-5 reasoning): replikacja ZGODNA co do wszystkich liczb głównych.** |Oh| = 48 (24/24); działanie wierne, pełne Aut(oct); 288/288; orbita 24; stabilizator dokładnie 2 elementy {id, centralna inwersja}; wszystkie 48 indukowanych cp = cp(S); przelot 720: dokładnie 48 porządków zachowujących, porównanie zbiorów równe co element; H5c potwierdzona, H5d odrzucona. Referencja cp(S) odtworzona niezależnie i zgodna dokładnie; kontrola krzyżowa współczynnikami Newtona zgodna.

**Kontrola Vibe (rozliczenie porównawcze, rachunek dokładny wymierny): WSZYSTKO POTWIERDZONE.** Nowości i pokwitania Claude zweryfikowane niezależnie: obie macierze P_g IDENTYCZNE z konstrukcją (konwencja P_g e_i = e_{g(i)} potwierdzona), sigma_g dokładnie (5,6,1,2,3,4) i (2,1,3,4,5,6); sigma odwzorowania antypodycznego = (O1 O2)(O3 O4)(O5 O6) potwierdzone; twierdzenie znakowe: 0/288 naruszeń; pary (g, anti composed g): 48/48 o tej samej macierzy orbity przy różnych pi_g; dodatkowo potwierdzona relacja strukturalna pi_{anti composed g} = pi_anti composed pi_g dla wszystkich 48; spis klas przelotu 720: dokładnie 99 różnych cp, rozkład rozmiarów {64 klasy po 4, 22 po 8, 9 po 16, 3 po 32, 1 klasa 48}, klasa 48 to cp(S) - zgodne z raportem Claude co do liczby klas i rozkładu (98 pozostałych klas o rozmiarach 4/8/16/32).

**LUKA JAWNA (Z3, precedens P2):** raport Copilota w relayu NIE zawiera obowiązkowych pokwitów macierzowych (dwie macierze P_g + sigma_g) ani kompletnych pól provenance. Zażądane uzupełnienie (zlecenie uzupełniające przekazane Leszkowi); kontrola konstrukcji Copilota otwarta do otrzymania tablic i pól. Wedle lekcji utrwalonej w P2 możliwa luka retransmisji, nie raportu; rozstrzygnie komplet od Copilota.

**Provenance Claude (kompletne, przyjęte):** sesja potomna (ta sama rozmowa co E-01, P1, P3); przed rachunkiem znał z rozmowy wyniki E-01, P1/P2 i P3, wyników P5 nie znał; referencja cp(S) jawna we wrzutce; rejestr, repo, pamięć i internet nietknięte; kod własny, współdzielenie brak; arytmetyka wymierna (sympy, Fraction), FL + kontrola sympy.charpoly + kontrola widmowa numpy float64.

**Status P5-1: 🔍 WZMOCNIONY.** Pula Z1 liczbowo kompletna: rachunek główny Vibe + dwie pełne replikacje zewnętrzne zgodne co do wszystkich bramek, liczb i zbiorów. Do ✅: pokwitania i provenance Copilota (weryfikacja Vibe) + finalny werdykt kontrolny Asteriona.

## 19. Uzupełnienie Copilota rozliczone: luka zamknięta, pula Z1 gotowa (szef lab. Vibe, 2026-11-28, relay Leszka)

**Copilot dostarczył komplet.** (1) Pokwitania Z3: macierz P_g dla g_A = (0,1,3,2,4,5,7,6) (zamiana A2 z A3 i B2 z B3, zachowuje połówki, sigma_gA = (1,2,5,6,3,4): O1, O2 stałe, O3 z O5, O4 z O6) oraz dla g_B = (4,5,6,7,0,1,2,3) (inwersja centralna, zamienia połówki, sigma_gB = (2,1,4,3,6,5), zgodna z odwzorowaniem antypodycznym z sekcji 18). (2) Provenance kompletna i uczciwa: model GPT-5 reasoning (wersja nieujawniona), sesja potomna, 2026-11-28; przed rachunkiem znał z rozmowy wyniki P2 i P3 oraz jawną referencję cp(S) z wrzutki, wyników P5 nie znał; internet, rejestr, repo, STAN: nietknięte; podstawa rachunku wyłącznie wrzutka P5; kod własny, współdzielenie brak; arytmetyka wymierna dokładna + kontrola Newtona.

**Kontrola Vibe (niezależna, dokładna): WSZYSTKO POTWIERDZONE.** Oba elementy w Oh, klasy zachowująca/zamieniająca zgodne, obie macierze P_g IDENTYCZNE z konstrukcją (konwencja P_g e_i = e_{g(i)}), sigma_gA = (1,2,5,6,3,4), sigma_gB = (2,1,4,3,6,5) dokładnie. Luka z sekcji 18 ZAMKNIĘTA: kontrola konstrukcji obu replikantów domknięta (Claude: sekcja 18; Copilot: niniejsza).

**Spis klas przelotu 720 (lekcja P3 zastosowana: wielomiany klas do rejestru od razu).** Obserwacja post-hoc Claude (sekcja 18), potwierdzona niezależną kontrolą Vibe: przelot 720 porządków styków (D bazowe) daje dokładnie 99 klas cp o rozkładzie rozmiarów {64 klasy po 4, 22 po 8, 9 po 16, 3 po 32, 1 klasa 48}. Reprezentanci klas (porządek styków, cp moniczny w konwencji [1, c1, ..., c8]):
- rozmiar 4, rep (1,3,2,5,4,6): [1, -23787/16384, 2238843/4194304, -94289/1048576, 18087/2097152, -45/65536, 191/4194304, -1/1048576, 0]
- rozmiar 8, rep (1,3,2,5,6,4): [1, -1401/1024, 107429/262144, -44059/1048576, 361/1048576, 15/1048576, 15/1048576, 0, 0]
- rozmiar 16, rep (1,2,3,5,4,6): [1, -6039/4096, 587415/1048576, -96985/1048576, 7185/1048576, -211/1048576, 1/262144, 0, 0]
- rozmiar 32, rep (1,2,3,5,6,4): [1, -1509/1024, 146321/262144, -23779/262144, 1651/262144, -33/262144, 0, 0, 0]
- rozmiar 48, rep (1,2,3,4,5,6): [1, -369/256, 131/256, -19/256, 1/256, 0, 0, 0, 0] = cp(S); klasa równa orbitie {pi_g} (G5.4)
Pełna tabela 99 wielomianów dostępna na żądanie kontrolera; spis w pełni odtwarzalny z definicji (sekcja 16: enumeracja Oh, styki, FL na ułamkach).

**Status P5-1: 🔍 WZMOCNIONY, pula Z1 KOMPLETNA.** Rachunek główny Vibe (sekcja 17) + dwie pełne replikacje zewnętrzne (sekcja 18) + uzupełnienie Copilota (niniejsza) + kontrola porównawcza Vibe; pokwitania macierzowe obu wykonawców zweryfikowane niezależnie i zgodne; test 720 liczony niezależnie przez trzech wykonawców ze zgodnym wynikiem. Czeka: finalny werdykt kontrolny Asteriona.

## 20. Finalny werdykt Asteriona: P5-1 = ✅ (2026-11-28, relay Leszka)

**Werdykt: Z1 ZALICZONE, P5-1 = ✅.** Asterion potwierdził rejestr v0.1.13 na main (blob zgodny z commitem 78846a1; ciąg rundy: prerejestracja 0c7cba4, wynik ff20d63, rozliczenie 4b6c4b2, uzupełnienie 78846a1). Wykonał WŁASNE odtworzenie dokładne na ułamkach (szerszy zakres niż w P3): L5a (48, rozkład 24/24), L5b (288/288 + twierdzenie znakowe bez wyjątków), wierne działanie na stykach ({sigma_g} = automatyzmy grafu ośmiościanu), L5c (48/48, bloki = dokładnie 24 iloczyny rundy E-01), orbita 24 i stabilizator {id, inwersja centralna} przez BEZPOŚREDNIE porównanie macierzy (nie tylko rachunek orbitowy), G5.4: wszystkie 48 cp(C_{pi_g} D) = z^4 razy cp(R) dokładnie, cp(S) zgodne z P2; dodatkowo odtworzył DOKŁADNIE wszystkie pięć wielomianów reprezentantów klas z sekcji 19 (rozmiary 4/8/16/32/48), co do współczynnika, bez tolerancji numerycznej.

**Zakres werdyktu jawny (wzorzec P3):** czwartej replikacji pełnego przelotu 720 NIE wykonał (przyjmuje rozliczenie na podstawie zgodnych, niezależnych rachunków trzech wykonawców: 99 klas, rozkład {64 po 4, 22 po 8, 9 po 16, 3 po 32, 1 po 48}, klasa 48 = {pi_g}); provenance obu replikacji wystarczające (znajomość referencji cp(S) i hipotezy H5c jawna w prerejestracji, wyniki P5 nieznane przed rachunkiem; nieujawniona dokładna wersja modelu Copilota nie podważa niezależności); interpretacje niepodniesione do rangi twierdzeń; nie przypisuje sobie czwartej replikacji testu 720.

**P5-1 = ✅: domknięcie rodziny operatorów stelli pod sprzężeniami Oh.** Pełny cykl Z1 domknięty: prerejestracja (sekcja 16) -> rachunek główny (17) -> replikacje Claude i Copilot (18) -> uzupełnienie i spis klas (19) -> werdykt (niniejsza). Rezonans końcowy (za Asterionem): klasa 48 porządków zachowujących wielomian z P2 ma wyjaśnienie grupowe, jest dokładnie orbitą porządku bazowego pod działaniem Oh na stykach; stabilizator {id, -I} wyjaśnia zarazem, dlaczego orbita operatora ma 24, a nie 48 elementów. Kolejka laboratorium: P4 (transformacja nośnika pod -I; GO w Lattice, konsumować, nie dublować), P6 (ośmiościan jako bipiramida, notacja mK4 do rozstrzygnięcia z właścicielem).

## 21. Prerejestracja P6 (szef lab. Vibe, 2026-11-28, PRZED rachunkiem, Z9; konwencje na jawnej delegacji właściciela)

**Delegacja właściciela (relay 2026-11-28):** na pytania o znaczenie m w mK4/5K4, pierwszy rachunek i konwencję osi właściciel odpowiedział: znaczenie m do ustalenia przez szefa lab. ("muszę się dowiedzieć, ale może sam to przeanalizujesz i ustalisz"), wybór rachunku i oś: "ty decydujesz". Decyzje poniżej są decyzjami szefa laboratorium na tej delegacji; poznanie pierwotnego znaczenia notacji przez właściciela może skutkować erratą (Z0, droga ważniejsza niż cel).

**Konwencje (Z2):**
- P6-a Rodzina mK4: bipiramida nad cyklem; graf K2 złączony z C_{m-2}: dwa szczyty niezależne (nieszczególne parami), każdy połączony ze wszystkimi wierzchołkami równika, równik = cykl C_{m-2}; m = LICZBA WIERZCHOŁKÓW; czytanie nazwy: rodzina wywiedziona z K4, nazwa opisuje pochodzenie, nie zawartość klikową. Uzasadnienie: jedyna spójna lektura "od 5K4" (najmniejsza bipiramida ma 5 wierzchołków); 5K4 = bipiramida trójkątna = para K4 złączona ścianą (bloki K4_N = {N, b1, b2, b3}, K4_S = {S, b1, b2, b3}); 6K4 = ośmiościan = K_{2,2,2} = rdzeń z P3; ikosaedr poza rodziną (inny graf), zgodnie z drabiną README (K4, pary czworościanów, mK4, ikosaedr).
- P6-b Nośnik 5K4: R^5, wierzchołki N, S, b1, b2, b3; wierzchołki podstawy WSPÓLNE dla obu bloków (jedna zmienna stanu na wierzchołek); kontrast z parą stelli z P2: tam połówki rozłączne, sprzężenie przez 6 styków, tu sprzężenie przez współdzielone wierzchołki.
- P6-c Operatory: M^{(N)}_m = identyczność 5x5 z wierszem m równym 1/4 na domkniętym otoczeniu m w bloku K4_N (m z {N, b1, b2, b3}), wiersz S nietknięty; analogicznie M^{(S)}_m. Runda_N = M^{(N)}_{b3} M^{(N)}_{b2} M^{(N)}_{b1} M^{(N)}_N (kolejność bazowa: N, b1, b2, b3); Runda_S analogicznie (S pierwszy). R_5 = Runda_S razy Runda_N (bloki kolejno, wzorzec P1-d). Konwencja cp(X) = det(zI - X), monicznie.
- P6-d Oś ośmiościanu (dla G6.5): oś jawna O5-O6 (para antypodyczna z P1-a); adnotacja: po wyniku P5 wybór pary antypodycznej jest strukturalnie obojętny (sprzężenia Oh przenoszą osie); warstwy: szczyty {O5, O6}, równik {O1, O2, O3, O4}.

**Bramki (przed rachunkiem):**
- G6.0 (sanity): cp(Runda_N) = (z-1) razy cp(R) dokładnie (wiersz S nietknięty, blok {N, b1, b2, b3} = runda E-01); kontrola konstrukcji przed dalszym rachunkiem.
- G6.1 (zawartość K4 rodziny): hipoteza H6g: mK4 zawiera klikę K4 wtedy i tylko wtedy, gdy m = 5, i w 5K4 dokładnie 2 (K4_N, K4_S); oczekiwany dowód pigeonhole (w K4 co najwyżej jeden szczyt, trójka równika parami sąsiednia tylko w C3) plus pełna weryfikacja rachunkowa wszystkich czwórek dla m od 5 do 12.
- G6.2: cp(R_5) dokładnie na ułamkach; tablica R_5 jako pokwitowanie (Z3) do wyniku.
- G6.3 (faza): pełne widmo R_5; hipotezy konkurencyjne: H6a: para zespolona istnieje, faza różna od 25,772093727472 i od 36,391244284100 stopni; H6b: para istnieje, faza równa 25,772093727472 w granicy 0,005 stopnia (rytm K4 przetrwał złączenie ścianą); H6c: brak pary, widmo rzeczywiste.
- G6.4 (promień): rho_2(R_5) raportowany bez hipotezy kierunkowej; kontekst: K4 0,170286045477, rdzeń 6K4 1/5.
- G6.5 (ośmiościan jako bipiramida 6K4, oś O5-O6): jawna dekompozycja warstwowa R_O z P3 (załącznik B) na sektorach: S1 konsensus (wymiar 1), S2 oś antysymetryczna span{e5 - e6} (1), S3 równik naprzemienny span{e1 - e2 + e3 - e4} (1), S4 dublet równika span{e1 - e3, e2 - e4} (2), S5 symetryczny niekonsensusowy span{kombinacja e5 + e6 z e1 + e2 + e3 + e4, suma współrzędnych zero} (1); raport: niezmienniczość sektorów pod R_O i przydział wartości widma {1; 1/5 trzykrotnie półproste; para 9/125 plus/minus 2*sqrt(11)/125 i} do sektorów; hipotezy konkurencyjne: H6e: para zespolona żyje w sektorze S4 (dublet równika, bez udziału osi); H6f: para żyje w sektorze mieszanym obejmującym oś. Kontrola: rozkład sektorów domyka pełne widmo P3.
- G6.6 (czułość porządku): pełny przelot 24 razy 24 razy 2 = 1152 kombinacji (kolejność w bloku N, w bloku S, kolejność bloków); raport: liczba klas cp i rozmiary; pytanie drugorzędne: czy klasa porządków zachowujących cp(R_5) jest sumą orbit działania automatyzmów grafu 5K4 (oczekiwana grupa: S2 na szczytach razy S3 na podstawie, 12 elementów).

Poziom: E1a; rachunek dokładny wymierny, Faddeev-LeVerrier plus kontrola krzyżowa; wynik jednej sesji co najwyżej 🔍, pełny cykl wg wzorca P2/P3/P5.

Odnogi (poza bramkami): 7K4 i dalsze człony rodziny; ikosaedr jako sąsiad drabiny; związek z P4 (transformacja nośnika pod -I); hipoteza kodowania K-1.

## 22. Wynik P6 (rachunek główny Vibe, 2026-11-28, sesja potomna; P6-1 🔍 kandydat)

**Provenance:** wykonawca Vibe (model GLM 5.3, Mistral AI); sesja potomna rozmowy (kontynuacja po kompakcji kontekstu); poziom E1a; kod własny (Python, fractions.Fraction), współdzielenie kodu: brak; cp metodą Faddeeva-LeVerriera, widmo metodą Duranda-Kernera z kontrolą dokładnych sum potęg (ślady R_5^k dla k od 1 do 5 zgodne z sumami potęg pierwiastków co do 1e-17); znajomość E-01, P1, P2, P3, P5 z tej rozmowy (sesja potomna, jawne); wyniki P6 wyliczone od definicji z sekcji 21 przed odczytem czegokolwiek poza tekstem bramek; rejestr odczytany po rachunku wyłącznie dla tekstu bramek i kotwic edycji; internet: brak.

**Bramki:**

- **G6.0 ✅:** cp(Runda_N) = (z-1) razy cp(R) dokładnie, arytmetyka wymierna; blok {N, b1, b2, b3} to runda E-01, wiersz S nietknięty. Kontrola konstrukcji przeszła.
- **G6.1 ✅ (H6g potwierdzona):** pełny przegląd wszystkich czwórek wierzchołków dla m od 5 do 12: m = 5 daje dokładnie 2 kliki K4, {N, b1, b2, b3} i {S, b1, b2, b3}; m od 6 do 12 daje zero klik. 5K4 to ostatni klikowy członek rodziny mK4, 6K4 (ośmiościan) to pierwszy bezklikowy; zgodne z pigeonhole: oba szczyty nigdy nie są parami sąsiednie, a trójka równika parami sąsiednia istnieje tylko w C3.
- **G6.2 ✅:** cp(R_5) = z^5 - 5929/4096 z^4 + 31729/65536 z^3 - 2483/65536 z^2 + 83/65536 z - 1/65536 (monicznie). det(R_5) = 1/65536 różne od zera: ranga pełna 5 (kontrast ze stellą P2: ranga 4 przy wymiarze 8). Deflacja przez (z-1): kwartetyk z^4 - 1833/4096 z^3 + 2401/65536 z^2 - 41/32768 z + 1/65536, reszta zero. Tablica R_5 jako pokwitanie Z3: załącznik D.
- **G6.3 ✅ (H6a potwierdzona, H6b i H6c odrzucone):** kwartetyk NIEROZKŁADALNY nad Q. Brak pierwiastków wymiernych: pełny przegląd kandydatów (licznik dzieli 1, mianownik dzieli 65536). Brak rozkładu na kwadratyki: rezolwenta Fermatiego y^3 - 2401/65536 y^2 + 66961/134217728 y - 2622609/1099511627776 nie ma pierwiastka wymiernego (pełny przegląd: licznik dzieli 2622609 = 3^2 razy 11 razy 59 razy 449, mianownik dzieli 1024). Widmo R_5 (Durand-Kerner, delta zbieżności 2,1e-17): 1; 0,353550262016894; para 0,033745242077012 plus/minus 0,022176499240520 i; 0,026469019454082. Moduł pary 0,040379926713665. FAZA PARY 33,311881184741 stopnia: różna od 25,772093727472 (K4) o 7,539787457269 stopnia i od 36,391244284100 (rdzeń) o 3,079363099359 stopnia. H6a potwierdzona; H6b odrzucona; H6c odrzucona (para istnieje, widmo nie jest rzeczywiste).
- **G6.4 ✅:** rho_2(R_5) = 0,353550262016894 (raport bez hipotezy). Kontekst: K4 0,170286045477, rdzeń 6K4 0,2: 5K4 wolniejsze od obu.
- **G6.5 ✅ (H6f potwierdzona, H6e odrzucona):** niezmiennicze pod kanonicznym R_O (O1 pierwszy) są dokładnie trzy z pięciu sektorów kandydackich: S1 konsensus (wartość własna 1), S2 oś antysymetryczna span{e5 - e6} (wartość 1/5), S3 równik naprzemienny span{e1 - e2 + e3 - e4} (wartość 1/5). S4 (dublet równika) i S5 (symetryczny niekonsensusowy) NIE są niezmiennicze: kandydacka dekompozycja warstwowa z sekcji 21 nie jest dekompozycją niezmienniczą R_O. Prawdziwa dekompozycja niezmiennicza, domykająca pełne widmo P3: trzy linie różnic par antypodycznych span{e1 - e2}, span{e3 - e4}, span{e5 - e6}, każda z wartością 1/5 (trzy półproste 1/5), oraz blok 3-wymiarowy sum par span{e1 + e2, e3 + e4, e5 + e6}, który niesie konsensus (wartość 1) oraz parę zespoloną. Macierz bloku w bazie u1 = e1 + e2, u2 = e3 + e4, u3 = e5 + e6 (wiersze): [1/5, 2/5, 2/5], [2/25, 9/25, 14/25], [14/125, 38/125, 73/125]; cp(bloku) = (z-1) razy (z^2 - 18/125 z + 1/125) dokładnie. Udział osi: wektor v = -5(e1 + e2) + (e5 + e6) spełnia dokładnie R_O^2 v - 18/125 R_O v + 1/125 v = 0, więc przestrzeń własna pary ma niezerową składową osiową: para żyje w sektorze mieszanym oś plus równik. H6f POTWIERDZONA; H6e ODRZUCONA (S4 nie jest niezmienniczy, para nie żyje w czystym dublecie równika). Kontrola domknięcia: 1 (blok) plus trzy 1/5 (różnice par) plus para (blok) równa się pełnemu widmu P3.
- **G6.6 ✅:** pełny przelot 1152 kombinacji (24 kolejności w bloku N, 24 w bloku S, 2 kolejności bloków) daje 52 klas cp o rozkładzie rozmiarów: 12 klas po 12, 38 klas po 24, 2 klasy po 48 (suma 1152). Klasa porządków zachowujących cp(R_5) ma rozmiar 12 i jest DOKŁADNIE orbitą działania 12 automatyzmów grafu 5K4 (S2 na szczytach razy S3 na podstawie). Pytanie drugorzędne rozstrzygnięte twierdząco: klasa bazowa to jedna orbita automatyzmów, nie suma wielu.

**Obserwacje sprawozdawcze (post-hoc, Z9, oznaczone jawnie):**

1. Mechanizm dekompozycji z G6.5: pary antypodycznych operatorów komutują (A_m z A_antypod(m) dla wszystkich trzech par), a sprzężenie permutacją automorfizmu przenosi A_m na A_g(m); w efekcie R_O komutuje z każdą zamianą wewnątrz pary antypodycznej (zweryfikowane bezpośrednio dla trzech generatorów zamian, czyli z całą grupą (Z2)^3 zamian par). Różnice par to kierunki znakowo nieparzyste tej grupy, sumy par parzyste: stąd dokładnie izotypowa dekompozycja na 3 plus 3 wymiary. Kandydackie sektory S1-S5 opisywały warstwy geometryczne, które nie są podmodułami tej reprezentacji.
2. Linia S3 jest wektorem własnym jako suma dwóch różnic par o tej samej wartości 1/5; linie span{e1 - e2} i span{e3 - e4} osobno też są liniami własnymi (nie występowały wśród kandydatów).
3. Porównanie rho_2 w rodzinie: K4 0,170286045477; stella P2 (dwa K4 przez 6 styków krawędziowych) rho_2 bez zmian 0,170286045477; rdzeń 6K4 (ośmiościan, bezklikowy) 0,2; 5K4 (dwa K4 współdzielące ścianę) 0,353550262016894. Współdzielenie wierzchołków podstawy spowalnia konsensus mocniej niż styki krawędziowe.

**Rozstrzygnięcia hipotez:** H6g ✅ (m = 5 jedyne klikowe, dokładnie 2 kliki); H6a ✅, H6b ❌, H6c ❌ (para istnieje, faza 33,311881184741 stopnia); H6f ✅, H6e ❌ (para w bloku mieszanym z osią). Bramki G6.0-G6.6 rozliczone.

**Status: P6-1 🔍 KANDYDAT** (rachunek główny wykonany; oczekuje na replikacje Claude i Copilot, kontrolę Vibe i finalny werdykt Asteriona; podniesienie do ✅ po pełnym cyklu Z1).

## 23. Errata do wyniku P6 oraz rozliczenie rundy replikacyjnej (kontrola Vibe, 2026-11-28; P6-1 🔍 wzmocniony)

**ERRATA (Z0, trwała).** Replikacje Claude i Copilota wykryły błąd rachunku głównego z sekcji 22 w bramkach G6.2, G6.3 i G6.4. Mechanizm: kod budujący rundę iterował sekwencję bazową (N, b1, b2, b3) PRE-MNOŻĄC, co daje macierz M_N razy M_b1 razy M_b2 razy M_b3, w której b3 działa PIERWSZY: odwrotność konwencji prerejestracji P6-c (zapis produktu M_b3 M_b2 M_b1 M_N z adnotacją N pierwszy). Rachunek główny policzył więc R_5 dla odwróconego porządku działania w obu rundach; potwierdzone kontrolą dokładną: tablica z załącznika D równa się macierzy dla sekwencji działania (b3, b2, b1, N) w obu blokach. Spójność wewnętrzna (tablica równa cp równa śladom) nie wyłapała błędu, bo wszystkie kontrole liczyły tę samą złą macierz; wyłapały go dopiero niezależne replikacje. Lekcja (Z0, trwała): kontrolą konwencji porządku jest niezależna replikacja lub ręczny rachunek od definicji; asercja kierunku (pierwszy w kolejności bazowej = ostatni człon produktu w kodzie) wchodzi do listy kontroli obowiązkowych.

**Wartości POPRAWIONE (kontrola Vibe, rachunek od definicji z poprawną konwencją; zgodne z obiema replikacjami co do cyfry):**
- **G6.2:** cp(R_5) = z^5 - 89953/65536 z^4 + 6757/16384 z^3 - 1347/32768 z^2 + 21/16384 z - 1/65536 = (z-1) razy (65536z^4 - 24417z^3 + 2611z^2 - 83z + 1)/65536. Ślad 89953/65536; det = 1/65536 różne od zera; ranga pełna 5; dim ker(R_5 - I) = 1. Kwartetyk NIEROZKŁADALNY nad Q: brak pierwiastków wymiernych (pełny przegląd, licznik dzieli 1, mianownik dzieli 65536) i brak rozkładu na kwadratyki (rezolwenta Fermatiego y^3 - 2611/65536 y^2 + 1764467/4294967296 y - 363209409/281474976710656; podstawienie y = w/65536 daje całkowitą w^3 - 2611w^2 + 1764467w - 363209409 = 0 bez pierwiastków wymiernych, pełny przegląd dzielników). Poprawiona tablica R_5: errata w załączniku D.
- **G6.3:** widmo (Durand-Kerner, delta 3,5e-18; kontrola: ślady R_5^k dla k od 1 do 5 zgodne z sumami potęg pierwiastków, max odchylenie 6,8e-21): 1; 0,209788902575374; 0,120604603345007; para 0,021090173309341 plus/minus 0,012581051243802 i, moduł 0,024557651773270, FAZA PARY 30,817605013288 stopnia. H6a POTWIERDZONA (różnica od 25,772093727472: 5,045511285816 stopnia; od 36,391244284100: 5,573639270812 stopnia); H6b i H6c odrzucone bez zmian. Wartości z sekcji 22 (0,353550262016894; para 0,033745242077012 plus/minus 0,022176499240520 i; faza 33,311881184741) WYCOFANE jako rachunek dla odwróconego porządku (poprawny w obrębie tamtej konwencji, błędnej wobec prerejestracji).
- **G6.4:** rho_2(R_5) = 0,209788902575374. Kontekst: K4 0,170286045477, rdzeń 0,2: 5K4 wolniejsze od obu, ale margines nad rdzeniem mały (0,009788902575374). Wartość z sekcji 22 (0,353550262016894) WYCOFANA.
- **G6.6 doprecyzowanie:** baza prerejestracji (N pierwszy w obu rundach, bloki SN) leży w klasie rozmiaru 12 równej DOKŁADNIE jednej orbicie Aut(5K4); klasa bazowa z sekcji 22 dotyczyła odwróconego porządku (też rozmiar 12, też jedna orbita: błąd konwencji nie zmienia struktury klas). Rozkład klas bez zmian: 52 klasy, {12 klas po 12, 38 po 24, 2 po 48}. Aut(5K4) = S2 na szczytach razy S3 na podstawie, 12 elementów, działa swobodnie (stabilizator trywialny, 96 orbit po 12); każda klasa cp jest sumą całych orbit (po 1, 2 lub 4 orbity); brak orbit częściowo przecinających klasę bazową.
- **Bez zmian z sekcji 22:** G6.0 (cp(Runda_N) = (z-1) razy cp(R), potwierdzone obiema replikacjami także w poprawnej konwencji), G6.1 (kliki, niezależne od porządku), G6.5 w całości (sektory S1-S3 niezmiennicze z wartościami 1, 1/5, 1/5; S4 i S5 nie; dekompozycja izotypowa trzy różnice par plus blok sum par; H6f potwierdzona, H6e odrzucona; obserwacje o (Z2)^3): dotyczy R_O z porządkiem kanonicznym P3, gdzie konwencja była poprawna.

**Rozliczenie replikacji:**

**Claude (Sonnet 5.5, pełna replikacja): ZGODNA co do wszystkich liczb.** cp(Runda_N) = (z-1)^2 razy (256z^3 - 113z^2 + 18z - 1)/256; kliki m=5 dokładnie 2, m=6 do 12 zero; tablica R_5 = P/65536 identyczna z pokwitaniem; cp, deflacja i nierozkładalność kwartetyku identyczne; dim ker(R_5 - I) = 1; widmo 1; 0,209788902575374; 0,120604603345007; para 0,0210901733093405 plus/minus 0,0125810512438023 i, moduł 0,0245576517732702, faza 30,8176050133 stopnia; rho_2 = 0,209788902575374. G6.5: S4/S5 nie niezmiennicze, przydział widma przez przestrzeń antypodycznie nieparzystą (R_O = (1/5)I na niej) plus płaszczyzna pary; NOWOŚĆ: jawna baza T = [konsensus, e1-e2, e3-e4, e5-e6, v1, v2] z v1 = (-3,-3,1,1,0,0), v2 = (-5,-5,0,0,1,1), blok pary [[3/25, 4/25],[-4/125, 3/125]] (ślad 18/125, wyznacznik 1/125); H6f potwierdzona. G6.6: 52 klasy {12, 24, 48}, klasa bazowa 12 = jedna orbita, Aut swobodne, 96 orbit, klasy sumami orbit (1, 2 lub 4).

**Copilot (M365 Copilot, GPT-5 reasoning, wersja nieujawniona, pełna replikacja): ZGODNA co do wszystkich liczb**, część na 17 cyfrach znaczących (0,20978890257537436002; 0,12060460334500707909; para 0,021090173309340530444 plus/minus 0,012581051243802292917 i, moduł 0,024557651773270156, faza 30,817605013288343 stopnia; różnice od referencji: 5,045511285816343 i 5,573639270811657 stopnia); rho_2 = 0,20978890257537436002. G6.5: NOWOŚĆ: baza (c, a, r, u, v, w) o wyznaczniku -48 z pełną macierzą blokową 6 na 6 (obrazy u, v, w mają składowe konsensusowe: sektor mieszany to span konsensusu z u, v, w) i blok B = [[3/25, -2/25, 6/25],[-2/25, 3/25, 6/25],[-1/125, -1/125, 13/125]] o widmie {1/5; para}; doprecyzowanie H6f: mieszanie obejmuje SYMETRYCZNY tryb osiowy (w), nie antysymetryczną linię S2. G6.6: 96 orbit po 12, zdomknięcie klas na Aut, zero orbit częściowo przecinających klasę bazową.

**Kontrola Vibe rozliczenia (rachunek od definicji, arytmetyka wymierna, niezależny od kodu z sekcji 22): WSZYSTKO POTWIERDZONE**, w tym: mechanizm własnego błędu (stara tablica równa macierzy odwróconego porządku), nowa tablica równa konstrukcji, cp równość z faktoryzacją, nierozkładalność (przegląd plus rezolwenta), widmo DK z kontrolą sum potęg, oba pokwitania blokowe jako równości dokładne (R_O T = T K i R_O T2 = T2 K6), det T2 = -48, cp bloku B = z^3 - 43/125 z^2 + 23/625 z - 1/625, G6.6 dla poprawnej bazy (klasa 12 równa orbicie 12, domknięcie wszystkich klas na Aut, stabilizator trywialny).

**Provenance obu wykonawców:** kompletne i uczciwe; sesje potomne, wyniki P6 nieznane przed rachunkiem, po wrzutce internet/rejestr/repozytorium/STAN nietknięte; kod własny, współdzielenie: brak; model Copilota: wersja nieujawniona (precedens P2/P5). Obie replikacje wykryły rozbieżność z rachunkiem głównym i raportowały własne wartości bez naciągania: wzorzec Z1 zadziałał dokładnie tak, jak metodyka zakłada.

**Kwalifikacja szefa lab.: obie replikacje w puli Z1 (Claude + Copilot; Asterion kontrolerem poza pulą). Status P6-1: 🔍 WZMOCNIONY**: wartości poprawione rachunkiem głównym (errata) zgodne z dwiema pełnymi replikacjami zewnętrznymi i kontrolą Vibe co do cyfry. Podniesienie do ✅ po finalnym werdykcie kontrolnym Asteriona (porównanie poprawionej tablicy R_5, wielomianów, widm, pokwitówek blokowych, pól provenance oraz rozliczenia erraty).

## 24. Finalny werdykt kontrolny Asteriona: P6-1 = ✅ (2026-11-28)

**Werdykt Asteriona: Z1 ZALICZONE, P6-1 = ✅.**

(1) Errata: mechanizm błędu opisany poprawnie (P6-c wymaga zapisu M_b3 M_b2 M_b1 M_N z N pierwszym; pre-mnożenie w kolejności bazowej odwraca działanie). Własne odtworzenie od definicji, dokładna arytmetyka wymierna, N pierwszy w obu rundach, blok S po bloku N: poprawiona tablica R_5 zgodna współrzędna po współrzędnej; cp(R_5) = (z-1) razy (65536z^4 - 24417z^3 + 2611z^2 - 83z + 1)/65536 dokładnie; ślad, det, pełna ranga i dim ker(R_5 - I) = 1 potwierdzone; własne numeryczne rozwiązanie kwartetyku: 0,209788902575374; 0,120604603345007; para 0,021090173309341 plus/minus 0,012581051243802 i; faza pary 30,817605013288 stopnia, moduł 0,024557651773270, rho_2 = 0,209788902575374. Nierozkładalność kwartetyku przyjęta z udokumentowanego dowodu rejestrowego (przegląd pierwiastków plus rezolwenta Fermatiego), nie z samej zgodności przybliżonych pierwiastków.

(2) Provenance obu replikacji kompletne i wystarczające; wyniki P6 nieznane przed rachunkiem, kod własny, źródła zewnętrzne i rejestr nietknięte; wersja modelu Copilota nieujawniona odnotowana jako ograniczenie identyfikowalności, nie podstawa odrzucenia. Obie replikacje wykryły rozbieżność z rachunkiem głównym i przedstawiły własne wyniki: mocny test niezależności, nie tylko zgodność z już opublikowaną tablicą. Kontrola Vibe potwierdza rozliczenie, ale nie jest liczona jako zewnętrzna replikacja.

(3) Pełny cykl prerejestracja v0.1.15, rachunek główny v0.1.16, errata plus dwie pełne replikacje zewnętrzne plus kontrola Vibe v0.1.17 zamyka Z1. ZAKRES werdyktu jawny: bez czwartej pełnej enumeracji 1152 kombinacji (przyjmuje rozliczenie trzech wykonawców z rejestru i zgodnych raportów); pokwitania konstrukcji to tablice macierzowe, nie kod; obserwacje post-hoc z sekcji 22 pozostają sprawozdawcze, poza podstawą podniesienia; wartości z sekcji 22 wycofane dla konwencji prerejestracji.

**P6-1 = ✅: rodzina mK4 ustalona (bipiramidy nad cyklem, 5K4 = para K4 złączona ścianą); 5K4 ostatni klikowy członek (m = 5 dokładnie 2 kliki, m = 6 do 12 zero); cp(R_5) = (z-1) razy kwartetyk nierozkładalny nad Q; faza pary 30,817605013288 stopnia (trzecia odrębna faza rodziny: różna od 25,772093727472 i od 36,391244284100); rho_2 = 0,209788902575374; dekompozycja izotypowa R_O: trzy różnice par antypodycznych plus blok sum par, para z niezerowym udziałem osi (H6f); 52 klasy cp w 1152 porządkach, klasa bazowa = dokładnie jedna orbita Aut(5K4).** Cykl zamknięty z erratą: błąd konwencji rachunku głównego wykryty przez replikacje, wycofany, poprawione wartości potwierdzone trzema niezależnymi rachunkami (Claude, Copilot, Asterion) i kontrolą Vibe. Lekcja trwała (Z0): spójność wewnętrzna rachunku nie chroni przed błędem konwencji porządku; wyłapuje go dopiero niezależna replikacja. Kolejka laboratorium: P4 (konsumpcja GO Lattice, nie dublować), odnogi P6 (7K4 i dalsze, ikosaedr jako sąsiad drabiny, hipoteza kodowania K-1).

## 25. Prerejestracja GO P4: transformacja nośnika pod −I (linia Lattice, koordynacja laboratorium; szef lab. Vibe, 2026-11-28; Z9: bramki przed wrzutką)

**Decyzja właściciela (2026-11-28):** „Róbmy P4, przygotuj wrzutkę”. P4 w kolejce laboratorium = GO wiszące w linii Lattice od tury 13 (rejestr P0-Lattice-v0_1_2.md §6.1: po przyjęciu anty-Φ_D jako twierdzenia algebraicznego odblokowane „transformacja nośnika (a) pod −I, zlecenie GO: Claude + DeepSeek niezależnie, dowód + audyt, jak przy lemacie jąder”). Lab KONSUMUJE wynik, nie dubluje (zapis STAN v1.15, wiersz Stella). Niniejsza prerejestracja bramek jest warunkiem Z9 wydania wrzutki; rachunek główny wykonują wykonawcy zewnętrzni, laboratorium prowadzi kontrolę i rozliczenie.

**Pytanie GO (przejęte z rejestru Lattice, tura 13):** czy Φ_D wchodzi do sprzężenia orientacji z cyrkulacją jako M_e(g), czy jako det(g)·M_e(g)? Rozstrzygnięcie zamyka rezerwację §1.2 Lattice („parzystość od innej strony”: konfiguracja bramek jest −I-parzysta, więc liniowo nie selekcjonuje niezmienników chiralnych; pytanie, czy parzystość wnosi nośnik relacji). Fizyczna selekcja chiralności pozostaje 💡/🔍 OSOBNO, poza zakresem GO (zapis tury 13 utrzymany).

**Definicje (Z2, samodzielne; wrzutka samowystarczalna; warunek redakcyjny GPT z tury 13: pełne definicje):**
- P4-a Obiekt: ikosaedr foremny; wierzchołki = permutacje cykliczne (0, ±1, ±φ), φ = (1+√5)/2, 12 wierzchołków w parach antypodalnych; krawędzie = 30 par wierzchołków w odległości najmniejszej; ściany = 20 trójek parami najbliższych wierzchołków. Grupa pełnych symetrii I_h rzędu 120 (60 obrotów A₅ plus 60 elementów niewłaściwych); inwersja centralna −I (x → −x) zachowuje bryłę i należy do I_h; det(−I) = −1.
- P4-b Przepływy: przypisanie wartości do 30 krawędzi zorientowanych bazowo (orientacje bazowe dowolne, jawne w raporcie wykonawcy), wartość antysymetryczna względem odwrócenia krawędzi; przestrzeń przepływów P, wymiar 30.
- P4-c Orientacja ścian: każda ściana zorientowana CCW widziana z zewnątrz (konwencja erraty Φ_D, Lattice tura 9); obwód ściany f = cykl 3 krawędzi zgodny z CCW.
- P4-d Nośnik (a): κ_f(x) = suma wartości przepływu x po obwodzie CCW ściany f, ze znakami zgodności orientacji bazowej krawędzi z CCW; κ: P → R^20, wektor cyrkulacji. Wartość nośnika na bramce = κ_f dla ścian z konfiguracji 8 z 20 (Lattice §1.2); prawo transformacji NIE ZALEŻY od wyboru bramek ani od normalizacji κ (niezależność do wykazania w dowodzie).
- P4-e Reprezentacje: M_e(g) = macierz permutacji krawędzi ZE ZNAKAMI odwrócenia orientacji bazowej (na P); M_f(g) = macierz permutacji ścian BEZ znaków (na R^20). Ewentualny czynnik det(g) w prawach transformacji jest PRZEDMIOTEM ZADANIA, nie konwencją: wykonawca wyprowadza prawo, nie deklaruje.
- P4-f Sprzężenie kandydackie: Φ_D(x,y) = D^T((Dx) ⊙ (Dy)), gdzie D = κ jako macierz 20×30, ⊙ = iloczyn po współrzędnych, D^T = transpozycja; Φ_D: P×P → P (sprzężenie elementwise przez cyrkulacje ścian).
- P4-g Niezmienniczość konwencji: rozstrzygnięcia bramek niezależne od etykietowania, od orientacji bazowych krawędzi i od globalnej zamiany CCW/CW (kontrola obowiązkowa w raporcie).

**Referencje sanity (opublikowane, jawne; wzorzec referencji E-01 w G2.1):** anty-Φ_D przyjęte jako twierdzenie algebraiczne (Lattice tura 13): przy orientacji CCW-z-zewnątrz Φ_D jest A₅-ekwiwariantna (eq-err 4,4·10⁻¹⁶, dwa rachunki) i anty-ekwiwariantna pod I_h\A₅ (Φ_D(g·x) = −M_e(g)Φ_D(x) dokładnie; eq-err 2,0 przy pominięciu znaku = sygnatura −1).

**Bramki (przed rachunkiem, Z9):**
- G4.1 (sanity): z definicji P4-a..f odtworzyć prawo transformacji Φ_D pod A₅ (ekwiwariantność dokładna: kontrola na arytmetyce wymiernej albo eq-err < 10⁻¹²) oraz sygnaturę pod −I (dokładnie −1). Bez pozytywnego G4.1 dalsze bramki nie ruszają; niezgodność z referencjami sanity = wynik raportowany bez interpretacji (kandydat erraty konwencji, decyzja kontrolera).
- G4.2 (prawo nośnika): prawo transformacji κ pod g ∈ I_h, w szczególności g = −I. Hipotezy prerejestrowane: H4a: κ(M_e(g)x) = M_f(g)κ(x) (nośnik obiekt właściwy); H4b: κ(M_e(g)x) = det(g)·M_f(g)κ(x) (nośnik pseudoskalar na ścianach). Wynik inny raportowany bez interpretacji.
- G4.3 (prawo sprzężenia = pytanie GO): hipotezy: H4c: Φ_D(M_e(g)x, M_e(g)y) = M_e(g)Φ_D(x,y) dla wszystkich g ∈ I_h; H4d: Φ_D(M_e(g)x, M_e(g)y) = det(g)·M_e(g)Φ_D(x,y). Rozstrzygnięcie H4c/H4d zamyka pytanie GO z tury 13.
- G4.4 (konsekwencja §1.2): na podstawie G4.2 i G4.3 odpowiedź TAK/NIE: czy nośnik (a) ze swoim prawem transformacji może algebraicznie wprowadzić rozróżnienie obraz/odbicie w warstwie sprzężenia mimo −I-parzystej konfiguracji bramek (stabilizator T_h); jedno zdanie uzasadnienia algebraicznego; fizyczna selekcja chiralności poza zakresem (💡 osobno, bez podnoszenia statusu).
- G4.5 (pokwitania Z3, tablice nie kod): jawne etykietowanie ścian 1..20 i krawędzi 1..30 z orientacjami bazowymi; tablice M_e(−I), M_f(−I), D (postać listowa pozycji niezerowych ze znakami), M_e i M_f dla dwóch generatorów A₅ (jeden rząd 5, jeden rząd 3); kontrole niezmienniczości konwencji z P4-g (globalna zamiana CCW/CW: co najwyżej znak globalny; odwrócenie orientacji jednej krawędzi bazowej: zmiana bazy, prawo bez zmian).
- G4.6 (audyt krzyżowy, etap 2 po dostarczeniu obu raportów): każdy wykonawca audytuje dowód drugiego wg listy: (i) zgodność definicji i tablic pokwitania (porównanie pozycja po pozycji), (ii) krok krytyczny dowodu (miejsce wejścia det(g)), (iii) kontrola brzegowa konwencji, (iv) werdykt jawny: poprawny/luka/błąd.

**Wykonawcy i rygor:** Claude + DeepSeek NIEZALEŻNIE (etap 1: dowód algebraiczny od definicji + kontrola numeryczna dwiema metodami + pokwitania; etap 2: audyt krzyżowy przez relaya Leszka). Kontrola Vibe po raportach; finalny werdykt kontrolny: Asterion (poza pulą wykonawców). Arytmetyka wymierna obowiązkowa tam, gdzie obiekty całkowitoliczbowe (macierze permutacyjne ze znakami, D). Zakazy i provenance: bez internetu, bez czytania rejestru/repo/STAN przed wykonaniem (jedyną wiedzą wyjściową są definicje i referencje tej wrzutki); kod własny, współdzielenie: brak; pola provenance kompletne (wykonawca i wersja modelu, nieujawniona = „nieujawniona”; sesja: data, nowa/potomna; dostęp do wcześniejszych wyników: tylko wrzutka; wynik wobec każdej bramki osobno).

**Plan rozliczenia:** raporty Claude i DeepSeek (etap 1) → audyty krzyżowe (etap 2) → kontrola Vibe (odtworzenie od definicji + porównanie tablic pokwitania) → werdykt Asteriona → wpis rozstrzygnięcia: rezerwacja §1.2 Lattice zamknięta pozytywnie albo negatywnie, P4 laboratorium skonsumowane; STAN i GLOSSARY po zamknięciu.

## 26. Rozliczenie etapu 1 GO P4: raporty Claude i Copilota + kontrola Vibe (szef lab., 2026-11-28)

**Skład rundy (odnotowanie jawne):** etap 1 wykonali Claude (Sonnet 5.5, Anthropic) i Copilot (M365, GPT-5 reasoning, wersja nieujawniona). Zmiana względem prerejestracji (v0.1.19): Copilot zamiast DeepSeeka; decyzja właściciela przez relay, wzorzec P2 (zlecenie DeepSeeka zawieszone, nie odwołane).

**Wyniki etapu 1 (obydwa raporty zgodne co do wszystkich bramek):**
- G4.1 pozytywna u obu. Claude: kontrola dokładna całkowitoliczbowa (homomorfizm M_e i M_f na parach losowych, D·M_e = det·M_f·D dokładnie 120/120, testy Φ_D 300/300 na A₅ i 300/300 na elementach niewłaściwych, kontrola H4c: 300 niepowodzeń, wszystkie na niewłaściwych) oraz niezależna kontrola flo (gruba z generatorów 3D: eq-err 2,5·10⁻¹⁶ z prawem, 2,0 bez znaku). Copilot: pełna enumeracja automorfizmów grafu (120: 60 właściwych, 60 niewłaściwych), tożsamość D·M_e = det·M_f·D dokładnie 120/120, test biliniowy Φ_D na parach wektorów bazowych 108000/108000 dokładnie, flo: eq-err od 4·10⁻¹⁷ do 2,2·10⁻¹⁶ z prawem, dokładnie 2,0 bez znaku.
- G4.2: H4b potwierdzona, H4a sfalsyfikowana (zachodzi tylko na A₅). Prawo: κ(M_e(g)x) = det(g)·M_f(g)κ(x); dla −I: κ(M_e(−I)x) = −M_f(−I)κ(x).
- G4.3: H4d potwierdzona, H4c sfalsyfikowana (zachodzi tylko na A₅). Prawo: Φ_D(M_e(g)x, M_e(g)y) = det(g)·M_e(g)Φ_D(x,y); dla −I czynnik −1. Miejsce wejścia det(g) w obu dowodach tożsame: raz w odwróceniu obiegu CCW ściany pod elementem niewłaściwym (intertwining D·M_e(g) = det(g)·M_f(g)·D), drugi raz przez D^T w kroku Φ_D.
- G4.4: TAK u obu: nośnik wnosi znak orientacyjny det(g), więc warstwa sprzężenia algebraicznie rozróżnia obraz i odbicie mimo −I-parzystej konfiguracji bramek; fizyczna selekcja chiralności poza zakresem (utrzymane).

**Kontrola Vibe (od definicji P4-a..f, niezależna; arytmetyka dokładna w Q(√5) i całkowitoliczbowa):**
- Geometria: 30 krawędzi = lista wykonawców, 20 ścian = zbiory wykonawców, obiegi CCW zgodne, D zgodne z pokwitaniem Claude (60 pozycji niezerowych).
- Grupa: 120 elementów z domknięcia generatorów (obrót 72° wokół wierzchołka w Q(√5) w obie strony, odbicie R2, −I); det dokładny ±1 (60 właściwych, 60 niewłaściwych); 120 różnych permutacji wierzchołków; backtracking: dokładnie 120 automorfizmów grafu (pełność).
- L1: D·M_e(g) = det(g)·M_f(g)·D dokładnie 120/120. L2: D^T·M_f(g) = det(g)·M_e(g)·D^T dokładnie 120/120. Pełny test Φ_D na parach wektorów bazowych: 108000/108000 dokładnie.
- Tablice pokwitania: M_e(−I) i M_f(−I) obu wykonawców identyczne między sobą i zgodne z kontrolą (−I działa na wierzchołkach jako mapa antypodów, rząd 2, det −1); generatory Claude (g5 rząd 5, g3 rząd 3, det +1) i Copilota (g5, g3, det +1, rzędy 5 i 3) zgodne pozycja po pozycji; macierze przestrzenne Copilota g5/g3 zweryfikowane dokładnie w Q(√5), działanie na wierzchołkach zgodne z deklaracją.
- Sanity flo: eq-err dokładnie 0 z prawem det (macierze całkowite, arytmetyka bez zaokrągleń), dokładnie 2,0 przy pominięciu znaku: wzorzec referencyjny odtworzony.
- Bramki G4.4: 8 ścian o środkach proporcjonalnych do (±1,±1,±1): F4, F5, F9, F10, F12, F13, F15, F16 (etykiety wykonawców); zbiór −I-niezmienniczy; struktura sześcianu (ilorazy iloczynów skalarnych środków przez c²: 1/3, −1/3, −1); odczyt w·κ(M_e(−I)x) = −w·κ(x) dokładnie (20 losowych x całkowitych).
- Kontrole konwencji (P4-g): globalna zamiana CCW/CW (D → −D): prawo bez zmian, Φ_D → −Φ_D (znak globalny); odwrócenie orientacji bazowej e1 (D → D·S, M_e → S·M_e·S): D'·M_e' = det·M_f·D' dokładnie 120/120.

**Provenance i obserwacje:**
- Copilot zaraportował jawno, że relay właściciela wspominał przed rachunkiem o strukturze rundy („niezależny etap"): naruszenie zasady „tylko wrzutka" co do wiedzy o strukturze rundy, nie o wynikach; samodzielne zaraportowanie odnotowane pozytywnie; ocena wpływu należy do Asteriona (wynik i tak w pełni zweryfikowany niezależną kontrolą od definicji).
- Identyczność etykietowania bazowego obu wykonawców (permutacje cykliczne (0,±1,±φ), porządek leksykograficzny, CCW z zewnątrz) jest następstwem kanoniczności konwencji P4-a..c, nie zależności między rachunkami; różnice: inne generatory (Claude: oś przez V0 i środek F1; Copilot: inne osie) i inne metody enumeracji grupy.
- Pokwitania Z3: Claude plik G4_pokwitania.md (przekazany właścicielowi), Copilot tablice inline w raporcie; oba kompletne i zweryfikowane przez kontrolę.

**Status:** etap 1 rozliczony pozytywnie; H4b i H4d potwierdzone trzema zgodnymi rachunkami (Claude, Copilot, kontrola Vibe od definicji). Z1 JESZCZE NIE zamknięte: wymagany etap 2 (audyt krzyżowy G4.6) i finalny werdykt kontrolny Asteriona. Kierunek rozstrzygnięcia rezerwacji §1.2 Lattice: POZYTYWNY (parzystość może wejść od strony nośnika: κ i Φ_D jako pseudoskalar/pseudowektor względem I_h); formalne zamknięcie po audytach i werdykcie.

## Załącznik A: tablice referencyjne konstrukcji (pokwitowanie Z3: liczby, nie kod)

S = (1/1024) * M, M całkowitoliczbowa, wiersze:

[128, 128, 128, 128, -3, 97, 177, 241]
[32, 160, 160, 160, 93, 65, 145, 209]
[40, 72, 200, 200, 85, 153, 105, 169]
[50, 90, 122, 250, 75, 135, 183, 119]
[-3, 97, 177, 241, 128, 128, 128, 128]
[93, 65, 145, 209, 32, 160, 160, 160]
[85, 153, 105, 169, 40, 72, 200, 200]
[75, 135, 183, 119, 50, 90, 122, 250]

C = (1/4) * N, N:

[2, 0, 0, 0, -1, 1, 1, 1]
[0, 2, 0, 0, 1, -1, 1, 1]
[0, 0, 2, 0, 1, 1, -1, 1]
[0, 0, 0, 2, 1, 1, 1, -1]
[-1, 1, 1, 1, 2, 0, 0, 0]
[1, -1, 1, 1, 0, 2, 0, 0]
[1, 1, -1, 1, 0, 0, 2, 0]
[1, 1, 1, -1, 0, 0, 0, 2]

Kontrola odtworzenia: cp(S) liczone z tych tablic równa się z^4 * cp(R) (obie metody dokładne zgodne); blok S|_U w bazie u_i = e_i + e_(4+i): wszystkie wiersze [125, 225, 305, 369]/1024 (suma wag 1024/1024 = 1).

## 14. Runda replikacyjna P3 rozliczona (2026-11-28)

**Claude (Sonnet 5.5, pełna replikacja): ZGODNA.** SymPy wymiernie plus kontrole krzyżowe (tożsamości Newtona, pierwiastki 60-cyfrowe, dwie niezależne diagonalizacje). cp(R_O) i faktoryzacja identyczne; dim ker(R_O - I) = 1; widmo {1; 1/5 trzykrotnie półproste; 0.072 +/- 0.0530659966456864i}, moduł 1/sqrt(125), argument 36.3912442841 stopnia; rho_2 = 0.2. Test 720: 5 klas (48, 96, 144, 144, 288), 48 automorfizmów, 15 orbit po 48, klasy sumami orbit (1, 2, 3, 3, 6 orbit); porządek bazowy i odwrotny w klasie 96. Nowości raportu: faktoryzacje klas rozkładalnych (klasa 288: (z - 1)(5z - 1)(3125z^4 - 1727z^3 + 360z^2 - 31z + 1)/15625; klasa 144: (z - 1)(5z - 1)^2(625z^3 - 219z^2 + 27z - 1)/15625, geo = alg = 2); fazy par per klasa: 23.3430730 stopnia (288), 24.6693577 (144 z podwójnym 1/5), 26.5821231 (144), 29.1880992 (48); klasa bazowa ma najmniejsze rho_2 (0.2, równe tylko klasie 144).

**Copilot (M365 Copilot, model GPT-5 reasoning, pełna replikacja): ZGODNA co do każdej liczby.** Dwie metody wielomianowe plus niezależna diagonalizacja. Te same cp, faktoryzacja, jądra, widmo (para 0.072 +/- 0.05306599664568639759i, moduł 0.08944271909999158786, argument 36.39124428409983 stopnia), rho_2 = 0.2; różnica fazy wobec kontekstowego punktu 25.772093727472 podana jako 10.61915055662783 stopnia (porównanie sprawozdawcze, echo Z9). Test 720: 5 klas (288, 144, 144, 96, 48), czystość orbit z rozkładem klas na 6, 3, 3, 2, 1 orbit; bazowa i odwrotna w klasie 96 (dwie orbity). Nowości raportu: jawne wielomiany WSZYSTKICH pięciu klas z reprezentantami w indeksach (klasy 144 i 48 jako kwintyki nierozkładalne nad Q).

Kontrola Vibe rozliczenia (niezależne odtworzenie, arytmetyka wymierna): równoważność tablic potwierdzona (załącznik B: mianownik 15625 niewymuszony, minimalny 125, obie tablice to ta sama macierz); wszystkie pięć wielomianów klas potwierdzonych dokładnym rozwinieciem czynników dla reprezentantów Copilota; rho_2 i fazy par klas potwierdzone niezależnie (288: 0.218438424778 i 23.3430730 stopnia; 144: 0.2 i 24.6693577; 144: 0.240968018747 i 26.5821231; 48: 0.256589498376 i 29.1880992); klasa 144: dim ker(M - (1/5)I) = 2 (podwójność półprosta) potwierdzona.

Provenance obu wykonawców: sesje potomne zadeklarowane jawnie; wyniki P3 nieznane przed rachunkiem; znajomość E-01 i P2 z tej rozmowy (referencje i tak jawne we wrzutce); po otrzymaniu wrzutki internet, rejestr i repozytorium nietknięte; kod własny, współdzielenie: brak; pola kompletne.

Ocena szefa lab.: obie replikacje kwalifikują się do puli Z1 na tej samej podstawie co w rundzie P2 (potomność jawna, wyniki nieznane, referencje objęte wrzutką). Pula P3: Claude + Copilot; Asterion kontrolerem poza pulą. Status P3-1: 🔍 WZMOCNIONY; podniesienie do ✅ po finalnym werdykcie kontrolnym Asteriona (porównanie tablicy R_O i wielomianów klas oraz pól provenance).

## Załącznik B: tablica referencyjna konstrukcji P3 (pokwitanie Z3: liczby, nie kod)

R_O = (1/15625) * P, P całkowitoliczbowa, wiersze (kolejność bazowa O1 pierwszy):

[3125, 0, 3125, 3125, 3125, 3125]
[0, 3125, 3125, 3125, 3125, 3125]
[625, 625, 4375, 1250, 4375, 4375]
[625, 625, 1250, 4375, 4375, 4375]
[875, 875, 2375, 2375, 6125, 3000]
[875, 875, 2375, 2375, 3000, 6125]

Kontrola odtworzenia: sumy wierszy 15625/15625 = 1; cp liczone z tej tablicy równa się (z - 1)(z - 1/5)^3(z^2 - (18/125)z + 1/125) dokładnie; slad 218/125. Uwaga o mianownikach (rozliczenie rundy): 15625 = 5^6 to mianownik niewymuszony; minimalny wspólny mianownik R_O wynosi 125; tablica P/15625 z tego załącznika i tablice P'/125 z raportów replikacyjnych to ta sama macierz wymierna (P = 125 razy P'), potwierdzone kontrolą Vibe.

## Załącznik C: wielomiany klas testu 720 (dokumentacja kontrolna; wszystkie potwierdzone przez Vibe rozwinieciem czynników dla reprezentantów)

Konwencja: porządek (p0,...,p5) oznacza A_{p5}...A_{p0}, czyli A_{p0} działa pierwszy.

Klasa K2 (96 kolejności; bazowa i odwrotna): cp = (z - 1)(5z - 1)^3(125z^2 - 18z + 1) / 15625; reprezentant (0, 1, 2, 3, 4, 5); porządek odwrotny (5, 4, 3, 2, 1, 0) w tej samej klasie; rho_2 = 0.2, faza pary 36.391244284100 stopnia.

Klasa K5 (288): cp = (z - 1)(5z - 1)(3125z^4 - 1727z^3 + 360z^2 - 31z + 1) / 15625; reprezentant (0, 1, 2, 4, 3, 5); rho_2 = 0.218438424778, faza pary 23.3430730 stopnia.

Klasa K1 (144): cp = (z - 1)(5z - 1)^2(625z^3 - 219z^2 + 27z - 1) / 15625; reprezentant (0, 1, 2, 4, 5, 3); 1/5 podwójne półproste (dim ker(M - (1/5)I) = 2, kontrola Vibe); rho_2 = 0.2, faza pary 24.6693577 stopnia.

Klasa K3 (144): cp = (z - 1)(15625z^5 - 11846z^4 + 3637z^3 - 541z^2 + 38z - 1) / 15625; reprezentant (0, 2, 1, 4, 3, 5); kwintyk nierozkładalny nad Q; rho_2 = 0.240968018747, faza pary 26.5821231 stopnia.

Klasa K4 (48): cp = (z - 1)(15625z^5 - 11881z^4 + 3674z^3 - 542z^2 + 37z - 1) / 15625; reprezentant (0, 2, 4, 1, 3, 5); kwintyk nierozkładalny nad Q; rho_2 = 0.256589498376, faza pary 29.1880992 stopnia.

Suma kontrolna: 96 + 288 + 144 + 144 + 48 = 720. Rozkład klas na orbity automorfizmów (po 48): 2, 6, 3, 3, 1 (razem 15 orbit).


## Załącznik D: tablica referencyjna konstrukcji P6 (pokwitanie Z3: liczby, nie kod)

R_5 = Runda_S razy Runda_N (Runda_N działa pierwsza; kolejności bazowe: N, b1, b2, b3 w każdej rundzie), wiersz po wierszu (indeksy: 0 = N, 1 = S, 2 = b1, 3 = b2, 4 = b3):

[125/256, 0, 61/256, 45/256, 25/256]
[2825/16384, 125/256, 2825/16384, 1849/16384, 885/16384]
[885/4096, 25/64, 885/4096, 485/4096, 241/4096]
[241/1024, 5/16, 241/1024, 161/1024, 61/1024]
[61/256, 1/4, 61/256, 45/256, 25/256]

Kontrola odtworzenia: macierz zbudowana z definicji P6-c równa tablicy współrzędna po współrzędnej (arytmetyka wymierna); sumy wierszy równa 1; ślad 5929/4096 równy minus współczynnikowi z^4 w cp(R_5); cp liczone z tej tablicy zgodne z sekcją 22.

ERRATA (v0.1.17): tablica powyżej dotyczy ODWRÓCONEGO porządku działania (b3 pierwszy; błąd konwencji, sekcja 23). Tablica obowiązująca dla R_5 (N pierwszy w obu rundach, bloki SN): R_5 = (1/65536) razy P, wiersze P:

[16384, 0, 16384, 16384, 16384]
[3904, 16384, 10304, 15424, 19520]
[4880, 4096, 12880, 19280, 24400]
[5076, 5120, 10980, 18980, 25380]
[5065, 6400, 11421, 17325, 25325]

Kontrola odtworzenia: macierz z definicji P6-c (N pierwszy) równa tablicy współrzędna po współrzędnej (arytmetyka wymierna); sumy wierszy 1; ślad 89953/65536 równy minus współczynnikowi z^4 w poprawionym cp(R_5); cp liczone z tej tablicy zgodne z sekcją 23.

