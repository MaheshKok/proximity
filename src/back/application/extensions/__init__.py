import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from application import constants
from application.extensions import database

db = SQLAlchemy()
migrations_path = os.path.join(constants.PROJECT_ROOT_PATH, "src", "back", "migrations")
migrate = Migrate(directory=migrations_path)


def register_extensions(app):
    database.register_database(app)
