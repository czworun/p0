# A-05 — błędne odnośniki do tabeli filarów

**Data:** 2026-11-21  
**Repozytorium:** `czworun/p0`  
**Benchmark:** `main` @ `ff5345f50f509ff95fafcd1e4b28ce64b388eb1c`

## Ustalenie

W sześciu dokumentach korzeni występuje aktywny odnośnik Markdown do `PILLARS-TABLE.md`, podczas gdy rzeczywisty plik w repozytorium na benchmarku to `docs/korzenie/PILLARS-TABLE-1.md`.

| Dokument | Wystąpienia aktywnego odnośnika |
|---|---:|
| `P0-Alchemy-v0_4_4-alpha.md` | 1 |
| `P0-Scalar-v0_3_5.md` | 1 |
| `P0-Wave-v0_6_1.md` | 1 |
| `P0_Applications_v0_5_2.md` | 2 |
| `P0_Experiments_v0_3_2.md` | 1 |
| `P0_Philosophy_v0_6_2.md` | 2 |
| **Razem** | **8** |

Wszystkie wskazują względnym adresem `PILLARS-TABLE.md` na plik o tej nazwie w katalogu `docs/korzenie/`. Takiego pliku nie ma; nazwa istniejącego pliku zawiera sufiks `-1`.

## Rozróżnienie

To nie jest tylko wzmianka tekstowa ani nieaktywna nazwa w adnotacji. Wskazane osiem wystąpień ma postać linków Markdown `[...](PILLARS-TABLE.md)`. Przy kliknięciu prowadzą do nieistniejącej ścieżki.

## Wpływ

- Uszkodzony jest nawigacyjny punkt wejścia do źródła architektury i wersji.
- Problem dotyczy sześciu korzeni, a nie wszystkich dokumentów repo.
- Sama tabela zawiera dodatkowo historyczne samoodniesienia tekstowe do nazwy bez sufiksu; nie należy ich mylić z tymi ośmioma aktywnymi linkami.

## Proponowana korekta

Po zatwierdzeniu przez właściciela korpusu ujednolicić nazwę: albo zmienić odnośniki na istniejący plik `PILLARS-TABLE-1.md`, albo — jeśli taka jest decyzja architektoniczna — zmienić nazwę pliku i zaktualizować wszystkie odwołania. Nie robię żadnej z tych zmian w audycie.

## Status

**A-05:** 🔍 potwierdzone, osiem błędnych odnośników w sześciu dokumentach.  
**Zakres zmian:** raport na gałęzi audytowej; bez zmian w korzeniach, tabeli i `main`.
