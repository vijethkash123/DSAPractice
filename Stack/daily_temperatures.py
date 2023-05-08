class Solution:
    def dailyTemperatures(self, temp):
        res = [0] * len(temp)
        stack = [] # pair: [temp, index where it occured]

        for i, t in enumerate(temp):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop() # see example below
                res[stackInd] = i - stackInd
            stack.append([t,i])
        return res

obj = Solution()
print(obj.dailyTemperatures([73,74,75,71,69,72,76,73]))

'''
tes = [[0,0], [1,1]]
x, y = tes.pop()
print(x,y)  # Prints 1,1
'''