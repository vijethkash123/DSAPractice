class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxVal):
            nonlocal res
            if not node:
                return
            if node.val >= maxVal:
                res+=1
                maxVal = node.val
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        dfs(root, root.val)
        return res

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
root.left.left.left = TreeNode(6)

obj = Solution()
print(obj.goodNodes(root))