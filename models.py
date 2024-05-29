#importar parcialmente parte de sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean
import db #doy acceso al fichero al fichero db

class Tarea(db.Base): #db.Base es el nombre de la variable utilizado en la vinculación dentro de db.py
    __tablename__ = "tarea" #el nombre de la tabla para el ORM. Por convenio se escriben los nombres de las bases de datos en minúscula
    #le decimos que columnas queremos que tenga nuestra tabla.Igual no queremos que todos los atributos aparezcan en la tabla.
    #Para que la tabla tenga la PK (primary key) y sea autoincremental
    __table_args__ = {'sqlite_autoincrement': True}
    #nombre, es una columna, de tipo integer y es una primary key
    id_tarea = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False) # El 200 es para que tengo un máximo de caracteres. nullable para que no pueda estar vacío
    finalizada = Column(Boolean)

    #Definimos los atributos que no necesariamente tienen que coincidir con las columnas de la tabla
    def __init__(self, contenido, finalizada):
        self.contenido = contenido
        self.finalizada = finalizada

    #Str de la clase tarea
    def __str__(self):
        return "Tarea: {}, {}, {}".format(self.id_tarea, self.contenido, self.finalizada)