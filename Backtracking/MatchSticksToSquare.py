from typing import *


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks)//4
        sides = [0]*4

        matchsticks.sort(reverse=True)

        if sum(matchsticks)/4 != length:
            return False
        
        def dfs(i):
            if i == len(matchsticks):
                return True

            for j in range(4):  # go left, top, right, bottom
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            
            return False
            
        
        return dfs(0)
print(Solution().makesquare(matchsticks = [1,1,2,2,2]))
# print(Solution().makesquare(matchsticks = [2,2,2,3,4,4,4,5,6]))