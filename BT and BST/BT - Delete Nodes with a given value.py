from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            # print(root.val)

            if root.left:
                root.left = dfs(root.left)
            if root.right:
                root.right = dfs(root.right)
            
            if root and not root.right and not root.left and root.val == target:
                return None
            
            return root
        
        return dfs(root)


# Testcase 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)

res = Solution().removeLeafNodes(root = root, target = 2)
print(res)


# Testcase 2
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)

res = Solution().removeLeafNodes(root = root, target = 3)
print(res)
