import pytest
from ahorcado import palabra_secreta, letra_pertenece_palabra, verificar_disponibilidad, arriesgar, adivinar_palabra, restar_vida, vidas, usadas


#FUNCIÓN: letra_pertenece_palabra

# test 1: valida letra y acierta
def test_validar_letra_acierto():
  assert letra_pertenece_palabra("a", palabra_secreta) is True

#test 2: valida letra y falla
def test_validar_letra_falla():
  assert letra_pertenece_palabra("z", palabra_secreta) is False

# test 3: la letra vale, así sea mayúscula o minúscula
def test_validar_letra_mayusc_minusc():
    usadas.clear()
    assert letra_pertenece_palabra("a", palabra_secreta) is True
    usadas.clear()
    assert letra_pertenece_palabra("A", palabra_secreta) is True

# test 4: ingreso de caracter inválido
def test_validar_caracter_invalido():
	assert letra_pertenece_palabra("#", palabra_secreta) is False


# FUNCIÓN: verificar_disponibilidad

# test 5: ingresa una letra que se encuentra disponible
def test_ingresa_letra_aun_no_dicha():
  usadas = {"c", "a"} #letras ya usadas
  assert verificar_disponibilidad("p", usadas) is True #p no está en usadas

# test 6: ingresa una letra que ya fue dicha
def test_ingresa_letra_dicha():
  usadas = {"c", "a"} #letras ya usadas
  assert verificar_disponibilidad("c", usadas) is False #c está en usadas

#-------------------------------
# FUNCIÓN: arriesgar
# test 7: arriesga la palabra y gana el juego
def test_arriesga_palabra_gana():
   assert arriesgar("pera", palabra_secreta) is True

# test 8: arriesga la palabra, y pierde el juego
def test_arriesga_palabra_pierde():
   assert arriesgar("manzana", palabra_secreta) is False

# test 10: la palabra vale, sin importar mayúsculas o minúsculas
def test_validar_palabra_mayusc_minusc():
    assert arriesgar("pera", palabra_secreta) is True
    assert arriesgar("PERA", palabra_secreta) is True

#-------------------------------
# FUNCIÓN: adivinar_palabra
# test 9: gana por adivinar todas las letras
def test_adivina_palabra():
  usadas = {"p", "e","r","a"} #letras ya usadas
  assert adivinar_palabra(usadas, palabra_secreta) is True

#-------------------------------
# FUNCIÓN: restar_vida
# test 11: quitar vida por letra incorrecta
def test_restar_vida_por_letra_incorrecta():
  assert restar_vida(6) == 5

# test 12: derrota si llega a 0 vidas
def test_derrota_llega_a_cero_vidas():
  assert restar_vida(1) == 0