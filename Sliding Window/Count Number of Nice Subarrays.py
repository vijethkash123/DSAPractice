from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        oddCount = 0
        subCount = 0
        ans = 0
        while j < len(nums):
            if nums[j] % 2 != 0:
                oddCount += 1

            if oddCount == k:
                subCount = 0
                while oddCount == k:
                    if nums[i] % 2 != 0:
                        oddCount -= 1
                    subCount += 1
                    i += 1
            ans += subCount
            j += 1

        return ans

# print(Solution().numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
print(Solution().numberOfSubarrays(nums = [2,2,1,1,2,1,2], k =3))  # good test case
print(Solution().numberOfSubarrays(nums = [2,2,1,1,2,1,1], k =3))  # good test case
