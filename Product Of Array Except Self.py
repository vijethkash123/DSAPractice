import sys
a=[1,2,3,4]
n=len(a)
ol=[]
lp=[]
rp=[]

#Normal solution is to have a multiplied number and divide it by all elements 

#Given condition: Not allowed to use Division

for i in range(n):
    lp.append(1)
for i in range(n):
    rp.append(1)
for i in range(n):
    ol.append(1)

#Code with Theta=3n complexity

for i in range(1,n):
    lp[i]=a[i-1]*lp[i-1]
for j in range(n-2,-1,-1):
    rp[j]=a[j+1]*rp[j+1]
for k in range(0,n):
    ol[k]=lp[k]*rp[k]


print(lp)
print(rp)
print(ol)