from collections import defaultdict, deque
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {i: float("inf") for i in range(1, n+1)}
        dist[k] = 0

        for _ in range(n-1): # n-1 = V-1
            for u, v, wei in times:
                if dist[u] != float("inf") and dist[u] + wei < dist[v]:
                    dist[v] = dist[u] + wei

        ans = max(dist.values())
        return ans if ans != float("inf") else -1



# Bellman Ford SPFA approach
    def networkDelayTimeSPFA(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {i: float("inf") for i in range(1, n+1)}
        dist[k] = 0
        adj = defaultdict(list)
        for u, v, d in times:
            adj[u].append((d, v))
        
        q = deque([[0, k]])
        while q:
            w1, n1 = q.popleft()

            for w2, n2 in adj[n1]:
                newDist = dist[n1] + w2
                if newDist < dist[n2]:
                    dist[n2] = newDist
                    q.append([newDist, n2])

        ans = max(dist.values())
        return ans if ans != float("inf") else -1


print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(Solution().networkDelayTimeSPFA(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))