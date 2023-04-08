def Solution():
    # a=[2,1,3,1,4]
    a=[2,3,1,1,4]
    farthest=a[0]
    curr_end=a[0]
    jumps=1
    n=len(a)
    if n==1 or a[0]==0:
        return 0
    for i in range(len(a)):
        if i==n-1:
            return jumps
        farthest = max(farthest,i+a[i])
        if i==curr_end:
            jumps+=1
            curr_end=farthest
    return jumps

print(Solution())