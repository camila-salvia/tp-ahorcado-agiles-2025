import pytest
from ahorcado import palabra_secreta, letra_pertenece_palabra, ingresa_una_letra, adivinar


#FUNCIÓN: letra_pertenece_palabra

# test 1: valida letra y acierta
def test_validar_letra_acierto():
  assert letra_pertenece_palabra("a", palabra_secreta) is True

#test 2: valida letra y falla
def test_validar_letra_falla():
  assert letra_pertenece_palabra("z", palabra_secreta) is False

# test 3: la letra vale, así sea mayúscula o minúscula
def test_validar_mayusc_minusc():
    assert letra_pertenece_palabra("a", palabra_secreta) is True
    assert letra_pertenece_palabra("A", palabra_secreta) is True

# test 4: ingreso de caracter inválido
def test_validar_caracter_invalido():
	assert letra_pertenece_palabra("#", palabra_secreta) is False


# FUNCIÓN: ingresa_una_letra

# test 5: ingresa una letra que se encuentra disponible
def test_ingresa_letra_aun_no_dicha():
  usadas = {"c", "a"} #letras ya usadas
  assert ingresa_una_letra("p", usadas) is True #p no está en usadas

# test 6: ingresa una letra que ya fue dicha
def test_ingresa_letra_dicha():
  usadas = {"c", "a"} #letras ya usadas
  assert ingresa_una_letra("c", usadas) is False #c está en usadas


# FUNCIÓN: adivina_palabra

# test 7: arriesga la palabra y gana el juego
def test_arriesga_palabra_gana():
   assert arriesgar("pera", palabra_secreta) is True

# test 8: arriesga la palabra, y pierde el juego
def test_arriesga_palabra_pierde():
   assert arriesgar("manzana", palabra_secreta) is False

# test 9: gana por adivinar todas las letras
def test_adivina_palabra():
  usadas = {"e","r","a"} #letras ya usadas
  assert adivinar_palabra(palabra_secreta, usadas) is True