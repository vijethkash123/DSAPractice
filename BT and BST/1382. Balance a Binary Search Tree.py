class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder_sorted = []
        def inorderDFS(root):
            if not root:
                return None
            inorderDFS(root.left)
            inorder_sorted.append(root.val)
            inorderDFS(root.right)

        def constructBST(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = constructBST(nums[:mid])
            root.right = constructBST(nums[mid + 1:])

            return root
        
        inorderDFS(root)
        return constructBST(inorder_sorted)


root = TreeNode(1)
root.left = TreeNode( None)
root.right = TreeNode( 2)
root.left.left = TreeNode( None)
root.left.right = TreeNode( 3)
root.right.left = TreeNode( None)
root.right.right = TreeNode( 4)
root.left.left.left = TreeNode( None)
root.left.left.right = TreeNode( None)
print(Solution().balanceBST(root = root))