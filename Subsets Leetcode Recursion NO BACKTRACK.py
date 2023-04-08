class Solution(object):
    def subsets(self, nums):
        print(self.helper(nums,len(nums)))
    
    def helper(self,nums,n):
        res=[]
        subset=[]
        
        if n==0:
            res.append(subset)
        else:
            res = self.helper(nums,n-1)
            for i in range(0,len(res)):
                subset = list(res[i])
                subset.append(nums[n-1]) #modifying res
                res.append(subset[:])
        return res
    
if __name__ == "__main__":
    obj = Solution() 
    obj.subsets([1,2,3])