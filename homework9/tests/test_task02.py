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
    with suppressor(TypeError):
        with suppressor(list):
            assert [][1]


@pytest.mark.parametrize(
    ["actual_error", "expected_error"],
    [
        [IndexError, ValueError],
        [IndexError, tuple],
        [IndexError, "not_an_error"],
    ],
)
def test_context_manager_class_realization_raises_exceptions(
    actual_error, expected_error
):
    with pytest.raises(actual_error):
        with Suppressor(expected_error):
            [][2]


@pytest.mark.parametrize(
    ["actual_error", "expected_error"],
    [
        [IndexError, ValueError],
        [TypeError, tuple],
        [TypeError, "not_an_error"],
    ],
)
def test_context_manager_generator_realization_raises_exceptions(
    actual_error, expected_error
):
    with pytest.raises(actual_error):
        with suppressor(expected_error):
            [][2]
