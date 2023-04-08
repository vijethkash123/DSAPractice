import sys
from pandas import DataFrame
class knightTour:

    xMoves = [2, 1, -1, -2, -2, -1, 1, 2] 
    yMoves = [1, 2, 2, 1, -1, -2, -2, -1] 

    def KT(self,size):
        self.size=size
        visited = [[0 for i in range(size) ]for i in range(size)]

        visited[0][0]=1

        if(self.solveKT(visited,2,0,0)):
            # self.printSolution(visited)
            pass
        else:
            print("No solution Found")
    
    def solveKT(self,visited,moveCount,x,y):
        if(moveCount == self.size**2  +1) :
            # return True
            self.printSolution(visited)
            print("======================")
        for i in range(8):
            nextX= x+self.xMoves[i]
            nextY= y+self.yMoves[i]



            if self.isValidMove(visited,nextX,nextY):
                
                visited[nextX][nextY] = moveCount

                if(self.solveKT(visited,moveCount+1,nextX,nextY)):
                    return True
                

                visited[nextX][nextY]=0
            
        return False

    def isValidMove(self,visited,x,y):
        n=len(visited)
        if x >= 0 and y >= 0 and x < n and y < n and visited[x][y]==0:
            return True
        else:
            return False
        
    def printSolution(self,visited):
        print(DataFrame(visited))
        
        # for i in range(len(visited)):
        #     print(visited[i])
        # print("\n")

obj=knightTour()
obj.KT(5)