from typing import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            elif sum(subset) < target:
                for ind in range(i, len(candidates)):
                    if sum(subset + [candidates[ind]]) > target:
                        return
                    dfs(ind, subset + [candidates[ind]])

        dfs(0, [])
        return res
          

obj = Solution()
print(obj.combinationSum(candidates=[2,3,5], target=8))
