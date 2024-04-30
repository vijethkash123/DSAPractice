class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def rec(n):
            nonlocal memo
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            else:
                res = rec(n-1) + rec(n-2) + rec(n-3)
                memo[n] = res
                return res
        
        return rec(n)

print(Solution().tribonacci(10))


# Non DP: Recalculates result everytime.
# class Solution: 
#     def tribonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1 or n == 2:
#             return 1
#         else:
#             return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)