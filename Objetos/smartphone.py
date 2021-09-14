class App:
    def __init__(self, nombre, sistemas_operativos):
        self.nombre_app = nombre
        self.os_soportados = sistemas_operativos

class Smartphone:
    def __init__(self, modelo, sistema_operativo):
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.Apps = []

    def instalar_app(self, aplicacion):
        if aplicacion.nombre_app in self.Apps:
            print("La app ya está instalada")
        elif not self.sistema_operativo in aplicacion.os_soportados:
            print("La app no es compatible")
        else:
            self.Apps.append(aplicacion.nombre_app)

    def __str__(self):
        return f"{self.modelo} ({self.sistema_operativo}). Apps: {', '.join(self.Apps)}"

app_fb, app_tw = App("Facebook", ["ios", "android"]), App("Twitter", ["ios", "android"])
motorola, nokia = Smartphone("Power Lite", "android"), Smartphone("Z1", "Windows")
motorola.instalar_app(app_fb)
motorola.instalar_app(app_tw)
print(motorola)
motorola.instalar_app(app_fb)
print(nokia)
nokia.instalar_app(app_fb) 