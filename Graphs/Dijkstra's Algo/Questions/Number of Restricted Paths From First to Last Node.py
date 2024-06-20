from collections import defaultdict
import heapq
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        # print(sys.maxsize)
        for u, v, w in edges:
            adj[u].append([w, v])
            adj[v].append([w, u])

        distanceToLastNode = self.dijkstra(n, adj) 
        # print(distanceToLastNode)

        dp = [-1] * (n+1)
        def dfs(node):
            if dp[node] != -1:
                return dp[node]
            if node == n:
                return 1
            res = 0
            for _, nei in adj[node]:
                if distanceToLastNode[nei] < distanceToLastNode[node]:
                    res = (res + dfs(nei)) % (10**9+7)
            dp[node] = res
            return res

        res = dfs(1)
        # print(res, res%(10**9+7))
        return res


    def dijkstra(self, n, adj):
        dist = {i: float("inf") for i in range(1, n+1)}
        minHeap = [[0, n]]  # initializing with 0 dist for source node - source node is last node, we calculate shortest dist from n to all other nodes.
        heapq.heapify(minHeap)
        dist[n] = 0

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
                if newDist < dist[n2]:
                    dist[n2] = newDist
                    heapq.heappush(minHeap, [newDist, n2])
                
        return dist



print(Solution().countRestrictedPaths(n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]))

print(Solution().countRestrictedPaths(n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]))

