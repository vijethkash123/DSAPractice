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



'''
In car pooling problem, also noticed, while popping it also sorts by second element, see output below
I had solved by sorting only by first element, so when passengers drop, i was not subtracting the count of 
passengers before adding new passengers after picking up, because i was sorting by keeping the 
first element as key like this, which was wrong:
trips.sort(key = lambda x:x[0]) -> wrong
just doing trips.sort() is enough, because it will also sort 2nd element
'''
import heapq
trips = [[3, 4], [3, 2], [4, 6], [5, 4], [5, -4], [5, -2], [6, -4], [7, -6]]

heapq.heapify(trips)

while trips:
    print(heapq.heappop(trips))

'''
Output:
for heappop() and trips.sort() are same
[3, 2]
[3, 4]
[4, 6]
[5, -4]
[5, -2]
[5, 4]
[6, -4]
[7, -6]
'''

'''
Output for trips.sort(key = lambda x:x[0]):
[[3, 4], [3, 2], [4, 6], [5, 4], [5, -4], [5, -2], [6, -4], [7, -6]]

Notice, the negative appears after the positive (picking up before drop) -> which we donot want.
'''