from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append([w, v])  # adding weight first so it can be easily added to minHeap when we get the neighbours
        
        dist = [float("inf") for _ in range(n + 1)]
        visited = set()

        minHeap = [[0, k]]  # [weight, toNode] -> k is the given source node        
        dist[k] = 0
        heapq.heapify(minHeap)

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in visited:
                continue
            visited.add(n1)

            for w2, n2 in adj[n1]:
                if n2 in visited:
                    continue
                newDist = w1 + w2
                if newDist < dist[n2]:
                    dist[n2] = newDist
                    heapq.heappush(minHeap, [newDist, n2])
        # print(dist)

        for i in range(1, len(dist)):  # looping from 1 to n instead of 0 to n -> graph is from 1 to n and also 0th index has inf
            if dist[i] == float("inf"):  # some nodes are unreachable
                return -1

        return max(dist[1:])


print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))