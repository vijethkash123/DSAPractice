import math
def pt(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            c = math.sqrt((arr[i]**2)+(arr[j]**2))
            if c in arr:
                count+=1
                return True
            else:
                continue
    return False




arr=[3,4,6,5,8,10]
n=len(arr)
print(pt(arr,n))
