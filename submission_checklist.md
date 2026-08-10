# Lab 01 Submission Checklist

Check every item before submitting. If an item does not apply, explain why instead of deleting it.

## Delivery window

- [ ] I started from the complete `lab01_student_starter.zip`, obtained from the course site or by instructor/TA local transfer.
- [ ] I completed the independent portion and am submitting before Day 2.

## Identity and execution

- [ ] `README.md` includes my name, student ID, Python version, and execution commands.
- [ ] I reran every command from the project root.
- [ ] `python --version` reports Python 3.11, 3.12, or 3.13, and the bitness command reports `64`.
- [ ] `python -c "import sys; print(sys.executable)"` points into this project's `.venv` or the dedicated `ncku-lab01` Conda environment, not a system interpreter or shared `base`.

## Required files

- [ ] `evidence/preflight.txt` contains all seven commands and their complete text output.
- [ ] `evidence/trace.md` contains the prediction, actual result, comparison, and a relative link to handwritten evidence or a dated TA verification note.
- [ ] If I used a photo or scan, it is stored inside `evidence/` and included in the final commit.
- [ ] `.gitignore`, `rubric.md`, `submission_checklist.md`, and `tests_public/README.md` are present.
- [ ] `evidence/debug_log.md` answers all five traceback questions and includes the minimal diff.
- [ ] `src/lab01.py` imports without producing top-level debug output.
- [ ] `tests/test_lab01_student.py` contains at least four focused tests.

## Verification

- [ ] `python -m pytest -q` passes.
- [ ] I checked 0, 59, 60, 79, 80, 100, and at least one invalid input.
- [ ] `git diff --check` reports no errors.
- [ ] I reviewed both `git diff` and `git diff --staged` before the final commit.
- [ ] `git status --short` is empty. If the instructor explicitly permits an untracked local file, I have named and explained it in the submission note.

## Git and integrity

- [ ] At least two understandable commits exist, and I can explain the purpose of each.
- [ ] `.venv/`, `__pycache__/`, `.pytest_cache/`, and `*.pyc` are not committed.
- [ ] I completed this L0 Lab without generative AI or generative code completion.
- [ ] I can explain one boundary and one exception decision without looking at the code.
- [ ] I completed the Lab completion ticket in my submission note.

## Final submission information

- Repository or submission URL:
- Branch:
- Final commit:
- Known limitations (`None` if there are none):
