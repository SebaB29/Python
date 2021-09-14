class CajaFuerte:
    def __init__(self, codigo):
        self.codigo = codigo
        self.caja_esta_abierta = False
        self.objetos_guardados = []

    def esta_abierta(self):
        print(self.caja_esta_abierta)

    def abrir(self, codigo):
        if codigo != self.codigo:
            raise Exception("La clave es inválida")
        self.caja_esta_abierta = True

    def cerrar(self):
        self.caja_esta_abierta = False

    def guardar(self, objeto):
        if not self.caja_esta_abierta:
            raise Exception("La caja fuerte está cerrada")
        elif self.objetos_guardados:
            raise Exception("No se puede guardar más de una cosa")
        self.objetos_guardados.append(objeto)

    def sacar(self):
        if not self.caja_esta_abierta:
            raise Exception("La caja fuerte está cerrada")
        elif not self.objetos_guardados:
            raise Exception("No hay nada para sacar")
        print(self.objetos_guardados.pop())

    def __str__(self):
        return f"Código: {self.codigo}  /   Esta abierta: {self.caja_esta_abierta}   /   Objetos: {''.join(self.objetos_guardados)}"

caja = CajaFuerte(1234)
caja.abrir(1234)
caja.guardar("pulsera")
caja.cerrar()
print(caja)