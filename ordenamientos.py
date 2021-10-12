# SELECCIÓN
def seleccion(lista):
    """
    Ordena una lista de elementos según el método de selección.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada
    """
    for i in range(len(lista) - 1):
        p = buscar_posicion_minimo(lista, i)
        lista[p], lista[i] = lista[i], lista[p]

def buscar_posicion_minimo(lista, i):
    """Devuelve la posición del elemento mínimo en lista[i:]"""
    posicion_minimo = i
    while i < len(lista):
        if lista[i] < lista[posicion_minimo]:
            posicion_minimo = i
        i += 1
    
    return posicion_minimo

# INSERCIÓN
def insercion(lista):
    """
    Ordena una lista de elementos según el método de inserción.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """
    for i in range(1, len(lista)):
        insertar_ordenado(lista, i)

def insertar_ordenado(lista, i):
    """
    Pre: lista[i] está ordenada.
    Post: lista[:i+1] está ordenada y contiene los mismos elementos que
    estaban en lista[:i] más el elemento que estaba en i.
    """
    v = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > v:
        lista[j + 1] = lista[j]
        j -= 1

    lista[j + 1] = v

# MERGESORT
def mergesort(lista):
    if len(lista) < 2:
        return lista
    
    med = len(lista) // 2
    izq = mergesort(lista[:med])
    der = mergesort(lista[med:])
    return merge(izq, der)

def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    
    resultado += lista1[i:]
    resultado += lista2[j:]
    
    return resultado

# QUICKSORT
def quicksort(lista):
    """Ordena la lista de forma recursiva.
    Pre: los elementos de la lista deben ser comparables.
    Devuelve: una nueva lista con los elementos ordenados.
    """
    if len(lista) < 2:
        return lista
    
    menores, medio, mayores = particionar(lista)

    return quicksort(menores) + medio + quicksort(mayores)

def particionar(lista):
    """
    Pre: lista no vacía.
    Devuelve: tres listas: menores, medio y mayores.
    """
    pivote = lista[0]
    menores = []
    mayores = []
    for i in range(1, len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])

    return menores, [pivote], mayores

# QUICKSORT IN-PLACE
def quicksort_in_place(lista):
    return _quicksort(lista, 0, len(lista) - 1)

def _quicksort_in_place(lista, desde, hasta):
    if desde >= hasta:
        return
    pivote = particionar(lista, desde, hasta)
    _quicksort(lista, desde, pivote - 1)
    _quicksort(lista, pivote + 1, hasta)

def particionar(lista, desde, hasta):
    pivote = desde
    for i in range(desde + 1, hasta + 1):
        if lista[i] <= lista[desde]:
            pivote += 1
            lista[i], lista[pivote] = lista[pivote], lista[i]
    
    lista[pivote], lista[desde] = lista[desde], lista[pivote]
    return pivote