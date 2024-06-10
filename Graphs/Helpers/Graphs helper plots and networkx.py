import networkx as nx
import matplotlib.pyplot as plt 

d  = {
    "A": ["B", "C"],
    "B": ["A", "D", "E", "C"],
    "C": ["A", 'B', "F"],
    "D": ["B"],
    "E": ["B", "G"],
    "F": ["C"],
    "G": ["E"]
}

d = [[0,2],[1,2],[2,0]]

# for undirected graph
# g = nx.Graph(d)

# for directed grph
g = nx.DiGraph(d)
nx.draw_networkx(g)
plt.draw()
plt.show()

# Also use for visualiztion - Best -> https://csacademy.com/app/graph_editor/