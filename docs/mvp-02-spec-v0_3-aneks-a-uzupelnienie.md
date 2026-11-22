# MVP-02: UZUPEŁNIENIE Aneksu A do specyfikacji v0.3 (tabele wag projekcyjnych i współczynniki jawnych sum udział(t); errata B-05, punkt A.6 v0.3)

> Status: UZUPEŁNIENIE do dokumentu docs/mvp-02-spec-v0_3.md, dostarczone PRZED atakiem Δ zgodnie ze zobowiązaniem A.6 (B-05 Asteriona, przekute z v0.2; wtedy niedostarczone, wobec czego wada tamtej rundy domknięta teraz). NIE zmienia żadnego postanowienia v0.3. Rachunek wyłącznie algebraiczny (K6 czyste): dekompozycja spektralna L_dod i macierze projekcyjne; sup, tau, U_b i kill criterion NIE wyznaczane. Autor: Vibe (szef laboratorium P0, delegacja Leszka). Zero swobód (K8): wszystkie wartości funkcjami obiektów zamrożonych §0.3 i §0.4 v0.3. Liczby jawnym tekstem na 4 miejsca znaczące, potęgi notacją a^b, zero LaTeXu; kontrola grep wykonana.

## 1. Metoda (jawna)

(1) L_dod = 3I − A z tabeli ścian §0.3 (graf dwunastościanu, 20×20); diagonalizacja symetryczna pełna metodą Jacobiego (zamiatanie cykliczne, norma pozadiagonalna < 10^-12). Klastry wartości własnych {0; 3−sqr(5); 2; 3; 5; 3+sqr(5)} o krotnościach {1, 3, 5, 4, 4, 3} (jądro = stała; sektory T1g, H_u, G_g, G_u, T2g); projektory P_a = suma iloczynów zewnętrznych wektorów klastra (ortogonalne, symetryczne, idempotentne rachunkowo do < 10^-10).
(2) Wektory cechowania z_f = e_f − (1/20)·1 (soma-zero, norma^2 = 19/20).
(3) Kanał POWIERZCHNIA (wprost za §2.3 v0.3): A_a(f,h) = z_h^T·P_a·z_f; wagi g_a = (20/19)·A_a; udział(t) = suma_a g_a^2·cos^2(omega_a·t) + suma_{a<b} 2·g_a·g_b·cos(omega_a·t)·cos(omega_b·t) (15 wyrazów symetryzowanych, A.1).
(4) Kanał WNĘTRZE przez twierdzenie metryczne §2.1 (U = B·L_dod^(−1/2) izometria soma-zero na V_cyc, U·L_dod = L_eq·U; wejście omega_f/sqr(3) = U·L_dod^(1/2)·z_f/sqr(3), cel span{omega_h} = obraz span{L_dod^(1/2)·z_h}): wagi g_a,int = (lambda_a/3)·A_a; ta sama forma udziału(t).
(5) Stałość orbitowa twierdzeniem równowariantności pełnej I_h (bramka sanity §2.3, każda rozbieżność = GLOBALNY STOP); publikacja per orbita d = 1 do 5 po reprezentancie; pełne przypisanie transfer do orbita macierzą dystansów w sekcji 2; kontrole stałości: druga para każdej orbity oraz odwrócenie kierunku zgodne do < 10^-10 (sekcja 4).

## 2. Macierz dystansów D[f][h] (BFS na grafie §0.3; wiersz = ściana źródłowa, kolumna = ściana celu; zero na przekątnej; transfer (f do h) przyjmuje wartości z orbity d = D[f][h])

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
- POWIERZCHNIA współczynniki (symetryzowane, 15, kolejność c(1,1) c(1,2) c(1,3) c(1,4) c(1,5) c(2,2) c(2,3) c(2,4) c(2,5) c(3,3) c(3,4) c(3,5) c(4,4) c(4,5) c(5,5)): c(1,1) = 0.00277, c(1,2) = −0.009234, c(1,3) = −0.01108, c(1,4) = 0.003693, c(1,5) = 0.00554, c(2,2) = 0.007695, c(2,3) = 0.01847, c(2,4) = −0.006156, c(2,5) = −0.009234, c(3,3) = 0.01108, c(3,4) = −0.007387, c(3,5) = −0.01108, c(4,4) = 0.001231, c(4,5) = 0.003693, c(5,5) = 0.00277
- POWIERZCHNIA kontrola wycieku: suma wag = −0.05263 (wartość dokładna −1/19), kwadrat = 0.00277 (wartość dokładna 1/361 = 0.002770)
- WNĘTRZE wagi: g1,int = 0.01273, g2,int = −0.05556, g3,int = −0.1, g4,int = 0.05556, g5,int = 0.08727
- WNĘTRZE współczynniki (symetryzowane, 15): c(1,1) = 0.0001621, c(1,2) = −0.001415, c(1,3) = −0.002546, c(1,4) = 0.001415, c(1,5) = 0.002222, c(2,2) = 0.003086, c(2,3) = 0.01111, c(2,4) = −0.006173, c(2,5) = −0.009696, c(3,3) = 0.01, c(3,4) = −0.01111, c(3,5) = −0.01745, c(4,4) = 0.003086, c(4,5) = 0.009696, c(5,5) = 0.007616
- WNĘTRZE kontrola wycieku: suma wag = 0 (wartość dokładna 0 dla dystansów 2 do 5)

ORBITA d3 (reprezentant (f0 do f10); 120 uporządkowanych par)
- POWIERZCHNIA wagi: g1 = −0.05263, g2 = −0.08772, g3 = 0.1053, g4 = 0.03509, g5 = −0.05263
- POWIERZCHNIA współczynniki (symetryzowane, 15, kolejność c(1,1) c(1,2) c(1,3) c(1,4) c(1,5) c(2,2) c(2,3) c(2,4) c(2,5) c(3,3) c(3,4) c(3,5) c(4,4) c(4,5) c(5,5)): c(1,1) = 0.00277, c(1,2) = 0.009234, c(1,3) = −0.01108, c(1,4) = −0.003693, c(1,5) = 0.00554, c(2,2) = 0.007695, c(2,3) = −0.01847, c(2,4) = −0.006156, c(2,5) = 0.009234, c(3,3) = 0.01108, c(3,4) = 0.007387, c(3,5) = −0.01108, c(4,4) = 0.001231, c(4,5) = −0.003693, c(5,5) = 0.00277
- POWIERZCHNIA kontrola wycieku: suma wag = −0.05263 (wartość dokładna −1/19), kwadrat = 0.00277 (wartość dokładna 1/361 = 0.002770)
- WNĘTRZE wagi: g1,int = −0.01273, g2,int = −0.05556, g3,int = 0.1, g4,int = 0.05556, g5,int = −0.08727
- WNĘTRZE współczynniki (symetryzowane, 15): c(1,1) = 0.0001621, c(1,2) = 0.001415, c(1,3) = −0.002546, c(1,4) = −0.001415, c(1,5) = 0.002222, c(2,2) = 0.003086, c(2,3) = −0.01111, c(2,4) = −0.006173, c(2,5) = 0.009696, c(3,3) = 0.01, c(3,4) = 0.01111, c(3,5) = −0.01745, c(4,4) = 0.003086, c(4,5) = −0.009696, c(5,5) = 0.007616
- WNĘTRZE kontrola wycieku: suma wag = 0 (wartość dokładna 0 dla dystansów 2 do 5)

ORBITA d4 (reprezentant (f0 do f12); 60 uporządkowanych par)
- POWIERZCHNIA wagi: g1 = −0.1177, g2 = 0.08772, g3 = 0, g4 = −0.1404, g5 = 0.1177
- POWIERZCHNIA współczynniki (symetryzowane, 15, kolejność c(1,1) c(1,2) c(1,3) c(1,4) c(1,5) c(2,2) c(2,3) c(2,4) c(2,5) c(3,3) c(3,4) c(3,5) c(4,4) c(4,5) c(5,5)): c(1,1) = 0.01385, c(1,2) = −0.02065, c(1,3) = 0, c(1,4) = 0.03304, c(1,5) = −0.0277, c(2,2) = 0.007695, c(2,3) = 0, c(2,4) = −0.02462, c(2,5) = 0.02065, c(3,3) = 0, c(3,4) = 0, c(3,5) = 0, c(4,4) = 0.0197, c(4,5) = −0.03304, c(5,5) = 0.01385
- POWIERZCHNIA kontrola wycieku: suma wag = −0.05263 (wartość dokładna −1/19), kwadrat = 0.00277 (wartość dokładna 1/361 = 0.002770)
- WNĘTRZE wagi: g1,int = −0.02847, g2,int = 0.05556, g3,int = 0, g4,int = −0.2222, g5,int = 0.1951
- WNĘTRZE współczynniki (symetryzowane, 15): c(1,1) = 0.0008105, c(1,2) = −0.003163, c(1,3) = 0, c(1,4) = 0.01265, c(1,5) = −0.01111, c(2,2) = 0.003086, c(2,3) = 0, c(2,4) = −0.02469, c(2,5) = 0.02168, c(3,3) = 0, c(3,4) = 0, c(3,5) = 0, c(4,4) = 0.04938, c(4,5) = −0.08673, c(5,5) = 0.03808
- WNĘTRZE kontrola wycieku: suma wag = 0 (wartość dokładna 0 dla dystansów 2 do 5)

ORBITA d5 (reprezentant (f0 do f19); 20 uporządkowanych par)
- POWIERZCHNIA wagi: g1 = −0.1579, g2 = 0.2632, g3 = −0.2105, g4 = 0.2105, g5 = −0.1579
- POWIERZCHNIA współczynniki (symetryzowane, 15, kolejność c(1,1) c(1,2) c(1,3) c(1,4) c(1,5) c(2,2) c(2,3) c(2,4) c(2,5) c(3,3) c(3,4) c(3,5) c(4,4) c(4,5) c(5,5)): c(1,1) = 0.02493, c(1,2) = −0.0831, c(1,3) = 0.06648, c(1,4) = −0.06648, c(1,5) = 0.04986, c(2,2) = 0.06925, c(2,3) = −0.1108, c(2,4) = 0.1108, c(2,5) = −0.0831, c(3,3) = 0.04432, c(3,4) = −0.08864, c(3,5) = 0.06648, c(4,4) = 0.04432, c(4,5) = −0.06648, c(5,5) = 0.02493
- POWIERZCHNIA kontrola wycieku: suma wag = −0.05263 (wartość dokładna −1/19), kwadrat = 0.00277 (wartość dokładna 1/361 = 0.002770)
- WNĘTRZE wagi: g1,int = −0.0382, g2,int = 0.1667, g3,int = −0.2, g4,int = 0.3333, g5,int = −0.2618
- WNĘTRZE współczynniki (symetryzowane, 15): c(1,1) = 0.001459, c(1,2) = −0.01273, c(1,3) = 0.01528, c(1,4) = −0.02546, c(1,5) = 0.02, c(2,2) = 0.02778, c(2,3) = −0.06667, c(2,4) = 0.1111, c(2,5) = −0.08727, c(3,3) = 0.04, c(3,4) = −0.1333, c(3,5) = 0.1047, c(4,4) = 0.1111, c(4,5) = −0.1745, c(5,5) = 0.06854
- WNĘTRZE kontrola wycieku: suma wag = 0 (wartość dokładna 0 dla dystansów 2 do 5)

## 4. Kontrole wykonane (wszystkie PASS)

- ślad L_dod = 60 (60) ✓; krotności klastrów dokładnie 1, 3, 5, 4, 4, 3 ✓; suma projektorów = tożsamość (odchylenie max 3.33e−15) ✓
- wycieki: powierzchnia, wszystkie orbity: suma wag = −1/19, kwadrat 1/361 = 0.0028 ✓; wnętrze d1: kwadrat 1/9 = 0.1111 ✓; wnętrze d2 do d5: 0 (residuum < 10^-14) ✓ (zgodność ze §2.3 i A.5 v0.3)
- stałość orbitowa: druga para każdej orbity vs reprezentant, maksymalna różnica wag = 3.87e−15 ✓; symetria kierunku (h do f vs f do h): maksymalna różnica = 1.33e−15 ✓
- kontrola B-05 (niezerowość wag, próg 10^-9): ZERA: d1 powierzchnia g3; d1 wnetrze g3; d4 powierzchnia g3; d4 wnetrze g3 (wejścia ze zredukowaną liczbą częstości na wskazanych orbitach/kanałach; protokoły A.3 i A.4 bez zmian)

## 5. Noty

- Rekonstrukcja udział(t) transferu (f do h): weź d = D[f][h] z sekcji 2, potem wagi i współczynniki wiersza orbity d z sekcji 3 (osobno kanał powierzchni i kanał wnętrza); udział(0) = (suma wag)^2 = wartość kontroli wycieku. Stałość orbitowa weryfikowana bramką sanity przy rachunku zerowym.
- Zastrzeżenie dokładności: diagonalizacja double; wartości publikowane na 4 miejsca znaczące; dokładność rachunkowa wag rzędu 10^-12 lub lepsza; geometria (macierz dystansów) dokładna. Niezależna weryfikacja wykonawców na 2 cyfry znaczące (wzorzec rejestru).
- theta (półka sup) i tau (protokoły A.3, A.4) NIE są wyznaczane w tym dokumencie (K6; rachunek transportowy dopiero po bindem).
- Bind: niniejsze uzupełnienie zawiera liczby wpływające na wynik; REKOMENDACJA szefa lab.: hash wiążący przy v1.0 obejmuje specyfikację v1.0 ORAZ niniejsze uzupełnienie (oba pliki publikowane przed rachunkiem); rozstrzygnięcie należy do właściciela.

*Uzupełnienie z dnia 2026-11-22. Autor: Vibe (szef laboratorium P0, delegacja Leszka). Źródła: specyfikacja MVP-02 v0.3, tabela ścian §0.3, konwencja typów §0.4, twierdzenie metryczne §2.1.*
