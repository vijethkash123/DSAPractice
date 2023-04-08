class Solution(object):
    def allPathsSourceTarget(self, graph):
        path=[]
        setOfPaths=[]
        path.append(0)
        self.backtrack(graph,0,len(graph)-1,path,setOfPaths)
        return setOfPaths
    
    def backtrack(self,graph,src,dest,path,setOfPaths):
        if(src == dest):
            setOfPaths.append(path.copy())
        else:
            for node in graph[src]:
                path.append(node)
                self.backtrack(graph,node,dest,path,setOfPaths)
                path.pop(len(path)-1)  #BackTracking

if __name__ == "__main__":
    obj=Solution()
    print(obj.allPathsSourceTarget([[1,2],[3],[3],[]]))