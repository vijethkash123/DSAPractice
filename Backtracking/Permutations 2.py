from typing import *

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subset, i, visited):
            if len(subset) == len(nums) and subset not in res:
                res.append(subset[:])
                return
            else:
                for ind in range(len(nums)):
                    if ind not in visited:
                        visited.append(ind)
                        subset.append(nums[ind])
                        dfs(subset, i+1, visited)
                        subset.pop()
                        visited.pop()
        dfs([], 0, [])
        return res


print(Solution().permuteUnique(nums=[1,1,2]))