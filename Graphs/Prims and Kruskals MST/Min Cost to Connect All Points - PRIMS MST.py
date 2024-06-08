# LC: 1584 - Min Cost to Connect All Points - PRIM'S Algorithm approach
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        edges = []
        heapq.heappush(edges, (0, 0))
        toVisit = set([i for i in range(len(points))])
        
        mst_weight = 0

        # PRIM'S
        while edges:
            weight, node = heapq.heappop(edges)
            if node not in toVisit:
                continue
            toVisit.remove(node)
            mst_weight += weight
            for i in toVisit:
                heapq.heappush(edges, (manhattan(points[node], points[i]), i))
                    
        return mst_weight


print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))