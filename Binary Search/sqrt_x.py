class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        m = 0
        while l <= r:
            m = (l+r)//2
            square = m*m
            if square == x:
                return m
            elif square < x:
                l = m+1
            else:
                r = m-1
        return r

obj = Solution()
print(obj.mySqrt(1))


# Using Max template from Patterns

import math

def mySqrt(x: int) -> int:
     left, right = 0, x
     while left < right:
         mid = math.ceil(left + (right-left)/2)
         if mid * mid <= x:
             left = mid
         else:
             right = mid-1
     return left

print(mySqrt(8))
