"""Published Lab 01 behaviour checks. Students must not edit this file."""

from __future__ import annotations

import pytest

from src.lab01 import classify_score, format_student_record


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (0, "red"),
        (59, "red"),
        (60, "amber"),
        (79, "amber"),
        (80, "green"),
        (100, "green"),
    ],
)
def test_classification_boundaries(score: int, expected: str) -> None:
    assert classify_score(score) == expected


@pytest.mark.parametrize("score", [-1, 101])
def test_out_of_range_scores_are_rejected(score: int) -> None:
    with pytest.raises(ValueError):
        classify_score(score)


@pytest.mark.parametrize("score", [True, False, 60.0, "60", None])
def test_non_integer_scores_are_rejected(score: object) -> None:
    with pytest.raises(TypeError):
        classify_score(score)  # type: ignore[arg-type]


def test_record_is_trimmed_and_classified() -> None:
    assert format_student_record("  Ada  ", 80) == "Ada | 80 | green"


def test_blank_name_is_rejected() -> None:
    with pytest.raises(ValueError):
        format_student_record("   ", 70)


def test_non_string_name_is_rejected() -> None:
    with pytest.raises(TypeError):
        format_student_record(123, 70)  # type: ignore[arg-type]
