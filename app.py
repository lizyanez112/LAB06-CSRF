from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Clave secreta requerida por Flask-WTF
app.config["SECRET_KEY"] = "MiClaveSuperSegura2026"

# Activar protección CSRF
csrf = CSRFProtect(app)


@app.route("/")
def index():
    return render_template("formulario.html")


@app.route("/formulario", methods=["GET", "POST"])
def formulario():

    resultado = ""

    if request.method == "POST":

        nombre = request.form.get("nombre")
        mensaje = request.form.get("mensaje")

        resultado = f"Nombre: {nombre} | Mensaje: {mensaje}"

    return render_template("formulario.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)