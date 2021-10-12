from pilas_colas_listas import *

def remover_duplicados_consecutivos(pila):
    
    aux = Pila()
    while not pila.esta_vacia():
        dato = pila.desapilar()
        if aux.esta_vacia() or dato != aux.ver_tope():
            aux.apilar(dato)
    
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
    
    return pila

pila = Pila()
pila.apilar(2)
pila.apilar(5)
pila.apilar(8)
pila.apilar(8)
pila.apilar(8)
pila.apilar(3)
pila.apilar(3)
pila.apilar(2)
pila.apilar(3)
pila.apilar(3)
pila.apilar(3)
pila.apilar(1)
pila.apilar(8)
pila.apilar(7)
print(pila)
print(remover_duplicados_consecutivos(pila))