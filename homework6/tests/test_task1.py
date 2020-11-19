from unittest.mock import patch

from homework6.task1.counter import instances_counter


class A:
    pass


@patch.object(A, "__init__", lambda self, x: None)
def test_instance_counter_get():
    instances_counter(A)
    assert A.get_created_instances() == 0
    a, _, _ = A(1), A(2), A(3)
    assert a.get_created_instances() == 3


@patch.object(A, "__init__", lambda self, x: None)
def test_instance_counter_reset():
    instances_counter(A)
    assert A.reset_instances_counter() == 0
    a, _, _ = A(1), A(2), A(3)
    assert a.reset_instances_counter() == 3
    assert a.get_created_instances() == 0
