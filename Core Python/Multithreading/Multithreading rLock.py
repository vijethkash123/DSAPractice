import threading

# Create an RLock
rlock = threading.RLock()  # change it to normal lock and deadlock happens

def recursive_function(n):
    rlock.acquire()
    print(f"Acquired lock in recursive call {n}")
    if n > 0:
        recursive_function(n - 1)
    rlock.release()

# Start a thread that will call the recursive function
thread = threading.Thread(target=recursive_function, args=(3,))
thread.start()
thread.join()

"""
An RLock (reentrant lock) can be acquired multiple times by the same thread without causing a deadlock. 
This is useful in scenarios where a thread needs to acquire the same lock multiple times, such as in recursive functions
or when one lock-acquiring function calls another lock-acquiring function.

In the above code, the same thread acquires the rlock multiple times as it makes recursive calls. 
Without an RLock, this would cause a deadlock as a thread cannot acquire a normal lock it already holds. 
With RLock, the same thread can repeatedly acquire and release the lock without issues.
"""