"""Add focused lifecycle tests; keep at least four Day 1 model tests total."""

import unittest

from star_sprout_lab import GameConfig, InputState, Phase, World


class StudentLab03Tests(unittest.TestCase):
    # Lab3 測試冷卻時間內無法發射子彈
    def test_replace_with_a_cooldown_or_cap_boundary(self) -> None:
        world = World.create(seed=42)
        world.step(InputState(fire=True), 0.01)
        self.assertEqual(len(world.bullets), 1)

    # Lab3 測試重置遊戲狀態後，玩家生命值是否正確保留
    def test_replace_with_seeded_spawn_or_restart_evidence(self) -> None: 
        self.skipTest("Replace this skip with your own focused assertion")

    # Lab3 測試冷卻時間內無法發射子彈，並且在冷卻時間結束後可以再次發射
    def test_max_bullets_blocks_fire_after_cooldown_expires(self) -> None: 
        config = GameConfig(
            fire_cooldown=0.01,
            max_bullets=1,
        )
        
        world = World.create(seed=42, config=config) # 創建一個新的遊戲世界，使用指定的隨機種子和配置
        
        world.step(InputState(fire=True), 0.01) # 第一次射擊
        world.step(InputState(fire=True), 0.01) # 第二次射擊，冷卻結束但子彈數量已達上限，應該無法射擊

        self.assertEqual(
            [bullet.bullet_id for bullet in world.bullets],
            [1],
        )

        # 確認 ID 計數器沒有因失敗射擊而增加
        self.assertEqual(world.next_bullet_id, 2)


    # Lab3 測試重置遊戲狀態後，玩家生命值是否正確保留
    def test_restart_matches_fresh_world_with_independent_lists(self) -> None: 
        world = World.create(seed=42)

        # 故意製造非初始狀態
        world.step(InputState(fire=True), 0.01) # 第一次射擊
        world.score = 99 # 故意修改分數
        world.player.lives = 1 # 故意修改玩家生命值

        # Resart 只在 WON or GAME_OVER 時呼叫
        world.phase = Phase.GAME_OVER
        world.step(InputState(restart=True))

        fresh = World.create(seed=42, config=world.config) # 創建一個新的遊戲世界，使用相同的隨機種子和配置

        self.assertEqual(world.snapshot(), fresh.snapshot()) # 比較重置後的世界狀態與新創建的世界狀態是否相同

        # 本幀應通知外部發生 restart
        self.assertEqual(
            [event.kind for event in world.events],
            ["restart"],
        )
        # 兩個 World 不應共用同一個清單
        self.assertIsNot(world.bullets, fresh.bullets)
        self.assertIsNot(world.enemies, fresh.enemies)





        

    
        





if __name__ == "__main__":
    unittest.main()
