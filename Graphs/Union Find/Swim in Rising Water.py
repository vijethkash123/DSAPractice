from itertools import product


class Solution:
    def swimInWater(self, grid):
        N = len(grid)
        parent = [i for i in range(N*N)]
        size = [1]*N*N
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p1] = p2
                size[p2] += size[p1]

            return True

        def find(n):
            p = n
            if parent[p] == p:
                return p
            parent[p] = find(parent[p])
            return parent[p]


        REACHABLE_AT_CURRENT_TIME = 1 
        d = {}
        for i,j in product(range(N), range(N)):  # itertools.product, same as using 2 loops or i and j, gives like cartesian product
            d[grid[i][j]] = (i, j)  # stores the indices of the grid in a dictionary with key as time as cells contain time, so when the loop gets to time t, we can mark this as REACHABLE
        
        grid = [[0] * N for _ in range(N)]  # initializes the grid to 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for i in range(N*N):  # i is time
            x, y = d[i]
            grid[x][y] = REACHABLE_AT_CURRENT_TIME
            for dx, dy in directions:
                if N>x+dx>=0 and N>y+dy>=0 and grid[x+dx][y+dy] == REACHABLE_AT_CURRENT_TIME :
                    # print(x+dx, y + dy)
                    curCell = x*N + y  # trick to convert 2D indices to 1D indices -> for x and y we do x*N + y, same for x+dx and y+dy below
                    neighbour = (x+dx)*N + y + dy
                    # print(curCell, neighbour)
                    # we union the indices now
                    union(curCell, neighbour)  # This is a trick to convert 2D indices to 1D indices, since unioning with single number is easier than maintaining 2D representation. See ChatGPT link below
                    
            if find(0) == find(N*N-1): return i

print(Solution().swimInWater(grid = [[0,2],[1,3]]))


class Solution2:
    def swimInWater(self, grid):
        N = len(grid)
        parent = {(i,j) : (i, j) for i in range(N) for j in range(N)}
        size = {(i,j) : 1 for i in range(N) for j in range(N)}
        # print(parent)
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p1] = p2
                size[p2] += size[p1]

            return True

        def find(n):
            p = n
            if parent[p] == p:
                return p
            parent[p] = find(parent[p])
            return parent[p]


        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        q = []
        ni, nj = len(grid), len(grid[0])
        for i in range(ni):
            for j in range(nj):
                q.append((grid[i][j], i, j))

        q.sort()  # items will come time wise.

        for time, i, j in q:
            for dx, dy in directions:
                iT, jT = i+dx, j+dy
                if 0<=iT<N and 0<=jT<N and grid[iT][jT] <= time:
                    union((i, j), (iT, jT))
                    if find((0, 0)) == find((N-1, N-1)): return time

print(Solution2().swimInWater(grid = [[0,2],[1,3]]))