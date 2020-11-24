import datetime as dt
from typing import Any, Sequence

import pytest
from homework5.oop1.oop1 import Homework, Student, Teacher


@pytest.mark.parametrize(
    ["args", "expected_result"], [[("homework1", 0), False], [("homework2", 2), True]]
)
def test_homework_is_active(args: Sequence[Any], expected_result: bool):
    hw = Homework(*args)
    assert hw.is_active() == expected_result


@pytest.mark.parametrize(["homework", "expected_result"], [(Homework("text", 0), None)])
def test_student_do_homework_too_late(homework: Homework, expected_result: Any, capfd):
    student = Student("Ivan", "Ivanov")
    actual_result = student.do_homework(homework)
    out, err = capfd.readouterr()
    assert actual_result is None
    assert out == "You are late\n"


@pytest.mark.parametrize("homework", [Homework("text", 1)])
def test_student_do_homework_on_time(homework: Homework):
    student = Student("Ivan", "Ivanov")
    assert student.do_homework(homework) is homework


@pytest.mark.parametrize("args", [("homework1", 0), ("homework2", 2)])
def test_teacher_create_homework(args: Sequence[Any]):
    teacher = Teacher("Ivan", "Ivanov")
    hw = teacher.create_homework(*args)
    assert hw.text == args[0]
    assert hw.deadline == dt.timedelta(days=args[1])
