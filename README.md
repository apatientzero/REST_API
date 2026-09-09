# Домашнее задание "Создание REST API на FastApi_часть 1"
полное решение с Docker-контейнеризацией

### Запуск проекта

Сборка и запуск

docker-compose up --build

API будет доступен по адресу:

http://localhost:8000

Swagger UI: http://localhost:8000/docs

### Примеры использования API

Создать объявление

curl -X POST "http://localhost:8000/advertisement" \
  -H "Content-Type: application/json" \
  
  -d '{
    "title": "iPhone 13",
    "description": "Продаю iPhone 13, состояние отличное",
    "price": 50000.00,
    "author": "Mike Tyson"
  }'


### Получить объявление по ID

curl -X GET "http://localhost:8000/advertisement/1"


### Поиск объявлений

curl -X GET "http://localhost:8000/advertisement?title=iPhone&min_price=40000&max_price=60000"


### Обновить объявление

curl -X PATCH "http://localhost:8000/advertisement/1" \
  
  -H "Content-Type: application/json" \
  
  -d '{"price": 45000.00}'


### Удалить объявление

curl -X DELETE "http://localhost:8000/advertisement/1"
