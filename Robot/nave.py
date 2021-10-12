from random import randint

CANTIDAD_TRIPULANTES = 10
TRIPULANTE = "☺"
ROBOT = "☻"

def abordar_nave():
    """
    -Ubica dentro de la nave a los tripulantes y al robot
    -Devuelve la nave con todos abordo
    """

    nave = [TRIPULANTE for tripulante in range(CANTIDAD_TRIPULANTES)]
    nave.insert(randint(0, CANTIDAD_TRIPULANTES - 1), ROBOT)

    return nave