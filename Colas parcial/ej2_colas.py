from pilas_colas_listas import *
def agregar_a_lista(lista, cola):
    while not cola.esta_vacia():

        lista.append(cola.desencolar())
def ordenar_menor_a_mayor(cola1, cola2):
    cola_ordenada = Cola()
    aux = []

    agregar_a_lista(aux, cola1)
    agregar_a_lista(aux, cola2)

    aux = sorted(aux)
    for elemento in aux:
        cola_ordenada.encolar(elemento)

    return cola_ordenada

cola1 = Cola()
cola2 = Cola()
cola1.encolar(5)
cola1.encolar(2)
cola1.encolar(9)
cola1.encolar(1)
cola1.encolar(0)
cola1.encolar(12)
cola1.encolar(7)
print("Cola Ordenada:", ordenar_menor_a_mayor(cola1, cola2))