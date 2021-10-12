from pilas_colas_listas import *

def es_par(numero):
    return numero % 2 == 0

def cola_filter(cola, funcion):
    nueva_cola = Cola()

    while not cola.esta_vacia():
        dato = cola.desencolar()
        if funcion(dato):
            nueva_cola.encolar(dato)
    
    return nueva_cola

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
print(cola_filter(cola, es_par))