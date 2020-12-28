import os

from homework12.base import Base
from homework12.models.homework import Homework
from homework12.models.homework_result import HomeworkResult
from homework12.models.student import Student
from homework12.models.teacher import Teacher
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

hw12_dir = os.path.dirname(__file__)
engine = create_engine(f"sqlite:///{hw12_dir}/db.sqlite")
Session = sessionmaker(bind=engine)

Base.prepare(engine, reflect=True)
