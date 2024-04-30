from typing import List


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [num[0]]
        i = 1

        while i <= len(num[1:]):
            if num[i] < stack[-1]:
                while stack and num[i] < stack[-1] and k > 0:
                    stack.pop()
                    k -= 1
                stack.append(num[i])
                i+=1
            else:
                stack.append(num[i])
                i += 1
            if k == 0:
                stack.extend(num[i:])
                break
        while k:
            stack.pop(-1)
            k -= 1

        return str(int("".join([i for i in stack]))) if stack else "0"


print(Solution().removeKdigits("1432219", 3))
print(Solution().removeKdigits("10", 2))
print(Solution().removeKdigits("112", 2))
print(Solution().removeKdigits("3200330", 4))
print(Solution().removeKdigits("12345607", 2))  # use of 2nd while instead of if