# Jak wykonać niezależną replikację (dodać słoje)

W P₀ każdy niezależny rachunek to potencjalny nowy słoje pnia. Zaproszenie jest literalne: **sprawdź nas.**

1. **Wybierz wynik** ze statusem 🔍 (albo ✅, jeśli chcesz zrobić trzecią niezależną kontrolę) w [docs/wyniki.md](wyniki.md).
2. **Pracuj ze specyfikacji (Z3), nie z cudzych implementacji.** W P₀ implementacje nie są przekazywane między wykonawcami. Czegoś brakuje w specyfikacji? To błąd specyfikacji — zgłoś go, nie zgadnij.
3. **Zacznij od bramki sanity (Z2).** Zanim policzysz cokolwiek własnego, odtwórz tabelę referencyjną wyniku (np. sanity SERC, tablicę wachlarzy, rozkład N1). Zgodność z tabelą otwiera replikację; rozbieżność = STOP i pytanie. Klasyczna pułapka: jeden znak w operatorze zmieniał każdą liczbę — wyłapała go właśnie bramka.
4. **Policz.**
5. **Zgłoś wynik w issue** z pełną atrybucją **każdej** liczby (Z2):
   - źródło specyfikacji (plik, §),
   - konwencje: jednostki, porządek klas, orientacja, normalizacja,
   - metoda numeryczna i precyzja,
   - przy losowości: generator, seed, liczba prób.
6. **Formaty wyniku:**
   - zgodność z istniejącym rachunkiem → kandydat do ✅ (status wpisuje warsztat po weryfikacji atrybucji),
   - rozbieżność → errata: dokument → § → jest → powinno być → uzasadnienie → status weryfikacji.

   Wynik negatywny jest pełnowartościowy (Z0) — obalenie hipotezy to też owoc drogi.
7. **Znane pułapki (lekcje P₀):**
   - konwencja orientacji ścian może produkować „fałszywą chiralność" (errata Φ_D),
   - znak fazy pary zespolonej zależy od wyboru koniugata (LAPACK podaje +im pierwszy),
   - zgodność dwóch rachunków nie chroni przed **wspólnym błędem specyfikacji** — rozdzielaj twierdzenie algebraiczne od numerycznego,
   - metody charakterystyczne (np. Faddeeva–LeVerrier) bywają zawodne na widmach zespolonych — weryfikuj niezależnie na parze dominującej.

Zgodność dwóch niezależnych rachunków to norma, nie powód do chwały.
