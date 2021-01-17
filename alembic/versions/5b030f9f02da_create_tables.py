"""create tables

Revision ID: 5b030f9f02da
Revises: 
Create Date: 2020-12-28 10:14:39.761583

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "5b030f9f02da"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "teachers",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("first_name", sa.String, nullable=False),
        sa.Column("last_name", sa.String, nullable=False),
    )
    op.create_table(
        "students",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("first_name", sa.String, nullable=False),
        sa.Column("last_name", sa.String, nullable=False),
    )
    op.create_table(
        "homeworks",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("text", sa.String, nullable=False),
        sa.Column("deadline", sa.String, nullable=False),
        sa.Column("teacher_id", sa.Integer, sa.ForeignKey("teachers.id")),
        sa.Column("created", sa.String, nullable=False),
    )

    op.create_table(
        "homework_results",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("author_id", sa.Integer, sa.ForeignKey("students.id")),
        sa.Column("homework_id", sa.Integer, sa.ForeignKey("homeworks.id")),
        sa.Column("solution", sa.String, nullable=False),
        sa.CheckConstraint("length(solution) > 5", "check1"),
    )


def downgrade():
    op.drop_table("homework_results")
    op.drop_table("homeworks")
    op.drop_table("students")
    op.drop_table("teachers")
