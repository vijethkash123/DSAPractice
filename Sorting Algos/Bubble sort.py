"""
Outer loop in reverse from n to 0
Inner loop from i to n
At each step the biggest number will be pushed to last, then last - 1, last - 2 positions...
Time complexity: O(n^2)
Space complexity: O(1)
"""

def bubble_sort(arr):

    # Outer loop to iterate through the list n times, at each step largest number gets bubbled to last index.
    for n in range(len(arr) - 1, 0, -1):  # going till index 1 is fine, we don't have to compare 0th index element

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


# Sample list to be sorted
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)
