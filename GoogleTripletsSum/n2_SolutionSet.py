def findTriplets(arr, n):
    found = False
    for i in range(n - 1):
        # print(str(i)+"----i")
        s = set()
        for j in range(i + 1, n):
            # print(str(j)+"----j")
            x = -(arr[i] + arr[j])
            # print(str(x)+"-----x")
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])
                # print(str(s)+"-----------s")
    if found == False:
        print("No Triplet Found")

# arr = [0, -1, 2, -3, 1,-2]
arr=[3,4,-7]
n = len(arr)
findTriplets(arr, n) 