import sys
l1=[-2,2,5,-11,6]
# l1=[-2, -3, 4, -1, -2, 1, 5, -3]
max=0
sum=0
for i in range(len(l1)):
    sum=l1[i]
    for j in range((i+1),len(l1)):
        sum=sum+l1[j]
        if sum>max:
            max=sum
print("Max: "+str(max))
