import pytest
from homework9.task02.contextManager import Suppressor, suppressor


def test_context_manager_class_realization_suppresses_exceptions():
    with Suppressor(ValueError):
        assert int("not_a_number")
    with Suppressor(IndexError):
        assert [][2]


def test_context_manager_generator_realization_suppresses_exceptions():
    with suppressor(ValueError):
        assert int("not_a_number")
    with suppressor(IndexError):
        assert [][2]


def test_context_manager_class_realization_raises_exceptions():
    with pytest.raises(IndexError):
        with Suppressor(ValueError):
            [][2]


def test_context_manager_generator_realization_raises_exceptions():
    with pytest.raises(IndexError):
        with suppressor(ValueError):
            [][2]
