'''
Very important Problem : HOW TO DETECT cycles in undirected graphs? - Same solution
'''
from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        res = True

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)  # Undirected, so add both directions
        
        def dfs(node, prev):
            nonlocal visited, res
            if node in visited:
                res = False
                return
            visited.add(node)
            for nei in adj[node]:
                if nei != prev:
                    dfs(nei, node):  # sending prev value as node is very important concept so that we don't detect false positive cycle in the graph
            return

        dfs(0, -1)  
        if len(visited) != n or not res:
            return False
        return True
    
# Check Union Find solution for it in Union Find folder, note in Notion.
