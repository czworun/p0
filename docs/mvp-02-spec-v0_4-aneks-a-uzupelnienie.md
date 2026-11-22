# MVP-02: UZUPEŁNIENIE Aneksu A do specyfikacji v0.4 (tabele wag projekcyjnych, współczynniki jawnych sum udział(t), FORMA ZAMKNIĘTA WAG; errata B-05 + E4)

> Status: UZUPEŁNIENIE do dokumentu docs/mvp-02-spec-v0_4.md, hashowane RAZEM ze specyfikacją przy v1.0 (decyzja właściciela, par. 2.5 v0.4). Sekcje 1 do 5: treść dostarczona przy ataku DELTA na v0.3, BEZ ZMIAN LICZBOWYCH. Sekcja 6: FORMA ZAMKNIĘTA WAG (errata (f) v0.4, E4 Claude; niezależnie potwierdzona przez Vibe na wszystkich 50 wagach z sekcji 3, maksymalna różnica 4.9·10^-5 = wylacznie zaokraglenia tabel 4-cyfrowych). Rachunek wyłącznie algebraiczny (K6 czyste): dekompozycja spektralna L_dod, macierze projekcyjne, rekurencja u_d; sup, tau, U_b i kill criterion NIE wyznaczane. Zero swobód (K8): wszystkie wartości funkcjami obiektów zamrożonych par. 0.3 i par. 0.4 v0.4. Liczby jawnym tekstem na 4 miejsca znaczące, potęgi notacją a^b, zero LaTeXu; kontrola grep wykonana.

## 1. Metoda (jawna)

(1) L_dod = 3I − A z tabeli ścian par. 0.3 v0.4 (graf dwunastościanu, 20×20); diagonalizacja symetryczna pełna (metoda Jacobiego, norma pozadiagonalna < 10^-12). Klastry wartości własnych {0; 3−sqr(5); 2; 3; 5; 3+sqr(5)} o krotnościach {1, 3, 5, 4, 4, 3} (jądro = stała; sektory T1g, H_u, G_g, G_u, T2g); projektory P_a = suma iloczynów zewnętrznych wektorów klastra (ortogonalne, symetryczne, idempotentne rachunkowo do < 10^-10).
(2) Wektory cechowania z_f = e_f − (1/20)·1 (soma-zero, norma^2 = 19/20).
(3) Kanał POWIERZCHNIA: A_a(f,h) = z_h^T·P_a·z_f; wagi g_a = (20/19)·A_a; udział(t) = suma_a g_a^2·cos^2(omega_a·t) + suma_{a<b} 2·g_a·g_b·cos(omega_a·t)·cos(omega_b·t) (15 wyrazów symetryzowanych, A.1).
(4) Kanał WNĘTRZE przez twierdzenie metryczne par. 2.1 v0.4 (U = B·L_dod^(−1/2) izometria soma-zero na V_cyc, U·L_dod = L_eq·U; wejście omega_f/sqr(3) = U·L_dod^(1/2)·z_f/sqr(3), cel span{omega_h} = obraz span{L_dod^(1/2)·z_h}): wagi g_a,int = (lambda_a/3)·A_a; ta sama forma udziału(t).
(5) Stałość orbitowa twierdzeniem równowariantności pełnej I_h (bramka sanity par. 2.3 v0.4, każda rozbieżność = GLOBALNY STOP); publikacja per orbita d = 1 do 5 po reprezentancie; pełne przypisanie transfer do orbita macierzą dystansów w sekcji 2; kontrole stałości: druga para każdej orbity oraz odwrócenie kierunku zgodne do < 10^-10 (sekcja 4).
(6) FORMA ZAMKNIĘTA (sekcja 6): wagi nie muszą być brane z diagonalizacji: istnieje rekurencja kombinatoryczna u_d(theta) wyznaczająca wszystkie 50 wartości z tablicy przecięć grafu; metoda kontrolna niezależna wobec tabelek (E4).

## 2. Macierz dystansów D[f][h] (BFS na grafie par. 0.3 v0.4; wiersz = ściana źródłowa, kolumna = ściana celu; zero na przekątnej; transfer (f do h) przyjmuje wartości z orbity d = D[f][h])

f0: 0 1 1 2 2 1 2 2 2 2 3 3 4 3 3 4 3 3 4 5
f1: 1 0 2 2 1 2 1 2 3 3 2 3 3 4 4 5 3 2 3 4
f2: 1 2 0 1 2 2 3 3 1 2 4 4 5 2 3 3 2 3 3 4
f3: 2 2 1 0 1 3 3 4 2 3 3 5 4 2 4 3 1 2 2 3
f4: 2 1 2 1 0 3 2 3 3 4 2 4 3 3 5 4 2 1 2 3
f5: 1 2 2 3 3 0 2 1 2 1 3 2 3 3 2 3 4 4 5 4
f6: 2 1 3 3 2 2 0 1 4 3 1 2 2 5 3 4 4 2 3 3
f7: 2 2 3 4 3 1 1 0 3 2 2 1 2 4 2 3 5 3 4 3
f8: 2 3 1 2 3 2 4 3 0 1 5 3 4 1 2 2 2 4 3 3
f9: 2 3 2 3 4 1 3 2 1 0 4 2 3 2 1 2 3 5 4 3
f10: 3 2 4 3 2 3 1 2 5 4 0 2 1 4 3 3 3 1 2 2
f11: 3 3 4 5 4 2 2 1 3 2 2 0 1 3 1 2 4 3 3 2
f12: 4 3 5 4 3 3 2 2 4 3 1 1 0 3 2 2 3 2 2 1
f13: 3 4 2 2 3 3 5 4 1 2 4 3 3 0 2 1 1 3 2 2
f14: 3 4 3 4 5 2 3 2 2 1 3 1 2 2 0 1 3 4 3 2
f15: 4 5 3 3 4 3 4 3 2 2 3 2 2 1 1 0 2 3 2 1
f16: 3 3 2 1 2 4 4 5 2 3 3 4 3 1 3 2 0 2 1 2
f17: 3 2 3 2 1 4 2 3 4 5 1 3 2 3 4 3 2 0 1 2
f18: 4 3 3 2 2 5 3 4 3 4 2 3 2 2 3 2 1 1 0 1
f19: 5 4 4 3 3 4 3 3 3 3 2 2 1 2 2 1 2 2 1 0

## 3. Tabele wag per orbita (reprezentant = najmniejsza uporządkowana para leksykograficznie; wszystkie transfery orbity przyjmują te wartości; częstości omega1 do omega5 z sektorami T1g, H_u, G_g, G_u, T2g)

ORBITA d1 (reprezentant (f0 do f1); 60 uporządkowanych par)
- POWIERZCHNIA wagi: g1 = 0.1177, g2 = 0.08772, g3 = 0, g4 = −0.1404, g5 = −0.1177
- POWIERZCHNIA współczynniki (symetryzowane, 15, kolejność c(1,1) c(1,2) c(1,3) c(1,4) c(1,5) c(2,2) c(2,3) c(2,4) c(2,5) c(3,3) c(3,4) c(3,5) c(4,4) c(4,5) c(5,5)): c(1,1) = 0.01385, c(1,2) = 0.02065, c(1,3) = 0, c(1,4) = −0.03304, c(1,5) = −0.0277, c(2,2) = 0.007695, c(2,3) = 0, c(2,4) = −0.02462, c(2,5) = −0.02065, c(3,3) = 0, c(3,4) = 0, c(3,5) = 0, c(4,4) = 0.0197, c(4,5) = 0.03304, c(5,5) = 0.01385
- POWIERZCHNIA kontrola wycieku: suma wag = −0.05263 (wartość dokładna −1/19), kwadrat = 0.00277 (wartość dokładna 1/361 = 0.002770)
- WNĘTRZE wagi: g1,int = 0.02847, g2,int = 0.05556, g3,int = 0, g4,int = −0.2222, g5,int = −0.1951
- WNĘTRZE współczynniki (symetryzowane, 15): c(1,1) = 0.0008105, c(1,2) = 0.003163, c(1,3) = 0, c(1,4) = −0.01265, c(1,5) = −0.01111, c(2,2) = 0.003086, c(2,3) = 0, c(2,4) = −0.02469, c(2,5) = −0.02168, c(3,3) = 0, c(3,4) = 0, c(3,5) = 0, c(4,4) = 0.04938, c(4,5) = 0.08673, c(5,5) = 0.03808
- WNĘTRZE kontrola wycieku: suma wag = −0.3333 (wartość dokładna −1/3, kwadrat = 1/9 = 0.1111)

ORBITA d2 (reprezentant (f0 do f3); 120 uporządkowanych par)
- POWIERZCHNIA wagi: g1 = 0.05263, g2 = −0.08772, g3 = −0.1053, g4 = 0.03509, g5 = 0.05263
- POWIERZCHNIA współczynniki (symetryzowane, 15, kolejność jak wyżej): c(1,1) = 0.00277, c(1,2) = −0.009234, c(1,3) = −0.01108, c(1,4) = 0.003693, c(1,5) = 0.00554, c(2,2) = 0.007695, c(2,3) = 0.01847, c(2,4) = −0.006156, c(2,5) = −0.009234, c(3,3) = 0.01108, c(3,4) = −0.007387, c(3,5) = −0.01108, c(4,4) = 0.001231, c(4,5) = 0.003693, c(5,5) = 0.00277
- POWIERZCHNIA kontrola wycieku: suma wag = −0.05263 (dokładnie −1/19), kwadrat = 0.00277 (dokładnie 1/361)
- WNĘTRZE wagi: g1,int = 0.01273, g2,int = −0.05556, g3,int = −0.1, g4,int = 0.05556, g5,int = 0.08727
- WNĘTRZE współczynniki (symetryzowane, 15): c(1,1) = 0.0001621, c(1,2) = −0.001415, c(1,3) = −0.002546, c(1,4) = 0.001415, c(1,5) = 0.002222, c(2,2) = 0.003086, c(2,3) = 0.01111, c(2,4) = −0.006173, c(2,5) = −0.009696, c(3,3) = 0.01, c(3,4) = −0.01111, c(3,5) = −0.01745, c(4,4) = 0.003086, c(4,5) = 0.009696, c(5,5) = 0.007616
- WNĘTRZE kontrola wycieku: suma wag = 0 (dokładnie 0 dla dystansów 2 do 5)

ORBITA d3 (reprezentant (f0 do f10); 120 uporządkowanych par)
- POWIERZCHNIA wagi: g1 = −0.05263, g2 = −0.08772, g3 = 0.1053, g4 = 0.03509, g5 = −0.05263
- POWIERZCHNIA współczynniki (symetryzowane, 15, kolejność jak wyżej): c(1,1) = 0.00277, c(1,2) = 0.009234, c(1,3) = −0.01108, c(1,4) = −0.003693, c(1,5) = 0.00554, c(2,2) = 0.007695, c(2,3) = −0.01847, c(2,4) = −0.006156, c(2,5) = 0.009234, c(3,3) = 0.01108, c(3,4) = 0.007387, c(3,5) = −0.01108, c(4,4) = 0.001231, c(4,5) = −0.003693, c(5,5) = 0.00277
- POWIERZCHNIA kontrola wycieku: suma wag = −0.05263 (dokładnie −1/19), kwadrat = 0.00277 (dokładnie 1/361)
- WNĘTRZE wagi: g1,int = −0.01273, g2,int = −0.05556, g3,int = 0.1, g4,int = 0.05556, g5,int = −0.08727
- WNĘTRZE współczynniki (symetryzowane, 15): c(1,1) = 0.0001621, c(1,2) = 0.001415, c(1,3) = −0.002546, c(1,4) = −0.001415, c(1,5) = 0.002222, c(2,2) = 0.003086, c(2,3) = −0.01111, c(2,4) = −0.006173, c(2,5) = 0.009696, c(3,3) = 0.01, c(3,4) = 0.01111, c(3,5) = −0.01745, c(4,4) = 0.003086, c(4,5) = −0.009696, c(5,5) = 0.007616
- WNĘTRZE kontrola wycieku: suma wag = 0 (dokładnie 0 dla dystansów 2 do 5)

ORBITA d4 (reprezentant (f0 do f12); 60 uporządkowanych par)
- POWIERZCHNIA wagi: g1 = −0.1177, g2 = 0.08772, g3 = 0, g4 = −0.1404, g5 = 0.1177
- POWIERZCHNIA współczynniki (symetryzowane, 15, kolejność jak wyżej): c(1,1) = 0.01385, c(1,2) = −0.02065, c(1,3) = 0, c(1,4) = 0.03304, c(1,5) = −0.0277, c(2,2) = 0.007695, c(2,3) = 0, c(2,4) = −0.02462, c(2,5) = 0.02065, c(3,3) = 0, c(3,4) = 0, c(3,5) = 0, c(4,4) = 0.0197, c(4,5) = −0.03304, c(5,5) = 0.01385
- POWIERZCHNIA kontrola wycieku: suma wag = −0.05263 (dokładnie −1/19), kwadrat = 0.00277 (dokładnie 1/361)
- WNĘTRZE wagi: g1,int = −0.02847, g2,int = 0.05556, g3,int = 0, g4,int = −0.2222, g5,int = 0.1951
- WNĘTRZE współczynniki (symetryzowane, 15): c(1,1) = 0.0008105, c(1,2) = −0.003163, c(1,3) = 0, c(1,4) = 0.01265, c(1,5) = −0.01111, c(2,2) = 0.003086, c(2,3) = 0, c(2,4) = −0.02469, c(2,5) = 0.02168, c(3,3) = 0, c(3,4) = 0, c(3,5) = 0, c(4,4) = 0.04938, c(4,5) = −0.08673, c(5,5) = 0.03808
- WNĘTRZE kontrola wycieku: suma wag = 0 (dokładnie 0 dla dystansów 2 do 5)

ORBITA d5 (reprezentant (f0 do f19); 20 uporządkowanych par)
- POWIERZCHNIA wagi: g1 = −0.1579, g2 = 0.2632, g3 = −0.2105, g4 = 0.2105, g5 = −0.1579
- POWIERZCHNIA współczynniki (symetryzowane, 15, kolejność jak wyżej): c(1,1) = 0.02493, c(1,2) = −0.0831, c(1,3) = 0.06648, c(1,4) = −0.06648, c(1,5) = 0.04986, c(2,2) = 0.06925, c(2,3) = −0.1108, c(2,4) = 0.1108, c(2,5) = −0.0831, c(3,3) = 0.04432, c(3,4) = −0.08864, c(3,5) = 0.06648, c(4,4) = 0.04432, c(4,5) = −0.06648, c(5,5) = 0.02493
- POWIERZCHNIA kontrola wycieku: suma wag = −0.05263 (dokładnie −1/19), kwadrat = 0.00277 (dokładnie 1/361)
- WNĘTRZE wagi: g1,int = −0.0382, g2,int = 0.1667, g3,int = −0.2, g4,int = 0.3333, g5,int = −0.2618
- WNĘTRZE współczynniki (symetryzowane, 15): c(1,1) = 0.001459, c(1,2) = −0.01273, c(1,3) = 0.01528, c(1,4) = −0.02546, c(1,5) = 0.02, c(2,2) = 0.02778, c(2,3) = −0.06667, c(2,4) = 0.1111, c(2,5) = −0.08727, c(3,3) = 0.04, c(3,4) = −0.1333, c(3,5) = 0.1047, c(4,4) = 0.1111, c(4,5) = −0.1745, c(5,5) = 0.06854
- WNĘTRZE kontrola wycieku: suma wag = 0 (dokładnie 0 dla dystansów 2 do 5)

## 4. Kontrole wykonane przy dostawie v0.3 (wszystkie PASS; bez zmian w v0.4)

- ślad L_dod = 60 ✓; krotności klastrów dokładnie 1, 3, 5, 4, 4, 3 ✓; suma projektorów = tożsamość (odchylenie max 3.33·10^-15) ✓
- wycieki: powierzchnia, wszystkie orbity: suma wag = −1/19, kwadrat 1/361 = 0.0028 ✓; wnętrze d1: kwadrat 1/9 = 0.1111 ✓; wnętrze d2 do d5: 0 (residuum < 10^-14) ✓ (zgodność ze par. 2.3 i A.5 v0.4)
- stałość orbitowa: druga para każdej orbity vs reprezentant, maksymalna różnica wag = 3.87·10^-15 ✓; symetria kierunku (h do f vs f do h): maksymalna różnica = 1.33·10^-15 ✓
- kontrola B-05 (niezerowość wag, próg 10^-9): ZERA: d1 powierzchnia g3; d1 wnętrze g3; d4 powierzchnia g3; d4 wnętrze g3 (wejścia ze zredukowaną liczbą częstości na wskazanych orbitach/kanałach; protokoły A.3 i A.4 bez zmian; patrz też adnotacja E5: par. A.2 v0.4)

## 5. Noty

- Rekonstrukcja udział(t) transferu (f do h): weź d = D[f][h] z sekcji 2, potem wagi i współczynniki wiersza orbity d z sekcji 3 (osobno kanał powierzchni i kanał wnętrza); udział(0) = (suma wag)^2 = wartość kontroli wycieku. Stałość orbitowa weryfikowana bramką sanity przy rachunku zerowym.
- Zastrzeżenie dokładności: diagonalizacja double; wartości publikowane na 4 miejsca znaczące; dokładność rachunkowa wag rzędu 10^-12 lub lepsza; geometria (macierz dystansów) dokładna. Forma zamknięta (sekcja 6) pozwala wyprowadzić wartości na dowolną liczbę cyfr bez diagonalizacji.
- theta (połowa supremum) i tau (protokoły A.3, A.4 v0.4) NIE są wyznaczane w tym dokumencie (K6; rachunek transportowy dopiero po bindzie v1.0).
- Bind: niniejsze uzupełnienie zawiera liczby wpływające na wynik; przy v1.0 hashowane RAZEM ze specyfikacją (decyzja właściciela, par. 2.5 v0.4).

## 6. FORMA ZAMKNIĘTA WAG (E4 Claude; wcielona erratą (f) v0.4; niezależnie potwierdzona przez Vibe na wszystkich 50 wagach sekcji 3: maksymalna różnica 4.9·10^-5 = wyłącznie zaokrąglenia tabel 4-cyfrowych)

**TABLICA PRZECIĘĆ grafu dwunastościanu (BFS niezależny warsztatu):** tablice (indeksowane od 0): b = (3, 2, 1, 1, 1) dla i = 0 do 4 (liczba ścian na dystansie i+1 od ściany bazowej w jej sąsiedztwie); c = (1, 1, 1, 2, 3) dla i = 1 do 5 (liczba ścian na dystansie i−1); pełne tablice równoważne a_i = 3 − b_i − c_i (dla i = 0: a_0 = 0, c_0 = 0).

**REKURENCJA u_d(theta) (jedyny obiekt wolny od diagonalizacji):** u_0 = 1; u_1 = theta/3; dla kroków i = 1 do 4: b_i·u_{i+1} = (theta − a_i)·u_i − c_i·u_{i−1}, gdzie krok i używa trójki (a_i, b_i, c_i) = (3 − b_i − c_i, b_i, c_i) z tablic (b_1, b_2, b_3, b_4) = (2, 1, 1, 1), (c_1, c_2, c_3, c_4) = (1, 1, 1, 2), (a_1, a_2, a_3, a_4) = (0, 1, 1, 0); (b_0, c_0, a_0) = (3, 0, 0). UWAGA (koncesja warsztatowa, wpisana wprost): indeksowanie tablic jest jednolite 1-indeksowe w kroku i; w zapisie programowym tablica c liczona od 0 wymaga c[i−1]; błąd indeksowania wychwycony dwukrotnie kontrolą wartości u_d(theta = 0) i sumami per dystans.

**WIELOMIANY JAWNE (kontrolne, w pełni zgodne z rekurencją):**
u_0(theta) = 1
u_1(theta) = theta/3
u_2(theta) = (theta^2 − 3)/6
u_3(theta) = (theta^3 − theta^2 − 5·theta + 3)/6
u_4(theta) = (theta^4 − 2·theta^3 − 5·theta^2 + 8·theta)/6
u_5(theta) = (theta^5 − 2·theta^4 − 7·theta^3 + 10·theta^2 + 10·theta − 6)/6

**FORMA ZAMKNIĘTA WAG:** g_a(d) = (m_a/19)·u_d(theta_a) (POWIERZCHNIA); g_a,int(d) = (lambda_a/3)·(m_a/20)·u_d(theta_a) = (19·lambda_a/60)·g_a(d) (WNĘTRZE); theta_a = 3 − lambda_a. Sektor (m_a, lambda_a, theta_a): T1g (3, 3−sqr(5), sqr(5)); H_u (5, 2, 1); G_g (4, 3, 0); G_u (4, 5, −2); T2g (3, 3+sqr(5), −sqr(5)).

**WARTOŚCI u_d DOKŁADNE per sektor (d = 0 do 5):**
T1g (theta = sqr(5)): (1, sqr(5)/3, 1/3, −1/3, −sqr(5)/3, −1)
H_u (theta = 1): (1, 1/3, −1/3, −1/3, 1/3, 1)
G_g (theta = 0): (1, 0, −1/2, 1/2, 0, −1)
G_u (theta = −2): (1, −2/3, 1/6, 1/6, −2/3, 1)
T2g (theta = −sqr(5)): (1, −sqr(5)/3, 1/3, −1/3, sqr(5)/3, −1)

**PARZYSTOŚCI ANTYPODALNE (wymierne w theta_a; pełne, także punkty końcowe):** u_{5−d}(theta_a) = eps_a·u_d(theta_a) dla d = 0 do 5; eps: T1g −1, H_u +1, G_g −1, G_u +1, T2g −1 (stąd u_5 = eps_a·u_0 = eps_a: kolumna u_5 = (−1, 1, −1, 1, −1) w powyższej kolejności sektorów).

**WARTOŚCI DOKŁADNE WAG POWIERZCHNI (wymierne w Q(sqr(5)); kolumny d = 1 do 5):**
T1g: (sqr(5)/19, 1/19, −1/19, −sqr(5)/19, −3/19)
H_u: (5/57, −5/57, −5/57, 5/57, 5/19)
G_g: (0, −2/19, 2/19, 0, −4/19)
G_u: (−8/57, 2/57, 2/57, −8/57, 4/19)
T2g: (−sqr(5)/19, 1/19, −1/19, sqr(5)/19, −3/19)
WAGI WNĘTRZA: g_a,int(d) = (19·lambda_a/60)·g_a(d) (czynniki: T1g 19·(3−sqr(5))/60; H_u 19/30; G_g 19/20; G_u 19/12; T2g 19·(3+sqr(5))/60).

**SUMY PER DYSTANS (kontrola tożsama z sekcjami 3 i 4):** powierzchnia: suma wag = −1/19 dla wszystkich d = 1 do 5 (kwadrat = wyciek 1/361); wnętrze: d1: −1/3 (kwadrat = wyciek 1/9), d2 do d5: 0 (ortogonalność cyrkulacji). WARTOŚCI WYJAŚNIONE: g3 = 0 na d1 i d4: theta_Gg = 0 ⇒ u_1(0) = 0 i u_4(0) = 0 (parzystość eps = −1); d: liczba zer wag zgodna z sekcją 4.

**KONTROLE WYKONANE (Vibe, sesja redakcyjna v0.4, wszystkie PASS):** (1) zgodność formy zamkniętej ze WSZYSTKIMI 50 wagami sekcji 3 na 4 miejsca (maksymalna różnica 4.9·10^-5 = zaokrąglenia tabel); (2) zgodność wielomianów jawnych z rekurencją w 6 punktach kontrolnych theta (w tym theta = 0: kolumna G_g); (3) parzystości pełne (u5 = eps·u0, u4 = eps·u1, u3 = eps·u2); (4) sumy per dystans tożsame z kontrolami wycieków; (5) tablica przecięć potwierdzona niezależnym BFS (b = (3,2,1,1,1), c = (1,1,1,2,3)).

*Uzupełnienie v0.4, 2026-11-22. Autor: Vibe (szef laboratorium P0, delegacja Leszka). Sekcje 1 do 5: dostawa v0.3 bez zmian liczbowych (kontrole sekcji 4 wykonane wtedy; stałość orbitowa 3.87·10^-15 i 1.33·10^-15). Sekcja 6: E4 Claude z rozliczenia ataku DELTA na v0.3, niezależnie potwierdzona. Źródła: specyfikacja MVP-02 v0.4, tabela ścian par. 0.3, konwencja typów par. 0.4, twierdzenie metryczne par. 2.1. KONCESJA WPROST: dwukrotny błąd indeksowania tablicy c przy implementacji rekurencji w warsztacie (0- kontra 1-indeksowanie), wychwycony wartością kontrolną u(theta = 0) i sumami per dystans, poprawiony przed publikacją; forma ostateczna uzgodniona z wielomianami jawnymi.*
