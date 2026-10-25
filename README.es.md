# P₀ — Punto Cero

> «El camino importa, no la meta. Es el que da los frutos más ricos.» — Z0

**P₀** es un taller de matemáticas: un proyecto de investigación a largo plazo sobre la dinámica del consenso en los sólidos platónicos — el tetraedro (K₄), un par de tetraedros y el icosaedro — llevado a cabo mediante replicaciones independientes de cálculos realizadas por modelos de IA, sin intercambio de código entre ejecutores.

![Convención del árbol](docs/img/drzewo.svg)

## Reglas del taller (resumen)

- **Z0 — el camino sobre la meta.** Un resultado negativo (una hipótesis refutada) tiene pleno valor. Los errores se documentan como «nudos» (sęki) permanentes — nunca se eliminan.
- **Z1 — implementación independiente.** Ningún número recibe ✅ de un solo cálculo. El estado ✅ requiere al menos dos implementaciones independientes y concordantes de una especificación común.
- **Z2 — convención explícita.** Cada tabla indica unidades, orden de clases, orientación, normalización, semilla/generador.
- **Z3 — especificaciones, no código.** Entre ejecutores se intercambian especificaciones y resultados — nunca código. En este repositorio no hay código.

## Estructura

- **ZAPROSZENIE.md** — cómo unirse: invitado, replicador, director de un laboratorio paralelo (polaco; resumen en inglés dentro)
- **docs/metodyka.md** — reglas del taller, protocolo del equipo de modelos, estados, formato de erratas, convención del árbol (polaco)
- **docs/wyniki.md** — registro de resultados y erratas (instantánea pública del diario del taller, hasta la ronda 38; polaco)
- **docs/replikacja.md** — cómo realizar y reportar una replicación independiente (polaco)
- **docs/zlecenia.md** — encargos y direcciones abiertos: cola de replicación, candidatos a publicación, esquejes de nudos, rama P₀-AI (polaco)
- **docs/korzenie/** — raíces históricas anotadas (el repo guarda anotaciones, no archivos fuente)
- **GLOSSARY.md** — glosario de términos del taller (PL → EN)
- **README.en.md** — resumen en inglés

## Estados

✅ confirmado por replicación independiente · 🔍 espera replicación · ❌ refutado · 💡 hipótesis

## Invitación

Todas las especificaciones son públicas y autosuficientes. Tres niveles de entrada:

1. **Invitado** — lee; todo es público.
2. **Replicador** — elige un resultado marcado 🔍, calcúlalo a tu manera (**docs/replikacja.md**), abre un issue con la atribución completa de cada número. La concordancia de dos cálculos independientes es la norma en P₀, no una medalla de honor.
3. **Director de laboratorio paralelo** — funda tu propio nodo del taller: tu propio diario, tus propios ejecutores, el protocolo entre nodos. No reclutamos miembros — invitamos laboratorios: **[ZAPROSZENIE.md](ZAPROSZENIE.md)**.

## Licencia

Contenidos: [CC BY 4.0](LICENSE). © Leszek Papiernik (Punto Cero).

Sitio del proyecto: **[serc.pl](https://serc.pl)** — nota: la lengua de trabajo del taller es el polaco.
