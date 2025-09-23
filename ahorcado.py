palabra_secreta = "pera"
usadas = set()

def letra_pertenece_palabra(letra: str, palabra_secreta: str) -> bool:
    if not letra.isalpha(): # test 4
        return False
    letra = letra.lower() # test 3
    return letra in palabra_secreta 

def ingresa_una_letra(letra: str, usadas: set) -> bool:
    if letra in usadas:
        return False
    return True

def adivinar_palabra(palabra_secreta: str, usadas: set) -> bool:
    return set(palabra_secreta).issubset(usadas) # test 9
        

def arriesgar(palabra: str, palabra_secreta: str) -> bool:
    if palabra.lower() == palabra_secreta: # test 7 y 10
        return True
    return False # test 8