# RESTful API для управления списком задач

## Требования

Для запуска проекта вам потребуется установить следующие зависимости:

- Python 3.11
- Flask
- Flask-MySQLdb
- python-dotenv
- Другие зависимости, указанные в файле `requirements.txt`

Вы также должны настроить базу данных MySQL для хранения задач.

## Установка

1. Клонируйте репозиторий:

```bash
git clone <https://github.com/Yanina-t/task_RAZRABOT>
cd task_RAZRABOT
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл .env на основе sample_env:
```bash
cp sample_env .env
```

## Настройка базы данных
1. Создайте базу данных MySQL и укажите соответствующие параметры подключения в файле .env.

## Запуск приложения
1. Запустите приложение:
```bash
flask run 
```
* Press CTRL+C to quit

## Тестирование
1. Запустите тесты:
```bash
pytest --cov=app
```
2.  Сохраните результаты тестов и сгенерируйте отчет о покрытии кода тестами в формате HTML, чтобы получить более подробную информацию о покрытии кода: 
```bash
pytest --cov=app --cov-report=html
```

## Использование
API предоставляет следующие эндпоинты:

* `POST /tasks`: Создание новой задачи.  
* `GET /tasks`: Получение списка всех задач.  
* `GET /tasks/<id>`: Получение информации о конкретной задаче.  
* `PUT /tasks/<id>`: Обновление информации о задаче.  
* `DELETE /tasks/<id>`: Удаление задачи.  


## Документация Postman
Для удобства использования API вы можете импортировать коллекцию Postman ([flask_todo_api.postman_collection.json](flask_todo_api.postman_collection.json)), которая содержит примеры запросов к каждому эндпоинту.

Ссылка на коллекцию Postman:
https://www.postman.com/yaninatv/workspace/flask-todo-api/collection/32891089-5a1a5322-761d-4020-92b8-a485c980a5a2?action=share&creator=32891089

## Доска Miro
Доска Miro используется для отслеживания прогресса проекта и планирования дальнейших шагов.

Ссылка на доску Miro:
https://miro.com/app/board/uXjVKDLOMOo=/?share_link_id=314915912752