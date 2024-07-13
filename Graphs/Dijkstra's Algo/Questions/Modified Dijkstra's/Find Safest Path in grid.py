from collections import deque
import heapq
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # create distance matrix using multi-source BFS
        ni = len(grid)
        nj = len(grid[0])
        if grid[ni - 1][nj - 1] == 1 or grid[0][0] == 1:
            return 0

        dist = [[-1 for i in range(ni)] for j in range(nj)]
        thieves = []
        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for i in range(ni):
            for j in range(nj):
                if grid[i][j] == 1:
                    thieves.append((i, j))
                    q.append((i, j))  # (i, j)

        curDist = -1
        while q:
            curDist += 1
            for _ in range(len(q)):  # Important part in multisource BFS, so that we calculate dist properly
                i, j = q.popleft()
                if dist[i][j] != -1:
                    continue
                
                dist[i][j] = curDist  # we can use dist itself to track visited

                for di, dj in directions:
                    iT, jT = i + di, j + dj
                    if iT in range(ni) and jT in range(nj) and dist[iT][jT] == -1:
                        q.append((iT, jT))

        print(dist)
        # calculate the minimum safeness factor along the way from (0, 0) to (n-1, n-1)
        # at each cell, pick the min safeness value till we reach (n-1, n-1) asminimum value is the safeness factor of the grid
        maxHeap = [(-dist[0][0], 0, 0)]
        heapq.heapify(maxHeap) # (max along the way, i, j). Using negative to implement maxHeap
        visited = set()
        
        while maxHeap:
            d, i, j = heapq.heappop(maxHeap)
            d = -d  # as we are dealing with maxHeap
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == ni - 1 and j == nj - 1:
                return d

            for di, dj in directions:
                iT, jT = i + di, j + dj
                if iT in range(ni) and jT in range(nj) and (iT, jT) not in visited:
                    newDist = min(d, dist[iT][jT])
                    heapq.heappush(maxHeap, (-newDist, iT, jT))


print(Solution().maximumSafenessFactor(grid = [[0,0,1],[0,0,0],[0,0,0]]))



