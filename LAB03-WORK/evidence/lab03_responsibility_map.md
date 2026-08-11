# Lab 03 Responsibility Map

Complete this before implementing object lifecycle rules.

| Type | Authoritative data | Permitted responsibilities | Prohibited dependencies |
|---|---|---|---|
| `World` | 全域設定、遊戲進度、Player、物件集合(bullets、enemies)、更新事件、敵人生成計時、唯一 ID 計數器、可重現的亂數產生器| 協調更新、判斷邊界、建立及移除實體 | Pygame、renderer、Surface、圖片、螢幕或作業系統事件 |
| `Player` | 位置、速度、碰撞半徑、生命值，以及冷卻／無敵計時 | 處理自身狀態 | 子彈／敵人清單、生成計時器、ID 計數器，以及任何繪圖物件 |
| `Bullet` | ID、位置、垂直速度與碰撞半徑 | 根據速度與時間更新自身位置 | World.bullets 清單、玩家生命、敵人生成，以及任何 renderer 或 Pygame 物件 |
| `Enemy` | ID、種類、位置、速度、碰撞半徑、血量與分數價值 | 只負責自己的位置與移動 | World.enemies 清單、Player.lives、其他敵人，以及任何 renderer 或 Pygame 物件 |

## Cross-object invariants

1. ID 唯一且依序增加
2. 每個物件只能移除／扣命一次
3. domain model 不依賴 renderer 或 Pygame

Explain why the renderer must not decide whether an object is removed:

renderer 不負責偵測或判定
它的用途是讀取 World 中目前存在的物件並根據物件座標把它們畫到畫面上。

如果由 renderer 決定移除物件，可能產生
沒有開啟畫面的 headless 測試可能不會移除物件。
遊戲規則會依賴 Pygame 或顯示設備。
繪製頻率不同可能導致不同結果。
World 不再是唯一可信的遊戲狀態來源。
等問題