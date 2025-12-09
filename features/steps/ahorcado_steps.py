import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

@given('abro el juego del ahorcado')
def step_open_game(context):
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("http://127.0.0.1:5000/")

@when('ingreso las letras "{letras}"')
def step_input_letters(context, letras):
    try:
        wait = WebDriverWait(context.driver, 5)

        input_box = wait.until(EC.presence_of_element_located((By.ID, "letra")))
        button = wait.until(EC.presence_of_element_located((By.ID, "btn-probar")))

        letras_limpias = letras.strip().replace(" ", "").replace(",", "")
        for letra in letras_limpias:
            input_box.clear()
            input_box.send_keys(letra)
            button.click()

            time.sleep(0.) 

    except Exception as e:
        print(f"Error al buscar elementos 'letra' o 'btn-probar': {e}")
        raise e

@then('veo el mensaje "{mensaje}"')
def step_see_message(context, mensaje):
    try:
        WebDriverWait(context.driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "mensaje"), mensaje)
        )
        assert True
    except TimeoutException:
        # Si entra acá es SOLO porque se acabó el tiempo (el mensaje no apareció)
        texto_actual = context.driver.find_element(By.ID, "mensaje").text
        print(f"Error: se esperaba '{mensaje}' pero se encontró '{texto_actual}'")
        assert False
    finally:
        context.driver.quit()
