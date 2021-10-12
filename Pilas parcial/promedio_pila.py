from pilas_colas_listas import *

def promedio_elementos(pila):
    aux = Pila()

    cantidad_numeros = 0
    suma_numeros = 0
    while not pila.esta_vacia():
        dato = pila.desapilar()
        suma_numeros += dato
        cantidad_numeros += 1
        aux.apilar(dato)
    
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

    if cantidad_numeros > 0:
        return suma_numeros / cantidad_numeros

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print(pila)
print(promedio_elementos(pila))
print(pila)