# def twoSum(nums, target):
#     for i in range(len(nums)):
#         comp=target-nums[i]
#         if comp in nums and nums.indmex(comp)!=i:
#             return [nums.index(comp),i]

# print(twoSum([3,2,4],6))

def twoSum(nums, target):
    ddict={}
    for i in range(len(nums)):
        comp=target-nums[i]
        if comp not in ddict:
            ddict[nums[i]]=i
        else:
            return [i,ddict[comp]]

print(twoSum([3,2,4],6))        