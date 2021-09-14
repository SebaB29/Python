from math import factorial, log

# FALTA AGREGAR LAS FUNCIONES TRIGONOMÉTRICAS Y LAS CONSTANTES PI Y NÚMERO E

class Calculadora:

    def __init__(self: object) -> None:
        """Inicializa la clase Calculadora"""

        self.__funcion = None

    def colocar_funcion(self: object, funcion: str) -> None:
        """Establece la función ejecutada en la calculadora"""

        self.__funcion = funcion

    def sumar(self: object, numero1: float, numero2: float) -> float:
        """Devuelve la suma de número1 y número2, recibidos por parámetro"""

        return numero1 + numero2

    def restar(self: object, numero1: float, numero2: float) -> float:
        """Devuelve la resta de número1 menos número2, recibidos por parámetro"""

        return numero1 - numero2

    def multiplicar(self: object, factor1: float, factor2: float) -> float:
        """Devuelve el producto entre factor1 y factor2, recibidos por parámetro"""

        return factor1 * factor2

    def dividir(self: object, dividendo: float, divisor: float) -> float:
        """Devuelve la división entre el dividendo y el divisor, recibidos por parámetro"""

        return dividendo / divisor

    def raiz(self: object, radicando: float, indice: float) -> float:
        """Devuelve la raíz del radicando e indice, recibidos por parámetro"""

        return pow(radicando, 1 / indice)

    def potencia(self: object, base: float, exponente: float) -> float:
        """Devuelve la potencia de la base y exponente, recibidos por parámetro"""

        return pow(base, exponente)

    def factorial(self: object, numbero: int) -> int:
        """Devuelve el factorial del número recibido por parámetro"""

        return factorial(numbero)

    def logaritmo(self: object, argumento: float, base: float) -> float:
        """Devuelve el logaritmo del argumento con base, recibidos por parámetro"""

        return log(argumento, base)

    def logaritmo_natural(self: object, argumento: float) -> float:
        """Devuelve el logaritmo natural del argumento recibido por parámetro"""

        return log(argumento)


# PRUEBAS

mical = Calculadora()
mical.colocar_funcion("sumar")
mical.add(5, 6)

# try:
#     mical.factorial(-1)
# except ValueError:
#     print("Math Error")
# except ZeroDivisionError:
#     print("Math Error")
