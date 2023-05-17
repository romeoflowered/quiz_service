from fastapi import FastAPI

from quiz_service.question.router import router

app = FastAPI(title="QUIZ_SERVICE")

app.include_router(router)
