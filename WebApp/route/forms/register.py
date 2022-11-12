from wtforms import Form,StringField
from wtforms.validators import DataRequired
class frmRegistro(Form):
    nombre = StringField("Nombre(s) del alumno:",validators=[DataRequired()])
    apellido_paterno = StringField("Apellido paterno:",validators=[DataRequired()])
    apellido_materno= StringField("Apellido Materno:",validators=[DataRequired()])
    correo = StringField("Correo institucional:",validators=[DataRequired()])
    telefono = StringField("Telefono de contacto:",validators=[DataRequired()])
    matricula = StringField("Numero de control:",validators=[DataRequired()])
    carrera = StringField("Carrera:",validators=[DataRequired()])
    modalidad = StringField("Modalidad:",validators=[DataRequired()])