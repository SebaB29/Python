from pilas_colas_listas import *

class ColaDistribuidora:
    def __init__(self, ids, f):
        self.colas = {id: Cola for id in ids}
        self.f = f
    
    def encolar(self, elemento):
        self.colas[self.f(elemento)].encolar(elemento)
    
    def desencolar(self, id):
        return self.colas[id].desencolar()
    
    def esta_vacia():
        for k, cola in self.colas.items():
            if not cola.esta_vacia():
                return False
        return True