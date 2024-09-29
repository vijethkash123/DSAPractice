from multiprocessing import Pool
import os


def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3)
    result = p.map(f,[1,2,3,4,5])
    print(list(result))
    

# also see another example from ArjanCodes added under GIL section in Notion notes!
"""
Pool(processors = n) -> to create Pool with n processes
Pool.map(function_name, input) -> 
The map method of the pool is called: result = p.map(f,[1,2,3,4,5]). 
This does the following:
It applies the function f to each element in the list [1,2,3,4,5].
The work is distributed among the 3 worker processes.
Each process will compute some of the results in parallel.
"""