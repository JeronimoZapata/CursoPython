import fermat
import prime
import mcd
from decorators import delta_time


@delta_time("GRUPO BIG BRAIN 🧠")
def carmichel(x, y):
    ls_carmichael = []
    list_prim = prime.is_prime_sieve(y)
    test_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    for num in range(x, y + 1):
        if not list_prim[num]:  
            limit = int(num ** 0.5) + 1
            is_carmichael = True
            
            for base in test_bases:
                if base >= num:
                    break
                if mcd.mcd(base, num) == 1:
                    if fermat.fermat(base, num-1, num) != 1:
                        is_carmichael = False
                        break

            if is_carmichael:
                for base in range(1, min(limit, num), 1):
                    if base not in test_bases and mcd.mcd(base, num) == 1:
                        if fermat.fermat(base, num-1, num) != 1:
                            is_carmichael = False
                            break
            
            if is_carmichael:
                ls_carmichael.append(num)
    
    return ls_carmichael

if __name__ == "__main__":
    print(carmichel(1, 1000000))