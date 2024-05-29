from flask import Flask, render_template, request, redirect, url_for
from models import Tarea  # Importamos mi modelo
import db
# 80 --> http
# 8080 --> https
# Esta línea de abajo es mejora poner arriba
app = Flask(__name__)  # En app se encuentra nuestro servidor web de Flask

@app.route("/") # Ruta de origen
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    for i in todas_las_tareas:
        print(i)
    return render_template("index.html", lista_de_tareas=todas_las_tareas)  # no hay que decirle que está en la carpeta templates porque son las normas de flask y el asume que estará ahí.

# Coger información del formulario
@app.route("/crear-tarea", methods=["POST"])
def crear():
    tarea = Tarea(contenido=request.form["contenidoTarea"], finalizada=False)  # Desde python cogemos la info del input con request
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home"))  # Le decimos que quiero ir a la función home para volver a index cuándo metamos una tarea nueva

@app.route("/eliminar-tarea/<id>")  # los símbolos de <> indican que es una variable
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/tarea-finalizada/<id>")  # los símbolos de <> indican que es una variable
def finalizada(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()
    tarea.finalizada = not(tarea.finalizada) #Le decimos así que sea el contrario de lo que actualmente indique la variable booleana
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/editar-tarea/<id>", methods=["POST", "GET"])
def editar(id):
    if request.method == "POST":
        tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()
        tarea.contenido = request.form.get("contenidoTareaEditar", tarea.contenido)
        db.session.commit()
        return redirect(url_for("home"))
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()
    return render_template("actualizar.html", tarea=tarea)

if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine) #instrucción para crear la base de datos
    app.run(debug=True) #Arrancar el servidor