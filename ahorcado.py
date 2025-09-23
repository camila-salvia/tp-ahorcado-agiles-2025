def letra_pertenece_palabra(letra: str, palabra_secreta: str) -> bool:
    if not letra.isalpha(): # test 4
        return False
    letra = letra.lower() # test 3
    return letra in palabra_secreta 

palabra_secreta = "pera"

def ingresa_una_letra(letra: str, letras_usadas: set) -> bool:
    if letra in letras_usadas:
        return False
    return True

def adivinar(palabra: str, palabra_secreta: str) -> bool:
    if palabra == palabra_secreta: # test 7
        return True
    return False # test 8