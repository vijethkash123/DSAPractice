import time

class Solution:
    def maxIndexAvoidingBadIndex(self, steps, badIndex) -> int:
        memo = {}
        def dfs(i, j):
            # Base cases
            if i == badIndex:
                return 0
            if j == steps + 1:
                return i

            if (i, j) in memo:
                # print((i, j))
                return memo[(i, j)]

            result = max(dfs(i + j, j + 1), dfs(i, j + 1))
            memo[(i, j)] = result
            return result

        return dfs(0, 1)


start = time.perf_counter()
print(Solution().maxIndexAvoidingBadIndex(steps = 4, badIndex = 6))  # (3, 4) will be overlapping subproblem in this case
print(Solution().maxIndexAvoidingBadIndex(steps = 40, badIndex = 620))
print(Solution().maxIndexAvoidingBadIndex(steps = 5, badIndex = 10))
print(Solution().maxIndexAvoidingBadIndex(steps = 1, badIndex = 2))

print(f" Time taken: {time.perf_counter() - start:0.9f}")



# O(1) approach - expected approach

import time
from math import sqrt

class Solution:
    def maxIndexAvoidingBadIndex(self, steps, badIndex) -> int:
        # assume we take all the steps
        result = steps * (steps + 1) // 2

        # did we pass `badIndex`?
        if result >= badIndex:
            # did we land on `badIndex` along the way?
            badStep = int ((sqrt (8 * badIndex + 1) - 1) / 2)
            # print(badStep)
            if badStep * (badStep + 1) // 2 == badIndex:
                # adjust result for skipping the first step
                result -= 1

        return result




# start = time.perf_counter()
print(Solution().maxIndexAvoidingBadIndex(steps = 4, badIndex = 7))  # (3, 4) will be overlapping subproblem in this case
print(Solution().maxIndexAvoidingBadIndex(steps = 99, badIndex = 620))
print(Solution().maxIndexAvoidingBadIndex(steps = 2, badIndex = 2))
# print(f" Time taken: {time.perf_counter() - start:0.9f}")
print(Solution().maxIndexAvoidingBadIndex(steps = 400, badIndex = 620))

