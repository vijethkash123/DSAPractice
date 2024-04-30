from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ni, nj = len(grid), len(grid[0])
        visited = set()
        def dfs(i, j):
            nonlocal visited

            if (i,j) in visited:
                return 0
            
            visited.add((i,j))

            if i < 0 or j < 0 or i >= ni or j >= nj or grid[i][j] == 0:
                return 1
            
            else:
                return dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
                # U D L R

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return dfs(i, j)
                
# print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(Solution().islandPerimeter([[0,1], 
                                  [1,1]]))