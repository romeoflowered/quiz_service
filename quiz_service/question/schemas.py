from datetime import datetime

from pydantic import BaseModel


class SQuestion(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True
