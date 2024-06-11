from collections import defaultdict, deque
from typing import List
import time


# Basic Bellman Ford, gives TLE
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # making edges bi-directional
        dist_prob = [float("-inf") for _ in range(n)]

        dist_prob[start_node] = 1

        for _ in range(n-1):
            for j in range(len(edges)):
                u, v, d = edges[j][0], edges[j][1], succProb[j]
                if dist_prob[u] != float("-inf") and dist_prob[u] * d > dist_prob[v]:
                    dist_prob[v] = dist_prob[u] * d
                if dist_prob[v] != float("-inf") and dist_prob[v] * d > dist_prob[u]:
                    dist_prob[u] = dist_prob[v] * d
        return dist_prob[end_node] if dist_prob[end_node] != float("-inf") else float(0)

    

    # for bigger edge case that gave TLE for above regular approach, this code solves it
    def maxProbability_BellmanFord_SPFA(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # SFPA Bellman Ford method
        dist_prob = [float("-inf") for _ in range(n)]

        adj = defaultdict(list)
        for i in range(len(edges)):
            u, v, d = edges[i][0], edges[i][1], succProb[i]
            # undirected graph
            adj[u].append([d, v])
            adj[v].append([d, u])

        q = deque([[1, start_node]])  # we use queue instead of iterative as in regular Bellman Ford
        dist_prob[start_node] = 1

        while q:
            w1, n1 = q.popleft()
            for w2, n2 in adj[n1]:
                newDist = dist_prob[n1] * w2
                if newDist > dist_prob[n2]:  # adding nodes to deque only if their probablity was greater than current value, we will ignore the edges that produce leser values. We will not even bother processing them like in Bellman Ford whhich processes all edges.
                    dist_prob[n2] = newDist
                    q.append([newDist, n2])
        
        return dist_prob[end_node] if dist_prob[end_node] != float("-inf") else float(0)


print(Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))
print(Solution().maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start_node = 0, end_node = 2))
print(Solution().maxProbability_BellmanFord_SPFA(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))
print(Solution().maxProbability_BellmanFord_SPFA(n = 3, edges = [[0,1]], succProb = [0.5], start_node = 0, end_node = 2))
