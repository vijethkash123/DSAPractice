class Solution(object):
    string = "aeiou"    
    powerSet=0
    def countVowelStrings(self, n):
        partialSet=""
        self.backtrack(n,0,partialSet,self.powerSet)
        return self.powerSet
    def backtrack(self,n,lastVowel,partialSet,powerSet):
        if len(partialSet)==n:
            self.powerSet+=1
        else:
            for i in range(lastVowel,len(self.string)):
                partialSet=partialSet+self.string[i]
                self.backtrack(n,i,partialSet,self.powerSet)  #We pass i itself, as we also want aa,ee,ii,oo,uu in result
                partialSet=partialSet[:-1]

if __name__ == "__main__":
    obj=Solution()
    print(obj.countVowelStrings(2))