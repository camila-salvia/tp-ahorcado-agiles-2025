import pytest
from ahorcado import (
   entrada_valida,
   verificar_disponibilidad,
   restar_vida,
   adivinar_palabra,
   arriesgar,
   procesar_letra
)

palabra_secreta = "pera"

#FUNCION: entrada_valida
# test: ingreso de caracter inválido
def test_validar_caracter_invalido():
	assert entrada_valida("#") is False
   
# test: ingreso caracter válido
def test_validar_caracter_valido():
  assert entrada_valida("a") is True

#-------------------------------
# FUNCIÓN: verificar_disponibilidad
# test: ingresa una letra que se encuentra disponible
def test_ingresa_letra_aun_no_dicha():
  usadas = {"c", "a"} #letras ya usadas
  assert verificar_disponibilidad("p", usadas) is True #p no está en usadas

# test: ingresa una letra que ya fue dicha
def test_ingresa_letra_dicha():
  usadas = {"c", "a"} #letras ya usadas
  assert verificar_disponibilidad("c", usadas) is False #c está en usadas


#-------------------------------
# FUNCIÓN: arriesgar
# test: arriesga la palabra y gana el juego
def test_arriesga_palabra_gana():
   assert arriesgar("pera", palabra_secreta) is True

# test: arriesga la palabra, y pierde el juego
def test_arriesga_palabra_pierde():
   assert arriesgar("manzana", palabra_secreta) is False

# test: la palabra vale, aunque sea mayúsculas
def test_validar_palabra_mayusc():
    assert arriesgar("PERA", palabra_secreta) is True


#-------------------------------
# FUNCIÓN: adivinar_palabra
# test: gana por adivinar todas las letras
def test_adivina_palabra():
  usadas = {"p", "e","r","a"} #letras ya usadas
  assert adivinar_palabra(usadas, palabra_secreta) is True

#-------------------------------
# FUNCIÓN: restar_vida
# test: quitar vida por letra incorrecta
def test_restar_vida_por_letra_incorrecta():
  assert restar_vida(6) == 5

# test: derrota si llega a 0 vidas
def test_derrota_llega_a_cero_vidas():
  assert restar_vida(1) == 0
  assert restar_vida(0) == 0 #no puede ser negativo

#-------------------------------
#FUNCIÓN: procesar_letra
# test: valida letra y acierta
def test_validar_letra_acierto():
  vidas, usadas, acierto = procesar_letra("p", palabra_secreta, 6, [])
  assert vidas == 6
  assert "p" in usadas
  assert acierto is True

#test: valida letra y falla
def test_validar_letra_falla():
  vidas, usadas, acierto = procesar_letra("z", palabra_secreta, 6, [])
  assert vidas == 5
  assert "z" in usadas
  assert acierto is False

# test: la letra vale, así sea mayúscula o minúscula
def test_validar_letra_mayusc_minusc():
   vidas, usadas, acierto = procesar_letra("A", palabra_secreta, 4, ["p", "e"])
   assert vidas == 4
   assert "a" in usadas
   assert acierto is True
   