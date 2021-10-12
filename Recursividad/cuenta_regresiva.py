def cuenta_regresiva(n):
    """Cuenta desde n hasta 0"""
    if n == 0:
        print("BOOM")
    else:
        print(n)
        cuenta_regresiva(n-1)

cuenta_regresiva(10)