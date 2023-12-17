import heapq
from typing import *

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        tasks = [[v[1], index, v[0]] for index, v in enumerate(tasks)]   # [processTime, index, enqueue time]
       
        tasks = sorted(tasks, key= lambda x:x[2])
        time = tasks[0][2]
        i = 0
        minHeap = []

        while minHeap or i < len(tasks):
            while i < len(tasks) and tasks[i][2] <= time:
                heapq.heappush(minHeap, [tasks[i][0],tasks[i][1]])
                i+=1
            
            if not minHeap:
                time = tasks[i][2]  # C1
            else:
                procTime, index = heapq.heappop(minHeap)
                time+=procTime
                res.append(index)

        return res

obj = Solution()
print(obj.getOrder(tasks=[[7,10],[7,12],[7,5],[7,4],[7,2]]))