#este es el que entregamos pero con los comentarios

from decorators import delta_time

def is_prime_sieve(n: int) -> list:
    """
    Devuelve True si n es primo, False en caso contrario,
    usando la Criba de Eratóstenes construida hasta n.
    """
    if n == 1:
        return True # Convención: para este caso tratamos al 1 como primo por conveniencia

    # Inicializa la criba (se asume que todos son primos inicialmente)
    is_prime = [True] * (n + 1) #hace una lista de booleanos
    is_prime[0] = False # 0 no es primo
    is_prime[1] = True # aca decia False (pero en este caso a nosotros nos sirve que 1 sea primo)

    # Solo es necesario revisar hasta la raíz cuadrada de n
    #No tiene un descubridor puntual porque es una consecuencia directa de la definición de número compuesto y las propiedades de la multiplicación, conocida desde hace siglos.
    #En tiempos modernos, esta propiedad es un resultado básico que se enseña en introducciones a la teoría de números, por ejemplo, en libros como:
        #Elementary Number Theory de David M. Burton
        #An Introduction to the Theory of Numbers de Hardy & Wright
    limit = int(n**0.5)
    for p in range(2, limit + 1):
        if is_prime[p]:
            # Marca múltiplos de p como False(numeros no primos)
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    # El valor en la posición n indica si n es primo
    return is_prime

# Cálculo del máximo común divisor usando el algoritmo de Euclides
def mcd(a, b):
    while b: #en Python, el número 0 es considerado falso, mientras que cualquier otro número distinto de cero es considerado verdadero.
        a, b = b, a % b 
        # la linea 3 la hace en el mismo instante de la manera que esta representado abajo, pero no se cambia el valor de A al dividir
        # a = b
        # b = a % b
    return a # El último valor no nulo de a es el MCD

@delta_time("GRUPO BIG BRAIN")
def carmichel(x, y):
    ls_carmichael = []
    list_prim = is_prime_sieve(y) # Generamos lista de primos hasta el numero mas grande
    test_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # Bases comunes para test de Fermat
    test_bases_set = set(test_bases) # Convertimos a conjunto para búsquedas más rápidas

    for num in range(x, y + 1):
        if list_prim[num]: #si le agregamos esto tarda la mitad inclusive or ((num % 2) == 0)
            continue   

        for test_base in test_bases_set:
            if test_base >= num:
                break  # No tiene sentido probar con bases mayores al número
            if mcd(test_base, num) == 1 and pow(test_base, num - 1, num) != 1:
                # usa POW para aprovechar la exponenciación modular eficiente(o exponenciación binaria)  de Python.
                # por ejemplo para pow(3, 13, 7)
                # No calcula 3**13 y luego el módulo. En vez de eso:
                # Escribe el exponente en binario:
                # 13 = 1101
                # Aplica el algoritmo binario para ir multiplicando mod 7 en cada paso, así nunca se manejan números grandes.
                # Esto se hace en log₂(exponente) pasos, por eso es tan rápido.
                break # Si falla el test de Fermat con alguna base, no es Carmichael                       
        else:
            # Si pasó todas las bases pequeñas, arranca desde 1 hasta la raíz
            is_carmichael = True
            raiz = int(num ** 0.5)
            for base in range(1, raiz + 1):
                # Evitamos repetir las bases ya probadas
                if (base not in test_bases_set) and (mcd(base, num)) == 1 and (pow(base, num - 1, num) != 1):
                    is_carmichael = False # No cumple con Fermat, descartado
                    break

            if is_carmichael:
                ls_carmichael.append(num) # Si pasó todas las pruebas, lo guardamos
    
    return ls_carmichael

if __name__ == "__main__":
    print(carmichel(1, 1000000))
