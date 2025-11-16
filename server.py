from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import random
import os
from palabras import palabras_posibles
from ahorcado import gestionar_entrada, generar_palabra_mostrada, obtener_mensaje_final

TEST_MODE = os.environ.get("TEST_MODE", "false").lower() == "true"
PALABRA_FIJA_TEST = "pera"

app = Flask(__name__, static_folder="ui", static_url_path="")
CORS(app)

@app.route("/palabra")
def palabra():
    if TEST_MODE:
        return jsonify({"palabra": PALABRA_FIJA_TEST})
    return jsonify({"palabra": random.choice(palabras_posibles)})


@app.route("/gestionar", methods=["POST"])
def gestionar():
    data = request.get_json() or {}
    entrada = data.get("entrada")
    intento_arriesgar = data.get("intento_arriesgar")
    palabra_secreta = data.get("palabra_secreta")
    vidas = data.get("vidas", 6)
    usadas = data.get("usadas", [])
    vidas, usadas, mensaje, juego_terminado = gestionar_entrada(
        entrada, intento_arriesgar, palabra_secreta, vidas, usadas
    )
    palabra_mostrada = generar_palabra_mostrada(palabra_secreta, usadas)
    final_message = obtener_mensaje_final(usadas, palabra_secreta) if juego_terminado else ""
    return jsonify({
        "vidas": vidas,
        "usadas": usadas,
        "mensaje": mensaje,
        "juego_terminado": juego_terminado,
        "palabra_mostrada": palabra_mostrada,
        "final_message": final_message
    })

@app.route("/")
def index():
    return send_from_directory("ui", "ahorcado_ui.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory("ui", filename)

if __name__ == "__main__":
  app.run(host='127.0.0.1', port=5000, debug=True)