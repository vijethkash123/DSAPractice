def quick_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
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
