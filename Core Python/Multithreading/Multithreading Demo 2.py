import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(1)
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(1)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()

t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
"""
Without threading everything would execute in linear order.
when the first thread is waiting, the other thread takes up the processing and starts 
executing that's why the output looks like this:

calculate square numbers
calculate cube of numbers
cube: 8
square: 4
cube: 27
square: 9
cube: 512
square: 64
cube: 729
square: 81
done in :  4.005697250366211
Hah... I am done with all my work now!
"""