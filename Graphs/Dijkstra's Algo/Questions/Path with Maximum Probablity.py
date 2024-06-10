from collections import defaultdict
import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dist_prob = [float("-inf") for _ in range(n)]
        dist_prob[start_node] = 1

        adj = defaultdict(list)
        for i in range(len(edges)):
            u, v, d = edges[i][0], edges[i][1], succProb[i]
            # undirected graph
            adj[u].append([-d, v])
            adj[v].append([-d, u])

        visited = set()

        minHeap = [(1, start_node)]
        heapq.heapify(minHeap)
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)

            for w2, n2 in adj[n1]:
                if n2 in visited:
                    continue
                newDist = (abs(w1) * abs(w2))
                if newDist > dist_prob[n2]:
                    dist_prob[n2] = newDist
                    heapq.heappush(minHeap, [-newDist, n2])
        
        return dist_prob[end_node] if dist_prob[end_node] != float("-inf") else float(0)

print(Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))
print(Solution().maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start_node = 0, end_node = 2))
