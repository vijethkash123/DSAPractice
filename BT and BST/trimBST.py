from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        if root.val < low:
            return root.right
        if root.val > high:
            return root.left
        return root


    # This is used to print the result
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
root.left = TreeNode(0) 
root.right = TreeNode(2)


obj = Solution()
x = obj.trimBST(root, 1, 2)
print(obj.inorderTraversal(x))

