from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left =  dfs(root.left)
            right = dfs(root.right)
        
            res = max(left+right, res) # Update res, so it can have the max diameter found till now
            return 1 + max(left,right)  # We return the height back to recursive call -> height is the maximum distance from current node to leaf node
    
        dfs(root)
        return res
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().diameterOfBinaryTree(root))