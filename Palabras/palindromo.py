def es_palindromo(palabra):
    """Recibe un texto y devuelve True si se lee igual al derecho qu al revéz y False en caso contrario"""

    palabra = "".join([caracter for caracter in palabra if caracter.isalpha()])
    palabra_invertida = "".join([caracter for caracter in palabra if caracter.isalpha()][::-1])
    return palabra.upper() == palabra_invertida.upper()