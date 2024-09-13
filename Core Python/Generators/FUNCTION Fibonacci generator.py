def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

f = fibonacci(10)

print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())