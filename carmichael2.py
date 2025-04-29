import mcd
import fermat
import prime

def carmichel(x, y):

    ls_carmichael = []
    for num in range(x, (y + 1)):

        if not (prime.is_prime_sieve(num)):

            for element in range(1, num):                          #An3 + Bn2 + C
                
                flag = True
                if mcd.mcd(element, num) == 1:      #Lo que mas tarda
                    
                    if not (fermat.fermat(element, num)):
                        flag = False
                        break

            if flag:
                print(num)
                ls_carmichael.append(num)

    return ls_carmichael

print(carmichel(1, 46657))
