import pytest
from app import create_app, db
from app.models import Task


@pytest.fixture
def app():
    """
    Фикстура для создания приложения Flask.
    Конфигурирует приложение для тестирования и использует SQLite в памяти для базы данных.
    Создает все таблицы перед тестами и удаляет их после завершения тестов.
    """
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Используем SQLite в памяти для тестов
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    """
    Фикстура для создания тестового клиента.
    Возвращает тестовый клиент для выполнения запросов к приложению Flask.
    """
    return app.test_client()


@pytest.fixture
def init_database(app):
    """
    Фикстура для инициализации базы данных.
    Создает все таблицы перед тестами и удаляет их после завершения тестов.
    """
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()


def test_create_task(client, init_database):
    """
    Тест для проверки создания задачи.
    Выполняет POST-запрос для создания новой задачи и проверяет, что задача успешно добавлена в базу данных.
    """
    response = client.post('/tasks', json={"title": "Test Task"})
    assert response.status_code == 201
    assert Task.query.count() == 1
    assert Task.query.first().title == "Test Task"


def test_get_tasks(client, init_database):
    """
    Тест для проверки получения списка задач.
    Создает задачу, выполняет GET-запрос для получения всех задач и проверяет, что задача присутствует в ответе.
    """
    task = Task(title="Task 1")  # Создаем объект Task
    db.session.add(task)         # Добавляем объект в сессию
    db.session.commit()          # Сохраняем изменения в базе данных

    response = client.get('/tasks')  # Выполняем запрос на получение всех задач

    assert response.status_code == 200  # Проверяем код ответа
    assert b'Task 1' in response.data   # Проверяем, что задача Task 1 присутствует в ответе


def test_get_task_by_id(client, init_database):
    """
    Тест для проверки получения задачи по ID.
    """
    task = Task(title="Task 1")
    db.session.add(task)
    db.session.commit()

    response = client.get(f'/tasks/{task.id}')
    assert response.status_code == 200
    assert b'Task 1' in response.data


def test_update_task(client, init_database):
    """
    Тест для проверки редактирования задачи.
    """
    task = Task(title="Task 1")
    db.session.add(task)
    db.session.commit()

    response = client.put(f'/tasks/{task.id}', json={"title": "Updated Task", "description": "Updated description"})
    assert response.status_code == 200

    updated_task = Task.query.get(task.id)
    assert updated_task.title == "Updated Task"
    assert updated_task.description == "Updated description"


def test_delete_task(client, init_database):
    """
    Тест для проверки удаления задачи.
    Создает задачу, выполняет DELETE-запрос для ее удаления и проверяет, что задача успешно удалена из базы данных.
    """
    task = Task(title="Task 1")  # Создаем объект Task
    db.session.add(task)         # Добавляем объект в сессию
    db.session.commit()          # Сохраняем изменения в базе данных

    response = client.delete(f'/tasks/{task.id}')
    assert response.status_code == 200
    assert Task.query.count() == 0
