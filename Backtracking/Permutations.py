
from typing import *

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         result = []
        
#         if len(nums) == 1:
#             return [nums.copy()]
        
#         for i in range(len(nums)):
#             n = nums.pop(0)  # popping the first element and sending rest down the recurssion
#             perms = self.permute(nums)
            
#             for perm in perms:
#                 perm.append(n)  # append the popped element to last to create permutations
            
#             result.extend(perms)  # append the permutations to result, this is intermediate res, and made complete in root of DFS

#             nums.append(n)  # we append the popped element to last instead of adding back to first position because, we donot want to pop the same element again in next call. If we have [1,2,3] -> returned nums after 1st dfs vertically will be [2,3,1]. So next time we can pop 2
        
#         return result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(visited):
            if len(visited) == len(nums):
                res.append(visited[:])
                return
            else:
                for ind in range(len(nums)):
                    if nums[ind] not in visited:
                        visited.append(nums[ind])
                        dfs(visited)
                        visited.pop()
        dfs([])
        
        return res


obj = Solution()
print(obj.permute(nums=[1,2,3]))