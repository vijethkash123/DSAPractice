'''
Solution for Kth largest element in an array. Leetcode - 215
Easy solutions are aray manipulation and Heap
This is to learn the Quick Select algorithm 
'''

def quickSelect(l, r):
    p =  l
    for i in range(l, r):
        if nums[i] <= nums[r]:
            nums [p], nums [i] = nums [i], nums [p]
            p += 1
    nums[p], nums[r] = nums[r], nums [p]
    if p > k:
        return quickSelect(l, p - 1)
    elif p < k: 
        return quickSelect (p + 1, r)
    else:
        return nums [p]

nums = [3,2,1,5,4,6]
k = 3  # find 3rd largest
k = len(nums) - k
print(quickSelect(0, len(nums) - 1))