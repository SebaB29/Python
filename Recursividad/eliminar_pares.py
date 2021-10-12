def eliminar_pares(lista, indice):
    if indice == len(lista):
        return lista
    if lista[indice] % 2 == 0:
        lista.remove(lista[indice])
    return eliminar_pares(lista, indice+1)

lista = [1,2,3,4,5,6,7,8,9]
print(eliminar_pares(lista, 0))