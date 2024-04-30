class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cur_depth = 0  # stack
        
        for i in s:
            if i == '(':
                cur_depth += 1
            elif i == ')':
                cur_depth -= 1
            
            res = max(res, cur_depth)
        return res