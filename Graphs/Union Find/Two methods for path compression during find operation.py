parent = [0, 0, 1, 2, 3, 4]
        # 0   1  2 3  4  5
def find(n):
    p = n
    if p == parent[p]:
        return p
    else:
        parent[p] = find(parent[p])
        return parent[p]

def find1(n):
    p = parent[n]
    while p != parent[p]:
        parent[p] = parent[parent[p]] # C1 [imp] - Set the parent to it's greandparent, path compression. It shortens the path and we find the ultimate parent faster. The last parent will continue ti return itself, so we won't get error after we reach root parent.
        p = parent[p]
    return p

print(find(5))  # 0
print(parent)   # [0, 0, 0, 0, 0, 0] -> Everything is set to ultimate parent after one find() call


parent = [0, 0, 1, 2, 3, 4]  # just resetting parent for calling again via Neetcode's method [find1(n)]

print(find1(5))  # 0
print(parent)  # [0, 0, 0, 2, 2, 4]

# find1 is Neetcode's method of path compression -> Doesn't guareantee O(1) parent lookup for 2nd/ later calls after the first find() call for that disjoint set is done
# find is Normal/ Striver's way of path compression -> Guareantees O(1) parent lookup for 2nd/ later calls after the first find() call for that disjoint set is done
