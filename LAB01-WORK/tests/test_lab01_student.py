"""Add at least four focused student-authored tests below."""

import pytest

from src.lab01 import classify_score, format_student_record


def test_typical_valid_score_is_amber() -> None:
    assert classify_score(70) == "amber"


def test_59_is_last_red_score() -> None:
    assert classify_score(59) == "red"


def test_60_is_first_amber_score() -> None:
    assert classify_score(60) == "amber"


def test_79_is_last_amber_score() -> None:
    assert classify_score(79) == "amber"


def test_80_is_first_green_score() -> None:
    assert classify_score(80) == "green"


def test_boolean_score_is_rejected() -> None:
    with pytest.raises(TypeError):
        classify_score(True)


def test_out_of_range_score_is_rejected() -> None:
    with pytest.raises(ValueError):
        classify_score(101)


def test_record_trims_the_name() -> None:
    assert format_student_record("  Lin  ", 60) == "Lin | 60 | amber"
