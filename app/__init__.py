# app/__init.py__
# pylint: disable=missing-docstring

from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)

    from .apis.tweets import api as tweets
    api = Api()
    api.add_namespace(tweets)
    api.init_app(app)

    app.config['ERROR_404_HELP'] = False
    return app
