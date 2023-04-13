import math
class Solution:
    piles = None
    h = 0
    def minEatingSpeed(self, piles, h: int) -> int:
        self.h = h
        self.piles = piles
        maxBananasPerHour = max(piles)
        return self.binarySearch(maxBananasPerHour)
    def binarySearch(self, maxVal: int):
        nums = [i for i in range(1, maxVal+1)]
        l = 0
        r = len(nums) - 1
        res = maxVal

        while l <= r:
            totalHoursForMid = 0
            mid = (l + r) // 2
            for i in range(len(self.piles)):
                totalHoursForMid += math.ceil(self.piles[i] / nums[mid])
            if totalHoursForMid > self.h:
                l = mid+1
            elif totalHoursForMid <= self.h:
                r = mid - 1
                res = min(res, nums[mid])

        return res

obj = Solution()
# print(obj.minEatingSpeed(piles = [3,6,7,11], h = 8))
print(obj.minEatingSpeed(piles = [2,2], h = 8))