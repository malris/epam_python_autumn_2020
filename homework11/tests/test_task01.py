from collections.abc import Iterable

import pytest
from homework11.task01.simplified_enum import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "GREEN", "BLUE", "YELLOW")


def test_attribute_in_enum():
    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.YELLOW == "YELLOW"


def test_attribute_not_in_enum():
    with pytest.raises(KeyError, match="BLACK"):
        ColorsEnum.BLACK


def test_enum_is_iterable():
    assert isinstance(ColorsEnum, Iterable)


def test_get_enum_length():
    assert len(ColorsEnum) == 4
