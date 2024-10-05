"""
Defining context managers using contextlib.contextmanager
"""


from contextlib import contextmanager

@contextmanager
def MyContextMan(name, mode):
    print(f"Setup, {name}")
    f = open(name, mode)

    yield f
    f.close


with MyContextMan("scratch 2.py", "r") as McM:
    # print(McM)
    print(McM.read())
    print("Process")


print("------------------------------------")

"""
Manual definition of custom Context Managers
"""

class MCM:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print("Started db connection")
        self.connection = "test"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):  
        print("Closing connection")
        self.connection = None
        return False


with MCM("db_vij") as db:
    print(db)