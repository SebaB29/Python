from pilas_colas_listas import _Nodo

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.longitud = 0
   
    def append(self, elemento):
        nuevo = _Nodo(elemento)

        if not self.primero:
            self.primero = nuevo
            return

        actual = self.primero
        while actual.proximo:
            actual = actual.proximo

        actual.proximo = nuevo
        self.longitud += 1

    def eliminar_repetidos(self):
        actual = self.primero
        while actual:
            if actual != self.primero and anterior.dato == actual.dato:
                anterior.proximo = actual.proximo
            else:
                anterior = actual
            actual = actual.proximo

    def __str__(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.proximo
        return " -> ".join(elementos)

lista = ListaEnlazada()
lista.append(1)
lista.append(1)
lista.append(1)
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(3)
lista.append(3)
lista.eliminar_repetidos()
print(lista)