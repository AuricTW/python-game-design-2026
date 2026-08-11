# Lab 03 - Shooter Domain Objects

> Course block: D1-B3, 16:00-19:00  
> Implementation timebox: 135 minutes  
> AI level: **L0** for the first 90 minutes; **L1 conceptual hints** after the TA checkpoint  
> Student overlay: `lab03_student_starter.zip`, applied to the student's own completed Lab 02 repository

## Task

Extend the player state into a pure-Python shooter model with `Player`, `Bullet`, and `Enemy` lifecycles. Your evidence must show when each object is created, updated, removed, and reset. Do not place renderer, image, or Pygame objects inside domain entities.

## Learning outcomes

- Use dataclasses, composition, and explicit responsibilities to manage game objects.
- Use unique IDs, safe collection updates, and cooldowns.
- Make enemy generation reproducible with a seed.
- Explain the invariants behind "remove once, score once, and reset completely."

## Public interface

```python
from star_sprout_lab import (
    Bullet,
    Enemy,
    GameEvent,
    InputState,
    Player,
    World,
)
```

Preserve the starter dataclass fields and `World.create/step/reset/snapshot`. You may add private methods, but these classes must not contain Pygame types.

## Required deliverables

```text
evidence/lab03_responsibility_map.md
evidence/lab03_lifecycle_trace.md
tests/test_lab03_student.py
AI_USE.md                         # Required: mark No AI used or document L1
src/star_sprout_lab/model.py
```

## Procedure

### 1. Responsibility map (15 minutes, L0)

For `World`, `Player`, `Bullet`, and `Enemy`, document authoritative data, permitted responsibilities, and prohibited dependencies. Include at least three cross-object invariants in `lab03_responsibility_map.md`.

### 2. Shooting and cooldown (30 minutes, L0)

- The first valid `fire=True` creates one bullet and one `shoot` event.
- Bullet IDs begin at 1, increase strictly, and are never reused.
- A new bullet begins above the player, travels upward, and takes its speed from the config.
- Each step reduces cooldown by bounded `dt` before deciding whether firing is allowed.
- Do not create a bullet while cooldown is active or `max_bullets` has been reached.
- Remove a bullet exactly once after its entire circle leaves the top of the playfield.

### 3. Enemy creation and cleanup (35 minutes, L0)

- Reduce `spawn_timer` by bounded `dt`; spawn only when the timer expires and the cap has not been reached.
- Add the interval back after each spawn so spawn count is not frame-rate dependent.
- Enemy IDs begin at 1 and increase strictly.
- Enemy type, position, and velocity may vary, but every random decision must use `World._rng`.
- Identical seeds and input sequences must produce identical enemy sequences.
- Remove an enemy after its entire circle leaves the bottom. Reduce player life exactly once, never below zero.
- Do not implement bullet/enemy or enemy/player geometry in this Lab; that belongs to Lab 04.

### 4. Reset and lifecycle trace (25 minutes)

A restart command in `WON` or `GAME_OVER` must restore a clean initial state. Reset entities, score, tick, elapsed time, timers, events, lives, and ID counters while preserving the config.

In `lab03_lifecycle_trace.md`, trace one bullet and one enemy. Record collection sizes, IDs, timers, and events before and after each transition. Identify the invariant that prevents double removal.

### 5. Tests, checkpoint, and commit (30 minutes)

By the end of Day 1, you must have at least four student-written model tests in total, counting Lab 02. At least one must test cooldown or a cap, and another must test restart or seeded spawning.

```bash
python -m unittest discover -s tests_public -v
python -m unittest discover -s tests -v
python -m star_sprout_lab --headless --seed 42 --frames 240 --assert-deterministic
git diff --check
```

Suggested commit: `lab03: add shooter entity lifecycle`

## L1 policy

After the first TA checkpoint, you may ask AI for conceptual hints, counterexamples, problem-isolation advice, or test-name suggestions. You may not request or adopt a submission-ready function, class, test, or patch. Submit `AI_USE.md` in every case: mark `No AI used`, or record the prompt, hint, your evaluation, and the change you completed yourself.

## Acceptance criteria

- The responsibility map demonstrates the domain/presentation boundary.
- Fire, cooldown, cap, bullet update, and cleanup match the contract.
- Enemy creation, update, escape, and cleanup are reproducible and use unique IDs.
- Restart leaves no residual state and creates independent collection objects.
- At least four student-written logic tests in total are green.
- You can explain one entity's complete lifecycle step by step.

Review [rubric.md](rubric.md), [submission_checklist.md](submission_checklist.md), and the [public test contract](public_test_contract.md) before submitting.
