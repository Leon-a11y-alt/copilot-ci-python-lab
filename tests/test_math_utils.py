"""Tests for the mathematical utility functions."""

from src.math_utils import add


def test_add():
    """Adding 2 and 3 should return 5."""
    assert add(2, 3) == 5
