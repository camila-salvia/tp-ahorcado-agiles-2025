palabra_secreta = "pera"
usadas = []
vidas = 6

def restar_vida(vidas: int)-> int:
    if vidas > 0:
        vidas -= 1
    return vidas


def verificar_disponibilidad(letra: str, usadas: list) -> bool:
    if letra in usadas:
        return False
    return True


#PRINCIPAL
def letra_pertenece_palabra(letra: str, palabra_secreta: str) -> bool:
    global vidas
    if not letra.isalpha(): # test 4  -> el caracter es inválido
        return False
    
    letra = letra.lower() 
   
    if not verificar_disponibilidad(letra, usadas): # test 5 y 6 -> la letra está disponible o no
        return False 
   
    usadas.append(letra) #agrego la nueva letra a las usadas
   
    if letra not in palabra_secreta.lower():
        vidas = restar_vida(vidas)
        if vidas == 0:
            return False # test 12 -> si llega a 0 vidas, pierde
        return False # test 2 -> la letra no está en la palabra      
    return True # test 1 -> la letra está en la palabra
    
    

def adivinar_palabra(usadas: list, palabra_secreta: str) -> bool:
    return set(palabra_secreta).issubset(usadas) # test 9
        

def arriesgar(palabra: str, palabra_secreta: str) -> bool:
    if palabra.lower() == palabra_secreta.lower(): # test 7 y 10
        return True
    return False # test 8