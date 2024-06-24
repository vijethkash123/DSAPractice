#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

from time import perf_counter, time

# Normal approach
start = time()
res = [0, 1]
maxx = 12
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        ans = fib(n-2) + fib(n-1)
        return ans


for i in range(12):
    ans = fib(i)
    print(ans)

print(time()- start)

# ----------------------------------------------------------------------------------------------- #

# DP approach - fast af boyyyyyyyyyyyyyy
start = time()
res = [0, 1]
maxx = 12
dp = [-1] * maxx
def fib(n):
    if dp[n] != -1:
        return dp[n]
    else:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            ans = fib(n-2) + fib(n-1)
            return ans


for i in range(maxx):
    ans = fib(i)
    dp[i] = ans
    # print(dp)

print(time()- start)


# Beautiful approach using generators:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

