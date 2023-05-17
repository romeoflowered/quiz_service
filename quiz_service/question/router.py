import requests
from fastapi import APIRouter
from sqlalchemy import delete, select

from quiz_service.database import session_maker
from quiz_service.question.models import Question
from quiz_service.question.request import QuestionRequest
from quiz_service.question.schemas import SQuestion

router = APIRouter(
    prefix="/questions",
    tags=["Вопросы"],
)


@router.get("/{question_id}")
def get_question_by_id(question_id: int):
    with session_maker() as session:
        query = select(Question).filter_by(id=question_id)
        result = session.execute(query)
        question = result.scalar_one_or_none()
        return SQuestion(
                id=question.id,
                question=question.question,
                answer=question.answer,
                created_at=question.created_at
            ) if question else {"message": "Вопрос не найден."}


@router.post("")
def get_quiz_questions(request: QuestionRequest):
    questions_num = request.questions_num

    added_questions = []

    with session_maker() as session:
        while len(added_questions) < questions_num:
            response = requests.get(f"https://jservice.io/api/random?count={questions_num}")
            question_data = response.json()[0]
            question = session.query(Question).filter_by(
                question=question_data["question"]
            ).first()

            if not question:
                new_question = Question(
                    question=question_data["question"],
                    answer=question_data["answer"],
                )
                session.add(new_question)
                session.commit()
                added_questions.append(new_question)

    if len(added_questions) >= 2:
        return added_questions[-2]
    else:
        return {}


@router.delete("")
def delete_question_by_id(question_id: int):
    with session_maker() as session:
        delete_query = delete(Question).where(Question.id == question_id)
        session.execute(delete_query)
        session.commit()
