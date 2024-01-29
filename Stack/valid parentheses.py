class Solution:
    def isValid(self, s: str) -> bool:  
        # We can use list to implement stack in python, list.pop() will pop the last added element similar to stack.pop() and list.append() will insert at the end/top of stack
        pairs = {'}':'{', ')':'(', ']':'['}
        stack = []
        if len(s)<2:
            return False
        for c in s:
            if c not in pairs.keys():
                stack.append(c)
            else:
                if len(stack)> 0 and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack # return true if list is empty else return false

obj = Solution()
print(obj.isValid(s="({[]})"))
print(obj.isValid(s="({[)}]"))
print(obj.isValid(s="(]"))
