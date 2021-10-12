from pilas_colas_listas import *

def apilar_pares(pila):
    nueva_pila = Pila()
    aux = []

    while not pila.esta_vacia():
        aux.insert(0, pila.desapilar())
    
    for numero in aux:
        if numero % 2 == 0:
            nueva_pila.apilar(numero)
        pila.apilar(numero)
    
    return nueva_pila

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
print("Pila Original", pila)
print("Nueva Pila", apilar_pares(pila))
print("Pila Original", pila)