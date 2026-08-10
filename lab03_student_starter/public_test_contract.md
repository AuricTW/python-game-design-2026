# Lab 03 Public Test Contract

Executable tests are added to the starter's `tests_public/` folder. They observe public results and do not require a particular private-method design.

## Import contract

```python
from star_sprout_lab import Bullet, Enemy, GameEvent, InputState, Player, World
```

## Published behaviour families

### Creation and isolation

- `World.create()` starts with empty bullets, enemies, and events. Worlds do not share list objects.
- `Player`, `Bullet`, and `Enemy` preserve the starter's public fields.

### Fire and bullets

- The first valid fire creates exactly one bullet with ID 1.
- The bullet starts at the player's horizontal position, above the player, with `vy == -config.bullet_speed`.
- Held fire respects `fire_cooldown`; another bullet is created only after expiry.
- Entity count never exceeds `max_bullets`.
- A bullet moves by `vy * bounded_dt` and is removed after its entire circle crosses the upper boundary.

### Spawning and enemies

- Spawning occurs only when the timer expires and never exceeds `max_enemies`.
- Enemy IDs begin at 1 and increase strictly without reuse.
- Each active enemy moves by `(vx * bounded_dt, vy * bounded_dt)` before escape cleanup.
- Matching seeds, configs, and steps produce matching `(kind, id, x, y, vx, vy)` sequences.
- Different seeds are not guaranteed to differ, but do not hard-code a single seed-42 sequence.
- An enemy that fully leaves the bottom is removed and costs exactly one life.

### Reset

- Restart resets only from `WON` or `GAME_OVER`.
- After restart, the observable state matches a new world with the same seed/config, with a `restart` event.
- ID counters return to 1, entities and score are cleared, and player life is restored.

The assessment may use a smaller custom `GameConfig` to reach time boundaries quickly. Do not hard-code 960 x 540, 60 seconds, or specific spawn coordinates.

## Public-test layout

```text
tests_public/
`-- test_public_lab03.py      # Distributed by the course; do not modify
```

This contract is packaged at the overlay root as `public_test_contract.md`. The executable test is included in the Lab 03 overlay and must not be modified. Add focused tests in `tests/test_lab03_student.py`; do not use an always-passing placeholder.
