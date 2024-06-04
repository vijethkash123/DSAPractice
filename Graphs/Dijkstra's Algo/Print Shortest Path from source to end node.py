from collections import defaultdict
import heapq


class Solution:

    def dijkstra(self, V, adj, S):
        dist = [float("inf") for _ in range(V)]
        prev = [None for _ in range(V)]   # To keep track of Shortest path from source S to end node
        minHeap = [[0, S]]
        dist[S] = 0

        heapq.heapify(minHeap)
        visited = set()

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            visited.add(n1)

            if dist[n1] < w1:  # optimization to ignore stale nodes which were added previously before we found shortest path
                continue

            for w2, n2 in adj[n1]:
                if n2 in visited:  # We already got the shortest path
                    continue
                newDist = w1 + w2
                if newDist < dist[n2]:  # we add to dist using neighbors n2 and not n1 
                    dist[n2] = newDist
                    prev[n2] = n1  #  updates as we find shorter path
                    heapq.heappush(minHeap, [newDist, n2])
        
        for i in range(V):
            if dist[i] == float("inf"):  # unreachble to graph/ disconnected node
                dist[i] = -1
        return dist, prev

    def printPath(self, V, adj, S):
        dist, prev = self.dijkstra(V, adj, S)
        
        endNode = V - 1  # 0 to n
        path = []  # we will construct this using prev now


        if dist[endNode] == float("inf"): # means we were not able to reach end node from the start node
            return []

        # reconstruction of path using prev
        i = endNode
        while i != None:  # loop untill we get to start node, NOTE: Start node's prev is always Null, we iterate in reverse from endNode to prevNode
            path.append(i)
            i = prev[i]

        path = path[::-1]
        return path

print(Solution().printPath(V = 4, adj = {0: [[7, 1], [4, 2]], 1: [] , 2: [[4, 1], [1, 3]], 3:[[1, 1]]}, S = 0))  # directed
print(Solution().printPath(V = 3, adj = {0: [[4, 1], [1, 2]], 1: [] , 2: [[2, 1]]}, S = 0))   # directed
print(Solution().printPath(V = 3, adj = {0: [[1, 1], [6, 2]], 1: [[3, 2], [1, 0]], 2: [[3, 1], [6, 0]]}, S = 0))  # undirected - NOTE: In case of undirected, make sure to add paths in both directions in adj! Noticed a test case fialed for not doing this in GFG.

