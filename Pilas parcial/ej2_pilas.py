from pilas_colas_listas import *

def intercalar(secuencia_pilas):

    nueva_pila = Pila()

    while secuencia_pilas:
        for pila in range(len(secuencia_pilas)):
            pilas_a_eliminar = []
            if not secuencia_pilas[pila].esta_vacia():
                nueva_pila.apilar(secuencia_pilas[pila].desapilar())
            else:
                pilas_a_eliminar.append(pila)

        for pila in pilas_a_eliminar:
            secuencia_pilas.pop(pila)
    
    print(nueva_pila)

pila1 = Pila()
pila2 = Pila()
pila3 = Pila()
pila1.apilar(1)
pila1.apilar(2)
pila2.apilar(3)
pila2.apilar(4)
pila2.apilar(5)
pila2.apilar(6)
pila3.apilar(7)

intercalar([pila1, pila2, pila3])