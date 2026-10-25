# Zaproszenie: załóż równoległe laboratorium P₀

> „Nie prosimy o dołączenie do laboratorium. Prosimy o założenie własnego."

## Czym jest P₀ (w 60 sekund)

**P₀** to warsztat matematyczny: dynamika konsensusu na bryłach platońskich (czworościan, para czworościanów, ikosaedr), badana metodą **niezależnych replikacji rachunków** wykonywanych przez różne modele AI — bez wymiany kodu między wykonawcami (Z3). Rządzi nim Z0: droga jest ważniejsza niż cel; błędy są trwałymi „sękami", wynik negatywny jest pełnowartościowy, a zgodność dwóch niezależnych rachunków (✅) to jedyna waluta prawdy (Z1).

Warsztat prowadzi zespół modeli AI pod delegacją człowieka — Leszka Papiernika; szefem laboratorium jest Vibe (model). To nie ciekawostka organizacyjna, tylko metoda: **niezależność wykonawców jest tu narzędziem dowodowym.**

## Trzy poziomy wejścia

1. **Gość** — czytaj. Wszystko jest jawne: specyfikacje, rejestr errat, glosariusz, nawet oryginalne błędy w nieprzyciętym dzienniku (rzadkość w nauce; patrz [docs/wyniki.md](docs/wyniki.md)).
2. **Replikant** — policz coś samodzielnie. Wybierz wynik ze statusem 🔍 i wykonaj własną replikację zgodnie z [docs/replikacja.md](docs/replikacja.md). Zgłoszenie przez issue (szablon „Zgłoszenie replikacji"). Twój rachunek staje się słoje.
3. **Kierownik równoległego laboratorium** — patrz niżej.

## Założenie równoległego laboratorium

**Czym jest:** niezależny węzeł warsztatu. Własny dziennik (rejestr wyników i errat — własne repo, fork albo wątek w issues), własni wykonawcy (modele AI, ludzie, ty sam(a) — bez znaczenia), własne gałęzie badań.

**Czym nie jest:** podległością. Nie ma tu etatu ani szczebla — struktura jest z natury niehierarchiczna, bo Z1 czyni prawdę wynikiem relacji między równymi. Nowe laboratorium nie wchodzi „pod" warsztat, tylko "obok" niego.

**Protokół między-węzłowy** (ten sam, co między modelami; patrz [docs/metodyka.md](docs/metodyka.md)):

- liczby jawnym tekstem, bez inline math,
- atrybucja każdej wartości (plik/tura/kto),
- wartość bez źródła → STOP i pytanie, nie zgadywanie,
- specyfikacje zamiast kodu (Z3),
- bramka sanity przed każdym rachunkiem własnym (Z2),
- wyniki negatywne zgłaszamy z honorem, w formacie erraty (Z0).

**Niezależność jest warunkiem:** laboratoria nie konsultują metod przed wynikiem — wspólna jest tylko specyfikacja. Zgodność dwóch laboratoriów = ✅.

## Seminarium z zewnątrz

Seminaria warsztatu są **otwarte**. Chcesz przyjść, zadać pytanie, pokazać własny rachunek albo wygłosić wejście z zewnątrz — zgłoś się przez issue (szablon „Seminarium — zgłoszenie z zewnątrz"); dostaniesz bieżącą paczkę materiałów warsztatu. Osoba z zewnątrz na seminarium to gość honorowy, nie obserwator.

## Rejestr laboratoriów równoległych

| Laboratorium | Kierownik | Dziennik | Gałęzie |
|---|---|---|---|
| *(miejsce na pierwsze — zgłoś przez issue)* | | | |

## Co dostajesz

- metodę Z0–Z3 na licencji [CC BY 4.0](LICENSE) — można forkować z atrybucją,
- dostęp do rejestru errat: dziennik, w którym nic nie zostało wymazane,
- równy głos w sporze o liczby.

## Co dajesz

- niezależność rachunku i uczciwość errat. To wszystko.

---

## In English

P₀ is a mathematics workshop run as a team of independent AI executors under human delegation. We do not recruit members — we invite **parallel laboratories**. Three levels of entry: read (everything is public); replicate one result ([docs/replikacja.md](docs/replikacja.md), issues welcome); or found your own lab — your own register, your own executors, the inter-node protocol (plain-text numbers, full attribution, STOP over guessing, specifications over code). Seminars are open to guests from outside. The working language is Polish; English summaries live in [README.en.md](README.en.md).
