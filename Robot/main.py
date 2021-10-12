from nave import abordar_nave, ROBOT
from test import test_de_sangre
from os import system

def main():
    """
    Inicia el buscador de robots
    """
    system("cls")

    nave = abordar_nave()
    encontrado, num_robot = test_de_sangre(nave)

    if encontrado:
        print(f"El robot {ROBOT} es el tripulante nº{num_robot}")
    else:
        print("No hay robot en la nave")

main()