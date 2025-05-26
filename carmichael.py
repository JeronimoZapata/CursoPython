from decorators import delta_time

def is_prime_sieve(n: int) -> list:
    if n == 1:
        return True

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = True

    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    return is_prime

def mcd(a, b):
    while b:
        a, b = b, a % b 
    return a

def coprime_list(n: int) -> list[int]:
    if n <= 2:
        return [1] if n == 2 else []

    factors = set()
    m = n
    while m % 2 == 0:
        factors.add(2)
        m //= 2
    f = 3
    while f * f <= m:
        if m % f == 0:
            factors.add(f)
            while m % f == 0:
                m //= f
        f += 2
    if m > 1:
        factors.add(m)

    if factors == {n}:          # n is prime
        return list(range(1, n))

    mark = bytearray(n)
    for p in factors:
        mark[p:n:p] = b'\x01' * ((n - 1) // p)
    return [k for k in range(1, n) if not mark[k]]


test_bases_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
test_bases_set = set(test_bases_list)  

@delta_time("GRUPO BIG BRAIN CON 🧠")
def carmichel(x, y):
    ls_carmichael = []
    list_prim = is_prime_sieve(y)

    for num in range(x, y + 1):
        if list_prim[num]:
            continue   

        for test_base in test_bases_list:
            if test_base >= num:
                break
            if mcd(test_base, num) == 1 and pow(test_base, num - 1, num) != 1:
                break                        
        else:
            is_carmichael = True
            for coprime in coprime_list(num):
                if pow(coprime, num - 1, num) != 1:
                    is_carmichael = False
                    break

            if is_carmichael:
                ls_carmichael.append(num)
    
    return ls_carmichael

if __name__ == "__main__":
    print(carmichel(1, 1000000))