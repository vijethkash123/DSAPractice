'''BASICS'''

'''
heappush(heap, ele): This function is used to insert the element mentioned in its arguments into a heap. The order is adjusted, so that heap structure is maintained.
heappop(heap): This function is used to remove and return the smallest element from the heap. The order is adjusted, so that heap structure is maintained.

By default heapq gives us minHeap
To get maxHeap we convert list of numbers to negative nums and then use heapify to get maxHeap. See Last Stone weight problem

Complexity of all operations on Heapify functions python:
Max Heap, which will take O(n + k.log(n)) 
where n -> for converting list to Heap
k-> popping k times from maxHeap, and each pop in Heap takes log(n) time, and popping k elements take O((n-k) log(n)) time, with n total elements
So, it's O(n+k.log(n))
So, if k is small, it will be better than O(n.log(n)) solution
https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library#:~:text=The%20complexity%20is%20O(n,O(n%20log%20n).
'''
import heapq

nums = [2,7,4,1,8,1]
nums = [-i for  i in nums]
heapq.heapify(nums)

while nums:
    print(heapq.heappop(nums))

'''
Output:
-8
-7
-4
-2
-1
-1
'''


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