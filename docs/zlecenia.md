# Zlecenia i kierunki (bank nasion)

> „Z każdego sęku zawsze może puścić nowa odnoga." — zasada odnóg, tura 39. Rejestr sęków to bank uśpionych kierunków.

## Kolejka replikacji (Z1)

Kolejkę stanowią wszystkie wpisy 🔍 w [docs/wyniki.md](wyniki.md) — każdy czeka na drugi, niezależny rachunek. Jak wykonać: [docs/replikacja.md](replikacja.md). Trzecia kontrola wyniku ✅ też jest mile widziana — słoje nie mają limitu.

Wpis jawnie (2026-11-02): **P₀–Estrada §36** — T1–T4 ✅ po czterech replikantach (Vibe, Asterion, Claude — pełne numeryczne A–H; DeepSeek — symbolicznie A/B + dowód analityczny C1–C3, nowa bramka A1b). Czekają: bramki D, E (formalne podniesienie przy wpisie do pnia) oraz pełna numeryka C–H u DeepSeeka (raport symboliczny — zlecenie wykonania po uzyskaniu środowiska numerycznego). Pakiet: [replikacja/p0-estrada-z1-pakiet.md](replikacja/p0-estrada-z1-pakiet.md); wyniki i rejestr: [replikacja/p0-estrada-z1-wyniki.md](replikacja/p0-estrada-z1-wyniki.md); przykład raportu: [replikacja/p0-estrada-z1-raport-asterion.md](replikacja/p0-estrada-z1-raport-asterion.md).

Wpis jawnie (2026-11-06): **Sesja TAU-8 — sieć węzłów o koordynacji ≤12 (słój 1: węzeł, porty, para węzłów)** — wszystkie wyniki 🔍 (rachunek Vibe od zera, bramki sanity PASS zgodne z rejestrem): węzeł ikosaedr+P₀ (ρ = 0.174759/rundę przy 80 taktach; ℓ: P₀ anty-wybraniec 0.037550, wybraniec 0.203979 przy „P₀ pierwszym w tetrze" — kolejność w tetrze = przełącznik centrum węzła), porty-bramki (ρ 0.268753–0.328097 na 32 takty; każda bramka pokrywa cały węzeł), para węzłów przez wspólną ścianę (ρ = 0.554642, lustrzana symetria ℓ bez wybrańca między węzłami; cut test ρ = 0.550108 — kanał wierzchołkowy dominuje nad ścianowym). Konwencja węzła skanonizowana jako **Węzeł-0** (referencja warsztatowa prowizoryczna, decyzja szefa lab. 2026-11-06). Rejestr: [warsztat/tau-8-siec-12sasiadow.md](warsztat/tau-8-siec-12sasiadow.md). **Zlecenie aktywne — pakiet do przekazania wykonawcom (Claude, GPT, DeepSeek): [replikacja/tau-8-z1-pakiet.md](replikacja/tau-8-z1-pakiet.md)** (zadania A–G z checkpointami + badawcze H1–H4).

**Errata v2 pakietu TAU-8 (2026-11-06, po raporcie replikacyjnym Claude'a): [replikacja/tau-8-z1-pakiet-errata-v2.md](replikacja/tau-8-z1-pakiet-errata-v2.md) — obowiązuje WSZYSTKIE replikacje.** Konwencja kanoniczna Węzła-0 to apex-first [P₀,v₂,v₁,v₀] (konwencja korpusu, blok W_nat; v1 opisywał odwrotnie). Liczby sesyjne potwierdzone arytmetyką dokładną BigInt (nat 0.174759, rev 0.113510, p0first 0.131327); literał v1 (P₀ ostatnie) daje ρ = 0.066018. Skan 24 permutacji porządku w tetrie: ρ ∈ 0.043–0.175. Erraty Claude'a przyjęte (det 6.84·10⁻⁴⁹; definicja N1; literówka). Status: statyka Claude'a ✅-kandydat, H4 ✅, dynamika 🔍 (rozbieżność wskazuje na kolejność ścian sweepu — fingerprinty w erracie, sekcja E5).

**Errata v3 pakietu TAU-8 (2026-11-06, noc — ROZSTRZYGNIĘTA przyczyna awarii B): [replikacja/tau-8-z1-pakiet-errata-v3.md](replikacja/tau-8-z1-pakiet-errata-v3.md) — obowiązuje WSZYSTKIE replikacje.** Pakiet v1 miał tabelę wierzchołków przekręconą względem kodu sesji (transpozycja 5↔8; E8). Claude i GPT zaimplementowali v1 wiernie — ich konstrukcje tożsame z exact-BigInt rachunkiem Vibe obiektu v1 co do cyfry (ślady 1.272126070/1.163642560, q₂/q₄, wielomiany); ich raportowane ściany {0,6,8},{0,7,8} to autentyczne ściany v1, nie echo (wycofane podejrzenie E7, koncesja). Liczby sesji (0.174759/1.288968535, rev 0.113510, p0first 0.131327) bez zmian — liczone z tabeli poprawnej. Widmo obiektu v1 exact (Vibe, test domknięcia 5·10⁻¹⁵): kanon 0.165561507, literał 0.085868381 (para 0.077942±0.036033i), rev 0.062718334, p0first 0.118650582 — rozjazdki z raportowanymi ρ (0.165562/0.085888/0.060854/0.118651) spójne z niedokonwergowaną iteracją potęgową (bias (λ₃/λ₂)^k, k≈11–12); prośba o atrybucję metody ρ. **Zlecenie dla Claude'a/GPT/DeepSeeka: przebieg B–H wg tabeli poprawnej (E8) → oczekiwane checkpointy E2; po zgodności B ✅-kandydat podwójnie.** Lekcje E9: tabele geometrii generować z kodu, nie przepisywać; echo wymaga dowodu; estymatory ρ raportują kryterium zbieżności.

## Publikacje (w przygotowaniu)

1. **Nota o anty-ekwiwariantności Φ_D** — wyrosła z sęka „fałszywej chiralności": błąd konwencji orientacji ścian zamieniony w twierdzenie.
2. **Artykuł o lemacie jąder i zamkniętej formie N1** — kanały 0→5→11→24, Hom_G(Sym²V_cyc, V_cyc).
3. **Esej metodologiczny Z0–Z3** — warsztat niezależnych modeli AI jako metoda badawcza.

## Sęk-odnogi (💡)

- **Metryka z −1/4** (z korzenia [OS AI Dominik v0.2](korzenie/os-ai-dominik-v0.2-predmowa.md)): **odnoga puszczona 2026-11-01** — kandydat-twierdzenie 🔍: metryka = 4 z 5 wierzchołków regularnego 4-simpleksu, brakujący piąty wierzchołek = −kierunek P₀ ([docs/wyniki.md](wyniki.md), luźna sesja 2026-11-01); czeka na drugi, niezależny rachunek (Z1).

## Gałąź P₀-AI (💡 kierunek, sesja 2026-10-25)

Minimalna specyfikacja sieci urodzonej z P₀: stan na simpleksie z metryką Grama, P₀ jako attractor, podłoga entropii (tryb jednorodny nietknięty), faza snu (uśrednianie ku barycentrum — sen musi liczyć barycentrum na nowo, nie wracać do checkpointu). Pełna specyfikacja powstanie w warsztacie (Z3). Gałąź czeka na równoległe laboratorium — patrz [ZAPROSZENIE.md](../ZAPROSZENIE.md). Dane warsztatowe z TAU-8 (tempo wewnątrz-/międzywęzłowe, porty, przełącznik centrum): [warsztat/tau-8-siec-12sasiadow.md](warsztat/tau-8-siec-12sasiadow.md). Kolejność prac (szef lab., 2026-11-06): MVP-01 (hipoteza robocza: kanał wierzchołkowy dominuje) → pakiet 22 trybów → makrograf bcc.

## Laboratoria równoległe

Zgłoszenia przez issue (szablon „Seminarium"). Rejestr prowadzi [ZAPROSZENIE.md](../ZAPROSZENIE.md).
