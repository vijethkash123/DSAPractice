from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)

        # find function
        def find(n):
            p = n
            if p == parent[p]:
                return p
            else:
                parent[p] = find(parent[p])
                return parent[p]

        # union function
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:  # size of parents! not n1 and n2, don't make this mistake
                parent[p2] = p1
                size[p1] += size[p2]
            else:  # less than or equal sizes
                parent[p1] = p2
                size[p2] += size[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]  # returning the redundant edge


print(Solution().findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))