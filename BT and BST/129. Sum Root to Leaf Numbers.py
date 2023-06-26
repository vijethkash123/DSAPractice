# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return []
            left = dfs(root.left)
            right = dfs(root.right)

            if not left and not right:
                return [str(root.val)]
            else:
                f = left + right
                f = list(map(lambda x: str(root.val) + x, f))
                return f


        return sum(int(x) for x in dfs(root))
        

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

obj = Solution()
print(obj.sumNumbers(root = root))