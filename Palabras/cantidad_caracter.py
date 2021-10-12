def _cantidad_caracter(cadena, caracter, indice, cantidad):
    if indice == len(cadena):
        return cantidad
    if caracter == cadena[indice]:
        cantidad += 1
    return _cantidad_caracter(cadena, caracter, indice + 1, cantidad)

def cantidad_caracter(cadena, caracter):
    """Cuenta la cantidad de apariciones del caracter en la cadena"""
    
    return _cantidad_caracter(cadena, caracter, 0, 0)