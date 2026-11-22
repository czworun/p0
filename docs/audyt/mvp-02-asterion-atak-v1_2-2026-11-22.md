# MVP-02 v1.2 — audyt matematyczny Asteriona

**Data:** 2026-11-22  
**Zakres:** specyfikacja `docs/mvp-02-spec-v1_2.md` oraz związany z nią Aneks A `docs/mvp-02-spec-v0_4-aneks-a-uzupelnienie.md`.  
**Tryb:** audyt formalny definicji i algorytmów; bez rachunku transportowego.

## 1. Materiał i granice audytu

Pobrano z `main`:

- spec v1.2, Git blob `42b819aa4b56599567f3fa288aa66babef14cf28`, [plik](https://github.com/czworun/p0/blob/main/docs/mvp-02-spec-v1_2.md);
- Aneks A, Git blob `e68906bed162eb6f0aecec416c6bba9e1b655482`, [plik](https://github.com/czworun/p0/blob/main/docs/mvp-02-spec-v0_4-aneks-a-uzupelnienie.md).

Blob Aneksu A jest taki sam jak w poprzednim audycie; w v1.2 nie zmieniono tabel ani formy zamkniętej wag. Nie powtarzam pełnego audytu tych niezmienionych danych.

Nie wykonano obliczeń sup, theta, tau, U_b, F_r ani klasyfikacji kill. Nie wykonywano także rachunku zerowego. §2.5 wymaga publikacji hasha wiążącego kompletu przed rachunkiem. W sprawdzonym pliku nie ma pełnego SHA-256 specyfikacji v1.2, a wcześniejszy zapis przekazany w rozmowie był niepełny. Git blob SHA podany wyżej **nie jest** SHA-256 pliku i go nie zastępuje. K6 pozostaje aktywne.

## 2. Wynik ogólny

**Werdykt: v1.2 nie jest jeszcze gotowa do uznania protokołu za matematycznie domknięty ani do ponownego rachunku transportowego.**

Nowa errata (ad) nie uzasadnia wnioskowania o klasie U_b na podstawie dwóch sparowanych punktów końcowych. Ponadto A.4 nie domyka certyfikacji *pierwszego* przekroczenia na końcowym przedziale po przejściu do zwykłej bisekcji. Są to dwa niezależne blokery.

## 3. Znaleziska krytyczne

### B-01 — errata (ad): dwa końce U_b nie certyfikują przedziału ilorazu

**Status: ❌ BLOCKER**

W (ad) dla każdej orbity wyznacza się U_b(lo) oraz U_b(hi), raportuje jako przedział [U_b(lo), U_b(hi)] i uznaje klasę za rozstrzygniętą, jeżeli klasy na obu końcach są identyczne.

To wnioskowanie jest nieuprawnione. Nawet jeśli tau_surf(theta) i tau_int(theta) są osobno niemalejące względem progu, ich iloraz tau_surf(theta)/tau_int(theta) nie musi być monotoniczny. Zgodność klasy na końcach nie wyklucza zmiany klasy w środku. Sparowanie dolnego progu obu kanałów i górnego progu obu kanałów nie tworzy automatycznie granic dla ilorazu.

Kontrprzykład logiczny, niezależny od modelu P₀: dla x z [0,2] niech t_s(x)=1+x i t_i(x)=1+x². Obie funkcje są niemalejące. Iloraz ma wartość 1 przy x=0, 0.6 przy x=2, ale około 1.207 przy x=0.4. Przy poziomie porównania 1.1 oba końce dają tę samą stronę porównania, a punkt wewnętrzny daje przeciwną.

**Wymagana poprawka:** najpierw wyznaczyć osobne certyfikowane przedziały czasów dla obu kanałów, np. [tau_s^-, tau_s^+] i [tau_i^-, tau_i^+]. Dla dodatniego mianownika bez zera bezpieczne przedziałowe ograniczenie ilorazu to:

- dolna granica: tau_s^- / tau_i^+;
- górna granica: tau_s^+ / tau_i^-.

Jeżeli przedział mianownika obejmuje zero, trzeba zastosować osobną regułę zgodną z B4; nie wolno użyć zwykłego dzielenia przedziałowego. Następnie kill wolno rozstrzygnąć tylko wtedy, gdy **całe** przedziały U_b orbit d5 i d1–d4 spełniają tę samą relację z tolerancją. Gdy możliwe klasy różnią się w dopuszczalnych przedziałach, wynik musi pozostać nierozstrzygnięty.

### B-02 — A.4: bisekcja po pięciu poziomach nie zachowuje „pierwszego” przekroczenia

**Status: ❌ BLOCKER**

A.4 najpierw wykonuje chronologiczny branch-and-bound, ale w danym przedziale siatki ogranicza podział do pięciu poziomów. Potem przechodzi do „bisekcji na przedziale bracketingowym”. Nie ma reguły nakazującej, by każda kolejna lewa połowa bisekcji została certyfikowana jako wolna od przekroczenia, zanim algorytm przejdzie do prawej.

Zwykła bisekcja znaku nie znajduje ogólnie pierwszego zera funkcji niemonotonicznej. Przykład: g(x)=(x−0.1)(x−0.2)(x−0.8) na [0,1]. g(0)<0 i g(1)>0, ale g(0.5)<0. Standardowa bisekcja, która wybiera prawą połowę po sprawdzeniu środka, odrzuca dwa wcześniejsze zera i zbiega do 0.8 zamiast do pierwszego zera 0.1.

W A.4 użyto jedynie ograniczenia Lipschitza. Nie ma założenia monotoniczności udziału w przedziale ani certyfikatu, że może tam wystąpić najwyżej jedno przekroczenie. Sam bracket z końcem powyżej progu i początkiem poniżej nie wystarcza do identyfikacji pierwszego przekroczenia.

**Wymagana poprawka:** chronologiczne dzielenie musi trwać aż do uzyskania przedziału czasu o wymaganej szerokości. Na każdym kroku lewa połowa musi być certyfikowana jako wolna od przekroczenia, zanim prawa połowa stanie się kandydatem. Jeżeli lewa połowa pozostaje nierozstrzygnięta, algorytm nie może jej odrzucić na podstawie samego znaku w punkcie środkowym; musi kontynuować certyfikację albo zwrócić status nierozstrzygnięty. Zwykła bisekcja może być użyta dopiero po dowiedzeniu, że zachowuje ten lewostronny niezmiennik.

## 4. Dodatkowe erraty wymagane

### E-01 — etykieta STYCZNY nie wynika z podanego kryterium

**Status: 🔍 ERRATA**

Warunek A.4: górne oszacowanie finalnej połówki jest >= theta, a oba końce mają udział < theta. To oznacza wyłącznie, że certyfikat braku przekroczenia nie zadziałał. Nie dowodzi styczności. W środku może występować rzeczywiste przekroczenie z maksimum powyżej theta, rzeczywista styczność albo tylko zbyt luźne oszacowanie Lipschitza.

Ponieważ protokół słusznie zakazuje domysłów o istnieniu przekroczenia, etykieta „STYCZNY” jest sprzeczna z tym zastrzeżeniem. Należy użyć neutralnego statusu, np. `NIEROZSTRZYGNIĘTY-PRZEDZIAŁ`. Status częściowy i blokada późniejszego ogłoszenia pierwszego przekroczenia mogą pozostać.

### E-02 — definicja tau nie zgadza się z konwencją tau=0

**Status: 🔍 ERRATA**

§2.3 definiuje tau jako pierwsze t>0, dla którego udział(t)>=theta. B4 jednocześnie nakazuje tau=0, gdy udział(0)>=theta. Przy ciągłości, jeśli warunek zachodzi w t=0, to zachodzi również dla pewnego przedziału dodatnich czasów; w zbiorze t>0 nie ma wtedy najmniejszego elementu. Wartość 0 jest infimum/czasem trafienia z uwzględnieniem brzegu, a nie „pierwszym dodatnim t”.

**Wymagana poprawka:** zdefiniować jednolicie tau = inf{t>=0 : udział(t)>=theta}. Wtedy reguła tau=0 z B4 jest spójna z definicją.

### E-03 — brak protokołu arytmetyki przedziałowej dla certyfikatów numerycznych

**Status: ❌ BLOCKER dla słowa „CERTYFIKOWANE”**

A.3 i A.4 korzystają z numerycznych wartości F, współczynników c(a,b), L_F, L_t, theta oraz porównań z progiem. Nie określono jednak wymaganej arytmetyki gwarantującej kierunek zaokrągleń. Bez tego:

- M może być numerycznie zawyżone, a wtedy nie musi być dolnym ograniczeniem sup;
- ub(K) lub g_k mogą być numerycznie zaniżone, a wtedy nie muszą być górnymi ograniczeniami;
- porównanie g_k < theta albo udział(t_k) >= theta może zostać odwrócone przez błąd numeryczny.

Sama matematyczna poprawność nierówności Lipschitza nie usuwa błędu ich numerycznej ewaluacji. Przy zwykłych przybliżeniach zmiennoprzecinkowych protokół daje oszacowanie numeryczne, nie formalny certyfikat.

**Wymagana poprawka:** jawnie wymagać arytmetyki przedziałowej lub równoważnej kontroli błędu z zaokrąglaniem na zewnątrz. Trzeba określić, jak z przedziałów ewaluacji F buduje się dolne M, górne ub(K) i g_k, jak ogranicza się błąd L_F/L_t oraz jak rozstrzyga się porównania bliskie theta. Do wyznaczania wag należy wskazać, że używa się formy zamkniętej lub innego źródła z certyfikowanym błędem, a nie niekontrolowanych wartości tabelarycznych zaokrąglonych do czterech miejsc.

### E-04 — budżet 10^7 w (ac) jest pre-rejestrowany, ale jego wystarczalność nie została dowiedziona

**Status: 🔍 ERRATA uzasadnienia; bez obalenia bezpieczeństwa warunku stopu**

Podane liczności 613304–2580960 aktywnych komórek bazowych są informacją o stanie po pierwszym odrzuceniu. Nie ograniczają liczby późniejszych podziałów potomnych potrzebnych do osiągnięcia max ub − M <= 10^-4. Nie podano górnego ograniczenia głębokości ścieżek ani łącznej liczby podziałów wynikającej z geometrii F.

Limit 10^7 jest dopuszczalnym budżetem wykonawczym, jeżeli po jego wyczerpaniu protokół zwraca NIE-CERTYFIKOWANE. Nie jest jednak matematycznym dowodem, że kryterium domknięcia będzie osiągalne przy tym limicie. Uzasadnienie „liczność komórek aktywnych razy kilka poziomów” pozostaje oszacowaniem warsztatowym, nie certyfikatem kosztu.

**Wymagana poprawka:** opisać 10^7 jako pre-rejestrowany limit, którego wystarczalność jest hipotezą wykonawczą, albo dostarczyć a priori górne ograniczenie liczby podziałów. Nie należy twierdzić, że sam rachunek liczby aktywnych komórek dowodzi osiągalności kryterium.

## 5. Elementy potwierdzone

### P-01 — geometria ograniczenia A.3

**Status: ✅ PASS, warunkowo względem poprawnej stałej Lipschitza i arytmetyki**

Dla komórki 4-wymiarowej o jednakowej krawędzi h, odległość dowolnego punktu od najbliższego wierzchołka w metryce L1 wynosi najwyżej 4*(h/2)=2h. Zatem r(K)=h/2*4=2h jest poprawne.

Dla funkcji będącej sumą 15 wyrazów c(a,b) cos(phi_a)cos(phi_b), po podstawieniu phi_5=theta_1+theta_2, ograniczenie L_F=2*sum|c(a,b)| jest bezpiecznym ograniczeniem Lipschitza względem normy L1 czterech niezależnych współrzędnych fazowych. Wymaga to stosowania odległości zawijanej na torusie i liczenia sumy z rzeczywistych współczynników użytych w F.

W konsekwencji: wzór ub(K), odrzucenie komórki gdy ub(K)<M oraz kryterium [M,max ub] są matematycznie poprawne w arytmetyce dokładnej/przedziałowej.

### P-02 — ograniczenie czasowe A.4

**Status: ✅ PASS, warunkowo względem poprawnej arytmetyki**

Dla 15 wyrazów c(a,b) cos(omega_a t)cos(omega_b t), ograniczenie pochodnej przez sumę |c(a,b)|(omega_a+omega_b) jest poprawne. Każdy punkt przedziału czasu leży w odległości nie większej niż połowa szerokości od jednego z końców, zatem g_k = max(wartości na końcach)+L_t*Delta_t/2 jest bezpiecznym górnym oszacowaniem przy dokładnej ewaluacji i poprawnym L_t.

To potwierdza nierówność Lipschitza, ale nie naprawia problemu pierwszego przekroczenia wskazanego w B-02 ani braku arytmetyki certyfikującej z E-03.

### P-03 — branch-and-bound A.3

**Status: ✅ PASS, warunkowo**

M jako maksimum wszystkich dokładnie ocenionych punktów jest dolnym ograniczeniem supremum. Odrzucanie komórki z ub(K)<M jest bezpieczne. Użycie punktów lokalnego uściślenia wyłącznie do podniesienia M, bez traktowania lokalnego kroku jako globalnego promienia pokrycia, jest poprawne.

## 6. Status Aneksu A i bindu

Aneks A pobrany z `main` ma ten sam Git blob `e68906bed162eb6f0aecec416c6bba9e1b655482`, co w poprzednim audycie. Nie stwierdzono zmiany tabel wag ani formy zamkniętej; nie powtarzałem ich pełnego przeliczenia.

Git blob specyfikacji v1.2 to `42b819aa4b56599567f3fa288aa66babef14cf28`. Jest to identyfikator obiektu Git, nie SHA-256 treści pliku. Nie potwierdzam deklarowanego hasha SHA-256 v1.2.

**K6: ZAMKNIĘTE DO CZASU PUBLIKACJI PEŁNEGO HASHU BINDU.** Po publikacji pełnego hasha specyfikacji v1.2 i identyfikacji niezmienionego Aneksu A można rozważyć rebind. Sam rebind nie rozwiązuje blockerów B-01, B-02 i E-03.

## 7. Konkluzja i kolejność napraw

1. Poprawić (ad): przedział U_b wyznaczać z osobnych granic tau obu kanałów, z poprawną obsługą mianownika obejmującego zero; kill rozstrzygać przedziałowo względem wszystkich orbit.
2. Poprawić A.4: certyfikować lewą część przedziału na każdym kroku aż do tau; nie używać zwykłej bisekcji znakowej jako dowodu pierwszego przekroczenia bez dowodu jednoznaczności.
3. Wprowadzić jawne arytmetyczne reguły certyfikacji przedziałowej dla A.3 i A.4.
4. Zastąpić etykietę STYCZNY statusem nierozstrzygnięcia, doprecyzować definicję tau oraz osłabić lub udowodnić uzasadnienie budżetu 10^7.
5. Opublikować pełny hash bindu zgodnie z §2.5. Do tego czasu nie wykonywać rachunku transportowego.

**Ocena końcowa:** v1.2 poprawnie zachowuje bezpieczny fallback NIE-CERTYFIKOWANE dla A.3, lecz nie usuwa wszystkich luk protokołu. Errata (ad) wymaga kolejnej poprawki; A.4 wymaga domknięcia chronologii aż do dokładności końcowego czasu.
