ss = "[[0,1,1],[0,2,5],[1,2,1],[2,3,1]]"
ss = ss.replace('[', '')
ss = ss.replace('],', '\n')
ss = ss.replace(',', ' ')
ss = ss.replace(']]','')
print(ss)

# To draw graphs when given (u, v, weight)
# Link: https://csacademy.com/app/graph_editor/

# Add swaps if u, v, w appears in different order. Split by ], swap vals within each list, and then use the same code :)