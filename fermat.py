
def fermat(a, e, n):
    # Calcula a^e mod n usando exponenciación rápida
    resultado = 1
    a = a % n
    while e > 0:
        if e % 2 == 1:
            resultado = (resultado * a) % n
        a = (a * a) % n
        e //= 2
    return resultado

