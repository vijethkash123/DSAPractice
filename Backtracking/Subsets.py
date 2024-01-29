from typing import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i): # `i` is the index we are currently processing
            if i >= len(nums):  # edge case
                res.append(subset.copy())
                return

            # decision to include the element at current index in `nums`
            subset.append(nums[i])
            dfs(i+1)  # Calling dfs for next index

            # decision to not include element at the current index in `nums`
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(subset[:])  # deepcopy
                return

            subset.append(nums[i])
            dfs(i+1)
            val = subset.pop()
            while i+1 < len(nums) and nums[i+1] == val:
                i+=1
            dfs(i+1)
            return
        
        dfs(0)
        return res



print(Solution().subsets([1,1,2]))
print(Solution().subsetsWithDup([1,1,2]))
