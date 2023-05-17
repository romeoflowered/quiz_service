FROM python:3.10.4

RUN mkdir /quiz

WORKDIR /quiz

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /quiz/docker/*.sh

CMD ["gunicorn", "quiz_service.main:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]

