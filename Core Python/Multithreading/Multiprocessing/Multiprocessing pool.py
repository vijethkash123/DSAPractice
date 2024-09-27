from multiprocessing import Pool
import os


def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3)
    result = p.map(f,[1,2,3,4,5])
    print(list(result))
    

# also see another example from ArjanCodes added under GIL section in Notion notes!
