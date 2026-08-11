# Lab 02 State Table

Complete the **prediction** columns before running the scenario.
Configuration: `player_speed=100.0`, `max_dt=0.05`, initial player `(480, 504)`.

| Step | Input and `dt` | Predicted tick / elapsed / x / y | Calculation | Observed result | Difference and correction |
|---:|---|---|---|---|---|
| 1 | right, 0.05 | `1 / 0.05 / 485.000 / 504.000` | `bounded_dt = min(0.05, 0.05) = 0.05`；方向為 `(1, 0)`；位移為 `(1, 0) * 100 * 0.05 = (5, 0)`；位置為 `(480, 504) + (5, 0) = (485, 504)`。 | tick=1, elapsed=0.05, x=485.000, y=504.000 | |
| 2 | right + up, 0.05 | `2 / 0.10 / 488.536 / 500.464` | 方向 `(1, -1)` 的長度為 `sqrt(2)`，所以正規化後為 `(1/sqrt(2), -1/sqrt(2))`；位移約為 `(3.536, -3.536)`；位置約為 `(485, 504) + (3.536, -3.536) = (488.536, 500.464)`。 | tick=2, elapsed=0.10, x=488.536, y=500.464 | |
| 3 | left + right, 0.05 | `3 / 0.15 / 488.536 / 500.464` | 水平方向為 `right - left = 1 - 1 = 0`；垂直方向也沒有輸入，所以位移為 `(0, 0)`，位置不變。 | tick=3, elapsed=0.15, x=488.536, y=500.464 | |
| 4 | neutral, 0.20 | `4 / 0.20 / 488.536 / 500.464` | `bounded_dt = min(0.20, 0.05) = 0.05`；沒有方向輸入，因此方向與位移都是 `(0, 0)`。`tick` 增加一次，`elapsed` 只增加 `0.05`，位置不變。 | tick=4, elapsed=0.20, x=488.536, y=500.464 | |

無差異；預測與實測相符。

Explain why diagonal input must be normalized:

 `(1, -1)` 的對角線方向長度是 `sqrt(2)`，但單軸方向的長度是 `1`。將非零方向除以它的歐幾里得長度後，向量長度會變成 `1`。


實際：

Step 1: tick=1, elapsed=0.05, x=485.000, y=504.000
Step 2: tick=2, elapsed=0.10, x=488.536, y=500.464
Step 3: tick=3, elapsed=0.15, x=488.536, y=500.464
Step 4: tick=4, elapsed=0.20, x=488.536, y=500.464