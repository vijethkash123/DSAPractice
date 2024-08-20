"""
We use both maximum and minimum subarray sums here
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # calculate global maximum subarray sum
        msf, meh = float("-inf"), 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            meh += nums[i]
            msf = max(msf, meh)
            if meh < 0:
                meh = 0
        
        # calculate global minimum subarray sum
        min_sf, min_eh = float("inf"), 0
        for i in range(len(nums)):
            min_eh = min(nums[i], nums[i] + min_eh)
            min_sf = min(min_sf, min_eh)
        # print(msf, min_sf)
        return max(msf, total - min_sf) if msf > 0 else msf

print(Solution().maxSubarraySumCircular(nums = [5, -3, 5]))
print(Solution().maxSubarraySumCircular(nums = [1, -2, 3, -2]))