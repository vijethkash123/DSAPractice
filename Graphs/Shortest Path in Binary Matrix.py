from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ni, nj = len(grid), len(grid[0])
        
        def bfs():
            q = deque()
            visited = set()
            dist = 0
            q.append((0, 0))
            visited.add((0, 0))

            while q:
                dist += 1
                i, j = q.popleft()
                if (i, j) == (ni - 1, nj - 1):
                    return dist
                directions = [[1, 0], [-1, 0], [-1, -1], [-1, 1], [0, 1], [0, -1], [1, 1], [1, -1]]
                for dx, dy in directions:
                    print(dx, dy)
                    iT, jT = i + dx, j + dy
                    if iT in range(ni) and jT in range(nj) and grid[iT][jT] == 0 and (iT, jT) not in visited:
                        q.append((iT, jT))
                        visited.add((iT, jT))
                
            return -1
        
        if grid[0][0] == 1:
            return -1
        else:
            return bfs()

print(Solution().shortestPathBinaryMatrix(
    grid = [[0,0,0],
            [1,1,0],
            [1,1,0]]
))