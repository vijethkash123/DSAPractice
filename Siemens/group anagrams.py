# Naive approach
from collections import defaultdict
from typing import *

words = ["eat", "tea", "tan", "ate", "nat", "bat"] # Collections -> Counter
temp = []


ans = defaultdict(list)
for w in words:
    freq  = {}
    for i in w:
        if freq.get(i) is not None:
            freq[i]+=1
        else:
            freq[i] = 1
    temp.append((w,freq))

print(temp)

'''
temp = [
('eat', {'e': 1, 'a': 1, 't': 1}), 
('tea', {'t': 1, 'e': 1, 'a': 1}), 
('tan', {'t': 1, 'a': 1, 'n': 1}),
('ate', {'a': 1, 't': 1, 'e': 1}),
('nat', {'n': 1, 'a': 1, 't': 1}),
('bat', {'b': 1, 'a': 1, 't': 1})
]
'''

'''
Now I had to compare dicts and if they are equal just append the keys. Then the anagrams will
be grouped. Used defaultdict to do that, but we cannot use dict as key for another dict,
because dicts are unhashable. 
So, the solution would be to convert dict like e1a1t1, t1e1a1 respectively as string and then use 
them as keys. Can do this using frozenset -> which allows us to use dict as keys for another
dict.
'''
for a, dv in temp:
    ans[frozenset(dv)].append(a)

print(list(ans.values()))



# Easiest solution by sorting letters in each string and then using them as defaultdict keys.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for s in strs:
            dd[str(sorted(s))].append(s)
        return dd.values()