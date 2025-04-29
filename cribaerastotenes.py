def criba(n):
    """
    Genera todos los números primos menores o iguales a n
    utilizando la Criba de Eratóstenes.
    """
    primos = []
    # Creamos una lista de booleanos para marcar los números primos
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos

    for i in range(2, int(n ** 0.5) + 1):
        if es_primo[i]:
            # Marcamos los múltiplos de i como no primos
            for j in range(i * i, n + 1, i):
                es_primo[j] = False

    # Recopilamos los números que quedaron marcados como primos
    for i in range(2, n + 1):
        if es_primo[i]:
            primos.append(i)

    return primos


# Obtener todos los números primos hasta 100
#print(criba(1000000))
