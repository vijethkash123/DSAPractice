from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        adj = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)  # Directed graph, no need to add v -> u. Only u -> v is enough 

        # if adj[crs] = [], it means it can be completed right away and has no prerequisites, or has outdegree of 0
        
        def dfs(node):
            if node in visited:  # we detected a cycle if we visit same node twice
                return False
            if adj[node] == []:
                return True   # marking as complete
            
            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False  # if we detect cycle, immediately return False
            visited.remove(node)
            adj[node] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True




print(Solution().canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]))
# print(Solution().canFinish(2, [[1,0]]))