# Naive approach
from collections import defaultdict
from typing import *

words = ["eat", "tea", "tan", "ate", "nat", "bat"] # Collections -> Counter



# Easiest solution by sorting letters in each string and then using them as defaultdict keys.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for s in strs:
            dd[str(sorted(s))].append(s)
        return dd.values()
