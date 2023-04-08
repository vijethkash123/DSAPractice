def ks(values,weights,capacity,n):

    if n==0 or capacity==0:
        return 0
    if weights[n-1] > capacity:
        return ks(values,weights,capacity,n-1)
    # elif weights[n-1] < capacity:
    else:
        return max(values[n-1]+ks(values,weights,capacity-weights[n-1],n-1),ks(values,weights,capacity,n-1))


if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8] 
    values = [1,5,8,9,10,17,17,20] 
    capacity = 8
    n = len(values)
    print(ks(values,weights,capacity,n))
    