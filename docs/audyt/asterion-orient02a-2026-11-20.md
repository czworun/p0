# ORIENT-02-A — audyt kompresji kanonicznej

**Autor:** Asterion  
**Data:** 2026-11-20  
**Baza korpusowa:** `main` @ `ff5345f50f509ff95fafcd1e4b28ce64b388eb1c`  
**Gałąź audytowa:** `audit/asterion-orient02a-2026-11-20`  
**Zakres:** ORIENT-02-A, kroki 1–2. Bez zmian w korzeniach, statusach i rejestrze.

## 1. Konkluzja wykonawcza

Przeliczenie według kanonicznej konwencji odtworzonej z `7atraktorow.ipynb` daje dokładnie rejestrowane widmo:

- 4.97841283 (1)
- 6 (2)
- 7.33333333 (3)
- 7.6 (1)
- 8.08825384 (1)
- 10 (11)

Pozostałe 11 wartości własnych pełnego operatora `P_cyc L_line P_cyc` wynosi zero. Ślad wynosi dokładnie 494/3 = 164.6666666667. Krotność wartości własnej 10 wynosi dokładnie 11.

**Wynik kroku 2: zgodność numeryczna i algebraiczna z widmem rejestrowym — TAK.**

Wartość wcześniejszej kompresji Asteriona 165.7333 nie jest wynikiem tej samej kompletnej konstrukcji kanonicznej: odtwarzając ją literalnie, otrzymujemy 164.6666666667. Zachowany raport wcześniejszego audytu nie zawiera jednak wektora znaków orientacji ani macierzy bazowej użytej w tamtym przebiegu. Dlatego nie mogę uczciwie przypisać różnicy wyłącznie innej orientacji krawędzi. Możliwa jest też różnica w bazie/projekcji lub implementacji. Krok 1 jest rozstrzygnięty w sensie negatywnym (stary wynik nie pochodzi z dokładnie tej samej kompletnej procedury), ale nie w sensie identyfikacji konkretnego starego wektora orientacji.

## 2. Kanoniczna konstrukcja odtworzona

### 2.1. Wierzchołki i krawędzie

Użyto 12 wierzchołków ikosaedru w kolejności zapisanej w notatniku:

```text
(0,1,φ), (0,1,-φ), (0,-1,φ), (0,-1,-φ),
(1,φ,0), (1,-φ,0), (-1,φ,0), (-1,-φ,0),
(φ,0,1), (φ,0,-1), (-φ,0,1), (-φ,0,-1)
```

Współrzędne podzielono przez normę pierwszego wierzchołka. Długość krawędzi docelowej:
`d_edge = 2/sqrt(2+φ)`.

Krawędzie wygenerowano przez `combinations(range(12),2)` i zachowano, gdy różnica długości od `d_edge` była mniejsza niż 0.01. W ten sposób powstało 30 krawędzi w porządku leksykograficznym, zawsze jako pary `(a,b)` z `a<b`.

### 2.2. Macierz incydencji i orientacja

Macierz `d` ma rozmiar 30×12. Dla krawędzi `(a,b)`, gdzie `a<b`, wiersz ma:
- +1 w kolumnie a,
- −1 w kolumnie b,
- zera w pozostałych kolumnach.

Macierz `B=dᵀ` ma rozmiar 12×30. Jest to dokładnie orientacja leksykograficzna notatnika, nie losowa orientacja i nie orientacja odziedziczona z kolejności zwracanej przez bibliotekę grafową.

### 2.3. Sektor cykliczny

Wykonano SVD macierzy `d` z `full_matrices=False`. Rangę określono jako liczbę wartości singularnych większych niż 10⁻¹⁰.

Wyniki:
- ranga `d` = 11;
- wymiar `V_cyc` = 30−11 = 19;
- `Q_im = U[:, :11]`;
- `P_cyc = I₃₀ − Q_im Q_imᵀ`.

### 2.4. Laplasjan grafu krawędziowego

Dwa wierzchołki grafu krawędziowego sąsiadują, gdy odpowiadające im krawędzie ikosaedru mają wspólny koniec.

Z tego wynika:
- stopień każdego wierzchołka grafu krawędziowego = 8;
- `L_line = diag(deg_line) − edge_adj`;
- operator jest kombinatoryczny, bez normalizacji stopni;
- `L_line = 10I₃₀ − |B|ᵀ|B|`.

Operator badany:
`L_cyc = P_cyc L_line P_cyc`.

## 3. Wynik pełnego przeliczenia

Widmo pełnej macierzy 30×30 `L_cyc`, z tolerancją prezentacji 10⁻⁸:

| Wartość własna | Krotność |
|---:|---:|
| 0 | 11 |
| 4.97841283 | 1 |
| 6 | 2 |
| 7.33333333 | 3 |
| 7.6 | 1 |
| 8.08825384 | 1 |
| 10 | 11 |

Wartości kontrolne:
- ślad = 164.66666666666666 = 494/3;
- ranga `L_cyc` = 19;
- krotność `λ=10` = 11;
- stopień grafu krawędziowego: min = max = 8.

Widmo dodatnie jest dokładnie zgodne z listą rejestrową: 4.9784; 6×2; 7.3333×3; 7.6; 8.0883; 10×11.

## 4. Niezależna bramka: przecięcie jąder

Niech `B` oznacza znakowaną macierz incydencji 12×30, a `|B|` jej wersję bezwzględną.

Dla tej samej konwencji:
- `dim ker(B) = 19`;
- `dim ker(|B|) = 18`;
- `dim(ker(B) ∩ ker(|B|)) = 11`.

Ostatnia liczba została obliczona z rangi macierzy sklejonej:
`dim intersection = 30 − rank([B; |B|]) = 30 − 19 = 11`.

Ponadto:
`L_line x = 10x` wtedy i tylko wtedy, gdy `|B|x=0`, ponieważ
`L_line = 10I − |B|ᵀ|B|`.

Po ograniczeniu do `V_cyc = ker(B)`, krotność wartości własnej 10 jest więc równa:
`dim(ker(B) ∩ ker(|B|)) = 11`.

To niezależnie potwierdza bramkę krotności, a nie tylko odczyt numerycznego diagonalizatora.

## 5. Porównanie ze starym wynikiem 165.7333

Wcześniej raportowana kompresja Asteriona miała ślad 165.7333 i krotność 10 dla wartości własnej 10. Przy obecnej specyfikacji wynik wynosi 164.6666666667 i krotność 11.

Różnica śladu:
`165.7333333333 − 164.6666666667 = 1.0666666666… = 16/15`.

Wniosek:
1. Stary wynik nie może być uznany za wynik dokładnie tej samej kompletnej procedury (tej samej `d`, SVD/progu rangi, `P_cyc`, `L_line` i iloczynu `P_cyc L_line P_cyc`).
2. Z samego śladu nie wynika, czy źródłem była inna orientacja, inna kolejność krawędzi, inna baza/projekcja, czy błąd konstrukcji operatora.
3. Nie zachował się w raporcie ORIENT-02 wektor 30 znaków ani macierz `B` z pierwotnego przebiegu. Bez tego nie da się odtworzyć starej konwencji jednoznacznie.
4. Nie wykonano i nie należy wykonywać pełnego sweepu 2³⁰ orientacji.

## 6. Minimalny kod replikacyjny

Poniższy kod wystarcza do odtworzenia zasadniczego rachunku:

```python
import numpy as np
from itertools import combinations

phi = (1 + np.sqrt(5)) / 2
V = np.array([
    [0,1,phi], [0,1,-phi], [0,-1,phi], [0,-1,-phi],
    [1,phi,0], [1,-phi,0], [-1,phi,0], [-1,-phi,0],
    [phi,0,1], [phi,0,-1], [-phi,0,1], [-phi,0,-1]
], dtype=float)
V /= np.linalg.norm(V[0])

d_edge = 2 / np.sqrt(2 + phi)
edges = [
    (i,j) for i,j in combinations(range(12),2)
    if abs(np.linalg.norm(V[i]-V[j])-d_edge) < 0.01
]

d = np.zeros((30,12))
for k,(a,b) in enumerate(edges):
    d[k,a] = 1.0
    d[k,b] = -1.0

U,S,_ = np.linalg.svd(d, full_matrices=False)
rank = int(np.sum(S > 1e-10))
P = np.eye(30) - U[:,:rank] @ U[:,:rank].T

edge_adj = np.zeros((30,30))
for i,(a,b) in enumerate(edges):
    for j,(c,e) in enumerate(edges):
        if i != j and len({a,b} & {c,e}) > 0:
            edge_adj[i,j] = 1.0

L = np.diag(edge_adj.sum(axis=1)) - edge_adj
L_cyc = P @ L @ P
evals = np.linalg.eigvalsh(L_cyc)

print("rank(d) =", rank)
print("trace =", np.trace(L_cyc))
print("eigenvalues =", evals)
```

## 7. Zalecenie dla warsztatu

Wynik kanoniczny jest zgodny z widmem rejestrowym. Zgodnie z instrukcją Vibe'a nie przypisuję statusu i nie proponuję samodzielnej erraty.

Dalsza kontrola, jeśli warsztat uzna ją za potrzebną, powinna być punktowa:
- odtworzyć pierwotny wektor znaków / macierz `B` z wcześniejszego przebiegu Asteriona;
- porównać go z kanonicznym `B`;
- sprawdzić, czy stary wynik 165.7333 wynikał z samej reorientacji, czy z innej konstrukcji projekcji/operatora.

**Nie wykonywać sweepu 2³⁰ orientacji.**

---
**Ograniczenie źródłowe:** przeliczenie wykonano niezależnie z jawnej specyfikacji odtworzonej z `7atraktorow.ipynb`. Nie wykorzystano `P0_dowody`, do którego nie mam dostępu.
