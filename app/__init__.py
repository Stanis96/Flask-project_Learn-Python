from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from flask_login import LoginManager, current_user, login_required

from .users.models import User
from .config import Config
from .main import blueprint as main_blueprint
from .users.views import blueprint as user_blueprint
from .admins.views import blueprint as admin_blueprint
from .headphones.views import blueprint as headphone_blueprint
from .db import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(headphone_blueprint)

    login_manager = LoginManager(app)
    login_manager.login_view = 'user.login_page'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    @app.route('/')
    @app.route('/index')
    @login_required
    def index_page():
        return redirect(url_for('main.index_page'))

    return app
