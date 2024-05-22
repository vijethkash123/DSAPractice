# LC: 1584 - Min Cost to Connect All Points - KRUSKAL'S Algorithm approach

import heapq
from typing import List


class Solution:
    parent, size = [], []
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = self.manhattan_distance(points[i], points[j])
                heapq.heappush(edges, (dist, i, j)) # just maintaining i and j is enough

        self.parent = [i for i in range(len(points) + 1)]
        self.size = [1] * (len(points) + 1)

        mst_weight = 0
        mst_edges = 0

        while edges:
            w, u, v = heappop(edges)
            if self.union(u, v):
                mst_weight += w
                mst_edges += 1
                if mst_edges == len(points) - 1:  # definition of mst, n nodes, n-1 edges, as soon as we reach it, we can return and no need to process remaining
                    break
                    
        return mst_weight


    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.size[p1] > self.size[p2]:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        return True

    def find(self, n):
        p = n
        if p == self.parent[p]:
            return p
        else:
            self.parent[p] = self.find(self.parent[p])
            return self.parent[p]
    
    
    def manhattan_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
