def _busqueda_binaria(lista, elemento, desde, hasta):
    if desde > hasta:
        return -1
    medio = (hasta + desde) // 2
    if lista[medio] == elemento:
        return medio
    if elemento < lista[medio]:
        return _busqueda_binaria(lista, elemento, desde, medio - 1)
    return _busqueda_binaria(lista, elemento, medio + 1, hasta)

def busqueda_binaria(lista, elemento):
    return _busqueda_binaria(lista, elemento, 0, len(lista) - 1)


lista = [1,2,3,4,5,6,7,89,9,8,5,5,2,1]
print(busqueda_binaria(lista, 9))