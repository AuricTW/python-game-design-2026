# Predict-first Trace

## Original handwritten prediction

精美手寫表格：[20260810_164905.jpg](20260810_164905.jpg)


| `turn` | 狀態?(不太知道這要寫什麼) | `energy` 變更前 | `energy` 變更後 | `score` 變更後 | 印出內容 |
|---:|---|---:|---:|---:|---|
| 1 | False， `else` | 5 | 6 | 0 | `1 6 0` |
| 2 | True，`if` | 6 | 4 | 4 | `2 4 4` |
| 3 | False， `else` | 4 | 5 | 4 | `3 5 4` |
| 4 | True，`if` | 5 | 3 | 7 | `4 3 7` |


## Actual output
執行指令：

```text
> python test.py
1 6 0
2 4 4
3 5 4
4 3 7
```

## Difference and corrected mental model

手寫表與實際輸出一致。最容易算錯的是第 2 回合的 `score after`：程式會先將 `energy` 從 6 減為 4，再把更新後的 4 加入 `score`。
