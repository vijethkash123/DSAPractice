from typing import *
import math

class Solution:
    def check(self, m):
        split = 0
        for i in self.candies:
            split += i//m
        if split >= self.k:
            return True
        else:
            return False
    def maximumCandies(self, candies: List[int], k: int) -> int:
        self.candies = candies
        self.k = k
        l, r = 0, max(candies)
        while l < r:
            m = math.ceil(l + (r-l)/2)
            if self.check(m):
                l = m
            else:
                r = m - 1
        return l

print(Solution().maximumCandies([4,7,5], 4))