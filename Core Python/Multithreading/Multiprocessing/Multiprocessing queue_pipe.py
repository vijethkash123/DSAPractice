import multiprocessing

def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)

if __name__ == "__main__":
    numbers = [2,3,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())

"""
multiprocessing.Queue() -> to create queue
q.empty() -> check if queue is empty
q.get() -> pop each item from queue front to get the result of calcuation that happened in the function called with multiprocessing
"""