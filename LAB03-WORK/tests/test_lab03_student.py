"""Add focused lifecycle tests; keep at least four Day 1 model tests total."""

import unittest

from star_sprout_lab import InputState, World


class StudentLab03Tests(unittest.TestCase):
    def test_replace_with_a_cooldown_or_cap_boundary(self) -> None:
        world = World.create(seed=42)
        world.step(InputState(fire=True), 0.01)
        self.assertEqual(len(world.bullets), 1)

    def test_replace_with_seeded_spawn_or_restart_evidence(self) -> None:
        self.skipTest("Replace this skip with your own focused assertion")


if __name__ == "__main__":
    unittest.main()
