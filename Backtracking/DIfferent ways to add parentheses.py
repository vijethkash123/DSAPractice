from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y
        }

        def backtrack(left, right):
            res = []
            for i in range(left, right + 1):
                op = expression[i]
                if op in operations:
                    nums1 = backtrack(left, i - 1)  # i - 1 as we exclude the operator
                    nums2 = backtrack(i + 1, right)  # i + 1 as we exclude the operator
                    
                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(operations[op](n1, n2))  # if we have [3], [4, 5] as left and right and op as *, we do 3*4, 3*5
            if res == []:  # base case, when res is empty we add the original number itself
                res.append(int(expression[left: right + 1]))
            return res  # returns res in both base case and also in normal case of line 18

        return backtrack(0, len(expression) - 1)

print(Solution().diffWaysToCompute("2*3-4*5"))
