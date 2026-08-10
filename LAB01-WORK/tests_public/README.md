# Lab 01 Public Test Contract

This document publishes the interface and representative behaviour. It does not contain an instructor solution or hidden tests. The executable `test_public_lab01.py` is distributed in this same `tests_public/` directory.

## Import contract

The following import must succeed when tests are run from the project root:

```python
from src.lab01 import classify_score, format_student_record
```

Importing the functions must not read keyboard input, print output, modify files, or open a window.

## Published cases

| Case | Call | Expected result |
|---|---|---|
| Lowest valid | `classify_score(0)` | `"red"` |
| First amber | `classify_score(60)` | `"amber"` |
| Last amber | `classify_score(79)` | `"amber"` |
| First green | `classify_score(80)` | `"green"` |
| Highest valid | `classify_score(100)` | `"green"` |
| Trimmed record | `format_student_record("  Ada  ", 80)` | `"Ada | 80 | green"` |
| Below range | `classify_score(-1)` | raises `ValueError` |
| Above range | `classify_score(101)` | raises `ValueError` |
| Boolean score | `classify_score(True)` | raises `TypeError` |
| Blank name | `format_student_record("   ", 70)` | raises `ValueError` |

`score` follows normal Python `int` behaviour except that `bool` is explicitly rejected. Hidden tests use different values from these same published behaviour families; they do not add requirements about integer subclasses or the order used to validate two simultaneously invalid arguments.

## Test-design boundary

The assessment may use names and scores not listed above, but it will check only the same behaviour families published in the Lab README. Do not hard-code the table values.

Add at least four tests of your own. Prefer one clear behaviour per test, such as "60 is the first amber value," rather than placing every case into one test.

## Public-test layout

```text
tests_public/
|-- README.md
`-- test_public_lab01.py      # Distributed by the course; do not modify
```

Run the complete public and student-authored suite from the project root:

```bash
python -m pytest -q
```

Do not create an unconditional test that only pretends to pass.
