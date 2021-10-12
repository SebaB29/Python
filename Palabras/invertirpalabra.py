from palabras import palabras

def invertir_palabra(palabra):
    """
    -Recibe: una palabra
    -Devulve: la palabra escrita al reves
    """

    return palabra[::-1]

print([palabra[::-1] for palabra in palabras]) # Usando lista por comprensión

print(list(map(invertir_palabra, palabras)))

print(list(map(lambda palabra: palabra[::-1], palabras)))