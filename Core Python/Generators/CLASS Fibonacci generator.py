class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration

        if self.count == 0 or self.count == 1:
            result = self.count
        else:
            result = self.a + self.b
            self.a, self.b = self.b, result

        self.count += 1
        return result


n = 10
fibonacci = FibonacciIterator(n)
first_fibonacci = fibonacci.__next__()
print(first_fibonacci)

# for num in fibonacci:
#     print(num, end=' ')