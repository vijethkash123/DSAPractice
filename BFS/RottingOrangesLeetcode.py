from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        R = len(grid) #Row size
        C = len(grid[0]) #Column size
        freshCount = 0  #Note 1
        q = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j]==2:
                    q.append((i,j)) #IMP NOTE
                elif grid[i][j]==1:
                    freshCount+=1 #Note 2
        
        minutes = 0
        while(q and freshCount > 0): #Note 3
            levelCount = len(q)
            while(levelCount>0):
                levelCount-=1
                cell = q[0]
                q.popleft()
                 
                i = cell[0]
                j = cell[1]
                if (i>0 and grid[i-1][j]==1):
                    q.append((i-1,j))
                    grid[i-1][j]=2
                    freshCount-=1
                if (j>0 and grid[i][j-1]==1):
                    q.append((i,j-1))
                    grid[i][j-1]=2
                    freshCount-=1
                if (i<R-1 and grid[i+1][j]==1):
                    q.append((i+1,j))
                    grid[i+1][j]=2
                    freshCount-=1
                if (j<C-1 and grid[i][j+1]==1):
                    q.append((i,j+1))
                    grid[i][j+1]=2
                    freshCount-=1
            minutes+=1

        if(freshCount>0):
            return -1
        else:
            print(minutes)
            return minutes
if __name__ == "__main__":
    obj=Solution()
    obj.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])