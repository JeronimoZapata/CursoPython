def fermat(a, n):

    rest = (a ** (n -1)) % n
    
    if rest == 1: 
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
