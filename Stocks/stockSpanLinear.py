stocks=[100, 80, 60, 70, 60, 75, 85]
n=len(stocks)

ans=[]
sStack=[]
# We make use of stacks

# ans.pop()   --> For pop()

# print(ans[len(ans)-1])   --> For top()
sStack.append(0)

for i in range(n):
    while(len(sStack)!=0 and stocks[i] >= stocks[sStack[len(sStack)-1]]):
        sStack.pop()
    if len(sStack)==0:
        ans.append(i+1) #At the first place
    else:
        ans.append(i-sStack[len(sStack)-1])
    sStack.append(i)

print(ans)


    