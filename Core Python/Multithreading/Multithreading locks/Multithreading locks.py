import threading
import time

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(10000000):
        with lock:  # Use lock to ensure thread-safe increments
            counter += 1

# Create two threads that will both increment the counter
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

start = time.time()
# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Final counter value:", counter)
print(f"Time taken: {time.time() - start}")

"""
Locks ensure thread safety, only 1 thread is allowed to process the shared variable at a time. 
`with lock` acquires the lock updates the variable and then releases the lock, so the other threads cannot access the same shared variable at the same time.
"""


# Without threads - take more time

import time

counter = 0

def increment():
    global counter
    for _ in range(10000000):
        counter += 1

increment()

print("Final counter value:", counter)
print(f"Time taken: {time.time() - start}")