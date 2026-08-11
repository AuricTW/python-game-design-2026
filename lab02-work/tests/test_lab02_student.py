"""Write at least two focused tests before submitting Lab 02."""

import unittest
from star_sprout_lab import GameConfig, InputState, initial_state, step


class StudentLab02Tests(unittest.TestCase):
    """
    def test_replace_with_a_specific_movement_or_boundary_case(self) -> None:
        before = initial_state(seed=42)
        after = step(before, InputState(right=True), 0.01)
        self.assertGreater(after.player.x, before.player.x)

    def test_replace_with_a_specific_repeatability_or_purity_case(self) -> None:
        self.skipTest("Replace this skip with your own focused assertion")
    """
    # 測試水平相反方向的按鍵是否互相抵消，並且垂直方向的按鍵是否仍然有效
    def test_horizontal_opposites_cancel_while_vertical_moves(self) -> None:
        before = initial_state(seed=42)
        after = step(
            before,
            InputState(left=True, right=True, up=True),
            0.01,
        )

        self.assertEqual(after.player.x, before.player.x)
        self.assertLess(after.player.y, before.player.y)

    # 測試精確模式下的移動是否使用了最大時間步長限制
    def test_precision_uses_bounded_dt(self) -> None:
        config = GameConfig(player_speed=120.0, max_dt=0.05)
        before = initial_state(seed=43, config=config)

        after = step(
            before,
            InputState(right=True, precision=True),
            0.20,
        )

        self.assertAlmostEqual(after.player.x - before.player.x, 3.0)
        self.assertAlmostEqual(after.elapsed, 0.05)

if __name__ == "__main__":
    unittest.main()
