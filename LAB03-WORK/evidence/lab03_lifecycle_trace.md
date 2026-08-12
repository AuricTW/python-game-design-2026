# Lab 03 Lifecycle Trace

>Lab3 step 6

Trace one Bullet and one Enemy from creation through removal.

| Step | Input / dt | Bullet IDs | Enemy IDs | Cooldown | Spawn timer | Events | Life | Explanation |
|---:|---|---|---|---:|---:|---|---:|---|
| 0 |  initial / 0.0 | `[]`|`[]`| 0.0 | 0.8| `[]`| 3 | 建立新世界，無子彈和敵人 |
| 1 | manual setup / 0.0 | `[99]` | `[5]` | 0.0 | 0.8 | `[]` | 3 | 手動放入測試物件(敵人和子彈)，尚未推進時間|
| 2 |  none / 0.05  | `[99]` | `[5]` | 0.0 | 0.75 | `[]` | 3 | 子彈與敵人皆移動，但兩者仍有部分位於遊戲區內，因此保留 |
| 3 |  none / 0.05 | `[]` | `[5]` | 0.0 | 0.7 | `[]` | 3 | 子彈`[99]`穿越頂部並移除一次 |
| 4 | none / 0.05 | `[]` | `[]` | 0.0 | 0.65 | `[]` | 2 | 敵人 `[5]` 完整越過底部，被移除並扣除一條生命。 |
| 5 | none / 0.05 | `[]` | `[]` | 0.0 | 0.60 | `[]` | 2 | 敵人已不在清單中，因此下一幀不會再次扣命。 |
| 6 | restart=True / dt=None | `[]` | `[]` | 0.0 | 0.80 | `["restart"]` | 3 | 在 GAME_OVER 狀態送入 restart 後，世界恢復初始狀態：清空子彈與敵人、恢復生命及計時器，並記錄 restart 事件。 |

#### Invariant that prevents double removal or double life loss:  
每一幀都會建立新的保留清單。敵人或子彈一旦完全越界，就不會被加入下一幀使用的清單。因為下一幀已找不到該物件，所以它不會再次被移除，逃脫敵人也不會再次扣除生命。


#### Restart observation and comparison with a new World:  
將 phase 設為 GAME_OVER 後送入 restart，
子彈與敵人清空、生命恢復為 3、spawn timer 恢復為 0.8，並產生 restart event。

重啟後的 snapshot 與相同 seed/config 建立的新 World 相同；
bullets 和 enemies 的 is 比較皆為 False，證明兩個 World 使用獨立清單。
   
    
  
#### 終端輸出紀錄：
0 bullets= [] enemies= [] cooldown= 0.0 spawn_timer= 0.8 events= [] life= 3

1 bullets= [99] enemies= [5] cooldown= 0.0 spawn_timer= 0.8 events= [] life= 3

2 bullets= [99] enemies= [5] cooldown= 0.0 spawn_timer= 0.75 events= [] life= 3

3 bullets= [] enemies= [5] cooldown= 0.0 spawn_timer= 0.7 events= [] life= 3