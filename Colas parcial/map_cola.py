from pilas_colas_listas import *

def numero_al_cuadrado(numero):
    return numero ** 2

def cola_map(cola, funcion):
    nueva_cola = Cola()

    aux = []
    while not cola.esta_vacia():
        aux.append(cola.desencolar())
    
    for elemento in range(len(aux)):
        cola.encolar(aux[elemento])
        nueva_cola.encolar(funcion(aux[elemento]))
    
    return nueva_cola

cola = Cola()
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
print("Cola_map:", cola_map(cola, numero_al_cuadrado))
print("Cola Original:", cola)