'''
NOTE: just heapify'ing it win't make it sorted.
Only when you pop, heap runs a bubbling operation, so it returns elements in sorted order.
See this example, that Observed during **Design Twitter** problem.

Heapifying test didn't make it sorted, but while popping it, it returns in sorted order.
[[-9, 1, 333], [-8, 1, 505], [-6, 1, 2], [-7, 1, 94], [-3, 1, 101], [-2, 1, 3], [-5, 1, 10], [-4, 1, 13]] -> Heapify
Pop 👇🏼
[-9, 1, 333]
[-8, 1, 505]
[-7, 1, 94]
[-6, 1, 2]
[-5, 1, 10]
[-4, 1, 13]
[-3, 1, 101]
[-2, 1, 3]
'''

# Check K-closest points to origin and Design Twitter Problem

import heapq

test = [[-9, 1, 333], [-8, 1, 505], [-6,1,  2], [-7, 1, 94], [-3, 1, 101], [-2, 1, 3], [-5,  1,10], [-4, 1, 13]]  

heapq.heapify(test)
print(test)

test = sorted(test, key= lambda x:x[0])
print(test)

while test:
    print(heapq.heappop(test))
