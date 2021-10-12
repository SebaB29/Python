from pilas_colas_listas import *

def repartir(cola, numero):
    lista_colas = []
    for i in range(numero):
        lista_colas.append(Cola())
    
    aux = []
    while not cola.esta_vacia():
        aux.append(cola.desencolar())

    cantidad_elementos = len(aux) // numero
    empieza = 0
    for elemento in lista_colas:
        for i in range(empieza, len(aux), 2):
            elemento.encolar(aux[i])
        empieza += 1
            
    
    return lista_colas

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)
cola.encolar(6)
cola.encolar(7)
cola.encolar(8)
cola.encolar(9)
for i in repartir(cola, 2):
    print(i)