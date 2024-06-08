from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        def bfs():
            q = deque([0])
            visited = set()
            visited.add(0)

            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if colors[nei] == -1 and nei not in visited:
                        colors[nei] = not colors[node]  # just changing between colors 0 and 1 for adjacent nodes
                        q.append(nei)
                        visited.add(nei)
                    elif colors[nei] == colors[node]:
                        return False
            return True
        
        return bfs()

print(Solution().isBipartite(graph = [[1,3],[0,2],[1,3],[0,2]]))