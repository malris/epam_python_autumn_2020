from contextlib import contextmanager

from homework12.db_mapper import Homework, HomeworkResult, Session, Student, Teacher


@contextmanager
def session_open():
    session = Session()
    try:
        yield session
    finally:
        session.close()


with session_open() as session:
    homeworks = (
        session.query(
            Student.last_name.label("student_surname"),
            Homework.created.label("creation_date"),
            Homework.teacher_id,
        )
        .filter(
            Student.id == HomeworkResult.author_id,
            Homework.id == HomeworkResult.homework_id,
        )
        .subquery()
    )

    completed_hws = (
        session.query(
            homeworks.c.student_surname,
            homeworks.c.creation_date,
            Teacher.last_name.label("teacher_surname"),
        )
        .filter(Teacher.id == homeworks.c.teacher_id)
        .all()
    )

    with open("report.csv", "w") as f_instance:
        f_instance.write(f"Student name, Creation date, Teacher name\n")
        for hw in completed_hws:
            f_instance.write(
                f"{hw.student_surname},{hw.creation_date},{hw.teacher_surname}\n"
            )
