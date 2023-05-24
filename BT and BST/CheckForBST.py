class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self,root):
        return self.helper(root, float("-inf"), float("inf"))
 
    def helper(self,root,minValue,maxValue):
        if root is None:
            return True
        if root.val <= minValue or root.val >= maxValue:
            return False
        validLeft = self.helper(root.left, minValue, root.val)
        validRight = self.helper(root.right, root.val, maxValue)
        return validLeft and validRight
        
if __name__ == "__main__":
    root=TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(7)
    root.left.left = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(8)
    
    s=Solution()
    print(s.isValidBST(root))