import pytest
from ahorcado import (
   entrada_valida,
   verificar_disponibilidad,
   restar_vida,
   adivinar_palabra,
   arriesgar,
   procesar_letra,
   generar_palabra_mostrada,
   obtener_mensaje_final,
   gestionar_entrada
)

palabra_secreta = "pera"
#-------------------------------
#FUNCION: entrada_valida

# test 1: ingreso de caracter inválido
def test_validar_caracter_invalido():
	assert entrada_valida("#") is False

# test 2: ingreso de más de un caracter
def test_validar_mas_de_un_caracter():
    assert entrada_valida("ab") is False

# test 3: ingreso de caracter vacío
def test_validar_caracter_vacio():
    assert entrada_valida("") is False
   
# test 4: ingreso caracter válido minúscula
def test_validar_caracter_valido_minuscula():
  assert entrada_valida("a") is True

# test 5: ingreso de caracter válido mayúscula
def test_validar_caracter_valido_mayuscula():
    assert entrada_valida("Z") is True


#-------------------------------
# FUNCIÓN: verificar_disponibilidad

# test 6: ingresa una letra que se encuentra disponible minuscula
def test_ingresa_letra_aun_no_dicha():
  usadas = ["c", "a"] 
  assert verificar_disponibilidad("p", usadas) is True 

# test 7: ingresa una letra que se encuentra disponible mayúscula
def test_ingresa_letra_aun_no_dicha_mayuscula():
  usadas = ["c", "a"] 
  assert verificar_disponibilidad("P", usadas) is True

# test 8: ingresa una letra que no se encuentra disponible minuscula
def test_ingresa_letra_dicha_minuscula():
  usadas = ["c", "a"] 
  assert verificar_disponibilidad("c", usadas) is False 

# test 9: ingresa una letra que no se encuentra disponible mayúscula
def test_ingresa_letra_dicha_mayuscula():
  usadas = ["c", "a"] 
  assert verificar_disponibilidad("C", usadas) is False


#-------------------------------
# FUNCIÓN: restar_vida

# test 10: quitar vida por letra incorrecta
def test_restar_vida_por_letra_incorrecta():
  assert restar_vida(6) == 5

# test 11: derrota si llega a 0 vidas
def test_derrota_llega_a_cero_vidas():
  assert restar_vida(1) == 0
  assert restar_vida(0) == 0 #no puede ser negativo

# test 12: restar vida en negativo
def test_restar_vida_negativo():
    assert restar_vida(-3) == -3  # no debería modificar valores negativos


#-------------------------------
# FUNCIÓN: adivinar_palabra

# test 13: gana por adivinar todas las letras
def test_adivina_palabra():
  usadas = ["p", "e","r","a"] #letras ya usadas
  assert adivinar_palabra(usadas, palabra_secreta) is True

# test 14: no gana si faltan letras por adivinar
def test_no_adivina_palabra_aun():
    usadas = ["p", "e"]
    assert adivinar_palabra(usadas, "pera") is False

#-------------------------------
# FUNCIÓN: arriesgar

# test 15: arriesga la palabra y gana el juego
def test_arriesga_palabra_gana():
   assert arriesgar("pera", palabra_secreta) is True

# test 16: arriesga la palabra, y pierde el juego
def test_arriesga_palabra_pierde():
   assert arriesgar("manzana", palabra_secreta) is False

# test 17: la palabra vale, aunque sea mayúsculas
def test_validar_palabra_mayusc():
    assert arriesgar("PERA", palabra_secreta) is True

# test 18: arriesga palabra vacía
def test_arriesgar_palabra_vacia():
   assert arriesgar("", palabra_secreta) is False


#-------------------------------
#FUNCIÓN: procesar_letra

# test 19: valida letra y acierta
def test_procesar_letra_acierto():
  vidas, usadas, acierto = procesar_letra("p", palabra_secreta, 6, [])
  assert vidas == 6
  assert "p" in usadas
  assert acierto is True

#test 20: valida letra y falla
def test_procesar_letra_fallo():
  vidas, usadas, acierto = procesar_letra("z", palabra_secreta, 6, [])
  assert vidas == 5
  assert "z" in usadas
  assert acierto is False

# test 21: la letra vale, así sea mayúscula o minúscula
def test_validar_letra_mayusc_minusc():
   vidas, usadas, acierto = procesar_letra("A", palabra_secreta, 4, ["p", "e"])
   assert vidas == 4
   assert "a" in usadas
   assert acierto is True

# test 22: no restar vida si ya no quedan vidas
def test_procesar_letra_sin_vidas():
    vidas, usadas, acierto = procesar_letra("z", palabra_secreta, 0, [])
    assert vidas == 0  # no puede ser negativo
    assert "z" in usadas
    assert acierto is False


#-------------------------------
# FUNCION: generar_palabra_mostrada
# test : muestra palabra vacia
def test_mostrar_palabra_vacia():
    assert generar_palabra_mostrada("gato", []) == "_ _ _ _ "

# test : muestra palabra con algunas letras adivinadas
def test_mostrar_palabra_parcial():
    assert generar_palabra_mostrada("gato", ["g", "o"]) == "g _ _ o "

# test : muestra palabra completamente adivinada
def test_mostrar_palabra_completa():
    assert generar_palabra_mostrada("gato", ["g", "a", "t", "o"]) == "g a t o "

#-------------------------------
# FUNCION: obtener_mensaje_final

# test : mostrar mensaje de victoria
def test_mensaje_final_victoria():
    usadas = {"p", "e", "r", "a"}
    assert "¡Felicitaciones!" in obtener_mensaje_final(usadas, "pera")

# test : mostrar mensaje de derrota
def test_mensaje_final_derrota():
    usadas = {"p", "e"}
    assert "¡Perdiste!" in obtener_mensaje_final(usadas, "pera")

# -------------------------------
# FUNCION: gestionar_entrada
palabra_secreta_test = "pera"
vidas_iniciales_test = 6
usadas_iniciales_test = ["p"]

# test : acierta una letra
def test_gestionar_letra_valida_acierto():
    vidas, usadas, msg, fin = gestionar_entrada("e", None, palabra_secreta_test, vidas_iniciales_test, usadas_iniciales_test)
    assert vidas == 6
    assert "e" in usadas
    assert "¡Bien hecho!" in msg
    assert fin is False

# test : falla una letra
def test_gestionar_letra_valida_error():
    vidas, usadas, msg, fin = gestionar_entrada("z", None, palabra_secreta_test, vidas_iniciales_test, usadas_iniciales_test)
    assert vidas == 5
    assert "z" in usadas
    assert "¡Incorrecto!" in msg
    assert fin is False

# test : repite una letra
def test_gestionar_letra_repetida():
    vidas, usadas, msg, fin = gestionar_entrada("p", None, palabra_secreta_test, vidas_iniciales_test, usadas_iniciales_test)
    assert vidas == 6
    assert usadas == usadas_iniciales_test # No debe cambiar
    assert "Ya intentaste" in msg
    assert fin is False

# test : entrada inválida
def test_gestionar_letra_invalida():
    vidas, usadas, msg, fin = gestionar_entrada("?#", None, palabra_secreta_test, vidas_iniciales_test, usadas_iniciales_test)
    assert vidas == 6
    assert "inválida" in msg
    assert fin is False

# test : arriesga y gana
def test_gestionar_arriesgar_gana():
    vidas, usadas, msg, fin = gestionar_entrada("arriesgar", "pera", palabra_secreta_test, vidas_iniciales_test, usadas_iniciales_test)
    assert vidas == 6
    assert set(palabra_secreta_test).issubset(usadas) # Verifica que se hayan agregado todas las letras
    assert fin is True

# test : arriesga y pierde
def test_gestionar_arriesgar_pierde():
    vidas, usadas, msg, fin = gestionar_entrada("arriesgar", "gato", palabra_secreta_test, vidas_iniciales_test, usadas_iniciales_test)
    assert vidas == 0 # Pierde todas las vidas
    assert "¡Incorrecto!" in msg
    assert fin is True

# test : acierta la última letra y gana
def test_gestionar_acierto_final_gana():
    usadas_casi = ["p", "e", "r"]
    vidas, usadas, msg, fin = gestionar_entrada("a", None, palabra_secreta_test, 6, usadas_casi)
    assert vidas == 6
    assert "a" in usadas
    assert "¡Bien hecho!" in msg
    assert fin is True # El juego debe terminar porque adivinó la palabra