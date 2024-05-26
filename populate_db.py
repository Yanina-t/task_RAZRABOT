from app import db
from app.models import Task
from app import create_app

# Создаем экземпляр приложения Flask
app = create_app()

# Создаем контекст приложения
app_ctx = app.app_context()
app_ctx.push()

# Список задач для заполнения базы данных
tasks = [
    {"title": "Помыть посуду", "description": "Вымыть тарелки, кастрюли и столовые приборы."},
    {"title": "Погулять с собакой", "description": "Прогулять собаку в парке."},
    {"title": "Сделать покупки", "description": "Купить продукты в магазине: молоко, яйца, овощи."},
    # Добавьте еще задачи по вашему усмотрению
]

try:
    # Добавление задач в базу данных
    for task_data in tasks:
        task = Task(title=task_data["title"], description=task_data["description"])
        db.session.add(task)

    # Сохранение изменений в базе данных
    db.session.commit()

    print("Задачи успешно добавлены в базу данных!")
except Exception as e:
    print("Произошла ошибка при добавлении задач:", e)
finally:
    # Освобождаем контекст приложения
    app_ctx.pop()
