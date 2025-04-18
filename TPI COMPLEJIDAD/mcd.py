def mcd(a, b):

    if a < b:
        divisor = a
        dividend = b

    else: 
        divisor = b
        dividend = a

    rest = divisor
    while rest != 0:

        resg_rest = dividend % divisor
        resg_dividend = dividend // divisor

        if resg_rest != 0:
            divisor = resg_rest
            rest = resg_dividend
        else:
            return(divisor)


