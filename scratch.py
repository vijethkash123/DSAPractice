from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ni, nj = len(grid), len(grid[0])
        res = 0
        visited = set()
        def backtrack(i, j, subset):
            nonlocal res
            nonlocal visited
            if grid[i][j] == 0 or (i, j) in visited:
                return
            if i == ni or j == nj:
                res = max(res, sum(subset))
                return

            visited.add((i, j))

            if i + 1 < ni:
                subset = subset + [grid[i+1][j]]
                backtrack(i + 1, j, subset)
                subset.pop()

            if i - 1 >= 0:
                subset = subset + [grid[i-1][j]]
                backtrack(i - 1, j, subset)
                
                subset.pop()

            if j + 1 < nj:
                subset = subset + [grid[i][j+1]]
                backtrack(i, j + 1, subset)
                subset.pop()

            if j - 1 >= 0:
                subset = subset + [grid[i][j-1]]
                backtrack(i, j - 1, subset)
                subset.pop()

        final = 0
        for i in range(ni):
            for j in range(nj):
                if grid[i][j] != 0:
                    # print(grid[i][j])
                    res = 0
                    visited = set()
                    visited.add((i, j))
                    backtrack(i, j, [grid[i][j]])
                    final = max(res, final)
            
        return final
    
print(Solution().getMaximumGold(grid=[[0,6,0],
                                      [5,8,7],
                                      [0,9,0]]))

# print(Solution().getMaximumGold(grid=[[1,0,7],
#                                       [2,0,6],
#                                       [3,4,5],
#                                       [0,3,0],
#                                       [9,0,20]]))