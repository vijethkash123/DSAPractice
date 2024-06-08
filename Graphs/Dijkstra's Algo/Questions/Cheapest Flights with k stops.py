from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf") for _ in range(n)]
        
        adj = defaultdict(list)
        for u, v, weight in flights:
            adj[u].append([weight, v])

        minHeap = [[0, 0, src]]  # [stops, cost, node]
        dist[src] = 0

        while minHeap:
            stops, w1, n1 = heapq.heappop(minHeap)

            for w2, n2 in adj[n1]:
                newDist = w1 + w2
                if stops + 1 <= k + 1 and newDist < dist[n2]:
                    dist[n2] = newDist
                    heapq.heappush(minHeap, [stops + 1, newDist, n2])
        

        return -1 if dist[dst] == float("inf") else dist[dst]


print(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))