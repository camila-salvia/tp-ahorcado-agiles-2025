from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

@given('abro el juego del ahorcado')
def step_open_game(context):
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("http://127.0.0.1:5000/")

@when('ingreso las letras {letras}')
def step_input_letters(context, letras):
    letras = [l.strip().replace('"', '').replace(',', '') for l in letras.split()]
    for letra in letras:
        input_box = context.driver.find_element(By.ID, "letra")
        button = context.driver.find_element(By.ID, "btn-probar")
        input_box.clear()
        input_box.send_keys(letra)
        button.click()
        time.sleep(0.3)

@then('veo el mensaje "{mensaje}"')
def step_see_message(context, mensaje):
    try:
        WebDriverWait(context.driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "mensaje"), mensaje)
        )
        assert True
    except:
        texto_actual = context.driver.find_element(By.ID, "mensaje").text
        print(f"Error: se esperaba '{mensaje}' pero se encontró '{texto_actual}'")
        assert False
    finally:
        context.driver.quit()
