from collections import deque
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        uniqueChars = set(("".join(words)))
        self.adj = {c: set() for c in uniqueChars}

        for i in range(0, len(words) - 1):
            if not self.compare(words[i], words[i+1]):
                return ""

        indegree = {c: 0 for c in uniqueChars}
        for _, vals in self.adj.items():
            for v in vals:
                indegree[v] += 1


        # top sort
        leaves = deque()
        visited = ""
        for k, v in indegree.items():
            if v == 0:
                leaves.append(k)

        while leaves:
            node = leaves.popleft()
            visited += node
            for nei in self.adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    leaves.append(nei)
        
        if len(uniqueChars) != len(visited):
            return ""
        else:
            return "".join(visited)


    def compare(self, w1, w2):

        minLen = min(len(w1), len(w2))
        if (len(w1) > len(w2) and w1[:len(w2)] == w2):
                return False
        for i in range(minLen):
            if w1[i] != w2[i]:
                self.adj[w1[i]].add(w2[i])
                return True
        return True

            
print(Solution().foreignDictionary(words = ["hrn","hrf","er","enn","rfnn"]))
print(Solution().foreignDictionary(words=["wrtkj","wrt"]))
print(Solution().foreignDictionary(words=["wrt","wrf","er","ett","rftt","te"]))

