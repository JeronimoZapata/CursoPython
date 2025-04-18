import mcd
import fermat
import prime

def carmichel(x, y):

    ls_carmichael = []
    for num in range(x, (y + 1)):

        ls_coprim = []
        for element in range(1, num):

            if mcd.mcd(element, num) == 1:
                ls_coprim.append(element)
        
        flag = True
        for coprim in ls_coprim:
            
            if not (fermat.fermat(coprim, num)):
                flag = False
                break
        
        if flag and (not (prime.prime(num))):
            ls_carmichael.append(num)

    return ls_carmichael
