Feature: Jugar al ahorcado desde la interfaz web

    Scenario: Juego perfecto
        Given abro el juego del ahorcado
        When ingreso las letras "p e r a"
        Then veo el mensaje "Ganaste!"

    Scenario: Peor juego
        Given abro el juego del ahorcado
        When ingreso las letras "z x c v i o"
        Then veo el mensaje "Perdiste!"

    Scenario: Gano con algunos errores
        Given abro el juego del ahorcado
        When ingreso las letras "p y e o r q a"
        Then veo el mensaje "Ganaste!"

    Scenario: Pierdo con algunos aciertos
        Given abro el juego del ahorcado
        When ingreso las letras "z u p l r d k c"
        Then veo el mensaje "Perdiste!"