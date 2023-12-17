#  Use this code to print values when TreeNode object is returned from the problem's output
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res



root = TreeNode(1)
root.left = TreeNode(2) 
root.right = TreeNode(3)

obj = Solution()
print(obj.inorderTraversal(root = root))