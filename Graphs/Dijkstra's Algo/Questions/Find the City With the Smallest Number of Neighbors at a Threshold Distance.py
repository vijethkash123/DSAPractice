from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for u, v, d in edges:
            adj[u].append([d, v])
            adj[v].append([d, u])
        
        res = []
        for cur in range(0, n):
            dist = {i: float("inf") for i in range(n)}
            dist[cur] = 0

            minHeap = [[0, cur]]
            heapq.heapify(minHeap)
            visited = set()

            while minHeap:
                w1, n1 = heapq.heappop(minHeap)
                if n1 in visited:
                    continue
                visited.add(n1)

                for w2, n2 in adj[n1]:
                    if n2 in visited:
                        continue
                    newDist = w1 + w2
                    if newDist < dist[n2] and newDist <= distanceThreshold:
                        dist[n2] = newDist
                        heapq.heappush(minHeap, [newDist, n2])
            res.append(dist)

        # Now all this circus to calculate JUST the last index of city with least number of reachable cities
        ans = 0
        for i, dist in enumerate(res):
            temp = 0
            for k,v in dist.items():
                if k != i and v <= distanceThreshold:
                    temp += 1
            res[i] = temp
        
        item = min(res)
        while True:
            if item in res:
                ans = res.index(item)
                res[ans] = -1
            else:
                return ans

print(Solution().findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))