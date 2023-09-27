from flask_login import UserMixin
from api import db
from datetime import datetime
# from sqlalchemy.sql import func

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    # date_created = db.Column(db.DateTime(timezone=True),  dafault=func.now())
    name = db.Column(db.String(length=150), nullable=False)
    email = db.Column(db.String(length=150),unique=True,nullable=False)
    password = db.Column(db.String(length=100), nullable=False)
