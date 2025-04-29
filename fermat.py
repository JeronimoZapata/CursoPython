def fermat_malo(a, n):

    if ((a ** (n - 1)) % n) == 1:
        return True
    else:
        return False

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

'''
resultado = fermat(2, 9)
if resultado:
    print('Cumple fermat')
else:   
    print('No cummple fermat')
'''
