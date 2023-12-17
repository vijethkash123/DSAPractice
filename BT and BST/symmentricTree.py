# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(p, q): 
            if not p and not q:
                return True
            if (not p.left and q.right) or (not p.right and q.left) or (p.left and not q.right) or (p.right and not q.left) or (not p.left and not q.right) or (not p.right and not q.left):
                return False
            if  (p.left.val != q.right.val or p.right.val != q.left.val):
                return False

            return isMirror(p.left, q.left) and isMirror(p.right, q.right)
        
        root1 = root.left
        root2 = root.right

        return isMirror(root1, root2)
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

obj = Solution()
print(obj.isSymmetric(root = root))