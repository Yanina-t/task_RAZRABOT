from app import ma
from app.models import Task


class TaskSchema(ma.SQLAlchemyAutoSchema):
    """Схема для сериализации и десериализации задач."""
    class Meta:
        model = Task
