from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField, PasswordField
from wtforms.fields.html5 import EmailField, TelField
from wtforms.validators import DataRequired, Email, ValidationError
#from length_validator_field import Length


errors = {
    'name_len': 'Ingrese un nombre de contacto entre 4 y 45 carácteres',
    'email': 'Ingrese un correo electronico valido',
    'username_len': 'Nombre de usuario ingresado demasiado corto',
    'password_len': 'Contraseña ingresada demasiado corta'
}


class Length(object):
    def __init__(self, min=-1, max=-1, message=None):
        self.min = min
        self.max = max
        if not message:
            message = "El campo debe de tener entre %i y %i caracteres de largo" %(min, max)
        self.message = message

    def __call__(self, form, field):
        l = field.data and len(field.data) or 0
        if l < self.min or self.max != -1 and l > self.max:
            raise ValidationError(self.message)


length = Length


class PersonForm(FlaskForm):
    id = HiddenField('')
    name = StringField('Nombre Completo', [DataRequired(), length(min=4, max=45, message=errors['name_len'])])
    email = EmailField('Correo electronico', [DataRequired(), Email(errors['email'])])
    direccion = TextAreaField('Domicilio', [DataRequired()])
    telefono = TelField('Número teléfonico', [DataRequired(), length(min=8)])
    submit = SubmitField('Enviar')


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', [DataRequired()])
    password = PasswordField('Contraseña', [DataRequired()])
    submit = SubmitField('Ingresar')


class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario', [DataRequired(), length(min=6, max=25, message=errors['username_len'])])
    name = StringField('Nombre completo', [DataRequired()])
    password = PasswordField('Contraseña', [DataRequired(), length(min=6, max=25, message=errors['password_len'])])
    submit = SubmitField('Registro')

    def errors(self):
        return list(self.username.errors + self.password.errors)
