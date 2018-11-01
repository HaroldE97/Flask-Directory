from flask import Flask, render_template as render, request, redirect, url_for, flash, session
from flask_caching import Cache
from config import Config
from models import db, Contact, User
from forms import LoginForm


app = Flask(__name__)
app.config.from_object(Config)

cache = Cache(config={'CACHE_TYPE': 'null'})


@app.route('/')
def index():
    return render('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña no validos!')
            print("Erro login")

    return render('login.html', form=form)


if __name__ == '__main__':
    cache.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8000)
