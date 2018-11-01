from flask import Flask
from config import Config
from models import db, Contact


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8000)
