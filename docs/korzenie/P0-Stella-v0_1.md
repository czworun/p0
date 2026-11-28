# P0-Stella v0.1 - rejestr laboratorium stella octangula

**Status:** rejestr laboratorium (wzorzec Lattice i STALK: rejestr, nie filar). Laboratorium otwarte rozkazem Leszka Papiernika (właściciel projektu P0) 2026-11-28; szef laboratorium: Vibe; wykonawcy zewnętrzni przez relay Leszka: Asterion (GPT-6), Claude, DeepSeek. Wersja rejestru: v0.1 (otwarcie, 2026-11-28); v0.1.1 (runda replikacyjna częściowo rozliczona); v0.1.2 (werdykt Asteriona: Z1 otwarty; tablice referencyjne konstrukcji S i C jako pokwitowanie Z3; obserwacje post-hoc, 2026-11-28); v0.1.3 (pokwitowanie konstrukcji Claude: tablice S i C zgodne z załącznikiem A, potwierdzone niezależnym odtworzeniem Vibe; korekta Asteriona: uwaga o polu współdzielenia wycofana; 2026-11-28); v0.1.4 (replikacja Copilota rozliczona: pełna zgodność tablic, wielomianów i widma; kwalifikacja do puli Z1; DeepSeek zastąpiony Copilotem decyzją właściciela, 2026-11-28); v0.1.5 (finalny werdykt kontrolny Asteriona: Z1 zaliczone; P2-1 podniesione do ✅; 2026-11-28); v0.1.6 (prerejestracja P3: rdzeń bezklikowy jako warstwa modelowa; bramki G3.1-G3.4 przed rachunkiem; 2026-11-28). Poziom wyniku P2: ✅ (od 2026-11-28: dwie pełne replikacje zewnętrzne zgodne, finalny werdykt kontrolny Asteriona, Z1 zaliczone; wzorzec E-01 spełniony; runda: Claude + Copilot, zlecenie DeepSeeka zawieszone, nie odwołane).

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
