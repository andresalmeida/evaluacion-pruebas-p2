from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app import routes  # Importar las rutas después de inicializar la app y la base de datos
    app.register_blueprint(routes.bp)

    return app
