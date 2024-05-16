# Leetcode - 2331
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root.left and not root.right:
                return root.val
            left = dfs(root.left)
            right = dfs(root.right)
            
            if root.val == 2:
                return left | right
            elif root.val == 3:
                return left & right
            
        return dfs(root)
    

root = TreeNode(2)
root.left = TreeNode(1)       
root.right = TreeNode(3)      
root.right.left = TreeNode(0) 
root.right.right = TreeNode(1)

print(Solution().evaluateTree(root))