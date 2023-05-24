class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        
        idx = len(nums) // 2
        
        if nums[idx] > target:
            return self.search(nums[:idx], target)
        
        if nums[idx] < target:
            result = self.search(nums[idx + 1:], target)
            return idx + result + 1 if result >= 0 else -1
        
        return idx

obj=Solution()
print(obj.search(nums = [1,2,3,4,5,6,7,8], target = 1))