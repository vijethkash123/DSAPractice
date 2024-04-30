from typing import *

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] = -nums[abs(i)-1]
            else:
                res.append(abs(i))
        
        return res

            
print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))