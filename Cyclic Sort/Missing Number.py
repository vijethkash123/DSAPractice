from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = self.cyclic_sort(nums)
        # print(nums)
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return max(nums) + 1
    
    def cyclic_sort(self, arr):
        j = 0

        while j < len(arr):
            correct_index = arr[j]

            if arr[j] < len(arr) and arr[j] != arr[correct_index] :
                # basic swap
                temp = arr[j]
                arr[j] = arr[correct_index]
                arr[correct_index] = temp
            else:
                j += 1
        
        return arr
print(Solution().missingNumber(nums=[0,2,3,4]))