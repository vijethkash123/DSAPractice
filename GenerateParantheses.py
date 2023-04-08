class Solution(object):
    def generateParenthesis(self, n):
        partialSet=""
        powerSet=[]
        
        self.backtrack(n,n,2*n,partialSet,powerSet)
        return powerSet
    
    def backtrack(self,openCount,closeCount,totalLen,partialSet,powerSet):
        if len(partialSet)==totalLen:
            if self.isValid(partialSet):
                powerSet.append(partialSet)
        else:
            if openCount>0:
                partialSet=partialSet+"("
                self.backtrack(openCount-1,closeCount,totalLen,partialSet,powerSet)
                partialSet=partialSet[:-1]
                openCount+=1
            if closeCount>0:
                partialSet=partialSet+")"
                self.backtrack(openCount,closeCount-1,totalLen,partialSet,powerSet)
                partialSet=partialSet[:-1]
                closeCount+=1

    def isValid(self,partialSet):
        balance=0
        if partialSet[0]==")" or partialSet[len(partialSet)-1]=="(":
            return False

        else:
            for i in partialSet:
                if i=="(":
                    balance+=1
                elif i==")":
                    balance-=1
                if balance<0:
                    return False
            return balance==0
            
if __name__ == "__main__":
    obj=Solution()
    print(obj.generateParenthesis(3))