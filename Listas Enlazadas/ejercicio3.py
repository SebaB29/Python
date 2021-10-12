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

    def ditribuir_en_colas(self, k):
        colas = []
        for i in range(k):
            colas.append(Cola())
        
        actual = self.primero
        while actual:
            for cola in range(len(colas)):
                colas[cola].encolar(actual.dato)
                actual = actual.proximo
                if not actual:
                    return colas

    def __str__(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.proximo
        return " -> ".join(elementos)

lista = ListaEnlazada()
lista.append("a")
lista.append("b")
lista.append("c")
lista.append("d")
lista.append("e")
lista.append("f")
lista.append("g")
colas = lista.ditribuir_en_colas(3)
print("Lista: ", lista)
for cola in colas:
    print("Cola: ", cola)