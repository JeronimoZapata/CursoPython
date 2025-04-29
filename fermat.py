def fermat(a, n):

    if ((a ** (n - 1)) % n) == 1:
        return True
    else:
        return False


'''
resultado = fermat(2, 9)
if resultado:
    print('Cumple fermat')
else:   
    print('No cummple fermat')
'''