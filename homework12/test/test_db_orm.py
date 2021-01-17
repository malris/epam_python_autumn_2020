from contextlib import contextmanager

from homework12.db_mapper import Homework, Session, Student, Teacher


@contextmanager
def session_open():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def test_orm_tables():
    with session_open() as session:
        students = session.query(Student).all()
        expected_data = [[1, "Mike", "Mishin"], [2, "Sofi", "Smith"]]
        actual_data = list([st.id, st.first_name, st.last_name] for st in students)
        assert actual_data == expected_data


def test_join_tables():
    with session_open() as session:
        homeworks = (
            session.query(Homework, Teacher)
            .filter(Homework.teacher_id == Teacher.id)
            .all()
        )
        expected_data = [
            ["hw1", "Peter", "Petrov"],
            ["hw2", "Peter", "Petrov"],
            ["hw2", "Ivan", "Ivanov"],
        ]
        actual_data = [[hw.text, t.first_name, t.last_name] for hw, t in homeworks]
        assert actual_data == expected_data
