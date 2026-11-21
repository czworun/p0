# Asterion — Centroid S4 / S3b: pierwszy atak matematyczny (2026-11-21)

## Zakres

Punkt odniesienia: `docs/korzenie/P0-Centroid-v5_2-zmiany.md` z `main`, SHA blob `009ceb524c1f82d6f02f60b327c7e9e88c0740ed`. To jest adnotacja i lista zmian v5.1→v5.2, nie pełny źródłowy korzeń ani skrypt. Dlatego nie przypisuję jej brakujących definicji, których tekst nie podaje.

Analizowany proces A2 odczytuję zgodnie z §11.12: pojedynczy węzeł aktualizuje swoją wartość do średniej z siebie i aktualnych sąsiadów w grafie progowym `G_t(ε)`, gdzie krawędź `ij` istnieje, gdy `|r_i-r_j|<ε`. Aktualizacje są sekwencyjne.

## 1. Twierdzenie o braku scalania składowych — dowód potwierdzony

Niech `C` będzie składową grafu progowego na osi rzeczywistej. Wartości w `C` leżą w pewnym przedziale `[m_C,M_C]`. Dwie różne składowe mają rozłączne otoczki wypukłe oddzielone luką co najmniej `ε`; inaczej skrajne punkty dwóch sąsiednich składowych byłyby połączone krawędzią.

Aktualizowany węzeł uśrednia wyłącznie siebie i sąsiadów z własnej bieżącej składowej. Nowa wartość jest więc kombinacją wypukłą wartości z tej składowej i pozostaje w jej dotychczasowej otoczce. Otoczka składowej nie rozszerza się. Nie może zatem powstać nowa krawędź między dwiema wcześniej rozdzielonymi składowymi.

Wniosek:
- składowe mogą się rozdzielać, ale nie mogą się ponownie scalać;
- liczba składowych rośnie co najwyżej `n−1` razy;
- po skończonej liczbie rozdzieleń partycja stabilizuje się.

**Status: ✅** dla A2 w 1D i dowolnej kolejności aktualizacji. To twierdzenie nie dowodzi jeszcze zbieżności wartości wewnątrz składowej.

## 2. S3b — dokładny kontrprzykład P₄ → K₃+K₁

Centroid v5.2 podaje kontrprzykład dziesiętny. Odtworzyłem go na liczbach wymiernych, bez błędu zaokrągleń.

Przyjmujemy `ε=1`, kolejność aktualizacji `1,2,3,4` i stan początkowy:
```
r = (3511/2500, 9033/5000, 12557/5000, 34423/10000)
  = (1.4044, 1.8066, 2.5114, 3.4423)
```
Kolejne różnice początkowe:
```
r2-r1 = 2011/5000 = 0.4022
r3-r2 = 881/1250  = 0.7048
r4-r3 = 9309/10000 = 0.9309
```
Wszystkie są mniejsze od 1, a różnice niekolejnych par są większe lub równe 1. Graf początkowy jest więc dokładnie ścieżką `P₄`.

Sekwencyjne aktualizacje:
```
r1' = (r1+r2)/2 = 3211/2000 = 1.6055

r2' = (r1' + r2 + r3)/3
    = 3949/2000 = 1.9745

r3' = (r1' + r2' + r3 + r4)/4
    = 95337/40000 = 2.383425

r4' = r4 = 34423/10000 = 3.4423
```
Końcowe różnice:
```
r2'-r1' = 369/1000 = 0.369
r3'-r2' = 16357/40000 = 0.408925
r4'-r3' = 8471/8000 = 1.058875
```
Ostatnia różnica przekracza próg. Graf końcowy to `K₃+K₁`, nie `K₄`.

**Status: ❌** dla naturalnego twierdzenia „P₄ → K₄”. Kontrprzykład jest dokładny i jednoznaczny. Jednocześnie pokazuje, że liczba krawędzi może spaść z 3 do 2.

## 3. S3b — co jest już uzasadnione, a co pozostaje numeryczne

Z listy zmian v5.2:
- pięć możliwych partycji końcowych N=4: `(4)`, `(3,1)`, `(2,2)`, `(2,1,1)`, `(1,1,1,1)`;
- `K₂+2K₁` prowadzi do partycji `(2,1,1)`;
- `P₄` i paw nie muszą kończyć jako `K₄`;
- przejścia z P₄, paw i diamond są podane jako wyniki `p0_n4_check.py` / 800 tys. stanów.

Pierwsze dwa punkty są zgodne z twierdzeniem o nierozszerzaniu się otoczek składowych. Pełna tabela przejść klas grafów nie wynika jednak z samego twierdzenia o składowych; wymaga osobnego rachunku przedziałów dla każdej klasy i wszystkich etykietowań/kolejności. Bez `p0_n4_check.py` i dokładnej definicji wszystkich przypadków brzegowych pozostaje to **🔍**, nie dowód ogólny.

## 4. S4 — właściwa luka matematyczna

Po stabilizacji partycji każda składowa pozostaje spójna w każdym mikro-kroku. To jest mocniejsze niż sama spójność grafu na początku rundy.

Dla aktualizacji węzła `i` macierz kroku jest wierszowo-stochastyczna: wiersz `i` jest średnią po `i` i jego aktualnych sąsiadach, a pozostałe wiersze są jednostkowe. Każdy niezerowy współczynnik w aktualizowanym wierszu jest co najmniej `1/n`.

Luka w prostym dowodzie ergodycznym: nie wolno po prostu zamrozić grafu z początku rundy i przypisać tej samej symetrycznej macierzy każdemu aktualizowanemu węzłowi. Po aktualizacji jednego końca krawędź może zniknąć, zanim drugi koniec zostanie zaktualizowany. Wzorzec macierzy całej rundy jest więc zależny od trajektorii.

### Kandydat na lemat do zamknięcia S4

Wystarczyłoby wykazać, że po stabilizacji, dla każdego ustalonego porządku aktualizacji, iloczyn macierzy jednej lub ograniczonej liczby kolejnych rund ma:
1. silnie spójny graf zależności;
2. dodatni przekątniowy współczynnik;
3. jednolitą dolną granicę dodatnich współczynników zależną wyłącznie od `n`.

Wtedy standardowy argument konsensusu dla iloczynów macierzy stochastycznych dawałby `diam(C,t) → 0`.

Nie przyjmuję jednak tego lematu bez dowodu. Sam fakt, że każda chwilowa sieć jest nieskierowana i spójna, nie wystarcza dla dowolnej sekwencji macierzy stochastycznych; istotna jest dodatkowa zależność między zmianą położenia a zmianą krawędzi.

### Kontrola eksploracyjna

Wykonałem dokładną kontrolę na skończonej siatce stanów wymiernych dla N=4: 13 056 kombinacji stanu początkowego i kolejności aktualizacji, dla których składowa pozostawała spójna po każdym mikro-kroku. Nie znaleziono przypadku, w którym graf zależności całej rundy byłby niesilnie spójny.

To jest wyłącznie **🔍 kontrola skończonej siatki**, nie dowód dla ciągłego zbioru stanów. Nie zamyka S4.

## 5. Wniosek bieżący

- Twierdzenie o nierozszerzaniu się składowych: **✅**.
- Naturalne `P₄ → K₄`: **❌**, kontrprzykład wymierny.
- Pełna klasyfikacja przejść S3b dla wszystkich stanów i kolejności: **🔍**, wymaga analitycznego rozpisania przypadków.
- Zbieżność średnic składowych po stabilizacji (S4): **💡 / otwarte**. Istnieje konkretny kierunek dowodu przez ograniczoną silną spójność iloczynów macierzy, ale nie został jeszcze wykazany.

## 6. Następne kroki

1. Sformalizować lemat o grafie zależności jednej/ograniczonej liczby rund po stabilizacji — albo znaleźć kontrprzykład.
2. Jeśli lemat przejdzie, uzyskać jawny współczynnik kontrakcji zależny od `n`.
3. Dopiero potem zamknąć S4.
4. Osobno przeprowadzić dokładną klasyfikację przejść S3b dla N=4, z podziałem na klasy początkowe i porządki aktualizacji.
