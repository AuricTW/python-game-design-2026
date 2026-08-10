# Traceback and Repair Log

## Observation and exception type

```python
print(format_student_record("Lin", "eighty"))
```

執行 `python src/lab01.py` 後，traceback 最後一行為：

```text
TypeError: score must be an integer, not bool
```

## First relevant frame in my code

進入點是 `src/lab01.py` 第 34 行。實際呼叫路徑為：

```text
src/lab01.py:34  <module>
src/lab01.py:30  format_student_record
src/lab01.py:9   classify_score
```

第一個位置是 `classify_score` 第 9 行，該行根據型別給出 `TypeError`。第 30 行則顯示錯誤的字串分數是由 `format_student_record` 傳入。

## Smallest reproducible case

```powershell
python -c "from src.lab01 import format_student_record; format_student_record('Lin', 'eighty')"
```

##  Hypothesis and evidence

型別錯誤。
要求 `score` 必須是 `int`，但傳入了 `str`。

函式邊界應保留型別驗證並拒絕字串分數；依照契約，責任在傳入錯誤型別的 caller，而不是函式邊界。修復方式是移除暫時呼叫。

## Minimal repair and verification command

加入差異：

```diff
+print(format_student_record("Lin", "eighty"))
```

修復時移除：

```diff
-print(format_student_record("Lin", "eighty"))
```

移除後結果：

```text
> python -c "import src.lab01"
> python -m pytest -q
........................                                                 [100%]
24 passed in 0.09s
```
