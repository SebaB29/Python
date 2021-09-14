class Pasajero:
    def __init__(self, destino):
        self.destino = destino

class Colectivo:
    def __init__(self):
        self.asientos = []

    def subir(self, pasajero):
        self.asientos.append(pasajero)

    def bajar(self, destino):
        for pasajero in self.asientos:
            if pasajero.destino == destino:
                self.asientos.remove(pasajero)

    def __str__(self):
        return f"Asientos: {self.asientos}"

pasajero1 = Pasajero("Beccar")
pasajero2 = Pasajero("San Isidro")
pasajero3 = Pasajero("Beccar")

bondi = Colectivo()
bondi.subir(pasajero1)
bondi.subir(pasajero1)
bondi.subir(pasajero3)
print(bondi)
bondi.bajar("Beccar")
print(bondi) 