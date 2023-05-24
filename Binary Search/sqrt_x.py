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