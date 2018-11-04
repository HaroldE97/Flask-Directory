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
    name = column(db.String(50))
    password = column(db.String(66))
    create_date = column(db.Text, default=time.strftime("%d/%m/%Y  %H:%M:%S"))
    persons = db.relationship('Person')

    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = self.__create_password(password)

    def __create_password(self, _password):
        return generate_password_hash(_password)

    def verify_password(self, _password):
        return check_password_hash(self.password, _password)


class Person(model):
    __tablename__ = 'persons'

    id = column(db.Integer, primary_key=True)
    user = column(db.String(30), db.ForeignKey('users.id'))
    name = column(db.String(50))
    email = column(db.String(35))
    direccion = column(db.String(75))
    telefono = column(db.String(25))
