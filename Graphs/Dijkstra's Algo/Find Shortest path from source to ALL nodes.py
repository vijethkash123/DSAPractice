from collections import defaultdict
import heapq


class Solution:

    # Function to find the shortest distance of all the vertices from the source vertex S.
    def dijkstra(V, adj, S):
        dist = [float("inf") for i in range(V)]
        # Building cusAdj here -> beacuse what I am building is simpler to process. Input adj format adj[0] = [[1, 1], [2, 6]] means 0 has 2 edges 0-1 with cost 1 and 0-2 with cost 6
        cusAdj = defaultdict(list)
        for i in range(len(adj)):
            for edge, weight in adj[i]:
                cusAdj[i].append([weight, edge])  # adding weight here so when we get neighbors we can add to minHeap and have access to weights :)

        
        minHeap = [[0, S]]  # S is source vertex
        heapq.heapify(minHeap)  # [weight, edge]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if dist[n1] != float("inf"):   # visited
                continue
            dist[n1] = w1  # adding distance
            for w2, n2 in cusAdj[n1]:
                if dist[n2] == float("inf"):  # unvisited - C1
                    heapq.heappush(minHeap, [w1 + w2, n2])
        
        for i in range(V):
            if dist[i] == float("inf"):  # unreachble to graph/ disconnected node
                dist[i] = -1
        return dist

print(Solution.dijkstra(V = 3, adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], S = 2))

'''
C1: We are doing greedy BFS → So, we don’t have to update dist[i] again in case thinking shortest path may come later. As we are doing BFS with popping least weight from minHeap at each step, the first time we visit it, we will be shortest path
'''