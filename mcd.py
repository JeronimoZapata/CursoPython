def mcd(a, b):
    while b != 0:
        a, b = b, a % b 
        # la linea 3 la hace en el mismo instante de la manera que esta representado abajo, pero no se cambia el valor de A al dividir
        # a = b
        # b = a % b
    return a

#print(mcd(543210,987654))
#este me dio chat gpt y lo estoy probando (gonza)