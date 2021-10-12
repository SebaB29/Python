from pilas_colas_listas import *

def transferir(pila1, pila2):
    aux = Pila()

    while not pila1.esta_vacia():
        aux.apilar(pila1.desapilar())
    
    while not aux.esta_vacia():
        pila2.apilar(aux.desapilar())

pila1 = Pila()
pila2 = Pila()
pila1.apilar(1)
pila1.apilar(2)
pila1.apilar(3)
pila2.apilar(4)
pila2.apilar(5)
pila2.apilar(6)
print("Pila1:", pila1)
print("Pila2:", pila2)
transferir(pila1, pila2)
print("Pila1:", pila1)
print("Pila2:", pila2)