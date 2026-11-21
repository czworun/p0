# Asterion — Centroid S4: ograniczenie lematu o grafach zależności (2026-11-21)

## Cel

Sprawdzić, czy do dowodu S4 wystarczy następujący skrót: „w każdej mikrochwili graf progowy jest spójny, więc iloczyn macierzy aktualizacji jednej rundy ma silnie spójny graf zależności”.

Wynik: **nie**. Sama spójność chwilowych grafów, nawet gdy każdy z nich jest grafem przedziałowym jednostkowym, nie wystarcza. Trzeba wykorzystać dodatkową zgodność grafów z trajektorią A2.

## Dokładny kontrprzykład dla zbyt mocnego lematu

Cztery aktualizacje w kolejności 1,2,3,4. W kolejnych mikrochwilach przyjmijmy grafy (krawędzie nieskierowane):

- G₁: 12, 13, 23, 34;
- G₂: 12, 13, 14, 23;
- G₃: 12, 13, 24;
- G₄: 12, 13, 23, 24, 34.

Każdy graf jest spójny i jest grafem przedziałowym jednostkowym. Aktualizowany w danym kroku węzeł uśrednia siebie i wszystkich swoich sąsiadów w tym grafie.

Macierze kroków są wierszowo-stochastyczne. Ich iloczyn (po czterech aktualizacjach) wynosi dokładnie:

```
P = [
  [1/3,  1/3,  1/3,   0  ],
  [1/9,  4/9,  4/9,   0  ],
  [1/6,  1/6,  2/3,   0  ],
  [5/54,11/54,10/27,  1/3]
]
```

Pierwsze trzy wyjściowe współrzędne nie zależą w ogóle od czwartej współrzędnej wejściowej. Graf zależności iloczynu nie jest silnie spójny.

To obala wyłącznie abstrakcyjny lemat oparty na spójności (także przedziałowości) każdej sieci z osobna. **Nie jest to kontrprzykład dla A2**: nie wykazano, że sekwencja G₁,…,G₄ może powstać z jednego stanu skalarnego przez wskazane aktualizacje progowe.

## Konsekwencja dla dowodu S4

Nie wolno wnioskować o silnej spójności iloczynu rundy z samej spójności każdej sieci chwilowej. Potrzebny jest lemat wykorzystujący dynamiczną zgodność:
1. wartości są skalarne;
2. krawędzie są dokładnie relacją `|rᵢ-rⱼ|<ε`;
3. po stabilizacji partycji nie może już zniknąć żadna ścieżka łącząca składową;
4. graf po każdym mikro-kroku musi być grafem progowym aktualnego wektora, nie dowolnie wybranym grafem przedziałowym.

## Następny atak

Zamiast badać dowolne ciągi spójnych grafów, należy śledzić ewolucję przerw między uporządkowanymi wartościami. Dla składowej spójnej, po uporządkowaniu `x₁≤…≤xₙ`, wszystkie luki sąsiednie spełniają `xᵢ₊₁−xᵢ<ε`. Aktualizacja jest średnią po przedziale indeksów obejmującym aktualizowany punkt. Należy znaleźć funkcję Lapunowa lub skończonookresową kontrakcję opartą na tych lukach, uwzględniając możliwe zmiany kolejności wartości.

## Status

- „Spójność każdej sieci chwilowej ⇒ silna spójność iloczynu rundy”: **❌** (kontrprzykład macierzowy powyżej).
- „A2 po stabilizacji ma `diam(C,t)→0`”: **otwarte**.
- Kontrprzykład nie obala S4; zawęża wymagany lemat i zapobiega użyciu nieuprawnionego argumentu.
