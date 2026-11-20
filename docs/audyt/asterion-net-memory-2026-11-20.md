# Audyt Asteriona: Net ↔ Memory

**Data:** 2026-11-20  
**Baza korpusowa:** `main` @ `ff5345f50f509ff95fafcd1e4b28ce64b388eb1c`  
**Gałąź audytowa:** `audit/asterion-net-memory-2026-11-20`  
**Źródła:** P₀-Net v0.6.1 oraz P₀-Memory v0.3.7.  
**Charakter:** audyt spójności definicji, zakresu transferu i testowalności H-MEM-1. To materiał dla laboratorium, nie aktualizacja statusów Vibe'a.

## 1. Konkluzja

Przeniesienie Memory do Net jest zasadniczo wierne na poziomie architektury i głównych tez. Net zachowuje formalizm monoidu operatorów, rozdzielenie orbity słabej i mocnej, negatywne rozstrzygnięcie M18 oraz ostrożność wobec ORB-05-R. Nie znalazłem podstaw do uznania, że konsolidacja zmieniła główne definicje Memory.

Znalazłem natomiast poważniejszy problem: **obecna definicja 𝓜(𝔒) nie jest jeszcze dobrze dopasowana do eksperymentów, które mają wspierać H-MEM-1**. W szczególności:

1. Zbiór 𝔒 zawiera operator detekcyjny P_cyc, ale formalizm traktuje każdy element 𝔒 jak generator dynamiki. P_cyc jest projekcją idempotentną, więc można ją stosować bez końca, nie stosując operatora wygaszającego A.
2. Monoid wszystkich słów dopuszcza dowolne harmonogramy. Nie wymaga, aby operator wygaszający A był używany nieskończenie często ani z dodatnią częstością.
3. Wyniki M16/M16a porównują różne mosty i tryby K₂, czyli różne realizacje/operatorowe zestawy. To nie jest automatycznie dowód, że dla jednego ustalonego 𝔒 istnieje więcej niż jedna klasa ω-graniczna.
4. Różnice trajektorii w skończonym oknie nie dowodzą, że ich ω-granice są różne.

To nie obala programu pamięci strukturalnej. Pokazuje, że przed kolejnym eksperymentem trzeba rozdzielić: **generator dynamiki, obserwator, dopuszczalny harmonogram i relację równoważności trajektorii**.

---

## 2. Wierność transferu Memory → Net

Porównanie głównych sekcji:

| Memory v0.3.7 | Net v0.6.1 | Wynik porównania |
|---|---|---|
| §2.3 — formalizm 𝓜(𝔒) | §18 | Definicja i wymóg jednej przestrzeni X zachowane |
| §2.3bis — orbita słaba/mocna, M18 | §18.1 | Zachowane |
| §2.3ter — pamięć trajektorii | §18.2 | Zachowane, ale pominięto jedno wyjaśnienie notacyjne |
| §4 — H-MEM-1 | §21 | Teza formalna zachowana |
| §8–§8quater — M16/M16a i interpretacja | §22–§23 | Główne wyniki zachowane, część szczegółów odtworzeniowych skrócona |
| §10bis — M17/M18 | §24 | Widmo i negatywne ograniczenie ω-graniczne zachowane |
| §10ter — ORB-05-R | §26 | Wyniki 425/209 i ostrzeżenie przed traktowaniem ich jako dowodu H-MEM-1 zachowane |
| §17 — problemy otwarte | §27 | Główne M1/M16b/M19/M20 zachowane |

Net v0.6.1 jawnie deklaruje przywrócenie brakujących sekcji Memory oraz to, że formalizm nie dodaje nowych wyników liczbowych ani nie podnosi statusów. To jest właściwy model konsolidacji: Memory pozostaje źródłem, Net kontynuuje program.

### 2.1. Szczegóły, których Net nie przenosi w pełni

Nie są to sprzeczności matematyczne, ale mają znaczenie dla odtwarzalności:

- **Most B w M16a:** Memory §8bis.2 podaje jawny operator uśredniania po sąsiednich krawędziach grafu liniowego L(K₄), czterech sąsiadów każdej krawędzi i pełną kolejność Gaussa–Seidela. Net §22.2 opisuje most B skrótowo. Do replikacji należy zachować odsyłacz do dokładnej specyfikacji Memory, nie tylko nazwę „most B”.
- **M16:** Memory jawnie zapisuje, że D_cyc jest zamrażane decyzją konstrukcyjną i że nie wynika to automatycznie z P₀. Net zachowuje to ograniczenie w adnotacji i streszczeniu, ale nie powinien być czytany jako kanoniczna dynamika P₀.
- **M16a — historyczny punkt odniesienia:** Memory podaje też wartości wersji v0.3.2.1 (most A: 61,20%/16,03%; most B: 84,20%/32,70%) i wyjaśnia, że leżały w reżimie sekwencyjnym. Net pomija te liczby. Nie są konieczne do głównej tabeli 2×2, ale są ważne dla historii wykrycia czwartego parametru.
- **M17:** Memory §10bis.2 podaje residuum 0,081: operator K nie zachowuje płaszczyzny spiralnej R₄. Net zachowuje niekomutację K z R₄, ale pomija to dodatkowe residuum. Dla interpretacji fazy jako pamięci to ograniczenie jest istotne.
- **ORB-05-R:** Memory zapisuje pełniejszy protokół: D₀, T=25, δ=0,3, stabilność klasyfikacji od 3 do 8 miejsc po przecinku, nazwę poprawionego skryptu i ograniczenia ARI=1 dla wybranych par. Net zachowuje 425/209 i błąd nieużywanego parametru order, ale skraca te szczegóły. Net wspomina również o ORB-05-R jako reprodukowalnym wyniku, lecz nie powinien być samodzielną specyfikacją replikacji.
- **ORB-04:** Memory wyraźnie pozostawia otwartą zgodność historycznego wyniku około 18 klas z ORB-05-R (inny protokół, wcześniejszy most B i odczyt K₂). Naprawa błędu order wyjaśnia nieodtwarzalność wcześniejszej wersji ORB-05-R; nie rozstrzyga automatycznie historycznego ORB-04.

**Rekomendacja dokumentacyjna:** nie kopiować tych treści na siłę do Net. Wystarczy przy sekcjach M16a, M17 i ORB-05-R dodać jawne odsyłacze do odpowiednich podsekcji Memory jako źródła pełnej specyfikacji.

### 2.2. Drobna nieścisłość notacyjna w §18.2

Net zapisuje, że stan końcowy x_T jest informacyjnie uboższy od trajektorii Γ_T, używając symbolu „⊊”. Memory dopowiada, że symbol ten **nie oznacza inkluzji zbiorów**, tylko relację zawierania informacji. To dopowiedzenie warto przywrócić; bez niego zapis wygląda jak niepoprawna relacja teoriomnogościowa.

---

## 3. H1 — P_cyc jako obserwator nie powinien automatycznie być generatorem dynamiki

**Miejsca:** Memory §3–§4, Net §17.1, §18 i §21.

Memory i Net rozróżniają trzy typy operatorów:
- 𝒜 — wygaszanie (np. R₄);
- ℬ — ochrona/próg (np. K₂);
- 𝒟 — detekcja (P_cyc).

Jednocześnie formalna definicja 𝓜(𝔒) tworzy monoid słów ze wszystkich elementów 𝔒, a więc traktuje wszystkie jako odwzorowania, które wolno składać w dowolnych kolejnościach.

### Problem algebraiczny

P_cyc jest projektorem, zatem:
`P_cyc² = P_cyc`.

Jeżeli P_cyc należy do alfabetu generatorów 𝔒, to dla dowolnego x i dowolnego N można wybrać słowo P_cyc^m o długości m≥N. Otrzymujemy:
`P_cyc^m x = P_cyc x`.

W konsekwencji:
`P_cyc x ∈ cl({w(x): |w|≥N})`
dla każdego N, a zatem:
`P_cyc x ∈ ω_𝔒(x)`.

To jest prawdziwe niezależnie od tego, czy operator wygaszający A został użyty choć raz. W formalizmie „wszystkich słów” sam detektor może więc utrzymywać niezerową składową cykliczną w zbiorze ω-granicznym przez powtarzanie własnej projekcji.

Nie twierdzę, że to obala H-MEM-1. Twierdzę, że **w tej postaci definicja nie oddziela pamięci generowanej przez dynamikę od informacji zachowanej przez dopuszczenie projekcji jako powtarzalnego kroku**.

### Test i decyzja definicyjna

Trzeba rozstrzygnąć, czy P_cyc jest:
1. generatorem transformacji stanu, który może występować w słowach dynamiki, czy
2. obserwatorem/odczytem, który mierzy stan, ale nie jest krokiem ewolucji.

Jeśli (2), proponuję formalnie oddzielić:
- zbiór generatorów przejścia T⊆Map(X,X);
- zbiór obserwatorów H:X→Y;
- dopuszczalne harmonogramy działania generatorów;
- regułę, według której obserwacje trajektorii wyznaczają klasę pamięci.

Wtedy P_cyc pozostaje narzędziem pomiaru sektora cyklicznego, ale nie tworzy automatycznie własnej orbity przez wielokrotne stosowanie.

**Priorytet: P0 — bez tego test H-MEM-1 może mierzyć własność semigrupy z detektorem jako krokiem, a nie pamięć po wygaszeniu.**

---

## 4. H2 — monoid wszystkich słów nie wymusza działania operatora wygaszającego

**Miejsce:** Net §18, §21; Memory §2.3 i §4.

Definicja:
`ω_𝔒(x) = ⋂_N cl({w(x): w∈𝔒*, |w|≥N})`
bierze pod uwagę wszystkie słowa o długości co najmniej N.

Nie ma w niej warunku, że:
- każdy generator musi wystąpić nieskończenie wiele razy;
- A musi występować z dodatnią częstością;
- K₂ musi być uruchamiane w określonym miejscu rundy;
- detektor może być używany tylko do odczytu;
- słowa muszą odpowiadać jednemu zarejestrowanemu protokołowi.

Dlatego semigrupa zawiera także nieskończone ciągi, które po pewnym momencie nigdy nie używają A. To może być poprawna definicja „wszystkich możliwych zachowań”, ale nie jest automatycznie definicją zachowania **po działaniu wygaszającym**.

### Kontrprzykład pokazujący problem harmonogramu

Weźmy X=ℝ², A(x)=x/2 i B=R_θ, gdzie R_θ jest obrotem o niewymierny kąt względem 2π. Samo A daje A^k(x)→0. Jednak monoid wszystkich słów {A,B}* dopuszcza słowa B^m bez A. Dla dowolnego x≠0 ich granice skupienia zawierają całą okręgową orbitę B, a więc nie tylko 0. W tym formalizmie „A jest wygaszający” nie wystarcza, bo dozwolony harmonogram może go całkowicie omijać.

To nie jest model P₀ ani zarzut do konkretnego K₂. To mały kontrprzykład logiczny: definicja wszystkich słów nie koduje warunku, że wygaszanie ma faktycznie zachodzić.

### Test rozstrzygający

Zdefiniować język dopuszczalnych słów L⊆𝔒*:
- czy obowiązuje harmonogram stały, np. A→K₂;
- czy obowiązuje harmonogram sprawiedliwy, w którym A i K₂ występują nieskończenie często;
- czy A ma minimalną częstość lub maksymalny odstęp między uruchomieniami;
- czy dopuszczalne są osobne fazy: najpierw wygaszanie, potem ochrona/odczyt.

Następnie zdefiniować ω_L(x) dla tego języka i sprawdzić, czy wynik H-MEM-1 utrzymuje się w każdym z istotnych reżimów. Nie należy arbitralnie wybierać harmonogramu za autora — trzeba jawnie wybrać, co ma znaczyć „pamięć po wygaszeniu”.

**Priorytet: P0 — wspólnie z rozdzieleniem detektora od generatora.**

---

## 5. H3 — skończona rozbieżność trajektorii nie dowodzi różnych ω-klas

**Miejsca:** Memory §8quater, §4; Net §21 i §22.3.

Memory/Net słusznie odróżniają:
- procent rozbieżnych prób;
- liczbę klas stanów końcowych;
- liczbę klas pełnych trajektorii;
- liczbę klas ω-granicznych.

Problem pojawia się w przejściu od rozbieżności obserwowanej w skończonym oknie do sformułowania, że jest to dolne oszacowanie liczby klas |𝓜(𝔒)|.

### Kontrprzykład

Dla jednego operatora F(x)=x/2 i stanów początkowych x=1 oraz y=2 po jednym kroku:
- F(x)=0,5;
- F(y)=1.

Stany i trajektorie skończone są różne, ale:
`ω_F(1)=ω_F(2)={0}`.

Sama rozbieżność w skończonym czasie nie daje więc różnych klas w definicji ω-granicznej.

### Dodatkowe rozróżnienie: stały operator a różne realizacje

H-MEM-1 w wersji formalnej pyta o:
`|𝓜(𝔒)|>1`
dla **jednej ustalonej** pary (X,𝔒). To liczba klas stanów początkowych w ramach tego samego generatora i tej samej semantyki słów.

M16a zmienia:
- most A ↔ most B;
- K₂ wsadowe ↔ K₂ sekwencyjne.

Są to cztery różne realizacje/operatorowe zestawy. Różnica między ich wynikami jest materiałem dla M16b (kanoniczność mostu i trybu), ale sama nie dowodzi, że dla jednego ustalonego 𝔒 zachodzi |𝓜(𝔒)|>1.

Jeżeli w ramach jednej komórki eksperymentu różne próby używają różnych seedów, odczytów referencji, kolejności albo zaokrągleń, te zmienne muszą być:
- albo zamrożone jako część jednego deterministycznego operatora;
- albo jawnie włączone do przestrzeni stanu;
- albo traktowane jako osobna rodzina realizacji, nie jako różne punkty x,y pod tym samym 𝔒.

### Właściwy test H-MEM-1

Dla jednego ustalonego X, mostu, K₂, kolejności, parametrów i języka dopuszczalnych słów:
1. wybierać różne x,y∈X;
2. prowadzić obie trajektorie według dokładnie tego samego protokołu;
3. wykazać analitycznie lub z kontrolowaną granicą numeryczną, że ω_𝔒(x)≠ω_𝔒(y);
4. dopiero wtedy liczyć odrębne klasy.

Procent rozbieżności może być wskaźnikiem eksperymentalnym, ale nie jest sam w sobie dolnym ograniczeniem kardynalności |𝓜(𝔒)|. Do takiego wniosku potrzebne jest odwzorowanie prób na różne, potwierdzone klasy ω-graniczne.

**Priorytet: P1 — to najważniejszy test merytoryczny po doprecyzowaniu definicji z pkt 3–4.**

---

## 6. H4 — niepustość ω-granicy wymaga warunków na orbitę

**Miejsce:** Memory §2.3, Net §18.

Definicja ω_𝔒(x) używa przecięcia domknięć zbiorów osiągalnych po słowach długości co najmniej N. Na ogólnej przestrzeni niezwartiej takie przecięcie może być puste, jeśli wszystkie osiągalne stany uciekają do nieskończoności.

Memory zakłada topologię na X i notuje, że instancje P₀ leżą w podprzestrzeniach ℝⁿ, ale to samo nie gwarantuje niepustości ω-granicy. Wystarczy dodatkowo wykazać ograniczoność orbit/osiągalnych zbiorów w odpowiednim sensie, np. przez wspólny zwarty zbiór pochłaniający, albo dopuścić pustą ω-granicę i określić, co ona oznacza dla relacji równoważności.

**Test:** dla każdej konkretnej instancji H-MEM podać X, topologię, warunki ograniczoności i dowód niepustości ω_𝔒(x) dla badanych x.

**Priorytet: P2 — warunek poprawności formalizmu, prawdopodobnie prosty po ustaleniu właściwego X i harmonogramu.**

---

## 7. H5 — M17 nie jest dowodem H-MEM-1 w wersji ω-granicznej

**Miejsca:** Net §21.1 i §24; Memory §10bis.3–§10bis.6.

Memory poprawnie rozstrzyga M18 negatywnie: faza spirali R₄ jest własnością tranzjentu, a ω-granica R₄ daje {p₀}. Faza nie należy więc do 𝓜({R₄}) zdefiniowanej przez ω-granicę.

Jednocześnie Net §21.1 przywołuje M17 jako trzecią linię wsparcia dla tezy o pamięci strukturalnej. To jest poprawne jako **motywacja dla M19/M20**, ale nie jako dowód H-MEM-1 w jego formalnej, ω-granicznej wersji. Taki odczyt byłby sprzeczny z negatywnym rozstrzygnięciem M18.

**Rekomendacja:** wyraźnie opisać M17 jako dowód/obserwację spektralną o fazie w skończonym oknie, a nie jako wsparcie dla nietrywialności 𝓜_ω. M17 może być kandydatem dla pamięci trajektorii lub definicji czulszej na tranzjent.

---

## 8. H6 — ORB-05-R jest argumentem za M20, a nie za H-MEM-1

W tej kwestii Net i Memory są zasadniczo zgodne i warto utrzymać ich ostrożność.

- 425 klas trajektorii i 209 klas stanów końcowych pokazuje, że stan końcowy nie determinuje pełnej historii w konkretnym protokole.
- Wynik zależy od określonej kolejności aktualizacji, długości T, tolerancji/zaokrąglenia i metryki RMS.
- Naprawa parametru order usuwa konkretny błąd implementacji; nie rozstrzyga starego ORB-04 (~18 klas).
- ARI=1 dla wybranych par nie dowodzi ogólnej niezależności partycji od D₀.
- Zbiór klas trajektorii M_traj i zbiór klas ω-granicznych M_ω to różne obiekty.

**Wniosek:** nie przenosić ORB-05-R do argumentacji dowodzącej H-MEM-1. Jego właściwym zadaniem jest motywować konstrukcję M20 — kanonicznej relacji równoważności pełnych trajektorii.

---

## 9. Kolejność testów dla laboratorium

| Kolejność | Zadanie | Minimalny wynik potrzebny do przejścia dalej |
|---|---|---|
| 1 — P0 | Rozdzielić generatory przejścia od obserwatorów; rozstrzygnąć, czy P_cyc może występować w słowach dynamiki | Jednoznaczne X, T, H i dopuszczalny język słów |
| 2 — P0 | Zdefiniować semantykę harmonogramu/fairness | Jawne warunki użycia A, K₂ i detektora; wyjaśnienie, co oznacza „po wygaszeniu” |
| 3 — P1 | Przeformułować H-MEM-1 dla jednego ustalonego operatora/mostu | Kwantyfikatory: dla jakiego X, O, mostu, K₂ i jakiej klasy harmonogramów |
| 4 — P1 | Test różnych warunków początkowych przy tym samym O | Co najmniej dwie rozłączne, uzasadnione ω-klasy, nie tylko różne końce przebiegów |
| 5 — P2 | Sprawdzić ograniczoność i niepustość ω-granic | Zbiór pochłaniający albo jawna obsługa pustych ω-granic |
| 6 — P2 | Replikować M16a/ORB-05-R z pełną specyfikacją | Dokładny most B, kolejność GS, tryb K₂, seed, D₀, T, δ, tolerancje i rozdzielenie ORB-04 |
| 7 — P3 | Opracować M20 | Metryka trajektorii odporna na skalę czasu, długość T i czysto numeryczne różnice |

## 10. Najważniejsze pytania do laboratorium

1. Czy P_cyc ma być generatorem transformacji stanu, czy tylko detektorem? Jeśli detektorem, dlaczego należy do monoidu słów?
2. Czy ω_𝔒 ma opisywać wszystkie możliwe przeploty operatorów, czy tylko trajektorie według protokołu, w którym A rzeczywiście wygasza stan?
3. Czy H-MEM-1 dotyczy wielu warunków początkowych dla jednego ustalonego operatora, czy porównania różnych mostów i trybów K₂? Obecny materiał eksperymentalny obejmuje oba pytania, ale nie są one równoważne.
4. Czy istnieje dowód, że rozbieżne próby M16/M16a prowadzą do różnych ω-granic, a nie tylko do różnych wyników w skończonym oknie?

## 11. Ostateczny wniosek audytowy

- **Transfer Memory → Net:** zasadniczo wierny; nie stwierdziłem zmiany rdzenia formalizmu. Net jest kontynuatorem, Memory pozostaje źródłem pełnych specyfikacji eksperymentalnych.
- **H-MEM-1:** program pozostaje interesujący, ale testowalna wersja wymaga doprecyzowania generatorów, obserwatorów, języka słów i kwantyfikatorów.
- **Najsilniejszy problem:** P_cyc jest operatorem idempotentnym i detekcyjnym, lecz w definicji semigrupy traktowany jest jak zwykły generator; dowolne słowa dopuszczają jego wielokrotne stosowanie bez A.
- **Drugi problem:** eksperymenty most×tryb K₂ porównują różne realizacje, nie dowodzą automatycznie wielu ω-klas w obrębie jednego ustalonego 𝔒.
- **ORB-05-R i M17:** dostarczają motywacji dla pamięci trajektorii, ale nie dowodu H-MEM-1 w wersji ω-granicznej.

Nie zmieniono statusów, treści korzeni ani gałęzi main. Raport jest zestawem pytań i testów dla laboratorium, nie decyzją kanoniczną.
