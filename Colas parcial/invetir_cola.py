from pilas_colas_listas import *

def invertir_cola(cola):
    
    if cola.esta_vacia():
        return
    
    dato = cola.desencolar()
    invertir_cola(cola)
    cola.encolar(dato)


cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print(cola)
invertir_cola(cola)
print(cola)