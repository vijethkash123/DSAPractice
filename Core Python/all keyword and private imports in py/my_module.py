# mymodule.py
__all__ = ['MyClass']

    
class MyClass:

    def __init__(self):
        self.__private_var = 42
        self._protected_var = 43

    def get_private_var(self):
        return self.__private_var

    def __private_func(self):
        return "private function"
    
    def _protected_func(self):
        return "protected function"

class MyClass2:
    pass