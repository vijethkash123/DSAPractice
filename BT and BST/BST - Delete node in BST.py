from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:  # simple case when there is no left child to the key to be deleted
                return root.right
            elif not root.right:  # simple case when there is no right child to the key to be deleted
                return root.left

            # when there are both left and right child subtrees, the minimum value in the right subtree should become the root instead of key value to be deleted - This is the trick to be understood in the poblem -> to get this value just keep going left.
            cur = root.right
            while cur.left:
                cur = cur.left

            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)  # To delete the node we replaced the actual key in the right subtree
        return root
