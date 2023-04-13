class Solution:
    def findMin(self, nums) -> int:
        start , end = 0 ,len(nums) - 1 
        curr_min = float("inf")
        
        while start  <=  end :
            mid = (start + end ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return curr_min

obj = Solution()
print(obj.findMin(nums=[4,5,6,7,0,1,2]))