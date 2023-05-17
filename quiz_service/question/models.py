import datetime

from sqlalchemy import Column, DateTime, Integer, String

from quiz_service.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)
