palabra_secreta = "pera"
usadas = set()

def letra_pertenece_palabra(letra: str, palabra_secreta: str) -> bool:
    if not letra.isalpha(): # test 4
        return False
    letra = letra.lower() # test 3
    return letra in palabra_secreta 

def ingresa_una_letra(letra: str, letras_usadas: set) -> bool:
    if letra in letras_usadas:
        return False
    return True

def adivinar_palabra(palabra_secreta: str, letras_usadas: set) -> bool:
    for letra in usadas:
        if letra in palabra_secreta:
            return True
        

def arriesgar(palabra: str, palabra_secreta: str) -> bool:
    if palabra == palabra_secreta: # test 7
        return True
    return False # test 8