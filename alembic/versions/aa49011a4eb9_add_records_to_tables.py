"""add records to tables

Revision ID: aa49011a4eb9
Revises: 5b030f9f02da
Create Date: 2020-12-28 11:17:29.713080

"""
import datetime as dt

from alembic import op

# revision identifiers, used by Alembic.
revision = "aa49011a4eb9"
down_revision = "5b030f9f02da"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        "INSERT INTO teachers(first_name, last_name)  VALUES ('Peter', 'Petrov'), ('Ivan', 'Ivanov')"
    )
    op.execute(
        "INSERT INTO students(first_name, last_name)  VALUES ('Mike', 'Mishin'), ('Sofi', 'Smith')"
    )
    cur_date = dt.datetime.now()
    interval = lambda x: dt.timedelta(days=x)
    op.execute(
        f"INSERT INTO homeworks(text, deadline, teacher_id, created)"
        f"VALUES"
        f"('hw1', '{interval(0)}', '1', '{cur_date}' ),"
        f"('hw2', '{interval(2)}', '1', '{cur_date}' ),"
        f"('hw2', '{interval(2)}', '2', '{cur_date}' )"
    )
    op.execute(
        "INSERT INTO homework_results(author_id, homework_id, solution)"
        "VALUES"
        "(1, 2, 'hw1_solution'),"
        "(2, 3, 'hw2_solution')"
    )


def downgrade():
    op.execute("DELETE FROM homework_results WHERE id < 3")
    op.execute("DELETE FROM homeworks WHERE id < 4")
    op.execute("DELETE FROM students WHERE id < 3")
    op.execute("DELETE FROM teachers WHERE id < 3")
