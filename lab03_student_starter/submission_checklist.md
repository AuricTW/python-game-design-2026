# Lab 03 Submission Checklist

- [ ] `lab03_responsibility_map.md` covers all four types and at least three invariants.
- [ ] `lab03_lifecycle_trace.md` tracks a bullet, enemy, collections, IDs, timer, and events.
- [ ] `Player`, `Bullet`, and `Enemy` contain no Pygame or renderer state.
- [ ] Fire cooldown and `max_bullets` are correct at their boundaries.
- [ ] Bullet and enemy IDs are unique and strictly increasing.
- [ ] Every random decision uses the seeded `World._rng`.
- [ ] Off-screen entities are processed once, and life never becomes negative.
- [ ] Restart clears entities, score, time, timers, events, and counters.
- [ ] I have at least four student-written model tests in total from Labs 02-03.
- [ ] Public tests, student tests, and deterministic smoke checks all pass.
- [ ] I submitted `AI_USE.md` with either `No AI used` or a complete L1 record.
- [ ] I can explain an entity lifecycle without AI or a game window.

Final commit:  
Known limitations:
