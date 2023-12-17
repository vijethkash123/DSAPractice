def find_optimal_middle_subsequence_sum(n, arr):
    min_sum = float('inf')

    for i in range(1, n - 1):
        chosen_1 = arr[i]

        left_min = min(arr[:i])
        right_min = min(arr[i + 1:])

        if left_min < chosen_1 > right_min:
            current_sum = left_min + chosen_1 + right_min
            min_sum = min(min_sum, current_sum)

    return min_sum if min_sum != float('inf') else -1

# Example usage
n = 7
arr = [3, 4, 5, 1, 2, 3, 1]
result = find_optimal_middle_subsequence_sum(n, arr)
print(result)  # Output: 4

