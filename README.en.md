# P₀ — Punkt Zerowy (Point Zero)

> "The path matters, not the goal. It bears the richest fruit." — Z0

**P₀** is a mathematics workshop: a long-term research project on the dynamics of consensus on a family of solids — from the tetrahedron (K₄), through pairs of tetrahedra (joined along a face and interpenetrating: the stella octangula) and mK₄ bipyramids (from 5K₄), to the icosahedron — conducted through independent replications of computations across AI models, with no code shared between executors.

![Tree convention](docs/img/drzewo.svg)

## Ground rules (short)

- **Z0 — the path over the goal.** A negative result (a refuted hypothesis) is fully valuable. Mistakes are documented as permanent "knots" — never deleted.
- **Z1 — independent implementation.** No number gets ✅ from a single computation. Status ✅ requires at least two consistent, independent implementations of a shared specification.
- **Z2 — explicit conventions.** Every table states units, class ordering, orientation, normalization, seed/generator.
- **Z3 — specifications, not code.** Executors exchange specifications and results — never code. No working workshop code lives in this repository; the only code listings appear as quotations inside the verbatim root documents.

## Layout

- **docs/INDEKS.md** — a map of the repository plus a per-line list of completed work, updated after every round (guards against duplicating work; Polish)
- **ZAPROSZENIE.md** — how to join: guest, replicator, director of a parallel laboratory (Polish; English summary inside)
- **docs/metodyka.md** — workshop rules (Polish)
- **docs/wyniki.md** — results & errata register: a dump of the workshop log, frozen at era 11cs (2026-11-19); the current map of work: docs/INDEKS.md (Polish)
- **docs/replikacja.md** — how to perform and report an independent replication
- **docs/zlecenia.md** — open problems & directions (state: era 11cs, queues partly settled; current state: docs/INDEKS.md): replication queue, publication candidates, knot-offshoots, the P₀-AI branch (Polish)
- **docs/warsztat/** — workshop materials: the original TAU-8 session (the 12-neighbour network) and the H-DEF diary: what the work looks like from the inside
- **docs/replikacja/** — replication packages ready to pick up (Z1): specifications, partial results, sample reports
- **docs/seminarium/** — seminar materials, internal and open
- **docs/mvp-01-spec…, docs/mvp-02-spec…** — MVP specifications (Z3: specification, not code) · **docs/p0-ai-komorka-spec-v0_1-DRAFT.md** — P₀-AI cell draft · **docs/wklejka-…** — executor reports (Claude, GPT/Asterion, DeepSeek) accepted into the workshop register
- **docs/korzenie/** — the roots of the tree: laboratory-head annotations plus full workshop documents (verbatim); originals with a life of their own in print (the SERC tetralogy, the original OS AI Dominik PDF) are not kept here — they stay in the author's archive
- **GLOSSARY.md** — glossary of workshop terms (PL → EN)
- **README.es.md** — resumen en español

## Statuses

✅ confirmed by independent replication · 🔍 awaiting replication · ❌ refuted · 💡 hypothesis

## Invitation

All specifications are public and self-contained. Three levels of entry:

1. **Guest** — read; everything is public.
2. **Replicator** — pick a result marked 🔍, compute it your way (**docs/replikacja.md**), open an issue with full attribution of every number. Agreement of two independent computations is the norm in P₀, not a badge of honor.
3. **Lab director** — found a parallel P₀ laboratory: your own register, your own executors, the inter-node protocol. We are not recruiting members — we are inviting laboratories: **ZAPROSZENIE.md** (Polish, with an English summary).

Questions, seminars, and open discussion: the **Discussions** tab. Errata and replications go through templated **Issues** (.github/ISSUE_TEMPLATE).

## License

Contents: [CC BY 4.0](LICENSE). © Leszek Papiernik (Point Zero).

Project site: **[serc.pl](https://serc.pl)** — note: the working language of the workshop is Polish.

