from flask import Flask
app = Flask(__name__)
from WebApp.route.register.alumnos import registro
app.register_blueprint(registro)