def mcd(a, b):
    while b: #en Python, el número 0 es considerado falso, mientras que cualquier otro número distinto de cero es considerado verdadero.
        a, b = b, a % b 
        # la linea 3 la hace en el mismo instante de la manera que esta representado abajo, pero no se cambia el valor de A al dividir
        # a = b
        # b = a % b
    return a