# N-R2: dwie algebry kompozycji — sekwencja aktów i algebra stabilnych profili

**Data:** 2026-11-23  
**Zakres:** matematyczne korzenie P₀; N-R2. MVP-02 poza zakresem.  
**Gałąź:** \`audit/asterion-continuation-2026-11-20\`  
**Punkty odniesienia:** P₀-Relacje v0.3 §§1–8; P₀-Centroid v5.2; P₀-Scalar v0.3.5; P₀-TAU v1.7.2; wcześniejsze raporty o wspólnych stabilnych profilach.  
**Status:** abstrakcyjny warunek profilo-dokładności daje łączną częściową kompozycję ✅; Centroid spełnia go dla dodatnich słów ✅; Scalar spełnia go dla stałografowych rund i dla punktów stałych jednej pełnej rundy lokalnej A2 ✅; nie zachodzi automatycznie dla ogólnych map stochastycznych ❌/kontrprzykład; Alchemy nie ma jeszcze profilo-dokładnego opisu w tej klasie 🔍/otwarte; n=4 wynika warunkowo z dokładnie jednego profilu resztkowego w parze Centroidu, ale nie z ogólnej algebry profili.

## 1. Rozdzielenie dwóch praw

Dotychczasowa analiza mieszała dwa pytania:

1. **Prawo czasowe:** jaka jest wartość wyniku, gdy najpierw wykonujemy akt A, a potem B?
2. **Prawo profilowe:** jakie rozróżnienia pozostają stabilne po obu aktach?

Prawo czasowe jest zwykle nieprzemienne:

\[
A;B\longleftrightarrow T_B T_A,
\qquad
B;A\longleftrightarrow T_A T_B.
\]

Prawo profilowe może być przemienne, ponieważ „to, co przetrwało oba akty”, jest przecięciem:

\[
\Phi(A;B)=\Phi(A)\cap\Phi(B).
\]

Nie są to konkurencyjne opisy tej samej operacji. Pierwszy zapisuje historię, drugi zapisuje stabilną strukturę pozostałą po historii.

To rozdzielenie jest zgodne z napięciem N-R2: τ/TAU potrzebuje kolejności, natomiast rekonstrukcja profili potrzebuje niezmienników.

## 2. Definicja profilo-dokładności

Niech akty działają na wspólnej przestrzeni konfiguracji Q. Dla aktu A oznaczmy jego profil stabilny:

\[
\Phi(A)=\operatorname{Fix}(A)
\]

albo, jeśli istnieje wyróżniony trywialny profil wspólny, jego ilorazową wersję po usunięciu tego profilu.

Rodzina aktów jest **profilowo dokładna**, jeśli dla każdej dopuszczalnej pary A,B:

\[
\boxed{\Phi(BA)=\Phi(A)\cap\Phi(B).}
\tag{PE}
\]

Warunek mówi, że złożony akt zachowuje dokładnie te konfiguracje, które każdy z dwóch aktów zachowuje osobno. Nie tworzy nowych stabilnych profili przez przypadkowe znoszenie się zmian.

Własność (PE) nie jest prawdziwa dla dowolnych przekształceń. Jest dodatkową własnością określonej rodziny dynamik.

## 3. Twierdzenie: profilowo dokładna rodzina daje łączne prawo częściowe

Załóżmy, że rodzina aktów jest domknięta na kompozycję i spełnia (PE). Definiujemy:

\[
A\diamond B=
\begin{cases}
BA,&\Phi(A)\cap\Phi(B)\ne\bot,\\
\text{nieokreślone},&\Phi(A)\cap\Phi(B)=\bot,
\end{cases}
\]

gdzie \(\bot\) oznacza brak niebanalnego profilu (np. tylko globalną stałą lub profil zerowy).

Dla trzech aktów A,B,C:

\[
\Phi((C\diamond B)\diamond A)
=
\Phi(A)\cap\Phi(B)\cap\Phi(C),
\]

oraz:

\[
\Phi(C\diamond(B\diamond A))
=
\Phi(A)\cap\Phi(B)\cap\Phi(C).
\]

Obie strony są określone dokładnie wtedy, gdy potrójne przecięcie jest różne od \(\bot\). Jeżeli są określone, wartości operatorowe są równe, ponieważ zwykła kompozycja przekształceń jest łączna:

\[
(T_C T_B)T_A=T_C(T_B T_A).
\]

**Wniosek ✅:** jeżeli rodzina aktów ma dokładny profil przecięcia, to kompozytowalność zdefiniowana przez niebanalny wspólny profil jest silnie łączna.

Profilowa część kompozycji jest meet-semilattice (przecięcie jest łączne, przemienne i idempotentne). Część czasowa pozostaje uporządkowana i nieprzemienna.

## 4. Przykład I — Centroid spełnia (PE)

Pracujemy na ilorazie przez wspólną linię konsensusu:

\[
\mathcal Q=\mathbb R^n/\langle\mathbf1\rangle.
\]

Dla dodatniego słowa P w generatorach \(M_i\), niech I(P) będzie zbiorem różnych indeksów użytych w słowie, a J(P) jego dopełnieniem.

Wcześniejszy rachunek daje:

\[
\Phi(P)=
\left\{x\in\mathbf1^\perp:
x_i=0\ (i\in I(P)),\
\sum_{j\in J(P)}x_j=0
\right\},
\]

z wymiarem:

\[
\dim\Phi(P)=\max(n-|I(P)|-1,0).
\]

Dla dwóch słów P,Q indeksy użyte w produkcie QP to:

\[
I(QP)=I(P)\cup I(Q).
\]

Stąd bezpośrednio:

\[
\boxed{\Phi(QP)=\Phi(P)\cap\Phi(Q).}
\]

Centroid spełnia zatem (PE) dla dodatniej półgrupy słów w swoich generatorach.

### Konsekwencja n=4

Dla dwóch różnych pojedynczych generatorów \(M_i,M_j\):

\[
\dim\Phi(M_jM_i)=n-3.
\]

| n | Wymiar profilu po dwóch różnych aktach |
|---:|---:|
| 2 | 0 |
| 3 | 0 |
| 4 | 1 |
| 5 | 2 |
| 6 | 3 |

Jeżeli wymagamy jedynie niezerowego profilu, minimalnym n jest 4. Jeżeli wymagamy **dokładnie jednego** niezależnego profilu, w rodzinie Centroidu n=4 jest jedynym rozwiązaniem.

To jest warunkowy selektor czterech: wymaga uzasadnienia, dlaczego po dwóch różnych aktach ma pozostać dokładnie jeden stopień swobody relacyjnej. Sama algebra Centroidu daje rachunek, nie uzasadnia jeszcze tego kryterium ontologicznego.

## 5. Przykład II — Scalar spełnia (PE), ale nie wybiera n=4

Dla pełnej rundy na ustalonym grafie G:

\[
\Phi(R_G)=
\{x:x\text{ jest stały na każdej składowej G}\}
/\langle\mathbf1\rangle.
\]

Dla sekwencji rund na grafach \(G_1,\ldots,G_m\), wcześniej dowiedziono:

\[
\Phi(R_{G_m}\cdots R_{G_1})
=
\bigcap_{s=1}^m\Phi(R_{G_s}).
\]

To jest (PE). Wartość profilu jest równoważna przestrzeni kontrastów między składowymi grafu-unii.

Jednak wymiar:

\[
\dim\Phi(R_G)=c(G)-1
\]

zależy od liczby składowych, nie od n. Dla każdego n≥2 można wybrać G z dokładnie dwiema składowymi i otrzymać dokładnie jeden niebanalny profil.

Zatem dokładnie jednowymiarowy profil resztkowy występuje w Scalar dla n=3,4,5,… . Kryterium „jeden profil po dwóch aktach” nie wybiera czterech w ogólnym formalizmie relacyjnym.

Dodatkowo dla rzeczywistego progowego A2, gdzie graf może zmieniać się w obrębie rundy, punkty stałe pojedynczej pełnej rundy są przecięciem punktów stałych lokalnych kroków. To rozszerza wynik na poziom punktów stałych, ale nie dowodzi automatycznie (PE) dla kompozycji wielu nieliniowych rund.

## 6. Kontrprzykład: (PE) nie wynika z samej stochastyczności

Niech:

\[
A=
\begin{pmatrix}
1&0&0\\
1/2&1/2&0\\
0&0&1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
1&0&0\\
0&1/2&1/2\\
0&0&1
\end{pmatrix}.
\]

Obie macierze są wierszowo-stochastyczne i mają dodatnią diagonalę.

Punkty stałe:
- Fix(A): \(x_1=x_0\), a \(x_2\) jest dowolne;
- Fix(B): \(x_1=x_2\), a \(x_0\) jest dowolne;
- Fix(A)∩Fix(B): wyłącznie wektory stałe.

Iloczyn:

\[
AB=
\begin{pmatrix}
1&0&0\\
1/2&1/4&1/4\\
0&0&1
\end{pmatrix}.
\]

Punkty stałe AB spełniają:

\[
x_1=\frac{2x_0+x_2}{3}.
\]

To jest przestrzeń dwuwymiarowa, większa niż Fix(A)∩Fix(B), która ma wymiar 1. Po usunięciu wspólnej stałej iloczyn ma niezerowy profil, chociaż przecięcie profili czynników jest trywialne.

Zatem:

\[
\operatorname{Fix}(AB)\ne\operatorname{Fix}(A)\cap\operatorname{Fix}(B).
\]

**Wniosek ❌:** sam fakt, że akty są stochastyczne, mają dodatnią diagonalę i reprezentują uśrednianie, nie gwarantuje (PE). Potrzebna jest silniejsza własność dynamiki, jak ta wykazana dla konkretnych rodzin Centroidu i Scalar.

## 7. Konsekwencja dla Alchemy

P₀-Alchemy nie mieści się obecnie w tej samej klasie:
- krok K₁ zachowuje centroid, lecz po usunięciu translacji skaluje kształt przez \(1-\alpha\);
- nie ma niezerowego liniowego profilu kształtu stałego dla K₁;
- atraktor K jest orbitą obrotową, a nie punktem stałym konfiguracji;
- stała sygnatura odległościowa atraktora jest niezmiennikiem granicznego ruchu, nie udowodnioną globalną przestrzenią punktów stałych.

Możliwe, że dla Alchemy odpowiednią \(\Phi\) jest niezmienniczy zbiór orbit, nie liniowa przestrzeń. Ale nie ma jeszcze dowodu, że jego złożenie spełnia (PE).

Nie należy na siłę unifikować tych korzeni pod jednym pojęciem niezmiennika.

## 8. Proponowany szkielet N-R2

Najbardziej oszczędny formalizm, do którego doszliśmy, składa się z dwóch warstw:

**Warstwa A — sekwencja**
\[
A_1,A_2,\ldots,A_k
\quad\longmapsto\quad
T_{A_k}\cdots T_{A_1}.
\]

Zapisuje kolejność i czas.

**Warstwa B — stabilny profil**
\[
\Phi(A_1,\ldots,A_k)
=
\bigcap_{j=1}^k\Phi(A_j)
\]
w klasie aktów spełniających (PE).

Zapisuje rozróżnienia, które przetrwały wszystkie akty.

Reguła kompozycji jest wtedy:

\[
\text{A i B mogą współtworzyć stabilny opis}
\iff
\Phi(A)\cap\Phi(B)\ne\bot.
\]

Nie jest to jeszcze pierwotna definicja P₀. Jest to minimalny formalizm pośredni, który:
- nie używa jawnych źródeł i celów;
- zachowuje kolejność w warstwie czasowej;
- rekonstruuje stabilne profile w warstwie strukturalnej;
- daje łączność tam, gdzie (PE) jest dowiedzione.

## 9. Co pozostaje do wyprowadzenia

N-R2 nie jest już pytaniem „jak wymyślić łączne działanie?”. Mamy kilka dokładnych konstrukcji i znamy ich warunki.

Pozostają trzy trudniejsze pytania:
1. Czy P₀-Relacje v0.3 może wyprowadzić samą przestrzeń konfiguracji, zamiast zakładać ją w \(R_t\)?
2. Czy profil \(\Phi(A)\) można zdefiniować jako relację nierozróżnialności bez użycia indeksów i współrzędnych?
3. Czy warunek (PE) wynika z zasady relacyjnej kompensacji, czy jest dodatkowym aksjomatem selekcji klas modeli?

Dopiero odpowiedź na te pytania pozwoli stwierdzić, czy algebra profili jest korzeniem, czy tylko narzędziem opisu Centroidu i Scalar.

## 10. Werdykt

- **✅** Profilowo dokładna rodzina aktów daje łączne częściowe prawo kompozycji przez niebanalne przecięcie profili.
- **✅** Dodatnia półgrupa Centroidu spełnia (PE).
- **✅** Stałografowe rundy Scalar i ich dowolne sekwencje spełniają (PE); pojedyncza pełna runda dynamicznego A2 ma przecięcie punktów stałych lokalnych kroków.
- **❌** (PE) nie wynika z samej stochastyczności, dodatniej diagonali ani ogólnego pojęcia uśredniania.
- **🔍** Alchemy wymaga innego, prawdopodobnie orbitowego pojęcia profilu.
- **❌** Ogólna algebra profili nie wybiera n=4; warunkowy wybór n=4 występuje w Centroidzie, gdy wymagamy dokładnie jednego profilu po dwóch różnych aktach.
- **💡** N-R2 może wymagać dwóch sprzężonych algebr: nieprzemiennej algebry sekwencji i przemiennej algebry stabilnych profili.

## 11. Następny krok

Należy wrócić do P₀-Relacje §1 i §7 i zadać pytanie, czy „relacja jako proces” może wyznaczyć zbiór konfiguracji i profil stabilny bez wprowadzania V lub \(X\times X\). Jeżeli nie, trzeba jasno wskazać minimalny dodatkowy aksjomat, który ten nośnik generuje — zamiast ukrywać go w notacji.

MVP-02 pozostaje poza zakresem; bez merge/rebase z main.
