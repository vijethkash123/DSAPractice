import bisect
'''
Video to learn about bisect module -> https://www.youtube.com/watch?v=mqaf7vj1AdA
'''

nums = [1,1,1,1,2,2,3]
target = 1
print(bisect.bisect_left(nums,2)) # Gives the index of first occurence of `target` in the array.
print(bisect.bisect_right(nums,2))
print(bisect.bisect(nums,2))
#Implenetation of bisect_left with normal Binary Search
l, r = 0 , len(nums) -1
res = len(nums)
while l <=r:
    m = (l+r)//2
    if nums[m] < target:
        l = m+1
    else:
        res = m
        r = m-1
print(res)

'''
The bisect module in Python provides functions for working with sorted sequences, specifically for inserting items into a sorted sequence while maintaining the order. Here is a brief summary of the functions:

bisect(list, x): This function returns the index where the item x can be inserted in the sorted list while maintaining the order. If the item is already in the list, it returns the index of the rightmost occurrence of the item.

bisect_left(list, x): It returns the index of the leftmost occurrence of the item x in the list, if it is present. If the item is not in the list, it returns the index where it can be inserted while maintaining the order.

bisect_right(list, x): This function is similar to bisect, but, it returns the index where it can be inserted while maintaining the order.

insort_left(list, x): This function inserts the item x into the sorted list while maintaining the order. If the item is already in the list, it is inserted to the left of the leftmost occurrence of the item.

insort_right(list, x): This function is similar to insort_left, but it inserts the item x to the right of the rightmost occurrence of the item if it is already in the list.
'''