set = [3, 34, 4, 12, 5, 2] 
sum = 36

def SS(set,sum,n):
    if sum >0 and n==0:
        return False
    if sum==0:
        return True
    if set[n-1]>sum:
        return SS(set,sum,n-1)
    else:
        return SS(set,sum,n-1) or SS(set,sum-set[n-1],n-1)
    
print(SS(set,sum,len(set)))