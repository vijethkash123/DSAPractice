def minSwaps(s: str) -> int:
    xlist = [i for i in s]
    end = len(s) - 1
    stack = 0
    ans = 0


    for start in range(end):
        if s[start] == '[':
            stack += 1
        elif stack:
            stack -= 1
        else:
            ans += 1

            while s[end] != '[':
                end -= 1
            xlist[start], xlist[end] = xlist[end], xlist[start]  # added for debugging how the output after the swaps will look it
            stack += 1
            end -= 1
    
    print(''.join(xlist))
    return ans

# Example usage
brackets = "]]][[[[]"
result = minSwaps(brackets)
# print(result)  # Output: 2
# # After balancing: [][[[]]]
# print(minSwaps("]][]]"))  # -1



# Another easy solution.

from typing import List


class Solution:
    def minSwaps(self, s: str) -> int:
        flips, cSum = 0, 0
        for b in s:
            if b == '[':
                cSum += 1
            else:
                cSum -= 1
            if cSum < 0:
                flips += 1
                cSum = 1  # because when swapped we have to count the [ opening bracket that was swapped too
        return flips

print(Solution().minSwaps("]]][[["))