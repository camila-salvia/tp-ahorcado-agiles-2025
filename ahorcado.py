def letra_pertenece_palabra(letra: str, palabra_secreta: str) -> bool:
    if not letra.isalpha():
        return False
    letra = letra.lower()
    return letra in palabra_secreta

palabra_secreta = "pera"
