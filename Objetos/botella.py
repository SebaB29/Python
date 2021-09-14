class Botella:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.contenido = 0

    def esta_vacia(self):
        print(self.contenido == 0)

    def cargar(self, cantidad):
        if (cantidad + self.contenido) > self.capacidad:
            raise Exception("La botella no cuenta con capacidad suficiente")

        self.contenido += cantidad

    def servir(self, cantidad):
        if cantidad > self.contenido:
            raise Exception("La botella no cuenta con carga suficiente")

        self.contenido -= cantidad

    def __str__(self):
        return f"Botella: {self.contenido}/{self.capacidad}cc"

botella = Botella(500)
print(botella)
botella.esta_vacia()
botella.cargar(200)
print(botella)
botella.servir(100)
print(botella)