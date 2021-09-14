class Tatuaje:
    def __init__(self, nombre, area, dolor):
        self.nombre = nombre
        self.area = area
        self.dolor = dolor

class Tatuador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tatuajes_realizados = 0

    def tatuar(self, zona_cuerpo, tatuaje):
        if tatuaje.area > zona_cuerpo.area:
            raise ValueError("Ya no te queda más lugar")
        elif tatuaje.dolor > zona_cuerpo.aguante:
            raise ValueError("No te la bancas")

        zona_cuerpo.area -= tatuaje.area
        self.tatuajes_realizados += 1

    def __str__(self):
        return f"{self.nombre}: {self.tatuajes_realizados} tatuajes realizados"

class ZonaCuerpo:
    def __init__(self, area, aguante):
        self.area = area
        self.aguante = aguante

tat_dragon = Tatuaje("Dragon", 10, 30)
tat_hoja = Tatuaje("Hoja", 10, 30)
tatuador = Tatuador("Sebastian")
brazo = ZonaCuerpo(20, 100)

tatuador.tatuar(brazo, tat_dragon)
print(tatuador)
tatuador.tatuar(brazo, tat_hoja)
print(tatuador)