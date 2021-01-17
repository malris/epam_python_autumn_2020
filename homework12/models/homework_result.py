from homework12.base import Base
from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String


class HomeworkResult(Base):
    __tablename__ = "homework_results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey("students.id"))
    homework_id = Column("homework_id", Integer, ForeignKey("homeworks.id"))
    solution = Column(String, nullable=False)
    check1 = CheckConstraint("length(solution) > 5")
