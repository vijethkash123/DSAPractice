price = [100, 80, 60, 70, 60, 70, 85]

res = []
stack = [] # [(price, consecutive count of elements lesser than it)]
for i in price:
    count = 1
    while stack and i >= stack[-1][0]:
        ele, prev_count = stack.pop()
        count += prev_count
    stack.append((i, count))
    res.append(count)

print(res)