from typing import List


class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        ni, nj = len(grid), len(grid[0])
        visited = []
        globalVisited = []

        def dfs(i, j):
            if i not in range(ni) or j not in range(nj) or grid[i][j] in (2,0):
                return
            else:
                visited.append((i, j))
                grid[i][j] = 2
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for iT, jT in directions:
                    dfs(i+iT, j+jT)
        
        for i in range(ni):
            for j in range(nj):
                if grid[i][j] == 1:
                    dfs(i,j)
                    globalVisited.append(visited)
                    visited = []
        print(globalVisited)
        # normalize visited cells to be comparable, subtract distance from first cell in visited for each item in globalVisited
        cnt = 0
        final = set()
        for vSet in globalVisited:
            first = [list(vSet)[0][0], list(vSet)[0][1]]
            norm = ""
            for j in vSet:
                start, end = j[0] - first[0], j[1] - first[1]
                norm = norm + str(start) + str(end)
            if norm not in final:
                cnt += 1
                final.add(norm)
            print(norm)
        return cnt

print(Solution().countDistinctIslands(grid=[[1, 1, 0, 1, 1], 
                                            [1, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 1], 
                                            [1, 1, 0, 1, 1]]))