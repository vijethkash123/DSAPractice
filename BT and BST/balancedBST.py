class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root) -> bool:
        res = []
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if ((left > right and left - right > 1) or (right > left and right - left > 1)):
                res.append(False)
            else:
                res.append(True)
            return 1 + max(left, right)

        dfs(root)
        if False in res:
            return False
        else:
            return True

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.isBalanced(root))