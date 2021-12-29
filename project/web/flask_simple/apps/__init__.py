import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import (Mail, Message)
from flask_sqlalchemy import SQLAlchemy

from . import email_config

bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
db = SQLAlchemy()



def init_config(app):
    # mail headers
    app.config['MAIL_SERVER'] = email_config.MAIL_SERVER
    app.config['MAIL_PORT'] = email_config.MAIL_PORT
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = email_config.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = email_config.MAIL_PASSWD
    # mail message
    app.config['MAIL_SUBJECT'] = "[bamboo web]"
    app.config['MAIL_SENDER'] = email_config.MAIL_USERNAME
    app.config['MAIL_ADMIN'] = email_config.MAIL_ADMIN

    # sqlite db
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SECRET_KEY'] = "I am a secret key"


def api_register_blueprints(app):
    from .apis import bp
    app.register_blueprint(bp, url_prefix='/api/v1')


def create_app():
    try:
        app = Flask(__name__)
        init_config(app)

        bootstrap.init_app(app)
        moment.init_app(app)
        mail.init_app(app)
        db.init_app(app)
        api_register_blueprints(app)
    except Exception as msg:
        print(msg)

    return app
