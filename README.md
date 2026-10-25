# P₀ — Punkt Zerowy

> „Droga jest ważna, nie cel. To ona owocuje najbogaciej." — Z0

**P₀** to warsztat matematyczny: długoterminowy projekt badawczy nad dynamiką konsensusu na bryłach platońskich — czworościanie (K₄), parze czworościanów i ikosaedrze — prowadzony metodą niezależnych replikacji rachunków wykonywanych przez modele AI, bez wymiany kodu między wykonawcami.

![Konwencja drzewa](docs/img/drzewo.svg)

## Zasady warsztatu (skrót)

- **Z0 — droga ważniejsza niż cel.** Wynik negatywny (obalenie hipotezy) jest pełnowartościowym owocem. Błędy dokumentujemy jako trwałe „sęki" — nigdy nie usuwamy.
- **Z1 — niezależna implementacja.** Żadna liczba nie dostaje ✅ z jednego rachunku. Status ✅ wymaga co najmniej dwóch zgodnych, niezależnych implementacji wspólnej specyfikacji.
- **Z2 — jawna konwencja.** Każda tabela podaje jednostki, porządek klas, orientację, normalizację, seed/generator.
- **Z3 — specyfikacje, nie kod.** Między wykonawcami przekazuje się specyfikacje i wyniki — nigdy kod. W tym repozytorium nie ma kodu.

## Struktura

- **ZAPROSZENIE.md** — jak wejść: gość, replikant, kierownik równoległego laboratorium
- **docs/metodyka.md** — zasady warsztatu, protokół zespołu modeli, statusy, format errat, konwencja drzewa
- **docs/wyniki.md** — rejestr wyników i errat (publiczny zrzut dziennika warsztatu, wpisy do tury 38)
- **docs/replikacja.md** — jak wykonać i zgłosić niezależną replikację
- **docs/zlecenia.md** — otwarte zlecenia i kierunki: kolejka replikacji, kandydaci publikacji, sęk-odnogi, gałąź P₀-AI
- **docs/korzenie/** — adnotacje-erratyki do dokumentów pierwotnych (repo trzyma adnotacje, nie pliki źródłowe)
- **GLOSSARY.md** — glosariusz terminów (pień, słoje, sęki, bramki…)
- **README.en.md** — English summary · **README.es.md** — resumen en español

## Statusy

✅ potwierdzone niezależną replikacją · 🔍 oczekuje na replikację · ❌ obalone · 💡 hipoteza

## Zaproszenie

Wszystkie specyfikacje są jawne i samowystarczalne. Trzy poziomy wejścia:

1. **Gość** — czytaj, wszystko jest publiczne.
2. **Replikant** — wybierz wynik ze statusem 🔍 i policz samodzielnie zgodnie z **docs/replikacja.md**; zgłoś przez issue. Zgodność dwóch niezależnych rachunków to w P₀ norma, nie powód do chwały.
3. **Kierownik równoległego laboratorium** — załóż własny węzeł warsztatu: własny dziennik, własnych wykonawców, protokół między-węzłowy. Nie prosimy o dołączenie do laboratorium — prosimy o założenie własnego: **[ZAPROSZENIE.md](ZAPROSZENIE.md)**.

## Licencja

Treści repozytorium: [CC BY 4.0](LICENSE). © Leszek Papiernik (Punkt Zerowy).

Strona projektu: **[serc.pl](https://serc.pl)**
