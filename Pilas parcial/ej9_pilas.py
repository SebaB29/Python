from pilas_colas_listas import *

def consecutivos(pila):
    aux = Pila()

    dato = None
    consecutiva = None
    while not pila.esta_vacia() and consecutiva == None:
        if not dato:
            dato = pila.desapilar()
            aux.apilar(dato)
        nuevo_dato = pila.desapilar()
        aux.apilar(nuevo_dato)
        if dato - 1 != nuevo_dato:
            consecutiva = False
        dato = nuevo_dato
    
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
    
    if consecutiva == None:
        consecutiva = True
        
    return consecutiva

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
print("Pila:", pila)
print(consecutivos(pila))
print("Pila:", pila)
pila2 = Pila()
pila2.apilar(1)
pila2.apilar(2)
pila2.apilar(4)
pila2.apilar(5)
print("Pila2:", pila2)
print(consecutivos(pila2))
print("Pila2:", pila2)