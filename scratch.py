from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)  # Undirected, so add both directions
        
        # print(adj)
        def dfs(node):
            nonlocal visited
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            return True

        res = dfs(0)
        if len(visited) == n and res:
            return True
        else:
            return False


print(Solution().validTree(n=5, edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]))
