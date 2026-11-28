# P0-Stella v0.1 - rejestr laboratorium stella octangula

**Status:** rejestr laboratorium (wzorzec Lattice i STALK: rejestr, nie filar). Laboratorium otwarte rozkazem Leszka Papiernika (właściciel projektu P0) 2026-11-28; szef laboratorium: Vibe; wykonawcy zewnętrzni przez relay Leszka: Asterion (GPT-6), Claude, DeepSeek. Poziom wyniku P2: 🔍 (jedna sesja, rachunek operatora E1a); podniesienie do ✅ wymaga replikacji Z1 (zlecenie przygotowane 2026-11-28).

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
