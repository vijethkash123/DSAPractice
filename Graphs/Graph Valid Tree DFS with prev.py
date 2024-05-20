'''
Very important Problem : HOW TO DETECT cycles in undirected graphs? - Same solution
'''
from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)  # Undirected, so add both directions
        
        def dfs(node, prev):
            nonlocal visited
            if node in visited :
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei != prev and not dfs(nei, node):  # sending prev value as node is very important concept so that we don't detect false positive cycle in the graph
                    return False
            return True

        res = dfs(0, -1)  
        if len(visited) != n or not res:
            return False
        return True
    
# Check Union Find solution for it in Union Find folder, note in Notion.
