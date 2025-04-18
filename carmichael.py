import mcd
import fermat
import prime

def carmichel(x, y):

    ls_carmichael = []
    for num in range(x, (y + 1)):

        if not (prime.prime(num)):
            ls_coprim = []
            for element in range(1, num):                           #An3 + Bn2 + C

                if mcd.mcd(element, num) == 1:
                    ls_coprim.append(element)
            
            flag = True
            for coprim in ls_coprim:
                
                if not (fermat.fermat(coprim, num)):
                    flag = False
                    break
            
            if flag:
                ls_carmichael.append(num)

    return ls_carmichael

print(carmichel(1, 46657))