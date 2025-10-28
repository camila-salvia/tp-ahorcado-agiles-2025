from flask import Flask, jsonify, send_from_directory
import random
from palabras import palabras_posibles
import os

app = Flask(__name__)


@app.route("/palabra")
def palabra():
    return jsonify({"palabra": random.choice(palabras_posibles)})

# Sirve la página y archivos estáticos desde la carpeta ui/
@app.route("/")
def index():
    return send_from_directory("ui", "ahorcado_ui.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory("ui", filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)