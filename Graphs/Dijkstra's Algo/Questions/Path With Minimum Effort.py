# LC: 1631. Path With Minimum Effort
from collections import defaultdict
import heapq
from typing import List
import time

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # building adjacency list
        adj = defaultdict(list) # [from: [weight, to]]
        ni, nj = len(heights), len(heights[0])
        for i in range(ni):
            for j in range(nj):
                if i + 1 < ni:
                    weight = abs(heights[i+1][j] - heights[i][j])
                    adj[(i, j)].append([weight, (i + 1, j)])
                if j + 1 < nj:
                    weight = abs(heights[i][j+1] - heights[i][j])
                    adj[(i, j)].append([weight,  (i, j + 1)])
                if i - 1 >= 0:
                    weight = abs(heights[i-1][j] - heights[i][j])
                    adj[(i, j)].append([weight, (i - 1, j)])
                if j - 1 >= 0:
                    weight = abs(heights[i][j-1] - heights[i][j])
                    adj[(i, j)].append([weight,  (i, j - 1)])


        minHeap = [[0, (0, 0)]]
        heapq.heapify(minHeap)
        
        visited = set()
        minEffort = float("-inf")
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in visited:
                continue

            visited.add(n1)
            minEffort = max(w1, minEffort)  # minEffort is the max effort in shortest path, see example: [[1,10,6,7,9,10,4,9]], O/P: 9

            if n1 == (ni-1, nj-1):
                # print(visited)
                return minEffort


            for w2, n2 in adj[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(minHeap, [w2, n2])
        
        return minEffort

start = time.perf_counter()
print(Solution().minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]))
print(Solution().minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
print(Solution().minimumEffortPath(heights = [[1,10,6,7,9,10,4,9]]))
print(time.perf_counter() - start)



### Neetcode's approach:

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:      
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ni, nj = len(heights), len(heights[0])


        minHeap = [[0, (0, 0)]]
        heapq.heapify(minHeap)
        visited = set()
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)  # w1 is the maxCostAlongShortestPath
            
            if n1 in visited:  # important, without this optimization we can get TLE
                continue

            visited.add(n1)

            if n1 == (ni - 1, nj - 1):
                return w1

            i, j = n1[0], n1[1]
            for di, dj in directions:
                iT, jT = i + di, j + dj
                if iT < 0 or jT < 0 or iT == ni or jT == nj or (iT, jT) in visited:
                    continue
                maxCostAlongShortestPath = max(w1, abs(heights[i][j] - heights[iT][jT]))
                heapq.heappush(minHeap, [maxCostAlongShortestPath, (iT, jT)])

start = time.perf_counter()
print(Solution().minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]))
print(Solution().minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
print(Solution().minimumEffortPath(heights = [[1,10,6,7,9,10,4,9]]))
print(time.perf_counter() - start)
