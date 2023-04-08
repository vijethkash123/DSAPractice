class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    flist=[]
    def insertIntoBST(self,root,insVal):
        if root is None:
            root=TreeNode(insVal)
        elif insVal<root.val:
            root.left=self.insertIntoBST(root.left,insVal)
        elif insVal>root.val:
            root.right=self.insertIntoBST(root.right,insVal)
        return root

    def printInorder(self,root):
        if root:
            self.printInorder(root.left)
            self.flist.append(root.val)
            self.printInorder(root.right)
        return self.flist






if __name__ == "__main__":
    root=TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    obj=Solution()
    print(obj.printInorder(root))
    troot = obj.insertIntoBST(root,5)
    obj.flist=[]
    print(obj.printInorder(root))
    