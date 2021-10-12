from pilas_colas_listas import *

def intercambiar_elementos(pila1, pila2):
    pila_aux1 = Pila()
    pila_aux2 = Pila()

    while not pila1.esta_vacia():
        pila_aux1.apilar(pila1.desapilar())
    while not pila2.esta_vacia():
        pila_aux2.apilar(pila2.desapilar())
    while not pila_aux2.esta_vacia():
        pila1.apilar(pila_aux2.desapilar())
    while not pila_aux1.esta_vacia():
        pila2.apilar(pila_aux1.desapilar())

pila1 = Pila()
pila2 = Pila()
pila1.apilar(1)
pila1.apilar(2)
pila1.apilar(3)
pila2.apilar(4)
pila2.apilar(5)
pila2.apilar(6)
print("Pila 1:", pila1)
print("Pila 2:", pila2)
intercambiar_elementos(pila1, pila2)
print("Pila 1:", pila1)
print("Pila 2:", pila2)