from my_module import *

obj = MyClass()
obj2 = MyClass2() # AttributeError: module 'my_module' has no attribute 'MyClass2', as this was not included in __all__
# Accessing the private variable will raise an AttributeError
try:
    # print(obj._MyClass__private_var) # works
    print(obj.__private_var) # AttributeError: 'MyClass' object has no attribute '__private_var'
except AttributeError as e:
    print(e)  # 'MyClass' object has no attribute '__private_var'

# print(obj.__private_func()) # AttributeError: 'MyClass' object has no attribute '__private_func'
# print(obj._MyClass__private_func()) # works
# print(_private_func())
print(obj._protected_var)  # 43
print(obj._protected_func()) # works
print(obj.__private_func()) # AttributeError: 'MyClass' object has no attribute '__private_func'
