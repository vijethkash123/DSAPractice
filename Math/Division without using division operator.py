a, b = 17, 2  # a / b
ans = 0
while a >= b:
    a -= b
    ans += 1

print(ans)