# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

# import Flask 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager 
from flask_mail import Mail
from flask_migrate import Migrate, upgrade

db = SQLAlchemy()
mail = Mail()
migrate = Migrate()

from .config import Config

# Inject Flask magic
app = Flask(__name__)

# load Configuration
app.config.from_object( Config ) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
db.init_app(app)
mail.init_app(app)
migrate.init_app(app, db)
from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()

# Import routing to render the pages
from app import views

