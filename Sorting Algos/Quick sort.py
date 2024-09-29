def quick_sort(arr):
    if len(arr) in (0, 1):
        return arr
    else:
        # Choose a pivot (here we are choosing the last element as the pivot)
        pivot = arr[-1]

        # Elements smaller than pivot
        left = [x for x in arr[:-1] if x <= pivot]

        # Elements larger than pivot
        right = [x for x in arr[:-1] if x > pivot]

        # Recursively apply quick sort to the left and right arrays
        return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage:
arr = [10, 80, 30, 90, 40, 50, 70]
sorted_arr = quick_sort(arr)
print(sorted_arr)


"""
Time Complexity

Best and Average Case: 
O(nlogn), where n is the number of elements.

Worst Case:
O(n^2) happens if the pivot is always the smallest or largest element, leading to unbalanced partitions.
You can improve the performance by picking a random pivot to reduce the chance of worst-case behavior.

Implementation using random:
[OPTIONAL] Just coded to check if it works hehe
import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        ind = random.randint(0, len(arr) - 1)
        pivot = arr[ind]
        left = [x for i, x in enumerate(arr) if x <= pivot and i != ind]
        right = [x for i, x in enumerate(arr) if x > pivot and i != ind]
        return quick_sort(left) + [pivot] + quick_sort(right)
"""