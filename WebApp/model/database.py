from WebApp import db
class dbAlumnos(db.Model):
    __tablename__="datos_alumnos"
    id_alumno = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre_alumno = db.Column(db.String(255))
    apellido_paterno = db.Column(db.String(255))
    apellido_materno = db.Column(db.String(255))
    def __init__(self,nombre,apellido1,apellido2):
        self.nombre_alumno = nombre
        self.apellido_paterno = apellido1
        self.apellido_materno = apellido2
    def __repr__(self):
        return "<dbAlumnos %r>" % self.nombre_alumno