import subprocess
import time
import os

server_process = None

def before_all(context):
    global server_process

    print("Iniciando servidor Flask en modo TEST...")

    # Forzar modo test para que /palabra devuelva siempre "pera"
    os.environ["TEST_MODE"] = "true"

    # Levantar el servidor Flask
    server_process = subprocess.Popen(
        ["python", "server.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Esperar a que arranque Flask
    time.sleep(1.5)

def after_all(context):
    global server_process

    print("Apagando servidor Flask...")

    if server_process:
        server_process.terminate()
        server_process.wait()
