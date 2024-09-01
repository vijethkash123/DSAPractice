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


        REACHABLE_AT_CURRENT_TIME = 1  # boolean
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
                    union(curCell, neighbour)  # Above used is a trick to convert 2D indices to 1D indices, since unioning with single number is easier than maintaining 2D representation. See ChatGPT link below
                    
            if find(0) == find(N*N-1): return i

print(Solution().swimInWater(grid = [[0,2],[1,3]]))


# without 2D to 1D conversion, and also using list and sort the times
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

        llist = []
        ni, nj = len(grid), len(grid[0])
        for i in range(ni):
            for j in range(nj):
                llist.append((grid[i][j], i, j))

        llist.sort()  # items will come time wise.

        for time, i, j in llist:
            for dx, dy in directions:
                iT, jT = i+dx, j+dy
                if 0<=iT<N and 0<=jT<N and grid[iT][jT] <= time:
                    union((i, j), (iT, jT))
                    if find((0, 0)) == find((N-1, N-1)): return time
        return 0

print(Solution2().swimInWater(grid = [[0,2],[1,3]]))



"""
## Dijkstra's algorithm - Small modification. More like simple minHeap problem

Dijkstra's as we know is minHeap + BFS technique
C1 - Modification: Instead of adding the value itself, we add the max value we found along the path. 
Our goal is to return the maxium in the shortest path. We have to maximise the value in the minimum distance
> We have to minimize the maximum height it takes us in the path

**Problem simplified**: We can only swim to the cell if the t is >= the value in that cell. Otherwise we wait till t gets to that value.

#### Intuition:
As we have to find path which takes least time to reach from top left to bottom right cell, we think in a way, where at each step we pick the adjacent cell with minimum value, *greedily*. And we are also finding the shortest path. This gives intution for greedy + Dijkstra's + minHeap kind of solution.


Dry run this example as in Neetcode video:
|=|=|=|
|---|---|---|
|0|1|3|
|2|4|1|
|1|2|1|

##### Code:
```
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
```


Another approach from solutions:
```
class DJS:
    def __init__(self, n, m):
        self._d = {
            (i, j): (i, j)
            for i in range(n)
            for j in range(m)
        }
    
    def find(self, a):
        aa = self._d[a]
        if a != aa:
            self._d[a] = self.find(aa)
        return self._d[a]
    
    def union(self, a, b):
        aa = self.find(a)
        bb = self.find(b)
        if aa != bb:
            self._d[aa] = bb

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n == m == 1:
            return grid[0][0]
        
        q = []
        for i, line in enumerate(grid):
            q.extend(
                (elem, i, j)
                for j, elem in enumerate(line)
            )
        q.sort()

        djs = DJS(n, m)
        start = (0, 0)
        finish = (n - 1, m - 1)

        for dist, i, j in q:
            for x, y in ((i - 1, j),
                         (i + 1, j),
                         (i, j - 1),
                         (i, j + 1)):
                if (
                    0 <= x < n
                    and 0 <= y < m
                    and grid[x][y] <= dist
                ):
                    djs.union((i, j), (x, y))
                    if djs.find(start) == djs.find(finish):
                        return dist
```



#### Union Find approach

ChatGPT link: 
https://chatgpt.com/share/5461a447-61d9-4405-86e4-08966be708b0
- 2D to 1D representation conversion
To convert a grid into a 1D array, you can use the formula to map the coordinates (i, j) of the 2D grid to a 1D index: index = i × N + j, where N is the number of columns in the grid.

### Mapping Example
Consider a 3x3 grid:

(0,0) (0,1) (0,2)  
(1,0) (1,1) (1,2)  
(2,0) (2,1) (2,2)  

Using the formula index = i × N + j, we can map the coordinates as follows:

- (0, 0) maps to 0 × 3 + 0 = 0  
- (0, 1) maps to 0 × 3 + 1 = 1  
- (0, 2) maps to 0 × 3 + 2 = 2  
- (1, 0) maps to 1 × 3 + 0 = 3  
- (1, 1) maps to 1 × 3 + 1 = 4  
- (1, 2) maps to 1 × 3 + 2 = 5  
- (2, 0) maps to 2 × 3 + 0 = 6  
- (2, 1) maps to 2 × 3 + 1 = 7  
- (2, 2) maps to 2 × 3 + 2 = 8


##### My version:
```
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
```


###### From Solutions:
- Excellent solution, uses union by rank (ignore that) but using itertoosl.product, representing 2D (i, j) as a single number etc are some neat tricks i learned from this solution. This is how good CPs code!

```
class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution:
    def swimInWater(self, grid):
        REACHABLE = 1
        d, N = {}, len(grid)
        for i,j in product(range(N), range(N)):  # itertools.product, same as using 2 loops or i and j
            d[grid[i][j]] = (i, j)
        
        dsu = DSU(N*N)
        grid = [[0] * N for _ in range(N)] 
        neib_list = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for i in range(N*N):  # i is time
            x, y = d[i]
            grid[x][y] = REACHABLE
            for dx, dy in neib_list:
                if N>x+dx>=0 and N>y+dy>=0 and grid[x+dx][y+dy] == REACHABLE :
                    # print(x+dx, y + dy)
                    neighbour = (x+dx)*N + y + dy
                    curCell = x*N + y
                    # print(curCell, x, y)
                    # print(neighbour, x+dx, y+dy)
                    # print("----------")
                    # we union the indices now
                    dsu.union((x+dx)*N + y + dy, x*N + y)  # This is a trick to convert 2D indices to 1D indices, since unioning with single number is easier than maintaining 2D representation. See ChatGPT link below
                    
            if dsu.find(0) == dsu.find(N*N-1): return i
```

###### Without 2D to 1D converison trick:
- Union used here is very simple, may not be super efficient because we are joining without caring about heights, just if the parents aren't same, we union them!

```
class DJS:
    def __init__(self, n, m):
        self._d = {
            (i, j): (i, j)
            for i in range(n)
            for j in range(m)
        }
    
    def find(self, a):
        aa = self._d[a]
        if a != aa:
            self._d[a] = self.find(aa)
        return self._d[a]
    
    def union(self, a, b):
        aa = self.find(a)
        bb = self.find(b)
        if aa != bb:
            self._d[aa] = bb

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n == m == 1:
            return grid[0][0]
        
        q = []
        for i, line in enumerate(grid):
            q.extend(
                (elem, i, j)
                for j, elem in enumerate(line)
            )
        q.sort()

        djs = DJS(n, m)
        start = (0, 0)
        finish = (n - 1, m - 1)

        for dist, i, j in q:
            for x, y in ((i - 1, j),
                         (i + 1, j),
                         (i, j - 1),
                         (i, j + 1)):
                if (
                    0 <= x < n
                    and 0 <= y < m
                    and grid[x][y] <= dist
                ):
                    djs.union((i, j), (x, y))
                    if djs.find(start) == djs.find(finish):
                        return dist
```

ChatGPT link: 
https://chatgpt.com/share/5461a447-61d9-4405-86e4-08966be708b0


Google results: [trick converting 2D coordinate to 1D cp](https://www.google.com/search?q=trick+converting+2D+coordinate+to+1D+cp&safe=active&sca_esv=a2302d5a134243eb&rlz=1C1GCEA_enIN1060IN1060&sxsrf=ADLYWIKv8nyYbwyC7FY73_S-R-2RXTURNw%3A1718996952485&ei=2M91Zr6nHbrl2roPqOm1qAY&ved=0ahUKEwi-8-PVsu2GAxW6slYBHah0DWUQ4dUDCBA&uact=5&oq=trick+converting+2D+coordinate+to+1D+cp&gs_lp=Egxnd3Mtd2l6LXNlcnAiJ3RyaWNrIGNvbnZlcnRpbmcgMkQgY29vcmRpbmF0ZSB0byAxRCBjcDIHECEYoAEYCjIHECEYoAEYCjIHECEYoAEYCjIEECEYFUj3V1CNDljbVnAGeAGQAQOYAZ0EoAHgR6oBDDAuMjMuNS41LjUuMbgBA8gBAPgBAZgCKqACwj-oAhTCAgoQABiwAxjWBBhHwgIEECMYJ8ICChAjGIAEGCcYigXCAgsQABiABBiRAhiKBcICCxAAGIAEGLEDGIMBwgIIEAAYgAQYsQPCAhEQLhiABBixAxjRAxiDARjHAcICERAAGIAEGJECGLEDGIMBGIoFwgIKEAAYgAQYQxiKBcICDhAuGIAEGLEDGIMBGIoFwgIOEAAYgAQYsQMYgwEYigXCAgcQIxgnGOoCwgIUEAAYgAQY4wQYtAIY6QQY6gLYAQHCAhQQABjjBBi0AhiJBRjpBBjqAtgBAcICFhAuGAMYtAIY5QIY6gIYjAMYjwHYAQLCAhYQABgDGLQCGOUCGOoCGIwDGI8B2AECwgIFEAAYgATCAgoQLhiABBhDGIoFwgINEAAYgAQYsQMYQxiKBcICChAAGIAEGBQYhwLCAg4QLhiABBiRAhixAxiKBcICCxAAGIAEGLEDGIoFwgIREC4YgAQYsQMYgwEYxwEYrwHCAh0QLhiABBiRAhixAxiKBRiXBRjcBBjeBBjgBNgBA8ICDRAuGIAEGLEDGEMYigXCAggQLhiABBixA8ICCxAuGIAEGLEDGNQCwgIOEC4YgAQYsQMYxwEYrwHCAi4QLhiABBhDGIoFGJcFGNwEGN4EGOAEGPQDGPEDGPUDGPYDGPcDGPgDGPkD2AEDwgILEC4YgAQYxwEYrwHCAg0QABiABBixAxiDARgKwgIHEAAYgAQYCsICGhAuGIAEGMcBGK8BGJcFGNwEGN4EGOAE2AEDwgIIEAAYFhgeGA_CAgYQABgWGB7CAgsQABiABBiGAxiKBcICCBAAGIAEGKIEwgIIEAAYCBgNGB7CAgUQIRigAcICBRAhGJ8FmAMHiAYBkAYIugYGCAEQARgBugYGCAIQARgLugYGCAMQARgUkgcKNi4yMy40LjMuNqAHsOoB&sclient=gws-wiz-serp)

#### Binary Search
Min template, find first T in FFFF..FTTT...T

Not checked, code is from solutions, check later
```
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n == m == 1:
            return grid[0][0]
        
        def get_nexts(i, j, visited):
            for x, y in ((i - 1, j),
                         (i + 1, j),
                         (i, j - 1),
                         (i, j + 1)):
                if (
                    0 <= x < n
                    and 0 <= y < m
                    and (x, y) not in visited
                ):
                    yield (x, y)

        def check(value):
            q = [(0, 0)]
            visited = {(0, 0)}
            while q:
                i, j = q.pop()
                for x, y in get_nexts(i, j, visited):
                    if grid[x][y] > value:
                        continue
                    if x == n - 1 and y == m - 1:
                        return True
                    q.append((x, y))
                    visited.add((x, y))
            return False
        
        left = max(grid[0][0], grid[-1][-1])
        right = max(max(line) for line in grid)

        if check(left):
            return left
        
        while right - left > 1:
            middle = (left + right) // 2
            if check(middle):
                right = middle
            else:
                left = middle
        
        return right
```
"""