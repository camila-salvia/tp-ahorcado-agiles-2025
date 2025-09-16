def letra_pertenece_palabra(letra: str, palabra_secreta: str) -> bool:
<<<<<<< HEAD
    if not letra.isalpha():
        return False
    letra = letra.lower()
    return letra in palabra_secreta

palabra_secreta = "pera"
=======
    if not letra.isalpha(): # test 4
        return False
    letra = letra.lower() # test 3
    return letra in palabra_secreta 

palabra_secreta = "pera"

def ingresa_una_letra(letra: str, letras_usadas: set) -> bool:
    if letra in letras_usadas:
        return False
    return True
>>>>>>> e14f97a7e6abfa2dc4c68e131771af708efa503b
