# N-R2: stabilne konfiguracje, przecięcie profili i łączność między rundami

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Punkty odniesienia:** P₀-Centroid v5.2; P₀-Scalar v0.3.5 §§2–4; P₀-TAU v1.7.2; poprzednie raporty Asteriona o wspólnych niezmiennikach.  
**Status:** dla Scalar z ustalonym grafem runda zachowuje wzorce stałe na składowych ✅; dla sekwencji różnych grafów przestrzeń punktów stałych jest przecięciem ✅; prawo częściowej kompozycji przez wspólny niezmiennik jest łączne ✅ w tej klasie; lewa przestrzeń niezmienników nie spełnia analogicznej reguły przy zmianie grafu ❌/kontrprzykład; n=4 nie jest wybierane przez Scalar ✅/kontrmodel; przeniesienie na graf zmieniający się wewnątrz rundy otwarte 🔍.

## 1. Korekta pojęciowa: zachowana obserwabla a zachowana konfiguracja

Dotychczas używaliśmy dwóch pojęć, które trzeba rozdzielić:

- lewy niezmiennik \(w^T A=w^T\): zachowana liniowa obserwabla / waga;
- prawy punkt stały \(Ax=x\): konfiguracja, która po akcie pozostaje niezmieniona.

Dla pojedynczego operatora i niektórych rodzin oba opisy mają tę samą liczność, ale przy składaniu różnych operatorów nie muszą się zachowywać tak samo.

Dla relacyjnej kompozycji bardziej naturalnym kandydatem na „profil, który przetrwał” jest **prawy punkt stały**, czyli konfiguracja stabilna pod działaniem aktu.

W macierzach stochastycznych stała konfiguracja \(\mathbf1\) jest trywialna. Dlatego pracujemy w przestrzeni ilorazowej:

\[
\mathcal Q=\mathbb R^n/\langle\mathbf1\rangle.
\]

Dla operatora wierszowo-stochastycznego A oznaczmy:

\[
\mathcal S(A)=\operatorname{Fix}(\bar A),
\]

gdzie \(\bar A\) jest działaniem indukowanym na \(\mathcal Q\).

Ponieważ A jest stochastyczna i \(\|A^k x\|_\infty\le\|x\|_\infty\), warunek \(\bar A[x]=[x]\) implikuje \(Ax=x\): gdyby \(Ax=x+c\mathbf1\), to \(A^k x=x+kc\mathbf1\), co przy \(c\ne0\) przeczyłoby ograniczoności. Zatem:

\[
\mathcal S(A)=\operatorname{Fix}(A)/\langle\mathbf1\rangle.
\]

To jest przestrzeń stabilnych rozróżnień po usunięciu wspólnego przesunięcia.

## 2. Runda Scalar na stałym grafie

Niech G będzie ustalonym, nieskierowanym grafem na \(V=\{1,\ldots,n\}\). Lokalny krok A2 w wierzchołku i aktualizuje \(r_i\) do średniej wartości na zamkniętym sąsiedztwie \(\{i\}\cup N_G(i)\), pozostałe współrzędne pozostawiając bez zmian.

Niech \(U_i(G)\) będzie macierzą tego kroku, a pełna runda w dowolnej ustalonej kolejności:

\[
R_G=U_{i_n}(G)\cdots U_{i_1}(G).
\]

Każdy U_i(G) jest wierszowo-stochastyczny, ma dodatni wpis diagonalny i nie miesza różnych składowych G. Ich iloczyn zachowuje te własności.

### Lemat o nośniku rundy

Dla każdej krawędzi \(\{i,j\}\in E(G)\):

\[
(R_G)_{ij}>0,\qquad(R_G)_{ji}>0.
\]

Uzasadnienie: w kroku aktualizacji i, wiersz i otrzymuje dodatni udział bieżącej współrzędnej j. Dodatnie wpisy diagonalne późniejszych kroków zachowują ten wpływ do końca rundy. W kierunku przeciwnym:
- jeśli j jest aktualizowany po i, jego krok uwzględnia już zmienioną wartość i, która zawiera dodatni udział pierwotnego i;
- jeśli j jest aktualizowany przed i, analogiczny argument działa w odwrotnej kolejności.

Nie ma też wpisów łączących różne składowe G, ponieważ żaden lokalny krok nie korzysta z wierzchołka spoza swojej składowej.

Wobec tego skierowany graf dodatniego nośnika R_G ma dokładnie te same silnie spójne składowe, co nieskierowany graf G: każda krawędź G pojawia się w obu kierunkach, a przejścia między składowymi są niemożliwe.

### Twierdzenie o punktach stałych Scalar

Dla wierszowo-stochastycznej macierzy o zamkniętych, silnie spójnych klasach komunikacji wektory stałe są dokładnie stałe na każdej takiej klasie. Stąd:

\[
\boxed{
\operatorname{Fix}(R_G)=
\{x\in\mathbb R^n:
x_i=x_j\text{ w każdej składowej G}\}.
}
\]

Jeśli \(c(G)\) oznacza liczbę składowych spójności G, to:

\[
\dim\mathcal S(R_G)=c(G)-1.
\]

Nie jest to liczba zachowanych wag, lecz liczba niezależnych kontrastów między stabilnymi domenami.

## 3. Zmiana grafu między pełnymi rundami

Niech \(G_1,\ldots,G_m\) będą różnymi ustalonymi grafami, każdy utrzymany przez całą swoją pełną rundę. Rozważmy:

\[
P=R_{G_m}\cdots R_{G_1}.
\]

Każda runda jest wierszowo-stochastyczna i ma dodatnią diagonalę. Jeśli \((R_{G_s})_{ij}>0\), to w produkcie P również \(P_{ij}>0\): w pozostałych czynnikach można pozostać na i przed krokiem s i na j po kroku s, korzystając z dodatnich wpisów diagonalnych.

Zatem dodatni nośnik P zawiera obustronne krawędzie wszystkich grafów \(G_s\). Jednocześnie P nie może przenieść wpływu pomiędzy różne składowe grafu-unii:

\[
G_\cup=G_1\cup\cdots\cup G_m.
\]

Silnie spójne klasy dodatniego nośnika P są więc dokładnie składowymi spójności \(G_\cup\).

Dostajemy:

\[
\operatorname{Fix}(P)
=\operatorname{Const}(\operatorname{Comp}(G_\cup)).
\]

Ale konfiguracja jest stała na każdej składowej G_\cup dokładnie wtedy, gdy jest stała na składowych każdego \(G_s\). Zatem:

\[
\boxed{
\operatorname{Fix}(R_{G_m}\cdots R_{G_1})
=
\bigcap_{s=1}^m\operatorname{Fix}(R_{G_s}).
}
\]

Po przejściu do ilorazu przez wspólną stałą:

\[
\boxed{
\mathcal S(R_{G_m}\cdots R_{G_1})
=
\bigcap_{s=1}^m\mathcal S(R_{G_s}).
}
\]

Tożsamość jest dokładna dla dowolnej liczby rund i dowolnej sekwencji ustalonych grafów.

## 4. Częściowa kompozycja przez wspólny stabilny profil

Dla produktów pełnych rund na stałych grafach definiujemy:

\[
A\diamond B=
\begin{cases}
BA,&\mathcal S(A)\cap\mathcal S(B)\ne\{0\},\\
\text{nieokreślone},&\mathcal S(A)\cap\mathcal S(B)=\{0\}.
\end{cases}
\]

Z §3:

\[
\mathcal S(BA)=\mathcal S(A)\cap\mathcal S(B).
\]

Dla trzech produktów A,B,C obie strony:

\[
(A\diamond B)\diamond C,\qquad
A\diamond(B\diamond C)
\]

są określone dokładnie wtedy, gdy:

\[
\mathcal S(A)\cap\mathcal S(B)\cap\mathcal S(C)\ne\{0\}.
\]

Jeśli są określone, obie dają ten sam zwykły iloczyn operatorów, z zachowaniem kolejności.

**Wynik ✅:** dla tej klasy aktów wspólna niezerowa stabilna konfiguracja wyznacza łączne częściowe prawo kompozycji.

Predykat kompozytowalności jest symetryczny, bo przecięcie jest symetryczne; sama wartość produktu nadal zależy od kolejności. Zatem ta reguła wyznacza możliwość współistnienia w jednym stabilnym opisie, ale sama nie nadaje kierunku czasowego.

## 5. Jawny kontrmodel n=4: prawa przestrzeń stała działa, lewa nie

Weźmy n=4.

Pierwszy graf:

\[
G_1=\{\{0,1\}\}\cup\{\{2\},\{3\}\}.
\]

Drugi:

\[
G_2=\{\{0,2\},\{2,1\}\}\cup\{\{3\}\}.
\]

Przy kolejności aktualizacji 0,1,2,3 pełne macierze rund wynoszą:

\[
R_{G_1}=
\begin{pmatrix}
1/2&1/2&0&0\\
1/4&3/4&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
\]

\[
R_{G_2}=
\begin{pmatrix}
1/2&0&1/2&0\\
0&1/2&1/2&0\\
1/6&1/6&2/3&0\\
0&0&0&1
\end{pmatrix}.
\]

Ich iloczyn:

\[
R_{G_2}R_{G_1}=
\begin{pmatrix}
1/4&1/4&1/2&0\\
1/8&3/8&1/2&0\\
1/8&5/24&2/3&0\\
0&0&0&1
\end{pmatrix}.
\]

Punkty stałe:
- \(\operatorname{Fix}(R_{G_1})\): \(x_0=x_1\);
- \(\operatorname{Fix}(R_{G_2})\): \(x_0=x_1=x_2\);
- \(\operatorname{Fix}(R_{G_2}R_{G_1})\): \(x_0=x_1=x_2\).

A więc prawy punkt stały produktu jest dokładnie przecięciem prawych przestrzeni stałych czynników.

Jednak analogiczna teza dla lewych niezmienników \(w^TA=w^T\) jest fałszywa:
- przecięcie lewych przestrzeni stałych \(R_{G_1}\) i \(R_{G_2}\) jest rozpięte wyłącznie przez \(e_3^T\);
- lewa przestrzeń stała produktu ma dodatkowy wektor proporcjonalny do \((5/21,3/7,1,0)\).

Wniosek: dla kompozycji zmiennych grafów poprawnym kandydatem na przetrwały profil jest przestrzeń stabilnych konfiguracji, a nie przestrzeń zachowanych funkcjonałów liniowych.

## 6. Czy ten wynik wybiera cztery?

Nie. Dla dowolnego n≥2 można wybrać graf o dokładnie dwóch składowych — na przykład ścieżkę na n−1 wierzchołkach i jeden izolowany wierzchołek. Wtedy:

\[
\dim\mathcal S(R_G)=2-1=1.
\]

Konkretnie:
- n=3: \(P_2+K_1\), jeden zachowany kontrast;
- n=4: \(P_3+K_1\), jeden zachowany kontrast;
- n=5: \(P_4+K_1\), jeden zachowany kontrast.

Tak więc warunek „zostaje dokładnie jeden niezerowy profil” nie wybiera n=4 w Scalar.

To jest ważny kontrmodel dla każdej próby wyprowadzenia K₄ wyłącznie z łączności lub minimalnej liczby stabilnych kontrastów.

## 7. Porównanie z Centroidem

W dodatnim semigroupeneratorowym Centroidzie również można użyć prawych punktów stałych na ilorazie przez \(\langle\mathbf1\rangle\).

Dla słowa P z użytym zbiorem generatorów I i nieużytym zbiorem J:

\[
\mathcal S(P)=
\{x\in\mathcal Q:
\text{istnieje reprezentant } \tilde x
\text{ z }\tilde x_i=0\ (i\in I),
\sum_{j\in J}\tilde x_j=0\}.
\]

Jej wymiar wynosi:

\[
\dim\mathcal S(P)=\max(n-|I|-1,0).
\]

Dla dwóch dodatnich słów P,Q zbiór użytych generatorów produktu QP jest unią użytych zbiorów, zatem:

\[
\boxed{\mathcal S(QP)=\mathcal S(P)\cap\mathcal S(Q).}
\]

W Centroidzie i w stałografowym Scalar występuje więc ten sam abstrakcyjny wzorzec:

- akt wyznacza przestrzeń konfiguracji, które pozostają stabilne;
- wspólna stabilna przestrzeń określa dopuszczalność kompozycji;
- kompozycja redukuje przestrzeń do przecięcia;
- przecięcie jest łączne.

Różni się jednak geometria profili:
- Centroid: po aktualizacjach pozostają kontrasty na współrzędnych nieużytych;
- Scalar: pozostają wzorce stałe na składowych grafu-unii.

To jest wspólna algebra stabilnych profili, nie identyczność mechanizmów.

## 8. Granica wyniku: graf zmienny wewnątrz rundy

P₀-Scalar ma graf progowy zależny od aktualnego stanu. Jeśli po aktualizacji jednej współrzędnej sąsiedztwo kolejnego wierzchołka zmienia się jeszcze w tej samej rundzie, cała runda nie jest już \(R_G\) dla jednego ustalonego G.

Dowód z §§2–4 obejmuje:
- rundy, w których graf zostaje zamrożony na czas całej rundy;
- dowolną sekwencję takich rund z różnymi grafami.

Nie obejmuje automatycznie:
- harmonogramu, w którym graf jest przeliczany po każdym lokalnym kroku;
- dowolnych niesymetrycznych, częściowych aktualizacji;
- Alchemy z nieliniową korektą progową.

Ten zakres trzeba zachować jawnie. Nie podnoszę statusu całego Scalar.

## 9. Werdykt

- **✅** Dla stałego grafu Scalar przestrzeń punktów stałych pełnej rundy to konfiguracje stałe na składowych grafu.
- **✅** Dla sekwencji pełnych rund na różnych ustalonych grafach przestrzeń punktów stałych produktu jest przecięciem przestrzeni czynników.
- **✅** Wspólna niezerowa stabilna konfiguracja definiuje łączne częściowe prawo kompozycji w tej klasie.
- **✅** Analogiczna reguła prawych przestrzeni stałych zachodzi dla dodatnich słów Centroidu.
- **❌** Lewych niezmienników nie można w ten sam sposób składać przy zmianie grafu — istnieje jawny kontrprzykład n=4.
- **❌** Jednowymiarowa przestrzeń przetrwałych kontrastów nie wybiera n=4 w Scalar; działa także dla n=3 i n=5.
- **🔍** Zastosowanie do rzeczywistego A2 z grafem przeliczanym po każdym lokalnym kroku wymaga osobnego dowodu.
- **💡** „Stabilny profil po akcie” może być wspólnym językiem Centroidu i Scalar, ale nie jest jeszcze wyprowadzony z pierwotnej relacji P₀.

## 10. Następny krok

Teraz trzeba sprawdzić, czy istnieje opis stabilnego profilu, który nie używa ani przestrzeni współrzędnych, ani macierzy stochastycznych:

1. czy profil można zdefiniować wyłącznie jako klasę rozróżnień nierozbijanych przez akty;
2. czy każdy akt indukuje relację równoważności „te konfiguracje stają się nierozróżnialne po akcie”;
3. czy złożenie aktów odpowiada domknięciu przechodniemu / łączeniu tych klas;
4. czy taka konstrukcja zachowuje łączność bez uprzedniego nośnika węzłów.

Dopiero wtedy będzie można powiedzieć, czy wspólna algebra profili jest pierwotna, czy tylko skutkiem konkretnej reprezentacji macierzowej.

MVP-02 pozostaje poza zakresem; nie wykonano merge ani rebase.

## 11. Integralność zakresu

Raport dotyczy matematycznych korzeni N-R2. Zapis wyłącznie na gałęzi audytowej.
