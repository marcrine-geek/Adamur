from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app
from config import DevelopmentConfig
from db import db

app.config.from_object(DevelopmentConfig)

db.init_app(app)

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
