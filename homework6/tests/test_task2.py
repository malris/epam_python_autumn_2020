from typing import Any, Sequence

import pytest
from homework6.task2.oop2 import (
    DeadlineError,
    Homework,
    HomeworkResult,
    Student,
    Teacher,
)


@pytest.mark.parametrize(
    ["homework_args", "expected_result"],
    [[("out_of_date_homework", 0), False], [("up_to_date_homework", 1), True]],
)
def test_homework_relevance(homework_args: Sequence[Any], expected_result: bool):
    assert Homework(*homework_args).is_active() == expected_result


def test_homework_result_get_invalid_attribute():
    st = Student("Ivan", "Ivanov")
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        HomeworkResult(st, "hw", "solution")


def test_student_do_homework():
    st = Student("Ivan", "Ivanov")
    hw = Homework("hw", 1)
    actual_hw_result = st.do_homework(hw, "solution")
    expected_hw_result = HomeworkResult(st, hw, "solution")
    assert actual_hw_result.homework is expected_hw_result.homework
    assert actual_hw_result.solution == expected_hw_result.solution


def test_student_miss_deadline():
    st = Student("Ivan", "Ivanov")
    hw = Homework("hw", 0)
    with pytest.raises(DeadlineError, match="You are late"):
        st.do_homework(hw, "solution")


@pytest.mark.parametrize(
    ["homework_args", "solution", "expected_result"],
    [[("hw1", 1), "bad", False], [("hw2", 1), "good solution", True]],
)
def test_teacher_check_homework(
    homework_args: Sequence[Any], solution: str, expected_result: bool
):
    teacher = Teacher("Peter", "Petrov")
    hw_r = HomeworkResult("auth", Homework(*homework_args), solution)
    assert teacher.check_homework(hw_r) is expected_result


def test_homework_done_list():
    teacher = Teacher("Peter", "Petrov")
    hw1 = Homework("hw1", 1)
    hw2 = Homework("hw2", 1)

    teacher.check_homework(HomeworkResult("st1", hw1, "solution"))
    hw_done_list_from_object = teacher.homework_done

    teacher.check_homework(HomeworkResult("st2", hw2, "bad"))
    teacher.check_homework(HomeworkResult("st2", hw1, "solution"))
    hw_done_list_from_class = Teacher.homework_done

    assert hw_done_list_from_object is hw_done_list_from_class


def test_teacher_reset_all_results():
    teacher = Teacher("Peter", "Petrov")
    hw1 = Homework("hw1", 1)
    hw2 = Homework("hw2", 1)
    teacher.check_homework(HomeworkResult("st", hw1, "solution"))
    teacher.check_homework(HomeworkResult("st", hw2, "solution"))
    teacher.reset_results()
    assert teacher.homework_done == {}


def test_teacher_reset_homework_results():
    teacher = Teacher("Peter", "Petrov")
    hw1 = Homework("hw1", 1)
    hw2 = Homework("hw2", 1)
    teacher.check_homework(HomeworkResult("st", hw1, "solution"))
    teacher.check_homework(HomeworkResult("st", hw2, "solution"))
    teacher.reset_results(hw1)
    assert teacher.homework_done == {hw2: ["solution"]}
