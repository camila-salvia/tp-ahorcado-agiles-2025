from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webriver.common.by import By

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
import time
import os

@given('abro el juego del ahorcado')
def step_open_game(context):
    path = os.path.abspath("ui/ahorcado_ui.html")
    context.driver = webdriver.Chrome()
    context.driver.get("file://" + path)

@when('ingreso las letras {letras}')
def step_input_letters(context, letras):
    letras = [l.strip().replace('"', '').replace(',', '') for l in letras.split()]
    for letra in letras:
        input_box = context.driver.find_element(By.ID, "letra")
        button = context.driver.find_element(By.ID, "btn-probar")
        input_box.clear()
        input_box.send_keys(letra)
        button.click()
        time.sleep(0.3)  # breve espera para actualizar DOM

@then('veo el mensaje "{mensaje}"')
def step_see_message(context, mensaje):
    result = context.driver.find_element(By.ID, "mensaje").text
    assert mensaje in result
    context.driver.quit()
