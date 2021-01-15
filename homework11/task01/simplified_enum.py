"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""
from typing import Any


class SimplifiedEnum(type):
    def __new__(cls, name, bases, dict) -> Any:
        class_instance = super().__new__(cls, name, bases, dict)
        setattr(class_instance, "_enum_attr_name", f"_{name}__keys")
        return class_instance

    def __getattr__(self, key):
        if key in self.__dict__[self._enum_attr_name]:
            return key
        raise KeyError(key)

    def __iter__(self):
        return iter(self.__dict__[self._enum_attr_name])

    def __len__(self):
        return len(self.__dict__[self._enum_attr_name])
