"""Write at least two focused tests before submitting Lab 02."""

import unittest

from star_sprout_lab import InputState, initial_state, step


class StudentLab02Tests(unittest.TestCase):
    def test_replace_with_a_specific_movement_or_boundary_case(self) -> None:
        before = initial_state(seed=42)
        after = step(before, InputState(right=True), 0.01)
        self.assertGreater(after.player.x, before.player.x)

    def test_replace_with_a_specific_repeatability_or_purity_case(self) -> None:
        self.skipTest("Replace this skip with your own focused assertion")


if __name__ == "__main__":
    unittest.main()
