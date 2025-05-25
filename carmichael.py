from decorators import delta_time

def is_prime_sieve(n: int) -> list:
    if n == 1:
        return True

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = True

    limit = int(n**0.5)
    for p in range(2, limit + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    return is_prime

def mcd(a, b):
    while b:
        a, b = b, a % b 
    return abs(a)


@delta_time("GRUPO BIG BRAIN 🧠")
def carmichel(x, y):
    ls_carmichael = []
    list_prim = is_prime_sieve(y)
    test_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    for num in range(x, y + 1):
        if not list_prim[num]:  
            is_carmichael = True
            
            for base in test_bases:
                if base >= num:
                    break
                if mcd(base, num) == 1:
                    if pow(base, num-1, num) != 1:
                        is_carmichael = False
                        break

            if not is_carmichael:
                continue

            for base in range(1, num, 1):
                if base not in test_bases and mcd(base, num) == 1:
                    if pow(base, num-1, num) != 1:
                        is_carmichael = False
                        break
            
            if is_carmichael:
                ls_carmichael.append(num)
    
    return ls_carmichael

if __name__ == "__main__":
    print(carmichel(1, 1000000))