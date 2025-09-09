palabra_secreta = "pera"
def letra_pertenece_palabra():
    letra = input("Ingrese una letra: ")
    if not letra.isalpha():
        print("Solo se permiten letras") # por el test 4
        return False
    letra = letra.lower() # por el test 3
    if letra in palabra_secreta:
        print("¡Correcto! La letra pertenece a la palabra.") # por el test 1
        return True
    else:
        print("Incorrecto. La letra no pertenece a la palabra.") # por el test 2
        return False