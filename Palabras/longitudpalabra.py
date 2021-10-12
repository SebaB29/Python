from palabras import palabras

def longitud_palabra(palabra, n):
    """
    -Recibe: una palabra y un numero entero positivo(n)
    -Devuelve:
    - True, si la palabra tiene longitud n
    - False, en caso contrario
    """

    return len(palabra) == n

n = 20

print()

#print( list( filter(lambda palabra: len( palabra ) == n , palabras) ) )

print()

#print( [ palabra for palabra in palabras if longitud_palabra(palabra, n) ] ) # Usando lista por comprensión