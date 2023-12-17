from typing import *
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(servers)
        taskHeap = []
        # heapq.heapify(taskHeap)  # no need to heapify! learnt newly
        time = 0
        res = []
        for index, task in enumerate(tasks):
            time = max(time, index)  # C1
            if len(servers) == 0:  # to fast forward to next time.
                time = taskHeap[0][0]  # C2
            while taskHeap and taskHeap[0][0] <= time:
                tn, w, i  = heapq.heappop(taskHeap)
                heapq.heappush(servers, (w, i))
            if servers:
                cur = heapq.heappop(servers)
                heapq.heappush(taskHeap, (time + task, cur[0], cur[1]))
                res.append(cur[1])
        return res


obj = Solution()
print(obj.assignTasks(servers = [1, 20, 300], tasks = [10, 9, 8, 1, 1, 1]))