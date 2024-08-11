from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        memo = {}

        def dfs(i, curSum):
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            if i < 0:
                return True if curSum == total / 2 else False
            memo[(i, curSum)] = dfs(i - 1, curSum + nums[i]) or dfs(i - 1, curSum) 
            return memo[(i, curSum)] 
        
        return dfs (len(nums) - 1, 0)
    
    def canPartition_BU(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        # Knapsack Space optimized implementation (2 row)
        prev = [False for _ in range(target + 1)]
        cur = prev[:]

        # Base case
        prev[0] = True
        cur[0] = True

        for i in range(1, len(nums)):
            for t in range(target + 1):
                no_take = prev[t]

                take = False
                if nums[i] <= t:
                    take = prev[t - nums[i]]
                cur[t] = take or no_take
            prev = cur[:]
        
        # print(prev)
        return prev[target]

print(Solution().canPartition_BU(nums = [1,5,11,5]))
print(Solution().canPartition(nums = [1,5,11,5]))