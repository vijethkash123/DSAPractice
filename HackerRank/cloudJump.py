jc=0 #jump_count
a=[0,0,0,1,0,0]
# a=[0,0,1,0,0,1,0]
n=len(a)
# for i in range(n):
i=0
while i < n-1:
    try:
        if a[i+2]!=1:
            i+=2
            jc+=1
        else:
            i+=1
            jc+=1
    except:
        if i<n:
            jc+=1
            i+=1
print(jc) 