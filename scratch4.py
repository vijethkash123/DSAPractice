from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ni = len(grid)
        nj = len(grid[0])
        minutes = 0
        def rot(i, j):
            canRot = False
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for di, dj in directions:
                iT, jT = i+di, j+dj
                if iT in range(ni) and jT in range(nj) and grid[iT][jT] == 1:
                    canRot = True
                    grid[iT][jT] = 2
            return canRot

        for i in range(ni):
            for j in range(nj):
                if grid[i][j] == 2:
                    if rot(i, j):
                        minutes += 1

        for i in range(ni):
            for j in range(nj):
                if grid[i][j] == 1: # never rotten
                    return -1
        return minutes
    
print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

[[2,0,1,1,1,1,1,1,1,1],
 [1,0,1,0,0,0,0,0,0,1],
 [1,0,1,0,1,1,1,1,0,1],
 [1,0,1,0,1,0,0,1,0,1],
 [1,0,1,0,1,0,0,1,0,1],
 [1,0,1,0,1,1,0,1,0,1],
 [1,0,1,0,0,0,0,1,0,1],
 [1,0,1,1,1,1,1,1,0,1],
 [1,0,0,0,0,0,0,0,0,1],
 [1,1,1,1,1,1,1,1,1,1]]

[[2, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
 [2, 0, 1, 0, 0, 0, 0, 0, 0, 1], 
 [2, 0, 1, 0, 1, 1, 1, 1, 0, 1], 
 [2, 0, 1, 0, 1, 0, 0, 1, 0, 1], 
 [2, 0, 1, 0, 1, 0, 0, 1, 0, 1], 
 [2, 0, 1, 0, 1, 1, 0, 1, 0, 1], 
 [2, 0, 1, 0, 0, 0, 0, 1, 0, 1], 
 [2, 0, 1, 1, 1, 1, 1, 1, 0, 1], 
 [2, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]