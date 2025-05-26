#esta funcion tampoco directamente no la usamos, quedo en el camino

def is_square_free(n):
    """Devuelve False si n tiene algún factor primo al cuadrado"""
    i = 2
    while i * i <= n:
        count = 0
        while n % i == 0:
            n //= i
            count += 1
            if count > 1:
                return False  # tiene i^2
        i += 1
    return True
