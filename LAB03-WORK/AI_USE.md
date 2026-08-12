# Lab 03 L1 Use Record

Choose one:

- [ ] No AI used.
- [X] L1 conceptual assistance used after the TA checkpoint; record it below.

Tool / service and date: gpt5.6 and 自己的本地蒸餾模型(deepseek家族) 、2026-08-11～12

Question asked (concept, counterexample, isolation advice or test-name idea only):   
請工具重新說明講義、解釋 class 、程式碼與指令、分析錯誤原因，並提供實作方向和引導。沒有要求工具直接修改檔案；程式與文件皆由本人理解後輸入及修改。

Hint received:  
釐清 World 與各實體的責任、self 的用途、cooldown 與 spawn timer 的更新順序、seeded RNG、唯一 ID，以及使用保留清單安全移除越界實體。

How I evaluated the hint:  
以 focused public tests、手算 trace、完整測試及 deterministic run 驗證。

What I implemented myself:  
自行輸入並修正 bullet/enemy lifecycle、測試與 evidence。

Evidence that no submission-ready code, test or patch was adopted:
我逐步實作、遇到語法與邏輯錯誤後自行修正，而不是貼入完整 patch。
