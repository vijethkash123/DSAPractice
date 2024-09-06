def nonRepeating(arr):
    freqMap = [0] * (max(arr) + 1)
    for i in arr:
        freqMap[i] += 1
    
    for i in range(len(freqMap)):
        if freqMap[i] == 1:
            return i
    
print(nonRepeating(arr=[1 ,2, 1, 3, 4]))

