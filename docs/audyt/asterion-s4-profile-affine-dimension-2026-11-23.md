# S4 działające na czterech profilach wymusza wymiar afiniczny 3

**Data:** 2026-11-23  
**Zakres:** matematyczny most między profilem relacyjnym, symetrią K₄ i geometrią 3D.  
**Status:** twierdzenie warunkowe ✅; spełnienie warunków przez N-R2 pozostaje 💡.

## 1. Twierdzenie

Niech (P={p_1,p_2,p_3,p_4}) będzie zbiorem czterech różnych punktów w rzeczywistej przestrzeni afinicznej. Załóżmy, że pełna grupa symetryczna (S_4) działa na (P) przez afiniczne automorfizmy otoczki afinicznej (operatorname{aff}(P)), zgodnie z naturalnym działaniem przez permutacje czterech profili.

Wtedy:
[
oxed{dimoperatorname{aff}(P)=3.}
]
W szczególności cztery profile są afinicznie niezależne.

To jest mocniejsze od samego warunku „cztery profile istnieją”. Pełna, wierna symetria (S_4) usuwa możliwość ich współpłaszczyznowości.

## 2. Dowód przez reprezentację standardową

Niech
[
ar p=rac14(p_1+p_2+p_3+p_4)
]
będzie barycentrum. Jest ono ustalone przez wszystkie permutacje, więc po przesunięciu początku do (ar p) afiniczne działanie (S_4) staje się liniowym działaniem na
[
W=operatorname{span}{p_i-ar p:i=1,ldots,4}.
]

Rozważmy standardową reprezentację:
[
V={xinmathbb R^4:x_1+x_2+x_3+x_4=0}.
]
Ma ona wymiar 3 i jest nieredukowalną rzeczywistą reprezentacją (S_4).

Definiujemy mapę:
[
T:Vlongrightarrow W,qquad
T(x)=sum_{i=1}^4x_i p_i.
]
Ponieważ (sum_i x_i=0), mapa nie zależy od wyboru początku afinicznego. Jest (S_4)-ekwiwariantna względem naturalnego działania permutacyjnego na współrzędnych i założonego działania na profilach.

Mapa (T) jest surjektywna: obrazy wektorów (e_i-e_j) to (p_i-p_j), a te rozpinają (W).

Jądro (ker T) jest podprzestrzenią niezmienniczą reprezentacji (V). Nieredukowalność (V) daje:
[
ker T={0}quad	ext{albo}quadker T=V.
]
Drugi przypadek oznaczałby (T=0), a więc (p_i=p_j) dla wszystkich (i,j), wbrew założeniu, że profile są różne. Zatem (ker T=0), czyli (T) jest izomorfizmem:
[
Wcong V,qquad dim W=3.
]
To kończy dowód.

## 3. Dlaczego samo (V_4) nie wystarcza

Niech cztery profile będą wierzchołkami kwadratu:
[
p_{00}=(1,1),quad p_{10}=(-1,1),quad
p_{01}=(1,-1),quad p_{11}=(-1,-1).
]
Działania
[
a(x,y)=(-x,y),qquad b(x,y)=(x,-y)
]
są komutującymi inwolucjami. Generują grupę
[
langle a,banglecong C_2	imes C_2=V_4,
]
która działa wiernie, regularnie i przechodnio na czterech profilach. Mimo to ich otoczka afiniczna ma wymiar 2.

Zatem:
- cztery profile + regularne działanie (V_4) nie wymuszają 3D;
- cztery profile + pełne afiniczne działanie (S_4) wymuszają dokładnie 3D.

To rozróżnienie jest istotne wobec wcześniejszego wyniku, że trzy nieidentycznościowe elementy normalnej podgrupy (V_4	riangleleft S_4) kodują trzy parowania. Sama obecność tych trzech inwolucji nie wystarcza; potrzebna jest pełna symetria (S_4) działająca na czterech profilach.

## 4. Odwrócenie twierdzenia

Jeżeli cztery punkty są afinicznie niezależne, to każda permutacja tych punktów przedłuża się jednoznacznie do afinicznego automorfizmu ich trójwymiarowej otoczki. Otrzymujemy więc wierne działanie (S_4).

W tym sensie dla czterech różnych profili zachodzi równoważność:

[
oxed{
egin{aligned}
&	ext{pełne naturalne działanie }S_4	ext{ przez afiniczne automorfizmy}\
&qquadLongleftrightarrow\
&	ext{afiniczna niezależność czterech profili}\
&qquadLongleftrightarrow\
&dimoperatorname{aff}(P)=3.
end{aligned}}
]

Pierwsza równoważność rozumiana jest przy założeniu, że działanie (S_4) jest wierne i permutuje cztery profile naturalnie.

## 5. Znaczenie dla P₀

W korzeniach P₀ mamy już kandydatów na dwa składniki:
- K₄/Centroid dostarcza naturalnego działania permutacyjnego (S_4) na czterech indeksach/generatorach;
- Axis/Defect identyfikują strukturę (V_4) i trzy parowania.

Ale nie wolno wykonać skrótu:
[
operatorname{Aut}(mathfrak g_4;{M_i})cong S_4
quad
otRightarrowquad
	ext{N-R2 wyprowadziło cztery profile}.
]
Pierwsza grupa jest automorfizmem już zadanego układu czterech generatorów. N-R2 ma dopiero wyprowadzić profile z pierwotnej relacji.

Potrzebny most musi wykazać kolejno:
1. cztery profile powstają jako klasy relacyjnej nierozróżnialności, a nie jako cztery zadane węzły;
2. pełna grupa automorfizmów pierwotnej struktury indukuje na tych klasach naturalne, wierne działanie (S_4);
3. istnieje kanoniczna mapa profili do przestrzeni afinicznej, ekwiwariantna względem tego działania.

Jeżeli te trzy punkty zostaną udowodnione, wymiar 3 nie będzie już dodatkowym postulatem geometrycznym — wynika z reprezentacji standardowej (S_4).

## 6. Statusy

- **✅** Cztery różne profile z pełnym naturalnym działaniem afinicznym (S_4) mają dokładnie trójwymiarową otoczkę afiniczną.
- **✅** Dowód wynika z nieredukowalności standardowej reprezentacji (S_4).
- **✅** Samo regularne działanie (V_4) nie wymusza 3D; kwadrat jest kontrprzykładem.
- **🔍** Wcześniejsze (S_4) z Centroidu jest działaniem na rodzinie zadanych generatorów; nie jest jeszcze działaniem na wyprowadzonych profilach N-R2.
- **💡** Jeśli N-R2 odzyska cztery profile i naturalne (S_4), geometria 3D będzie twierdzeniem, a nie założeniem.

**Werdykt:** to jest najsilniejszy dotąd kandydat na matematyczny most między „cztery” i „3D”. Nie dowodzi jeszcze emergencji czterech profili, ale redukuje geometrię do konkretnego zadania algebraicznego: wyprowadzić z pierwotnej relacji cztery klasy, na których działa pełne (S_4), a nie tylko (V_4).

## 7. Integralność repo

Raport zapisano na gałęzi audytowej `audit/asterion-continuation-2026-11-20`. Gałąź pozostaje rozbieżna z `main`; nie wykonano merge ani rebase. `main` nie został zmieniony. MVP-02 pozostaje poza zakresem.
