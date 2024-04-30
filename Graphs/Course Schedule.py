from collections import defaultdict, deque
from typing import List

#  Using Kahn's algorithm for Cycle detection.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visitedC = 0
        adj = defaultdict(list)
        for i in prerequisites:
            adj[i[0]].append(i[1])  # Directed graph, no need to add v -> u. Only u -> v is enough 

        indegree = [0] * numCourses
        for u,v in adj.items():
            for vertex in v:
                indegree[vertex] += 1

        leaves = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                leaves.append(i)

        while leaves:
            node = leaves.popleft()
            visitedC += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    leaves.append(nei)
        
        return visitedC == numCourses



print(Solution().canFinish(3, [[0,1],[0,2],[1,2],[2,1]]))