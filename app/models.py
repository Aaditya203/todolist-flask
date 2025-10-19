from . import db
from flask_login import UserMixin



class Users(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(250),nullable=False)
    email=db.Column(db.String(255),unique=True,nullable=False)
    password = db.Column(db.Text,nullable=False)
    tasks = db.relationship('Task',backref='user',lazy=True)
class Task(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(150),nullable=False)
    status = db.Column(db.String(20),default="Pending")
    user_id = db.Column(db.Integer(),db.ForeignKey('users.id'),nullable=False)


