# LC-979
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            l_extra = dfs(root.left)
            r_extra = dfs(root.right)

            extra_coins = (root.val - 1) + l_extra + r_extra
            
            res += abs(extra_coins)
            return extra_coins
        dfs(root)
        return res


# root = TreeNode(3)
# root.left = TreeNode(0)
# root.right = TreeNode(0)
# print(Solution().distributeCoins(root=root))

root = TreeNode(0)
root.left = TreeNode(3)
root.right = TreeNode(0)
print(Solution().distributeCoins(root=root))


# root = TreeNode(0)
# root.left = TreeNode(0)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(0)
# print(Solution().distributeCoins(root=root))
