"""Representative public checks for the published Lab 03 contract."""

import unittest

from star_sprout_lab import Bullet, GameConfig, InputState, Phase, World


class PublicLab03Tests(unittest.TestCase):
    def test_first_valid_fire_creates_one_bullet_and_event(self) -> None:
        world = World.create(seed=21)
        world.step(InputState(fire=True), 0.01)
        self.assertEqual([bullet.bullet_id for bullet in world.bullets], [1])
        bullet = world.bullets[0]
        self.assertAlmostEqual(bullet.x, world.player.x)
        self.assertLess(bullet.y, world.player.y)
        self.assertAlmostEqual(bullet.vy, -world.config.bullet_speed)
        self.assertEqual([event.kind for event in world.events], ["shoot"])

    def test_cooldown_and_bullet_cap_are_respected(self) -> None:
        config = GameConfig(fire_cooldown=0.05, max_bullets=2)
        world = World.create(seed=22, config=config)
        world.step(InputState(fire=True), 0.01)
        world.step(InputState(fire=True), 0.01)
        self.assertEqual(len(world.bullets), 1)
        world.step(InputState(fire=True), 0.04)
        self.assertEqual([bullet.bullet_id for bullet in world.bullets], [1, 2])
        world.step(InputState(fire=True), 0.05)
        self.assertEqual([bullet.bullet_id for bullet in world.bullets], [1, 2])

    def test_bullet_moves_and_cleans_up_above_playfield(self) -> None:
        world = World.create(seed=23)
        world.bullets.append(Bullet(99, x=100.0, y=world.config.hud_height + 4.0, vy=-100.0, radius=5.0))
        world.step(InputState(), 0.05)
        self.assertEqual([bullet.bullet_id for bullet in world.bullets], [99])
        world.step(InputState(), 0.05)
        self.assertEqual(world.bullets, [])

    def test_seeded_enemy_sequence_repeats(self) -> None:
        config = GameConfig(spawn_interval=0.01, max_enemies=4)
        first = World.create(seed=24, config=config)
        second = World.create(seed=24, config=config)
        for _ in range(4):
            first.step(InputState(), 0.02)
            second.step(InputState(), 0.02)
        observe = lambda world: [(e.kind, e.enemy_id, e.x, e.y, e.vx, e.vy) for e in world.enemies]
        self.assertEqual(len(first.enemies), 4)
        self.assertEqual(len(second.enemies), 4)
        self.assertEqual([enemy.enemy_id for enemy in first.enemies], [1, 2, 3, 4])
        self.assertEqual(observe(first), observe(second))

    def test_escaped_enemy_costs_one_life_once(self) -> None:
        world = World.create(seed=25)
        from star_sprout_lab import Enemy
        world.enemies.extend(
            [
                Enemy(5, "scout", 50.0, world.config.height + 10.0, 0.0, 100.0, 5.0, 1, 10),
                Enemy(6, "scout", 50.0, 100.0, 10.0, 20.0, 5.0, 1, 10),
                Enemy(7, "scout", 70.0, world.config.height + 4.0, 0.0, 0.0, 5.0, 1, 10),
            ]
        )
        world.step(InputState(), 0.01)
        self.assertEqual(world.player.lives, 2)
        self.assertEqual([enemy.enemy_id for enemy in world.enemies], [6, 7])
        self.assertAlmostEqual(world.enemies[0].x, 50.1)
        self.assertAlmostEqual(world.enemies[0].y, 100.2)
        world.step(InputState(), 0.01)
        self.assertEqual(world.player.lives, 2)

    def test_restart_matches_new_world_and_reports_event(self) -> None:
        world = World.create(seed=26)
        world.score = 99
        world.bullets.append(Bullet(1, 100.0, 100.0, -1.0))
        world.next_bullet_id = 2
        world.step(InputState(restart=True), 0.01)
        self.assertIs(world.phase, Phase.PLAYING)
        self.assertEqual(world.score, 99)
        self.assertEqual([bullet.bullet_id for bullet in world.bullets], [1])
        self.assertEqual(world.next_bullet_id, 2)
        world.phase = Phase.GAME_OVER
        world.step(InputState(restart=True))
        expected = World.create(seed=26, config=world.config)
        self.assertEqual(world.snapshot(), expected.snapshot())
        self.assertEqual([event.kind for event in world.events], ["restart"])
        self.assertEqual(world.next_bullet_id, 1)


if __name__ == "__main__":
    unittest.main()
