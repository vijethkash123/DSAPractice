print("-----------------------------------------------------------------------------------")

tup1 = ([1,2,3,4,5], 34.34)
tup2 = (1,2,3,4,5,34.34)

def delete_element(tup):
    try:
        del tup[0][1]
    except:
        print("TypeError")
    else:
        print("Deletion successful")
    
delete_element(tup1)
delete_element(tup2)
print(tup2[3])

"""
Tuples are immutable, they can be accessed via index, but single items cannot be deleted
"""

print("-----------------------------------------------------------------------------------")

sset = set([0,1,2,3])
try:
    del sset[0]
except:
    print("Cannot delete")
    print(sset)

try:
    sset.remove(3)
except:
    print("Cannot delete")
else:
    print(f"Deletion successful: {sset}")


print("-----------------------------------------------------------------------------------")

sset = set([0,1,2,3])
try:
    print(sset[0])
except:
    print("Cannot call using index")
    print(sset)

"""
Sets are mutable, meaning you can add or remove elements from them after creation.
The elements within a set must be immutable. This means you can have integers, floats, strings, or tuples in a set, 
but not lists or dictionaries.
Sets are unordered, so you can't access elements by index.

"""
print("-----------------------------------------------------------------------------------")

def number(x):
    def sub(y):
        print(x - y)
    return sub

res=number(100)
res(50)


res=number(40)
res(70)

print("-----------------------------------------------------------------------------------")

class OOPS:
    def __init__(self):
        self.m = 10
        self.__n = 20
    def output(self):
        return self.__n

obj1 = OOPS()
print(obj1.m)
print(obj1.output())

print("-----------------------------------------------------------------------------------")

import re
text1="India iS My country"
text2="Jndia is my country"

def text_validator(func):
    def wrapper(*args):
        text=func(*args)
        print(text)
        # print(re.findall('[A-Z]', text))
        if re.findall(r"\d", text):  # digits
            return False
        elif "I" not in re.findall('[A-Z]', text):  # uppercase letters
            return False
    return wrapper

@text_validator
def content_generator(text):
    return text

if content_generator (text1)==False:
    print("Invalid Text")
else:
    print("Valid Text")

if content_generator (text2)==False:
    print("Invalid Text")
else:
    print("Valid Text")

print("-----------------------------------------------------------------------------------")

import re
input_str="7 Wonders of the World"
for i in range(len(input_str[0])):
    a = re.findall(r'\A[0-9]\s', input_str)  # \A starting, [0-9] or \d for digit - only 1 we don't have * after this, \s for space
    b = re.findall(r'W[a-zA-Z0-9]*d', input_str)  # W - words starting with W, any characters/ numbers between (*), ending with d
else:
    print(a, "\n",b)

"""
a = re.findall(r'\A[0-9]\s', input_str)
This line searches for a pattern at the beginning of the string.
\A: Matches the start of the string
[0-9]: Matches any single digit from 0 to 9
\s: Matches any whitespace character (space, tab, newline, etc.)
So, this regex looks for a single digit followed by a whitespace character at the very beginning of the string.
In the given input "7 Wonders of the World", it will match "7 ".
b = re.findall(r'W[a-zA-Z0-9]*d', input_str)
This line searches for a pattern anywhere in the string.
W: Matches the literal character 'W'
[a-zA-Z0-9]*: Matches zero or more occurrences of any lowercase letter, uppercase letter, or digit
d: Matches the literal character 'd'
So, this regex looks for patterns that start with 'W', followed by any number of alphanumeric characters, and end with 'd'.
In the given input "7 Wonders of the World", it will match "World".
"""

print("-----------------------------------------------------------------------------------")

import random
import string
def generate_password():
    characters = string.ascii_letters + string.digits
    # print(characters)
    password = ''

    for _ in range(8):
        password += random.choice(characters)
    return password

print(generate_password())

print("-----------------------------------------------------------------------------------")

import threading
import time
def thread1(num):
    print("First thread value : {}".format(num))
    time.sleep(2)
def thread2(num):
    print("Second thread value : {}".format(num))

t1 = threading.Thread(target=thread1 , args=(100,))
t2 = threading.Thread (target=thread2, args=(50,))

t1.start()
t2.start()


print("-----------------------------------------------------------------------------------")

import threading
import time
def thread1(num):
    time.sleep(0.2)
    print("First thread value : {}".format(num))
def thread2(num):
    print("Second thread value : {}".format(num))

t3 = threading.Thread(target=thread1 , args=(100,))
t4 = threading.Thread (target=thread2, args=(50,))

t3.start()
t4.start()

t3.join()
t4.join()
# adding join so that next print happens after both are executed
print("-----------------------------------------------------------------------------------")

