from typing import List
class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        prevMin = self.get_prevMin(heights)  
        nextMin = self.get_nextMin(heights)

        res = []

        for i, h in enumerate(heights):
            res.append((nextMin[i] - prevMin[i] + 1) * h)
        
        return max(res)

    
    def get_prevMin(self, heights):
        prevMin = [0] * len(heights)
        mon_inc_stack = []  # [(height, index)]
        for i in range(0, len(heights)):
            while mon_inc_stack and heights[i] < mon_inc_stack[-1][0]:
                mon_inc_stack.pop()
            if mon_inc_stack:
                prevMin[i] = mon_inc_stack[-1][1] + 1
            else:
                prevMin[i] = 0
            mon_inc_stack.append((heights[i], i))
        
        return prevMin

    def get_nextMin(self, heights):
        nextMin = [len(heights)-1] * len(heights)
        mon_inc_stack = []  # [(height, index)]
        for i in range(0, len(heights)):
            while mon_inc_stack and heights[i] < mon_inc_stack[-1][0]:
                height, index = mon_inc_stack.pop()
                nextMin[index] = i-1
            mon_inc_stack.append((heights[i], i))
        
        return nextMin

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # at each horizontal level (i) apply find the max area
        level_heights = [0] * len(matrix[0])
        ans = 0
        for row in matrix:
            for i, val in enumerate(row):
                if val == '0':
                    level_heights[i] = 0
                else:
                    level_heights[i] += int(val)
            print(level_heights)
            ans = max(self.largestRectangleArea(level_heights), ans)
        return ans
    
print(Solution().maximalRectangle(
    matrix = [["0","1"],
              ["1","0"]]
))