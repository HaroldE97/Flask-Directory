from flask import Flask, render_template as render, request, redirect, url_for, flash, session
from flask_caching import Cache
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config
from models import db, Contact, User
from forms import LoginForm, RegisterForm, ContactForm


app = Flask(__name__)
app.config.from_object(Config)

cache = Cache(config={'CACHE_TYPE': 'null'})


@app.before_request
def before_request():
    pass
    if 'username' not in session and request.endpoint in ['index', 'new']:
        return redirect(url_for('login'))
    elif 'username'in session and request.endpoint in ['login', 'register']:
        return redirect(url_for('index'))


@app.route('/')
def index():
    username = session.get('username') or 'Harold'
    contacts_list = Contact.query.filter_by(user_id=username).all()
    return render('index.html', user=username, contacts=contacts_list)


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

    return render('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        user = User(
            username=form.username.data,
            name=form.name.data,
            password=form.password.data
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render('register.html', form=form, errors=form.errors())


@app.route('/new', methods=['GET', 'POST'])
def new():
    form = ContactForm(request.form)
    if request.method == 'POST':
        contact = Contact(
            name=form.name.data,
            email=form.email.data,
            telefono=form.telefono.data,
            domicilio=form.direccion.data,
            user_id=session['username']
        )

        db.session.add(contact)
        db.session.commit()

        return redirect(url_for('index'))

    return render('new.html', form=form)


if __name__ == '__main__':
    cache.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    manager = Manager(app)

    manager.add_command('db', MigrateCommand)

    with app.app_context():
        db.create_all()
    app.run(port=8000)
    #manager.run()
