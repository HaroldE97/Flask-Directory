from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import time


db = SQLAlchemy()
model = db.Model
column = db.Column


class Contact(model):
    __tablename__ = 'contacts'

    id = column(db.Integer, primary_key=True)
    name = column(db.String(45))
    email = column(db.String(30))
    telefono = column(db.String(25))
    domicilio = column(db.Text)


class User(model):
    __tablename__: 'users'

    id = column(db.Integer, primary_key=True)
    username = column(db.String(25), unique=True)
    password = column(db.String(66))
    create_date = column(db.Text, default=time.strftime("%d/%m/%Y  %H:%M:%S"))

    def __init__(self, username, password):
        self.username = username
        self.password = self.__create_password(password)

    def __create_password(self, _password):
        return generate_password_hash(_password)

    def verify_password(self, _password):
        return check_password_hash(self.password, _password)
