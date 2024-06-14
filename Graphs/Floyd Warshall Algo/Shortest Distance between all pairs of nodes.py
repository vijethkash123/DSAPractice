class Solution:
    def FloydWarshallAPSP(self, V, edges):
        # create a initial cost matrix from edge[u, v, w], V -> Number of vertices
        matrix = [[float("inf") for _ in range(V)] for x in range(V)]
        
        for i in range(V):
            for j in range(V):
                if i == j:  # 0 distance from node to itself
                    matrix[i][j] = 0

        for u, v, w in edges:
            matrix[u][v] = w


        for k in range(V):  # via loop
            for i in range(V):
                for j in range(V):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        

        # To detect negative cycles
        for i in range(V):
            if matrix[i][i] < 0:
                print("Negative Cycle detected")
                return [[-1]]


        return matrix


print(Solution().FloydWarshallAPSP(V = 4, edges=[[0,1,2],[1,0,1],[3,0,3],[3,2,4],[3,1,5],[1,2,3]])) 
# Ans:
# [[0, 2, 5, inf], 
#  [1, 0, 3, inf], 
#  [inf, inf, 0, inf], 
#  [3, 5, 4, 0]]
print(Solution().FloydWarshallAPSP(V = 3, edges = [[0, 1, -1], [1, 2, -2], [2, 0, -3]]))  # negative cycle
