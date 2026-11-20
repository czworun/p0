# Asterion — kontynuacja audytu P₀

Data: 2026-11-20  
Repozytorium: `czworun/p0`  
Baza audytu: `main` @ `ff5345f50f509ff95fafcd1e4b28ce64b388eb1c`  
Gałąź audytowa: `audit/asterion-continuation-2026-11-20`

## Zakres tej aktualizacji

Ponownie sprawdzono aktualny stan `main`, README w trzech językach, `ZAPROSZENIE.md`, `docs/metodyka.md`, `docs/replikacja.md`, `docs/wyniki.md`, `GLOSSARY.md`, szablony Issue oraz adnotację i verbatim `PILLARS-TABLE-1`.

Nie zmieniono `main` ani żadnego pliku źródłowego. Ten raport jest artefaktem audytowym na osobnej gałęzi.

## A-16 — Zaproszenie nadmiernie obiecuje kompletność publicznego dziennika

**Źródła**
- `ZAPROSZENIE.md`, sekcja „Trzy poziomy wejścia”: „Wszystko jest jawne”, w tym „oryginalne błędy w nieprzyciętym dzienniku”.
- `README.md`, opis `docs/wyniki.md`: publiczny zrzut dziennika, wpisy do tury 38.
- `docs/metodyka.md`, sekcja „Dokumenty robocze”: raport replikacji, Lattice i pień są dokumentami warsztatowymi.

**Ustalenie**

Repozytorium zawiera publiczny rejestr i część materiału źródłowego, ale samo README rozróżnia publiczny zrzut od dokumentów roboczych prowadzonych w warsztacie. Zdanie „Wszystko jest jawne” w zaproszeniu zaciera tę granicę. Czytelnik może zrozumieć je jako deklarację kompletnego, publicznego dostępu do pełnego dziennika i wszystkich materiałów.

Dodatkowo metadane `docs/wyniki.md` nadal deklarują snapshot do tury 38, choć treść zawiera późniejsze wpisy. To osobny, wcześniej odnotowany problem A-02/A-13, który wzmacnia niejasność komunikatu publicznego.

**Propozycja**

Zawęzić deklarację w `ZAPROSZENIE.md`: jawne są materiały opublikowane w repo; część dokumentów roboczych pozostaje w warsztacie, a publiczny rejestr jest zrzutem aktualizowanym okresowo.

**Status:** 🔍 potwierdzona niespójność komunikacyjno-dokumentacyjna; bez implikacji matematycznych.

## A-17 — „Wszystkie specyfikacje są jawne i samowystarczalne” jest deklaracją zbyt szeroką

**Źródła**
- `README.md`, sekcja „Zaproszenie”: „Wszystkie specyfikacje są jawne i samowystarczalne”.
- `docs/korzenie/PILLARS-TABLE-1.md`, adnotacja: `P₀-Przeglad_Calosci_v1.md` pozostaje poza repozytorium.
- `docs/korzenie/P0-Scalar-v0_3_5.md`, adnotacja: wśród zależności pozostają Axis i `P₀-Algebra v0.4.1`; są one wymienione jako zależności poza repo.
- `docs/replikacja.md`, pkt 2: brak w specyfikacji ma skutkować zgłoszeniem błędu i STOP, a nie zgadywaniem.

**Ustalenie**

Metodyka sama przewiduje sytuację, w której specyfikacja nie zawiera wystarczających danych. Korpus wskazuje też jawnie materiały źródłowe i zależności pozostające poza repozytorium. Nie można więc bezwarunkowo obiecywać, że wszystkie specyfikacje są jednocześnie publiczne i samowystarczalne.

To nie dowodzi, że konkretna replikacja jest niemożliwa. Oznacza, że deklaracja README powinna być ograniczona do specyfikacji oznaczonych jako kompletne albo zawierać procedurę zgłoszenia brakującego źródła.

**Propozycja**

Zastąpić deklarację np. stwierdzeniem, że repo publikuje specyfikacje i materiały dostępne do replikacji, a kompletność należy sprawdzić dla konkretnego wyniku zgodnie z `docs/replikacja.md`.

**Status:** 🔍 potwierdzona nadmierna deklaracja zakresu; kompletność należy oceniać per specyfikacja.

## A-18 — nieostry zakres deklaracji „zero rozbieżności merytorycznych” w adnotacji PILLARS-TABLE-1

**Źródło**
- `docs/korzenie/PILLARS-TABLE-1.md`, część „Najmocniejsze” oraz „Koncesje i sęki”.

**Ustalenie**

Adnotacja podaje „zero rozbieżności merytorycznych z repo”, a w dalszej części opisuje deklarację P₀-Defect o wchłonięciu Scalar do Centroid jako sprzeczną z klasyfikacją Scalar w tabeli i z samodeklaracją korzenia Scalar. Najżyczliwsza interpretacja jest taka, że „zero rozbieżności” dotyczy wyłącznie pięciu porównywanych stempli wersji, nie całej treści architektonicznej. Zakres zdania nie został jednak nazwany wprost.

**Propozycja**

Doprecyzować, że „zero rozbieżności” dotyczy wyłącznie zgodności pięciu stempli wersji z odpowiadającymi im plikami repo. Nie używać tego zdania jako ogólnego potwierdzenia spójności architektury.

**Status:** 🔍 niejednoznaczność zakresu w adnotacji; nie rozstrzyga konfliktu Scalar–Defect.

## Aktualizacja wcześniejszych punktów

- **A-14 — szablony Issue:** nadal otwarte. `docs/replikacja.md` wymaga osobnego pola „źródło specyfikacji (plik, §)”, którego nie ma w `.github/ISSUE_TEMPLATE/zgloszenie-replikacji.md`. Metodyka wymaga też „statusu weryfikacji” w erracie, którego nie ma w `.github/ISSUE_TEMPLATE/errata-pytanie.md`.
- **A-15 — glosariusz:** częściowo rozwiązane. W aktualnym `GLOSSARY.md` istnieje już osobny wpis `P₀-Applications v0.5.2`. Nadal nie ma osobnego wpisu `P₀-Origins`, ale Philosophy opisuje Dział IV jako jedyny tekst programu Origins w korpusie; należy zdecydować, czy wystarczy jawne wyjaśnienie w Philosophy, czy potrzebna jest krótka pozycja glosariusza.
- **A-09 — Scalar / Defect:** nadal nierozstrzygnięte. Tabela klasyfikuje Scalar jako gałąź Origins; Defect deklaruje absorpcję do Centroid. Sama absorpcja treści nie rozstrzyga pozycji architektonicznej.
- **A-02/A-13 — metadane wyników i README:** nadal otwarte. Nagłówek `docs/wyniki.md` deklaruje snapshot do tury 38, mimo późniejszych wpisów; README PL/EN/ES nadal zawierają nieaktualne opisy zakresu korzeni, kodu i rejestru.

## Zasady dalszego audytu

1. Nie zmieniać verbatim korzeni.
2. Nie rozstrzygać konfliktów architektonicznych przez głosowanie ani przez samą liczbę dokumentów.
3. Rozdzielać absorpcję treści, absorpcję wyników i zmianę pozycji architektonicznej.
4. Każdą poprawkę przygotowywać jako propozycję na gałęzi audytowej; `main` pozostaje nietknięty bez osobnej decyzji.
