from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
            dist = [float("inf") for _ in range(n)]
            temp = [float("inf") for _ in range(n)]
            
            dist[src] = 0
            temp[src] = 0  # BFS each layer, +1 stop each time

            for _ in range(k + 1):
                for u, v, d in flights:
                    if dist[u] != float("inf") and dist[u] + d < temp[v]:  # C1 - Comparing with temp[v] and not dist[v] because with the same number of stops if there's a better path in the current layer more than once, we have to update it in the same stop's iteration !
                        temp[v] = dist[u] + d  # Note addind dist[u] + d not temp[u] + d
                dist = temp.copy()  # Using copy is important, otherwise it will just copy the reference!

            return -1 if dist[dst] == float("inf") else dist[dst]


print(Solution().findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
print(Solution().findCheapestPrice(n=4, flights=[[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src=0, dst=3, k=1))