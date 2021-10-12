from pilas_colas_listas import *

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.longitud = 0
   
    def append(self, elemento):
        nuevo = Nodo(elemento)

        if not self.primero:
            self.primero = nuevo
            return
        
        actual = self.primero
        while actual.proximo:
            actual = actual.proximo
        
        actual.proximo = nuevo
        self.longitud += 1
    
    def clonar(self):
        nueva_lista = ListaEnlazada()
        actual = self.primero
        nueva_lista_actual = None
        while actual:
            if not nueva_lista_actual:
                nueva_lista.primero = Nodo(self.primero.dato, actual.proximo)
                nueva_lista_actual = nueva_lista.primero
            else:
                nueva_lista_actual = Nodo(actual, actual.proximo)
                
            nueva_lista_actual = nueva_lista_actual.proximo
            actual = actual.proximo
        
        return nueva_lista

    def __str__(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.proximo
        return " -> ".join(elementos)

lista = ListaEnlazada()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista_clonada = lista.clonar()
print("Lista Original:", lista)
print("Lista Clonada:", lista_clonada)