'''
We solve it using MaxHeap + Queue
**MaxHeap**:
Idea is to use the most frequent element first to get the quickest time otherwise the most occurring element would remind and we have to wait in the idle time for the same task as all the others would be already processed.
So we use the MaxHeap to keep most frequent element first and easy yo perform push and pop in MaxHeap.

**Queue**:
Usage of queue is to keep track of the time untill we can reuse the same character/ same task
'''
from typing import *
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = Counter(tasks)  # To convert to dict with item count.
        maxHeap = [-t for t in tasks.values()]  # Using Negative values to be converted to MaxHeap
        heapq.heapify(maxHeap)  # Creating MaxHeap
        
        # print(maxHeap)
        q = deque()  # This is to keep track of time untill we can re run the task with same name again; [[taskCount, timeToCallNext]]
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # Actually a subtraction, but doing + as we store negatvie number in MinHeap to make it MaxHeap
                if cnt:  # not equal to 0: task still to be processed
                    q.append([cnt, time + n])

            if q and q[0][1] == time:  # Can process next task in queue. Note that if the time is lesser than the first task in queue, we will not do anything, that will suffice the idle time calculation.
                heapq.heappush(maxHeap, q.popleft()[0])  # Add back the task in queue to maxHeap to be processed
        return time

obj = Solution()
print(obj.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))