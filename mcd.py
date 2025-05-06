def mcd(a, b):
    while b != 0:
        a, b = b, a % b 
        # la linea 3 la hace en el mismo instante de la manera que esta representado abajo, pero no se cambia el valor de A al dividir
        # a = b
        # b = a % b
    return a
