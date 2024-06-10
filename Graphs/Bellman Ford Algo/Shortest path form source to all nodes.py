class Solution:
    '''
    V: number of vertices/ nodes in graph
    edges: adjacency list for the graph (u, v, weight/ dist)
    S: Source node
    '''
    def bellman_ford(self, V, edges, S):
        
        dist = [float("inf") for _ in range(V)]
        dist[S] = 0  # source node
        
        # Bellman Ford Algorithm - TC is V x E -> V = number of vertices and E = number of edges
        for _ in range(V-1):
            for u, v, d in edges:
                if dist[u] != float("inf") and dist[u] + d < dist[v]:
                    dist[v] = dist[u] + d
        
        # Detect negative cycle in Nth iteration. Only once
        for u, v, d in edges:
            if dist[u] != float("inf") and dist[u] + d < dist[v]:
                return [-1]

        return dist

# print(Solution().bellman_ford(V = 3, edges = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]], S = 2))
# print(Solution().bellman_ford(V = 2, edges = [[0,1,9]], S = 0))
print(Solution().bellman_ford(V = 4, edges=[[0,1,1], [1,2,1], [2,0,1], [2,3,1]], S = 0))  # Graph with positive cycle, shortest path still works
# Example 3 explanation:
# https://stackoverflow.com/questions/70681479/can-bellman-ford-algorithm-handle-positive-cycles