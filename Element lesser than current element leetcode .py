num = [8,1,2,2,3]
# num=[6,5,4,8]
nums=num
nums=sorted(num)
n=len(nums)
# print(nums)
# count=0
ans=[]
fans=[]
for i in range(n-1,-1,-1):
    prev=i
    while(prev!=0 and nums[i]==nums[prev-1]):
        prev-=1
    # if prev==0:
    #     ans.append(0)
    # ans.insert(num.index(nums[i]),prev)

    ans.append(prev)
ans.reverse()
for i in range(n):
    x=num[i]
    m=nums.index(num[i])
    fans.append(ans[m])
print(fans)