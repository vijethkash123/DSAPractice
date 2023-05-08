class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, x):
        if(len(self.minStack)==0 or x<=self.minStack[-1]):
            self.minStack.append(x)
        self.stack.append(x)
        
    def pop(self):
        if self.stack[-1]==self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()