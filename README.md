# 📅 EventManager – Платформа для управління подіями

**EventManager** — це REST API застосунок, створений за допомогою Django та Django REST Framework, який дозволяє користувачам створювати події, приєднуватись до них, відмовлятись від участі, фільтрувати івенти, а також отримувати email-підтвердження після взаємодії.

## 🔧 Функціональність

- 🔐 JWT-автентифікація користувачів
- 🧑‍💼 Реєстрація та профілі користувачів з датою народження
- 🗓️ Створення, редагування, перегляд та видалення подій
- 🧍 Приєднання / відміна участі в подіях
- ⛔ Вікові обмеження (наприклад, 18+)
- 📨 Надсилання email після дій користувача
- 🔍 Фільтрація подій за параметрами: місто, дата, вікове обмеження
- 📑 Swagger / ReDoc документація

## ⚙️ Встановлення та запуск проєкту

1. Клонувати репозиторій:
   git clone <тут твій репозиторій>
   cd EventManager

2. Створити віртуальне середовище та активувати його:
   python -m venv venv
   source venv/bin/activate  # або venv\Scripts\activate для Windows

3. Встановити залежності:
   pip install -r requirements.txt

4. Створити `.env` файл у корені проєкту з таким вмістом:
   SECRET_KEY=твій_секретний_ключ
   DEBUG=True
   EMAIL_PORT=587
   EMAIL_HOST_USER=твоя_пошта@gmail.com
   EMAIL_HOST_PASSWORD=твій_пароль_або_app_password

5. Провести міграції:
   python manage.py migrate

6. Запустити сервер:
   python manage.py runserver

## 🔐 Авторизація

- POST `/api/token/` — отримати JWT токен
- POST `/api/token/refresh/` — оновити токен

## 📨 Email

Email надсилаються через Gmail SMTP. Для цього потрібно:
- Увімкнути 2-факторну автентифікацію в Google акаунті
- Створити App Password і використати його у `EMAIL_HOST_PASSWORD`

## 🔍 Приклади запитів

- GET `/events/` — список подій
- POST `/events/` — створити подію
- POST `/events/<id>/join/` — приєднатись
- POST `/events/<id>/cancel/` — скасувати участь
- GET `/user/` — свій профіль
- POST `/user/` — реєстрація
- GET `/organizer/` — побачити усіх організаторів
- GET `/organizer/id` — побачити конкретного організатора

Фільтрація подій:
- `/events/?location_city=lviv`
- `/events/?age_limit=true`

## 📘 Документація

- Swagger: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## 🛠 Стек технологій

- Django 5.2.3
- Django REST Framework
- Simple JWT
- drf-yasg (Swagger)
- Gmail SMTP
- django-filter

## 📎 Автор

Зроблено з ❤️ Іллею Петуховим 
