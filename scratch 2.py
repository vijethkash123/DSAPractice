from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(i, subset):
            if len(subset) > k or sum(subset) > n:
                return
            if subset and sum(subset) == n and len(subset) == k:
                res.append(subset.copy())
            else:
                for num in range(i + 1, 10):
                    dfs(num, subset + [num])

        dfs(0, [])
        return res
    
print(Solution().combinationSum3(k = 3, n = 7))