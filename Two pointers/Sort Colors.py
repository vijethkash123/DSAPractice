from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        l = 0
        i = 0
        r = len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                # Swap with left pointer
                swap(l,i)
                l+=1
                i+=1
            elif nums[i] == 2:
                # Swap with right pointer
                swap(r,i)
                r-=1
            elif nums[i] == 1:
                i+=1
        return nums

obj = Solution()
print(obj.sortColors(nums=[2,0,2,1,1,0]))