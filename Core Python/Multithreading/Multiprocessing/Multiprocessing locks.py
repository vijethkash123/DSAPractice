import time
import multiprocessing


def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:  # we can also use syntax like this instead of manually specifying lock.acquire() and lock.release()
            balance.value = balance.value + 1

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance,lock))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)

"""
# Without locks - produces inconsistent outputs when run, different output at different runs because of race conditions

import time
import multiprocessing

def deposit(balance):
    for i in range(100):
        time.sleep(0.01)  # added to introduce wait time, so context switching can happen
        balance.value = balance.value + 1

def withdraw(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value - 1

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    d = multiprocessing.Process(target=deposit, args=(balance,))
    w = multiprocessing.Process(target=withdraw, args=(balance,))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)
"""