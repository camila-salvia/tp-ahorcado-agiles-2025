import random
from palabras import palabras_posibles

"""
    entrada_valida()
        Descripción: Verifica si la entrada es válida o no.
        Devuelve True si la entrada es válida.
        Devuelve False si no es válida.
"""
def entrada_valida(letra_ingresada: str) -> bool:
    if letra_ingresada.isalpha() and len(letra_ingresada) == 1:
        return True # es válida        # TEST 
    return False # no es válida        # TEST 

"""
    verificar_disponibilidad()
        Descripción: Verifica si la letra ingresada ya fue usada.
        Devuelve True si la letra está disponible.
        Devuelve False si no está disponible (ya fue usada).
"""
def verificar_disponibilidad(letra: str, usadas: list) -> bool:
    letra = letra.lower()
    usadas = [l.lower() for l in usadas]
    return letra not in usadas

"""
    restar_vida()
        Descripción: Resta una vida al contador de vidas.
        Devuelve el nuevo número de vidas.
"""
def restar_vida(vidas: int)-> int:
    if vidas > 0:
        vidas -= 1
    return vidas


"""
    adivinar_palabra()
        Descripción: Verifica si todas las letras de la palabra secreta han sido adivinadas, comprobando si el conjunto de letras de la palabra es un subconjunto de las letras ya dichas.
        Devuelve True si la palabra ha sido adivinada: gana el juego.
        Devuelve False si la palabra no ha sido adivinada: sigue jugando.
"""
def adivinar_palabra(usadas: list, palabra_secreta: str) -> bool:
    return set(palabra_secreta).issubset(usadas) 

"""
    arriesgar()
        Descripción: Jugador arriesga la palabra completa y verifica si la palabra arriesgada es correcta.
        Devuelve True si la palabra arriesgada es correcta: gana el juego.
        Devuelve False si la palabra arriesgada es incorrecta: pierde el juego.
"""
def arriesgar(palabra: str, palabra_secreta: str) -> bool:
    if not palabra.lower() == palabra_secreta:
        return False
    return True


"""
    procesar_letra()
        Descripción: Procesa la letra ingresada, actualiza las vidas y las letras usadas.
        Devuelve una tupla con (nuevas_vidas, nuevas_usadas, fue_acierto)
"""
def procesar_letra(letra: str, palabra_secreta: str, vidas: int, usadas: list) -> tuple[int, list, bool]:
    
    letra = letra.lower() 
    nuevas_usadas = usadas + [letra]

    if letra in palabra_secreta:
        return (vidas, nuevas_usadas, True) # Acierto
    else:
        nuevas_vidas = restar_vida(vidas)
        return (nuevas_vidas, nuevas_usadas, False) # Error
    

"""
    generar_palabra_mostrada()
        Descripción: Genera la representación de la palabra secreta con las letras adivinadas y guiones bajos para letras no adivinadas.
        Devuelve una cadena con la palabra mostrada.
"""
def generar_palabra_mostrada(palabra_secreta: str, usadas: list) -> str: 
    palabra_mostrada = ""
    for letra in palabra_secreta:
        if letra in usadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    return palabra_mostrada 

"""
    obtener_mensaje_final()
        Descripción: Genera el mensaje final del juego según si el jugador ganó o perdió.
"""
def obtener_mensaje_final(usadas: list, palabra_secreta: str) -> str:
    if adivinar_palabra(usadas, palabra_secreta):
        return f"\n¡Felicitaciones! Adivinaste la palabra y ganaste el juego."
    else:
        return f"\n¡Perdiste! La palabra secreta era '{palabra_secreta}'."

"""
    gestionar_entrada()
        Descripción: Contiene la lógica principal de decisión del juego.
        Devuelve: (nuevas_vidas, nuevas_usadas, mensaje_usuario, juego_terminado)
    
        'intento_arriesgar' es la palabra ingresada si entrada=='arriesgar'. 
"""
def gestionar_entrada(entrada: str, intento_arriesgar: str, palabra_secreta: str, vidas: int, usadas: list) -> tuple:
    juego_terminado = False
    mensaje = ""

    if entrada == "arriesgar":
        if arriesgar(intento_arriesgar, palabra_secreta):
            # Agrega todas las letras de la palabra secreta a 'usadas' para ganar
            nuevas_usadas = usadas + list(set(palabra_secreta) - set(usadas))
            mensaje = "" # se maneja al final
            juego_terminado = True
            return (vidas, nuevas_usadas, mensaje, juego_terminado)
        else:
            mensaje = f"¡Incorrecto! La palabra no es '{intento_arriesgar}'. Perdiste."
            juego_terminado = True
            return (0, usadas, mensaje, juego_terminado) # Vidas a 0

    elif entrada_valida(entrada):
        if verificar_disponibilidad(entrada, usadas):
            vidas, usadas, acierto = procesar_letra(entrada, palabra_secreta, vidas, usadas)
            if acierto:
                mensaje = f"¡Bien hecho! La letra '{entrada}' está en la palabra."
            else:
                mensaje = f"¡Incorrecto! La letra '{entrada}' no está. Pierdes una vida."
        else:
            mensaje = f"Ya intentaste con la letra '{entrada}'. ¡Prueba otra!"
    else:
        mensaje = "Entrada inválida. Por favor, ingrese una sola letra o la palabra ARRIESGAR."
    
    # Comprobar si ganó después del turno
    if adivinar_palabra(usadas, palabra_secreta):
            juego_terminado = True
    elif vidas == 0:  # se quedó sin vidas
        juego_terminado = True
    return (vidas, usadas, mensaje, juego_terminado)

#PROGRAMA PRINCIPAL
def jugar():
    palabra_secreta = random.choice(palabras_posibles)
    usadas = []
    vidas = 6
    juego_terminado = False

    print("¡Bienvenido al juego del Ahorcado!")

    while vidas > 0 and not juego_terminado:
        print(f"\nVidas restantes: {vidas}")
        print(f"Letras usadas: {', '.join(usadas) if usadas else 'Ninguna'}")
        print("Palabra: " + generar_palabra_mostrada(palabra_secreta, usadas))

        entrada = input("Ingrese una letra o escriba ARRIESGAR para intentar adivinar la palabra: ").lower()
        intento_arriesgar = None
        
        if entrada == "arriesgar":
            intento_arriesgar = input("Ingrese la palabra: ")
        
        # Toda la lógica de decisión se mueve a la función testable
        vidas, usadas, mensaje, juego_terminado_turno = gestionar_entrada(
            entrada, intento_arriesgar, palabra_secreta, vidas, usadas
        )
        
        if mensaje:
            print(mensaje)
        
        # 'juego_terminado_turno' es True si se arriesgó (bien o mal) o si se adivinó la última letra
        if juego_terminado_turno:
            juego_terminado = True
    
    print(obtener_mensaje_final(usadas, palabra_secreta))

if __name__ == "__main__":
    jugar()