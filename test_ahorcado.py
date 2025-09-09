from ahorcado import validar_letra

# test 1: valida letra y acierta
def test_validar_letra_acierto():
  assert letra_pertenece_palabra("a", palabra_secreta) is True


#test 2: valida letra y falla
def test_validar_letra_falla():
  assert letra_pertenece_palabra("z", palabra_secreta)