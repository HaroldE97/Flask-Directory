from flask_sqlalchemy import SQLAlchemy


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
