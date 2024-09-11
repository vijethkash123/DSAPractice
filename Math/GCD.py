"""
If we have 48 and 18
We do:
- 48 % 18 = 12
- 18 % 12 = 6
- 12 % 6 = 0
- 6 % 0 -> `b` became 0, so return `a`

C1: 
One cool extra point is even if `a` was smaller number and `b` was bigger number, it's get's swapped 
automatically `a` gets `b's` value and `b` gets` a % b` value. When this happens, 
`18 % 48 is 18` and this value is assigned to `b` and `a` gets value in `b` that was 48. 
So in this version of Euclidian GCD, this is handled


Time complexity is $$O(log(n))$$ it's not $$log_2$$ on average it's more than $$log_2$$ as the input gets divided more than half at each step.
Space complexity is $$O(1)$$

"""

from typing import List


class Solution:
    def findGCD(self, a, b) -> int:
        while b > 0:  # C1
            a, b = b, a % b

        return a
    
print(Solution().findGCD(48, 18))
print(Solution().findGCD(18, 48))  # C1
print(Solution().findGCD(100, 122))

