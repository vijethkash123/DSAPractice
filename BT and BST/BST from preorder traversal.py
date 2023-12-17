from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def dfs(l, h):
            nonlocal preorder
            if not preorder:
                return
            val = preorder.pop(0)
            
            if val > l and val < h:
                root = TreeNode(val)
            else:
                preorder = [val] + preorder
                return None

            root.left = dfs(l, root.val)
            root.right = dfs(root.val, h)
            return root
        return dfs(float("-inf"), float("inf"))

obj = Solution()
print(obj.bstFromPreorder([8,5,1,7,10,12]))