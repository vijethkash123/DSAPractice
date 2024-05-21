from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        nums = self.cyclic_sort(nums)
        for i in range(len(nums)):
            if i+1 != nums[i]:
                res.append(nums[i])
        return res

    def cyclic_sort(self, arr):
        j = 0
        while j < len(arr):
            correct_index = arr[j] - 1

            if arr[j] != arr[correct_index]:
                temp = arr[j]
                arr[j] = arr[correct_index]
                arr[correct_index] = temp
            else:
                j += 1
        return arr

print(Solution().findDuplicates(nums=[4,3,2,7,8,2,3,1]))