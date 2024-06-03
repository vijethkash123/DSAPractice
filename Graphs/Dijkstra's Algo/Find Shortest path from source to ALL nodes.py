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

print(Solution.dijkstra(V = 3, adj = {0: [[1, 1], [6, 2]], 1: [[3, 2], [1, 0]], 2: [[3, 1], [6, 0]]}, S = 2))
