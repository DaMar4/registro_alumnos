from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
app = Flask(__name__)
db = SQLAlchemy(app)
#app.config.from_object("configuration.DevelopmentConfig")
app.config["SECRET_KEY"]= secrets.token_urlsafe(64)
app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://postgres:2909@127.0.0.1:5432/dbAlumnos'
app.config["DEBUG"]=True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from WebApp.route.register.alumnos import registro
app.register_blueprint(registro)
db.create_all()