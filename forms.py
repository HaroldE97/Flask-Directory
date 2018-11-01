from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField
from wtforms.fields.html5 import EmailField, TelField
from wtforms.validators import DataRequired, length, Email


errors = {
    'name_len': 'Ingrese un nombre de contacto entre 4 y 45 carácteres',
    'email': 'Ingrese un correo electronico valido'
}


class Person(FlaskForm):
    id = HiddenField('')
    name = StringField('Nombre Completo', [DataRequired(), length(min=4, max=45, message=errors['name_len'])])
    email = EmailField('Correo electronico', [DataRequired(), Email(errors['email'])])
    direccion = TextAreaField('Domicilio', [DataRequired()])
    telefono = TelField('Número teléfonico', [DataRequired(), length(min=8)])
    submit = SubmitField('Enviar')
