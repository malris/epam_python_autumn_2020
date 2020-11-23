from unittest.mock import patch

from homework6.task1.counter import instances_counter


@instances_counter
class A:
    pass


def test_instance_counter_get():
    assert A.get_created_instances() == 0
    a, _, _ = A(), A(), A()
    assert a.get_created_instances() == 3
    a.reset_instances_counter()


def test_instance_counter_reset():
    assert A.reset_instances_counter() == 0
    a, _, _ = A(), A(), A()
    assert a.reset_instances_counter() == 3
    assert a.get_created_instances() == 0
