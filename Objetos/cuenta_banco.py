class Cuenta:
    def __init__(self, apellido):
        self.apellido = apellido
        self.dinero_cuenta = 0
        self.movimientos_cuenta = []

    def acreditar(self, cantidad, tipo):
        self.dinero_cuenta += cantidad
        self.movimientos_cuenta.append(("acreditación", cantidad, tipo))

    def extraer(self, cantidad, tipo):
        if cantidad > self.dinero_cuenta:
            raise ValueError("Fondos Insuficioentes")
        self.dinero_cuenta -= cantidad
        self.movimientos_cuenta.append(("extracción", cantidad, tipo))

    def transferir(self, cantidad, otra_cuenta):
        if cantidad > self.dinero_cuenta:
            raise ValueError("Fondos Insuficioentes")
        self.dinero_cuenta -= cantidad
        self.movimientos_cuenta.append(("extracción", cantidad, f"Cuenta de {otra_cuenta.apellido}"))
        otra_cuenta.dinero_cuenta += cantidad
        otra_cuenta.movimientos_cuenta.append(("acreditación", cantidad, f"Cuenta de {self.apellido}"))

    def movimientos(self):
        print(self.movimientos_cuenta)

    def saldo(self):
        print(self.dinero_cuenta)

    def __str__(self):
        return f"Cuenta de {self.apellido}"

c = Cuenta("Perez")
d = Cuenta("Brizuela")

c.acreditar(100, "Sueldo")
# c.extraer(60, "Shopping")
# c.saldo()
# print(c)
# c.transferir(30, d)
c.saldo()
# d.saldo()
# c.movimientos()
# d.movimientos()
# d.extraer(10, "Deudas") 
