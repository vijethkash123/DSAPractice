#Maximum difference between two elements such that larger element appears after the smaller number


#This program is same as Best time to but and sell stocks (Stocks.py)


a=[1, 2, 90, 10, 110]
mmin=float("inf")
diff=0
for i in range(len(a)):
    if a[i]<mmin:
        mmin = a[i]
    else:
        diff=max(diff,a[i]-mmin)
print(diff)
