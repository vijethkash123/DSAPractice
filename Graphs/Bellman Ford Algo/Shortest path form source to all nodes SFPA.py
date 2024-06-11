from collections import defaultdict, deque
import time


class Solution:
    '''
    V: number of vertices/ nodes in graph
    edges: adjacency list for the graph (u, v, weight/ dist)
    S: Source node
    '''
    def bellman_ford_SFPA(self, V, edges, S):
        # Shortest path Fast Algorithm Bellman Ford
        dist = [float("inf") for _ in range(V)]
        dist[S] = 0  # source node
        cnt = [0 for i in range(V)]

        adj = defaultdict(list)
        for u, v, d in edges:
            adj[u].append([d, v])
            # adj[v].append([d, u])  If undirected also add this
        
        q = deque([[0, S]])  # [weight, node]
        while q:
            w1, n1 = q.popleft()

            for w2, n2 in adj[n1]:
                newDist = dist[n1] + w2
                if newDist < dist[n2]:  # Bellman Ford part here, we use previously relaxed edges to calculate shortest distance for new edge
                    dist[n2] = newDist
                    q.append([newDist, n2])  # only add to queue in case where the if condition is true - C1
                    cnt[n2] += 1
                    
                    # to detect negative cycles
                    if cnt[n2] > V:
                        return -1
        
        return dist


start = time.perf_counter()
print(Solution().bellman_ford_SFPA(V = 3, edges = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]], S = 2))
print(Solution().bellman_ford_SFPA(V = 2, edges = [[0,1,9]], S = 0))
print(Solution().bellman_ford_SFPA(V = 4, edges=[[0,1,1], [1,2,1], [2,0,1], [2,3,1]], S = 0))  # Graph with positive cycle, shortest path still works
# Example 3 explanation:
# https://stackoverflow.com/questions/70681479/can-bellman-ford-algorithm-handle-positive-cycles
print(Solution().bellman_ford_SFPA(V = 3, edges = [[0, 1, -1], [1, 2, -2], [2, 0, -3]], S = 0)) # negative cycle
# C1 - # adding nodes to deque only if their cost/ dist was lesser than current value, we will ignore the edges that have greater values. We will not even bother processing them like in Bellman Ford whhich processes all edges.
# If you have doubt why add node to queue after we found max probability of that node? That's how all shortest path algos work, using this node, we will find shortest path to other upcoming nodes, right? :) Because what you found was shortest path till that node, next using that we will continue finding shortest path further.
print(time.perf_counter() - start)

