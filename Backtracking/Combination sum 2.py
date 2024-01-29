from typing import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        subset = []
        res = []

        def dfs(subset, i):
            if sum(subset) == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or sum(subset) > target:
                return

            subset.append(candidates[i])
            dfs(subset, i+1)
            val = subset.pop()
            while i+1 < len(candidates) and candidates[i+1] == val:
                i+=1
            dfs(subset, i+1)

        dfs([], 0)
        return res           

obj = Solution()
print(obj.combinationSum2(candidates=[14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12], target=27))
