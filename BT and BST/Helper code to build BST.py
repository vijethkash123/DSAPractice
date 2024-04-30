def build_tree(s):
    s = s[1:-1].split(',')
    if len(s) == 0:
        return
    nodes = [('root', s[0])]
    for i, c in enumerate(s[1:]):
        if c != 'null':
            if i & 1:
                nodes.append((nodes[i // 2][0] + '.right', c))
            else:
                nodes.append((nodes[i // 2][0] + '.left', c))
    for node in nodes:
        print(node[0] + ' = TreeNode(' + node[1] + ')')

# Call build_tree function by passing the input string
# build_tree('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]')
build_tree('[4,9,0,5,1]')


'''
Binary Search Tree - Visualization: https://www.cs.usfca.edu/~galles/visualization/BST.html
'''
