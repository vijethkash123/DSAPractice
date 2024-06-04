from collections import defaultdict
import heapq


class Solution:

    # Function to find the shortest distance of all the vertices from the source vertex S.
    def dijkstra(V, adj, S):
        dist = [float("inf") for i in range(V)]
        minHeap = [[0, S]]  # S is source vertex
        heapq.heapify(minHeap)  # [weight, edge]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if dist[n1] != float("inf"):   # visited
                continue
            dist[n1] = w1  # adding distance
            for w2, n2 in adj[n1]:
                if dist[n2] == float("inf"):  # unvisited
                    heapq.heappush(minHeap, [w1 + w2, n2])
        
        for i in range(V):
            if dist[i] == float("inf"):  # unreachble to graph/ disconnected node
                dist[i] = -1
        return dist

print(Solution.dijkstra(V = 3, adj = {0: [[1, 1], [6, 2]], 1: [[3, 2], [1, 0]], 2: [[3, 1], [6, 0]]}, S = 2))  # undirected
print(Solution.dijkstra(V = 3, adj = {0: [[4, 1], [1, 2]], 1: [] , 2: [[2, 1]]}, S = 0))   # directed
print(Solution.dijkstra(V = 4, adj = {0: [[7, 1], [4, 2]], 1: [] , 2: [[4, 1], [1, 3]], 3:[[1, 1]]}, S = 0))  # directed



# Optimized version
class Solution:

    # Function to find the shortest distance of all the vertices from the source vertex S.
    def dijkstra(V, adj, S):
        dist = [float("inf") for i in range(V)]
        dist[S] = 0

        minHeap = [[0, S]]  # S is source vertex
        heapq.heapify(minHeap)  # [weight, edge]
        visited = set()

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            visited.add(n1)  # remember to add visited here and not in for loop, because we want to mark it visited when we have greedily picked the path with least cost i.e shortest path

            if dist[n1] < w1:  # optimization to ignore stale nodes which were added previously before we found shortest path
                continue

            for w2, n2 in adj[n1]:
                if n2 in visited:
                    continue
                newDist = w1 + w2
                if newDist < dist[n2]:
                    dist[n2] = newDist
                    heapq.heappush(minHeap, [newDist, n2])
        
        for i in range(V):
            if dist[i] == float("inf"):  # unreachble to graph/ disconnected node
                dist[i] = -1
        return dist

print(Solution.dijkstra(V = 3, adj = {0: [[1, 1], [6, 2]], 1: [[3, 2], [1, 0]], 2: [[3, 1], [6, 0]]}, S = 2))  # undirected
print(Solution.dijkstra(V = 3, adj = {0: [[4, 1], [1, 2]], 1: [] , 2: [[2, 1]]}, S = 0))   # directed
print(Solution.dijkstra(V = 4, adj = {0: [[7, 1], [4, 2]], 1: [] , 2: [[4, 1], [1, 3]], 3:[[1, 1]]}, S = 0))  # directed
