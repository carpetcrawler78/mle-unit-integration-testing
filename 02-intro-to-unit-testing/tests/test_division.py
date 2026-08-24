"""Baseline divide tests for the parametrization refactor."""

# @TODO Exercise (file-based):
# Objective: Refactor this baseline test into a parameterized pytest test.
# Edit files:
# - tests/test_division.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_division.py
# Solution:
# - tests/test_division_solution.py
# - 02-intro-to-unit-testing.ipynb (<summary>Solution</summary> block)

import pytest

from src.unit_test_examples.division import divide


@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (3, 2, 1.5),
        (5, 5, 1),
        (6, 2, 3),
        (-2, 0, "Cannot divide by zero"),
        (10, -2, -5),
    ],
)
def test_divide(x, y, expected_result):
    assert divide(x, y) == expected_result
    pass
    # This baseline is intentionally repetitive so it can be refactored.
    #assert divide(3, 2) == 1.5
    #assert divide(5, 5) == 1
    #assert divide(6, 2) == 3
    #assert divide(-2, 0) == "Cannot divide by zero"
    #assert divide(10, -2) == -5
