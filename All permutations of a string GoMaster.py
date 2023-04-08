class Solution(object):
    def permute(self, nums):
        partialSet=[]
        powerSet=[]
        flags=[True]*len(nums)  #if flag[i]==True, it means it is available to be used or not fixed..See notes
        self.backtrack(nums,len(nums),partialSet,powerSet,flags)
        return powerSet
    
    def backtrack(self,nums,n,partialSet,powerSet,flags):
        if(len(partialSet)==len(nums)):
            powerSet.append(partialSet[:])
        else:
            for i in range(len(flags)):  #flags and nums are of same length
                if(flags[i]):
                    flags[i]=False
                    partialSet.append(nums[i])
                    self.backtrack(nums,n-1,partialSet,powerSet,flags)
                    partialSet.pop(len(partialSet)-1)
                    flags[i]=True
if __name__ == "__main__":
    obj=Solution()
    print(obj.permute(['A','B','C']))