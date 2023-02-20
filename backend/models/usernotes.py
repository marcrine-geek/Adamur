from datetime import datetime

from sqlalchemy.orm import relationship

from db import db

from .helpers import BaseClass


class UsernotesModel(BaseClass, db.Model):
    __tablename__ = "user_notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, notes):
        now = datetime.now()
        self.timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        self.notes = notes
        
