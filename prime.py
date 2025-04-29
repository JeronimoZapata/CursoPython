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

#print (is_prime_sieve(561))