class Vijeth:
    print("Entered the class Vijeth")
    def f1(self):
        print("Entered f1()")
    def f2(self):
        print("Entered f2()")
    def f3(self):
        self.f1()
        self.f2()

if __name__ == "__main__":
    o=Vijeth()
    o.f3()

