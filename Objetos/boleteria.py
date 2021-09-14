class Boleteria:
    def __init__(self, evento, asientos):
        self.evento = evento
        self.asientos = asientos
        self.asientos_vendidos = 0

    def vender_asientos(self, cantidad):
        if (self.asientos_vendidos + cantidad) > self.asientos:
            raise ValueError("No hay asientos suficientes")
        self.asientos_vendidos += cantidad

    def asientos_agotados(self):
        print(self.asientos == self.asientos_vendidos)

    def __str__(self):
        return f"Evento: {self.evento}  -  Asientos vendidos: {self.asientos_vendidos} de {self.asientos}"

evento1 = Boleteria("LolaPalooza", 1000)
evento1.vender_asientos(900)
print(evento1)
evento1.asientos_agotados()
print(evento1)
evento1.vender_asientos(100)
evento1.asientos_agotados()
print(evento1)