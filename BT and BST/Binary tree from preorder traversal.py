from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(data):

    def dfs():
        val = data.pop(0)
        if val == "N":
            return None
        root = TreeNode(int(val))
        root.left = dfs()
        root.right = dfs()
        return root
    return dfs()

print(deserialize(data = [1, 2, 'N', 'N', 3, 4, 'N', 'N', 5, 'N', 'N']))

# We use the same code in LeetCode serialize and deserialize tree problem, to make a tree just from Preorder traversal

'''
For Tree
      1
     / \
    2   3
       / \
      4   5
'''