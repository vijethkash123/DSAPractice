from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        prev = -1
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)  # Undirected, so add both directions
        
        # print(adj)
        def dfs(node):
            nonlocal visited, prev
            if node in visited and node != prev:
                return False
            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            return True


        res = dfs(0)
        if len(visited) != n or not res:
            return False
        return True


print(Solution().validTree(n=5, edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]))
