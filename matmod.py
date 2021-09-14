from math import factorial


def calcular_promedio(numeros: list) -> float:
    """Recibe una lista de números, devuelve el promedio"""
    
    return sum(numeros) / len(numeros) if numeros else None



def calcular_media_geometrica(numeros: list) -> float:
    """Recibe una lista de números, devuelve la media geométrica"""

    if not numeros:
        return
  
    producto_numeros = 1
    for numero in numeros:
        producto_numeros *= numero

    return producto_numeros ** (1 / len(numeros))



def calcular_integral(funcion, a: float, b: float, dx: float) -> float:
    """Calcula la integral de la función pasada por parámetro entre los extremos a y b"""

    resultado = 0
    while a < b:
        resultado += funcion(a + dx) * dx if resultado == 0 else funcion(a + dx) * dx
        a += dx

    return resultado



def aproximar_pi(indice_sumatoria: int) -> float:
    """Aproxima el valor de pi"""

    factor = 2 * pow(2, 0.5) / 9801
    sumatoria = 0
    for i in range(indice_sumatoria):
        sumatoria += factorial(4 * i) * (1103 + 26390 * i) / (factorial(i)**4 * 396**(4 * i))

    return 1 / (factor * sumatoria)



def aproximar_e(self:object, cantidad_terminos: int) -> float:
    """Aproxima el valor del número e"""

    resultado = 0
    for numero in range(cantidad_terminos):
        resultado += 1 / factorial(numero)

    return resultado



def collatz(numero: int) -> list:
    """Calcula la conjetura de Collatz"""

    return __collatz_recursivo(numero, [])

def __collatz_recursivo(numero: int, pasos: list) -> list:
    """Calcula recursivamente la conjetura de Collatz, devuelve los pasos realizados"""

    pasos.append(numero)
    if numero == 1:
        return pasos
    if numero % 2 == 0:
        return __collatz_recursivo(numero // 2, pasos)
    return __collatz_recursivo(numero * 3 + 1, pasos)



def fibonacci(terminos: int) -> list:
    """Calcula la secuencia de Fibonacci, devuelve la cantidad de terminos pasada por parámetro"""

    return __fibonacci_recursivo(terminos, []) if terminos >= 0 else None

def __fibonacci_recursivo(terminos: int, secuencia: list) -> list:
    """Calcula recursivamente la secuencia de Fibonacci"""

    if not terminos:
        return secuencia
    if len(secuencia) == 0:
        secuencia.append(0)
    elif len(secuencia) == 1:
        secuencia.append(1)
    else:
        secuencia.append(secuencia[-2] + secuencia[-1])
    return __fibonacci_recursivo(terminos - 1, secuencia)