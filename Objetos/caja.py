class Item:
    def __init__(self, objeto, peso):
        self.nombre_objeto = objeto
        self.peso_objeto = peso

class CajaLlena(Exception):
        pass

class Caja:
    def __init__(self, capacidad):
        self.almacenamiento = []
        self.capacidad = capacidad

    def guardar_item(self, item):
        if self.capacidad >= item.peso_objeto:
            self.capacidad -= item.peso_objeto
            self.almacenamiento.append((item.nombre_objeto, item.peso_objeto))
        else:
            raise CajaLlena("LA CAJA ESTÁ LLENA")

    def obtener_mas_pesado(self):
        objeto_mas_pesado, mayor_peso = None, 0
        for objeto, peso in self.almacenamiento:
            if peso > mayor_peso:
                objeto_mas_pesado, mayor_peso = objeto, peso

        return objeto_mas_pesado

    def obtener_mas_liviano(self):
        objeto_mas_liviano, menor_peso = None, self.capacidad
        for objeto, peso in self.almacenamiento:
            if peso < menor_peso:
                objeto_mas_liviano, menor_peso = objeto, peso

        return objeto_mas_liviano


    def __str__(self):
        objetos = []
        for objeto, peso in self.almacenamiento:
            objetos.append(objeto)
        return f"Objetos: {', '.join(objetos)}"

pelota = Item("Pelota", 5)
parl = Item("Parlante", 4)
tv = Item("TV", 5)
caja = Caja(100)
caja.guardar_item(pelota)
caja.guardar_item(parl)
caja.guardar_item(tv)
print(caja)
print("Objeto mas pesado:", caja.obtener_mas_pesado())
print("Objeto mas liviano:", caja.obtener_mas_liviano()) 