palabra_secreta = "pera"
usadas = []
vidas = 6

def restar_vida(vidas: int)-> int:
    if vidas > 0:
        vidas -= 1
    return vidas

def letra_pertenece_palabra(letra: str, palabra_secreta: str) -> bool:
    if not letra.isalpha(): # test 4  -> el caracter es inválido
        return False
    letra = letra.lower() # el caracter es válido. test 3 -> mayúscula o minúscula
    usadas.append(letra) #agrego la nueva letra a las usadas
    if letra not in palabra_secreta:
        restar_vida(vidas)
        return False # test 2 -> la letra no está en la palabra
    return True # test 1 -> la letra está en la palabra
    

def verificar_disponibilidad(letra: str, usadas: list) -> bool:
    if letra in usadas:
        return False
    return True

def adivinar_palabra(palabra_secreta: str, usadas: list) -> bool:
    return set(palabra_secreta).issubset(usadas) # test 9
        

def arriesgar(palabra: str, palabra_secreta: str) -> bool:
    if palabra.lower() == palabra_secreta: # test 7 y 10
        return True
    return False # test 8