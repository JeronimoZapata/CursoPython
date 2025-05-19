import fermat
import prime
import mcd
from decorators import delta_time
import multiprocessing
from multiprocessing import Pool

def process_chunk(args):
    start, end, primes = args
    ls_carmichael = []
    
    for num in range(start, end + 1):
        if not primes[num]:  # Si no es primo
            raiz_cuadrada = int(num ** 0.5) + 1
            is_carmichael = True
            
            # Probamos bases pequeñas primero para fallar rápido
            for base in range(2, min(31, num)):
                if mcd.mcd(base, num) == 1:
                    if fermat.fermat(base, num-1, num) != 1:
                        is_carmichael = False
                        break
            
            # Si pasa las bases pequeñas, probamos hasta la raíz cuadrada
            if is_carmichael:
                for base in range(31, min(raiz_cuadrada, num)):
                    if mcd.mcd(base, num) == 1:
                        if fermat.fermat(base, num-1, num) != 1:
                            is_carmichael = False
                            break
            
            if is_carmichael:
                ls_carmichael.append(num)
    
    return ls_carmichael

@delta_time("GRUPO BIG BRAIN")
def carmichel(x, y):
    # Calculamos la criba de primos una sola vez
    list_prim = prime.is_prime_sieve(y)
    
    # Determinamos el número de cores a usar (dejamos uno libre para el sistema)
    num_cores = max(1, multiprocessing.cpu_count() - 1)
    print('num_cores ', num_cores)
    
    # Calculamos el tamaño de cada chunk
    chunk_size = (y - x + 1) // num_cores
    if chunk_size < 10000:  # Si los chunks son muy pequeños, no vale la pena paralelizar
        return process_chunk((x, y, list_prim))
    
    # Preparamos los argumentos para cada proceso
    chunks = []
    for i in range(num_cores):
        start = x + i * chunk_size
        end = start + chunk_size - 1 if i < num_cores - 1 else y
        chunks.append((start, end, list_prim))
    
    # Creamos el pool de procesos y ejecutamos en paralelo
    with Pool(num_cores) as pool:
        results = pool.map(process_chunk, chunks)
    
    # Combinamos los resultados de todos los procesos
    ls_carmichael = []
    for result in results:
        ls_carmichael.extend(result)
    
    return sorted(ls_carmichael)

if __name__ == "__main__":
    print(carmichel(1, 1000000))