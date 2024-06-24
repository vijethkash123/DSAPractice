import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ni, nj = len(grid), len(grid[0])
        minHeap = ([[grid[0][0], 0, 0]]) # [max_val, i, j]

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heapq.heapify(minHeap)

        visited = set()
        while minHeap:
            v, i, j = heapq.heappop(minHeap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if (i, j) == (ni - 1, nj - 1):
                return v

            for di, dj in directions:
                iT, jT = i + di ,j + dj
                if iT in range(ni) and jT in range(nj) and (iT, jT) not in visited:
                    # modification regading max value in heappush - C1
                    heapq.heappush(minHeap, [max(v, grid[iT][jT]), iT, jT])

print(Solution().swimInWater(grid = [[0,2],[1,3]]))
