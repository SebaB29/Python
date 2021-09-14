class Personaje:

    def __init__(self, daño):
        self.vida = 100
        self.daño = daño

    def atacar(self, enemigo):
        if enemigo.vida <= 0:
            raise Exception("El enemigo está muerto")
        elif self.vida <= 0:
            raise Exception("Estás muerto")

        enemigo.vida -= self.daño

    def curar(self, cantidad_regenerada):
        if self.vida <= 0:
            raise Exception("Estas muerto")
        while self.vida > 100:
            self.vida -= 1

    def esta_muerto(self):
        print(self.vida <= 0)

jugador1 = Personaje(75)
jugador2 = Personaje(10)

jugador1.atacar(jugador2)
jugador2.esta_muerto()
jugador1.atacar(jugador2)
jugador2.esta_muerto()
jugador1.curar(100)
print(jugador1.vida)