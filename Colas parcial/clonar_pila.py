from pilas_colas_listas import *

def clonar_pila(pila):
    pila_clonada = Pila()
    aux = []
    while not pila.esta_vacia():
        aux.insert(0, pila.desapilar())
    
    for elemento in range(len(aux)):
        pila.apilar(aux[elemento])
        pila_clonada.apilar(aux[elemento])
    
    return pila_clonada

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)
print("Pila Original:", pila)
print("Pila Clonada:", clonar_pila(pila))
print("Pila Original despues de clonar:", pila)