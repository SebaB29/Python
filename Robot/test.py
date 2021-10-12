from nave import ROBOT

def test_de_sangre(nave):
    """
    -Recibe: la nave(lista)
    -Verifica la sangre de los tripulantes para encontrar al robot
    -Devuelve:
    - True, si se encuentra al ROBOT
    - False, si no se encuentra
    """

    encontrado = False

    num_min = 0
    num_max = len(nave) - 1
    encontrado = ""

    while (not encontrado) or (num_min <= num_max):
        medio = (num_min + num_max) // 2
        if nave[medio] == ROBOT:
            encontrado = "Si"
        if medio > nave.index(ROBOT):
            num_max = medio - 1       
        else:
            num_min = medio + 1
    
    if encontrado:
        return True, nave.index(ROBOT)
    
    return False, 0