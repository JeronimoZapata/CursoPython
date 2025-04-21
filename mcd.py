def mcd(divisor, dividend):

    modulo = divisor
    while modulo != 0:

        modulo = dividend % divisor
        resultado = dividend // divisor

        if modulo != 0:
            divisor = modulo
            dividend = divisor
        else:
            return(divisor)


