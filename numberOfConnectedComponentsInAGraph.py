#Given the connected edges in an undirected graph, return the muber of components.In the given call, 
#(0,1,2) is 1 component and (3,4) is another component. So return 2.
# Here we are just given the edges..We do not have adjacency matrix or adjacency list.. We have to create it by ourselves.
class Solution:
    def countComponents(self,n,edges):
        #Create the adjacency Matrix
        M=[[0 for i in range(n)]for j in range(n)]
        visited=[0]*n
        components=0
        for edge in edges:
            u=edge[0]
            v=edge[1]
            M[u][v]=1
            M[v][u]=1  #Doing for both uv and vu becuase it is an undirected graph

        for i in range(len(M)): #⬇
            if visited[i]==0:   #This not not matrix 
                components+=1
                self.dfs(M,visited,i)
        print(components)
        return components  

    def dfs(self,M,visited,i):
        visited[i]=1
        for j in range(len(M)): #➡
            if visited[j]==0 and M[i][j]==1:
                self.dfs(M,visited,j)
        





if __name__ == "__main__":
    obj=Solution()
    obj.countComponents(5,[[0,1],[1,2],[3,4]])   #2
    obj.countComponents(5,[[0,1],[1,2],[2,3],[3,4]])  #1