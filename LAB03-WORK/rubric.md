# Lab 03 Rubric - 100 points

| Dimension | Points | Full evidence |
|---|---:|---|
| Responsibilities and boundaries | 15 | Four clear responsibility descriptions, at least three invariants, and no presentation dependency in the domain |
| Bullet lifecycle | 20 | Fire, ID, cooldown, cap, movement, cleanup, and events are correct |
| Enemy lifecycle | 20 | Timer, seeded spawn, ID, movement, escape, and cleanup are correct |
| Reset and state isolation | 20 | Every gameplay field resets; config is preserved; collections are not shared |
| Tests and lifecycle evidence | 15 | At least four model tests in total; trace demonstrates exactly-once behaviour |
| Git, explanation, and AI compliance | 10 | Focused diff, clear commit, accurate explain-back, and an L1 record or explicit no-use statement |

## Scoring constraints

- If the domain imports Pygame or stores a Surface or OS event, the total is capped at 60.
- If an entity can be charged, removed, or assigned the same ID more than once, the corresponding lifecycle dimension is capped at half credit.
- Without student-written tests, Tests and lifecycle evidence earns 0.
- Undeclared L1 use is handled under the Syllabus, not as an ordinary point deduction.

