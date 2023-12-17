# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return 

        if root1 and root2:
            finalRoot = TreeNode(root1.val + root2.val)
            finalRoot.left = self.mergeTrees(root1.left, root2.left)
            finalRoot.right = self.mergeTrees(root1.right, root2.right)

        elif not root2:
            finalRoot = TreeNode(root1.val)
            finalRoot.left = self.mergeTrees(root1.left, None)
            finalRoot.right = self.mergeTrees(root1.right, None)

        elif not root1:
            finalRoot = TreeNode(root2.val)
            finalRoot.left = self.mergeTrees(None, root2.left)
            finalRoot.right = self.mergeTrees(None, root2.right)

        print(finalRoot.val)


        return finalRoot



root1 = TreeNode(1)
root1.left = TreeNode(3) 
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

obj = Solution()
print(obj.mergeTrees(root1, root2))
