from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while j < len(popped) and stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack

print(Solution().validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))
