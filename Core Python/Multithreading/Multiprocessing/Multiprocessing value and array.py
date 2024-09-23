import multiprocessing

def calc_square(numbers, result, v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        result[idx] = n*n

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('i',3)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))

    p.start()
    p.join()
    print(result[:])
    print(v.value)

"""
calc_square runs in separate process, so result is not returned after calculation. So in order to share data between 2 processes, we have to make use of IPC - 
interprocess communication techniques.
To share a list, we use Array and to share a value we use value
i -> integer, d -> double
"""