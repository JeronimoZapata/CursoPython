import mcd
import fermat
import prime
import decorators


@decorators.delta_time("GRUPO GN")
def carmichel(x, y):

    ls_carmichael = []
    for num in range(x, (y + 1)):
        print("main for ", num)
        if not (prime.prime(num)):
            ls_coprim = []
            print("is prime ", num)
            for element in range(1, num):                           #An3 + Bn2 + C
                print("for element ", element)
                if mcd.mcd(element, num) == 1:
                    print("is coprim ", element)
                    ls_coprim.append(element)
            
            flag = True
            for coprim in ls_coprim:
                print("for coprim ", coprim)
                if not (fermat.fermat(coprim, num)):
                    print("not fermat ", coprim, num)
                    flag = False
                    break
            
            if flag:
                print("is carmichael ", num)
                ls_carmichael.append(num)

    return ls_carmichael

print(carmichel(1, 2821))