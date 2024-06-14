from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create a initial cost matrix from edge[u, v, w], n -> Number of vertices
        matrix = [[float("inf") for _ in range(n+1)] for x in range(n+1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:  # 0 distance from node to itself
                    matrix[i][j] = 0


        for u, v, w in times:
            matrix[u][v] = w  # directed, one is enough

        # Floyd Warshall Algo
        for z in range(1, n+1):  # via loop
            for i in range(1, n+1):
                for j in range(1, n+1):
                    matrix[i][j] = min(matrix[i][j], matrix[i][z] + matrix[z][j])

        print(matrix)
        ans = max(matrix[k][1:])
        return ans if ans != float("inf") else -1

print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))