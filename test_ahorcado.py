from ahorcado import validar_letra

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