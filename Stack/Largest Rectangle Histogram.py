from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prevMin = self.get_prevMin(heights)  
        nextMin = self.get_nextMin(heights)
        
        # print(heights)
        # print(prevMin)
        # print(nextMin)
        res = []

        for i, h in enumerate(heights):
            res.append((nextMin[i] - prevMin[i] + 1) * h)
        
        # print(res)
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



print(
    Solution().largestRectangleArea(heights=[1,3,5,4,6,7,2])
)

print(
    Solution().largestRectangleArea(heights=[2,1,5,6,2,3])
)

print(
    Solution().largestRectangleArea(heights=[4,2,0,3,2,4,3,4])
)

