class Solution:
    def searchInsert(self, nums, target: int) -> int:
        l, r = 0 , len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        if l>=r:
            return l

obj = Solution()
print(obj.searchInsert([1,3,5,6], target = 6))