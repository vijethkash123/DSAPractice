from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def list_to_binary_tree(lst):
    if not lst:
        return None
    
    # Create the root node
    root = TreeNode(lst[0])
    queue = deque([root])
    index = 1
    
    while index < len(lst):
        node = queue.popleft()
        
        # Assign the left child
        if index < len(lst):
            node.left = TreeNode(lst[index])
            queue.append(node.left)
            index += 1
        
        # Assign the right child
        if index < len(lst):
            node.right = TreeNode(lst[index])
            queue.append(node.right)
            index += 1
            
    return root

lst = [1, 2, 3, 4, 5, 6, 7]
root = list_to_binary_tree(lst)
