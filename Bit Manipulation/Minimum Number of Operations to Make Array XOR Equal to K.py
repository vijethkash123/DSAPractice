# LeetCode 2997
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        final_xor = 0
        # XOR of all integers in the array.
        for n in nums:
            final_xor = final_xor ^ n

        count = 0
        # Keep iterating until both k and final_xor becomes zero.
        while k or final_xor:
            print(k, final_xor)
            # k % 2 returns the rightmost bit in k,
            # final_xor % 2 returns the rightmost bit in final_xor.
            # Increment counter, if the bits don't match.
            if (k % 2) != (final_xor % 2):
                count += 1

            # Remove the last bit from both integers.
            # print(k//2, final_xor//2)
            k //= 2
            final_xor //= 2

        return count

print(Solution().minOperations(nums = [2,1,3,4], k = 1))




# rightshifting 4 -> 
# 4 in binary -> 0100
# Right shifting -> 010 -> gives 2
# Right shifting again -> 01 -> gives 1
# We do right shifting by floor division. Doing floor division on normal intergers is same as right shifting on binary numbers.

# Right shifting using right shift operator
# For binary Base 2:
# k = 0b100
# i = 0b001
# print(k>>1)  # 2
# print(k>>2)  # 1
# For integer/decimal Base 10:
# k = 4
# print(k>>1)  # 2

k = 4
print(2<<0)