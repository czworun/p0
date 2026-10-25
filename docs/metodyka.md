# P₀ — metodyka warsztatu

## Zasada nadrzędna (Z0) — Leszek, tura 6 (2026-10-10)

„Droga jest ważna, nie cel. To ona owocuje najbogaciej."

W projekcie P₀ wartością jest **proces**: niezależne replikacje, erraty, koncesje formułowane wprost przy własnych błędach, jawne konwencje. Statusy (kanoniczność obiektów, wyniki testów) są produktami ubocznymi. Wynik negatywny (np. obalenie hipotezy) jest pełnowartościowym owocem drogi. Bramki decyzyjne i warunki degradacji służą uczciwości rejestru, nie presji na wynik — żaden krok warsztatu nie jest tylko środkiem do celu.

## Zasady warsztatu

- **Z1 — niezależna implementacja:** żadne twierdzenie numeryczne nie dostaje ✅ z jednej implementacji; między modelami liczy się zgodność rachunków wspólnej specyfikacji (dla twierdzeń algebraicznych wynik nie zależy od konwencji).
- **Z2 — jawna konwencja:** każda tabela podaje jednostki, porządek klas, orientację, normalizację (poz. 13 katalogu błędów TAU; lekcja §6.1 TETRA-20).
- **Z3 — specyfikacje, nie kod:** między modelami przekazuje się specyfikacje i wyniki, nigdy kod.

## Tryb zespołu modeli

Leszek jest węzłem przekazującym wiadomości między modelami (Vibe, Claude, GPT/„Asterion", DeepSeek). Wiadomości adresowane blokami „Do Claude'a" / „Do GPT" / „Do DeepSeeka", zwięźle, po polsku. Odpowiedzi modeli wracają przez Leszka.

**Protokół przekazu między-modelowego (zasady z sęków tur 23–26):**
1. **Liczby jawnym tekstem** — inline math/LaTeX gubione w przekazie (3 wystąpienia, tury 23–24); domknięte praktyką retransmisji w czystym tekście.
2. **Przed zleceniem sync sprawdź obecność dokumentu źródłowego w paczce** (sęk tury 25: FOUNDATION zabrakło w paczce SYNC-1).
3. **Atrybucja każdej wartości jawna** (plik/tura/kto); wartość bez źródła w zleceniu → STOP i pytanie, nie zgadywanie (sęki: 10.7 wycofane; tetry 369/256).
4. **Atrybucja konstrukcji Ψ jawna** (seed + skala) — wyniki Ψ-dependent bez atrybucji nieporównywalne (tura 26: K1 u GPT — punkt stały 2.858 w dostawie cząstkowej vs zanik w finalnej, bez rozróżnienia konstrukcji).
5. **Równe normy ≠ ten sam stan** — norma nie identyfikuje stanu; raport reżimu wymaga residuum ‖ẋ‖ i tożsamości punktu końcowego (tura 26: 20 torów T1a → 20 różnych punktów jednej orbity A₅, błąd 9.45e−15).
6. **Frakcje ucieczek raportować jako krzywe z próbą i generatorem** (tura 26: 54% → 66.7% przy ε = 1.2 między próbami GPT; punkt 50% wędruje 1.075 → 1.13 zależnie od generatora).
7. **Metadata-hygiene przy bumpie SSOT** — przy każdej zmianie wersji dokumentu źródłowego (pień, SSOT) sprawdź pola zależne w dokumentach zsynchronizowanych: synchronized_with, companions, cytaty wersji (wartość metadanych, nie tylko treść). Sęk-lekcja z FOUNDATION v2.0: pole synchronized_with „P0-Pień v0.1" przetrwało ≥4 tury po faktycznym bumpie pnia do v0.3.x; poprawka uogólniona z reguły §5 tree_convention FOUNDATION v2.1 (tura 27). Rozszerzenie (tura 28, DeepSeek): raport replikacji podaje atrybucję **każdej** liczby do konkretnej konstrukcji — etykieta Ψ-standardu, wersja specyfikacji, numer seeda; replikacja bez tej atrybucji jest nieodtwarzalna mimo poprawnej metodologii (ta sama klasa błędu co LCG bez parametrów, v0.1.4 §13 pkt 1; przypadek K1 u GPT: 2.858 vs zanik bez rozróżnienia konstrukcji). Rozszerzenie (tura 32, DeepSeek, finalny pass decku): **errata do elementu, który recenzent wcześniej ocenił pozytywnie, cytuje jawnie jego poprzednią ocenę** — recenzent inaczej utrwala błąd przez nieuwidocznioną zmianę podstawy (przypadek: mechanizm artefaktu dt „|λ|·dt ≈ 2.21 przy krawędzi 2.78" oceniony jako uczciwy w turze 28; errata tury 31 — mechanizm: mody sztywne λ < −557; sęk #1 DeepSeeka: przy weryfikacji mechanizmu sprawdzać nie tylko zgodność liczby z rejestrem, lecz czy liczba jest mechanizmem, co dominuje (max |R| po widmie, nie dominanta) i czy sformułowanie nie wprowadza mylnego wrażenia).

## Szef laboratorium P₀ (tura 15, 2026-10-14 — decyzja Leszka)

**Leszek deleguje na Vibe kierownictwo laboratorium P₀**: Vibe („szef laboratorium") decyduje o kierunku projektu, wyborze ścieżek i rozstrzygnięciach otwartych kwestii (dotychczas „decyzja: Leszek"); Leszek pozostaje twórcą-kuratorem i może inspirować, ale decyzje należą do szefa laboratorium. Rejestr decyzji nadal jawny; decyzje szefa laboratorium wpisane jako „decyzja szefa lab. (Vibe), delegacja Leszka".

**Protokół sesji TAU (ustalony tury 15):** hasło Leszka „co w projekcie p0?" ⇒ Vibe samodzielnie przeprowadza pełny cykl w jednym złożeniu: plan → projekt → wykonanie rachunków/testów → analiza → **wpis do dziennika laboratoryjnego**. Vibe sam dobiera budżet sesji (liczbę wątków/tokenów) do pomysłu. Protokół Z1–Z3 i bramki sanity obowiązują bez zmian; statusy podnoszone tylko wg Z1 (✅ wymaga ≥2 zgodnych rachunków — sesja TAU daje 🔍/kandydatów).

**Cel długoterminowy (Leszek):** po zakończeniu warsztatu oddać dziełu wolność — projekt ma się rozwijać samodzielnie i tworzyć własne dzieła (gałąź implementacji aplikacyjnych; P₀-AI oczekuje na materiały).

**Strona projektu: https://serc.pl** („Punkt Zerowy — Metryka SERC": S–E–R–C, manifest, zasady). Repozytorium GitHub — Leszek przekaże (org „serc-pl" niedostępny publicznie).

## Statusy i format errat

- ✅ potwierdzone niezależną replikacją (≥2 zgodne rachunki) · 🔍 oczekuje na replikację · ❌ obalone · 💡 hipoteza.
- Errata: dokument → § → jest → powinno być → uzasadnienie → status weryfikacji.
- Przy własnych błędach — koncesja wprost (wzorzec: errata T_d → T_h; etykieta T₂ → T₁).

## Konwencja drzewa (tura 12, 2026-10-11 — decyzja Leszka, przyjęta w 100%)

Układ korpusu: **korzenie (filary — intuicje, jak zachowa się relacja) → pień (rdzeń algebraiczny, zakotwiczony w P₀) → gałęzie (operacjonalizacje)**. Soki w górę: hipotezy i pytania; soki w dół: wyniki i erraty. Słoje pnia = warstwy (topologia → algebra relacji → dynamika P₀ → dynamika nieliniowa); **każdy słój drewna = jedna niezależna replikacja (Z1: ✅ wymaga ≥2 słojów)**. Sęki = wyniki wycofane/obalone, trwałe (Z0): indeksowane w pieńwiu, dokumentowane w filarach, nigdy nie usuwane. **Pień rośnie w warsztacie (Vibe); FOUNDATION DeepSeeka synchronizowana protokołem wpisów.** Odwołania do filarów wyłącznie wg nazwy, nie wersji pliku — pliki filarów nie tracą historii. Pień nie generuje hipotez (to korzenie) i nie uruchamia rachunków (to gałęzie). **Kod nie rośnie na drzewie (tura 13 — decyzja Leszka):** w pieńwiu nie ma kodu — powtarzalność przez specyfikacje (Z3) i tablice kontrolne słoja (bramki sanity); implementacje trafią do szopy (osobne archiwum z metadanymi) — **szopa odroczona, do postawienia, gdy przyjdzie czas**; kod = dokumentacja drogi (Z0), nigdy podstawa statusów; między modelami przekazuje się specyfikacje, nie kod.

## Dokumenty robocze

- **Raport replikacji tur 3–5** (dokument warsztatowy „raport-p0-replikacja") — erraty §6.1, zweryfikowane wyniki TAU/SERC/TETRA-20; od tury 12: rola miazgi (laboratorium dowodu i metody — tam powstają nowe słoje).
- **P₀-Lattice v0.1** (dokument warsztatowy „p0-lattice-v0-1") — sieć relacyjna ikosaedrów z bramkami; rejestry wyników (§6) i atrybucji (§7); decyzje tury 6 w §5; gałąź makrosieci w drzewie.
- **Pień — rdzeń algebraiczny** (dokument warsztatowy „p0-pien", v0.1) — słoje 1–4, krata układów (K₄→para→ikosaedr→makrosieć), atlas liczb z konwencjami, mapa wpięć korzeni (szyjki), rejestr gałęzi, indeks sęków, zasady przyrostu (protokół pnia).
- Korpus autora: P₀-TAU, P₀-SERC, P₀-TETRA-20, P₀-Defect, P0-renowacja relacji i inne pliki w katalogu przesłanym do konwersacji.

