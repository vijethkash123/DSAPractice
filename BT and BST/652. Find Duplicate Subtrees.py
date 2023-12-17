from typing import *
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hashmap = defaultdict(list)
        res = []
        def dfs(root):
            if not root:
                return 'N'
            serialized = ",".join([str(root.val), dfs(root.left), dfs(root.right)])
            if len(hashmap[serialized]) == 1:  
                res.append(root)
            hashmap[serialized].append(root.val)
            return serialized
        
        dfs(root)
        print(hashmap)
        return res
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


obj = Solution()
print(obj.findDuplicateSubtrees(root = root))