import random

# Verifica si la entrada es válida o no
def entrada_valida(letra_ingresada: str) -> bool:
    if letra_ingresada.isalpha() and len(letra_ingresada) == 1:
        return True # es válida TEST 2
    return False # no es válida TEST 1

# Verifica si la letra ingresada ya fue usada
def verificar_disponibilidad(letra: str, usadas: list) -> bool:
    if letra in usadas:
        return False # no está disponible (ya fue usada) TEST 4
    return True # está disponible (puede usarse) TEST 3


def restar_vida(vidas: int)-> int:
    if vidas > 0:
        vidas -= 1
    return vidas

# Comprueba si el conjunto de letras de la palabra es un subconjunto de las letras ya dichas
def adivinar_palabra(usadas: list, palabra_secreta: str) -> bool:
    return set(palabra_secreta).issubset(usadas) 
            # True -> gana juego
            # False -> sigue jugando

# Jugador arriesga la palabra completa
def arriesgar(palabra: str, palabra_secreta: str) -> bool:
    if not palabra.lower() == palabra_secreta: # TEST 7
        return False   #arriega y falla TEST 6
    return True   #arriega y gana   TEST 5

# Procesa la letra ingresada y devuelve el nuevo estado del juego
    # Devuelve (nuevas_vidas, nuevas_usadas, fue_acierto)
def procesar_letra(letra: str, palabra_secreta: str, vidas: int, usadas: list) -> tuple[int, list, bool]:
    
    letra = letra.lower() 
    nuevas_usadas = usadas + [letra]

    if letra in palabra_secreta:
        return (vidas, nuevas_usadas, True) # Acierto
    else:
        nuevas_vidas = restar_vida(vidas)
        return (nuevas_vidas, nuevas_usadas, False) # Error


#PROGRAMA PRINCIPAL
if __name__ == "__main__":

    palabras_posibles = ["pera", "gato", "elefante", "computadora", "python", "televisor"]
    palabra_secreta = random.choice(palabras_posibles)
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

        entrada = input("Ingrese una letra o escriba ARRIESGAR para intentar adivinar la palabra: ").lower()
        if entrada == "arriesgar":
            intento = input("Ingrese la palabra: ")
            if arriesgar (intento, palabra_secreta):
                usadas.extend(list(set(palabra_secreta))) #agrega las letras que faltan
            else:
                vidas = 0
            break

        elif entrada_valida(entrada):
            if verificar_disponibilidad(entrada, usadas):
                vidas, usadas, acierto = procesar_letra(entrada, palabra_secreta, vidas, usadas)
                if acierto:
                    print(f"¡Bien hecho! La letra '{entrada}' está en la palabra.")
                else:
                    print(f"¡Incorrecto! La letra '{entrada}' no está. Pierdes una vida.")
            else:
                print(f"Ya intentaste con la letra '{entrada}'. ¡Prueba otra!")
        else:
            print("Entrada inválida. Por favor, ingrese una sola letra o la palabra ARRIESGAR.")
        
    if adivinar_palabra(usadas, palabra_secreta):
        print(f"\n¡Felicitaciones! Adivinaste la palabra '{palabra_secreta}' y ganaste el juego.")
    else:
        print(f"\n¡Perdiste! La palabra secreta era '{palabra_secreta}'.")
