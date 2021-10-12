from pilas_colas_listas import *

def operaciones_pila(cadena, pila):
    suma_numeros = 0
    for caracter in cadena:
        if not caracter.isdigit():
            if not pila.esta_vacia():
                suma_numeros -= pila.desapilar()
        else:
            caracter = int(caracter)
            suma_numeros += caracter
            pila.apilar(caracter)
    
    return suma_numeros

pila = Pila()
cadena = "x85x179xx"
print(operaciones_pila(cadena, pila))
print(pila)