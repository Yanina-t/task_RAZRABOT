from flask import Blueprint, request, jsonify
from app import db
from app.models import Task
from app.schemas import TaskSchema

bp = Blueprint('routes', __name__)


def init_app(app):
    """Инициализирует маршруты."""
    app.register_blueprint(bp)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


@bp.route('/tasks', methods=['POST'])
def create_task():
    """Создает новую задачу."""
    title = request.json['title']
    description = request.json.get('description', '')

    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task), 201


@bp.route('/tasks', methods=['GET'])
def get_tasks():
    """Возвращает список всех задач."""
    tasks = Task.query.all()
    return tasks_schema.jsonify(tasks), 200


@bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    """Возвращает задачу по ее идентификатору 'id'."""
    task = db.session.get(Task, id)
    if task:
        return task_schema.jsonify(task), 200
    else:
        return jsonify({"message": "Задача не найдена, проверьте 'id'"}), 404


@bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """Обновляет задачу по ее идентификатору 'id'."""
    task = db.session.get(Task, id)
    if task:
        title = request.json.get('title', task.title)
        description = request.json.get('description', task.description)

        task.title = title
        task.description = description

        db.session.commit()

        return task_schema.jsonify(task), 200
    else:
        return jsonify({"message": "Задача не найдена, проверьте 'id'"}), 404


@bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """Удаляет задачу по ее идентификатору 'id'."""
    task = db.session.get(Task, id)
    if task:
        task_title = task.title
        db.session.delete(task)
        db.session.commit()
        return f"Задача '{task_title}' успешно удалена", 200
    else:
        return "Задача не найдена, проверьте 'id'", 404
