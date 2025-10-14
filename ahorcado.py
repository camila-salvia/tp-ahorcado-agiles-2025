def entrada_valida(letra_ingresada: str) -> bool:
    if letra_ingresada.isalpha() and len(letra_ingresada) == 1: #test 4
        return True
    return False


def verificar_disponibilidad(letra: str, usadas: list) -> bool:
    if letra in usadas:
        return False
    return True


def restar_vida(vidas: int)-> int:
    if vidas > 0:
        vidas -= 1
    return vidas


def adivinar_palabra(usadas: list, palabra_secreta: str) -> bool:
    # Comprueba si el conjunto de letras de la palabra es un subconjunto de las letras usadas
    # True -> gana juego
    # False -> sigue jugando
    return set(palabra_secreta).issubset(usadas) # test 9
        

def arriesgar(palabra: str, palabra_secreta: str) -> bool:
    if not palabra.lower() == palabra_secreta: # test 8 y 10
        vidas = 0
        return False
    return True # test 7 -> gana el juego si acierta la palabra


def procesar_letra(letra: str, palabra_secreta: str, vidas: int, usadas: list) -> tuple[int, list, bool]:
    """
    Procesa una letra y devuelve el nuevo estado del juego
    Devuelve (nuevas_vidas, nuevas_usadas, fue_acierto)
    """
    letra = letra.lower() 

    if letra in palabra_secreta:
        nuevas_usadas = usadas + [letra]
        return (vidas, nuevas_usadas, True) # Acierto
    else:
        nuevas_vidas = restar_vida(vidas)
        nuevas_usadas = usadas + [letra]
        return (nuevas_vidas, nuevas_usadas, False) # Error


#PROGRAMA PRINCIPAL
if __name__ == "__main__":

    #VARIABLES
    palabra_secreta = "pera"
    usadas = []
    vidas = 6

    print("¡Bienvenido al juego del Ahorcado!")

    while vidas > 0 and not adivinar_palabra(usadas, palabra_secreta):
        print(f"\nVidas restantes: {vidas}")
        print(f"Letras usadas: {', '.join(usadas) if usadas else 'Ninguna'}")

        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in usadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "
        print("Palabra: " + palabra_mostrada)

        letra_ingresada = input("Ingrese una letra: ")

        if not entrada_valida(letra_ingresada.lower()):
            print("Entrada inválida. Por favor, ingrese una sola letra.")
            continue

        if not verificar_disponibilidad(letra_ingresada.lower(), usadas):
            print("Letra ya usada. Intente con otra letra.")
            continue

        usadas.append(letra_ingresada.lower())

        if letra_ingresada.lower() not in palabra_secreta:
            print(f"La letra '{letra_ingresada}' no está en la palabra. ¡Perdiste una vida!")
            vidas = restar_vida(vidas)
        else:
            print(f"¡Bien hecho! La letra '{letra_ingresada}' está en la palabra.")

        
    if adivinar_palabra(usadas, palabra_secreta):
        print(f"\n¡Felicitaciones! Adivinaste la palabra '{palabra_secreta}' y ganaste el juego.")
    else:
        print(f"\n¡Perdiste! La palabra secreta era '{palabra_secreta}'.")
