"""
Given the names where 
[x1, x2] where x2 tells joke to x1. We have to find the popularity of the joke, that is how long the joke was shared.
Basically have to do a DFS.We have to find joke popularity only for person named "aman".
Original image added here: https://imgur.com/a/gFItycn

"""

from collections import defaultdict

maxdist = 0
distance = {"aman": 0}
visited = set()
adj = defaultdict(list)

def dfs(node):
    visited.add(node)
    if node not in adj:
        return 1
    for nei in adj[node]:
        if nei not in visited:
            neiDist = 1 + dfs(nei)
            distance[node] = max(distance.get(node, 0), neiDist) # max amonng all neighbors
    return distance[node]


def jokePopularity(name):
    for i in range(len(name)):
        name1, name2 = name[i][0], name[i][1]
        adj[name2].append(name1)
    # print(adj)

    ans = dfs("aman")
    return ans


names = [
        ["petr", "aman"],
        ["wjmzbmr", "petr"],
        ["sdya", "wjmzbmr"],
        ["vepifanov", "sdya"]
    ]
#  a->p->w->s->v

# just to reset values
maxdist = 0
distance = {"aman": 0}
visited = set()
adj = defaultdict(list)
print(jokePopularity(names))

# names = [
#         ["ram", "aman"],
#         ["rohn", "aman"],
#         ["repu", "aman"],
#         ["akst", "aman"],
#         ["tuf", "ram"],
#         ["sam", "tuf"],
#         ["meet", "repu"],
#         ["pal", "akst"],
	
#     ]

# maxdist = 0
# distance = {"aman": 0}
# visited = set()
# adj = defaultdict(list)
# print(jokePopularity(names))
# # print(distance)

names = [
    ["petr", "aman"],
    ["gogh", "brad"]
]

maxdist = 0
distance = {"aman": 0}
visited = set()
adj = defaultdict(list)
print(jokePopularity(names))



"""
BFS approach
"""

from collections import defaultdict, deque

def find_longest_chain(graph, start):
    """Finds the longest chain in a directed graph using Breadth-First Search (BFS).

    Args:
        graph: A dictionary representing the graph, where keys are nodes and values are lists of adjacent nodes.
        start: The starting node for the BFS traversal.

    Returns:
        The length of the longest chain found.
    """

    queue = deque([start])
    visited = set([start])
    distances = {start: 1}

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return max(distances.values())

name = [
        ["petr", "aman"],
        ["wjmzbmr", "petr"],
        ["sdya", "wjmzbmr"],
        ["vepifanov", "sdya"]
    ]

adj = defaultdict(list)

for i in range(len(name)):
    name1, name2 = name[i][0], name[i][1]
    adj[name2].append(name1)

print(adj)
print(find_longest_chain(adj, "aman"))