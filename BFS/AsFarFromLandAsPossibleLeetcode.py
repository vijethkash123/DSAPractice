from collections import deque
class Solution(object):
    def maxDistance(self, grid):
        if len(grid)==0:
            return -1
        N=len(grid)
        waterBodies=0
        q=deque()
        for i in range(N):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    q.append((i,j))
                elif grid[i][j]==0:
                    waterBodies+=1
        maxDist=0
        leng=0
        if waterBodies==0:
            return -1
        while(q and waterBodies>=0):
            levelCount=len(q)
            maxDist=max(maxDist,leng)
            # print(maxDist)
            while(levelCount>0):
                levelCount-=1
                # print(q)
                cell = q[0]
                q.popleft()
                
                i = cell[0]
                j = cell[1]
                
                if (i>0 and grid[i-1][j]==0):
                    q.append((i-1,j))
                    grid[i-1][j]=1
                    waterBodies-=1
                if (j>0 and grid[i][j-1]==0):
                    q.append((i,j-1))
                    grid[i][j-1]=1
                    waterBodies-=1
                if (i<N-1 and grid[i+1][j]==0):
                    q.append((i+1,j))
                    grid[i+1][j]=1
                    waterBodies-=1                    
                if (j<N-1 and grid[i][j+1]==0):
                    q.append((i,j+1))
                    grid[i][j+1]=1
                    waterBodies-=1
            leng+=1
        if waterBodies > 0 : 
            return -1
        else:
            return maxDist
                
if __name__ == "__main__":
    obj = Solution()
    obj.maxDistance([[1,0,0],[0,0,0],[0,0,0]])                
    obj.maxDistance([[1,0,1],[0,0,0],[1,0,1]])                

