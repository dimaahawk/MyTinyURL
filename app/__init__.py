from flask import Flask

from app.views import Main
from app.views import Retrieve
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/urls.db'
    app.add_url_rule('/', view_func=Main.as_view('home'))
    app.add_url_rule('/<token>', view_func=Retrieve.as_view('retrieve'))
    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app
