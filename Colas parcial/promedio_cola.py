from pilas_colas_listas import *

def calcular_promedio(cola):
    aux = []

    while not cola.esta_vacia():
        aux.append(cola.desencolar())
    
    suma_elementos = 0
    for elemento in aux:
        suma_elementos += elemento
        cola.encolar(elemento)
    
    return suma_elementos / len(aux)

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print(calcular_promedio(cola))
print(cola)