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

## Доработка: добавляем фильтры по description и created_at

### Что изменил:

Файлы: 

crud.py:

- Добавлены параметры description и created_at в функцию get_advertisements + логика фильтрации

main.py:

- Добавлены description и created_at как query-параметры + импорт date

### Примеры запросов после доработки

Поиск по описанию (подстрока, регистронезависимо)

curl "http://localhost:8000/advertisement?description=отличное+состояние"

Поиск по дате создания (формат YYYY-MM-DD)

curl "http://localhost:8000/advertisement?created_at=2026-09-10"

Комбинированный поиск

curl "http://localhost:8000/advertisement?title=iPhone&description=новый&created_at=2026-09-10&min_price=40000"

### Как проверить
1. Запустите контейнеры: docker-compose up --build
2. Откройте Swagger UI: http://localhost:8000/docs
3. В эндпоинте GET /advertisement теперь видны все параметры, включая description и created_at