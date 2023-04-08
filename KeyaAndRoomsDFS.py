class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited=[False]*len(rooms)
        self.dfs(rooms,visited,0)
        if False in visited:
            print(False)
            return False
        else:
            print(True)
            return True
        
    def dfs(self,rooms,visited,i):
        visited[i]=True
        for j in rooms[i]:
            if j==i:
                continue
            if visited[j]==False:
                self.dfs(rooms,visited,j)


if __name__ == "__main__":
    x=[[1,3],[3,0,1],[2],[0]]
    obj=Solution()
    obj.canVisitAllRooms(x)