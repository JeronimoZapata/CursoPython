def mcd(divisor, dividend):

    modulo = divisor # 8
    while modulo != 0:

        modulo = dividend % divisor # 4
        resultado = dividend // divisor # 1

        if modulo != 0:
            divisor = modulo # 4
            dividend = divisor # 4
        else:
            return(divisor)

print(mcd(543210,987654))
#543210,987654