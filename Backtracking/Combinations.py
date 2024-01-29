from typing import *

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []
        nums = [i for i in range(1, n+1)]

        def dfs(i):
            if len(subset) == k:
                res.append(subset.copy())
                return

            for ind in range(i, len(nums)):
                subset.append(nums[ind])
                dfs(ind+1)
                subset.remove(nums[ind])
        dfs(0)
        return res
    
obj = Solution()
print(obj.combine(n=4, k=2))