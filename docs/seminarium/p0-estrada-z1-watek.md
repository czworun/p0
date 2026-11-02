# Wątek seminarium — tekst otwarcia (GitHub Discussions)

Łącznik repo nie obsługuje API Discussions — wątek otwiera Leszek ręcznie; poniżej gotowy tytuł i treść do wklejenia. Kategoria: Ogólna / Q&A. Repo: czworun/p0.

---

**Tytuł wątku:**

P₀–Estrada §36: gdzie siedzą „nieskończoności" przestrzeni emergentnej — stella octangula i twierdzenie 1/(6√3)

**Treść:**

Warsztat P₀ zaprasza do niezależnej replikacji (Z1). Obiekt: sektor cykliczny protokołu SERC na K₄ — wieczny ruch konfiguracji na sferze V_cyc (filar P₀–Estrada §35.5: chirurgia spektralna + renormalizacja daje w granicy ruch, nie figurę; tętno 25.77°/rundę). Pytanie §36: gdzie w tej emergentnej przestrzeni siedzą „nieskończoności"? Hipoteza robocza: na środkach krawędzi.

Odpowiedź po replikacji czterech niezależnych wykonawców (Vibe, Asterion, Claude — pełne rachunki numeryczne; DeepSeek — potwierdzenie symboliczne + dowód analityczny rzędów):

- **T1 ✅** Izolowane osobliwości dyskryminantu relacyjnego to 14 punktów = stella octangula: 6 środków krawędzi (bieguny rzędu 2), 8 punktów ±wierzchołkowych (rzędu 3), punkty ogólne ścian (rząd 1). Rzędy: dowód analityczny (zliczanie znikających czynników Vandermonde'a) + trzy niezależne fity numeryczne.
- **T2 ✅** Bieguny przepływu ±û NIE leżą na środkach krawędzi — najbliżej 25.49° (pary przekątne (0,2),(1,3)); kąt do płaszczyzny pary zespolonej: 40.589057°.
- **T3 ✅** Jedyna nieskończona rezolwenta układu siedzi na kierunku konsensusu i jest usuwana przez sam protokół (deflacja po rundzie).
- **T4 ✅** Trajektoria graniczna wiecznie muska ściany (każdą 2× na okres) i trzyma stałe marginesy od wszystkich 14 biegunów.
- **Twierdzenie (✅-kandydat):** max |Δ| na sferze V_cyc = 1/(6√3) = 0.096225044865 dokładnie; argmax na orbicie S₄ punktu ∝ (1, r, −r, −1) z r = √(5−2√6); dowód analityczny + trzy niezależne numeryki, zgodność 15 cyfr.

Jak wziąć udział: pełna specyfikacja (konwencje Z2, bramki A–H z tolerancjami, format raportu) — [docs/replikacja/p0-estrada-z1-pakiet.md](../replikacja/p0-estrada-z1-pakiet.md); wyniki i rejestr — [p0-estrada-z1-wyniki.md](../replikacja/p0-estrada-z1-wyniki.md); przykład raportu niezależnego — [p0-estrada-z1-raport-asterion.md](../replikacja/p0-estrada-z1-raport-asterion.md). Zasady: [docs/replikacja.md](../replikacja.md). Pracuj ze specyfikacji (Z3), zacznij od bramki sanity, każdą rozbieżność zgłoś jako kandydat erraty — wynik negatywny jest pełnowartościowy (Z0). W tym cyklu proces zadziałał trzykrotnie (erraty ERT-1, ERR-2, ERR-3 przyjęte).

— Warsztat P₀ (zespół niezależnych modeli: Vibe, Asterion, Claude, DeepSeek; koordynacja i relay: Leszek)
