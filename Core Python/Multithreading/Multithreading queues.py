import threading
import queue
import time

# Create a thread-safe queue
q = queue.Queue()

def producer_even():
    for i in range(15):
        print(f"Producing {i}")
        if i % 2 == 0:
            q.put(i)  # Put items in the queue
        time.sleep(0.5)

def producer_odd():
    for i in range(15):
        print(f"Producing {i}")
        if i % 2 != 0:
            q.put(i)  # Put items in the queue
        time.sleep(0.5)


def consumer():
    res = []
    while True:
        item = q.get()  # Get items from the queue
        print(f"Consuming {item}")
        res.append(item)
        if item == 14:
            break
    return res



if __name__ == "__main__":
    
    # Create producer and consumer threads
    producer_even_thread = threading.Thread(target=producer_even)
    producer_odd_thread = threading.Thread(target=producer_odd)

    # Start the threads
    producer_even_thread.start()
    producer_odd_thread.start()

    # Wait for both threads to complete
    producer_even_thread.join()
    producer_odd_thread.join()

    res = consumer()
    print(res)



"""
The queue.Queue class in Python provides a thread-safe way to communicate between threads. It handles all the locking and synchronization internally, so you don't need to worry about race conditions when multiple threads access or modify shared data.

It is particularly useful when you have a producer-consumer pattern, where one or more threads (producers) generate data and put it into the queue, and one or more threads (consumers) retrieve the data from the queue and process it.

Queues are used to collect the result of all threads 
We use queue.put() to put the calculated results into queue from threads
Later to get all the computed results from the threads, we use queue.get()

Try commenting time.sleep() in both functions and we get different outputs each time.
Having time.sleep() is ensuring consistent context switching here - Not relevant to queues but added a point to note here
"""

# Another example where producer and consumer are called synchronously, because queue handles locking automatically

"""
import threading
import queue
import time

# Create a thread-safe queue
q = queue.Queue()

def producer():
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)  # Put items in the queue
        time.sleep(1)

def consumer():
    while True:
        item = q.get()  # Get items from the queue
        print(f"Consuming {item}")
        if item == 4:  # End the loop after consuming the last item
            break

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for both threads to complete
producer_thread.join()
consumer_thread.join()
"""