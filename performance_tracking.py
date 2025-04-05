import time
from typing import Callable

# float performance counter in Funktion wichtig, da Aufruf zu nicht Validen ergebnissen führen würde. So wird die übergebene Funktion innerhalb der performance time_function ausgeführt und so eine Repruduzierbares Ergebnis zur Optimierung geliefert.
def time_function(func, arg: str = None):
    start_time: float = time.perf_counter() 

    if arg is not None:
        result: str = func(arg)
        #print(f'{func.__name__}("{arg}") = {result}')
    else:
        result: str = func()
        #print(f'{func.__name__}() = {result}')

    end_time: float = time.perf_counter()

    #Print
    print(f'{func.__name__}() = {result}')
    print(f'\033[92mTotal time: {end_time - start_time:.4f}s\033[0m')
    return result