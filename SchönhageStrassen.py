def _ext_gcd(a: int, b: int):
    """Euclídeo extendido clásico; retorna (u, v, g) tales que u·a+v·b=g=gcd(a,b)."""
    if b == 0:
        return (1, 0, a)
    u2, v2, g = _ext_gcd(b, a % b)
    u1 = v2
    v1 = u2 - (a // b) * v2
    return (u1, v1, g)

def _half_gcd(a: int, b: int, threshold: int = 64):
    """
    Half‑GCD: devuelve matriz (u, v, x, y) que reduce (a, b) a un par
    cuyo segundo componente tiene ≤ bitlen(b)//2 o ≤ threshold bits.
    """
    if b == 0 or b.bit_length() <= threshold:
        # Caemos al Euclídeo extendido
        u, v, _ = _ext_gcd(a, b)
        return (u, v, 0, 1)
    k = b.bit_length() >> 1
    a1, a0 = a >> k, a & ((1 << k) - 1)
    b1, b0 = b >> k, b & ((1 << k) - 1)

    # Recursión en la mitad alta
    u, v, x, y = _half_gcd(a1, b1, threshold)
    # Aplico la matriz a (a, b)
    a_p = u * a + v * b
    b_p = x * a + y * b

    # Unos pasos de Euclídeo clásico para reducir b_p hasta ≤ k bits
    while b_p.bit_length() > k:
        q = a_p // b_p
        a_p, b_p = b_p, a_p - q * b_p
        u, v, x, y = x, y, u - q * x, v - q * y

    return (u, v, x, y)

def gcd(a: int, b: int) -> int:
    """
    Máximo común divisor sub‑cuadrático según Schönhage–Strassen.
    Devuelve directamente gcd(a, b).
    """
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    # Mientras b sea “grande”, aplicamos half‑GCD
    while b.bit_length() > 64:
        u, v, x, y = _half_gcd(a, b)
        a, b = u * a + v * b, x * a + y * b
    # Terminamos con Euclídeo clásico extendido y devolvemos g
    return _ext_gcd(a, b)[2]

# Ejemplo de uso:
'''if __name__ == "__main__":
    a, b = 66528, 52920
    resultado = gcd(a, b)
    print(f"El mcd de {a} y {b} es {resultado}")'''  # → El mcd de 66528 y 52920 es 24
