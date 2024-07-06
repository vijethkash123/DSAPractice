'''
It is insertion sort using recursion. TC is O(n^2)
See hand drawn explanation in: https://i.ibb.co/NnFCytc/unnamed.jpg

We start processing elements from first to last.
We have nums with single element -> nums[0] and compare it with nums[1] -> element
We do insertion sort and sort the subarray
Then we compare next element with sorted array at left
This process continues untill the whole array is sorted.
'''

class Solution:
    def sort(self, nums):
        self.sortRecur(nums, len(nums) - 1)
        return nums

    def sortRecur(self, nums, lastIndex):
        if lastIndex == 0:
            return
        element = nums[lastIndex]
        self.sortRecur(nums, lastIndex - 1)
        
        i = lastIndex - 1
        while i >=0 and nums[i] > element:
            nums[i + 1] = nums[i]
            i = i - 1

        nums[i + 1] = element
        

print(Solution().sort(nums = [3,2,1,5,4,7,6]))

