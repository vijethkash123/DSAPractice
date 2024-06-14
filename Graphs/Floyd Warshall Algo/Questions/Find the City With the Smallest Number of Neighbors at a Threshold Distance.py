from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # create a initial cost matrix from edge[u, v, w], n -> number of vertices
        matrix = [[float("inf") for _ in range(n)] for x in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == j:  # 0 distance from node to itself
                    matrix[i][j] = 0

        for u, v, w in edges:
            matrix[u][v] = w
            matrix[v][u] = w  # undirected


        # Floyd Warshall Algorithm
        for k in range(n):  # via loop
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        

        # now all this circus to calculate JUST the last index of city with least number of reachable cities
        res = [0] * (n)
        for i in range(n):
            for j in range(n):
                if i != j and matrix[i][j] != float("inf") and matrix[i][j] <= distanceThreshold:
                    res[i] += 1
        
        # return last min index
        mmin = min(res)
        ans = 0
        for i, v in enumerate(res):
            if v == mmin:
                ans = i
        return ans

print(Solution().findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
