from string import ascii_letters, digits
from random import choice

CARACTERES = ascii_letters + digits

class Clave:

    def __init__(self: object, longitud: int = 12) -> None:
        """..."""

        self.__clave = self.__crear_clave(longitud)

    def __crear_clave(self: object, longitud: int) -> str:
        """..."""

        return "".join([choice(CARACTERES) for _ in range(longitud)])

    def encriptado_rot_n(self: object, n: int) -> None:
        """..."""

        nueva_cadena = ""

        for caracter in self.__clave:
            indice = CARACTERES.index(caracter)
            indice_cambiado = (indice + n) % len(CARACTERES)
            nueva_cadena += CARACTERES[indice_cambiado]

        self.__clave = nueva_cadena
    
    def __str__(self: object) -> str:
        return f"Clave -> {self.__clave}"


clave = Clave()
print(clave)
clave.encriptado_rot_n(13)
print(clave)
clave.encriptado_rot_n(-13)
print(clave)
