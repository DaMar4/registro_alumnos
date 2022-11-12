from flask import Blueprint,render_template,redirect,url_for
from WebApp.route.forms.register import frmRegistro
from WebApp.model.database import dbAlumnos
registro = Blueprint("registro",__name__)
@registro.route("/")
@registro.route("/home")
def start():
    return render_template("index.html")
@registro.route("/add",methods=["GET","POST"])
def nuevo_registro():
    form = frmRegistro()
    return render_template("registro.html",form=form)
@registro.route("/added",methods=["GET","POST"])
def added():
    return redirect(url_for("registro.start"))