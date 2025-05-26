#este es el que entregamos pero con los comentarios

from decorators import delta_time

def is_prime_sieve(n: int) -> list:
    """
    Devuelve True si n es primo, False en caso contrario,
    usando la Criba de Eratóstenes construida hasta n.
    """
    if n == 1:
        return True

    # Inicializa la criba
    is_prime = [True] * (n + 1) #hace una lista de booleanos
    is_prime[0] = False
    is_prime[1] = True # aca decia False (pero en este caso a nosotros nos sirve que 1 sea primo)

    # Solo necesitamos marcar hasta sqrt(n)
    limit = int(n**0.5)
    for p in range(2, limit + 1):
        if is_prime[p]:
            # Marca múltiplos de p como no primos
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    # El valor en la posición n indica si n es primo
    return is_prime # aca decia is_prime[n] y lo saque

def mcd(a, b):
    while b: #en Python, el número 0 es considerado falso, mientras que cualquier otro número distinto de cero es considerado verdadero.
        a, b = b, a % b 
        # la linea 3 la hace en el mismo instante de la manera que esta representado abajo, pero no se cambia el valor de A al dividir
        # a = b
        # b = a % b
    return a

@delta_time("BIG BRAIN alejito pro")
def carmichel(x, y):
    ls_carmichael = []
    list_prim = is_prime_sieve(y)
    test_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    test_bases_set = set(test_bases) #lo hace mas rapido

    for num in range(x, y + 1):
        if list_prim[num]:
            continue   

        for test_base in test_bases_set:
            if test_base >= num:
                break
            if mcd(test_base, num) == 1 and pow(test_base, num - 1, num) != 1:
                break                        
        else:
            is_carmichael = True
            raiz = int(num ** 0.5)
            for base in range(1, raiz + 1):
                if base not in test_bases_set and mcd(base, num) == 1 and pow(base, num - 1, num) != 1:
                    is_carmichael = False
                    break

            if is_carmichael:
                ls_carmichael.append(num)
    
    return ls_carmichael

if __name__ == "__main__":
    print(carmichel(1, 1000000))
