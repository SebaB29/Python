from pilas_colas_listas import *

def fases_covid(cola):
    aux = []
    while not cola.esta_vacia():
        fase = cola.desencolar()
        if not aux or fase > aux[-1]:
            aux.append(fase)
    
    for fase in aux:
        cola.encolar(fase)
    
    return cola

cola = Cola()
cola.encolar(1)
cola.encolar(5)
cola.encolar(4)
cola.encolar(3)
cola.encolar(2)
cola.encolar(8)
print(fases_covid(cola))