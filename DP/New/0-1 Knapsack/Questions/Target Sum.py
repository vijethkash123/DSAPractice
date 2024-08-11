from typing import List


class Solution:
    # Top Down Memoization
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(i, curSum):
            if (i, curSum) in memo:
                return memo[(i, curSum)]

            if i < 0:
                return 1 if curSum == target else 0

            memo[(i, curSum)] = dfs(i-1, curSum + nums[i]) + dfs(i-1, curSum - nums[i])
            return memo[(i, curSum)]
        
        return dfs(len(nums) - 1, 0)
    

    # Bottom Up Tabulation
    def findTargetSumWays_BUDP(self, nums: List[int], target: int) -> int:
        pass

print(Solution().findTargetSumWays(nums = [1,1,1,1,1], target = 3))
print(Solution().findTargetSumWays(nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], target = 1))

print(Solution().findTargetSumWays_BUDP(nums = [1,1,1,1,1], target = 3))
print(Solution().findTargetSumWays_BUDP(nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], target = 1))

