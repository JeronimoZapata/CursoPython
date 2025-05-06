import fermat
import prime
import mcd
from decorators import delta_time

def modular_exp(base, exp, mod):
    if exp == 0:
        return 1
    if exp == 1:
        return base % mod
    
    temp = modular_exp(base, exp // 2, mod)
    temp = (temp * temp) % mod
    
    if exp % 2 == 1:
        temp = (temp * base) % mod
    
    return temp

@delta_time("GRUPO BIG BRAIN 🧠")
def carmichel(x, y):
    ls_carmichael = []
    list_prim = prime.is_prime_sieve(y)
    
    for num in range(x, y + 1):
        if not list_prim[num]:  # Si no es primo
            # Optimización: Solo necesitamos probar hasta la raíz cuadrada del número
            # más algunas bases adicionales para garantizar la corrección
            limit = int(num ** 0.5) + 1
            is_carmichael = True
            
            # Probamos bases pequeñas primero
            test_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
            for base in test_bases:
                if base >= num:
                    break
                if mcd.mcd(base, num) == 1:
                    if modular_exp(base, num-1, num) != 1:
                        is_carmichael = False
                        break
            
            # Si pasa las bases pequeñas, probamos algunas bases adicionales
            if is_carmichael:
                for base in range(31, min(limit, num), 2):
                    if mcd.mcd(base, num) == 1:
                        if modular_exp(base, num-1, num) != 1:
                            is_carmichael = False
                            break
            
            if is_carmichael:
                ls_carmichael.append(num)
    
    return ls_carmichael

if __name__ == "__main__":
    print(carmichel(1, 1000000))