def es_primo(n):
    for num in range(2, n):
        if n % num == 0:
            return False
        return True

def _eliminar_sucedidos_por_primos(lista, indice, nueva_lista):
    if indice == len(lista)-1:
        nueva_lista.append(lista[indice])
        return nueva_lista

    if not es_primo(lista[indice+1]):
        nueva_lista.append(lista[indice])
    return _eliminar_sucedidos_por_primos(lista, indice+1, nueva_lista)

def eliminar_sucedidos_por_primos(lista):
    return _eliminar_sucedidos_por_primos(lista, 0, [])

print(eliminar_sucedidos_por_primos([4,7,6,11,13]))