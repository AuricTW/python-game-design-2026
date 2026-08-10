"""Lab 01 public functions.
"""


def classify_score(score: int) -> str:
    """Return ``red``, ``amber``, or ``green`` for a score from 0 to 100.""" # 根據分數的範圍回傳對應的顏色分類

    if isinstance(score, bool) or not isinstance(score, int):
        raise TypeError("score must be an integer, not bool")
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")

    if score < 60:
        return "red"
    if score < 80:
        return "amber"
    return "green"


def format_student_record(name: str, score: int) -> str:
    """Return ``<trimmed name> | <score> | <classification>``."""

    if not isinstance(name, str):
        raise TypeError("name must be a string")

    trimmed_name = name.strip()
    if not trimmed_name:
        raise ValueError("name must not be blank")

    classification = classify_score(score)
    return f"{trimmed_name} | {score} | {classification}"
