prices=[7,1,5,3,6,4]
prices=[2,1,4]
diff=0
min=float("inf")
for i in range(len(prices)):
    if prices[i]<min:
        min=prices[i]
    else:
        diff=max(diff,prices[i]-min)
print(diff)
