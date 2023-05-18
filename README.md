# Quiz Service

Quiz Service - это RESTful API для управления викториной. Он позволяет пользователям получать случайные вопросы для викторины и добавлять новые вопросы в базу данных.

## Используемые технологии

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker

## Начало работы

### Предварительные требования

- Docker

### Установка и настройка

1. Клонируйте репозиторий:
  
  git clone https://github.com/romeoflowered/quiz_service.git

2. Перейдите в директорию проекта:  
  
  cd quiz_service

3. Соберите Docker-образ: 
  
  docker build -t quiz-service .

4. Запустим наше приложение для проверки без БД:
  
  docker run -p 9000:8000 "name-image"

5. Откройте файл docker-compose.yml в текстовом редакторе. 

  Проверьте настройки сервиса quiz-service. Убедитесь, что они соответствуют вашим требованиям. Например, вы можете изменить порт, на котором будет доступен сервис, или       добавить другие переменные среды, если это необходимо. 

6. Создать файл .env-non-dev и заполняем данными:

  DB_HOST=db
  DB_PORT=5432
  DB_USER=*
  DB_PASS=*
  DB_NAME=quiz_service

  POSTGRES_DB=quiz_service
  POSTGRES_USER=*
  POSTGRES_PASSWORD=*
  
7. Соберите Docker-Compose:

  docker compose build

8. Теперь выполните команду docker-compose up для сборки и запуска контейнеров:

  docker-compose up -d

После успешного выполнения команды, сервис должен быть доступен на указанном вами порту. Вы можете использовать API-клиент, такой как cURL или Postman, для отправки запросов к сервису.

Пример запроса к POST API сервиса:

curl -X POST http://localhost:8000/quiz/questions -H "Content-Type: application/json" -d '{"questions_num": 5}'

Здесь мы отправляем POST-запрос на  http://localhost:8000/quiz/questions с параметром questions_num равным 5.
