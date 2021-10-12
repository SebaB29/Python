def _producto_digitos(cadena, indice):
    if indice == len(cadena):
        return 1
    return int(cadena[indice]) * _producto_digitos(cadena, indice+1)

def producto_digitos(numero):
    return _producto_digitos(str(numero), 0)

print(producto_digitos(356))