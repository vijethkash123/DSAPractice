"""
Intuition:
Cycle detection - If it is impossible to finish all courses, return an empty array.
Topological sort - As Topological sort order is not unique and can differ based on how which independent node we pick among multiple - Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them.
This is enough to understand we need Kahn's algorithm for Topological sorting along with Cycle detection for Directed graphs.
I know we have to consider outdegree to be logically correct with this problem, but just using basic Kahn's algo for cycle detection which uses inorder.
But as I am using indegree, just reverse the ans at last. As we go from least dependent to most dependent in my case, whereas in the actual problem I have to go from most dependent first to least dependent :)
Kahn's algo Top Sort for the save!
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        indep = deque()
        visited = set()
        ans = []
    
        for crs, pre in prerequisites:
            adj[crs].append(pre)  # Undirected, only 1 direction is enough
        
        for u, v in adj.items():
            for vertex in v:
                indegree[vertex] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                indep.append(i)  # getting nodes with 0 indegree/ independent nodes
        
        while indep:
            node = indep.popleft()
            visited.add(node)
            ans.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    indep.append(nei)  
        
        if len(visited) != numCourses:
            return []
        return reversed(ans)
                
        