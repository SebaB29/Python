from pilas_colas_listas import *

def clonar_pila(pila):
    pila_clonada = Pila()
    aux = []

    while not pila.esta_vacia():
        aux.insert(0, pila.desapilar())
    
    for elemento in aux:
        pila.apilar(elemento)
        pila_clonada.apilar(elemento)
    
    return pila_clonada

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print("Pila Original:", pila)
print("Pila Clonada: ", clonar_pila(pila))
print("Pila Original:", pila)