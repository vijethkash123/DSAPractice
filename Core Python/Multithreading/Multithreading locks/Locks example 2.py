import threading
import time


def first_person():
    with lock:
        print("Person 1 has acquired the meeting room")
        time.sleep(0.5)
        print("Person 1 has released meeting room")

def second_person():
    lock.acquire()
    print("Person 2 has acquired the meeting room")
    time.sleep(0.5)
    print("Person 2 has released meeting room")
    lock.release


lock = threading.Lock()
thread1 = threading.Thread(target=first_person)
thread2 = threading.Thread(target=second_person)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


print("----------------------------------------------")
# without

def first_person():
    print("Person 1 has acquired the meeting room")
    time.sleep(0.5)
    print("Person 1 has released meeting room")

def second_person():
    print("Person 2 has acquired the meeting room")
    time.sleep(0.5)
    print("Person 2 has released meeting room")


lock = threading.Lock()
thread1 = threading.Thread(target=first_person)
thread2 = threading.Thread(target=second_person)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

"""
Person 1 has acquired the meeting room
Person 2 has acquired the meeting room
Person 1 has released meeting room
Person 2 has released meeting room
"""