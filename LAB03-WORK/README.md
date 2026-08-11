# Lab 03 Student Overlay

Continue in **your own completed Lab 02 repository**. This overlay deliberately does not include a completed Lab 02 model.

Extract the overlay outside the repository, verify your Lab 02 files, and merge the overlay into the repository root. Do not replace the repository directory in Finder or Explorer.

macOS/Linux:

```bash
test -f src/star_sprout_lab/model.py
test -f tests/test_lab02_student.py
test -f tests_public/test_public_lab02.py
unzip -q ../lab03_student_starter.zip -d ../lab03-overlay
cp -R ../lab03-overlay/. .
test -f src/star_sprout_lab/model.py
test -f tests/test_lab02_student.py
test -f tests_public/test_public_lab02.py
git status --short
```

PowerShell:

```powershell
Test-Path src/star_sprout_lab/model.py
Test-Path tests/test_lab02_student.py
Test-Path tests_public/test_public_lab02.py
Expand-Archive -Path ..\lab03_student_starter.zip -DestinationPath ..\lab03-overlay -Force
Copy-Item ..\lab03-overlay\* . -Recurse -Force
Test-Path src/star_sprout_lab/model.py
Test-Path tests/test_lab02_student.py
Test-Path tests_public/test_public_lab02.py
git status --short
```

The overlay adds or updates only these student-facing paths; it does not contain `src/`:

```text
evidence/
tests/
tests_public/
AI_USE.md
```

Also keep the included `LAB_README.md`, `rubric.md`, `submission_checklist.md`, and `public_test_contract.md` beside your submission evidence.

Run the cumulative checks:

```bash
python -m unittest discover -s tests_public -v
python -m unittest discover -s tests -v
python -m star_sprout_lab --headless --seed 42 --frames 240 --assert-deterministic
```

Before Lab 03 implementation, the cumulative public suite must report `Ran 21 tests` with the expected `FAILED (failures=5)`. All Lab 02 checks must remain green. A valid Lab 03 implementation makes all 21 public tests green.

AI level: L0 for the first 90 minutes. After the TA checkpoint, L1 permits conceptual hints only; it does not permit generated deliverable code, tests or patches.
