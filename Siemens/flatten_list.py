llist = [0, [1, 2], [3, 4], [5, 6], [7, [8, [9,[10,[11,[12]]]]], 13]]

final = []

def flatten(l):
    for item in l:
        if isinstance(item, list):
            flatten(item)
        else:
            final.extend([item])
    
flatten(llist)
print(final)
