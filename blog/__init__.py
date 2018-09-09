#!/usr/bin/env python

from flask import Flask

from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

from .main import main as main_bp

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)
    app.register_blueprint(main_bp)
    return app

# EOF
