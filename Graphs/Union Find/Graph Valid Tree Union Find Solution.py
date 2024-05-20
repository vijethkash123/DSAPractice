from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        size = [1] * (n)

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
                return False
        
        if len(set(parent)) == 1:  # making sure there's only 1 root remaining, means there are no disconnected components which leads to invalid Tree
            return True
        else:
            return False

print(Solution().validTree(n=5, edges=[[0,1],[2,3]]))
print(Solution().validTree(n=5, edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]))
print(Solution().validTree(n=5, edges=[[0,1],[0,2],[0,3],[1,4]]))

