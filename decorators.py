import time

def delta_time(n):
    def count_elapsed_time(f):
       
        def w(*args, **kwargs):
            start_time = time.perf_counter()
            ret = f(*args, **kwargs)
            elapsed_time = (time.perf_counter()) - start_time
            print(f"{n} --> Tardo: {elapsed_time:.8f} Seconds.")
            return ret
        
        return w
    return count_elapsed_time