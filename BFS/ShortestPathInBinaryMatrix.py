from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        N=len(grid)
        if grid[0][0]!=0: return -1
        q=deque()
        q.append((0,0))
        pathLength = 1
        grid[0][0]=1 #Marking it as visited
        while(q):
            levelCount=len(q)
            while(levelCount>0):
                print(q)
                levelCount-=1
                cell = q[0]
                q.popleft()

                i=cell[0]
                j=cell[1]
                
                if (i==N-1 and j==N-1):  #We reached right bottom corner
                    return pathLength
                
                if (i>0 and grid[i-1][j]==0):
                    q.append((i-1,j))
                    grid[i-1][j]=1
                if (j>0 and grid[i][j-1]==0):
                    q.append((i,j-1))
                    grid[i][j-1]=1
                if (i<N-1 and grid[i+1][j]==0):
                    q.append((i+1,j))
                    grid[i+1][j]=1
                if (j<N-1 and grid[i][j+1]==0):
                    q.append((i,j+1))
                    grid[i][j+1]=1
                if i > 0:
                    if (j>0 and grid[i-1][j-1]==0):
                        q.append((i-1,j-1))
                        grid[i-1][j-1]=1
                    if (j<N-1 and grid[i-1][j+1]==0):
                        q.append((i-1,j+1))
                        grid[i-1][j+1]=1
                if i < N-1:
                    if (j>0 and grid[i+1][j-1]==0):
                        q.append((i+1,j-1))
                        grid[i+1][j-1]=1
                    if (j<N-1 and grid[i+1][j+1]==0):
                        q.append((i+1,j+1))
                        grid[i+1][j+1]=1
                        
            pathLength+=1 #After checking and marking all it's adjacent nodes in all 8 directions in if statements, all possibble paths for that level is done. So, increment pathLength
                
        return -1
                        
if __name__ == "__main__":
    obj=Solution()
    obj.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])