# Lab 01 Rubric - 100 points

| Dimension | Points | Full evidence | Partial evidence | Missing or invalid evidence |
|---|---:|---|---|---|
| Reproducible environment | 20 | All seven preflight items are complete; Python is 64-bit 3.11-3.13 and points to `.venv` or the dedicated `ncku-lab01` Conda environment; commands can be rerun | One item is missing or the environment path is not fully explained | No text output, an unsupported interpreter, or the environment cannot be reproduced |
| Predict-first state trace | 15 | Four complete rows, written before execution, with a specific comparison and a photo or dated TA verification | A table exists but fields, provenance, or reasoning are incomplete | Only program output, a reconstructed prediction, or no handwritten evidence |
| Public function contract | 25 | Types, range, all three bands, trimming, and output format are correct | Main cases work, but one boundary or exception is missing | Import fails, interface changed, or core behaviour is incorrect |
| Student-written tests | 15 | At least four focused tests cover a valid case, boundaries, and an exception | Tests run, but cover only the happy path or use weak assertions | No tests or tests do not run |
| Traceback and repair reasoning | 15 | Exception, call path, repair point, classification, and contract reasoning are clear; minimal diff included | The failure is located, but reasoning or repair evidence is incomplete | Guesswork, screenshot only, or no explanation |
| Git and submission hygiene | 10 | At least two meaningful commits; environment and caches ignored; clean working tree | Commit is too large, message is vague, or minor unnecessary files are included | No commit, `.venv` submitted, or provenance is unclear |

## Scoring constraints

- Passing public tests is one correctness signal; it does not automatically earn full credit.
- If `src/lab01.py` cannot be imported, Public function contract is capped at 10/25.
- Without predict-first evidence, Predict-first state trace earns 0. A reconstruction written after execution must not be presented as a prior prediction.
- An L0 violation is handled under the Syllabus and academic-integrity policy, not as an ordinary point deduction.

## Explain-back questions

The TA may select one question. Answer in your own words.

1. Why can `python -m pytest` reduce the risk of using the wrong interpreter compared with invoking `pytest` directly?
2. Why do you normally read the last traceback line first, then search upward for a frame in your own file?
3. Python reports `isinstance(True, int)` as true. Why does this task still reject `bool`?
4. Which commit is easiest to revert safely, and why?
