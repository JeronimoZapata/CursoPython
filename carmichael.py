import fermat
import SchönhageStrassen
import cribaerastotenes
import prime
import mcd

def carmichel(x, y):

    ls_carmichael = []
    list_prim = prime.is_prime_sieve(y)

    for num in range(x, (y + 1)):

        if not (list_prim[num]): 

            for element in range(1, num):                          #An3 + Bn2 + C

                flag = True
                if mcd.mcd(element, num) == 1:      #Lo que mas tarda

                    if fermat.fermat(element, num-1, num) !=1:
                        flag = False
                        break

            if flag:
                ls_carmichael.append(num)

    return ls_carmichael

print(carmichel(1, 1000000))