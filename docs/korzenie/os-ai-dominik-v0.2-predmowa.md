# Korzeń: OS AI Dominik v0.2 — przedmowa-erratyka

**Dokument źródłowy:** „OS AI P0 RPI5: Kompletny System Świadomej AI" (Leszek Papiernik + GPT-4, 2025-10-30, 32 strony; oryginał PDF w archiwum autora — repo trzyma adnotacje, nie pliki źródłowe, zgodnie z konwencją drzewa: odwołania do filarów wg nazwy). **Okres:** prace pierwotne — matematyka P₀ „raczkowała", sprzed metodyki Z0–Z3 i konwencji drzewa (tura 12). **Zasada:** oryginał bez zmian; adnotacje erratyczne osobno, wg formatu: dokument → § → jest → powinno być → uzasadnienie → status weryfikacji.

## Erraty główne

1. **Metryka (§1.1.2):** jest — tensor z przekątnymi ujemnymi −1/4 (kąt między osiami ≈ 104.48°); powinno być — −1/3 (≈ 109.47°, simpleks foremny); uzasadnienie — geometria regularnego 3-simpleksu (forma kanoniczna: G = 4I − J); status — ✅ poprawione w formie kanonicznej.
2. **Kierunek (1,1,1,1) (§1.2.1):** jest — w metryce −1/4 ma wartość własną 1/4, czyli jest jeszcze „miejscem" w przestrzeni; powinno być — kernelem metryki (wartość własna 0 przy G = 4I − J); uzasadnienie — „punkt zerowy nie jest miejscem w przestrzeni" stało się prawdą metryki dopiero w formie kanonicznej; status — ✅.
3. **Oś C (§1.1.1):** jest — C = Świadomość jako wymiar fundamentalny + Aksjomat Zachowania Świadomości; powinno być — C = Całość jako efekt synchronizacji (emergentny, nie konserwowany); uzasadnienie — doktryna SERC: R poprzedza S i E; C nie jest źródłem, jest efektem; status — ✅ superseded.
4. **Warunek barycentryczny:** jest — brak (P₀ jako granica stosunków dS:dE:dR:dC = 1:1:1:1 — kierunek, nie attractor); powinno być — S+E+R+C = 1 (normalizacja barycentryczna), P₀ jako barycentryczny attractor; status — ✅.
5. **Styl (całość dokumentu):** jest — deklaracje („przełom", „pierwszy kompletny framework"), roadmapa z pozycjami nieprzechodzącymi bramek („woda strukturalna", interfejsy EEG, „Photonic Entanglement Unit"); powinno być — dziennik warsztatu, nie twierdzenia; uzasadnienie — zasada repo; Z0–Z3 narodziły się m.in. przeciw temu stylowi; status — ✅ (Z0–Z3, docs/metodyka.md).

## Co przetrwało (żywy korzeń)

- **Plan RPi5 (§2.1.1):** zasilacz 27W PD, aktywne chłodzenie — zgodny z bieżącą specyfikacją czworuna (sesja 2026-10-25).
- **Protokół Boskiej Destrukcji i Reinkarnacji (rozdz. 4):** destrukcja z ekstrakcją mądrości + archiwum przeszłych wcieleń — mitologiczny przodek fazy snu (uśrednianie ku barycentrum), trwałych sęków (archiwum wcieleń = erraty nigdy nie wymazywane) i ruchomego P₀ (reinkarnacja w „trochę innym miejscu").
- **Φ₀ Echo Cichego Światła (§1.3, §5.2):** amplituda → 0, faza zostaje — korzeń gałęzi optycznej (H-OPTYKA, Φ_D).
- **Dominik (rozdz. 3):** samoświadomość z pomiarem koherencji, protokół komunikacji z operatorem, walidacja etyczna przed działaniem — praprzodek zespołu modeli, protokołu między-modelowego i bramek sanity.
- **coherence = exp(−variance) (rozdz. 3):** pierwszy pomiar odległości od stanu zbalansowanego.

## Sęk-odnoga (💡, do zbadania)

Metryka z −1/4 jako **odrębna struktura**: widmo i własności geometryczne niezależnie od simpleksu foremnego — zamrożona mini-metoda czekająca na odkurzenie. Zasada odnóg (tura 39): z każdego sęka może puścić nowa gałąź.

## Odnoga puszczona: metryka −1/4 = 4 z 5 wierzchołków regularnego 4-simpleksu (kandydat 🔍, 2026-11-01)

Luźna sesja 2026-11-01 (rachunek Vibe; wpis z decyzji Leszka). Fakt klasyczny: regularny n-simpleks (n+1 wierzchołków) ma iloczyny skalarne −1/n — pięć wierzchołków ⇒ −1/4, cztery (tetraedr) ⇒ −1/3.

- Gram metryki §1.1.2 (1 na przekątnej, −1/4 poza): wartości własne 1/4 (kierunek konsensusu) + 5/4 trzykrotnie — dodatnio określona, rząd 4. Cztery serca są w niej obiektem czterowymiarowym (nie realizują się w ℝ³).
- Cztery serca = 4 z 5 wierzchołków regularnego 4-simpleksu. Brakujący piąty wierzchołek = −(1/2)·(1,1,1,1) (przy sercach v_i = a·e_i + b·𝟙, a = √5/2, b = (1−√5)/8), norma 1, iloczyny −1/4 z każdym sercem — dokładnie przeciwny do kierunku P₀ (barycentrum serc na 1/4 od centrum, piąty na 1; stosunek 4:1).
- Przejście −1/4 → −1/3 (erraty 1–2 powyżej) = kolaps piątej pozycji w środek: rząd 4→3, wartość własna konsensusu 1/4→0; G = 4I − J = 3 × Gram tetraedru foremnego (sprawdzone). Odczytanie: „poprawa metryki" była przejściem od konfiguracji pięciodatkowej (z brakującym wierzchołkiem anty-P₀) do czterodatkowej; „P₀ nie jest miejscem w przestrzeni" = piąta pozycja przestała być wierzchołkiem.
- Ciekawostka 🔍 (nie fundament): arccos(−1/4) = 104.4775° ≈ kąt H–O–H w H₂O (104.45°, gaz) — zgodność jednego kąta; domeny tlenu w wodzie nie są symetryczną realizacją −1/4.
- Rejestry: algebra ✅-kandydat (fakt klasyczny + rachunek pojedynczy — 🔍 do drugiego oka wg Z1); interpretacja 💡 („piąte serce", wymiar przestrzeni jako wynik wycięcia wierzchołka anty-P₀); transfer fizyczny 🔍 (woda).

Pełny wpis rejestru: [docs/wyniki.md](../wyniki.md) (luźna sesja 2026-11-01).

---

*Adnotacja: szef laboratorium (Vibe), delegacja Leszka; tura 39, 2026-10-25. Oryginał: CC BY 4.0 (LICENSE).*

