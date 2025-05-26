#a diferencia del que entregamos le sacamos varios if y aparte ordenamos

#import fermat
import prime
import mcd
#import is_square_free
from decorators import delta_time

@delta_time("BIG BRAIN sin raiz")
def carmichel(x, y):
    ls_carmichael = []
    list_prim = prime.is_prime_sieve(y)
    test_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    test_bases_set = set(test_bases) #lo hace mas rapido

    for num in range(x, y + 1):
        if not list_prim[num]:  # Si no es primo
            
            # Optimización: Solo necesitamos probar hasta la raíz cuadrada del número
            # más algunas bases adicionales para garantizar la corrección
            raiz = int(num ** 0.5) + 1
            is_carmichael = True
            
            # Probamos bases pequeñas primero
            for base in test_bases_set:
                if base >= num:
                    break
                if mcd.mcd(base, num) == 1:
                    if pow(base, num-1, num) != 1:
                        is_carmichael = False
                        break

            if is_carmichael: #and is_square_free(num)
                for base in range(1, raiz, 1):
                    if (base not in test_bases_set) and (mcd.mcd(base, num)) == 1: # estas bases ya calculamos el mcd antes(base not in test_bases)
                        if pow(base, num-1, num) != 1:
                            is_carmichael = False
                            break

            if is_carmichael:
                ls_carmichael.append(num)

    return ls_carmichael

if __name__ == "__main__":
    print(carmichel(1, 1000000))
