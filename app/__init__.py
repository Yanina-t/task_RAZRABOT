from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app():
    """Создает экземпляр приложения Flask и инициализирует его."""
    app = Flask(__name__)

    # Конфигурация приложения
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from app import routes
    routes.init_app(app)

    return app
