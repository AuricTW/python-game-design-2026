# Lab 01 - Environment, Git, and Tracebacks

> Course block: D1-B1, 09:00-12:00  
> Estimated total work: approximately 110 minutes  
> In class: 30-minute Parts A/B checkpoint during 11:20-11:50  
> Independent completion: approximately 80 minutes, due before Day 2  
> Protected lunch: 12:00-13:00 is not Lab catch-up time  
> AI level: **L0 Human-only**  
> Work mode: Individual

## Scenario

You have just joined a Python game team. Your first task is not to create polished graphics. It is to prove that you can reproduce your environment, reason about program state, use a traceback to locate the first actionable frame, and leave a reviewable Git history.

This Lab does not require a Pygame window and does not permit generative AI. You may consult official Python and Git documentation, the course Notebook, and notes you wrote yourself.

## Learning outcomes

By the end of this Lab, you should be able to:

1. Explain the relationship among a shell, Python interpreter, virtual environment, and package.
2. Use consistent `python -m ...` commands to identify the active Python environment.
3. Trace variables, types, branches, and loops by hand.
4. Read the final line of a traceback to identify the exception, then move upward to the first relevant frame in your own code.
5. Create small, meaningful, reversible Git commits.

## Delivery and completion window

The canonical student route is to obtain `lab01_student_starter.zip` from the course-site download button and extract it locally. The archive creates a self-contained top-level `lab01-work/` directory containing this README, the rubric, submission checklist, public-test contract, and starter code. Do not move individual files out of that directory. If the course site is unavailable, obtain the same ZIP from the instructor or a TA by local transfer.

S01 teaches the required concepts and launches this Lab. During the 11:20-11:50 checkpoint, use approximately 20 minutes for Part A and 10 minutes to begin Part B. Finish the remaining approximately 80 minutes independently and submit before Day 2. Stop at 12:00 for the protected 12:00-13:00 lunch break; lunch is not scheduled catch-up time.

## Required submission structure

Do not rename the provided templates, code, or test files. Save all text as UTF-8. Add one handwritten-evidence image with a clear filename only when you use the photo/scan route.

```text
lab01-work/
|-- .gitignore
|-- README.md                 # Name, student ID, commands, known limitations
|-- rubric.md
|-- submission_checklist.md
|-- requirements.txt          # Course-pinned test dependency
|-- evidence/
|   |-- preflight.txt         # Commands and complete text output
|   |-- trace.md              # Prediction, comparison, and handwritten evidence link
|   |-- trace_photo.(jpg/png/pdf) # Add one format; omit only with a TA note in trace.md
|   `-- debug_log.md          # Traceback analysis and repair record
|-- src/
|   `-- lab01.py              # The two required functions
|-- tests/
|   `-- test_lab01_student.py # At least four student-written tests
`-- tests_public/
    |-- README.md             # Published behaviour contract; do not modify
    `-- test_public_lab01.py  # Distributed public tests; do not modify
```

## Part A - Build a reproducible environment (20 minutes)

### A1. Select a supported interpreter before creating the environment

Download and extract `lab01_student_starter.zip` as described above, then enter `lab01-work/`. Before creating a virtual environment, confirm that the interpreter is 64-bit CPython 3.11, 3.12, or 3.13. Do not create an environment from macOS system Python 3.9 or from Python 3.14+.

macOS or Linux with a supported `python3`:

```bash
python3 --version
python3 -c "import struct; print(struct.calcsize('P') * 8)"
git init
python3 -m venv .venv
source .venv/bin/activate
```

If `python3 --version` is outside 3.11-3.13, use an explicitly installed interpreter such as `python3.11`, or use the Conda route:

```bash
conda create -n ncku-lab01 python=3.11
conda activate ncku-lab01
git init
python --version
```

Windows PowerShell with the Python launcher:

```powershell
py -3.11 --version
git init
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
```

After activation, run `python --version` again and use `python -m ...` throughout this Lab. Stop and ask for setup help if it does not report Python 3.11, 3.12, or 3.13, or if the bitness check does not report `64`.

### A2. Install the test tool and record the preflight

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Copy each command and its complete output into `evidence/preflight.txt`:

```bash
python --version
python -c "import sys; print(sys.executable)"
python -c "import struct; print(struct.calcsize('P') * 8)"
python -m pip --version
python -m pytest --version
git --version
git status
```

The `sys.executable` path should point into this project's `.venv`, or into the dedicated `ncku-lab01` Conda environment if you used that route. If it points to a system interpreter or a shared Conda `base`, stop and correct the environment before continuing.

### A3. Create the first commit

The package already contains `.gitignore`. Verify that it includes at least:

```text
.venv/
__pycache__/
.pytest_cache/
*.pyc
.DS_Store
```

Review the working tree, stage only the named Lab files, review the staged diff, and then commit:

```bash
git status
git diff
git add .gitignore README.md rubric.md submission_checklist.md requirements.txt
git add evidence/preflight.txt evidence/trace.md evidence/debug_log.md
git add src/__init__.py src/lab01.py
git add tests/test_lab01_student.py tests_public/README.md tests_public/test_public_lab01.py
git diff --staged
git commit -m "lab01: record reproducible preflight"
```

If Git reports that no author is configured, set your own name and university email. Do not copy an instructor's or classmate's identity.

## Part B - Predict before you run (15 minutes)

Trace the following code on paper **before you execute it**:

```python
energy = 5
score = 0

for turn in range(1, 5):
    if turn % 2 == 0:
        energy -= 2
        score += energy
    else:
        energy += 1
    print(turn, energy, score)
```

Create a four-row state table with at least these columns:

| `turn` | condition | `energy` before | `energy` after | `score` after | printed line |
|---:|---|---:|---:|---:|---|

Only then run the code. Add the following to `evidence/trace.md`:

1. Your original prediction.
2. The actual output.
3. A comparison. If your prediction was correct, identify the cell most likely to cause an error and explain why.
4. A relative link to a JPG, PNG, or PDF of the handwritten table stored in `evidence/`, or a dated TA verification note in `trace.md`.

## Part C - Implement the public function contract (35 minutes)

Implement these functions in `src/lab01.py`. You may add private helpers, but do not change the public names or parameters.

```python
def classify_score(score: int) -> str:
    """Return 'red', 'amber', or 'green' for an integer score from 0 to 100."""


def format_student_record(name: str, score: int) -> str:
    """Return '<trimmed name> | <score> | <classification>'."""
```

Required behaviour:

- `score` must be an `int`, but `bool` is not a valid score. Raise `TypeError` for an invalid type.
- `score` must be between 0 and 100 inclusive. Raise `ValueError` outside that range.
- Scores 0-59 are `red`, 60-79 are `amber`, and 80-100 are `green`.
- `name` must be a `str`. Raise `TypeError` for an invalid type.
- `name.strip()` must not be empty. Raise `ValueError` if it is.
- `format_student_record("  Ada  ", 80)` returns `"Ada | 80 | green"`.

Write at least four tests in `tests/test_lab01_student.py`, including:

1. One typical valid case.
2. At least one side of the 59/60 boundary.
3. At least one side of the 79/80 boundary.
4. One invalid case that checks the correct exception type.

Run from the project root:

```bash
python -m pytest -q
```

## Part D - Read the traceback instead of guessing (25 minutes)

Temporarily add this call at the bottom of `src/lab01.py`, run the file, and inspect the failure:

```python
print(format_student_record("Lin", "eighty"))
```

Do not immediately replace `"eighty"` with `80`. Answer these questions in `evidence/debug_log.md`:

1. What exception type and message appear on the final traceback line?
2. Which file and line are the top-level entry point?
3. Where is the first location in your own code that should be inspected?
4. Is this an environment, syntax, type, value, or logic failure? Why?
5. Should the repair be made at the caller or function boundary? How does the contract support your decision?

Remove the temporary call and confirm that all tests are green again. Record the smallest before-and-after diff and the test result in the debug log.

## Part E - Clean run and second commit (10 minutes)

Run from the project root:

```bash
python -m pytest -q
git status
git diff
git diff --check
```

Confirm that `.venv`, caches, and temporary files are not tracked. Then create the second commit:

```bash
git add README.md
git add evidence/preflight.txt evidence/trace.md evidence/debug_log.md
# If you used a photo, add its exact filename, for example:
# git add evidence/trace_photo.jpg
git add src/lab01.py tests/test_lab01_student.py
git diff --staged
git commit -m "lab01: implement score contract and debug evidence"
git status --short
```

## Acceptance criteria

- The seven-item preflight identifies a supported 64-bit Python 3.11-3.13 interpreter, pip, pytest, and Git in the dedicated environment.
- A four-row state table was completed before execution.
- Both public functions satisfy the type, range, boundary, and formatting contracts.
- At least four student-written tests pass.
- The debug log uses the traceback to identify the repair point and includes a minimal diff.
- At least two meaningful commits exist, and the working tree is clean.
- You can explain within 60 seconds why `bool` is not accepted as a score in this task.

See [rubric.md](rubric.md), [submission_checklist.md](submission_checklist.md), and the [public test contract](tests_public/README.md) before submitting.

## Lab completion ticket (at submission) - 5 minutes

Add these answers to the end of your submission note:

1. What was the most useful piece of information in a traceback today?
2. What is your environment confidence level: Red, Amber, or Green?
3. Provide the first eight characters of your final commit hash.
