class Solution:
    def maxSubArray(self, nums):
        globMax = nums[0]
        curMax = 0

        for n in nums:
            curMax = max(n, curMax + n)
            globMax = max(globMax, curMax)
        
        return globMax

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6


"""
Simple implementation below. But avoid using this. We were using this before
"""

nums = [1, -2, 3, -1]
meh = 0
msf = float("-inf")
for i in range(len(nums)):
    meh += nums[i]
    msf = max(msf, meh)
    if meh < 0:  # sum is only going to decrease if we have negative/ positive number next when the current subarray sum is negative. So we set it to 0
        meh = 0
print(msf)