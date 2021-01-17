from homework12.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Homework(Base):
    __tablename__ = "homeworks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    deadline = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    created = Column(String, nullable=False)
